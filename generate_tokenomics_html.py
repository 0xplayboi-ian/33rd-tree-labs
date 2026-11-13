#!/usr/bin/env python3
import os
from build_subpages_full import get_page_head, get_page_foot

SITE_DIR = "/Users/ianmora/Desktop/Projects/33rd-tree-labs-site"

def build():
    head = get_page_head(
        title="33RD TREE LABS // Tokenomics Architecture &amp; Monetary Policy &bull; 33rdtreelabs.tech",
        description="Comprehensive Tokenomics Architecture for 33rd Tree Labs: Strict 33,333,333 $33RD Hard Cap, 100% Incinerated LP, Deflationary Burn Mathematics, and PoI Emission Decay Schedule.",
        active_page="tokenomics"
    )

    body = r"""
  <main class="page-wrap">
    <!-- EDITORIAL HERO / HEADER -->
    <header class="ed-hero">
      <div class="ed-kicker">( 006 ) // TOKEN ARCHITECTURE &amp; MONETARY POLICY &bull; 33RDTREELABS.TECH</div>
      <h1 class="ed-headline">TOKENOMICS ARCHITECTURE &amp;<br><span class="accent">MONETARY POLICY</span></h1>
      <p class="ed-lead">
        A mathematically capped, anti-inflationary utility and settlement asset on Solana. Strict asymptotic ceiling of 33,333,333 $33RD tokens, 100% LP incinerated to the canonical burner, zero mint authority, and continuous deflationary burn dynamics.
      </p>

      <!-- TELEMETRY STRIP (NO CARD CONTAINERS) -->
      <div class="telemetry-strip">
        <div class="telemetry-cell">
          <span class="telemetry-lbl">Immutable Hard Cap</span>
          <span class="telemetry-val accent">33,333,333 $33RD</span>
        </div>
        <div class="telemetry-cell">
          <span class="telemetry-lbl">Liquidity Pool Status</span>
          <span class="telemetry-val">100% LP INCINERATED</span>
        </div>
        <div class="telemetry-cell">
          <span class="telemetry-lbl">Mint Authority</span>
          <span class="telemetry-val">PERMANENTLY REVOKED (NONE)</span>
        </div>
        <div class="telemetry-cell">
          <span class="telemetry-lbl">Net Deflationary Threshold</span>
          <span class="telemetry-val green">&gt; 51,370 $33RD / DAY</span>
        </div>
      </div>
    </header>

    <!-- SECTION 01: CANONICAL ALLOCATION & IMMUTABLE SUPPLY -->
    <section class="ed-section" id="genesis-allocation">
      <div class="ed-sec-head">
        <div class="sec-badge-col">
          <span class="sec-giant-num">01</span>
          <span class="sec-kicker">// SUPPLY INVARIANTS</span>
        </div>
        <div>
          <h2 class="sec-title">Canonical Genesis Allocation &amp; Invariants</h2>
          <p class="sec-summary">
            The entire lifetime supply of 33,333,333 $33RD was minted at genesis under Solana's SPL Token-2022 standard. Immediately following genesis minting, the mint authority was permanently revoked via a signed on-chain transaction with <code>new_authority: None</code>. No additional tokens can ever be minted.
          </p>
        </div>
      </div>

      <!-- 4-COLUMN COMPARISON GRID (OPEN EDITORIAL - ZERO CARDS) -->
      <div class="ed-grid-4">
        <div class="ed-grid-col ed-grid-cell">
          <div>
            <span class="cell-tag">[ 45.0% // POI SUBSIDY ]</span>
            <h3 class="cell-title">Compute Subsidy</h3>
            <p class="cell-body">
              Distributed exclusively to verified hardware node operators executing deterministic forward passes and zero-knowledge neural evaluations over 96 epochs.
            </p>
          </div>
          <ul class="cell-spec-list">
            <li><span>Total Tokens:</span> <strong>15,000,000 $33RD</strong></li>
            <li><span>Distribution:</span> <strong>Epoch Decay Schedule</strong></li>
            <li><span>Halving Interval:</span> <strong>24 Epochs (~336 Days)</strong></li>
            <li><span>Vault PDA:</span> <strong>CanaryEmissionVault...</strong></li>
          </ul>
        </div>

        <div class="ed-grid-col ed-grid-cell">
          <div>
            <span class="cell-tag">[ 15.0% // PERMANENT LP ]</span>
            <h3 class="cell-title">Liquidity Pool</h3>
            <p class="cell-body">
              Paired with SOL for Raydium / Orca decentralized liquidity. 100% of LP tokens were transferred directly to the canonical Solana Incinerator address.
            </p>
          </div>
          <ul class="cell-spec-list">
            <li><span>Total Tokens:</span> <strong>5,000,000 $33RD</strong></li>
            <li><span>LP Burn Address:</span> <strong>1nc1nerator1111...1111</strong></li>
            <li><span>Rug Risk:</span> <strong>Mathematically Zero</strong></li>
            <li><span>Lock Window:</span> <strong>Permanent Eternity</strong></li>
          </ul>
        </div>

        <div class="ed-grid-col ed-grid-cell">
          <div>
            <span class="cell-tag">[ 15.0% // PROTOCOL R&amp;D ]</span>
            <h3 class="cell-title">Core Engineering</h3>
            <p class="cell-body">
              Dedicated to continuous research in hyperbolic geometry, recursive STARK folding, and Solana runtime optimizations. Locked under a 48-month linear stream.
            </p>
          </div>
          <ul class="cell-spec-list">
            <li><span>Total Tokens:</span> <strong>5,000,000 $33RD</strong></li>
            <li><span>Vesting Model:</span> <strong>48-Month Linear Stream</strong></li>
            <li><span>Initial Cliff:</span> <strong>6 Months (0% Upfront)</strong></li>
            <li><span>Custody PDA:</span> <strong>CanaryEngStreamVault...</strong></li>
          </ul>
        </div>

        <div class="ed-grid-col ed-grid-cell">
          <div>
            <span class="cell-tag">[ 25.0% // ECOSYSTEM &amp; BACKERS ]</span>
            <h3 class="cell-title">Ecosystem &amp; Grants</h3>
            <p class="cell-body">
              15% reserved for open-source AI model developer grants and TEE node tooling; 10% allocated to early strategic canary backers under 36-month vesting.
            </p>
          </div>
          <ul class="cell-spec-list">
            <li><span>Total Tokens:</span> <strong>8,333,333 $33RD</strong></li>
            <li><span>Ecosystem Allocation:</span> <strong>5,000,000 $33RD</strong></li>
            <li><span>Institutional Canary:</span> <strong>3,333,333 $33RD</strong></li>
            <li><span>Vesting Window:</span> <strong>36-Month Linear Vesting</strong></li>
          </ul>
        </div>
      </div>

      <!-- OPEN MONOSPACE ALLOCATION SPECIFICATION TABLE -->
      <div class="ed-table-wrap">
        <table class="ed-table">
          <thead>
            <tr>
              <th>Allocation Category</th>
              <th>Token Amount ($33RD)</th>
              <th>Percentage</th>
              <th>On-Chain Vesting Contract</th>
              <th>Release Mechanism</th>
              <th>Verification State</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="accent">Hardware Compute Subsidy (PoI)</td>
              <td class="highlight">15,000,000 $33RD</td>
              <td>45.0%</td>
              <td>Anchor Emission Vault PDA</td>
              <td>Epoch Decay ($E(k) = E_0 \cdot \gamma^k$)</td>
              <td class="green">PROGRAM LOCKED</td>
            </tr>
            <tr>
              <td class="accent">Initial DEX Liquidity (LP)</td>
              <td class="highlight">5,000,000 $33RD</td>
              <td>15.0%</td>
              <td>Solana Incinerator (1nc1nerator...)</td>
              <td>100% LP Tokens Incinerated</td>
              <td class="green">PERMANENTLY BURNED</td>
            </tr>
            <tr>
              <td class="accent">Core Cryptographic Engineering</td>
              <td class="highlight">5,000,000 $33RD</td>
              <td>15.0%</td>
              <td>Anchor Linear Stream PDA</td>
              <td>48-Month Stream // 6-Month Cliff</td>
              <td class="green">ON-CHAIN STREAM</td>
            </tr>
            <tr>
              <td class="accent">Ecosystem &amp; Node Operator Grants</td>
              <td class="highlight">5,000,000 $33RD</td>
              <td>15.0%</td>
              <td>Multisig Governance Vault PDA</td>
              <td>Milestone Deliverable Audits</td>
              <td class="green">MULTISIG CONTROLLED</td>
            </tr>
            <tr>
              <td class="accent">Strategic Canary Institutional</td>
              <td class="highlight">3,333,333 $33RD</td>
              <td>10.0%</td>
              <td>Anchor Institutional Vesting PDA</td>
              <td>36-Month Linear Vesting // 0% TGE</td>
              <td class="green">ESCROW LOCKED</td>
            </tr>
            <tr style="border-top:2px solid var(--border-light);">
              <td class="accent">CANONICAL TOTAL HARD CAP</td>
              <td class="highlight" style="color:var(--t); font-size:14px;">33,333,333 $33RD</td>
              <td style="color:var(--t); font-size:14px;">100.0%</td>
              <td>Mint Authority: Revoked (None)</td>
              <td>Zero Additional Minting Capacity</td>
              <td class="green">IMMUTABLE CAP</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- SECTION 02: DEFLATIONARY BURN MATHEMATICS -->
    <section class="ed-section" id="burn-mathematics">
      <div class="ed-sec-head">
        <div class="sec-badge-col">
          <span class="sec-giant-num">02</span>
          <span class="sec-kicker">// MONETARY DYNAMICS</span>
        </div>
        <div>
          <h2 class="sec-title">Deflationary Burn Mathematics &amp; Net Velocity</h2>
          <p class="sec-summary">
            The Singularity Protocol implements a continuous algorithmic burning mechanism. Every compute request, dispute resolution challenge, and slashing penalty permanently removes $33RD tokens from circulation via the Solana Incinerator.
          </p>
        </div>
      </div>

      <div class="ed-prose-cols">
        <div class="prose-block">
          <h3>Differential Rate of Supply Evolution</h3>
          <p>
            The instantaneous rate of change of the circulating token supply $S(t)$ is defined by the differential equation between gross scheduled validator emissions $E(t)$ and continuous protocol burns $B(t)$:
          </p>
          <div class="math-display-box">
            $$\frac{dS(t)}{dt} = E(t) - B(t)$$
          </div>
          <p>
            Gross token burn $B(t)$ is decomposed into three deterministic components:
          </p>
          <div class="math-display-box">
            $$B(t) = B_{\min} + \beta \cdot V(t) + \sum_{j=1}^M S_{\text{slashed}, j}(t)$$
          </div>
          <p>
            Where $B_{\min} = 1,440\text{ }33RD/\text{day}$ is the base protocol state maintenance burn floor, $\beta = 0.10$ is the 10% permanent burn captured on all network compute billing fees, $V(t)$ is the 24-hour network compute volume in $33RD$, and $S_{\text{slashed}}$ is the 30% portion of slashed validator bonds routed to the incinerator.
          </p>
        </div>

        <div class="prose-block">
          <h3>The Critical Deflationary Volume Floor</h3>
          <p>
            The network achieves **net deflationary velocity** ($\frac{dS}{dt} < 0$) when total continuous burns exceed gross emissions. The critical daily compute volume threshold $V_{\text{crit}}$ required for structural supply reduction is derived as:
          </p>
          <div class="math-display-box">
            $$V_{\text{crit}}(t) = \frac{E(t) - B_{\min}}{\beta} = \frac{E(t) - 1,440}{0.10}$$
          </div>
          <p>
            During Epoch 1 ($E_1 \approx 6,577\text{ }33RD/\text{day}$), the threshold resolves to:
          </p>
          <div class="math-display-box">
            $$V_{\text{crit}} = \frac{6,577 - 1,440}{0.10} \approx 51,370\text{ }33RD/\text{day}$$
          </div>
          <p>
            Whenever 24-hour decentralized compute demand exceeds $51,370\text{ }33RD$, the circulating token supply contracts monotonically, permanently driving scarcity as network adoption scales.
          </p>
        </div>
      </div>

      <!-- SUPPLY SIMULATION ACROSS EPOCHS -->
      <h3 style="font-family:var(--fh); font-size:22px; text-transform:uppercase; margin:40px 0 16px;">Supply Trajectory &amp; Burn Projection Table</h3>
      <div class="ed-table-wrap">
        <table class="ed-table">
          <thead>
            <tr>
              <th>Epoch Index</th>
              <th>Time Elapsed</th>
              <th>Daily Emission $E(t)$</th>
              <th>Low Volume (15k $33RD/d)</th>
              <th>Medium Volume (60k $33RD/d)</th>
              <th>High Volume (250k $33RD/d)</th>
              <th>Net Velocity Regime</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="accent">EPOCH 01</td>
              <td>Day 0 - 14</td>
              <td>6,577 $33RD/day</td>
              <td>+3,637 $33RD/day</td>
              <td class="green">-863 $33RD/day</td>
              <td class="green">-19,863 $33RD/day</td>
              <td class="highlight">Deflationary at Volume &gt; 51.3k</td>
            </tr>
            <tr>
              <td class="accent">EPOCH 12</td>
              <td>Day 154 - 168</td>
              <td>4,332 $33RD/day</td>
              <td>+1,392 $33RD/day</td>
              <td class="green">-3,108 $33RD/day</td>
              <td class="green">-22,108 $33RD/day</td>
              <td class="highlight">Deflationary at Volume &gt; 28.9k</td>
            </tr>
            <tr>
              <td class="accent">EPOCH 24</td>
              <td>Day 322 - 336</td>
              <td>2,854 $33RD/day</td>
              <td>-86 $33RD/day</td>
              <td class="green">-4,586 $33RD/day</td>
              <td class="green">-23,586 $33RD/day</td>
              <td class="highlight">Deflationary at Volume &gt; 14.1k</td>
            </tr>
            <tr>
              <td class="accent">EPOCH 48</td>
              <td>Day 658 - 672</td>
              <td>1,239 $33RD/day</td>
              <td class="green">-1,701 $33RD/day</td>
              <td class="green">-6,201 $33RD/day</td>
              <td class="green">-25,201 $33RD/day</td>
              <td class="highlight">Strictly Deflationary (All Loads)</td>
            </tr>
            <tr>
              <td class="accent">EPOCH 96</td>
              <td>Day 1,330 - 1,344</td>
              <td>233 $33RD/day</td>
              <td class="green">-2,707 $33RD/day</td>
              <td class="green">-7,207 $33RD/day</td>
              <td class="green">-26,207 $33RD/day</td>
              <td class="highlight">Terminal Asymptotic Scarcity</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- SECTION 03: POI EMISSION DECAY SCHEDULE -->
    <section class="ed-section" id="emission-schedule">
      <div class="ed-sec-head">
        <div class="sec-badge-col">
          <span class="sec-giant-num">03</span>
          <span class="sec-kicker">// EMISSION DECAY</span>
        </div>
        <div>
          <h2 class="sec-title">Proof of Inference (PoI) Emission Schedule</h2>
          <p class="sec-summary">
            Hardware compute subsidies are emitted per 14-day epoch according to an immutable exponential decay schedule. Rewards are mathematically apportioned to validators based on delivered compute units, TEE security grade, and quadratic stake dampening.
          </p>
        </div>
      </div>

      <div class="ed-prose-cols">
        <div class="prose-block">
          <h3>Exponential Epoch Decay Function</h3>
          <p>
            Let $k \in \{0, 1, \dots, 95\}$ denote the epoch index. The aggregate token subsidy allocated to epoch $k$ is given by:
          </p>
          <div class="math-display-box">
            $$E(k) = E_0 \cdot \gamma^k$$
          </div>
          <p>
            Where base emission $E_0 = 92,078\text{ }33RD/\text{epoch}$, decay coefficient $\gamma = 0.965$ (a 3.5% reduction per 14-day epoch), and total emission budget $\sum_{k=0}^{\infty} E(k) = 15,000,000\text{ }33RD$.
          </p>
        </div>

        <div class="prose-block">
          <h3>Validator Reward Distribution Algorithm</h3>
          <p>
            Individual validator rewards $R_i$ within epoch $k$ are computed deterministically by the Solana Anchor program:
          </p>
          <div class="math-display-box">
            $$R_i(k) = E(k) \times \frac{CU_i \cdot G_i \cdot L_i \cdot \sqrt{\text{Stake}_i}}{\sum_{j=1}^M CU_j \cdot G_j \cdot L_j \cdot \sqrt{\text{Stake}_j}}$$
          </div>
          <p>
            Where:
          </p>
          <ul class="cell-spec-list" style="border:none; padding:0;">
            <li><span>$CU_i$:</span> <strong>Verified Compute Units delivered</strong></li>
            <li><span>$G_i$:</span> <strong>TEE Security Grade ($1.0$ SGX, $1.2$ TDX/SNP, $1.5$ Hopper CC)</strong></li>
            <li><span>$L_i$:</span> <strong>Liveness Coefficient ($L_i \in [0.0, 1.0]$)</strong></li>
            <li><span>$\sqrt{\text{Stake}_i}$:</span> <strong>Square-root stake weighting (prevents cartelization)</strong></li>
          </ul>
        </div>
      </div>
    </section>

    <!-- SECTION 04: PROTOCOL UTILITY SINKS -->
    <section class="ed-section" id="utility-sinks">
      <div class="ed-sec-head">
        <div class="sec-badge-col">
          <span class="sec-giant-num">04</span>
          <span class="sec-kicker">// VALUE ACCRUAL</span>
        </div>
        <div>
          <h2 class="sec-title">Protocol Utility Sinks &amp; Collateral Locking</h2>
          <p class="sec-summary">
            The $33RD token is not a speculative governance wrapper. It is the mandatory economic fuel and collateral instrument required to interact with every layer of the Singularity compute fabric.
          </p>
        </div>
      </div>

      <!-- 4-COLUMN UTILITY SINKS GRID (ZERO CARDS) -->
      <div class="ed-grid-4">
        <div class="ed-grid-col ed-grid-cell">
          <div>
            <span class="cell-tag">[ SINK 01 // BONDING ]</span>
            <h3 class="cell-title">Validator Collateral</h3>
            <p class="cell-body">
              Every node operator must lock between 1,000 and 100,000 $33RD in an Anchor staking vault PDA to be eligible for Byzantine committee selection and job allocation.
            </p>
          </div>
          <ul class="cell-spec-list">
            <li><span>Circulation Impact:</span> <strong>Removes 3M-8M $33RD</strong></li>
            <li><span>Lock Window:</span> <strong>7-Day Unbonding Cooldown</strong></li>
            <li><span>Slashing Risk:</span> <strong>5% to 100% Forfeiture</strong></li>
          </ul>
        </div>

        <div class="ed-grid-col ed-grid-cell">
          <div>
            <span class="cell-tag">[ SINK 02 // GAS &amp; FEES ]</span>
            <h3 class="cell-title">Inference Execution Gas</h3>
            <p class="cell-body">
              Enterprise users pay for model inference queries in $33RD. 75% routes directly to node operators, 15% to protocol research PDA, and 10% is burned permanently.
            </p>
          </div>
          <ul class="cell-spec-list">
            <li><span>Operator Share:</span> <strong>75% Direct Yield</strong></li>
            <li><span>Protocol Treasury:</span> <strong>15% R&amp;D Vault</strong></li>
            <li><span>Permanent Burn:</span> <strong>10% Incinerator Send</strong></li>
          </ul>
        </div>

        <div class="ed-grid-col ed-grid-cell">
          <div>
            <span class="cell-tag">[ SINK 03 // DISPUTE BONDS ]</span>
            <h3 class="cell-title">Dispute Challenge Bonds</h3>
            <p class="cell-body">
              Challengers initiating interactive bisection disputes against suspect inference logits must post a 5,000 $33RD challenge bond to prevent frivolous denial-of-service attacks.
            </p>
          </div>
          <ul class="cell-spec-list">
            <li><span>Challenge Bond:</span> <strong>5,000 $33RD</strong></li>
            <li><span>Success Reward:</span> <strong>70% of Slashed Stake</strong></li>
            <li><span>Frivolous Penalty:</span> <strong>100% Bond Burned</strong></li>
          </ul>
        </div>

        <div class="ed-grid-col ed-grid-cell">
          <div>
            <span class="cell-tag">[ SINK 04 // GOVERNANCE ]</span>
            <h3 class="cell-title">Quadratic Voting Weight</h3>
            <p class="cell-body">
              Runtime upgrades, TEE hardware classification changes, and grant allocations require stake-locked governance voting weighted quadratically by lock duration.
            </p>
          </div>
          <ul class="cell-spec-list">
            <li><span>Voting Formula:</span> <strong>$\sqrt{\text{Stake} \times \Delta t_{\text{lock}}}$</strong></li>
            <li><span>Max Lockup:</span> <strong>24 Months</strong></li>
            <li><span>Sybil Defense:</span> <strong>Quadratic Dampening</strong></li>
          </ul>
        </div>
      </div>
    </section>

    <!-- SECTION 05: ON-CHAIN CONTRACT ARCHITECTURE -->
    <section class="ed-section" id="onchain-contracts">
      <div class="ed-sec-head">
        <div class="sec-badge-col">
          <span class="sec-giant-num">05</span>
          <span class="sec-kicker">// ON-CHAIN ARCHITECTURE</span>
        </div>
        <div>
          <h2 class="sec-title">Solana Anchor Programs &amp; Verification Registry</h2>
          <p class="sec-summary">
            All token distribution, staking vaults, and burn routing execute on Solana Mainnet-Beta via audited Anchor framework smart contracts. Verification instructions are provided below.
          </p>
        </div>
      </div>

      <!-- PROGRAM TABLE -->
      <div class="ed-table-wrap">
        <table class="ed-table">
          <thead>
            <tr>
              <th>Entity Name</th>
              <th>Solana Program / Account Address</th>
              <th>Program Authority</th>
              <th>Immutable Logic Enforced</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="accent">$33RD Token Mint</td>
              <td class="highlight">33rdxxxx...SPL2022TokenMint</td>
              <td>None (Revoked Permanently)</td>
              <td>Total Supply Capped at 33,333,333 Tokens</td>
            </tr>
            <tr>
              <td class="accent">Canonical Burn Target</td>
              <td class="highlight">1nc1nerator11111111111111111111111111111111</td>
              <td>None (System Incinerator)</td>
              <td>100% LP Tokens Permanently Destroyed</td>
            </tr>
            <tr>
              <td class="accent">PoI Emission Program</td>
              <td class="highlight">CanaryEmission111111111111111111111111111111</td>
              <td>Anchor Emission PDA</td>
              <td>$E(k) = 92,078 \times 0.965^k$ Distribution</td>
            </tr>
            <tr>
              <td class="accent">Validator Staking Vault</td>
              <td class="highlight">CanaryStakeVault1111111111111111111111111111</td>
              <td>Anchor Staking PDA</td>
              <td>7-Day Unbonding Cooldown &amp; Slashing Escrow</td>
            </tr>
            <tr>
              <td class="accent">Protocol Insurance Vault</td>
              <td class="highlight">CanaryInsurance11111111111111111111111111111</td>
              <td>Anchor Governance PDA</td>
              <td>70% Slashed Bond Accumulation for User SLA</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- ON-CHAIN VERIFICATION CLI -->
      <div class="ed-code-block">
        <div class="ed-code-header">
          <span>ON-CHAIN VERIFICATION VIA SOLANA CLI</span>
          <span>BASH // SOLANA MAINNET-BETA</span>
        </div>
        <div class="ed-code-content">
<span class="cmd-comment"># 1. Verify token total supply is strictly 33,333,333 $33RD</span>
<span class="cmd-prompt">$</span>spl-token --url https://api.mainnet-beta.solana.com supply 33rdxxxx...SPL2022TokenMint
<span class="cmd-comment"># Output: 33333333</span>

<span class="cmd-comment"># 2. Verify mint authority has been permanently revoked</span>
<span class="cmd-prompt">$</span>spl-token --url https://api.mainnet-beta.solana.com display 33rdxxxx...SPL2022TokenMint | grep "Mint authority"
<span class="cmd-comment"># Output: Mint authority: (not set) [PERMANENTLY REVOKED]</span>

<span class="cmd-comment"># 3. Verify LP tokens balance at canonical incinerator address</span>
<span class="cmd-prompt">$</span>spl-token --url https://api.mainnet-beta.solana.com accounts --owner 1nc1nerator11111111111111111111111111111111
        </div>
      </div>
    </section>

    <!-- SECTION 06: INTERACTIVE MONETARY POLICY SIMULATOR -->
    <section class="ed-section" id="burn-simulator">
      <div class="ed-sec-head">
        <div class="sec-badge-col">
          <span class="sec-giant-num">06</span>
          <span class="sec-kicker">// SIMULATION ENGINE</span>
        </div>
        <div>
          <h2 class="sec-title">Interactive Burn Velocity &amp; Monetary Simulator</h2>
          <p class="sec-summary">
            Test supply expansion and contraction dynamics by modulating 24-hour network compute volume, validator staking collateral ratio, and epoch decay parameters.
          </p>
        </div>
      </div>

      <div class="calc-matrix-grid">
        <div class="calc-controls">
          <div class="calc-field">
            <label for="sim-epoch">Select Protocol Epoch</label>
            <select id="sim-epoch" onchange="updateTokenSim()">
              <option value="1" selected>Epoch 1 (Day 0 - 14): 6,577 $33RD / day emission</option>
              <option value="12">Epoch 12 (Day 154 - 168): 4,332 $33RD / day emission</option>
              <option value="24">Epoch 24 (Day 322 - 336): 2,854 $33RD / day emission</option>
              <option value="48">Epoch 48 (Day 658 - 672): 1,239 $33RD / day emission</option>
              <option value="96">Epoch 96 (Day 1,330 - 1,344): 233 $33RD / day emission</option>
            </select>
          </div>
          <div class="calc-field">
            <label for="sim-volume">24h Network Compute Volume ($33RD)</label>
            <input type="number" id="sim-volume" value="75000" step="5000" min="0" oninput="updateTokenSim()">
          </div>
          <div class="calc-field">
            <label for="sim-slashing">Daily Slashed Collateral ($33RD)</label>
            <input type="number" id="sim-slashing" value="500" step="100" min="0" oninput="updateTokenSim()">
          </div>
        </div>

        <div class="calc-outputs">
          <div class="out-metric-row">
            <span class="out-metric-lbl">Daily Protocol Burn Rate</span>
            <span class="out-metric-val accent" id="out-burn-day">9,090 $33RD</span>
          </div>
          <div class="out-metric-row">
            <span class="out-metric-lbl">Scheduled Daily Emission</span>
            <span class="out-metric-val" id="out-emission-day">6,577 $33RD</span>
          </div>
          <div class="out-metric-row">
            <span class="out-metric-lbl">Net Daily Supply Change</span>
            <span class="out-metric-val green" id="out-net-supply">-2,513 $33RD</span>
          </div>
          <div class="out-metric-row">
            <span class="out-metric-lbl">Annualized Supply Impact</span>
            <span class="out-metric-val green" id="out-annual-impact">-2.75% Deflationary</span>
          </div>
        </div>
      </div>
    </section>
  </main>

  <script>
    const EPOCH_EMISSIONS = {
      "1": 6577,
      "12": 4332,
      "24": 2854,
      "48": 1239,
      "96": 233
    };

    function updateTokenSim() {
      const epochKey = document.getElementById('sim-epoch').value;
      const volume = parseFloat(document.getElementById('sim-volume').value) || 0;
      const slashed = parseFloat(document.getElementById('sim-slashing').value) || 0;

      const dailyEmission = EPOCH_EMISSIONS[epochKey] || 6577;
      const baseBurnFloor = 1440;
      const volumeBurn = volume * 0.10; // 10% fee burn
      const slashBurn = slashed * 0.30; // 30% incinerated

      const totalDailyBurn = baseBurnFloor + volumeBurn + slashBurn;
      const netDailyChange = dailyEmission - totalDailyBurn;

      const annualChange = netDailyChange * 365;
      const totalCirculating = 33333333;
      const annualPct = ((annualChange / totalCirculating) * 100).toFixed(2);

      document.getElementById('out-burn-day').innerText = Math.round(totalDailyBurn).toLocaleString() + ' $33RD';
      document.getElementById('out-emission-day').innerText = Math.round(dailyEmission).toLocaleString() + ' $33RD';
      
      const netEl = document.getElementById('out-net-supply');
      const annualEl = document.getElementById('out-annual-impact');

      if (netDailyChange <= 0) {
        netEl.innerText = Math.round(netDailyChange).toLocaleString() + ' $33RD';
        netEl.className = 'out-metric-val green';
        annualEl.innerText = Math.abs(annualPct) + '% Deflationary';
        annualEl.className = 'out-metric-val green';
      } else {
        netEl.innerText = '+' + Math.round(netDailyChange).toLocaleString() + ' $33RD';
        netEl.className = 'out-metric-val accent';
        annualEl.innerText = '+' + annualPct + '% Expansionary';
        annualEl.className = 'out-metric-val accent';
      }
    }
    updateTokenSim();
  </script>
"""
    foot = get_page_foot()
    full_html = head + body + foot

    out_path = os.path.join(SITE_DIR, "tokenomics.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    print("tokenomics.html successfully generated!")

if __name__ == "__main__":
    build()
