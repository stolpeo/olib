# olib

[![Build Status](https://travis-ci.org/stolpeo/olib.svg?branch=master)](https://travis-ci.org/stolpeo/olib)

## Installation

A virtual environment is recommended:

```
$ virtualenv -p python3 ~/venv
$ source ~/venv/bin/activate
```

Install:

```
$ python setup.py install
```

Run the tests:

```
$ python setup.py test
```

## Functions

```python
from olib import olib
```

### `olib.debug()`

```python
from olib import olib

@olib.debug(True)
def some_function(n):
  # do something
```
