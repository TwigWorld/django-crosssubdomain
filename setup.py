from distutils.core import setup
from setuptools import find_packages

setup(
    name="django-crosssubdomain",
    version="1.0.0",
    author="Colin Barnwell",
    packages=find_packages(),
    package_data={},
    scripts=[],
    description="A small Django application for providing templates with a document.domain setting for cross-subdomain JS",
    long_description=open("README.md").read(),
    install_requires=["Django<3"],
    extras_require={"testing": ["pytest", "pytest-django", "black", ]},
)
