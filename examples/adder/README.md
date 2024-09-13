<sub>*This file has been auto-generated using the [AbiMarkdowner](https://github.com/0xk0stas/AbiMarkdowner).*</sub>

# Smart Contract: Adder

One of the simplest smart contracts possible,

it holds a single variable in storage, which anyone can increment.
<details>
<summary><b>`Build info`</b></summary>

- **Rustc Version**: 1.79.0
- **Commit Hash**: 129f3b9964af4d4a709d1383930ade12dfe7c081
- **Commit Date**: 2024-06-10
- **Channel**: Stable

- **Framework**: multiversx-sc
- **Version**: 0.52.3
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

