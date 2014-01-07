OCULUS
======

**NOTE: This is tailored for the twined project structure, it probably won't work too well without customization on other project bootstraps.**

Installation:
-------------

    pip install -e git://github.com/twined/oculus.git#egg=oculus-dev

Add `oculus` to `INSTALLED_APPS` in your `conf/settings.py`

    # oculus settings.py vars

    GOOGLE_ANALYTICS_LOGIN = 'your@google.login.com'
    GOOGLE_ANALYTICS_PASSWORD = 'yourgooglepass'
    GOOGLE_ANALYTICS_APP_NAME = 'yourappname'
    GOOGLE_ANALYTICS_TABLE_ID = 'yourtableid'


Usage:
------

**Oculus** plugs in automatically to the twined admin application. Just add to `INSTALLED_APPS` and it will be auto discovered