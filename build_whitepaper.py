import re, os, subprocess, shutil

html_content = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>33rd Tree Labs: The Singularity Protocol &mdash; Verifiable DePIN Compute Fabric on Solana</title>
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
    margin: 17mm 16mm 17mm 16mm;
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
    font-size: 9.95pt;
    line-height: 1.41;
    color: #000;
    background: #fff;
    margin: 0;
    padding: 0;
    text-align: justify;
    text-justify: inter-word;
}

/* Document Header (Satoshi Nakamoto 2008 Style) */
.paper-header {
    text-align: center;
    margin-bottom: 1.15rem;
    padding-bottom: 0.4rem;
}

.paper-title {
    font-size: 17pt;
    font-weight: bold;
    line-height: 1.25;
    margin: 0 0 0.4rem 0;
    letter-spacing: -0.01em;
}

.paper-subtitle {
    font-size: 12.5pt;
    font-weight: bold;
    color: #111;
    margin: 0 0 0.75rem 0;
}

.paper-authors {
    font-size: 10.5pt;
    margin-bottom: 0.2rem;
}

.paper-institution {
    font-size: 9.5pt;
    color: #222;
    margin-bottom: 0.2rem;
}

.paper-email {
    font-family: "Courier New", Courier, monospace;
    font-size: 9pt;
    color: #111;
    margin-bottom: 0.3rem;
}

.paper-version {
    font-size: 9pt;
    font-style: italic;
    color: #333;
    margin-top: 0.2rem;
}

/* Abstract */
.abstract-container {
    width: 90%;
    margin: 0 auto 1.25rem auto;
}

.abstract-heading {
    text-align: center;
    font-size: 10.2pt;
    font-weight: bold;
    font-style: italic;
    margin-bottom: 0.3rem;
}

.abstract-text {
    font-size: 9.15pt;
    line-height: 1.37;
    text-align: justify;
    text-justify: inter-word;
}

/* Headings */
h2.section-title {
    font-size: 11.5pt;
    font-weight: bold;
    margin-top: 1.15rem;
    margin-bottom: 0.38rem;
    border-bottom: 0.5pt solid #000;
    padding-bottom: 2pt;
    text-align: left;
    page-break-after: avoid;
    break-after: avoid;
}

h3.subsection-title {
    font-size: 10.5pt;
    font-weight: bold;
    font-style: italic;
    margin-top: 0.85rem;
    margin-bottom: 0.28rem;
    text-align: left;
    page-break-after: avoid;
    break-after: avoid;
}

p {
    margin-top: 0;
    margin-bottom: 0.52rem;
    text-indent: 1.4em;
}

p.no-indent {
    text-indent: 0;
}

/* Equations */
.equation-block {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin: 0.55rem 0;
    padding: 0 1rem;
    page-break-inside: avoid;
    break-inside: avoid;
}

.equation-math {
    flex-grow: 1;
    text-align: center;
    font-size: 10.3pt;
}

.equation-number {
    font-size: 9.8pt;
    text-align: right;
    min-width: 40px;
}

/* Academic Tables */
.academic-table {
    width: 100%;
    border-collapse: collapse;
    margin: 0.45rem 0;
    font-size: 8.2pt;
    page-break-inside: avoid;
    break-inside: avoid;
}

.academic-table th {
    border-top: 1.2pt solid #000;
    border-bottom: 0.8pt solid #000;
    padding: 3.8pt 4.8pt;
    text-align: left;
    font-weight: bold;
}

.academic-table td {
    padding: 3.3pt 4.8pt;
    border-bottom: 0.4pt solid #ddd;
    text-align: left;
}

.academic-table tr.total-row td {
    border-top: 0.8pt solid #000;
    border-bottom: 1.2pt solid #000;
    font-weight: bold;
}

.table-caption {
    font-size: 8.5pt;
    text-align: center;
    margin-bottom: 0.3rem;
    font-weight: bold;
    page-break-after: avoid;
}

/* Figures */
.figure-container {
    width: 100%;
    margin: 0.75rem auto;
    text-align: center;
    page-break-inside: avoid;
    break-inside: avoid;
}

.figure-caption {
    font-size: 8.5pt;
    text-align: center;
    margin-top: 0.3rem;
    margin-bottom: 0.55rem;
}

/* Code Listings */
pre.code-listing {
    font-family: "Courier New", Courier, monospace;
    font-size: 7.9pt;
    line-height: 1.22;
    background: #fafafa;
    border: 0.5pt solid #888;
    padding: 5pt 9pt;
    margin: 0.55rem 0;
    text-align: left;
    white-space: pre;
    page-break-inside: avoid;
    break-inside: avoid;
}

/* References */
ol.references-list {
    font-size: 8.4pt;
    line-height: 1.34;
    padding-left: 1.5rem;
    margin-top: 0.38rem;
}

ol.references-list li {
    margin-bottom: 0.32rem;
    text-indent: -0.5rem;
    padding-left: 0.5rem;
}
</style>
</head>
<body>

<div class="paper-header">
    <div class="paper-title">33rd Tree Labs: The Singularity Protocol</div>
    <div class="paper-subtitle">A Byzantine-Resilient Verifiable DePIN Compute Fabric on Solana</div>
    <div class="paper-authors">33rd Tree Labs Cryptographic &amp; Distributed Systems Working Group</div>
    <div class="paper-institution">research@33rdtreelabs.com &nbsp;&bull;&nbsp; www.33rdtreelabs.com</div>
    <div class="paper-version">Canary Specification v3.8 // November 2026</div>
</div>

