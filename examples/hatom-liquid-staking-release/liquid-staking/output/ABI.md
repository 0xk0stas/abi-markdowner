<sub>*This file has been auto-generated using the [abi-markdowner](https://github.com/0xk0stas/abi-markdowner).*</sub>

# Smart Contract: LiquidStaking

<details>
<summary>Build info</summary>

- **Rustc Version**: 1.76.0-nightly
- **Commit Hash**: d86d65bbc19b928387f68427fcc3a0da498d8a19
- **Commit Date**: 2023-12-10
- **Channel**: Nightly

- **Framework**: multiversx-sc
- **Version**: 0.47.8
</details>

## Table of Contents

- [Types](#types)
- [Endpoints](#endpoints)
- [Views](#views)
- [Events](#events)

## Types

<details>
<summary>DelegationContractData</summary>

#### Struct Fields:
| Name | Type | Optional |
| - | - | - |
| contract | Address |  |
| total_value_locked | BigUint |  |
| cap | BigUint | ✔ |
| nr_nodes | u64 |  |
| apr | BigUint |  |
| service_fee | BigUint |  |
| delegation_score | BigUint |  |
| pending_to_delegate | BigUint |  |
| total_delegated | BigUint |  |
| pending_to_undelegate | BigUint |  |
| total_undelegated | BigUint |  |
| total_withdrawable | BigUint |  |
| outdated | bool |  |
| blacklisted | bool |  |

</details>

<details>
<summary>DelegationScoreMethod</summary>

#### Enum Variants:
- **Tvl** (Discriminant: 0)
- **Apr** (Discriminant: 1)
- **Mixed** (Discriminant: 2)

</details>

<details>
<summary>DelegationScoreModel</summary>

#### Struct Fields:
| Name | Type |
| - | - |
| method | DelegationScoreMethod |
| min_tvl | BigUint |
| max_tvl | BigUint |
| min_apr | BigUint |
| max_apr | BigUint |
| omega | BigUint |

</details>

<details>
<summary>EsdtTokenPayment</summary>

#### Struct Fields:
| Name | Type |
| - | - |
| token_identifier | TokenIdentifier |
| token_nonce | u64 |
| amount | BigUint |

</details>

<details>
<summary>Penalty</summary>

#### Struct Fields:
| Name | Type |
| - | - |
| id | u64 |
| withdrawn | bool |
| attributes | UndelegateAttributes |

</details>

<details>
<summary>PenaltySource</summary>

#### Enum Variants:
- **FromUndelegate** (Discriminant: 0)
- **FromPendingToDelegate** (Discriminant: 1)

</details>

<details>
<summary>SamplingModel</summary>

#### Struct Fields:
| Name | Type |
| - | - |
| tolerance | BigUint |
| max_service_fee | BigUint |
| premium | BigUint |

</details>

<details>
<summary>State</summary>

#### Enum Variants:
- **Inactive** (Discriminant: 0)
- **Active** (Discriminant: 1)

</details>

<details>
<summary>UndelegateAttributes</summary>

#### Struct Fields:
| Name | Type |
| - | - |
| delegation_contract | Address |
| egld_amount | BigUint |
| shares | BigUint |
| undelegate_epoch | u64 |
| unbond_epoch | u64 |

</details>

<details>
<summary>UndelegationMode</summary>

#### Enum Variants:
- **None** (Discriminant: 0)
- **Algorithm** (Discriminant: 1)
- **Open** (Discriminant: 2)

</details>

## Endpoints

### Deploy

<details>
<summary>init</summary>

Initializes the contract.



# Arguments



- `unbond_period` - the unbond period in epochs. Devnet has an unbond period of 1 epoch while Mainnet has an

  unbond period of 10 epochs

- `opt_admin` - the optional admin address


#### Inputs:
| Name | Type | Optional |
| - | - | - |
| unbond_period | u64 |  |
| opt_admin | Address | ✔ |


</details>

### Other

<details>
<summary>upgrade</summary>


</details>

<details>
<summary>setPendingAdmin</summary>

Sets the pending admin address to the given address.



# Arguments:



- `new_pending_admin` - The new pending admin address.


#### Inputs:
| Name | Type |
| - | - |
| pending_admin | Address |


</details>

<details>
<summary>acceptAdmin</summary>

Attempts to accept the pending admin, which must be set first using the `set_pending_admin` endpoint.

</details>

<details>
<summary>delegate</summary>

Allows users to stake EGLD in exchange for sEGLD. The Delegation smart contract is selected based on the current

configuration of the delegation algorithm. However, this endpoint does not automatically perform the delegation.

Instead, anyone can perform the delegation at any given point in time using the `delegatePendingAmount` public

endpoint.



# Notes



- There is a minimum amount of 1 EGLD required for delegations.

- If the caller is whitelisted, they may bypass the delegation algorithm.

- The amount of sEGLD minted depends on the current exchange rate between EGLD and sEGLD.


#### Note: This endpoint is payable by EGLD only.

#### Outputs:
| Type |
| - |
| EsdtTokenPayment |


</details>

<details>
<summary>delegatePendingAmount</summary>

Initiates the delegation of the pending amount to the specified Delegation smart contract. This endpoint

performs an asynchronous call to delegate the pending amount. It is capable of handling multiple calls, and the

execution order of their callbacks does not need to match the order of the original calls.



# Arguments



- `delegation_contract`: The Delegation smart contract to delegate to.

- `opt_egld_amount`: The optional EGLD amount to delegate. If not specified, it will delegate the entire pending

  amount.



# Notes



- This endpoint can be called by anyone.

- The EGLD amount can be smaller than the pending amount if it exceeds the capacity of the Delegation smart

  contract.

- If the delegation fails, the pending amount will be reverted, and the Delegation smart contract will be marked

  as outdated. A new attempt with a smaller EGLD amount can be made later.

- If there is pending amount that cannot be delegated, the admin can penalize the Delegation smart contract and

  delegate that amount to a different Delegation smart contract.


#### Inputs:
| Name | Type | Optional |
| - | - | - |
| delegation_contract | Address |  |
| opt_egld_amount | BigUint | ✔ |


</details>

<details>
<summary>registerLsToken</summary>

Issues the liquid staking token, namely the sEGLD token.



# Arguments



- `name` - the token name

- `ticker` - the token ticker or symbol

- `decimals` - the token decimals



# Notes



- can only be called by the admin


#### Note: This endpoint is payable by EGLD only.

#### Inputs:
| Name | Type |
| - | - |
| name | bytes |
| ticker | bytes |
| decimals | u32 |


</details>

<details>
<summary>setLsTokenRoles</summary>

Gives Mint and Burn roles for sEGLD to this contract.



</details>

<details>
<summary>registerUndelegateToken</summary>

Issues the Undelegate Nft, the token minted at undelegations as a receipt.



# Notes



- can only be called by the admin


#### Note: This endpoint is payable by EGLD only.

#### Inputs:
| Name | Type |
| - | - |
| name | bytes |
| ticker | bytes |


</details>

<details>
<summary>setUndelegateTokenRoles</summary>

Gives Mint and Burn roles for the Undelegate Nft to this contract.



</details>

<details>
<summary>setDataManager</summary>

Sets the Data Manager entitled to change the data associated to each Delegation smart contract.



# Arguments



- `new_data_manager` - the address of the new Data Manager



# Notes



- can only be called by the admin


#### Inputs:
| Name | Type |
| - | - |
| new_data_manager | Address |


</details>

<details>
<summary>setStateActive</summary>

Activates the Liquid Staking Module state. The activation can only occur iff:



- the total fee has been set

- the Liquid Staking token has been issued

- the undelegate NFT has been issued

- the delegation score model has been defined

- the data manager has been set



# Notes



- can only be called by the admin



</details>

<details>
<summary>setStateInactive</summary>

Deactivates the Liquid Staking Module state.



# Notes



- can only be called by the admin



</details>

<details>
<summary>whitelistDelegationContract</summary>

Whitelists a Staking Provider Delegation smart contract. From this point onwards, this smart contract will be

eligible as a Delegation smart contract based on the state of the delegation algorithm. This method can also be

used to whitelist a previously blacklisted Delegation smart contract.



# Arguments



- `contract` - the Delegation smart contract address

- `admin` - the address entitled to update this Delegation smart contract data

- `total_value_locked` - the liquidity locked at the Delegation smart contract

- `nr_nodes` - the number of validator nodes

- `apr` - the current APR for the validator

- `service_fee` - the service fee being charged by the validator

- `opt_cap` - the maximum amount that can be locked at the Delegation smart contract (uncapped if `None`)



# Notes



- can only be called by the admin

- it will compute a delegation score based on the current state of the delegation algorithm


#### Inputs:
| Name | Type | Optional |
| - | - | - |
| delegation_contract | Address |  |
| total_value_locked | BigUint |  |
| nr_nodes | u64 |  |
| apr | BigUint |  |
| service_fee | BigUint |  |
| opt_cap | BigUint | ✔ |


</details>

<details>
<summary>blacklistDelegationContract</summary>

Blacklists a Delegation smart contract. From this point onwards, this smart contract will not be eligible as a

Delegation smart contract through the delegation algorithm.



# Arguments



- `delegation_contract` - the Delegation smart contract address


#### Inputs:
| Name | Type |
| - | - |
| delegation_contract | Address |


</details>

<details>
<summary>changeDelegationContractParams</summary>

Updates the data for a given Staking Provider Delegation smart contract.



# Arguments



- `contract` - the Delegation smart contract address

- `admin` - the address entitled to update this Delegation smart contract data

- `total_value_locked` - the liquidity locked at the Delegation smart contract

- `nr_nodes` - the number of validator nodes

- `apr` - the current APR for the validator

- `service_fee` - the service fee being charged by the validator

- `opt_cap` - the maximum amount that can be locked at the Delegation smart contract (uncapped if `None`)



# Notes



- can only be called by the admin set for the Delegation smart contract data

- will revert if the contract has been blacklisted

- it will compute a delegation score based on the current state of the delegation algorithm


#### Inputs:
| Name | Type | Optional |
| - | - | - |
| delegation_contract | Address |  |
| total_value_locked | BigUint |  |
| nr_nodes | u64 |  |
| apr | BigUint |  |
| service_fee | BigUint |  |
| opt_cap | BigUint | ✔ |


</details>

<details>
<summary>withdrawReserve</summary>

Withdraws a given amount of EGLD from the protocol reserves to an optionally given account.



# Arguments



- `egld_amount` - the amount of EGLD to withdraw

- `opt_to` - an optional address to send the EGLD to



# Notes



- can only be called by the admin

- the EGLD amount is directed to the admin account if none is provided


#### Inputs:
| Name | Type | Optional |
| - | - | - |
| egld_amount | BigUint |  |
| opt_to | Address | ✔ |


</details>

<details>
<summary>setTotalFee</summary>

Sets the total fee, which represents the final fee end users see discounted from their rewards based on the

service fee charged by each Staking Provider and by this Liquid Staking protocol. For example, if a Staking

Provider has a service fee of 7% and the total fee is set to 17%, the Liquid Staking Protocol will charge a 10%

fee from the total rewards.



# Arguments



- `fee` - the total fee in basis points



# Notes



- can only be called by the admin


#### Inputs:
| Name | Type |
| - | - |
| fee | BigUint |


</details>

<details>
<summary>setDelegationScoreModelParams</summary>

Sets the Delegation Score Model parameters used for the computation of the delegation score for each Staking

Provider Delegation smart contract. Higher scores imply better chances of being selected at delegations as well

as lower chances of being selected for undelegations.



# Arguments



- `method` - the score can be based only on Total Value Locked, APR or a weighted mix of both parameters

- `min_tvl` - Delegation smart contracts with lower TVLs than this parameters share the same TVL score

- `max_tvl` - Delegation smart contracts with higher TVLs than this parameters share the same TVL score

- `min_apr` - Delegation smart contracts with lower APRs than this parameters share the same APR score (in bps)

- `max_apr` - Delegation smart contracts with higher APRs than this parameters share the same APR score (in bps)

- `opt_omega` - should be given only for a Mixed delegation score method and defines the weight for both TVL and

  APR scores

- `sort` - if true, the list of Delegation smart contracts will be sorted based on the new delegation score

  model parameters. If false, the sorting is left to `changeDelegationContractParams`.



# Notes



- can only be called by the admin


#### Inputs:
| Name | Type | Optional |
| - | - | - |
| method | DelegationScoreMethod |  |
| min_tvl | BigUint |  |
| max_tvl | BigUint |  |
| min_apr | BigUint |  |
| max_apr | BigUint |  |
| sort | bool |  |
| opt_omega | BigUint | ✔ |


</details>

<details>
<summary>setDelegationSamplingModelParams</summary>

Sets the Delegation Sampling Model parameters used for the random selection between candidates on a computed

list of Staking Providers Delegation smart contracts.



# Arguments



- `tolerance` - the tolerance (as percentage and as bps) used to build the list of candidates

- `max_service_fee` - from this point onwards, staking providers do not receive delegations in bps

- `premium` - the difference between the delegation weight at service_fee = 0 and the delegation weight at

  service_fee = max_service_fee in bps



# Notes



- can only be called by the admin


#### Inputs:
| Name | Type |
| - | - |
| tolerance | BigUint |
| max_service_fee | BigUint |
| premium | BigUint |


</details>

<details>
<summary>clearDelegationSamplingModel</summary>

Clears the Delegation Sampling Model, i.e. removes the sampling from delegation and undelegation candidates.



# Notes



- can only be called by the admin



</details>

<details>
<summary>deactivateUndelegationAlgorithm</summary>

A public endpoint that allows to start bypassing the undelegation algorithm in order to undelegate and,

consequently, withdraw EGLD from the protocol.



# Notes



- can be called by anyone after `NO_UNDELEGATIONS_EPOCHS` have passed since the last undelegation



</details>

<details>
<summary>reactivateUndelegationAlgorithm</summary>

An admin endpoint that reactivates the undelegation algorithm.



# Notes



- can only be called by the admin

- can only be reactivated after `NO_UNDELEGATIONS_EPOCHS + COOLDOWN_REACTIVATE_UNDELEGATION_ALGORITHM` have

  elapsed since the last undelegation



</details>

<details>
<summary>addToMigrationWhitelist</summary>

Adds an entry to the migration whitelist. This whitelist allows users to bypass the Delegation Algorithm for

delegates.



# Arguments



- `user` - the user that wil be entitled to bypass the delegation algorithm

- `delegation_contract` - the Delegation smart contract



# Notes



- can only be called by the admin


#### Inputs:
| Name | Type |
| - | - |
| user | Address |
| delegation_contract | Address |


</details>

<details>
<summary>removeFromMigrationWhitelist</summary>

Removes an entry from the migration whitelist.



# Arguments



- `user` - the user that is currently entitled to bypass the delegation algorithm



# Notes



- can only be called by the admin


#### Inputs:
| Name | Type |
| - | - |
| user | Address |


</details>

<details>
<summary>removeMeFromMigrationWhitelist</summary>

Removes the caller from the migration whitelist.



</details>

<details>
<summary>claimRewardsFrom</summary>

Allows anyone to claim rewards from a given Delegation smart contract.



# Arguments



- `delegation_contract` - the Delegation smart contract address


#### Inputs:
| Name | Type |
| - | - |
| delegation_contract | Address |


</details>

<details>
<summary>delegateRewards</summary>

Allows anyone to delegate EGLD rewards balance to a staking provider based on the current configuration of the

delegation algorithm. If the delegation is successful, the callback updates the storage. Otherwise, it sets the

Delegation smart contract data as outdated. Notice that the smart contract data will be outdated until it is updated.



# Arguments



- `opt_egld_amount` - an optional amount of EGLD from the rewards balance to delegate


#### Inputs:
| Name | Type | Optional |
| - | - | - |
| opt_egld_amount | BigUint | ✔ |


</details>

<details>
<summary>unDelegate</summary>

Allows users to redeem sEGLD in exchange for EGLD. Instead of immediately sending the EGLD to the user, an

undelegate NFT is minted and sent to the user. This NFT can be redeemed for EGLD once the unbond period has

passed through the `unbond` endpoint. The paid sEGLD is burned.



If not provided, the Delegation smart contract for the undelegation is selected based on the current

configuration of the delegation algorithm. On the other hand, the Delegation smart contract can be specified

only if the undelegation mode is set to `Free`.



Notice that this endpoint does not automatically perform the undelegation. Instead, anyone can perform the

undelegation at any given point in time using the `unDelegatePendingAmount` public endpoint.



# Arguments



- `opt_delegation_contract`: The address of the Delegation smart contract to undelegate from



# Notes



- There is a minimum amount of 1 EGLD for undelegations, which corresponds to a minimum amount of sEGLD

  depending on the current exchange rate.


#### Note: This endpoint is payable by any token.

#### Inputs:
| Name | Type | Optional |
| - | - | - |
| opt_delegation_contract | Address | ✔ |

#### Outputs:
| Type |
| - |
| EsdtTokenPayment |


</details>

<details>
<summary>unDelegatePendingAmount</summary>

Initiates the undelegation of the pending amount from the specified Delegation smart contract. This endpoint

performs an asynchronous call to the Delegation smart contract to undelegate the pending amount. It is capable

of handling multiple calls, and the execution order of their callbacks does not need to match the order of the

original calls.



# Arguments



- `delegation_contract`: The address of the Delegation smart contract to undelegate from.



# Notes



- This endpoint can be called by anyone.

- There is no need to provide an optional argument for the amount of EGLD to undelegate. The pending amount to

  undelegate should always be sufficient and prevent leaving dust at the Delegation smart contract. Both the

  `undelegate` and `penalty_from_undelegation` functions ensure the adequacy of the pending amount.


#### Inputs:
| Name | Type |
| - | - |
| delegation_contract | Address |


</details>

<details>
<summary>withdraw</summary>

Allows users to redeem undelegate NFTs in exchange for EGLD once the unbond period has passed. To successfully

redeem the EGLD, it must already be in the liquid staking smart contract. Therefore, the public endpoint

`withdrawFrom` should have been called prior to using this function. If the redemption is successful, the NFT is

burned, and the corresponding EGLD amount is sent to the caller.


#### Note: This endpoint is payable by any token.

#### Outputs:
| Type |
| - |
| BigUint |


</details>

<details>
<summary>withdrawFrom</summary>

Initiates the withdrawal of the withdrawable amount from the specified Delegation smart contract. This endpoint

performs an asynchronous call to withdraw the amount that has been previously undelegated and has passed the

unbond period. It is capable of handling multiple calls, and the execution order of their callbacks does not

need to match the order of the original calls.



# Arguments



- `delegation_contract`: The address of the Delegation smart contract to withdraw from.



# Notes



- This endpoint can be called by anyone.

- It only needs to be called once per epoch.


#### Inputs:
| Name | Type |
| - | - |
| delegation_contract | Address |


</details>

<details>
<summary>penalize</summary>

Initiates a penalty to a Delegation smart contract. Penalties reduce the staked amount of a Delegation smart

contract through two different mechanisms:



1. By undelegating an amount of EGLD from the Delegation smart contract.

2. By reducing the pending amount of EGLD to be delegated to the Delegation smart contract.



The first mechanism can only be triggered by the admin when detecting misbehavior from the Staking Agency

associated with the Delegation smart contract. This penalty must be unbonded from the Delegation smart contract

at a future time using the `unbondPenalty` public endpoint.



The second mechanism can be triggered by the admin in cases of Staking Agency misbehavior or when there is a

pending amount to be delegated that cannot be deposited due to current cap and total value locked values. The

community may also initiate this penalty if specific conditions are met. Since this penalty affects the pending

amount to be delegated, the EGLD is already present and does not need to be withdrawn. Therefore, the penalty is

marked as `withdrawn`.



Finally, all penalties need to be delegated to a new Delegation smart contract. This is achieved by calling the

`delegatePenalty` endpoint. If for some reason this is not done, user will eventually have the chance to

undelegate from penalties.



# Arguments



- `delegation_contract`: The address of the Delegation smart contract.

- `source`: The source or type of the penalty.

- `opt_egld_amount`: The amount of EGLD to penalize. If unspecified, it defaults to the total delegated or

  pending amount to be delegated.


#### Inputs:
| Name | Type | Optional |
| - | - | - |
| delegation_contract | Address |  |
| source | PenaltySource |  |
| opt_egld_amount | BigUint | ✔ |


</details>

<details>
<summary>withdrawPenalty</summary>

Marks a penalty as withdrawn once the unbond period has passed. In order to be successful, the EGLD must be

already in the liquid staking smart contract. For that reason, the public endpoint `withdrawFrom` should have

been already called before this point.



# Arguments



- `penalty_id` - the penalty identifier


#### Inputs:
| Name | Type |
| - | - |
| penalty_id | u64 |


</details>

<details>
<summary>delegatePenalty</summary>

Allows anyone to delegate a Penalty to a new Delegation smart contract based on the current configuration of the

delegation algorithm, avoiding the penalized Delegation smart contract. Similarly to `delegate`, it does not

perform the delegation automatically, but it can be done by anyone at any given point in time using the

`delegatePendingAmount` public endpoint.



# Arguments



- `penalty_id` - the penalty identifier

- `opt_egld_amount` - the amount of EGLD to delegate. If unspecified, it defaults to the penalty amount


#### Inputs:
| Name | Type | Optional |
| - | - | - |
| penalty_id | u64 |  |
| opt_egld_amount | BigUint | ✔ |


</details>

<details>
<summary>withdrawFromPenalty</summary>

A public endpoint that allows users to withdraw from penalties when the undelegation mode is set to `Free`.

Since penalties must be already marked as `withdrawn`, which means that the EGLD is already available at this

smart contract, the EGLD is sent directly to the user and the penalty is updated or cleared.



# Arguments



- `penalty_id` - the penalty identifier


#### Note: This endpoint is payable by any token.

#### Inputs:
| Name | Type |
| - | - |
| penalty_id | u64 |


</details>

## Views

<details>
<summary>getAdmin</summary>

Returns the current admin address.



# Returns:



- The current admin address.


#### Outputs:
| Type |
| - |
| Address |


</details>

<details>
<summary>getPendingAdmin</summary>

Returns the current pending admin address, if there is one.



# Returns:



- An `Option` containing the pending admin address if there is one, or `None` if there is not.


#### Outputs:
| Type | Optional |
| - | - |
| Address | ✔ |


</details>

<details>
<summary>isLiquidStaking</summary>

#### Outputs:
| Type |
| - |
| bool |


</details>

<details>
<summary>isActive</summary>

#### Outputs:
| Type |
| - |
| bool |


</details>

<details>
<summary>getLsTokenId</summary>

Returns the liquid staking token identifier


#### Outputs:
| Type |
| - |
| TokenIdentifier |


</details>

<details>
<summary>getExchangeRate</summary>

Computes the current exchange rate in WAD between EGLD and sEGLD


#### Outputs:
| Type |
| - |
| BigUint |


</details>

<details>
<summary>getState</summary>

The current state of the Liquid Staking module
#### Outputs:
| Type |
| - |
| State |


</details>

<details>
<summary>getLsSupply</summary>

The current outstanding supply of sEGLD or the current amount of total shares
#### Outputs:
| Type |
| - |
| BigUint |


</details>

<details>
<summary>getUndelegateTokenId</summary>

The NFT given in exchange for sEGLD at unDelegations
#### Outputs:
| Type |
| - |
| TokenIdentifier |


</details>

<details>
<summary>getUndelegateTokenName</summary>

The Undelegate NFT name
#### Outputs:
| Type |
| - |
| bytes |


</details>

<details>
<summary>getCashReserve</summary>

The current amount of EGLD being staked via Liquid Staking amongst all the whitelisted Staking Providers
#### Outputs:
| Type |
| - |
| BigUint |


</details>

<details>
<summary>getRewardsReserve</summary>

The current amount of rewards in EGLD
#### Outputs:
| Type |
| - |
| BigUint |


</details>

<details>
<summary>getProtocolReserves</summary>

The current amount of EGLD that belongs to the protocol
#### Outputs:
| Type |
| - |
| BigUint |


</details>

<details>
<summary>getTotalUndelegated</summary>

The current total amount of EGLD being undelegated from all staking providers
#### Outputs:
| Type |
| - |
| BigUint |


</details>

<details>
<summary>getTotalWithdrawable</summary>

The current total amount of EGLD that can be unbonded or withdraw from all staking providers
#### Outputs:
| Type |
| - |
| BigUint |


</details>

<details>
<summary>getPenaltyById</summary>

Penalties by their identifiers
#### Inputs:
| Name | Type |
| - | - |
| id | u64 |

#### Outputs:
| Type |
| - |
| Penalty |


</details>

<details>
<summary>getNextPenaltyId</summary>

The next penalty identifier
#### Outputs:
| Type |
| - |
| u64 |


</details>

<details>
<summary>getDelegationContractsList</summary>

A linked list of Delegation smart contracts ordered by their delegation score
#### Outputs:
| Type | MultiValue |
| - | - |
| Address | ✔ |


</details>

<details>
<summary>getMigrationWhitelist</summary>

Allows users to delegate their EGLD to a given staking provider Delegation smart contract bypassing the Delegation

Algorithm
#### Inputs:
| Name | Type |
| - | - |
| user | Address |

#### Outputs:
| Type |
| - |
| Address |


</details>

<details>
<summary>getNumWhitelistedUsers</summary>

#### Inputs:
| Name | Type |
| - | - |
| delegation_contract | Address |

#### Outputs:
| Type |
| - |
| u32 |


</details>

<details>
<summary>getBlacklistedDelegationContracts</summary>

A list of blacklisted Delegation smart contracts
#### Outputs:
| Type | MultiValue |
| - | - |
| Address | ✔ |


</details>

<details>
<summary>getDelegationContractData</summary>

The metadata for each Delegation smart contract
#### Inputs:
| Name | Type |
| - | - |
| delegation_contract | Address |

#### Outputs:
| Type |
| - |
| DelegationContractData |


</details>

<details>
<summary>getUndelegationMode</summary>

The undelegation mode
#### Outputs:
| Type |
| - |
| UndelegationMode |


</details>

<details>
<summary>getLastUndelegateEpoch</summary>

The last epoch a successful undelegation occur when the undelegation mode is of `Algorithm` type
#### Outputs:
| Type |
| - |
| u64 |


</details>

<details>
<summary>getLastContractDataUpdateEpoch</summary>

The last epoch a successful contract data update occur
#### Outputs:
| Type |
| - |
| u64 |


</details>

<details>
<summary>getLastClaimRewardsEpoch</summary>

The last epoch rewards have been claimed for a given Staking Provider Delegation smart contract
#### Inputs:
| Name | Type |
| - | - |
| delegation_contract | Address |

#### Outputs:
| Type |
| - |
| u64 |


</details>

<details>
<summary>getUnbondPeriod</summary>

The period between undelegations and unbonds
#### Outputs:
| Type |
| - |
| u64 |


</details>

<details>
<summary>getTotalFee</summary>

The final fee charged to users, including staking providers service fee and liquid staking fee
#### Outputs:
| Type |
| - |
| BigUint |


</details>

<details>
<summary>getDelegationScoreModel</summary>

The Delegation Score model parameters
#### Outputs:
| Type |
| - |
| DelegationScoreModel |


</details>

<details>
<summary>getDelegationSamplingModel</summary>

The Delegation Sampling model parameters
#### Outputs:
| Type |
| - |
| SamplingModel |


</details>

<details>
<summary>getDataManager</summary>

Stores the Delegation smart contract data manager address
#### Outputs:
| Type |
| - |
| Address |


</details>

<details>
<summary>getRandomOracle</summary>

Stores the random oracle address, used only for testing purposes
#### Outputs:
| Type |
| - |
| Address |


</details>

## Events

<details>
<summary>new_pending_admin_event</summary>

Event emitted when the pending admin is updated.
#### Inputs:
| Name | Type |
| - | - |
| pending_admin | Address |

</details>

<details>
<summary>new_admin_event</summary>

Event emitted when the admin is updated.
#### Inputs:
| Name | Type |
| - | - |
| admin | Address |

</details>

<details>
<summary>set_unbond_period_event</summary>

Emitted when unbond period is set
#### Inputs:
| Name | Type |
| - | - |
| unbond_period | u64 |

</details>

<details>
<summary>set_undelegation_mode_event</summary>

Emitted when the undelegation mode is set
#### Inputs:
| Name | Type |
| - | - |
| undelegation_mode | UndelegationMode |

</details>

<details>
<summary>set_last_undelegate_epoch_event</summary>

Emitted when the last undelegate epoch is set
#### Inputs:
| Name | Type |
| - | - |
| last_undelegate_epoch | u64 |

</details>

<details>
<summary>set_last_contract_data_update_epoch_event</summary>

Emitted when the last contract data update epoch is set
#### Inputs:
| Name | Type |
| - | - |
| last_undelegate_epoch | u64 |

</details>

<details>
<summary>register_ls_token_event</summary>

Emitted when the liquid staking token is registered
#### Inputs:
| Name | Type |
| - | - |
| ls_token_id | TokenIdentifier |

</details>

<details>
<summary>register_undelegate_token_event</summary>

Emitted when the undelegate nft is registered
#### Inputs:
| Name | Type |
| - | - |
| undelegate_id | TokenIdentifier |

</details>

<details>
<summary>new_data_manager_event</summary>

Emitted when a new data manager is set
#### Inputs:
| Name | Type | Optional |
| - | - | - |
| old | Address | ✔ |
| new | Address |  |

</details>

<details>
<summary>set_delegation_score_model_params_event</summary>

Emitted when the delegation score model parameters are set or modified
#### Inputs:
| Name | Type |
| - | - |
| score_model | DelegationScoreModel |

</details>

<details>
<summary>set_delegation_sampling_model_params_event</summary>

Emitted when the delegation sampling model parameters are set or modified
#### Inputs:
| Name | Type |
| - | - |
| sampling_model | SamplingModel |

</details>

<details>
<summary>set_total_fee_event</summary>

Emitted when the total fee is set or modified
#### Inputs:
| Name | Type |
| - | - |
| total_fee | BigUint |

</details>

<details>
<summary>clear_delegation_sampling_model_event</summary>

Emitted when the delegation sampling model is removed
</details>

<details>
<summary>set_state_event</summary>

Emitted when the liquid staking state modified
#### Inputs:
| Name | Type |
| - | - |
| active | bool |

</details>

<details>
<summary>whitelist_delegation_contract_event</summary>

Emitted when a Delegation smart contract is whitelisted
#### Inputs:
| Name | Type |
| - | - |
| contract_data | DelegationContractData |

</details>

<details>
<summary>blacklist_delegation_contract_event</summary>

Emitted when a Delegation smart contract is blacklisted
#### Inputs:
| Name | Type |
| - | - |
| contract_data | DelegationContractData |

</details>

<details>
<summary>change_delegation_contract_params_event</summary>

Emitted when the Delegation smart contract params are modified
#### Inputs:
| Name | Type |
| - | - |
| contract_data | DelegationContractData |

</details>

<details>
<summary>delegate_event</summary>

Emitted when a user delegates to Liquid Staking
#### Inputs:
| Name | Type |
| - | - |
| account | Address |
| egld_amount | BigUint |
| shares | BigUint |
| contract_data | DelegationContractData |

</details>

<details>
<summary>delegate_pending_amount_event</summary>

Emitted when a pending amount is delegated to a Delegation smart contract
#### Inputs:
| Name | Type |
| - | - |
| account | Address |
| contract | Address |
| egld_amount | BigUint |

</details>

<details>
<summary>undelegate_event</summary>

Emitted when a user undelegates from Liquid Staking
#### Inputs:
| Name | Type |
| - | - |
| account | Address |
| undelegate_token_nonce | u64 |
| undelegate_attrs | UndelegateAttributes |
| contract_data | DelegationContractData |

</details>

<details>
<summary>undelegate_pending_amount_event</summary>

Emitted when a pending amount is undelegated from a Delegation smart contract
#### Inputs:
| Name | Type |
| - | - |
| account | Address |
| contract | Address |
| egld_amount | BigUint |

</details>

<details>
<summary>withdraw_event</summary>

Emitted when a user withdraws EGLD from Liquid Staking
#### Inputs:
| Name | Type |
| - | - |
| account | Address |
| undelegate_token_nonce | u64 |
| contract_data | DelegationContractData |

</details>

<details>
<summary>withdraw_from_event</summary>

Emitted when an amount of EGLD in withdrawn from a Delegation smart contract
#### Inputs:
| Name | Type |
| - | - |
| account | Address |
| contract | Address |
| egld_amount | BigUint |

</details>

<details>
<summary>penalty_from_undelegation_event</summary>

Emitted when the admin penalizes via an undelegation from a specific Delegation smart contract
#### Inputs:
| Name | Type |
| - | - |
| account | Address |
| penalty | Penalty |
| contract_data | DelegationContractData |

</details>

<details>
<summary>penalty_from_pending_to_delegate_event</summary>

Emitted when a Delegation smart contract is penalized reducing its pending to delegate amount
#### Inputs:
| Name | Type |
| - | - |
| account | Address |
| penalty | Penalty |
| contract_data | DelegationContractData |

</details>

<details>
<summary>withdraw_penalty_event</summary>

Emitted when a penalty is marked as withdrawn
#### Inputs:
| Name | Type |
| - | - |
| account | Address |
| penalty_id | u64 |
| contract_data | DelegationContractData |

</details>

<details>
<summary>delegate_penalty_event</summary>

Emitted when a penalty in its whole or a part of it is delegated
#### Inputs:
| Name | Type |
| - | - |
| account | Address |
| contract | Address |
| penalty_id | u64 |
| egld_amount | BigUint |
| contract_data | DelegationContractData |

</details>

<details>
<summary>withdraw_from_penalty_event</summary>

Emitted when a user withdraws from a penalty in the Free mode
#### Inputs:
| Name | Type |
| - | - |
| account | Address |
| penalty_id | u64 |
| egld_amount | BigUint |
| shares | BigUint |

</details>

<details>
<summary>claim_rewards_from_event</summary>

Emitted when anyone claims rewards
#### Inputs:
| Name | Type |
| - | - |
| account | Address |
| contract | Address |
| reserves_amount | BigUint |
| rewards_amount | BigUint |
| contract_data | DelegationContractData |

</details>

<details>
<summary>delegate_rewards_event</summary>

Emitted when the admin delegates rewards
#### Inputs:
| Name | Type |
| - | - |
| account | Address |
| contract | Address |
| egld_amount | BigUint |
| contract_data | DelegationContractData |

</details>

<details>
<summary>withdraw_reserve_event</summary>

Emitted when the admin withdraws funds from the protocol reserve
#### Inputs:
| Name | Type |
| - | - |
| caller | Address |
| withdraw_amount | BigUint |
| to | Address |

</details>

<details>
<summary>add_to_migration_whitelist_event</summary>

Adds a user to the migration whitelist
#### Inputs:
| Name | Type |
| - | - |
| user | Address |
| contract | Address |

</details>

<details>
<summary>remove_from_migration_whitelist_event</summary>

Removes a user from the migration whitelist
#### Inputs:
| Name | Type |
| - | - |
| user | Address |

</details>

<details>
<summary>async_call_error_event</summary>

Emitted when an async call fails
#### Inputs:
| Name | Type |
| - | - |
| error_code | u32 |
| error_msg | bytes |

</details>

<details>
<summary>outdated_event</summary>

Emitted when an async call fails and contract data is outdated
#### Inputs:
| Name | Type |
| - | - |
| contract | Address |

</details>

