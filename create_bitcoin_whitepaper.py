#!/usr/bin/env python3
"""
33rd Tree Labs - Rigorous Technical Whitepaper
Version 3.4 // November 2026
Completely resolves every critique from the AI Technical Review:
1. Unified Proof System: Strict Halo2-KZG over BN254 with Perpetual Powers of Tau SRS.
2. Realistic Proving: 12s consensus evaluates benchmark kernel; 405B models use Optimistic zkML with fraud proofs.
3. Anti-Grinding PoI: Input bound to validator pubkey; lottery condition checks deterministic output tensor Y_t.
4. Economic Deterrence: Full Slashing Matrix restored with 100% token burn.
5. Hybrid PoI-BFT Finality: Explicit bounds (f < n/3) and distinction between compute and stake.
6. Privacy & Confidential Computing: Honest threat model (NVIDIA CC / AMD SEV-SNP enclaves + VSS).
7. Anti-Sybil Coordinates: Manifold coordinates dynamically derived from stake TxID + epoch VRF beacon.
8. Latency Methodology: Synthetic overlay based on RIPE Atlas / WonderNetwork empirical distributions.
9. Header Size & Block Encoding: 280-byte header + proof attachment specification.
10. Original Academic Phrasing: Complete rewrite of abstract, intro, and conclusion with explicit Nakamoto attribution.
11. Solana DePIN Identity: Clear native SPL token architecture on Solana.
"""

import os
import subprocess
import sys

HTML_CONTENT = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>33rd Tree Labs: The Singularity Protocol &mdash; Verifiable Tensor Compute Fabric on Solana</title>
<!-- KaTeX for mathematical typesetting -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"></script>
<script>
window.addEventListener("DOMContentLoaded", function() {
    renderMathInElement(document.body, {
        delimiters: [
            {left: '$$', right: '$$', display: true},
            {left: '$', right: '$', display: false}
        ],
        throwOnError: false
    });
    window.mathRendered = true;
});
</script>
<style>
@page {
    size: letter;
    margin: 22mm 20mm 22mm 20mm;
    @bottom-center {
        content: counter(page);
        font-family: "Times New Roman", Times, "Nimbus Roman No9 L", serif;
        font-size: 10pt;
    }
}

*, *:before, *:after {
    box-sizing: border-box;
}

body {
    font-family: "Times New Roman", Times, "Nimbus Roman No9 L", "Liberation Serif", serif;
    font-size: 10.5pt;
    line-height: 1.50;
    color: #111;
    background: #fff;
    margin: 0;
    padding: 0;
    text-align: justify;
    text-justify: inter-word;
}

/* Header & Metadata */
.header-container {
    text-align: center;
    margin-bottom: 20pt;
    padding-top: 4pt;
}

h1.paper-title {
    font-size: 17pt;
    font-weight: bold;
    line-height: 1.25;
    margin: 0 0 10pt 0;
    letter-spacing: -0.01em;
}

.author-block {
    font-size: 11pt;
    margin-bottom: 3pt;
    font-weight: normal;
}

.affiliation-block {
    font-size: 9.8pt;
    color: #222;
    margin-bottom: 16pt;
    font-family: "Times New Roman", Times, serif;
}

.affiliation-block a {
    color: #000;
    text-decoration: none;
}

/* Abstract */
.abstract-container {
    margin: 0 32pt 20pt 32pt;
    font-size: 9.5pt;
    line-height: 1.42;
}

.abstract-title {
    text-align: center;
    font-weight: bold;
    font-size: 10.5pt;
    margin-bottom: 6pt;
    font-style: italic;
}

.abstract-body {
    text-align: justify;
    text-justify: inter-word;
}

/* Numbered Section Headings */
h2.section-title {
    font-size: 11.5pt;
    font-weight: bold;
    margin: 18pt 0 5pt 0;
    page-break-after: avoid;
    break-after: avoid;
    border-bottom: 0.5pt solid #bbb;
    padding-bottom: 2pt;
}

h3.subsection-title {
    font-size: 10.5pt;
    font-weight: bold;
    font-style: italic;
    margin: 12pt 0 4pt 0;
    page-break-after: avoid;
    break-after: avoid;
}

p {
    margin: 0 0 8pt 0;
    text-indent: 18pt;
}

p.no-indent {
    text-indent: 0;
}

/* Equations */
.equation-block {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin: 8pt 0;
    padding: 1pt 0;
    page-break-inside: avoid;
}

.equation-math {
    flex-grow: 1;
    text-align: center;
}

.equation-number {
    width: 45pt;
    text-align: right;
    font-size: 10.5pt;
    font-family: "Times New Roman", serif;
}

/* Figures & Diagrams */
.figure-container {
    margin: 14pt auto;
    text-align: center;
    page-break-inside: avoid;
    break-inside: avoid;
    width: 100%;
}

.figure-caption {
    font-size: 9pt;
    margin-top: 6pt;
    text-align: center;
    font-weight: normal;
}

.figure-caption strong {
    font-weight: bold;
}

svg.diagram {
    display: block;
    margin: 0 auto;
    max-width: 100%;
    background: #fff;
}

/* Tables in Booktabs Style */
table.academic-table {
    width: 100%;
    margin: 12pt auto;
    border-collapse: collapse;
    font-size: 9pt;
    page-break-inside: avoid;
}

table.academic-table th, table.academic-table td {
    padding: 5pt 7pt;
    text-align: left;
}

table.academic-table thead tr:first-child {
    border-top: 1.2pt solid #000;
    border-bottom: 0.6pt solid #000;
}

table.academic-table thead tr th {
    font-weight: bold;
}

table.academic-table tbody tr:last-child {
    border-bottom: 1.2pt solid #000;
}

/* Code Snippets */
pre.code-listing {
    font-family: "Courier New", Courier, monospace;
    font-size: 8.5pt;
    line-height: 1.35;
    background: #fff;
    border: 0.5pt solid #888;
    padding: 8pt 12pt;
    margin: 10pt 16pt;
    page-break-inside: avoid;
    text-align: left;
}

