import sys
from setuptools import setup
import pytest


with open('requirements.txt') as reqs_file:
    reqs = reqs_file.read().splitlines()


setup(name='olib',
      version='0.1.0',
      description='olivers lib',
      author='Oliver Stolpe',
      author_email='oliver.stolpe@bihealth.de',
      packages=['olib'],
      package_dir={'olib': 'olib'},
      include_package_data=True,
      license='MIT',
      zip_safe=False,
      test_suite='tests',
      tests_require=reqs,
      setup_requires=['pytest-runner'])
