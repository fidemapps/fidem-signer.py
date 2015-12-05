
# Fidem Signer (Python)

The Fidem Signer is used to generate signed headers, which are injected to requests made to Fidem servers.

Transliterated to Python by [Francis Roch](http://www.linkedin.com/profile/view?id=8546024).

[Original Javascript tool](https://github.com/fidemapps/fidem-signer) by [Sebastien Guimont](https://ca.linkedin.com/in/sebastienguimont) et al.

The Fidem API is [Swagger-1.2](https://demo-api.fidem360.com/api-docs/) compliant.

## Quick start

* Clone the repo: `git clone git@bitbucket.org:mightycast/fidem-signer.py.git`.
* Get in there: `cd /this/repo/root/`
* install virtualenv: `pip install virtualenv`
* init a virtualenv at repo root: `virtualenv venv`
* activate the virtualenv to contain dependencies: `source venv/bin/activate`
* install requirements to venv: `pip install -r requirements.txt`

## Unit Tests

* Run all the tests: `nosetests test.py --logging-level=ERROR`

## Copyright and License

© Copyright 2015 Fidem Solutions, inc. 

This file is subject to the terms and conditions defined in file 'LICENSE.md', 
which is part of this source code package.