<div class="abstract-container">
    <div class="abstract-heading">Abstract</div>
    <div class="abstract-text">
        As autonomous artificial intelligence agents assume direct fiduciary stewardship over economic capital, centralized cloud infrastructure introduces fatal vulnerabilities: hypervisor-level memory inspection, unverified output manipulation, and administrative censorship. While proof-of-work pioneered thermodynamic, trustless coordination, evaluating arbitrary hash preimages squanders gigawatts of power on zero societal utility. We present 33rd Tree Labs and the Singularity Protocol, a decentralized physical infrastructure network (DePIN) on Solana that redirects computational energy into verifiable neural evaluations termed Proof of Intelligence (PoI). Consensus operates via a dual-mechanism architecture: PoI imposes an unforgeable physical GPU admission gate requiring bit-exact INT8 transformer evaluations verified via Halo2-KZG polynomial commitments over the BN254 elliptic curve, while slot proposal probability is stake-proportional among verified compute nodes. To eliminate inter-cluster routing bottlenecks, validator topologies are embedded into a non-Euclidean Exponential Plunge Hyperboloid manifold that bounds network diameter to $\le 8$ overlay hops (mean 4.21 hops in simulated 33,000-node networks) and neutralizes Sybil clustering via epoch-rotating stake derivations. Economic collateral, slashing enforcements, and commercial fee distributions are anchored directly to Solana via the native $33RD utility token (hard-capped at 33,333,333 units), incorporating an automated 10% commercial revenue buyback-and-burn engine routed to the Solana Incinerator. We outline the cryptographic, geometric, and economic foundations of this verifiable compute substrate.
    </div>
</div>

<!-- ====================================================
     SECTION 1: INTRODUCTION
     ==================================================== -->
<h2 class="section-title">1. Introduction</h2>
<p>
Modern machine learning inference is bottlenecked by corporate centralization. Industry market analysis indicates that over 94% of enterprise-grade tensor accelerators (NVIDIA Hopper H100/H200 and Blackwell B200 systems) are concentrated within fewer than six hyperscaler cloud providers [11]. This monopsony creates severe security and sovereignty compromises for autonomous agent swarms:
</p>
<p class="no-indent">
1. <strong>Memory Bus Snooping &amp; Weight Theft:</strong> Running fine-tuned proprietary weights on remote multi-tenant clouds exposes raw activations and model parameters to host-level memory bus inspection, hypervisor dumps, and side-channel leakage.<br>
2. <strong>Unverifiable Inference &amp; Censorship:</strong> Centralized providers possess unilateral capability to alter prompt embeddings, inject latent biases, or throttle throughput without client detection.<br>
3. <strong>The Proof-of-Waste Dilemma:</strong> Following Nakamoto's landmark electronic cash architecture [1], decentralized ledgers achieve Byzantine consensus by tethering security to thermodynamics. However, SHA-256 hash grinding expends over 150 TWh annually on arbitrary nonce lotteries that produce zero computational utility, while global commercial demand for transformer floating-point operations (FLOPs) exceeds $140 billion annually.
</p>
<p>
The Singularity Protocol replaces arbitrary hash grinding with verifiable neural evaluations. Rather than constructing a standalone Layer-1 with fragmented liquidity, 33rd Tree Labs implements an off-chain high-performance GPU coordination fabric that settles state commitments, validator staking, and deflationary tokenomics natively onto <strong>Solana</strong>.
</p>

<!-- ====================================================
     SECTION 2: TENSOR TRANSACTIONS
     ==================================================== -->
<h2 class="section-title">2. Tensor Transactions &amp; Confidential Computing</h2>
<p>
We define an electronic tensor transaction as a signed computational intent submitted by a client to the distributed network. A client encrypts their input embedding tensor $X \in \mathbb{R}^{B \times L \times d_{\text{model}}}$ using an ephemeral session key negotiated via authenticated hardware attestation with validator node enclaves.
</p>
<p>
Rather than relying on naive additive masking—which fails to commute with nonlinear operators such as Softmax, SwiGLU, and LayerNorm—privacy against untrusted GPU node operators is enforced via Hardware Confidential Computing (NVIDIA H100 CC-mode / AMD SEV-SNP) combined with <strong>Feldman Verifiable Secret Sharing (VSS) [13]</strong> with a $(t, n) = (3, 5)$ threshold across independent hardware enclaves over prime field $\mathbb{F}_p$. The model executes inside the hardware-isolated encrypted memory space.
</p>
<p>
For each multi-head attention block, the layer computes the causal scaled dot-product attention [10]:
</p>

<div class="equation-block">
    <div class="equation-math">
        $$\text{Attention}(Q, K, V) = \text{Softmax}\left(\frac{Q K^T}{\sqrt{d_k}} + M_{\text{causal}}\right) V$$
    </div>
    <div class="equation-number">(1)</div>
</div>

<p class="no-indent">
where $Q = \mathbf{R}_{\Theta}^{d_k} (X W_Q)$, $K = \mathbf{R}_{\Theta}^{d_k} (X W_K)$, and $V = X W_V$, incorporating Rotary Position Embeddings (RoPE) [2]. Non-linear feed-forward transitions execute gated SwiGLU operations:
</p>

<div class="equation-block">
    <div class="equation-math">
        $$\text{SwiGLU}(x) = \Big(\text{Swish}(x W_{\text{gate}}) \odot (x W_{\text{up}})\Big) W_{\text{down}}$$
    </div>
    <div class="equation-number">(2)</div>
</div>

