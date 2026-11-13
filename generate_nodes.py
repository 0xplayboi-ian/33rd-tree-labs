import os
from generate_editorial_subpages import get_header, get_footer

def build_nodes():
    head = get_header(
        title="33RD TREE LABS // Node Operator &amp; Validator Architecture &bull; 33rdtreelabs.tech",
        description="Comprehensive Node Operator & Validator Manual for 33rd Tree Labs Singularity Protocol: Multi-TEE Remote Attestation, Hardware Matrix, Slashing Proof Register, and CLI Daemon Runbook.",
        active_page="nodes"
    )

    body = """
  <main class="page-wrap">
    <!-- EDITORIAL HERO / HEADER -->
    <header class="ed-hero">
      <div class="ed-kicker">( 005 ) // DEPIN VALIDATOR SPECIFICATION &bull; 33RDTREELABS.TECH</div>
      <h1 class="ed-headline">NODE ARCHITECTURE &amp;<br><span class="accent">OPERATOR RUNBOOK</span></h1>
      <p class="ed-lead">
        A Byzantine-Fault-Tolerant distributed compute fabric anchored on Solana. Hardware-enforced Confidential Computing via Multi-TEE remote attestation, deterministic INT8 tensor execution, and cryptographic slashing penalties enforced on-chain.
      </p>

      <!-- TELEMETRY STRIP (NO CARD CONTAINERS) -->
      <div class="telemetry-strip">
        <div class="telemetry-cell">
          <span class="telemetry-lbl">Byzantine Committee Quorum</span>
          <span class="telemetry-val accent">K = 64 NODES (&gt; 2/3 BFT)</span>
        </div>
        <div class="telemetry-cell">
          <span class="telemetry-lbl">Hardware TEE Standard</span>
          <span class="telemetry-val">AMD SEV-SNP // INTEL TDX // HOPPER CC</span>
        </div>
        <div class="telemetry-cell">
          <span class="telemetry-lbl">Minimum Collateral Stake</span>
          <span class="telemetry-val">25,000 $33RD (TIER 3)</span>
        </div>
        <div class="telemetry-cell">
          <span class="telemetry-lbl">Dispute Bisection Window</span>
          <span class="telemetry-val green">64 SLOTS (~25.6 SECONDS)</span>
        </div>
      </div>
    </header>

    <!-- SECTION 01: HARDWARE MATRIX -->
    <section class="ed-section" id="hardware-matrix">
      <div class="ed-sec-head">
        <div class="sec-badge-col">
          <span class="sec-giant-num">01</span>
          <span class="sec-kicker">// PHYSICAL MATRIX</span>
        </div>
        <div>
          <h2 class="sec-title">Hardware Classification &amp; Compute Tiers</h2>
          <p class="sec-summary">
            Nodes in the Singularity Protocol are categorized into four deterministic tiers based on memory bus width, high-bandwidth VRAM, thermal dissipation capacity (TDP), and hardware-enforced remote attestation capabilities. Each tier services a dedicated layer of the Tensor Arbor hierarchy.
          </p>
        </div>
      </div>

      <!-- 4-COLUMN COMPARISON GRID (OPEN EDITORIAL - ZERO BOXED CARDS) -->
      <div class="ed-grid-4">
        <div class="ed-grid-col ed-grid-cell">
          <div>
            <span class="cell-tag">[ TIER 01 // CANARY EDGE ]</span>
            <h3 class="cell-title">Edge Canary</h3>
            <p class="cell-body">
              Low-latency edge inference, prompt token preprocessing, and speculative decoding verification. Ideal for distributed consumer-grade workstation operators.
            </p>
          </div>
          <ul class="cell-spec-list">
            <li><span>GPU Target:</span> <strong>1x RTX 4090 / L40S</strong></li>
            <li><span>VRAM Capacity:</span> <strong>24 GB GDDR6X</strong></li>
            <li><span>Memory Bus Width:</span> <strong>384-bit</strong></li>
            <li><span>Peak Bandwidth:</span> <strong>1.008 TB/s</strong></li>
            <li><span>Thermal TDP:</span> <strong>450W Max</strong></li>
            <li><span>Host Interconnect:</span> <strong>PCIe Gen4 x16</strong></li>
            <li><span>Required Stake:</span> <strong>1,000 $33RD</strong></li>
            <li><span>PoI Multiplier:</span> <strong>1.0x Base Weight</strong></li>
          </ul>
        </div>

        <div class="ed-grid-col ed-grid-cell">
          <div>
            <span class="cell-tag">[ TIER 02 // CLUSTER WORKER ]</span>
            <h3 class="cell-title">Cluster Worker</h3>
            <p class="cell-body">
              Mid-scale transformer execution, intermediate layer tensor sharding, and INT8 quantized model weight hosting for 8B-34B parameter models.
            </p>
          </div>
          <ul class="cell-spec-list">
            <li><span>GPU Target:</span> <strong>4x A100 / 8x 4090</strong></li>
            <li><span>VRAM Capacity:</span> <strong>320 GB HBM2e</strong></li>
            <li><span>Memory Bus Width:</span> <strong>4096-bit (HBM2e)</strong></li>
            <li><span>Peak Bandwidth:</span> <strong>2.039 TB/s</strong></li>
            <li><span>Thermal TDP:</span> <strong>1,600W Enclosure</strong></li>
            <li><span>Host Interconnect:</span> <strong>NVLink 600 GB/s</strong></li>
            <li><span>Required Stake:</span> <strong>5,000 $33RD</strong></li>
            <li><span>PoI Multiplier:</span> <strong>2.8x Weight</strong></li>
          </ul>
        </div>

        <div class="ed-grid-col ed-grid-cell">
          <div>
            <span class="cell-tag">[ TIER 03 // FOUNDATION VALIDATOR ]</span>
            <h3 class="cell-title">Foundation Node</h3>
            <p class="cell-body">
              Enterprise foundation model hosting (70B-405B MoE architectures), full recursive zero-knowledge proof generation, and BFT consensus committee voting.
            </p>
          </div>
          <ul class="cell-spec-list">
            <li><span>GPU Target:</span> <strong>8x H100 80GB SXM5</strong></li>
            <li><span>VRAM Capacity:</span> <strong>640 GB HBM3</strong></li>
            <li><span>Memory Bus Width:</span> <strong>5120-bit (HBM3)</strong></li>
            <li><span>Peak Bandwidth:</span> <strong>3.35 TB/s per GPU</strong></li>
            <li><span>Thermal TDP:</span> <strong>5,600W SXM Tray</strong></li>
            <li><span>Host Interconnect:</span> <strong>NVLink 900 GB/s</strong></li>
            <li><span>Required Stake:</span> <strong>25,000 $33RD</strong></li>
            <li><span>PoI Multiplier:</span> <strong>8.5x Weight</strong></li>
          </ul>
        </div>

        <div class="ed-grid-col ed-grid-cell">
          <div>
            <span class="cell-tag">[ TIER 04 // SOVEREIGN BACKBONE ]</span>
            <h3 class="cell-title">Datacenter Pod</h3>
            <p class="cell-body">
              Multi-rack supercomputing cluster providing global root routing for the Tensor Arbor manifold, recursive IVC proof aggregation, and ultra-dense training runs.
            </p>
          </div>
          <ul class="cell-spec-list">
            <li><span>GPU Target:</span> <strong>32x H100 / B200 Pod</strong></li>
            <li><span>VRAM Capacity:</span> <strong>6.14 TB HBM3e</strong></li>
            <li><span>Memory Bus Width:</span> <strong>8192-bit (HBM3e)</strong></li>
            <li><span>Peak Bandwidth:</span> <strong>8.0 TB/s per GPU</strong></li>
            <li><span>Thermal TDP:</span> <strong>35 kW Liquid Cooled</strong></li>
            <li><span>Host Interconnect:</span> <strong>NVLink 1.8 TB/s</strong></li>
            <li><span>Required Stake:</span> <strong>100,000 $33RD</strong></li>
            <li><span>PoI Multiplier:</span> <strong>32.0x Weight</strong></li>
          </ul>
        </div>
      </div>

      <!-- OPEN MONOSPACE HARDWARE SPECIFICATION TABLE -->
      <div class="ed-table-wrap">
        <table class="ed-table">
          <thead>
            <tr>
              <th>Compute Tier</th>
              <th>Processor Engine</th>
              <th>Memory Bus Width</th>
              <th>VRAM Bandwidth</th>
              <th>Host Network Uplink</th>
              <th>TEE Enclave Support</th>
              <th>Minimum Bond</th>
              <th>Attestation SLA</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="accent">TIER 1 (CANARY)</td>
              <td class="highlight">AD102-300-A1 (RTX 4090)</td>
              <td>384-bit GDDR6X</td>
              <td>1,008 GB/s</td>
              <td>500 Mbps Synchronous</td>
              <td>Intel SGX v2 / User Enclave</td>
              <td>1,000 $33RD</td>
              <td>99.90% Uptime</td>
            </tr>
            <tr>
              <td class="accent">TIER 2 (CLUSTER)</td>
              <td class="highlight">4x GA100-SXM4-80GB</td>
              <td>4096-bit HBM2e</td>
              <td>2,039 GB/s per GPU</td>
              <td>10 Gbps SFP+ Fiber</td>
              <td>AMD SEV-SNP (Gen 3 EPYC)</td>
              <td>5,000 $33RD</td>
              <td>99.95% Uptime</td>
            </tr>
            <tr>
              <td class="accent">TIER 3 (VALIDATOR)</td>
              <td class="highlight">8x GH100-SXM5-80GB</td>
              <td>5120-bit HBM3</td>
              <td>3,350 GB/s per GPU</td>
              <td>400 Gbps InfiniBand NDR</td>
              <td>NVIDIA Hopper CC + Intel TDX</td>
              <td>25,000 $33RD</td>
              <td>99.99% Uptime</td>
            </tr>
            <tr>
              <td class="accent">TIER 4 (SOVEREIGN)</td>
              <td class="highlight">32x B200 / H200 SuperPod</td>
              <td>8192-bit HBM3e</td>
              <td>8,000 GB/s per GPU</td>
              <td>800 Gbps Dark Fiber Fabric</td>
              <td>Dual-Root SEV-SNP + TDX + CC</td>
              <td>100,000 $33RD</td>
              <td>99.999% Uptime</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- SECTION 02: MULTI-TEE CONFIDENTIAL COMPUTING -->
    <section class="ed-section" id="tee-attestation">
      <div class="ed-sec-head">
        <div class="sec-badge-col">
          <span class="sec-giant-num">02</span>
          <span class="sec-kicker">// ZERO-TRUST SECURITY</span>
        </div>
        <div>
          <h2 class="sec-title">Multi-TEE Confidential Computing &amp; Remote Attestation</h2>
          <p class="sec-summary">
            Trust in the Singularity Protocol does not rely on validator reputations or subjective human audits. All computation occurs inside hardware-isolated Trusted Execution Environments (TEEs) validated by rigorous cryptographic measurements.
          </p>
        </div>
      </div>

      <div class="ed-prose-cols">
        <div class="prose-block">
          <h3>Intel SGX / TDX Remote Attestation</h3>
          <p>
            Intel Trust Domain Extensions (TDX) isolates entire virtual machine guests from the host hypervisor, system management mode (SMM), and external DMA buses. During boot, the processor measures the initial state of the memory pages into the <code>MRTD</code> (Measurement of Trust Domain) and <code>RTMR[0..3]</code> (Runtime Measurement Registers).
          </p>
          <p>
            The hardware enclave generates an asymmetric ECDSA P-256 quote signed by the Intel Provisioning Certification Key (PCK). This quote is verified on-chain by the 33rd Tree Labs Solana Anchor program using the Secp256r1 verification instruction, ensuring that node binaries have not been altered or debugged by the operator.
          </p>
        </div>
        <div class="prose-block">
          <h3>AMD SEV-SNP Cryptographic Validation</h3>
          <p>
            AMD Secure Encrypted Virtualization-Secure Nested Paging (SEV-SNP) provides memory encryption (AES-128/AES-256) with physical hardware page isolation against hypervisor-induced replay attacks, memory remapping, and memory corruption.
          </p>
          <p>
            Each validator node retrieves an attestation report from the AMD Secure Processor (ASP) containing the cryptographic hash of the launch digest, guest policy flags, and the chip's unique Versioned Chip Endorsement Key (VCEK). The Solana verification contract validates the full X.509 certificate path up to the AMD KDS root authority.
          </p>
        </div>
      </div>

      <div class="ed-prose-cols">
        <div class="prose-block">
          <h3>NVIDIA Hopper CC (Confidential Computing)</h3>
          <p>
            On NVIDIA H100 and B200 platforms, hardware TEE protection extends across the high-speed PCIe Gen5 and NVLink bus directly into the GPU silicon. NVIDIA Hopper Confidential Computing operates in On-Die hardware isolated mode, encrypting all GPU high-bandwidth memory (HBM3) and command queues.
          </p>
          <p>
            Communication between the CPU enclave and the GPU is established via Security Protocol and Data Model (SPDM 1.2) session handshake. The GPU returns an SPDM attestation measurement block containing the exact hash of the GPU microcode, firmware VBIOS, and active security policy, preventing rogue kernel hooks or model weight extraction.
          </p>
        </div>
        <div class="prose-block">
          <h3>On-Chain Attestation Pipeline</h3>
          <p>
            Before a node is permitted to participate in the Byzantine committee ($K=64$), it must post an on-chain Attestation Commitment Transaction. The transaction packages:
          </p>
          <ul class="cell-spec-list" style="border:none; padding:0;">
            <li><span>1. CPU Enclave Quote:</span> <strong>DCAP Intel TDX / AMD SEV-SNP</strong></li>
            <li><span>2. GPU Device Certificate:</span> <strong>NVIDIA SPDM 1.2 Device Leaf</strong></li>
            <li><span>3. Model Weight Digest:</span> <strong>Merkle Tree Root over INT8 Tensors</strong></li>
            <li><span>4. Node Identity Signature:</span> <strong>Ed25519 Validator Keypair</strong></li>
          </ul>
        </div>
      </div>

      <div class="math-callout">
        <div class="math-callout-title">// MATHEMATICAL ATTESTATION INTEGRITY CONDITION</div>
        $$\text{VerifyAttestation}(Q_{\text{TDX}}, C_{\text{Hopper}}, H_{\text{Weights}}, \text{PubKey}_{\text{Ed25519}}) \equiv 1 \iff \begin{cases} \text{ECDSA\_Verify}(Q_{\text{TDX}}, \text{Root}_{\text{Intel}}) = 1 \\ \text{SPDM\_Validate}(C_{\text{Hopper}}, \text{Root}_{\text{NVIDIA}}) = 1 \\ H(\text{Weights}_{\text{Enclave}}) = H_{\text{Canonical}} \end{cases}$$
        Failure to satisfy any sub-condition results in immediate hardware rejection and forfeiture of the admission gas fee.
      </div>
    </section>

    <!-- SECTION 03: NODE OPERATOR ONBOARDING RUNBOOK -->
    <section class="ed-section" id="onboarding-manual">
      <div class="ed-sec-head">
        <div class="sec-badge-col">
          <span class="sec-giant-num">03</span>
          <span class="sec-kicker">// OPERATOR RUNBOOK</span>
        </div>
        <div>
          <h2 class="sec-title">Node Onboarding Manual &amp; CLI Daemon Reference</h2>
          <p class="sec-summary">
            A step-by-step production installation runbook for bare-metal enterprise servers running Ubuntu Server 22.04 LTS or 24.04 LTS. Execute these instructions inside a hardened administrative shell.
          </p>
        </div>
      </div>

      <!-- STEP 1 -->
      <div class="ed-code-block">
        <div class="ed-code-header">
          <span>STEP 01: HOST PROVISIONING &amp; KERNEL HARDENING</span>
          <span>BASH // UBUNTU 22.04 / 24.04 LTS</span>
        </div>
        <div class="ed-code-content">
<span class="cmd-comment"># Update package index and install foundational dependencies</span>
<span class="cmd-prompt">$</span>sudo apt-get update &amp;&amp; sudo apt-get install -y build-essential curl git jq libssl-dev pkg-config

<span class="cmd-comment"># Configure hugepages and kernel memory locking for zero-copy DMA</span>
<span class="cmd-prompt">$</span>echo "vm.nr_hugepages = 8192" | sudo tee -a /etc/sysctl.d/99-singularity.conf
<span class="cmd-prompt">$</span>echo "fs.file-max = 2097152" | sudo tee -a /etc/sysctl.d/99-singularity.conf
<span class="cmd-prompt">$</span>sudo sysctl -p /etc/sysctl.d/99-singularity.conf

<span class="cmd-comment"># Validate NVIDIA Open Kernel Module 550+ and CUDA 12.4+</span>
<span class="cmd-prompt">$</span>nvidia-smi --query-gpu=driver_version,name,pstate,temperature.gpu --format=csv
        </div>
      </div>

      <!-- STEP 2 -->
      <div class="ed-code-block">
        <div class="ed-code-header">
          <span>STEP 02: DAEMON INITIALIZATION &amp; KEYPAIR GENERATION</span>
          <span>CLI BINARY // canary-node</span>
        </div>
        <div class="ed-code-content">
<span class="cmd-comment"># Download and verify the signed 33rd Tree Labs daemon binary</span>
<span class="cmd-prompt">$</span>curl -fsSL https://get.33rdtreelabs.tech/canary-node-v4.0-linux-amd64.tar.gz | tar -xz -C /usr/local/bin/
<span class="cmd-prompt">$</span>canary-node --version <span class="cmd-comment"># Verify: canary-node v4.0.2-canary (rev 33rd-c918a)</span>

<span class="cmd-comment"># Initialize node data directory and configuration skeleton</span>
<span class="cmd-prompt">$</span>canary-node init <span class="cmd-flag">--network</span> <span class="cmd-val">mainnet-beta</span> <span class="cmd-flag">--moniker</span> <span class="cmd-val">"singularity-prod-01"</span> <span class="cmd-flag">--home</span> <span class="cmd-val">~/.33rd/</span>

<span class="cmd-comment"># Generate Ed25519 node identity keypair and print public address</span>
<span class="cmd-prompt">$</span>canary-node keygen <span class="cmd-flag">--keypair</span> <span class="cmd-val">~/.33rd/validator-identity.json</span>
<span class="cmd-comment"># Output: [SUCCESS] Validator Identity Pubkey: 33rd7xGqN...8YwP2</span>
        </div>
      </div>

      <!-- STEP 3 -->
      <div class="ed-code-block">
        <div class="ed-code-header">
          <span>STEP 03: BONDING COLLATERAL STAKE ON SOLANA</span>
          <span>SOLANA ANCHOR CLI</span>
        </div>
        <div class="ed-code-content">
<span class="cmd-comment"># Deposit minimum required $33RD tokens into validator stake account</span>
<span class="cmd-prompt">$</span>canary-node stake <span class="cmd-flag">--keypair</span> <span class="cmd-val">~/.33rd/validator-identity.json</span> \\
    <span class="cmd-flag">--amount</span> <span class="cmd-val">25000</span> \\
    <span class="cmd-flag">--tier</span> <span class="cmd-val">h100</span> \\
    <span class="cmd-flag">--rpc</span> <span class="cmd-val">https://api.mainnet-beta.solana.com</span> \\
    <span class="cmd-flag">--program-id</span> <span class="cmd-val">CanaryStake1111111111111111111111111111111111</span>

<span class="cmd-comment"># Verify on-chain stake delegation status</span>
<span class="cmd-prompt">$</span>canary-node query-stake <span class="cmd-flag">--validator-pubkey</span> <span class="cmd-val">33rd7xGqN...8YwP2</span>
        </div>
      </div>

      <!-- STEP 4 -->
      <div class="ed-code-block">
        <div class="ed-code-header">
          <span>STEP 04: GENERATE HARDWARE TEE ATTESTATION EVIDENCE</span>
          <span>SECURITY ATTESTATION</span>
        </div>
        <div class="ed-code-content">
<span class="cmd-comment"># Query hardware TEE registers and synthesize multi-layer cryptographic quote</span>
<span class="cmd-prompt">$</span>canary-node attest <span class="cmd-flag">--tee</span> <span class="cmd-val">tdx-sev-hopper</span> \\
    <span class="cmd-flag">--quote-out</span> <span class="cmd-val">~/.33rd/attestation.bin</span> \\
    <span class="cmd-flag">--spdm-port</span> <span class="cmd-val">4128</span>

<span class="cmd-comment"># Submit quote to Solana Anchor verification program</span>
<span class="cmd-prompt">$</span>canary-node submit-attestation <span class="cmd-flag">--quote</span> <span class="cmd-val">~/.33rd/attestation.bin</span> \\
    <span class="cmd-flag">--keypair</span> <span class="cmd-val">~/.33rd/validator-identity.json</span>
        </div>
      </div>

      <!-- STEP 5 -->
      <div class="ed-code-block">
        <div class="ed-code-header">
          <span>STEP 05: LAUNCH PRODUCTION SYSTEMD SERVICE</span>
          <span>SYSTEMD CONFIGURATION</span>
        </div>
        <div class="ed-code-content">
<span class="cmd-comment"># /etc/systemd/system/canary-node.service</span>
[Unit]
Description=33rd Tree Labs Singularity Node Daemon
After=network-online.target time-sync.target
Wants=network-online.target

[Service]
User=root
WorkingDirectory=/root/.33rd
ExecStart=/usr/local/bin/canary-node run \\
    --tier h100 \\
    --gpus 0,1,2,3,4,5,6,7 \\
    --port 9033 \\
    --metrics 9100 \\
    --p2p-addr /ip4/0.0.0.0/tcp/9033 \\
    --rpc-url https://api.mainnet-beta.solana.com \\
    --keypair /root/.33rd/validator-identity.json
Restart=always
RestartSec=5s
LimitNOFILE=1048576
LimitMEMLOCK=infinity

[Install]
WantedBy=multi-user.target
        </div>
      </div>

      <!-- JSON-RPC API REFERENCE -->
      <h3 style="font-family:var(--fh); font-size:22px; text-transform:uppercase; margin:40px 0 16px;">Daemon Local JSON-RPC 2.0 API Reference</h3>
      <div class="ed-table-wrap">
        <table class="ed-table">
          <thead>
            <tr>
              <th>Method Name</th>
              <th>Parameters</th>
              <th>Return Type</th>
              <th>Description</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="accent">node_getAttestation</td>
              <td><code>{"format": "dcap_v4"}</code></td>
              <td><code>{"quote_hex": String, "cert_chain": String}</code></td>
              <td>Returns current CPU/GPU hardware attestation binary and X.509 cert bundle.</td>
            </tr>
            <tr>
              <td class="accent">node_submitInferenceBatch</td>
              <td><code>{"batch_id": U64, "tensors": String}</code></td>
              <td><code>{"status": "ACK", "slot": U64, "receipt": String}</code></td>
              <td>Queues INT8 deterministic forward pass inference job to TEE worker thread.</td>
            </tr>
            <tr>
              <td class="accent">node_queryStakeAccount</td>
              <td><code>{"validator_pubkey": String}</code></td>
              <td><code>{"staked_33rd": U64, "status": "ACTIVE"}</code></td>
              <td>Queries Anchor stake vault PDA for current collateral balance and lock status.</td>
            </tr>
            <tr>
              <td class="accent">node_getPeerTopology</td>
              <td><code>{"depth": 3}</code></td>
              <td><code>{"peers": Array, "hyperbolic_coord": Object}</code></td>
              <td>Returns neighboring nodes in Poincaré disk metric space with RTT metrics.</td>
            </tr>
            <tr>
              <td class="accent">node_requestDisputeResolution</td>
              <td><code>{"divergent_slot": U64, "proof": String}</code></td>
              <td><code>{"bisection_step": U32, "target_layer": U32}</code></td>
              <td>Initiates interactive binary bisection dispute on Solana for conflicting logits.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- SECTION 04: SLASHING PROOF REGISTER -->
    <section class="ed-section" id="slashing-register">
      <div class="ed-sec-head">
        <div class="sec-badge-col">
          <span class="sec-giant-num">04</span>
          <span class="sec-kicker">// PROTOCOL DISCIPLINE</span>
        </div>
        <div>
          <h2 class="sec-title">Byzantine Slashing Proof Register &amp; Cryptographic SLA</h2>
          <p class="sec-summary">
            The Singularity Protocol enforces cryptographic finality discipline. Any node operator attempting to falsify inference logits, equivocate across slots, or forge hardware attestations is subjected to autonomous on-chain slashing.
          </p>
        </div>
      </div>

      <!-- SLASHING TABLE -->
      <div class="ed-table-wrap">
        <table class="ed-table">
          <thead>
            <tr>
              <th>Offense Category</th>
              <th>Detection Trigger</th>
              <th>Cryptographic Verification Proof</th>
              <th>Penalty (% Stake Slashed)</th>
              <th>Cooldown Freeze</th>
              <th>Token Route Allocation</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="accent">EQUIVOCATION / DOUBLE-SIGNING</td>
              <td>Conflicting slot headers</td>
              <td>Two distinct Ed25519 signatures for same slot index</td>
              <td class="accent">100% COLLATERAL BURN</td>
              <td>Permanent Blacklist</td>
              <td>70% Insurance Vault // 30% Incinerator</td>
            </tr>
            <tr>
              <td class="accent">TENSOR WEIGHT POISONING</td>
              <td>Deterministic logit divergence</td>
              <td>Bitwise state divergence vector ($\Delta\epsilon &gt; 0.00$)</td>
              <td class="accent">100% COLLATERAL BURN</td>
              <td>Permanent Blacklist</td>
              <td>70% Insurance Vault // 30% Incinerator</td>
            </tr>
            <tr>
              <td class="accent">HARDWARE ATTESTATION FORGERY</td>
              <td>Invalid TEE signature</td>
              <td>Broken DCAP / SPDM X.509 certificate chain</td>
              <td class="accent">100% COLLATERAL BURN</td>
              <td>Permanent Blacklist</td>
              <td>100% Solana Incinerator Burn</td>
            </tr>
            <tr>
              <td class="accent">DETERMINISM DRIFT (&Delta;&epsilon; &gt; 0.00)</td>
              <td>Interactive bisection mismatch</td>
              <td>SVM RISC-V layer execution trace proof</td>
              <td>50% COLLATERAL BURN</td>
              <td>90 Epochs Unbonding Freeze</td>
              <td>80% Insurance Vault // 20% Incinerator</td>
            </tr>
            <tr>
              <td class="accent">LIVENESS / HEARTBEAT TIMEOUT</td>
              <td>Missed &gt; 3 consecutive epochs</td>
              <td>Anchor slot timeout challenge proof</td>
              <td>5% PROGRESSIVE SLASH</td>
              <td>14 Epochs (Jail Status)</td>
              <td>100% Protocol Insurance Vault</td>
            </tr>
            <tr>
              <td class="accent">ZK-PROOF SUBMISSION TIMEOUT</td>
              <td>Failure to deliver proof &gt; 12 slots</td>
              <td>Anchor slot clock expiration receipt</td>
              <td>10% TASK PENALTY</td>
              <td>7 Epochs Suspension</td>
              <td>50% Insurance // 50% Incinerator</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="math-callout">
        <div class="math-callout-title">// ESCALATING BYZANTINE SLASHING FORMULA</div>
        $$S_{\text{slash}}(\text{offense}) = S_{\text{base}} \times \left(1 + \mu \cdot \frac{N_{\text{byzantine}}}{K}\right)$$
        Where $S_{\text{base}}$ is the base penalty fraction, $K = 64$ is committee size, $N_{\text{byzantine}}$ is the number of co-violators detected in the current epoch, and escalation factor $\mu = 3.0$. If correlated Byzantine behavior is detected across multiple nodes, penalties rapidly compound toward 100% total burn.
      </div>
    </section>

    <!-- SECTION 05: P2P GOSSIP & NETWORK TOPOLOGY -->
    <section class="ed-section" id="p2p-topology">
      <div class="ed-sec-head">
        <div class="sec-badge-col">
          <span class="sec-giant-num">05</span>
          <span class="sec-kicker">// NETWORK LAYER</span>
        </div>
        <div>
          <h2 class="sec-title">P2P Network Topology &amp; libp2p Gossip Protocol</h2>
          <p class="sec-summary">
            Inter-node communications operate over a high-throughput libp2p Gossipsub v1.1 mesh mapped onto a continuous Gromov $\delta$-hyperbolic Riemannian metric space $\mathbb{H}^2$.
          </p>
        </div>
      </div>

      <div class="ed-prose-cols">
        <div class="prose-block">
          <h3>Gossipsub v1.1 Configuration</h3>
          <p>
            The protocol enforces a dynamic mesh degree $D = 8$, with lower bound $D_{\text{low}} = 6$ and upper bound $D_{\text{high}} = 12$. A gossip fanout degree $D_{\text{lazy}} = 6$ ensures that transaction broadcasts and inference requests propagate across the entire global network within 120 milliseconds.
          </p>
          <p>
            Heartbeat intervals are tuned to $\tau_{\text{heartbeat}} = 100\text{ ms}$. Peer scoring continuously prunes slow or non-responsive links using exponential decay weighting based on verified delivery latency.
          </p>
        </div>
        <div class="prose-block">
          <h3>Hyperbolic Coordinate Assignment</h3>
          <p>
            Each validator node is assigned fixed radial and angular coordinates $(r, \theta)$ on the Poincaré disk model of $\mathbb{H}^2$. Distance calculations between node $u$ and node $v$ follow the hyperbolic metric:
          </p>
          <p style="font-family:var(--fm); font-size:13px; color:var(--chalk);">
            $$d_{\mathbb{H}}(u, v) = \text{arcosh}\left(1 + 2\frac{\|u - v\|^2}{(1 - \|u\|^2)(1 - \|v\|^2)}\right)$$
          </p>
          <p>
            Greedy hyperbolic routing guarantees message delivery in $O(\log N)$ hops with mathematically proven immunity to routing table saturation attacks.
          </p>
        </div>
      </div>
    </section>

    <!-- SECTION 06: INTERACTIVE YIELD ESTIMATOR -->
    <section class="ed-section" id="yield-estimator">
      <div class="ed-sec-head">
        <div class="sec-badge-col">
          <span class="sec-giant-num">06</span>
          <span class="sec-kicker">// ECONOMIC SIMULATION</span>
        </div>
        <div>
          <h2 class="sec-title">Interactive Compute Yield &amp; Revenue Estimator</h2>
          <p class="sec-summary">
            Simulate protocol emissions and estimated operational returns across different GPU hardware configurations, current network difficulty, and collateral staking allocations.
          </p>
        </div>
      </div>

      <div class="calc-matrix-grid">
        <div class="calc-controls">
          <div class="calc-field">
            <label for="calc-gpu">Select Hardware Architecture</label>
            <select id="calc-gpu" onchange="updateNodeYield()">
              <option value="tier1">Tier 1: 1x RTX 4090 24GB (450W, 1,000 $33RD Stake)</option>
              <option value="tier2">Tier 2: 4x A100 80GB SXM4 (1,600W, 5,000 $33RD Stake)</option>
              <option value="tier3" selected>Tier 3: 8x H100 80GB SXM5 (5,600W, 25,000 $33RD Stake)</option>
              <option value="tier4">Tier 4: 32x H100 Datacenter Pod (35kW, 100,000 $33RD Stake)</option>
            </select>
          </div>
          <div class="calc-field">
            <label for="token-price-sim">Simulated Token Price ($33RD / USD)</label>
            <input type="number" id="token-price-sim" value="3.30" step="0.10" min="0.10" oninput="updateNodeYield()">
          </div>
          <div class="calc-field">
            <label for="power-cost-sim">Electricity Cost ($ / kWh)</label>
            <input type="number" id="power-cost-sim" value="0.08" step="0.01" min="0.01" oninput="updateNodeYield()">
          </div>
        </div>

        <div class="calc-outputs">
          <div class="out-metric-row">
            <span class="out-metric-lbl">Daily Token Emission</span>
            <span class="out-metric-val accent" id="yield-tokens-day">640.80 $33RD</span>
          </div>
          <div class="out-metric-row">
            <span class="out-metric-lbl">Gross Monthly Revenue</span>
            <span class="out-metric-val" id="yield-usd-month">$63,439.20</span>
          </div>
          <div class="out-metric-row">
            <span class="out-metric-lbl">Monthly Electricity Cost</span>
            <span class="out-metric-val" id="yield-power-month">-$322.56</span>
          </div>
          <div class="out-metric-row">
            <span class="out-metric-lbl">Net Estimated APY</span>
            <span class="out-metric-val green" id="yield-net-apy">91.8%</span>
          </div>
        </div>
      </div>
    </section>
  </main>

  <script>
    const TIER_DATA = {
      tier1: { tokensPerDay: 18.4, stake: 1000, powerWatts: 450 },
      tier2: { tokensPerDay: 94.2, stake: 5000, powerWatts: 1600 },
      tier3: { tokensPerDay: 640.8, stake: 25000, powerWatts: 5600 },
      tier4: { tokensPerDay: 2680.0, stake: 100000, powerWatts: 35000 }
    };

    function updateNodeYield() {
      const tierKey = document.getElementById('calc-gpu').value;
      const price = parseFloat(document.getElementById('token-price-sim').value) || 3.30;
      const powerRate = parseFloat(document.getElementById('power-cost-sim').value) || 0.08;
      const tier = TIER_DATA[tierKey];

      const dailyTokens = tier.tokensPerDay;
      const monthlyTokens = dailyTokens * 30;
      const grossMonthUsd = monthlyTokens * price;

      // Electricity: (watts * 24 * 30) / 1000 * rate
      const kwhMonth = (tier.powerWatts * 24 * 30) / 1000;
      const powerCostMonth = kwhMonth * powerRate;

      const netMonthUsd = grossMonthUsd - powerCostMonth;
      const netYearUsd = netMonthUsd * 12;
      const stakeValueUsd = tier.stake * price;
      const netApy = ((netYearUsd / stakeValueUsd) * 100).toFixed(1);

      document.getElementById('yield-tokens-day').innerText = dailyTokens.toFixed(2) + ' $33RD';
      document.getElementById('yield-usd-month').innerText = '$' + grossMonthUsd.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2});
      document.getElementById('yield-power-month').innerText = '-$' + powerCostMonth.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2});
      document.getElementById('yield-net-apy').innerText = netApy + '%';
    }
    updateNodeYield();
  </script>
"""
    foot = get_footer()
    full_html = head + body + foot
    
    with open(os.path.join(SITE_DIR, "nodes.html"), "w", encoding="utf-8") as f:
        f.write(full_html)
    print("Successfully built nodes.html!")

if __name__ == "__main__":
    build_nodes()
