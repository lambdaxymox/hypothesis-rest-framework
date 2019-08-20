import sys
import setuptools
import os

from setuptools import setup
from setuptools.command.test import test as TestCommand


config = dict(
    description = 'Extension of Hypothesis testing framework to integrate property tests into Django Rest Framework.',
    author = 'LambdaXymox',
    url = 'https://github.com/lambdaxymox/hypothesis-rest-framework',
    download_url = 'https://github.com/lambdaxymox/hypothesis-rest-framework.git',
    author_email = 'lambda.xymox@gmail.com',
    version = '0.1',
    install_requires = ['hypothesis', 'hypothesis[django]', 'djangorestframework'],
    license = "LICENSE-APACHE",
    package_dir = {'': 'src'},
    packages = ['hypothesis_rest_framework'],
    scripts = [],
    name = 'hypothesis_rest_framework',
)

setup(**config)