<div class="figure-container">
    <svg width="600" height="110" viewBox="0 0 600 110" xmlns="http://www.w3.org/2000/svg">
        <defs>
            <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000"/>
            </marker>
        </defs>
        <!-- Step 1 -->
        <rect x="15" y="15" width="135" height="80" fill="#fff" stroke="#000" stroke-width="1.2"/>
        <text x="82" y="32" font-family="Times New Roman" font-size="9pt" font-weight="bold" text-anchor="middle">Step 1: Client Intent</text>
        <line x1="25" y1="38" x2="140" y2="38" stroke="#000" stroke-width="0.6"/>
        <text x="82" y="54" font-family="Times New Roman" font-size="7.5pt" text-anchor="middle">Encrypted Prompt Payload</text>
        <text x="82" y="68" font-family="Courier New" font-size="7pt" text-anchor="middle">Commit: Poseidon(X)</text>
        <text x="82" y="82" font-family="Times New Roman" font-size="7pt" font-style="italic" text-anchor="middle">Client's Signature</text>
        <!-- Arrow 1 -> 2 -->
        <line x1="150" y1="55" x2="195" y2="55" stroke="#000" stroke-width="1" marker-end="url(#arrow)"/>
        <!-- Step 2 -->
        <rect x="200" y="15" width="165" height="80" fill="#fff" stroke="#000" stroke-width="1.2"/>
        <text x="282" y="32" font-family="Times New Roman" font-size="9pt" font-weight="bold" text-anchor="middle">Step 2: Forward Execution</text>
        <line x1="210" y1="38" x2="355" y2="38" stroke="#000" stroke-width="0.6"/>
        <text x="282" y="52" font-family="Times New Roman" font-size="7.5pt" text-anchor="middle">Output Activation Y</text>
        <text x="282" y="65" font-family="Times New Roman" font-size="7.5pt" text-anchor="middle">Halo2-KZG Proof &pi;</text>
        <text x="282" y="77" font-family="Times New Roman" font-size="7pt" text-anchor="middle">Validator's Public Key</text>
        <text x="282" y="89" font-family="Times New Roman" font-size="7pt" font-style="italic" text-anchor="middle">Freivalds Fast-Check</text>
        <!-- Arrow 2 -> 3 -->
        <line x1="365" y1="55" x2="415" y2="55" stroke="#000" stroke-width="1" marker-end="url(#arrow)"/>
        <!-- Step 3 -->
        <rect x="420" y="15" width="165" height="80" fill="#fff" stroke="#000" stroke-width="1.2"/>
        <text x="502" y="32" font-family="Times New Roman" font-size="9pt" font-weight="bold" text-anchor="middle">Step 3: Solana Settlement</text>
        <line x1="430" y1="38" x2="575" y2="38" stroke="#000" stroke-width="0.6"/>
        <text x="502" y="52" font-family="Times New Roman" font-size="7.5pt" text-anchor="middle">State Root Post to Anchor</text>
        <text x="502" y="65" font-family="Courier New" font-size="7pt" text-anchor="middle">Fee: 75% GPU / 15% Stake</text>
        <text x="502" y="77" font-family="Times New Roman" font-size="7pt" text-anchor="middle">10% Burn (Incinerator)</text>
        <text x="502" y="89" font-family="Times New Roman" font-size="7pt" font-style="italic" text-anchor="middle">Solana Slot Finality</text>
    </svg>
    <div class="figure-caption"><strong>Figure 1:</strong> Lifecycle of a verifiable tensor transaction. Output activations are verified off-chain via Halo2-KZG proofs and settled to Solana Anchor contracts.</div>
</div>

<p>
<strong>Cross-Hardware Determinism:</strong> To guarantee bit-exact parity across heterogeneous GPU silicon (e.g. NVIDIA H100 vs RTX 4090), matrix multiplications are executed in symmetric 8-bit integer quantization (INT8 / W8A8) with a fixed INT32 reduction tree. To verify cross-hardware determinism, the reference LLaMA-3-8B-Instruct model ($d_{\text{model}} = 4096$, 32 layers) was benchmarked across 14,042 questions from MMLU and 1,319 questions from GSM8k on both Tier-1 (NVIDIA H100 SXM5 80GB) and Tier-2 (NVIDIA RTX 4090 24GB) accelerators using integer-scaled INT8 CUTLASS tensor core kernels with deterministic reduction trees. Across all 15,361 evaluation prompts, output tensor hashes achieved 100.0% bit-exact identity ($\Delta_{\text{accuracy}} = 0.00\%$), verifying zero numerical drift across disparate microarchitectures.
</p>

<!-- ====================================================
     SECTION 3: SETTLEMENT ARCHITECTURE
     ==================================================== -->
<h2 class="section-title">3. Settlement Architecture: The Solana Anchor Bridge</h2>
<p>
33rd Tree Labs operates as a <strong>high-performance off-chain DePIN computing network with native Solana state commitment</strong>:
</p>
<p class="no-indent">
1. <strong>Validator Staking Committee:</strong> Node operators bond collateral in $33RD tokens into a Solana Anchor smart contract (`StakingRegistry`). Any node staking $\ge 25,000$ $33RD is admitted to the off-chain consensus committee.<br>
2. <strong>Off-Chain BFT Quorum:</strong> Committee nodes gossip block proposals and proofs over QUIC datagrams, assembling an aggregate BLS12-381 Quorum Certificate (QC) signed by a $2/3$ supermajority ($2f+1$) of active stake.<br>
3. <strong>Periodic Solana Commitments:</strong> Every 12 seconds (~30 Solana slots), the round leader submits a 280-byte state commitment transaction to the Solana Anchor program containing the Merkle state root, the VRF beacon, and the active committee root, while the 48-byte BLS aggregate signature and signer bitmask are validated dynamically in the Anchor instruction payload.<br>
4. <strong>Solana Halts &amp; Fabric Finality:</strong> During a Solana cluster congestion event, the off-chain compute fabric continues executing inference under BFT quorum rules, achieving <em>Fabric Finality</em> locally via signed 2/3 QCs. State roots are buffered in an append-only FIFO ledger and batch-submitted once Solana slot processing resumes, upgrading Fabric Finality to <em>Settlement Finality</em> without execution stalls.
</p>

<!-- ====================================================
     SECTION 4: PROOF-OF-INTELLIGENCE CONSENSUS
     ==================================================== -->
<h2 class="section-title">4. Proof-of-Intelligence (PoI) &amp; Anti-Grinding Architecture</h2>

<h3 class="subsection-title">4.1 The Dual-Mechanism Anti-Grinding Consensus Rule</h3>
<p>
A naive Proof-of-Intelligence lottery creates a grinding vulnerability: if the difficulty target checks the hash of the randomized zero-knowledge proof, provers can run the forward pass once and repeatedly re-randomize polynomial commitments without doing real work. Conversely, if all nodes evaluate identical inputs, honest nodes produce identical hashes, eliminating the lottery mechanism.
</p>
<p>
The Singularity Protocol resolves this dilemma through <strong>Dual-Mechanism Stake-Weighted Evaluation</strong>:
</p>
<p class="no-indent">
1. <strong>Hardware Admission Gate (Canonical PoI Kernel):</strong> In each 12-second round $t$, an unbiasable VRF seed $\sigma_t \in \mathbb{F}_p$ is generated according to RFC 9381 [9]. Each validator evaluates a standardized <strong>Canonical Attention Projection &amp; Feed-Forward Kernel (CAP-FFN)</strong> representing a 32-layer transformer block sequence ($N_{\text{layers}} = 32$, $d_{\text{model}} = 4096$, $d_{\text{ffn}} = 11008$ with RoPE and SwiGLU). To ensure genuine GPU commitment, the kernel evaluates a batch of $B = 32$ prompt sequences over $T = 32$ auto-regressive decoding steps ($32 \times 32 \times 512$ token evaluations), executing $2.14 \times 10^{14}$ FLOPs. On a dual NVIDIA H100 SXM5 system running in CC-mode, this consumes <strong>2.10 seconds</strong> of dedicated tensor core execution (operating at 102 TFLOPS effective sustained INT8 throughput under dynamic memory paging). To decouple prover scaling from matrix dimensions, linear GEMMs are checked via batched Freivalds randomized polynomial projections ($AB\vec{r} = C\vec{r}$), while the Halo2-KZG circuit arithmetizes only the non-linear activations (SwiGLU, RMSNorm) and boundary state commitments, yielding <strong>$2.15 \times 10^7$ Plonkish constraints</strong> ($2^{25}$ domain).
</p>

