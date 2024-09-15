<sub>*This file has been auto-generated using the [abi-markdowner](https://github.com/0xk0stas/abi-markdowner).*</sub>

# Smart Contract: Adder

<details>
<summary>Documentation</summary>

One of the simplest smart contracts possible,

it holds a single variable in storage, which anyone can increment.
</details>

<details>
<summary>Build info</summary>

- **Rustc Version**: 1.79.0
- **Commit Hash**: 129f3b9964af4d4a709d1383930ade12dfe7c081
- **Commit Date**: 2024-06-10
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

- [Endpoints](#endpoints)
- [Views](#views)
## Endpoints

### Deployment - Upgrade

<details>
<summary>init</summary>

#### Inputs:
| Type | Optional | List | MultiValue | Raw Type |
| - | - | - | - | - |
| BigUint |  |  |  |  |

</details>

<details>
<summary>upgrade</summary>

#### Inputs:
| Type | Optional | List | MultiValue | Raw Type |
| - | - | - | - | - |
| BigUint |  |  |  |  |

</details>

### Other

<details>
<summary>add</summary>

Add desired amount to the storage variable.
#### Inputs:
| Name | Type | Optional | List | MultiValue | Raw Type |
| - | - | - | - | - | - |
| value | BigUint |  |  |  |  |


</details>

## Views

<details>
<summary>getSum</summary>

#### Outputs:
| Type | Optional | List | MultiValue | Raw Type |
| - | - | - | - | - |
| BigUint |  |  |  |  |


</details>

