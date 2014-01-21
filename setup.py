# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages

setup(
    name='oculus',
    version='0.2.0',
    author=u'Twined',
    author_email='www.twined.net',
    packages=find_packages(),
    include_package_data=True,
    url='http://github.com/twined/oculus',
    license='Do what thou wilt.',
    description='Google Analytics integration for Twined apps',
    long_description=open('README.md').read(),
    zip_safe=False,
)