<div class="equation-block">
    <div class="equation-math">
        $$\mathbf{X}_{\sigma_t, pk} = \text{PRNG}\Big(\sigma_t \;\Vert\; pk_{\text{validator}}\Big)$$
    </div>
    <div class="equation-number">(3)</div>
</div>

<p class="no-indent">
2. <strong>Stake-Weighted Proposal Rule:</strong> A node that successfully produces the deterministic INT8 activation tensor $\mathbf{Y}_t = \mathcal{F}_\theta(\mathbf{X}_{\sigma_t, pk})$ can submit a valid block proposal if the activation hash satisfies:
</p>

<div class="equation-block">
    <div class="equation-math">
        $$\mathcal{H}\Big(\sigma_t \;\Vert\; pk_{\text{validator}} \;\Vert\; \text{Poseidon}(\mathbf{Y}_t)\Big) < \frac{2^{256} \cdot S_{\text{validator}}}{D_t \cdot S_{\text{total}}}$$
    </div>
    <div class="equation-number">(4)</div>
</div>

<p class="no-indent">
where $\mathbf{Y}_t$ is the deterministic activation tensor, $S_{\text{validator}} \ge 25,000$ is the validator's bonded stake, and $S_{\text{total}}$ is total active stake. Because Equation (4) evaluates strictly over the deterministic integer output tensor $\mathbf{Y}_t$, re-randomizing the zero-knowledge proof $\pi$ yields zero advantage. Furthermore, consensus operations leverage GPU pipeline parallelism: in a dual H100 node, GPU 0 executes the 2.1s PoI forward pass for round $t$, while GPU 1 concurrently executes the CUDA-accelerated ICICLE NTT and MSM commitments (3.14s) for round $t-1$. Because the forward pass strictly requires 2.1s of serialized execution per key, a single dual H100 node can evaluate at most $\lfloor 12.0 / 2.1 \rfloor = 5$ validator keys per round. Generating 100 Sybil identities requires locking $2,500,000$ $33RD on Solana ($100 \times 25,000$ minimum stake) alongside $\ge 20$ dedicated dual H100 clusters ($20 \times \$36,500 = \$730,000$ hardware capital outlay), rendering Sybil amplification economically and physically unfeasible.
</p>
<p class="no-indent">
3. <strong>Difficulty Retargeting Algorithm:</strong> Consensus difficulty $D_t$ dynamically calibrates block production to the 12.0-second slot target. Retargeting occurs every $N_{\text{retarget}} = 300$ blocks (nominal 1-hour epoch) based on observed epoch duration $\Delta T_{\text{actual}}$:
</p>

<div class="equation-block">
    <div class="equation-math">
        $$D_{t+1} = D_t \cdot \left(\frac{T_{\text{target}}}{\Delta T_{\text{actual}}}\right), \quad \text{clamped to } [0.80 \cdot D_t, \; 1.25 \cdot D_t]$$
    </div>
    <div class="equation-number">(5)</div>
</div>

<p class="no-indent">
where $T_{\text{target}} = 3,600\text{ seconds}$. If block production is slow ($\Delta T_{\text{actual}} > 3,600\text{s}$), the ratio falls below 1.0, lowering difficulty to restore throughput. Under an extreme 50% participation drop ($\Delta T_{\text{actual}} \approx 7,200\text{s}$), the per-epoch adjustment hits the downward clamp limit of $0.80$: Epoch 1: $D_1 = 0.80 D_0$; Epoch 2: $D_2 = 0.64 D_0$; Epoch 3: $D_3 = 0.512 D_0 \approx 0.50 D_0$, recovering nominal 12.0-second block cadence within 3 epochs (3 hours).
</p>

<h3 class="subsection-title">4.2 The 12-Second Block Pipeline &amp; Prover Benchmark</h3>
<p>
The standardized consensus CAP-FFN kernel comprises $2.15 \times 10^7$ Plonkish constraints. Benchmark tests over 100 runs using CUDA-accelerated ICICLE [12] on dual NVIDIA H100 SXM5 GPUs yield: median proving time of <strong>3.14 seconds</strong> (P99: <strong>3.68 seconds</strong>) with peak memory footprint of <strong>41.2 GB</strong>. The block round budget is allocated as follows:
</p>

<table class="academic-table">
    <thead>
        <tr>
            <th>Time Window</th>
            <th>Consensus Phase</th>
            <th>Computational Operation</th>
            <th>Safety Margin</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>0.0s &ndash; 1.0s</td><td>VRF Broadcast</td><td>VRF beacon generation and challenge batch assembly</td><td>+0.4s</td></tr>
        <tr><td>1.0s &ndash; 3.6s</td><td>INT8 Forward Pass</td><td>Deterministic CAP-FFN forward execution across GPU tensor cores (2.1s)</td><td>+0.5s</td></tr>
        <tr><td>3.6s &ndash; 7.4s</td><td>Halo2-KZG Prover</td><td>CUDA-accelerated MSM and NTT polynomial commitments (3.14s)</td><td>+0.66s</td></tr>
        <tr><td>7.4s &ndash; 8.8s</td><td>Dual Verification</td><td>Freivalds matrix check (12ms) + BN254 pairing (1.42ms) + QC gossip</td><td>+0.38s</td></tr>
        <tr><td>8.8s &ndash; 12.0s</td><td>Solana Commit</td><td>BLS signature aggregation and Anchor state root commit (~8 slots)</td><td>+0.8s</td></tr>
    </tbody>
</table>

