import sys
from setuptools import setup
import pytest

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
      tests_require=['pytest', 'pytest-pep8', 'pytest-cov'],
      setup_requires=['pytest-runner'])
