# abi-markdowner

**`abi-markdowner`** is a Python tool that converts MultiversX Smart Contract ABI files into structured and detailed Markdown documentation. This makes it easy to document, share, understand, and interact with smart contracts.

## TL;DR

<details><summary>Expand for a quick look ⤵️</summary>

The `abi-markdowner` tool can transform the following ABI file of a MultiversX SC:

<div style="background-color: black; padding: 40px;">

```json
{
    "buildInfo": {
        "rustc": {
            "version": "1.80.1",
            "commitHash": "3f5fd8dd41153bc5fdca9427e9e05be2c767ba23",
            "commitDate": "2024-08-06",
            "channel": "Stable",
            "short": "rustc 1.80.1 (3f5fd8dd4 2024-08-06)"
        },
        "contractCrate": {
            "name": "ping-pong-egld",
            "version": "0.0.2"
        },
        "framework": {
            "name": "multiversx-sc",
            "version": "0.52.3"
        }
    },
    "docs": [
        "A contract that allows anyone to send a fixed sum, locks it for a while and then allows users to take it back.",
        "Sending funds to the contract is called \"ping\".",
        "Taking the same funds back is called \"pong\".",
        ""
    ],
    "name": "PingPong",
    "constructor": {
        "docs": [
            "Necessary configuration when deploying:",
            "`ping_amount` - the exact EGLD amounf that needs to be sent when `ping`-ing.",
            "`duration_in_seconds` - how much time (in seconds) until contract expires.",
            "`opt_activation_timestamp` - optionally specify the contract to only actvivate at a later date.",
            "`max_funds` - optional funding cap, no more funds than this can be added to the contract."
        ],
        "inputs": [
            {
                "name": "ping_amount",
                "type": "BigUint"
            },
            {
                "name": "duration_in_seconds",
                "type": "u64"
            },
            {
                "name": "opt_activation_timestamp",
                "type": "Option<u64>"
            },
            {
                "name": "max_funds",
                "type": "optional<BigUint>",
                "multi_arg": true
            }
        ],
        "outputs": []
    },
    "endpoints": [
        {
            "docs": [
                "User sends some EGLD to be locked in the contract for a period of time.",
                "Optional `_data` argument is ignored."
            ],
            "name": "ping",
            "mutability": "mutable",
            "payableInTokens": [
                "EGLD"
            ],
            "inputs": [
                {
                    "name": "_data",
                    "type": "ignore",
                    "multi_arg": true
                }
            ],
            "outputs": []
        },
                {
            "docs": [
                "Lists the addresses of all users that have `ping`-ed,",
                "in the order they have `ping`-ed"
            ],
            "name": "getUserAddresses",
            "mutability": "readonly",
            "inputs": [],
            "outputs": [
                {
                    "type": "variadic<Address>",
                    "multi_result": true
                }
            ]
        }
    ],
    "types": {
        "UserStatus": {
            "type": "enum",
            "variants": [
                {
                    "name": "New",
                    "discriminant": 0
                },
                {
                    "name": "Registered",
                    "discriminant": 1
                },
                {
                    "name": "Withdrawn",
                    "discriminant": 2
                }
            ]
        }
    }
}
```
</div>


to this Markdown file:

