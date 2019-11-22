#!/usr/bin/env python3

from setuptools import setup, find_packages

with open('requirements.txt', 'r') as reqs:
	requirements = reqs.readlines()

setup(name='wiretap',
	version='1.0',
	description='watch all your users',
	author='Philip Bove',
	install_requires=requirements,
	author_email='phil@bove.online',
	packages=find_packages(),
	scripts=['bin/wiretap-bot.py']
)
