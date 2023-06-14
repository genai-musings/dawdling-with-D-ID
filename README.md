# dawdling-with-D-ID [![License: MPL 2.0](https://img.shields.io/badge/License-MPL%202.0-brightgreen.svg)](https://opensource.org/licenses/MPL-2.0)

Repository for dawdling with D-ID Studio.

 This repository contains Python code, and associated unit tests, which uses the D-ID Studio API to retrieve animations from an account.

## To run program

Your D-ID key needs to be passed to program via an environment variable

```shell
export DID_KEY="Your DID Api key"
python main.py
```

To generate an D-ID key browse to [D-ID API Keys](https://studio.d-id.com/account-settings) and select "Generate key".

## Credits

You can generate animations using a trial account at [D-ID Studio](https://studio.d-id.com/). To generate images you need credits, after the trial period expires you will need to purchase [D-ID Studio Credits](https://www.d-id.com/pricing/).

## To run unit tests

```shell
pytest
```

## D-ID Studio API Reference

For more information on the API available see the [D-ID Studio API Reference Documentation](https://docs.d-id.com/reference/get-started).

