#!/usr/bin/env python
import os
import sys
from setuptools import setup, find_packages

repo_base_dir = os.path.abspath(os.path.dirname(__file__))
# pull in the packages metadata
package_about = {}
with open(os.path.join(repo_base_dir, "include", "__about__.py")) as about_file:
    exec(about_file.read(), package_about)


with open(os.path.join(repo_base_dir, 'README.rst'), 'r') as README:
    long_description = README.read()

if __name__ == '__main__':
    setup(
        name=package_about['__title__'],
        version=package_about['__version__'],
        description=package_about['__summary__'],
        long_description=long_description.strip(),
        author=package_about['__author__'],
        author_email=package_about['__email__'],
        url=package_about['__url__'],
        packages=find_packages(),
        # dependencies
        install_requires=[],
        # metadata for package search
        license='MIT',
        # https://pypi.python.org/pypi?%3Aaction=list_classifiers
        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'Intended Audience :: System Administrators',
            'Topic :: System :: Monitoring',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
        ],
        keywords='import include eval exec pickle multiprocess',
        # unit tests
        test_suite='test_include',
        # use unittest backport to have subTest etc.
        tests_require=['unittest2'] if sys.version_info < (3, 4) else [],
    )
