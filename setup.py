from distutils.core import setup
from setuptools import find_packages

setup(
    name='django-crosssubdomain',
    version='0.1.1',
    author='Colin Barnwell',
    packages=find_packages(),
    package_data={},
    scripts=[],
    description='A small Django application for providing templates with a document.domain setting for cross-subdomain JS',
    long_description=open('README.md').read(),
    install_requires=[
        "Django >= 1.4"
    ],
)
