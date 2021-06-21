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
    author_email="team@nlpsandbox.io",
    url="",
    keywords=["OpenAPI", "NLP Sandbox Date Annotator API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    # Introduction A date annotator takes as input a clinical note and outputs a list of predicted date annotations found in the clinical note. This OpenAPI document describes the specification of the NLP Sandbox Date Annotator API. This specification includes the schemas of the input and output data, and the requirements that this annotator must meet if you want to benchmark its performance on [nlpsandbox.io](https://nlpsandbox.io). # Getting Started The GitHub repository [nlpsandbox/date-annotator-example](https://github.com/nlpsandbox/date-annotator-example) provides an example implementation of the NLP Sandbox Date Annotator API in Python-Flask. By the end of the tutorial available in the README, you will have built a Docker image for this NLP Sandbox tool. You will then be able to submit this image to [nlpsandbox.io](https://nlpsandbox.io) to benchmark its performance. # Benchmarking Requirements Your NLP Sandbox tool must meet the following requirements before evaluating its performance on [nlpsandbox.io](https://nlpsandbox.io). - The endpoint &#x60;/&#x60; must redirect to &#x60;/api/v1/tool&#x60;. - The endpoint &#x60;/ui&#x60; must redirect to the Swagger User Interface (UI). - The output of this tool must be reproducible: a given input should always   generate the same output.  - To ensure the results are reproducible and robust, and the data are   secured, this tool must not connect to any remote server. When benchmarked   on [nlpsandbox.io](https://nlpsandbox.io), this tool will not be able to   connect to remote servers.  # Examples - [NLP Sandbox Date Annotator Example (Python)](https://github.com/nlpsandbox/date-annotator-example) - [NLP Sandbox Date Annotator Example (Java)](https://github.com/nlpsandbox/date-annotator-example-java) 
    """
)