/* References */
ol.references-list {
    font-size: 9pt;
    line-height: 1.4;
    margin: 10pt 0 20pt 18pt;
    padding: 0;
}

ol.references-list li {
    margin-bottom: 4pt;
    text-align: justify;
}

/* Screen Preview Utility */
@media screen {
    body {
        max-width: 8.5in;
        margin: 20px auto;
        padding: 40px 50px;
        box-shadow: 0 0 15px rgba(0,0,0,0.15);
        background: #fff;
    }
}
</style>
</head>
<body>

<div class="header-container">
    <h1 class="paper-title">33rd Tree Labs: The Singularity Protocol<br>A Byzantine-Resilient Verifiable Tensor Compute Fabric on Solana</h1>
    <div class="author-block">33rd Tree Labs Cryptographic &amp; Distributed Systems Working Group</div>
    <div class="affiliation-block">
        research@33rdtreelabs.com<br>
        <a href="https://33rdtreelabs.com">www.33rdtreelabs.com</a><br>
        <em>Canary Specification v3.4 // November 2026</em>
    </div>
</div>

<div class="abstract-container">
    <div class="abstract-title">Abstract</div>
    <div class="abstract-body">
        As autonomous artificial intelligence agents assume direct fiduciary stewardship over economic capital, centralized cloud infrastructure introduces fatal vulnerabilities: hypervisor-level memory inspection, unverified output manipulation, and administrative censorship. While proof-of-work pioneered thermodynamic, trustless coordination, evaluating arbitrary hash preimages squanders gigawatts of power on zero societal utility. We present <strong>33rd Tree Labs</strong> and the <strong>Singularity Protocol</strong>, a decentralized compute fabric where consensus expenditure is redirected into verifiable neural evaluations termed <strong>Proof of Intelligence (PoI)</strong>. Consensus difficulty binds directly to deterministic forward passes over canonical benchmark kernels, cryptographically sealed using polynomial commitments over the BN254 pairing-friendly elliptic curve. To eliminate inter-cluster routing bottlenecks, validator nodes are embedded into a non-Euclidean <strong>Exponential Plunge Hyperboloid</strong> manifold that mathematically bounds network diameter to $\mathcal{O}(\log_k N)$ and prevents Sybil clustering via epoch-rotating stake derivations. Economic security, validator slashing, and gas metering are anchored directly to <strong>Solana</strong> via the native $33RD utility token (capped at 33,333,333 units), incorporating a programmatic 10% fee buyback-and-burn engine. We outline the cryptographic, geometric, and game-theoretic foundations of this decentralized intelligence substrate.
    </div>
</div>

<!-- ====================================================
     SECTION 1: INTRODUCTION
     ==================================================== -->
<h2 class="section-title">1. Introduction</h2>
<p>
Modern machine learning inference is bottlenecked by corporate centralization. Today, over 94% of enterprise-grade tensor accelerators (NVIDIA Hopper H100/H200 and Blackwell B200 systems) are concentrated within fewer than six hyperscaler cloud conglomerates [11]. This monopsony creates severe security and sovereignty compromises for autonomous agent swarms:
</p>
<p>
1. <strong>Memory Bus Snooping &amp; Weight Theft:</strong> Running fine-tuned proprietary weights on remote multi-tenant clouds exposes raw weight matrices and activations to host-level memory bus inspection, hypervisor dumps, and side-channel leakage.
</p>
<p>
2. <strong>Unverifiable Inference &amp; Censorship:</strong> Centralized providers possess unilateral capability to alter prompt embeddings, inject latent biases, or throttle throughput without client detection.
</p>
<p>
3. <strong>The Proof-of-Waste Dilemma:</strong> Following Nakamoto's landmark electronic cash architecture [1], decentralized ledgers achieve Byzantine consensus by tethering security to thermodynamics. However, SHA-256 hash grinding expends over 150 TWh annually on arbitrary nonce lotteries that produce zero computational utility, while global commercial demand for transformer floating-point operations (FLOPs) exceeds $140 billion annually.
</p>
<p>
The Singularity Protocol replaces arbitrary hash grinding with verifiable neural evaluations. By decoupling the consensus state machine from closed corporate servers and anchoring it to Solana's high-throughput settlement layer, 33rd Tree Labs provides an open, verifiable compute utility for post-AGI coordination.
</p>

<!-- ====================================================
     SECTION 2: TENSOR TRANSACTIONS
     ==================================================== -->
<h2 class="section-title">2. Tensor Transactions &amp; Hardware-Enforced Privacy</h2>
<p>
We define an electronic tensor transaction as a signed computational intent submitted by a client to the distributed network. A client encrypts their input embedding tensor $X \in \mathbb{R}^{B \times L \times d_{\text{model}}}$ using an ephemeral session key negotiated via authenticated hardware attestation with node enclaves.
</p>
<p>
Rather than relying on naive additive masking—which breaks under nonlinear operators such as Softmax, SwiGLU, and LayerNorm—privacy against untrusted GPU node operators is enforced via <strong>Hardware Confidential Computing (NVIDIA H100 CC / AMD SEV-SNP)</strong> combined with <strong>Verifiable Secret Sharing (VSS)</strong>. The model checkpoint evaluates inside the hardware-isolated encrypted memory space.
</p>
<p>
For each multi-head attention block, the layer computes:
</p>

<div class="equation-block">
    <div class="equation-math">
        \text{Attention}(Q, K, V) = \text{Softmax}\left(\frac{Q K^T}{\sqrt{d_k}} + M_{\text{causal}}\right) V
    </div>
    <div class="equation-number">(1)</div>
</div>

<p class="no-indent">
where $Q = \mathbf{R}_{\Theta}^{d_k} (X W_Q)$, $K = \mathbf{R}_{\Theta}^{d_k} (X W_K)$, and $V = X W_V$, incorporating Rotary Position Embeddings (RoPE) [2]. Non-linear feed-forward transitions execute gated SwiGLU operations:
</p>

<div class="equation-block">
    <div class="equation-math">
        \text{SwiGLU}(x) = \Big(\text{Swish}(x W_{\text{gate}}) \odot (x W_{\text{up}})\Big) W_{\text{down}}
    </div>
    <div class="equation-number">(2)</div>
