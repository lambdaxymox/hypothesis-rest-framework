# Hypothesis Rest Framework
**Hypothesis Rest Framework** is an extension library for the `hypothesis` property testing library. Its purpose is to simplify writing REST API tests with the Django Rest Framework.

## Installation
The main way to install this package is from source.

### Installation From Source
[Fork](https://github.com/stallmanifold/hypothesis-rest-framework) the Hypothesis Rest Framework code, enter the source tree, and then enter
```bash
python setup.py sdist
python setup.py install --user
```
Alternatively, you can install it directly into your Django project virtual environment.
```bash
cd /path/to/your/django/project/
python setup.py sdist
python setup.py install --user
```
This will install the package into your virtual environment, assuming your project has one. Alternatively, you can install it directly using pip.
```bash
pip install git+https://github.com/stallmanifold/hypothesis-rest-framework.git
```

### Installation From PyPI
This is currently not available.

### Uninstallation
If you no longer want to use `hypothesis-rest-framework`, you can remove it with pip.
```bash
pip remove hypothesis-rest-framework
```

## Usage
To integrate the package into your project, include the line
```
hypothesis_rest_framework
```
in your requirements file.