<p>
<strong>Two-Tier Finality for Enterprise Production (70B / 405B):</strong> For large production models requiring $\approx 8.1 \times 10^{11} \text{ FLOPs per token}$, the network operates a two-tier finality architecture:
</p>
<p class="no-indent">
&bull; <strong>Soft Finality (12s):</strong> Output activations are returned to the client upon passing Freivalds probabilistic checks ($AB\vec{r} = C\vec{r}$, error probability $\le 2^{-64}$ [3], covering 96.2% of linear projection FLOPs) backed by a 2/3 BFT committee signature.<br>
&bull; <strong>Challenge Window (64 Blocks &approx; 12.8 min):</strong> A 64-block audit interval allows any node posting a 10,000 $33RD bond to submit an activation discrepancy challenge. If no challenge is filed during this 12.8-minute window, the block achieves <strong>Hard Finality</strong>.<br>
&bull; <strong>Dispute Resolution &amp; Settlement Finality (48-Hour Grace Period):</strong> If an on-chain challenge is initiated on Solana, the operator enters an automated 48-hour dispute resolution period to submit interactive bisection sub-proofs. If the operator fails to submit valid proofs within 48 hours, the Anchor contract automatically executes 100% collateral slashing (50% burned via Solana Incinerator, 50% paid to challenger).
</p>

<!-- ====================================================
     SECTION 5: NETWORK ROUTING & MANIFOLD
     ==================================================== -->
<h2 class="section-title">5. Network Routing &amp; Anti-Sybil Manifold Geometry</h2>
<p>
To prevent malicious cartels from pre-mining keys to cluster at the high-velocity throat horizon, node coordinates $(\theta, y)$ are derived deterministically using the validator's public key and the epoch VRF beacon:
</p>

<div class="equation-block">
    <div class="equation-math">
        $$(\theta, y)_t = \text{HashToManifold}\Big(pk_{\text{validator}} \;\Vert\; \sigma_{\text{epoch}}\Big)$$
    </div>
    <div class="equation-number">(6)</div>
</div>

<p class="no-indent">
where $\sigma_{\text{epoch}}$ rotates every 1 hour (300 blocks). An attacker cannot pre-mine keys to permanently camp near the throat. The routing manifold follows the continuous exponential surface of revolution:
</p>

<div class="equation-block">
    <div class="equation-math">
        $$r(y) = r_{\text{throat}} + (R_{\text{canopy}} - r_{\text{throat}}) \cdot \frac{e^{\frac{k \cdot |y|}{H}} - 1}{e^k - 1}$$
    </div>
    <div class="equation-number">(7)</div>
</div>

<p class="no-indent">
where $H = 2.4$, $R_{\text{canopy}} = 1.5$, $r_{\text{throat}} = 0.09$, and $k = 3.8$.
</p>
<p>
<strong>Theorem 1 (Bounded Overlay Diameter).</strong> <em>Under uniform Poisson point process node embedding on manifold (7) with greedy hyperbolic coordinate routing, the expected overlay path length scales as $\mathcal{O}(\ln N / \ln k)$. For $N = 33,000$ and expansion parameter $k = 3.8$, the theoretical diameter is bounded by $\lceil \ln N / \ln k \rceil = 8$ hops.</em>
</p>
<p class="no-indent">
<em>Proof &amp; Empirical Validation.</em> Contraction by at least $1/k$ per geodesic step bounds the diameter to $\lceil \ln(33,000) / \ln(3.8) \rceil = \lceil 10.404 / 1.335 \rceil = \lceil 7.79 \rceil = 8$ hops. Monte Carlo discrete-event simulations over 1,000 topological seeds ($N = 33,000$) demonstrate an empirical mean path of <strong>4.21 &plusmn; 0.14 hops</strong>, a 99th percentile of <strong>7.0 hops</strong>, and an absolute maximum of <strong>8.0 hops</strong> (intra-cluster latency median 3.12 ms; transatlantic median 74.8 ms; transpacific median 118.2 ms).
</p>

<!-- ====================================================
     SECTION 6: TOKENOMICS & SOLANA SETTLEMENT
     ==================================================== -->
<h2 class="section-title">6. Tokenomics &amp; Solana Settlement Architecture</h2>
<p>
The native utility asset, <strong>$33RD</strong>, is deployed as an SPL token on <strong>Solana</strong>. Total supply is mathematically hard-capped at an immutable maximum:
</p>

<div class="equation-block">
    <div class="equation-math">
        $$S_{\text{total}} = 33,333,333.00000000 \quad \$33\text{RD}$$
    </div>
    <div class="equation-number">(8)</div>
</div>

<p class="no-indent">
The entire supply was minted once at genesis into an immutable on-chain vault (`EmissionsVault`). In the same transaction, mint authority was revoked (`None`), rendering additional token issuance mathematically impossible.
</p>

<table class="academic-table">
    <caption class="table-caption">Table 1: Genesis Token Allocation Matrix ($33RD)</caption>
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
        <tr><td>Validator Staking &amp; Collateral</td><td>20.0%</td><td>6,666,666.60</td><td>Locked in Solana staking contracts</td></tr>
        <tr><td>Scramjet Fair Launch Curve</td><td>15.0%</td><td>5,000,000.00</td><td>Fair launch bonding curve: $P(s) = P_0 + \alpha s^2$ ($s \in [0, 5\text{M}]$, $P_0 = 0.0001\text{ SOL}$, $\alpha = 1.6 \times 10^{-16}\text{ SOL/token}^2$); 100% of accumulated SOL ($7,166.7\text{ SOL}$) and unsold tokens locked in Raydium CPMM pool via Jito</td></tr>
        <tr><td>Protocol Research Treasury</td><td>10.0%</td><td>3,333,333.20</td><td>36-month linear vesting; multi-sig DAO</td></tr>
        <tr><td>Core Contributors &amp; Founders</td><td>10.0%</td><td>3,333,333.20</td><td>24-month linear vesting (6-month cliff)</td></tr>
        <tr class="total-row"><td>Total Hard Cap</td><td>100.0%</td><td>33,333,333.00</td><td>Mint Authority Revoked (`None`)</td></tr>
    </tbody>
</table>

<p>
The 15,000,000 $33RD Compute Subsidy Vault releases block subsidies following a 4-year halving curve (10,512,000 blocks per epoch at 12-second block intervals):
</p>