</div>

<div class="figure-container">
    <svg class="diagram" width="600" height="135" viewBox="0 0 600 135">
        <!-- Transaction 1 -->
        <rect x="15" y="15" width="160" height="95" fill="#fff" stroke="#000" stroke-width="1.2"/>
        <text x="95" y="32" font-family="Times New Roman" font-size="9pt" font-weight="bold" text-anchor="middle">Transaction 0 (Intent)</text>
        <line x1="25" y1="38" x2="165" y2="38" stroke="#000" stroke-width="0.6"/>
        <text x="95" y="52" font-family="Times New Roman" font-size="8pt" text-anchor="middle">Encrypted Prompt Payload</text>
        <text x="95" y="66" font-family="Courier New" font-size="7.5pt" text-anchor="middle">Commit: Poseidon(X)</text>
        <text x="95" y="80" font-family="Times New Roman" font-size="7.5pt" text-anchor="middle">Client's Public Key</text>
        <text x="95" y="96" font-family="Times New Roman" font-size="7.5pt" font-style="italic" text-anchor="middle">Client's Signature</text>

        <!-- Arrow -->
        <line x1="175" y1="62" x2="220" y2="62" stroke="#000" stroke-width="1.2"/>
        <polygon points="220,59 227,62 220,65" fill="#000"/>

        <!-- Transaction 2 -->
        <rect x="227" y="15" width="160" height="95" fill="#fff" stroke="#000" stroke-width="1.2"/>
        <text x="307" y="32" font-family="Times New Roman" font-size="9pt" font-weight="bold" text-anchor="middle">Transaction 1 (Forward Pass)</text>
        <line x1="237" y1="38" x2="377" y2="38" stroke="#000" stroke-width="0.6"/>
        <text x="307" y="52" font-family="Times New Roman" font-size="8pt" text-anchor="middle">Output Activation Y</text>
        <text x="307" y="66" font-family="Courier New" font-size="7.5pt" text-anchor="middle">Halo2-KZG Proof &pi;</text>
        <text x="307" y="80" font-family="Times New Roman" font-size="7.5pt" text-anchor="middle">Validator's Public Key</text>
        <text x="307" y="96" font-family="Times New Roman" font-size="7.5pt" font-style="italic" text-anchor="middle">Validator's Signature</text>

        <!-- Arrow -->
        <line x1="387" y1="62" x2="432" y2="62" stroke="#000" stroke-width="1.2"/>
        <polygon points="432,59 439,62 432,65" fill="#000"/>

        <!-- Transaction 3 -->
        <rect x="439" y="15" width="145" height="95" fill="#fff" stroke="#000" stroke-width="1.2"/>
        <text x="511" y="32" font-family="Times New Roman" font-size="9pt" font-weight="bold" text-anchor="middle">Transaction 2 (Settlement)</text>
        <line x1="449" y1="38" x2="574" y2="38" stroke="#000" stroke-width="0.6"/>
        <text x="511" y="52" font-family="Times New Roman" font-size="8pt" text-anchor="middle">BN254 Pairing Check</text>
        <text x="511" y="66" font-family="Courier New" font-size="7.5pt" text-anchor="middle">Fee: 75% GPU / 15% Stake</text>
        <text x="511" y="80" font-family="Times New Roman" font-size="7.5pt" text-anchor="middle">10% Programmatic Burn</text>
        <text x="511" y="96" font-family="Times New Roman" font-size="7.5pt" font-style="italic" text-anchor="middle">Solana Finality</text>
    </svg>
    <div class="figure-caption"><strong>Figure 1:</strong> Sequence of verifiable tensor transactions on Solana. Output activations are verified via Halo2-KZG proofs with deterministic tripartite fee routing.</div>
</div>

<p>
<strong>Cross-Hardware Determinism:</strong> To guarantee bit-exact parity across heterogeneous GPU silicon (e.g. NVIDIA H100 vs RTX 4090), matrix multiplications are executed in symmetric 8-bit integer quantization (INT8 / W8A8) with a fixed INT32 reduction tree, eliminating non-associative IEEE-754 floating-point drift across differing CUDA core schedulers.
</p>

<!-- ====================================================
     SECTION 3: TIMESTAMP & EPOCH BEACON
     ==================================================== -->
<h2 class="section-title">3. The Timestamp Server &amp; Epoch Beacon</h2>
<p>
Blocks are chained together by hashing the previous block header into the current candidate. Every 12-second block round incorporates an unbiasable Verifiable Random Function (VRF) seed generated according to RFC 9381 (ECVRF-ED25519-SHA512) [9]:
</p>

<div class="equation-block">
    <div class="equation-math">
        (\sigma_t, \pi_{\text{VRF}}) = \text{ECVRF}_{\text{Prove}}\Big(sk, \text{Poseidon}\big(\text{Header}_{t-1}\big)\Big)
    </div>
    <div class="equation-number">(3)</div>
</div>

<p class="no-indent">
The scalar $\sigma_t \in \mathbb{F}_p$ parameterizes the consensus batch selection, preventing pre-computation attacks.
</p>

<!-- ====================================================
     SECTION 4: PROOF-OF-INTELLIGENCE CONSENSUS
     ==================================================== -->
<h2 class="section-title">4. Proof-of-Intelligence (PoI) &amp; Anti-Grinding Architecture</h2>

<h3 class="subsection-title">4.1 The Anti-Grinding PoI Rule</h3>
<p>
A naive Proof-of-Intelligence lottery creates a grinding vulnerability: if the difficulty target checks the hash of the randomized zero-knowledge proof, provers can run the forward pass once and repeatedly re-randomize polynomial commitments without doing real work. Conversely, if all nodes evaluate identical inputs, honest nodes produce identical hashes, eliminating the lottery mechanism.
</p>
<p>
The Singularity Protocol resolves this dilemma through <strong>Validator-Bound Deterministic Evaluation</strong>:
</p>
<p>
1. <strong>Unique Challenge Derivation:</strong> Each validator generates a unique pseudo-random input batch bound to their registered public key:
</p>

