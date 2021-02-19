# NLP Sandbox Date Annotator Stub

<!-- [![GitHub Release](https://img.shields.io/github/release/nlpsandbox/date-annotator-stub.svg?include_prereleases&color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/nlpsandbox/date-annotator-stub/releases) -->
[![GitHub CI](https://img.shields.io/github/workflow/status/nlpsandbox/date-annotator-stub/ci.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/nlpsandbox/date-annotator-stub/actions)
[![GitHub License](https://img.shields.io/github/license/nlpsandbox/date-annotator-stub.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/nlpsandbox/date-annotator-stub/blob/develop/LICENSE)
[![Docker Pulls](https://img.shields.io/docker/pulls/nlpsandbox/date-annotator-stub.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/r/nlpsandbox/date-annotator-stub)
[![Discord](https://img.shields.io/discord/770484164393828373.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=Discord&logo=discord)](https://discord.gg/Zb4ymtF "Realtime support / chat with the community and the team")

Python-Flask stub for the [NLP Sandbox Date Annotator API]

## Overview

This repository contains a Python-Flask stub for the [NLP Sandbox Date Annotator
API]. A Date Annotator takes as input a clinical note and outputs a list of
predicted date annotations found in the clinical note.

The stub available in the folder [server](server/) has been generated from the
OpenAPI specification of the NLP Sandbox Date Annotator API
([openapi.json](openapi.json)) using the [OpenAPI generator] -- just don't
expect much from it as this API service will return the string "do some magic!"
to all the requests it receives!

> **Important**: The Docker image built using the CI/CD workflow of this
repository is used as part of the documentation of the [nlpsandbox.io]. Please
visit this website for more information and actual example implementations of
this annotator.

### Specification

- Date Annotator API version: 1.0.0
- Docker image: [nlpsandbox/date-annotator-stub]

## Usage

### Requirements

- [Node JS](https://nodejs.org/)
- Java (required by [OpenAPITools/openapi-generator])

### Generating this stub

The file [package.json](package.json) defines the version of the OpenAPI
generator to use and provides an utility function to run the generator.

Install the generator:

    npm ci

(Re-)generate the content of the folder *server/* based on the latest OpenAPI
specification of the [NLP Sandbox Date Annotator API]:

    npm run generate:server

### Running with Docker

This command will start this API service stub:

    docker-compose up --build

The web interface of this API service will be available at
http://localhost:8080/api/v1/ui.

## License

[Apache License 2.0]

<!-- Links -->

[NLP Sandbox Date Annotator API]: https://nlpsandbox.github.io/nlpsandbox-schemas/date-annotator/latest/docs/
[nlpsandbox.io]: https://nlpsandbox.io
[nlpsandbox/nlpsandbox-schemas]: https://github.com/nlpsandbox/nlpsandbox-schemas
[Apache License 2.0]: https://github.com/nlpsandbox/date-annotator-stub/blob/develop/LICENSE
[OpenAPI Generator]: https://github.com/OpenAPITools/openapi-generator
[OpenAPITools/openapi-generator]: https://github.com/OpenAPITools/openapi-generator
[nlpsandbox/date-annotator-stub]: https://hub.docker.com/r/nlpsandbox/date-annotator-stub
