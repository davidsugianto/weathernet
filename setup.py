#!/usr/bin/env python
from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [
    'Click>=7.0',
]

setup(
    name='jcli',
    version='0.1',
    description='',
    long_description=readme,
    author='David Sugianto',
    author_email='idiots718@gmail.com',
    url='https://github.com/davidsugianto/jcli.git',
    packages=find_packages(include=['jcli']),
    entry_points={
        'console_script': [
            'jcli=jcli:cli'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='jcli',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ]
)