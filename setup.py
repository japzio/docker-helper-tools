#!/usr/bin/env python3 

from setuptools import setup, find_packages

setup(
    name='ecr2ecr',
    version='1.9',
    author='Jasper Culong',
    author_email='jculongit10@yahoo.com',
    packages=find_packages(),
    license='LICENSE',
    description='AWS ECR docker image cross-region replicator',
    long_description=open('README.md').read(),
    url="https://pypi.org/project/ecr2ecr",
    entry_points={
        'console_scripts': [
            'ecr2ecr = ecr2ecr.core:main'
        ]
    },
    install_requires=[
        "docker-py <= 1.10.6",
        "boto3 >= 1.7.57",
        "twine == 1.13.0",
        "unittest2"
    ],
)