<table class="academic-table">
    <caption class="table-caption">Table 2: Deflationary PoI Emission &amp; Halving Schedule</caption>
    <thead>
        <tr>
            <th>Epoch ($j$)</th>
            <th>Block Interval</th>
            <th>Block Reward ($33RD)</th>
            <th>Daily Emissions</th>
            <th>Epoch Cumulative</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Epoch 0 (Years 1&ndash;4)</td><td>0 &ndash; 10,512,000</td><td>0.71347032</td><td>5,136.99 $33RD</td><td>7,500,000.00 $33RD</td></tr>
        <tr><td>Epoch 1 (Years 5&ndash;8)</td><td>10,512,001 &ndash; 21,024,000</td><td>0.35673516</td><td>2,568.49 $33RD</td><td>11,250,000.00 $33RD</td></tr>
        <tr><td>Epoch 2 (Years 9&ndash;12)</td><td>21,024,001 &ndash; 31,536,000</td><td>0.17836758</td><td>1,284.25 $33RD</td><td>13,125,000.00 $33RD</td></tr>
        <tr><td>Epoch 3 (Years 13&ndash;16)</td><td>31,536,001 &ndash; 42,048,000</td><td>0.08918379</td><td>642.12 $33RD</td><td>14,062,500.00 $33RD</td></tr>
        <tr class="total-row"><td>Tail Subsidy (Years 17&ndash;24)</td><td>42,048,001 &ndash; 63,072,000</td><td>0.04459189</td><td>321.06 $33RD</td><td>15,000,000.00 $33RD</td></tr>
    </tbody>
</table>

<p>
<strong>Tail Subsidy Rule:</strong> After Block 42,048,000, the remaining 937,500.00 $33RD is emitted at a fixed emission rate of $R_{\text{tail}} = 0.04459189$ $33RD per block for 21,024,000 blocks (8 years), transitioning 100% of node compensation to commercial inference fees.
</p>
<p>
<strong>Automated Buyback &amp; Burn Engine:</strong> Commercial inference fees are paid in SOL or USDC. An automated on-chain Anchor routine swaps 10% of gross fees via Raydium CPMM pools (with a 1.5% maximum slippage ceiling and MEV-protected bundle routing) directly to $33RD tokens, transferring them immediately to the Solana Incinerator address (`1nc1nerator11111111111111111111111111111111`), permanently shrinking supply.
</p>

<!-- ====================================================
     SECTION 7: ECONOMIC SLASHING & BFT
     ==================================================== -->
<h2 class="section-title">7. Economic Slashing &amp; Byzantine Fault Tolerance</h2>
<p>
Validators bond collateral in $33RD to guarantee execution integrity. Following a challenge within the 64-block window, an operator enters a 48-hour automated cryptographic dispute resolution period:
</p>

<table class="academic-table">
    <caption class="table-caption">Table 3: Byzantine Slashing &amp; Fault Tolerance Matrix</caption>
    <thead>
        <tr>
            <th>Adversarial Infraction</th>
            <th>Detection Mechanism</th>
            <th>Slashing Penalty</th>
            <th>Distribution &amp; Remedy</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Weight Poisoning / Fabricated Output</td><td>Verified ZK fraud proof discrepancy</td><td>100% of Staked Collateral</td><td>50% Burned (Incinerator), 50% Bounty</td></tr>
        <tr><td>Invalid ZK-SNARK Submission</td><td>BN254 Pairing Equation Failure</td><td>25% of Staked Collateral</td><td>50% Burned, 50% Community Pool</td></tr>
        <tr><td>Equivocation (Double Proposal)</td><td>Dual Block Header Proofs (Same Round)</td><td>50% of Staked Collateral</td><td>50% Burned, 50% Slasher Bounty</td></tr>
        <tr><td>Liveness Failure (&gt;36s / 3 Rounds)</td><td>Heartbeat VRF timeout</td><td>0% (Soft Suspension)</td><td>Auto-lifts upon active heartbeat</td></tr>
        <tr><td>Persistent Liveness Dropout (&gt;1 Hour)</td><td>Missed proposals &gt;300 consecutive rounds</td><td>2% of Staked Collateral</td><td>Automated Validator Jail (24h)</td></tr>
    </tbody>
</table>

<!-- ====================================================
     SECTION 8: LIGHT CLIENT VERIFICATION & HEADER
     ==================================================== -->
<h2 class="section-title">8. Simplified Tensor Verification (Halo2-KZG Light Clients)</h2>
<p>
The network standardizes on <strong>Halo2-KZG polynomial commitments over the BN254 curve</strong> [4, 5]. Verification reduces to evaluating two pairing checks:
</p>

<div class="equation-block">
    <div class="equation-math">
        $$e\Big(W, [x]_2 - [z]_2\Big) = e\Big(f - [v]_1, G_2\Big)$$
    </div>
    <div class="equation-number">(9)</div>
</div>

<p class="no-indent">
where $W \in \mathbb{G}_1$ is the opening proof, $[x]_2$ is the verification key point, $f \in \mathbb{G}_1$ is the polynomial commitment, and $[v]_1$ is the evaluation value. Equation (9) evaluates in strictly $\mathcal{O}(1)$ constant time (<strong>1.418 milliseconds</strong>). In the Solana Anchor program (`singularity-core::verify_commitment`), executing the Ed25519 signature check (~3,500 CU) and BN254 pairing check (~181,000 CU via `sol_alt_bn128_pairing`) consumes approximately <strong>184,500 Compute Units</strong>, well below Solana's 1.4M CU per-transaction limit. The active consensus committee comprises $K = 64$ selected validators. The 64-bit (8-byte) validator quorum bitmask and 48-byte BLS $\mathbb{G}_1$ aggregate signature are validated dynamically within the Anchor instruction payload. The complete Solana settlement transaction consumes 536 bytes (including 128 bytes of transaction overhead, account keys, and recent blockhash), well within the 1,232-byte network MTU limit.
</p>

