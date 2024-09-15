<sub>*This file has been auto-generated using the [abi-markdowner](https://github.com/0xk0stas/abi-markdowner).*</sub>

# Smart Contract: PingPong

<details>
<summary>Documentation</summary>

A contract that allows anyone to send a fixed sum, locks it for a while and then allows users to take it back.

Sending funds to the contract is called "ping".

Taking the same funds back is called "pong".



Restrictions:

- `ping` can be called only after the contract is activated. By default the contract is activated on deploy.

- Users can only `ping` once, ever.

- Only the set amount can be `ping`-ed, no more, no less.

- The contract can optionally have a maximum cap. No more users can `ping` after the cap has been reached.

- The `ping` endpoint optionally accepts

- `pong` can only be called after the contract expired (a certain duration has passed since activation).

- `pongAll` can be used to send to all users to `ping`-ed. If it runs low on gas, it will interrupt itself.

It can be continued anytime.
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
<summary>OperationCompletionStatus</summary>

</details>

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

<details>
<summary>pong</summary>

User can take back funds from the contract.

Can only be called after expiration.

</details>

<details>
<summary>pongAll</summary>

Send back funds to all users who pinged.

Returns

- `completed` if everything finished

- `interrupted` if run out of gas midway.

Can only be called after expiration.
#### Outputs:
| Type |
| - |
| OperationCompletionStatus |


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

<details>
<summary>getPingAmount</summary>

#### Outputs:
| Type |
| - |
| BigUint |


</details>

<details>
<summary>getDeadline</summary>

#### Outputs:
| Type |
| - |
| u64 |


</details>

<details>
<summary>getActivationTimestamp</summary>

Block timestamp of the block where the contract got activated.

If not specified in the constructor it is the the deploy block timestamp.
#### Outputs:
| Type |
| - |
| u64 |


</details>

<details>
<summary>getMaxFunds</summary>

Optional funding cap.
#### Outputs:
| Type | Optional |
| - | - |
| BigUint | ✔ |


</details>

<details>
<summary>getUserStatus</summary>

State of user funds.

0 - user unknown, never `ping`-ed

1 - `ping`-ed

2 - `pong`-ed
#### Inputs:
| Name | Type |
| - | - |
| user_id | u32 |

#### Outputs:
| Type |
| - |
| UserStatus |


</details>

<details>
<summary>pongAllLastUser</summary>

Part of the `pongAll` status, the last user to be processed.

0 if never called `pongAll` or `pongAll` completed..
#### Outputs:
| Type |
| - |
| u32 |


</details>