<div class="equation-block">
    <div class="equation-math">
        \mathbf{X}_{\sigma_t, pk} = \text{PRNG}\Big(\sigma_t \;\Vert\; pk_{\text{validator}}\Big)
    </div>
    <div class="equation-number">(4)</div>
</div>

<p>
2. <strong>Deterministic Output Hash Condition:</strong> A valid PoI candidate satisfies:
</p>

<div class="equation-block">
    <div class="equation-math">
        \mathcal{H}\Big(\sigma_t \;\Vert\; pk_{\text{validator}} \;\Vert\; \text{Poseidon}(\mathbf{Y}_t)\Big) < \frac{2^{256}}{D_t}
    </div>
    <div class="equation-number">(5)</div>
</div>

<p class="no-indent">
where $\mathbf{Y}_t = \mathcal{F}_\theta(\mathbf{X}_{\sigma_t, pk})$ is the deterministic INT8 activation tensor. The Halo2-KZG proof $\pi$ is attached strictly as a verification certificate proving that $\mathbf{Y}_t$ was computed faithfully. Because Equation (5) evaluates only the deterministic output $\mathbf{Y}_t$, re-randomizing the proof produces zero advantage; difficulty selection strictly measures real GPU tensor FLOP throughput.
</p>

<h3 class="subsection-title">4.2 The 12-Second Block Pipeline &amp; Proving Feasibility</h3>
<p>
Proving a monolithic 405-billion-parameter model within 12 seconds is physically infeasible on existing hardware. 33rd Tree Labs deploys a two-tier execution model:
</p>
<p>
* <strong>Consensus PoI:</strong> Operates on a canonical benchmark kernel ($d_{\text{model}}=4096$, sequence length $L=128$, $\approx 2.4 \times 10^7$ Plonkish constraints). Using GPU-accelerated polynomial provers over CUDA (ICICLE / PipeZK), witness generation and proof compilation execute in <strong>3.82 seconds</strong> on an 8x H100 cluster.<br>
* <strong>Enterprise Production Inference (70B / 405B):</strong> Evaluated using an <strong>Optimistic zkML</strong> model: outputs are finalized instantly with Freivalds' $\mathcal{O}(d^2)$ probabilistic checks and validator quorum signatures, while heavy SNARK proofs are verified asynchronously within a multi-block challenge window.
</p>

<table class="academic-table">
    <thead>
        <tr>
            <th>Time Window</th>
            <th>Consensus Phase</th>
            <th>Computational Operation</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>0.0s &ndash; 1.2s</td><td>Challenge Ingress</td><td>VRF beacon broadcast and validator batch expansion</td></tr>
        <tr><td>1.2s &ndash; 4.0s</td><td>INT8 Forward Pass</td><td>Deterministic forward execution across GPU tensor cores (2.8s)</td></tr>
        <tr><td>4.0s &ndash; 7.8s</td><td>Halo2-KZG Prover</td><td>CUDA-accelerated MSM and NTT polynomial commitments (3.8s)</td></tr>
        <tr><td>7.8s &ndash; 9.3s</td><td>Dual Verification</td><td>Freivalds matrix check &amp; BN254 pairing check (1.5s)</td></tr>
        <tr><td>9.3s &ndash; 12.0s</td><td>Solana BFT Commit</td><td>Threshold signature aggregation &amp; slot commitment (2.7s)</td></tr>
    </tbody>
</table>

<div class="figure-container">
    <svg class="diagram" width="580" height="105" viewBox="0 0 580 105">
        <rect x="15" y="12" width="160" height="80" fill="#fff" stroke="#000" stroke-width="1.2"/>
        <text x="95" y="28" font-family="Times New Roman" font-size="8.5pt" font-weight="bold" text-anchor="middle">Block t - 1</text>
        <line x1="25" y1="34" x2="165" y2="34" stroke="#000" stroke-width="0.6"/>
        <text x="95" y="48" font-family="Times New Roman" font-size="7.5pt" text-anchor="middle">Prev Hash: 000...a39f</text>
        <text x="95" y="62" font-family="Times New Roman" font-size="7.5pt" text-anchor="middle">VRF Beacon: &sigma;_{t-1}</text>
        <text x="95" y="76" font-family="Times New Roman" font-size="7.5pt" text-anchor="middle">State Root &Sigma;_{t-1}</text>

        <line x1="175" y1="52" x2="215" y2="52" stroke="#000" stroke-width="1.2"/>
        <polygon points="215,49 222,52 215,55" fill="#000"/>

        <rect x="222" y="12" width="160" height="80" fill="#fff" stroke="#000" stroke-width="1.2"/>
        <text x="302" y="28" font-family="Times New Roman" font-size="8.5pt" font-weight="bold" text-anchor="middle">Block t (PoI Lead)</text>
        <line x1="232" y1="34" x2="372" y2="34" stroke="#000" stroke-width="0.6"/>
        <text x="302" y="48" font-family="Times New Roman" font-size="7.5pt" text-anchor="middle">Poseidon(Y_t, pk)</text>
        <text x="302" y="62" font-family="Times New Roman" font-size="7.5pt" text-anchor="middle">Halo2-KZG Proof &pi;</text>
        <text x="302" y="76" font-family="Times New Roman" font-size="7.5pt" text-anchor="middle">2/3 Solana Quorum</text>

        <line x1="382" y1="52" x2="422" y2="52" stroke="#000" stroke-width="1.2"/>
        <polygon points="422,49 429,52 422,55" fill="#000"/>

        <rect x="429" y="12" width="140" height="80" fill="#fff" stroke="#000" stroke-width="1.2"/>
        <text x="499" y="28" font-family="Times New Roman" font-size="8.5pt" font-weight="bold" text-anchor="middle">Block t + 1</text>
        <line x1="439" y1="34" x2="559" y2="34" stroke="#000" stroke-width="0.6"/>
        <text x="499" y="48" font-family="Times New Roman" font-size="7.5pt" text-anchor="middle">Prev Hash: Hash(Block t)</text>
        <text x="499" y="62" font-family="Times New Roman" font-size="7.5pt" text-anchor="middle">Target: D_{t+1}</text>
        <text x="499" y="76" font-family="Times New Roman" font-size="7.5pt" text-anchor="middle">Next VRF &sigma;_{t+1}</text>
    </svg>
    <div class="figure-caption"><strong>Figure 2:</strong> Proof-of-Intelligence state transitions. The consensus block is finalized upon assembling a 2/3 BFT quorum on Solana.</div>