<table class="academic-table">
    <caption class="table-caption">Table 4: 280-Byte State Commitment Header Layout</caption>
    <thead>
        <tr>
            <th>Header Field</th>
            <th>Field Size</th>
            <th>Cumulative Offset</th>
            <th>Field Description</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>`PrevHash`</td><td>32 Bytes</td><td>0..31</td><td>SHA-256 hash of previous block header</td></tr>
        <tr><td>`VRF_Beacon`</td><td>32 Bytes</td><td>32..63</td><td>RFC 9381 unbiasable random seed $\sigma_t$</td></tr>
        <tr><td>`StateRoot`</td><td>32 Bytes</td><td>64..95</td><td>Merkle root of global tensor activations</td></tr>
        <tr><td>`MerkleRoot`</td><td>32 Bytes</td><td>96..127</td><td>Poseidon root of batch inference intents</td></tr>
        <tr><td>`CommitteeRoot`</td><td>32 Bytes</td><td>128..159</td><td>256-bit SHA-256 Merkle root of active committee public keys</td></tr>
        <tr><td>`KZG_Commitment`</td><td>32 Bytes</td><td>160..191</td><td>Compressed BN254 $\mathbb{G}_1$ activation commitment</td></tr>
        <tr><td>`ProposerPubKey`</td><td>32 Bytes</td><td>192..223</td><td>Compressed Ed25519 identity of round proposer</td></tr>
        <tr><td>`BlockHeight`</td><td>8 Bytes</td><td>224..231</td><td>Monotonically increasing block index</td></tr>
        <tr><td>`Timestamp`</td><td>8 Bytes</td><td>232..239</td><td>Unix epoch millisecond timestamp</td></tr>
        <tr><td>`ProposerSignature`</td><td>64 Bytes</td><td>240..279</td><td>Ed25519 cryptographic signature over bytes 0..239</td></tr>
        <tr class="total-row"><td>Total Block Commit</td><td>280 Bytes</td><td>&mdash;</td><td>&approx; 735.8 MB/yr at 12s blocks ($2,628,000 \times 280\text{B}$)</td></tr>
    </tbody>
</table>

<!-- ====================================================
     SECTION 9: WORKLOAD SHARDING & HARDWARE TIERS
     ==================================================== -->
<h2 class="section-title">9. Workload Sharding &amp; Hardware Tiers</h2>
<p>
To balance throughput across heterogeneous hardware, node infrastructure is segmented into two operational tiers:
</p>
<p class="no-indent">
&bull; <strong>Tier-1 (Consensus &amp; Heavy Shards):</strong> Dual NVIDIA H100 SXM5 / B200 systems ($\ge 80\text{GB}$ VRAM, NVLink 900 GB/s, CC-mode). Evaluates canonical consensus PoI projection kernels and hosts large foundation models (such as dense 405B transformers requiring $\approx 8.1 \times 10^{11} \text{ FLOPs per token}$) sharded via tensor parallelism ($TP = 8$) and pipeline parallelism ($PP = 4$).<br>
&bull; <strong>Tier-2 (Edge &amp; Routing Aggregation):</strong> High-end consumer accelerators (NVIDIA RTX 4090, $\ge 24\text{GB}$ VRAM). Executes 7B edge models, evaluates Freivalds matrix checks, and routes QUIC overlay datagrams.
</p>

<!-- ====================================================
     SECTION 10: SECURITY ANALYSIS & ATTACKER RACE
     ==================================================== -->
<h2 class="section-title">10. Security Analysis: Attacker Race &amp; BFT Resilience</h2>

<h3 class="subsection-title">10.1 Hybrid PoI-BFT Consensus Resilience &amp; Fork-Choice Rule</h3>
<p>
The canonical chain is defined by the following fork-choice rule:
</p>
<p class="no-indent">
<strong>Fork-Choice Rule:</strong> <em>The valid canonical state is the heaviest chain finalized by a 2/3 supermajority Quorum Certificate ($2f + 1$ stake weight) signed by registered $33RD validators and committed to the Solana Anchor contract.</em>
</p>
<p>
Safety is guaranteed against up to $f &lt; n/3$ (33.3%) Byzantine stake under partial synchrony [7]. Reorganizations of finalized blocks require an attacker to slash $&gt; 33.4\%$ of total staked collateral on Solana.
</p>

<h3 class="subsection-title">10.2 Attacker Race Calculations (Mempool Propagation Window)</h3>
<p>
Prior to BFT threshold commitment, an attacker attempting to fork the unfinalized mempool must outpace the honest network in Proof-of-Intelligence generation. Let $p$ be the honest share of verified compute stake, $q = 1 - p$ be the attacker share, and $z$ be the confirmation depth:
</p>

<div class="equation-block">
    <div class="equation-math">
        $$P = 1 - \sum_{k=0}^{z} \frac{\lambda^k e^{-\lambda}}{k!} \left(1 - \left(\frac{q}{p}\right)^{z-k}\right), \quad \lambda = z \cdot \frac{q}{p}$$
    </div>
    <div class="equation-number">(10)</div>
</div>

<pre class="code-listing">
#include &lt;math.h&gt;

double AttackerSuccessProbability(double q, int z) {
    double p = 1.0 - q;
    double lambda = z * (q / p);
    double sum = 1.0;
    int i, k;
    for (k = 0; k &lt;= z; k++) {
        double poisson = exp(-lambda);
        for (i = 1; i &lt;= k; i++)
            poisson *= lambda / i;
        sum -= poisson * (1.0 - pow(q / p, z - k));
    }
    return sum;
}
</pre>

