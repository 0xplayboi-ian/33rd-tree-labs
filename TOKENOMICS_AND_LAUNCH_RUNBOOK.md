# 33RD TREE LABS // TOKENOMICS SPECIFICATION & TOKEN LAUNCH RUNBOOK
**Document Version:** Canary Specification v4.0  
**Target Network:** Solana Mainnet-Beta  
**Official Protocol Domain:** [33rdtreelabs.tech](https://33rdtreelabs.tech)  
**Token Symbol:** $33RD  
**Canonical Hard Cap:** 33,333,333 $33RD (Immutable on-chain)  
**Standard:** SPL Token / Token-2022 Standard (9 Decimals)  
**Canonical Burn Target:** Solana Incinerator (`1nc1nerator11111111111111111111111111111111`)

---

## 1. Executive Summary & Monetary Philosophy

The $33RD token is the native utility, staking, and settlement instrument powering the 33rd Tree Labs Verifiable DePIN Compute Fabric. Designed as an anti-inflationary, hard-capped utility asset, $33RD anchors physical GPU cluster capacity directly to on-chain cryptographic consensus on Solana.

Centralized AI clouds operate on opaque billing, vendor lock-in, and unverified execution. Conversely, traditional crypto proof-of-work exhausts petawatts on unconstrained SHA-256 hash grinding. 33rd Tree Labs replaces hash grinding with **Proof of Inference (PoI)**: nodes evaluate bit-exact INT8/FP8 transformer kernels (CAP-FFN), generate zero-knowledge polynomial proofs (Halo2-KZG / HyperNova-Plonky3), and settle consensus slots under strict stake-weighted rules.

### Core Economic Constants

| Parameter | Specification | Cryptographic / Settlement Rationale |
| :--- | :--- | :--- |
| **Total Hard Cap** | **33,333,333 $33RD** | Strict asymptotic ceiling. Mint authority revoked at genesis. |
| **Token Standard** | SPL Token (9 Decimals) | High-speed native settlement on Solana; compatible with DEXs & Anchor. |
| **Decimals** | 9 | $1\text{ }33RD = 1,000,000,000\text{ atomic lamports/subunits}$. |
| **Minimum Node Stake** | 25,000 $33RD | Hardware admission barrier against Sybil identities (~$1.24M capital gate). |
| **Unbonding Window** | 7 Days (10,080 Blocks) | Exceeds the 64-block optimistic dispute window and 48h interactive bisection. |
| **Byzantine Quorum** | $K = 64$ Nodes | BFT committee requiring $> 2/3$ stake-weighted attestation for slot commits. |
| **Protocol Fee Split** | **75% / 15% / 10%** | 75% Node Operators, 15% Treasury R&D, 10% Permanent Incinerator Burn. |
| **Slot Cadence** | 12.0 Seconds | Synchronized with Solana Anchor state commit transactions. |

---

## 2. Supply Architecture & Genesis Allocation Schedule

The entire lifetime supply of 33,333,333 $33RD is minted at genesis into dedicated vault accounts before the mint authority is permanently disabled.

```
+-----------------------------------------------------------------------------------+
|                     CANONICAL GENESIS ALLOCATION (33,333,333 $33RD)               |
+-----------------------------------------------------------------------------------+
| [45.0%] Hardware Compute Subsidy (PoI Emissions)        : 15,000,000 $33RD        |
| [15.0%] Initial Liquidity & Market Bootstrapping        :  5,000,000 $33RD        |
| [15.0%] Core Protocol Engineering & Cryptography        :  5,000,000 $33RD        |
| [15.0%] Ecosystem Growth & Node Grants                  :  5,000,000 $33RD        |
| [10.0%] Strategic Canary Institutional Backers          :  3,333,333 $33RD        |
+-----------------------------------------------------------------------------------+
```

### Allocation Breakdown Table

| Category | Allocation (%) | Total Tokens | Vesting Schedule / Lockup Terms |
| :--- | :---: | :---: | :--- |
| **Hardware Compute Subsidy** | 45.00% | 15,000,000 | 4-Year geometric halving schedule governed by on-chain Anchor program. |
| **Initial DEX Liquidity** | 15.00% | 5,000,000 | 100% unlocked at TGE, paired with SOL/USDC. **LP tokens burned to Solana Incinerator**. |
| **Core Engineering & Cryptography** | 15.00% | 5,000,000 | 12-month cliff, followed by 36-month linear per-second stream via Streamflow. |
| **Ecosystem & Node Grants** | 15.00% | 5,000,000 | Multi-sig locked. 10% unlocked at TGE, 90% released quarterly over 4 years on milestone gates. |
| **Strategic Canary Backers** | 10.00% | 3,333,333 | 6-month cliff, followed by 24-month linear vesting via Streamflow. |
| **Total** | **100.00%** | **33,333,333** | **Hard cap mathematically enforceable.** |

---

## 3. Emission Halving Schedule (Hardware Compute Subsidy)

The 15,000,000 $33RD allocated to compute node operators is distributed asymptotically via geometric halving every 4 years (10,512,000 Solana slots at 12s per block):

$$\mathcal{E}(t) = \mathcal{E}_0 \cdot \left(\frac{1}{2}\right)^{\lfloor t / T_{\text{epoch}} \rfloor}$$

Where $T_{\text{epoch}} = 4\text{ years}$ and $\mathcal{E}_0 = 7,500,000\text{ }33RD$.

| Halving Era | Duration | Daily Emission ($33RD) | Era Emission ($33RD) | Cumulative Distributed | Remaining Reserve |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **Era 1** | Year 1 – 4 | 5,136.98 | 7,500,000 | 7,500,000 (50.0%) | 7,500,000 |
| **Era 2** | Year 5 – 8 | 2,568.49 | 3,750,000 | 11,250,000 (75.0%) | 3,750,000 |
| **Era 3** | Year 9 – 12 | 1,284.25 | 1,875,000 | 13,125,000 (87.5%) | 1,875,000 |
| **Era 4** | Year 13 – 16 | 642.12 | 937,500 | 14,062,500 (93.75%) | 937,500 |
| **Tail** | Year 17+ | Asymptotic | 937,500 | 15,000,000 (100.0%) | 0 |

---

## 4. Fee Mechanics, Value Accrual & Solana Incinerator Burn

All inference requests submitted to the fabric must pay service fees in $33RD or native SOL (which the protocol auto-swaps to $33RD via on-chain Jupiter/Raydium liquidity routing).

Every fee unit collected by the Anchor settlement program is split atomically on-chain:

```
                          [ INCOMING INFERENCE FEE ]
                                      |
              +-----------------------+-----------------------+
              | (75%)                 | (15%)                 | (10%)
              v                       v                       v
      [ NODE OPERATORS ]      [ PROTOCOL TREASURY ]   [ SOLANA INCINERATOR ]
      Distributed to K=64     Dedicated Squads        1nc1nerator111111...
      committee based on      Multisig for audits,    PERMANENT SUPPLY
      PoI INT8 exactness.     security, and grants.   DESTRUCTION (BURN)
```

### Mathematical Net Deflationary Tipping Point

Net daily supply delta $\Delta S$ is defined as:

$$\Delta S = \mathcal{E}_{\text{daily}} - \mathcal{B}_{\text{daily}}$$

Where:
- $\mathcal{E}_{\text{daily}}$ is the daily hardware emission.
- $\mathcal{B}_{\text{daily}} = 0.10 \times \text{Daily Invoiced Fee Volume}$.

When daily network inference fees exceed $51,370\text{ }33RD$ in Era 1, daily burn exceeds daily emissions ($\mathcal{B}_{\text{daily}} > \mathcal{E}_{\text{daily}}$), making the token supply strictly deflationary.

---

## 5. Staking Architecture & Byzantine Slashing Rules

To qualify for admission into the $K=64$ slot proposal committee, compute clusters must lock a minimum of 25,000 $33RD into the protocol staking program.

### Slashing Penalty Matrix

| Violation Type | Severity | Slashed Stake | Slashed Allocation | Protocol Action |
| :--- | :---: | :---: | :--- | :--- |
| **Dual-Signing / Equivocation** | Critical | **100%** | 50% Burned, 50% Whistleblower bounty | Permanent ban of Node ID & Hardware Key |
| **Invalid INT8 Tensor Output** | Critical | **50%** | 50% Burned to Incinerator | Node disqualified from epoch; slot rolled back |
| **Failed Halo2-KZG Proof Challenge** | High | **25%** | 25% Burned to Incinerator | Challenger rewarded with 5,000 $33RD |
| **Liveness Failure (>10 Omitted Slots)** | Medium | **5%** | Transferred to Protocol Treasury | Node demoted to standby queue |
| **TEE Attestation Mismatch** | High | **30%** | 100% Burned to Incinerator | Silicon attestation revoked |

---

## 6. Technical Step-by-Step Token Launch Runbook

This runbook provides the exact CLI instructions for deploying, verifying, and launching $33RD on Solana mainnet.

### Phase 1: Environment & Tooling Setup

```bash
# 1. Ensure Solana CLI is updated
solana --version  # Must be >= 1.18.0

# 2. Configure for Solana Mainnet-Beta
solana config set --url https://api.mainnet-beta.solana.com

# 3. Verify hardware key / deployer wallet
solana address
solana balance
```

### Phase 2: Create Token Mint (SPL Standard, 9 Decimals)

```bash
# 1. Create a dedicated mint keypair
solana-keygen new -o /path/to/33rd_mint_keypair.json

# 2. Create the token mint with 9 decimals
spl-token create-token \
  --program-id TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA \
  --decimals 9 \
  /path/to/33rd_mint_keypair.json

# Record the generated MINT_ADDRESS:
export MINT_ADDR="<DEPLOYED_MINT_ADDRESS>"
```

### Phase 3: Create Metadata Account (Metaplex On-Chain)

Create `metadata.json` and host on `https://33rdtreelabs.tech/assets/token_metadata.json`:

```json
{
  "name": "33rd Tree Labs",
  "symbol": "33RD",
  "description": "Verifiable DePIN Compute Fabric on Solana. Hierarchical Tensor Arbor coordination and zero-knowledge neural evaluations.",
  "image": "https://33rdtreelabs.tech/assets/official_logo_mark.png",
  "external_url": "https://33rdtreelabs.tech",
  "properties": {
    "files": [
      {
        "uri": "https://33rdtreelabs.tech/assets/official_logo_mark.png",
        "type": "image/png"
      }
    ],
    "category": "image"
  }
}
```

Upload metadata on-chain via Metaplex CLI or Umi script.

### Phase 4: Mint Exact Hard Cap (33,333,333 Tokens)

```bash
# 1. Create the primary distribution treasury token account
spl-token create-account $MINT_ADDR

# 2. Mint exactly 33,333,333 tokens (plus 9 zeros for decimals)
spl-token mint $MINT_ADDR 33333333

# 3. Verify total supply on-chain
spl-token supply $MINT_ADDR
# Output must read exactly: 33333333
```

### Phase 5: Irrevocable Authority Revocation (Guaranteeing Hard Cap)

> [!CAUTION]
> Once mint authority is revoked, no additional tokens can ever be created. This step is irreversible.

```bash
# 1. Permanently disable Mint Authority
spl-token authorize $MINT_ADDR mint --disable

# 2. Permanently disable Freeze Authority
spl-token authorize $MINT_ADDR freeze --disable

# 3. Verify revocation on-chain
spl-token display $MINT_ADDR
# Mint authority: None
# Freeze authority: None
```

### Phase 6: Multi-Sig Governance & Vesting Setup

1. **Deploy Squads v4 Multi-Sig**:
   - Establish a 3-of-5 hardware key multi-sig for the Protocol Treasury vault (`5,000,000 $33RD`) and Ecosystem Grants vault (`5,000,000 $33RD`).
2. **Configure Streamflow Vesting Contracts**:
   - Core Engineering: `5,000,000 $33RD` with 12-month cliff and 36-month linear streaming.
   - Strategic Canary Backers: `3,333,333 $33RD` with 6-month cliff and 24-month linear streaming.
3. **Fund Anchor Emissions Staking Vault**:
   - Transfer `15,000,000 $33RD` into the on-chain Anchor staking PDA program for PoI hardware subsidy distribution.

### Phase 7: Liquidity Bootstrapping & Permanent LP Burn

1. **Raydium CPMM / CLMM Pool Creation**:
   - Pair: `$33RD / SOL` and `$33RD / USDC`.
   - Allocation: `5,000,000 $33RD` paired with initial quote liquidity.
   - Price Banding: Configured via concentrated liquidity parameters.
2. **Permanent LP Token Destruction**:
   ```bash
   # Transfer 100% of the LP tokens directly to the Solana Incinerator:
   spl-token transfer <LP_TOKEN_MINT> <LP_TOKEN_AMOUNT> 1nc1nerator11111111111111111111111111111111
   ```
   Verify transaction signature on Solscan to provide public mathematical proof of locked liquidity.

---

## 7. Pre-Launch T-Minus Countdown Checklist

```
+-----------------------------------------------------------------------------------+
|                           T-MINUS OPERATIONAL RUNBOOK                             |
+-----------------------------------------------------------------------------------+
| [X] T-30 DAYS: Anchor Smart Contract Security Audits (OtterSec / Halborn).        |
| [X] T-14 DAYS: Testnet stress test with K=64 simulated Byzantine clusters.        |
| [X] T-7  DAYS: Multi-sig key ceremony (3-of-5 Ledger hardware wallets).          |
| [X] T-3  DAYS: Deploy official token metadata and verify on Solscan / Birdeye.    |
| [X] T-24 HRS : Pre-fund liquidity deployment wallets and test RPC failover.       |
| [X] T-0  HRS : Mint creation, disable mint/freeze authorities, fund LP.          |
| [X] T+5  MIN : Burn 100% of LP tokens to 1nc1nerator11111111111111111111111111111 |
| [X] T+15 MIN : Enable Anchor Staking Program deposit instruction.                 |
| [X] T+1  HR  : Verify first 10% fee burn transaction into Solana Incinerator.     |
+-----------------------------------------------------------------------------------+
```

---

## 8. Official Verification Links & Resources

- **Official Protocol Portal:** [https://33rdtreelabs.tech](https://33rdtreelabs.tech)
- **Tokenomics Specification:** [https://33rdtreelabs.tech/tokenomics.html](https://33rdtreelabs.tech/tokenomics.html)
- **Consensus & Byzantine Simulator:** [https://33rdtreelabs.tech/simulator.html](https://33rdtreelabs.tech/simulator.html)
- **Hardware Staking Yield Calculator:** [https://33rdtreelabs.tech/yield.html](https://33rdtreelabs.tech/yield.html)
- **Academic Whitepaper (Canary v4.0):** [https://33rdtreelabs.tech/whitepaper.html](https://33rdtreelabs.tech/whitepaper.html)
- **GitHub Repository:** [https://github.com/0xplayboi-ian/33rd-tree-labs.git](https://github.com/0xplayboi-ian/33rd-tree-labs.git)
- **Solana Incinerator Address:** `1nc1nerator11111111111111111111111111111111`
