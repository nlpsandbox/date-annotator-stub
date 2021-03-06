# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "openapi_server"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion>=2.0.2",
    "swagger-ui-bundle>=0.0.2",
    "python_dateutil>=2.6.0"
]

setup(
    name=NAME,
    version=VERSION,
    description="NLP Sandbox Date Annotator API",
    author_email="thomas.schaffter@sagebionetworks.org",
    url="",
    keywords=["OpenAPI", "NLP Sandbox Date Annotator API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    # Overview  This NLP tool detects references of dates in the clinical note given as input and returns a list of date annotations.  # Examples  - [NLP Sandbox Date Annotator (Python)](https://github.com/nlpsandbox/date-annotator-example) - [NLP Sandbox Date Annotator (Java)](https://github.com/nlpsandbox/date-annotator-example-java) 
    """
)

