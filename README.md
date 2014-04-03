Django-Hei!
==========

Hides technical info on Django error page when DEBUG=True, while still lets you
quickly access it.
This saves your customer from scary error messages while let's you debug the
app.
Useful for demonstration before release. Don't use on production!

Installation
------------

1. Install application:
`pip install -e git://github.com/semargal/django-cms.git@placeholder_by_lang#egg=django-hei`
2. Add application to INSTALLED_APPS

Configuration
-------------

The feature is activated by default. Set `HIDE_TECHNICAL_ERROR_INFO=True` in
your local settings to disable it.

Usage
-----

Just press 'e' when you want to dive into detailed error info.
