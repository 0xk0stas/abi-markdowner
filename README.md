# abi-markdowner

**`abi-markdowner`** is a Python tool that converts MultiversX Smart Contract ABI files into structured and detailed Markdown documentation. This makes it easy to document, share, understand, and interact with smart contracts.

## TL;DR


Discover how `abi-markdowner` effortlessly transforms complex and cumbersome *abi.json* files into clear, structured documentation. Check out these examples:

- The simple yet illustrative [Ping-Pong SC](https://github.com/0xk0stas/abi-markdowner/blob/main/examples/ping-pong-egld/output/ABI.md).
- The more advanced [Hatom Liquid Staking SC](https://github.com/0xk0stas/abi-markdowner/blob/main/examples/hatom-liquid-staking-release/liquid-staking/output/ABI.md).


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
