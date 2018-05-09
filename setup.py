import sys
import setuptools
import os

from setuptools import setup
from setuptools.command.test import test as TestCommand

TAR_FILE = os.path.join('tarballs', 'sample.tar.gz')
SAMPLE_ROOT = 'sample'


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to pytest")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = ''

    def run_tests(self):
        import shlex
        # Import here, because imports outside the eggs aren't loaded.
        import pytest
        errno = pytest.main(shlex.split(self.pytest_args))
        sys.exit(errno)


config = dict(
    description = 'Extension to Django Rest Framework to incorporate Hypothesis property tests.',
    author = 'Stallmanifold',
    url = 'https://github.com/stallmanifold/hypothesis-rest-framework',
    download_url = 'https://github.com/stallmanifold/hypothesis-rest-framework.git',
    author_email = 'stallmanifold@gmail.com',
    version = '0.1',
    install_requires = ['hypothesis'],
    license = "LICENSE-APACHE",
    package_dir = {'': 'src'},
    packages = [''],
    scripts = [],
    name = 'bookworm',
    tests_require = ['hypothesis'],
    cmdclass = {
        'test': PyTest,
    },
)

setup(**config)

