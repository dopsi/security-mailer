security-mailer
===============

security-mailer is a utility to send a security digest email about the system.

Installation
------------

There is a [AUR package available](https://aur.archlinux.org/packages/security-mailer),
as well as one for the
[development version](https://aur.archlinux.org/packages/security-mailer-git).

Configuration
-------------

The configuration is read, in this order, from :

* `./config.json`
* `$HOME/.config/security-mailer/config.json`
* `/etc/security-mailer/config.json`

Once the first configuration file is read, the reading stops and the program
continues.

Versionning
-----------

this project follows the semantic versionning guidelines provided at
[semver.org](http://semver.org/) with versions numbered as 
`major.minor.revision` :

* `major` is increased after a backwards incompatible api change.
* `minor` is increased after a backwards compatible api change.
* `revision` is increased after a change with no effect on the api.

any version with `major` being 0 *should* not be considered stable nor
should its api.

Versions history can be found in the file ChangeLog.md

License
-------

> The MIT License (MIT)
> 
> Copyright (c) 2016 Simon Doppler <dopsi@member.fsf.org>
> 
> Permission is hereby granted, free of charge, to any person obtaining a copy
> of this software and associated documentation files (the "Software"), to deal
> in the Software without restriction, including without limitation the rights
> to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
> copies of the Software, and to permit persons to whom the Software is
> furnished to do so, subject to the following conditions:
> 
> The above copyright notice and this permission notice shall be included in all
> copies or substantial portions of the Software.
> 
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
> FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
> AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
> LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
> OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
> SOFTWARE.

Author
------

Copyright 2016 Simon Doppler <dopsi@member.fsf.org>
