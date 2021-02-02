# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in costlow/__init__.py
from costlow import __version__ as version

setup(
	name='costlow',
	version=version,
	description='App for Costlow Co. Ltd',
	author='Sione Taumoepeau',
	author_email='sione.taumoepeau@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
