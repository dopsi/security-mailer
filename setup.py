from distutils.core import setup

setup(name='security-mailer',
    version='1.0.0',
    scripts=['scripts/security-mailer'],
    data_files=[
        ('lib/systemd/system',
        ['systemd/security-mailer.timer','systemd/security-mailer.service'])
    ]
)