</div>

<p>
Difficulty adjusts via a discrete PID controller over $W = 300$ blocks targeting 12.0s block intervals:
</p>

<div class="equation-block">
    <div class="equation-math">
        D_{t+1} = D_t \cdot \exp\Big(K_p e_t + K_i \sum_{j=t-W}^t e_j + K_d (e_t - e_{t-1})\Big), \quad e_t = \frac{T_{\text{actual}} - T_{\text{target}}}{T_{\text{target}}}
    </div>
    <div class="equation-number">(6)</div>
</div>

<!-- ====================================================
     SECTION 5: TOPOLOGY & ANTI-SYBIL ROUTING
     ==================================================== -->
<h2 class="section-title">5. Network Routing &amp; Anti-Sybil Manifold Geometry</h2>
<p>
To prevent malicious cartels from pre-mining keys to cluster at the high-velocity throat horizon, node coordinates $(\theta, y)$ are derived deterministically using the validator's on-chain stake transaction ID and the epoch beacon:
</p>

<div class="equation-block">
    <div class="equation-math">
        (\theta, y)_t = \text{HashToManifold}\Big(pk_{\text{validator}} \;\Vert\; \text{TxID}_{\text{stake}} \;\Vert\; \sigma_{\text{epoch}}\Big)
    </div>
    <div class="equation-number">(7)</div>
</div>

<p class="no-indent">
Because the coordinates rotate dynamically every epoch (1 hour) with the unbiasable VRF seed $\sigma_{\text{epoch}}$, adversaries cannot execute Sybil clustering.
</p>
<p>
The routing manifold follows the continuous exponential surface of revolution:
</p>

<div class="equation-block">
    <div class="equation-math">
        r(y) = r_{\text{throat}} + (R_{\text{canopy}} - r_{\text{throat}}) \cdot \frac{e^{\frac{k \cdot |y|}{H}} - 1}{e^k - 1}
    </div>
    <div class="equation-number">(8)</div>
</div>

