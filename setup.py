#!/usr/bin/env python

import os.path
from setuptools import setup, find_packages


here = os.path.realpath(os.path.dirname(__file__))

setup(
    name='slackup',
    version='0.0',
    description='A tool for uploading files to Slack from the command line.',
    author='Rock Kitchen Harris',
    packages=find_packages(here),
    scripts=[
        os.path.join('slackup', 'slackup'),
    ],
    install_requires=[
        'slacker',
    ],
)
