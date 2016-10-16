#! /usr/bin/env python3

from subprocess import run,PIPE

import itertools
from datetime import datetime
import json
import sys
import smtplib
import string

def printable_clean(s):
    rval = ''

    for x in s:
        if x in string.printable:
            rval += x
        else:
            rval += '-'
    return rval

def sort_uniq(sequence, forbidden=[]):
    return (x[0] for x in itertools.groupby(sorted(sequence)) if x[0] not in forbidden)

def gen_msg(config):
    proc_all_pkg = run(['arch-audit','-q'], stdout=PIPE)
    proc_up_pkg = run(['arch-audit','-q', '-u'], stdout=PIPE)
    
    packages_all = proc_all_pkg.stdout.decode('utf8').split('\n')
    packages_all = list(sort_uniq(packages_all, ['']))
    packages_up = proc_up_pkg.stdout.decode('utf8').split('\n')
    packages_up = list(sort_uniq(packages_up, ['']))

    dt_value = datetime.utcnow().strftime("%F %T UTC")
    message = "From: {}\n".format(config['mailer']['from'])
    message += "To: {}\n".format(config['mailer']['to'])
    message += "Subject: System security digest {}\n\n".format(dt_value)
    message += "This is an automated vulnerability summary email.\n"
    message += "It was generated on {}.".format(dt_value)

    message += '\n\n'
    message += 'There are '+str(len(packages_all))
    message += ' vulnerable packages, '+str(len(packages_up))
    message += ' of which are upgradable.\n'

    if len(packages_up):
        message += '\n# Vulnerable and upgradable packages\n\n'

        for i in packages_up:
            message += '* '+i+'\n'

    if (len(packages_all)):
        message += '\n'
        message += '# Vulnerable packages\n\n'

        for i in packages_all:
            message += '* '+i+'\n'

        message += '\n# Dependency trees for all packages\n\n'

        for i in packages_all:
            proc_pkg = run(['pactree','-r',i], stdout=PIPE)
            message += printable_clean(proc_pkg.stdout.decode('utf8'))
            message += '\n'

    return message

def load_config():
    config_files = ['config.json',
            '$HOME/.config/security-mailer/config.json',
            '/etc/security-mailer/config.json']

    for i in config_files:
        try:
            with open(i) as config_file:
                config = json.load(config_file)
        except FileNotFoundError:
            pass
        else:
            return config

    sys.exit(1)

def mailer():
    config = load_config()

    # Prepare actual message

    content = gen_msg(config).encode('ascii', 'replace')

    # Send the mail

    server = smtplib.SMTP(host=config['mailer']['server']['hostname'], port=config['mailer']['server']['port'])
    server.sendmail(config['mailer']['from'], [config['mailer']['to']], content)
    server.quit()

if __name__ == '__main__':
    mailer()

