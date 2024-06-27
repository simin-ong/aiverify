
[![Integration Tests](https://github.com/aiverify-foundation/aiverify/actions/workflows/integration-tests.yml/badge.svg)](https://github.com/aiverify-foundation/aiverify/actions/workflows/integration-tests.yml)  [![Integration Tests for aiverify-user (Docker)](https://github.com/aiverify-foundation/aiverify/actions/workflows/integration-tests-docker.yml/badge.svg)](https://github.com/aiverify-foundation/aiverify/actions/workflows/integration-tests-docker.yml)

## ✨New API Connector Feature!

We're excited to introduce a powerful enhancement to AI Verify – the API Connector feature! 
Now, instead of uploading your AI Model file onto AI Verify, you can seamlessly configure an API Connection to your model server. 
Learn more about the modes of accessing AI models [here](https://aiverify-foundation.github.io/aiverify/getting-started/accessing-ai-model/)

### Key Advantages:
- Bypass Size Limitations: Say goodbye to the constraints imposed by browser upload size limits.
- Test previously unsupported AI frameworks: The API Connector empowers you to work with models of any framework, such as PyTorch. Learn more about compatibility of model uploads [here](https://aiverify-foundation.github.io/aiverify/others/compatibility/).
- Connection Settings for Batch Requests: Optimise your test runs by configuring connection timeouts, connection retries, max connections, rate limit and rate limit timeouts.
* Important Note: This feature currently supports tabular data only.

### Getting Started:
To take advantage of this feature, refer to our [How-To Guide](https://aiverify-foundation.github.io/aiverify/how-to/connect-to-ai-model-api/). This guide provides step-by-step instructions on setting up the API Connector for seamless integration with your model server.

We are excited to have you try it out and hear what you think about this feature!
[Discussion Board](https://github.com/aiverify-foundation/aiverify/discussions)

## Introduction

Welcome to AI Verify! AI Verify is launched under the [AI Verify Foundation](https://aiverifyfoundation.sg/?utm_source=Github&utm_medium=referral&utm_campaign=20230607_AI_Verify_Foundation_GitHub), a subsidiary under the IMDA.

[AI Verify](https://aiverifyfoundation.sg/what-is-ai-verify/?utm_source=Github&utm_medium=referral&utm_campaign=20230607_AI_Verify_GitHub) is an AI governance testing framework and software toolkit that validates the performance of AI systems against a set of internationally recognised principles through standardised tests. AI Verify is consistent with international AI governance frameworks such as those from European Union, OECD and Singapore.

It is a single integrated toolkit that operates within an enterprise environment. It can perform technical tests on common supervised learning classification and regression models for most tabular and image datasets. It however does not define AI ethical standards and does not guarantee that any AI system tested will be free from risks or biases or is completely safe.

This document provides important notices and information about the project that contributors and users should be aware of. Please take the time to read through this document thoroughly. 

## Installing AI Verify

New to AI Verify? Generally, you should install AI Verify by building and running the [Dockerfile](https://aiverify-foundation.github.io/aiverify/getting-started/docker-setup/), which contains all the dependencies you need. This should get you ready to use AI Verify! See the installation guide for building and running from [source code](https://aiverify-foundation.github.io/aiverify/getting-started/source-code-setup/) if you wish to deal with dependencies on your own. 

## User Guide

Learn how you may utilise AI Verify effectively [here](https://aiverify-foundation.github.io/aiverify).

## Developer Guide

Learn how you can utilise the developer tools effectively to contribute to the project [here](https://aiverify-foundation.github.io/aiverify-developer-tools/getting_started/start_here/).

## Contributing Guidelines

We encourage contributions from the community to help improve this project. Before contributing, please read our [Contributing Guidelines](https://github.com/aiverify-foundation/aiverify-developer-tools/blob/main/CONTRIBUTING.md) to understand the process and expectations.

## Issue Tracker

Found a bug or have a feature request? Please report it on our issue tracker. We appreciate your feedback and contributions to making this project better. Make sure to adhere to the designated format as provided in the contributing guidelines.

## Documentation

Comprehensive documentation is available for your reference. It includes installation and setup instructions, user guides, and other relevant information. Please refer to the documentation before opening an issue or asking for support.

## License

This project is released under the Apache 2.0 license, which can be found under the project's license file. By contributing to this project, you agree to release your contributions under the same license. Please ensure that you are familiar with the license terms. You may find a list of the licenses used by dependencies and any other material used by this project there too.

## Support

If you have any questions or need assistance, please check the project discussions or issue tracker for existing threads. If you cannot find a resolution, feel free to create a new discussion or issue, or head over to our [contact page](https://aiverifyfoundation.sg/contact-us/?utm_source=Github&utm_medium=referral&utm_campaign=20230607_Queries_from_GitHub) if you require assistance.

Thank you for your interest in AI Verify, and we look forward to your contributions!

## Notice

```
AI Verify
Copyright 2024 AI Verify Foundation

This product includes software developed under the AI Verify Foundation.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