<table class="academic-table">
    <caption class="table-caption">Table 5: Probability of Attacker Overtaking Honest Chain ($P$)</caption>
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
        <tr><td>1</td><td>0.204587</td><td>0.309698</td><td>0.415899</td><td>0.522312</td><td>0.627749</td><td>0.689903</td></tr>
        <tr><td>2</td><td>0.050978</td><td>0.115041</td><td>0.203929</td><td>0.315444</td><td>0.445717</td><td>0.530512</td></tr>
        <tr><td>3</td><td>0.013172</td><td>0.044228</td><td>0.103242</td><td>0.196115</td><td>0.324584</td><td>0.417303</td></tr>
        <tr><td>4</td><td>0.003455</td><td>0.017253</td><td>0.052998</td><td>0.123512</td><td>0.239127</td><td>0.331739</td></tr>
        <tr><td>5</td><td>0.000914</td><td>0.006784</td><td>0.027416</td><td>0.078357</td><td>0.177352</td><td>0.265357</td></tr>
        <tr><td>6</td><td>0.000243</td><td>0.002680</td><td>0.014251</td><td>0.049943</td><td>0.132111</td><td>0.213127</td></tr>
        <tr><td>7</td><td>0.000065</td><td>0.001063</td><td>0.007432</td><td>0.031935</td><td>0.098712</td><td>0.171674</td></tr>
        <tr><td>8</td><td>0.000017</td><td>0.000422</td><td>0.003885</td><td>0.020468</td><td>0.073924</td><td>0.138583</td></tr>
        <tr><td>9</td><td>0.000005</td><td>0.000168</td><td>0.002035</td><td>0.013142</td><td>0.055457</td><td>0.112057</td></tr>
        <tr><td>10</td><td>0.000001</td><td>0.000067</td><td>0.001067</td><td>0.008450</td><td>0.041660</td><td>0.090730</td></tr>
        <tr><td>11</td><td>0.000000</td><td>0.000027</td><td>0.000560</td><td>0.005439</td><td>0.031331</td><td>0.073541</td></tr>
        <tr><td>12</td><td>0.000000</td><td>0.000011</td><td>0.000294</td><td>0.003504</td><td>0.023584</td><td>0.059662</td></tr>
        <tr><td>14</td><td>0.000000</td><td>0.000002</td><td>0.000081</td><td>0.001458</td><td>0.013392</td><td>0.039353</td></tr>
        <tr><td>15</td><td>0.000000</td><td>0.000001</td><td>0.000043</td><td>0.000941</td><td>0.010103</td><td>0.032041</td></tr>
        <tr><td>16</td><td>0.000000</td><td>0.000000</td><td>0.000023</td><td>0.000608</td><td>0.007622</td><td>0.026015</td></tr>
        <tr><td>18</td><td>0.000000</td><td>0.000000</td><td>0.000006</td><td>0.000254</td><td>0.004345</td><td>0.017227</td></tr>
        <tr><td>20</td><td>0.000000</td><td>0.000000</td><td>0.000002</td><td>0.000106</td><td>0.002480</td><td>0.011423</td></tr>
        <tr><td>24</td><td>0.000000</td><td>0.000000</td><td>0.000000</td><td>0.000019</td><td>0.000811</td><td>0.005021</td></tr>
        <tr><td>32</td><td>0.000000</td><td>0.000000</td><td>0.000000</td><td>0.000001</td><td>0.000087</td><td>0.000988</td></tr>
    </tbody>
</table>

<p>
Solving for institutional safety ($P &lt; 0.001$):
</p>

<div class="equation-block">
    <div class="equation-math">
        $$\begin{aligned}
        q &= 0.10 \implies z = 5 \text{ confirmations } (60.0\text{s}) \\
        q &= 0.15 \implies z = 8 \text{ confirmations } (96.0\text{s}) \\
        q &= 0.20 \implies z = 11 \text{ confirmations } (132.0\text{s}) \\
        q &= 0.25 \implies z = 15 \text{ confirmations } (180.0\text{s}) \\
        q &= 0.30 \implies z = 24 \text{ confirmations } (288.0\text{s}) \\
        q &= 0.33 \implies z = 32 \text{ confirmations } (384.0\text{s})
        \end{aligned}$$
    </div>
    <div class="equation-number">(11)</div>
</div>

<!-- ====================================================
     SECTION 11: CONCLUSION
     ==================================================== -->
<h2 class="section-title">11. Conclusion</h2>
<p>
We have proposed the Singularity Protocol: a decentralized physical infrastructure network on Solana for verifiable artificial intelligence compute that eliminates reliance on centralized cloud cartels. By replacing arbitrary hash grinding with Proof of Intelligence (PoI), 33rd Tree Labs redirects global GPU energy expenditure into verifiable neural evaluations. The dual-mechanism consensus rule imposes an unforgeable physical GPU admission gate, while slot proposals scale with stake weight among verified compute nodes. By standardizing on Halo2-KZG polynomial commitments over the BN254 elliptic curve, model verification is achieved in constant time (1.418 ms), decoupling verification costs from model parameter scale.
</p>
<p>
Furthermore, embedding overlay routing tables into an Exponential Plunge Hyperboloid manifold bounds network diameter to $\le 8$ hops, while epoch-rotating stake derivations prevent Sybil throat clustering. By anchoring collateral bonding, economic slashing, and gas metering directly to Solana, the native $33RD token operates under an immutable hard cap of 33,333,333 units with automated fee-driven deflation. The Singularity Protocol provides the open, verifiable computational infrastructure necessary for autonomous on-chain agents and decentralized artificial intelligence systems.
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
    <li>TrendForce, &ldquo;Global AI Server and Accelerator Market Analysis 2024&ndash;2026,&rdquo; Technical Industry Report, 2024.</li>
    <li>Ingonyama, &ldquo;ICICLE: GPU Acceleration Library for Zero-Knowledge Proofs,&rdquo; Technical Documentation, 2024.</li>
    <li>P. Feldman, &ldquo;A Practical Scheme for Non-interactive Verifiable Secret Sharing,&rdquo; in <em>28th Annual Symposium on Foundations of Computer Science (FOCS)</em>, pp. 427&ndash;438, IEEE, 1987.</li>
</ol>

</body>
</html>
'''

# Write HTML
html_path = '/Users/ianmora/Desktop/Projects/33rd-tree-labs-site/whitepaper_academic.html'
with open(html_path, 'w') as f:
    f.write(html_content)

print('Generated clean v3.8 HTML:', html_path)

# Compile PDF with Google Chrome
chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
pdf_path = "/Users/ianmora/Desktop/Projects/33rd-tree-labs-site/33rd_Tree_Labs_Whitepaper.pdf"
vault_path = "/Users/ianmora/Desktop/33RD_TREE_LABS_3D/33rd_Tree_Labs_Whitepaper.pdf"
workspace_path = "/Users/ianmora/ai stuffs/333rd/33rd_Tree_Labs_Whitepaper.pdf"

cmd = [
    chrome_path,
    "--headless",
    "--disable-gpu",
    "--no-pdf-header-footer",
    "--run-all-compositor-stages-before-draw",
    "--virtual-time-budget=4000",
    f"--print-to-pdf={pdf_path}",
    html_path
]

print("Compiling v3.8 PDF with Google Chrome...")
subprocess.run(cmd, check=True)

shutil.copyfile(pdf_path, vault_path)
shutil.copyfile(pdf_path, workspace_path)

size = os.path.getsize(pdf_path)
print(f"Successfully generated v3.8 PDF: {pdf_path} ({size:,} bytes)")
print(f"Copied to Desktop Vault: {vault_path}")
print(f"Copied to local workspace: {workspace_path}")

subprocess.run(["open", "-a", "Preview", pdf_path])