<div style="background-color: black; padding: 40px;">
<sub>*This file has been auto-generated using the [abi-markdowner](https://github.com/0xk0stas/abi-markdowner).*</sub>

# Smart Contract: PingPong

<details>
<summary>Documentation</summary>

A contract that allows anyone to send a fixed sum, locks it for a while and then allows users to take it back.

Sending funds to the contract is called "ping".

Taking the same funds back is called "pong".


</details>

<details>
<summary>Build info</summary>

- **Rustc Version**: 1.80.1
- **Commit Hash**: 3f5fd8dd41153bc5fdca9427e9e05be2c767ba23
- **Commit Date**: 2024-08-06
- **Channel**: Stable

- **Framework**: multiversx-sc
- **Version**: 0.52.3
</details>

<details>
<summary>Links</summary>

- **Mainnet Deployments**:
  - **[Shard 0](https://explorer.elrond.com/address/erd1qqqqqqqqqqqqqpgqvc7gdl0p4s97guh498wgz75k8sav6sjfjlwqh679jy)**: erd1qqqqqqqqqqqqqpgqvc7gdl0p4s97guh498wgz75k8sav6sjfjlwqh679jy
  - **[Shard 1](https://explorer.elrond.com/address/erd1qqqqqqqqqqqqqpgqhe8t5jewej70zupmh44jurgn29psua5l2jps3ntjj3)**: erd1qqqqqqqqqqqqqpgqhe8t5jewej70zupmh44jurgn29psua5l2jps3ntjj3
- **Devnet Deployments**:
  - **[Address](https://devnet-explorer.elrond.com/address/erd1qqqqqqqqqqqqqpgqvn9ew0wwn7a3pk053ezex98497hd4exqdg0q8v2e0c)**: erd1qqqqqqqqqqqqqpgqvn9ew0wwn7a3pk053ezex98497hd4exqdg0q8v2e0c
</details>

## Table of Contents

- [Types](#types)
- [Endpoints](#endpoints)
- [Views](#views)

## Types

<details>
<summary>UserStatus</summary>

#### Enum Variants:
- **New** (Discriminant: 0)
- **Registered** (Discriminant: 1)
- **Withdrawn** (Discriminant: 2)

</details>

## Endpoints

### Deploy

<details>
<summary>init</summary>

Necessary configuration when deploying:

`ping_amount` - the exact EGLD amounf that needs to be sent when `ping`-ing.

`duration_in_seconds` - how much time (in seconds) until contract expires.

`opt_activation_timestamp` - optionally specify the contract to only actvivate at a later date.

`max_funds` - optional funding cap, no more funds than this can be added to the contract.
#### Inputs:
| Name | Type | Optional |
| - | - | - |
| ping_amount | BigUint |  |
| duration_in_seconds | u64 |  |
| opt_activation_timestamp | u64 | ✔ |
| max_funds | BigUint | ✔ |


</details>

### Other

<details>
<summary>ping</summary>

User sends some EGLD to be locked in the contract for a period of time.

Optional `_data` argument is ignored.
#### Note: This endpoint is payable by EGLD only.

#### Inputs:
| Name | Type |
| - | - |
| _data | ignore |


</details>

## Views

<details>
<summary>getUserAddresses</summary>

Lists the addresses of all users that have `ping`-ed,

in the order they have `ping`-ed
#### Outputs:
| Type | MultiValue |
| - | - |
| Address | ✔ |


</details>


</div>

</details>

## Features

- **Convert ABI to Markdown:** Generates comprehensive Markdown documentation from smart contract ABI files.
- **Customizable Output:** Organizes endpoints, views, events, and types with formatted tables and detailed descriptions based on documentations in the contracts.
- **Matrix-Style Input/Output Tables:** Automatically formats function inputs and outputs into a clear matrix with support for optional and multi-value parameters.
- **Automatic Table of Contents:** Includes a TOC for easy navigation within the generated documentation.
- **Deployment Links:** Supports including multiple mainnet and devnet addresses with customizable labels from a `deployments.json` file.

## Installation

Install `abi-markdowner` using pip

```bash
pip install abi-markdowner
```

or pipx

```bash
pipx install abi-markdowner
```

## Usage

Simply run the tool from your SC main directory:

```bash
abi-markdowner
```

Alternatively, you can pass another project directory as argument. For more information, check the `Parameters` section.

### Parameters

- `--sc-path`:

  (Optional - default is the current working directory)

  Specify the path to your smart contract project containing the Cargo.toml and optionally the deployments.json files. The ABI file will be read from the output directory within this path.

- `--output-file`:

  (Optional - default is ABI.md in the `sc-path/output` directory)

  Specify the output file path for the generated Markdown.

- `--cargo-toml`:

  (Optional - default is Cargo.toml in the `sc-path` directory)

  Specify the path to the Cargo.toml file.

- `--deployments-json`:

  (Optional - default is deployments.json in the `sc-path` directory)

  Specify the path to the deployments.json file containing deployment addresses.

**Important**:
ABI file is obtained from the `/output` folder in the `sc-path` directory.

## Execution example

```bash
abi-markdowner --sc-path path_to_sc/
```

This will generate a Markdown document summarizing your smart contract's structure, including types, endpoints, views, and events, along with links to the specified deployment addresses.

### Example of `deployments.json` file

The existence of this file is not mandatory. If found, a `Links` section will be created in the documentation.

Here’s an example of how your deployments.json file can be structured:

```json
{
  "mainnet": [
    {
      "address": "erd1qqqqqqqqqqqqqpgqvc7gdl0p4s97guh498wgz75k8sav6sjfjlwqh679jy",
      "label": "Shard 0"
    },
    {
      "address": "erd1qqqqqqqqqqqqqpgqhe8t5jewej70zupmh44jurgn29psua5l2jps3ntjj3",
      "label": "Shard 1"
    }
  ],
  "devnet": [
    {
      "address": "erd1qqqqqqqqqqqqqpgqvn9ew0wwn7a3pk053ezex98497hd4exqdg0q8v2e0c"
    }
  ]
}
```

The above would result in something similar to the following:

```css
Links
    - Mainnet Deployments:
        - Shard 0: erd1qqqqqqqqqqqqqpgqvc7gdl0p4s97guh498wgz75k8sav6sjfjlwqh679jy
        - Shard 1: erd1qqqqqqqqqqqqqpgqhe8t5jewej70zupmh44jurgn29psua5l2jps3ntjj3
    - Devnet Deployments:
        - Address: erd1qqqqqqqqqqqqqpgqvn9ew0wwn7a3pk053ezex98497hd4exqdg0q8v2e0c
```

## Tests

Tests have not been added yet.

## License

`abi-markdowner` is licensed under the MIT License. See the LICENSE file for more information.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.
