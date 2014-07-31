#!/usr/bin/env python

import os
import sys

try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup

if sys.argv[-1] == 'publish':
  os.system('python setup.py sdist upload')
  sys.exit()

setup(
  name="anidb",
  version="0.0.1",
  description="AniDB API wrapper",
  long_description="",
  url="https://github.com/iamale/anidb.py",
  author="Ale",
  author_email="ale@incrowd.ws",
  packages=['anidb'],
  package_dir={'anidb': 'anidb'},
  install_requires=["requests==2.3.0", "beautifulsoup4==4.3.2"],
  license='MIT',
  classifiers=(
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Developers',
    'Natural Language :: English',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7'
  ),
)