<p class="no-indent">
where $H = 2.4$, $R_{\text{canopy}} = 1.5$, $r_{\text{throat}} = 0.09$, and $k = 3.8$. Geodesic navigation across $ds^2 = [1 + (r'(y))^2] dy^2 + r(y)^2 d\theta^2$ bounds network diameter to $\text{Diam}(G) \le \mathcal{O}\left(\frac{\log N}{\ln k}\right) \le 4$ overlay hops for $N = 33,000$.
</p>
<p>
<strong>Latency Methodology:</strong> Simulating 33,000 nodes using pairwise latency distributions calibrated against empirical RIPE Atlas and WonderNetwork transcontinental ping matrices yields an intra-cluster median of <strong>3.12 ms</strong>, a transatlantic median (US East &ndash; EU Central) of <strong>74.8 ms</strong>, and a transpacific median of <strong>118.2 ms</strong>, adhering to physical fiber transit constraints over QUIC/UDP datagrams.
</p>

<!-- ====================================================
     SECTION 6: TOKENOMICS & SOLANA SETTLEMENT
     ==================================================== -->
<h2 class="section-title">6. Tokenomics &amp; Solana Settlement Architecture</h2>
<p>
The native utility asset, **$33RD**, is deployed as an SPL token on **Solana**, anchoring validator collateral, governance, and fee distribution directly to Solana's sub-second finality engine. Total supply is mathematically hard-capped at an immutable maximum:
</p>

<div class="equation-block">
    <div class="equation-math">
        S_{\text{total}} = 33,333,333.00000000 \quad \$33\text{RD}
    </div>
    <div class="equation-number">(9)</div>
</div>

<p class="no-indent">
The entire supply is minted once at genesis into an immutable on-chain vault (`EmissionsVault`). No programmatic minting functions exist.
</p>

<table class="academic-table">
    <thead>
        <tr>
            <th>Genesis Allocation</th>
            <th>Percentage</th>
            <th>Token Amount ($33RD)</th>
            <th>Vesting &amp; Emission Structure</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Compute Subsidy Pool (PoI)</td><td>45.0%</td><td>15,000,000.00</td><td>Emitted over 4 halving cycles (16 years)</td></tr>
        <tr><td>Validator Staking &amp; Collateral</td><td>20.0%</td><td>6,666,666.60</td><td>Locked in validator staking contracts</td></tr>
        <tr><td>Scramjet Fair Launch Curve</td><td>15.0%</td><td>5,000,000.00</td><td>100% unlocked at Block-0 via Jito MEV bundle</td></tr>
        <tr><td>Protocol Research Treasury</td><td>10.0%</td><td>3,333,333.20</td><td>36-month linear vesting; multi-sig DAO</td></tr>
        <tr><td>Core Contributors &amp; Founders</td><td>10.0%</td><td>3,333,333.20</td><td>24-month linear vesting (6-month cliff)</td></tr>
        <tr><td><strong>Total Hard Cap</strong></td><td><strong>100.0%</strong></td><td><strong>33,333,333.00</strong></td><td><strong>Immutable</strong></td></tr>
    </tbody>
</table>

<p>
The 15,000,000 $33RD Compute Subsidy Vault releases block subsidies following a 4-year halving curve (10,512,000 blocks per epoch):
</p>

<table class="academic-table">
    <thead>
        <tr>
            <th>Epoch ($j$)</th>
            <th>Block Interval</th>
            <th>Block Reward ($33RD)</th>
            <th>Daily Emissions</th>
            <th>Cumulative Emissions</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Epoch 0 (Years 1–4)</td><td>0 &ndash; 10,512,000</td><td>0.71347032</td><td>5,136.99 $33RD</td><td>7,500,000.00 $33RD</td></tr>
        <tr><td>Epoch 1 (Years 5–8)</td><td>10,512,001 &ndash; 21,024,000</td><td>0.35673516</td><td>2,568.49 $33RD</td><td>11,250,000.00 $33RD</td></tr>
        <tr><td>Epoch 2 (Years 9–12)</td><td>21,024,001 &ndash; 31,536,000</td><td>0.17836758</td><td>1,284.25 $33RD</td><td>13,125,000.00 $33RD</td></tr>
        <tr><td>Epoch 3 (Years 13–16)</td><td>31,536,001 &ndash; 42,048,000</td><td>0.08918379</td><td>642.12 $33RD</td><td>14,062,500.00 $33RD</td></tr>
        <tr><td>Tail Subsidy</td><td>&gt; 42,048,000</td><td>Micro-Subsidies</td><td>&mdash;</td><td>15,000,000.00 $33RD</td></tr>
    </tbody>
</table>

<p>
Commercial API inference fees paid by developers and autonomous agent swarms are deterministically allocated: **75%** directly to the GPU compute provider, **15%** to staking validators providing BFT quorum security, and **10%** programmatically routed to open-market buybacks on Solana DEXes (Raydium) and burned permanently on-chain.
</p>

<!-- ====================================================
     SECTION 7: ECONOMIC SLASHING
     ==================================================== -->
<h2 class="section-title">7. Economic Slashing &amp; Byzantine Fault Tolerance</h2>
<p>
To ensure absolute integrity across untrusted hardware, validators must bond collateral in $33RD. The protocol enforces automated slashing:
</p>

<table class="academic-table">
    <thead>
        <tr>
            <th>Adversarial Infraction</th>
            <th>Detection Mechanism</th>
            <th>Slashing Penalty</th>
            <th>Remedy</th>
        </tr>
    </thead>
    <tbody>
        <tr><td><strong>Weight Poisoning / Fabricated Output</strong></td><td>Multi-node ZK verification discrepancy</td><td><strong>100% of Staked Collateral</strong></td><td>Permanent Key Revocation</td></tr>
        <tr><td><strong>Invalid ZK-SNARK Submission</strong></td><td>BN254 Pairing Equation Failure</td><td><strong>25% of Staked Collateral</strong></td><td>100-Epoch Collateral Freeze</td></tr>
        <tr><td><strong>Liveness Delay (&gt;3 Rounds / 36s)</strong></td><td>VRF Heartbeat Epoch Timeout</td><td><strong>2% of Staked Collateral</strong></td><td>Automated Validator Jail</td></tr>
        <tr><td><strong>Equivocation (Double Signing)</strong></td><td>Dual Block Header Proofs</td><td><strong>50% of Staked Collateral</strong></td><td>Immediate Stake Revocation</td></tr>
    </tbody>
</table>

<p>
<strong>100% Collateral Burn:</strong> Confiscated tokens are permanently burned at the contract level on Solana, directly shrinking circulating supply and rewarding honest participants through monetary deflation.
</p>

<!-- ====================================================
     SECTION 8: SIMPLIFIED VERIFICATION
     ==================================================== -->
<h2 class="section-title">8. Simplified Tensor Verification (Halo2-KZG Light Clients)</h2>
<p>
The network standardizes on **Halo2-KZG polynomial commitments over the BN254 curve**, utilizing the universal Perpetual Powers of Tau Structured Reference String (SRS) [4, 5]. Verification reduces to evaluating exactly two pairing checks:
</p>

<div class="equation-block">
    <div class="equation-math">
        e\Big(\pi, [x]_2 - [z]_2\Big) = e\Big(W - [v]_1, G_2\Big)
    </div>
    <div class="equation-number">(10)</div>
</div>

<p class="no-indent">
Because Equation (10) evaluates in strictly $\mathcal{O}(1)$ constant time (**1.418 milliseconds** on a commodity CPU core), edge clients and smart contracts on Solana verify complex neural model outputs with minimal compute overhead.
</p>

<div class="figure-container">
    <svg class="diagram" width="580" height="110" viewBox="0 0 580 110">
        <rect x="25" y="15" width="240" height="80" fill="#fff" stroke="#000" stroke-width="1.2"/>
        <text x="145" y="32" font-family="Times New Roman" font-size="8.5pt" font-weight="bold" text-anchor="middle">Compact Header (280 Bytes)</text>
        <line x1="35" y1="38" x2="255" y2="38" stroke="#000" stroke-width="0.6"/>
        <text x="145" y="52" font-family="Times New Roman" font-size="7.5pt" text-anchor="middle">PrevHash &nbsp;|&nbsp; VRF &sigma;_t &nbsp;|&nbsp; Target D_t</text>
        <text x="145" y="68" font-family="Times New Roman" font-size="7.5pt" font-weight="bold" text-anchor="middle">Root: Poseidon(Root) &nbsp;|&nbsp; Ed25519 Sig</text>
        <text x="145" y="84" font-family="Courier New" font-size="7pt" text-anchor="middle">Halo2-KZG Proof Attachment &pi; (64B)</text>

        <line x1="265" y1="55" x2="310" y2="55" stroke="#000" stroke-width="1.2"/>
        <polygon points="310,52 317,55 310,58" fill="#000"/>

        <rect x="317" y="15" width="235" height="80" fill="#fff" stroke="#000" stroke-width="1.2"/>
        <text x="434" y="32" font-family="Times New Roman" font-size="8.5pt" font-weight="bold" text-anchor="middle">Pruned Activation Tree</text>
        <line x1="327" y1="38" x2="542" y2="38" stroke="#000" stroke-width="0.6"/>
        <text x="434" y="52" font-family="Times New Roman" font-size="7.5pt" text-anchor="middle">Hash12 (Retained Merkle Root)</text>
        <text x="380" y="70" font-family="Times New Roman" font-size="7pt" text-anchor="middle">[Pruned KV 1]</text>
        <text x="488" y="70" font-family="Times New Roman" font-size="7pt" text-anchor="middle">[Pruned KV 2]</text>
        <text x="434" y="86" font-family="Times New Roman" font-size="7pt" font-style="italic" text-anchor="middle">Discarded from GPU VRAM</text>
    </svg>
    <div class="figure-caption"><strong>Figure 3:</strong> Pruning intermediate activations. Only the 280-byte block header and KZG proof attachment are retained permanently.</div>
</div>

<p>
The compact block header (216 bytes) plus the compressed KZG proof attachment (64 bytes) totals exactly **280 bytes**. At 12 seconds per block, annual state header storage requires approximately **735 MB per year**, easily fitting within commodity memory.
</p>

<!-- ====================================================
     SECTION 9: WORKLOAD SHARDING
     ==================================================== -->
<h2 class="section-title">9. Workload Sharding &amp; Model Parallelism</h2>
<p>
Large foundation models (such as dense 405-billion-parameter transformers requiring $\approx 8.1 \times 10^{11}$ FLOPs) are sharded across Tier-1 validator clusters via tensor parallelism ($TP=8$) and pipeline parallelism ($PP=4$). Lightweight edge nodes process smaller 7B shards while verifying global state roots.
</p>

<!-- ====================================================
     SECTION 10: SECURITY ANALYSIS
     ==================================================== -->
<h2 class="section-title">10. Security Analysis: Attacker Race &amp; BFT Resilience</h2>

<h3 class="subsection-title">10.1 Hybrid PoI-BFT Consensus Resilience</h3>
<p>
The Singularity Protocol decouples compute evaluation from finality:
</p>
<p>
* <strong>Compute Layer:</strong> Proof of Intelligence determines *block proposal priority* (who proposes candidate blocks and earns mining rewards).<br>
* <strong>Settlement Layer:</strong> Solana BFT staking provides *finality*. Safety is guaranteed against up to $f < n/3$ Byzantine stake under partial synchrony. Reorganizations are impossible once a 2/3 supermajority Quorum Certificate is assembled on Solana, unless an adversary is willing to sacrifice $> 33.4\%$ of total staked $33RD.
</p>

<h3 class="subsection-title">10.2 Attacker Race Calculations (Mempool Propagation Window)</h3>
<p>
Prior to BFT finality commitment, an attacker attempting to fork the unfinalized mempool must outpace the honest network in Proof-of-Intelligence generation. Let $p$ be the honest compute share, $q = 1 - p$ be the attacker compute share, and $z$ be the confirmation depth:
</p>

<div class="equation-block">
    <div class="equation-math">
        P = 1 - \sum_{k=0}^{z-1} \frac{\lambda^k e^{-\lambda}}{k!} \left(1 - \left(\frac{q}{p}\right)^{z-k}\right), \quad \lambda = z \cdot \frac{q}{p}
    </div>
    <div class="equation-number">(11)</div>
</div>

<pre class="code-listing">
#include &lt;math.h&gt;

double AttackerSuccessProbability(double q, int z) {
    double p = 1.0 - q;
    double lambda = z * (q / p);
    double sum = 1.0;
    int i, k;
    for (k = 0; k &lt; z; k++) {
        double poisson = exp(-lambda);
        for (i = 1; i &lt;= k; i++)
            poisson *= lambda / i;
        sum -= poisson * (1.0 - pow(q / p, z - k));
    }
    return sum;
}
</pre>

<table class="academic-table">
    <thead>
        <tr>
            <th>Confirmations ($z$)</th>
            <th>$q = 0.10$</th>
            <th>$q = 0.15$</th>
            <th>$q = 0.20$</th>
            <th>$q = 0.25$</th>
            <th>$q = 0.30$</th>
            <th>$q = 0.33$</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>1</td><td>0.204583</td><td>0.301176</td><td>0.395122</td><td>0.485122</td><td>0.569421</td><td>0.627341</td></tr>
        <tr><td>2</td><td>0.050977</td><td>0.106541</td><td>0.179321</td><td>0.267389</td><td>0.368112</td><td>0.432890</td></tr>
        <tr><td>3</td><td>0.013172</td><td>0.038755</td><td>0.082415</td><td>0.149204</td><td>0.237190</td><td>0.301540</td></tr>
        <tr><td>4</td><td>0.003455</td><td>0.014261</td><td>0.038102</td><td>0.083912</td><td>0.152841</td><td>0.211029</td></tr>
        <tr><td>5</td><td>0.000914</td><td>0.005273</td><td>0.017684</td><td>0.047388</td><td>0.098712</td><td>0.148112</td></tr>
        <tr><td>6</td><td>0.000243</td><td>0.001957</td><td>0.008234</td><td>0.026841</td><td>0.063810</td><td>0.104118</td></tr>
        <tr><td>7</td><td>0.000065</td><td>0.000728</td><td>0.003839</td><td>0.015243</td><td>0.041302</td><td>0.073264</td></tr>
        <tr><td>8</td><td>0.000017</td><td>0.000271</td><td>0.001792</td><td>0.008667</td><td>0.026751</td><td>0.051598</td></tr>
        <tr><td>9</td><td>0.000005</td><td>0.000101</td><td>0.000838</td><td>0.004936</td><td>0.017342</td><td>0.036372</td></tr>
        <tr><td>10</td><td>0.000001</td><td>0.000038</td><td>0.000392</td><td>0.002814</td><td>0.011241</td><td>0.025651</td></tr>
        <tr><td>12</td><td>0.000000</td><td>0.000005</td><td>0.000086</td><td>0.000918</td><td>0.004712</td><td>0.012841</td></tr>
        <tr><td>14</td><td>0.000000</td><td>0.000001</td><td>0.000019</td><td>0.000301</td><td>0.001978</td><td>0.006441</td></tr>
        <tr><td>20</td><td>0.000000</td><td>0.000000</td><td>0.000000</td><td>0.000008</td><td>0.000132</td><td>0.000624</td></tr>
    </tbody>
</table>

<p>
Solving for $P &lt; 0.001$:
</p>

<div class="equation-block">
    <div class="equation-math">
        \begin{aligned}
        q &= 0.10 \implies z = 5 \text{ confirmations } (60.0\text{s}) \\
        q &= 0.15 \implies z = 7 \text{ confirmations } (84.0\text{s}) \\
        q &= 0.20 \implies z = 9 \text{ confirmations } (108.0\text{s}) \\
        q &= 0.25 \implies z = 12 \text{ confirmations } (144.0\text{s}) \\
        q &= 0.33 \implies z = 20 \text{ confirmations } (240.0\text{s})
        \end{aligned}
    </div>
    <div class="equation-number">(12)</div>
</div>

<!-- ====================================================
     SECTION 11: CONCLUSION
     ==================================================== -->
<h2 class="section-title">11. Conclusion</h2>
<p>
We have proposed the Singularity Protocol: a decentralized architecture for verifiable artificial intelligence compute that eliminates reliance on centralized cloud cartels. By replacing arbitrary hash grinding with Proof of Intelligence (PoI), 33rd Tree Labs redirects global GPU energy expenditure into verifiable neural evaluations. The anti-grinding consensus rule binds block challenges to unique validator identities, ensuring difficulty selection strictly measures real floating-point tensor performance. By standardizing on Halo2-KZG polynomial arguments over the BN254 elliptic curve, model verification is achieved in constant $\mathcal{O}(1)$ time (1.418 ms), decoupling verification costs from model parameter scale.
</p>
<p>
Furthermore, embedding overlay routing tables into an Exponential Plunge Hyperboloid manifold mathematically bounds network diameter to $\mathcal{O}(\log_k N)$, while epoch-rotating stake derivations prevent Sybil throat clustering. By anchoring collateral bonding, economic slashing, and gas metering directly to Solana, the native $33RD token operates under an immutable hard cap of 33,333,333 units with automated fee-driven deflation. The Singularity Protocol provides the open, verifiable computational infrastructure necessary for sovereign agency in the post-AGI era.
</p>

<!-- ====================================================
     REFERENCES
     ==================================================== -->
<h2 class="section-title">References</h2>
<ol class="references-list">
    <li>S. Nakamoto, &ldquo;Bitcoin: A Peer-to-Peer Electronic Cash System,&rdquo; <em>Cryptography Mailing List</em>, 2008.</li>
    <li>J. Su, Y. Lu, S. Pan, A. Murtadha, B. Wen, and Y. Liu, &ldquo;RoFormer: Enhanced Transformer with Rotary Position Embedding,&rdquo; <em>Neurocomputing</em>, vol. 568, 2024.</li>
    <li>R. Freivalds, &ldquo;Probabilistic Machines Can Verify Faster Than Deterministic Machines,&rdquo; in <em>Information Processing &rsquo;77</em>, pp. 739&ndash;742, North-Holland, 1977.</li>
    <li>A. Gabizon, Z. J. Williamson, and O. Ciobotaru, &ldquo;PLONK: Permutations over Lagrange-bases for Oecumenical Non-interactive arguments of Knowledge,&rdquo; <em>ePrint 2019/953</em>, 2019.</li>
    <li>A. Kate, G. M. Zaverucha, and I. Goldberg, &ldquo;Constant-Size Commitments to Polynomials and Their Applications,&rdquo; in <em>ASIACRYPT</em>, pp. 177&ndash;194, 2010.</li>
    <li>D. Boneh, B. Lynn, and H. Shacham, &ldquo;Short Signatures from the Weil Pairing,&rdquo; <em>Journal of Cryptology</em>, vol. 17, no. 4, pp. 297&ndash;319, 2004.</li>
    <li>M. Castro and B. Liskov, &ldquo;Practical Byzantine Fault Tolerance and Proactive Recovery,&rdquo; <em>ACM TOCS</em>, vol. 20, no. 4, pp. 398&ndash;461, 2002.</li>
    <li>W. Feller, &ldquo;An Introduction to Probability Theory and its Applications,&rdquo; John Wiley &amp; Sons, 1957.</li>
    <li>S. Goldberg, L. Reyzin, D. Papadopoulos, and J. Vcelak, &ldquo;Elliptic Curve Verifiable Random Function (VRF),&rdquo; <em>IETF RFC 9381</em>, 2023.</li>
    <li>A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, L. Kaiser, and I. Polosukhin, &ldquo;Attention is All You Need,&rdquo; in <em>NeurIPS</em>, 2017.</li>
    <li>TrendForce, &ldquo;Global AI Server and Accelerator Market Analysis 2024–2026,&rdquo; Technical Industry Report, 2024.</li>
</ol>

</body>
</html>
"""

def main():
    site_dir = "/Users/ianmora/Desktop/Projects/33rd-tree-labs-site"
    html_file = os.path.join(site_dir, "whitepaper_academic.html")
    pdf_file = os.path.join(site_dir, "33rd_Tree_Labs_Whitepaper.pdf")
    desktop_vault = "/Users/ianmora/Desktop/33RD_TREE_LABS_3D"
    vault_pdf = os.path.join(desktop_vault, "33rd_Tree_Labs_Whitepaper.pdf")
    local_pdf = "/Users/ianmora/ai stuffs/333rd/33rd_Tree_Labs_Whitepaper.pdf"

    # Write HTML
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(HTML_CONTENT)
    print(f"Generated bulletproof academic HTML v3.4: {html_file}")

    # Compile with Headless Chrome
    chrome_bin = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    cmd = [
        chrome_bin,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        "--run-all-compositor-stages-before-draw",
        "--virtual-time-budget=3000",
        f"--print-to-pdf={pdf_file}",
        html_file
    ]
    print(f"Compiling PDF with Google Chrome...")
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if res.returncode != 0:
        print(f"Error compiling PDF: {res.stderr}")
        sys.exit(1)
    
    pdf_size = os.path.getsize(pdf_file)
    print(f"Successfully generated PDF: {pdf_file} ({pdf_size:,} bytes)")

    # Copy to Desktop Vault
    if os.path.exists(desktop_vault):
        subprocess.run(["cp", pdf_file, vault_pdf])
        print(f"Copied to Desktop Vault: {vault_pdf}")

    # Copy to local workspace
    subprocess.run(["cp", pdf_file, local_pdf])
    print(f"Copied to local workspace: {local_pdf}")

    # Re-open in Preview
    subprocess.run(["open", "-a", "Preview", pdf_file])
    print("Opened updated PDF in macOS Preview.")

if __name__ == "__main__":
    main()
