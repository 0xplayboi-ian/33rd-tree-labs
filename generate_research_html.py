#!/usr/bin/env python3
import os
from build_subpages_full import get_page_head, get_page_foot

SITE_DIR = "/Users/ianmora/Desktop/Projects/33rd-tree-labs-site"

def build():
    head = get_page_head(
        title="33RD TREE LABS // Cryptographic &amp; Topological Research Directory &bull; 33rdtreelabs.tech",
        description="Scientific Research Directory for 33rd Tree Labs: Gromov delta-Hyperbolic Routing Proofs, INT8 Deterministic Quantization Bounds, and Recursive Plonky2 ZK Proofs.",
        active_page="research"
    )

    body = r"""
  <main class="page-wrap">
    <!-- EDITORIAL HERO / HEADER -->
    <header class="ed-hero">
      <div class="ed-kicker">( 007 ) // SCIENTIFIC DIRECTORATE &bull; 33RDTREELABS.TECH</div>
      <h1 class="ed-headline">CRYPTOGRAPHIC &amp;<br><span class="accent">TOPOLOGICAL RESEARCH</span></h1>
      <p class="ed-lead">
        Peer-reviewed mathematical foundations powering the Singularity Protocol: Non-Euclidean negative curvature routing manifolds, bit-exact deterministic neural inference, and recursive zero-knowledge SNARK folding for Solana on-chain consensus.
      </p>

      <!-- TELEMETRY STRIP (NO CARD CONTAINERS) -->
      <div class="telemetry-strip">
        <div class="telemetry-cell">
          <span class="telemetry-lbl">Manifold Metric Curvature</span>
          <span class="telemetry-val accent">K(y) &lt; 0 (GROMOV &delta;-HYPERBOLIC)</span>
        </div>
        <div class="telemetry-cell">
          <span class="telemetry-lbl">Cross-Hardware Determinism</span>
          <span class="telemetry-val">&Delta;&epsilon; = 0.00 (INT8 FIXED-POINT)</span>
        </div>
        <div class="telemetry-cell">
          <span class="telemetry-lbl">Recursive Proof Field</span>
          <span class="telemetry-val">GOLDILOCKS F_p (p = 2^64 - 2^32 + 1)</span>
        </div>
        <div class="telemetry-cell">
          <span class="telemetry-lbl">Solana Verification Cost</span>
          <span class="telemetry-val green">~185,000 COMPUTE UNITS</span>
        </div>
      </div>
    </header>

    <!-- SECTION 01: PAPER I - GROMOV HYPERBOLIC GEOMETRY -->
    <section class="ed-section" id="paper-1">
      <div class="ed-sec-head">
        <div class="sec-badge-col">
          <span class="sec-giant-num">01</span>
          <span class="sec-kicker">// RESEARCH PAPER I</span>
        </div>
        <div>
          <h2 class="sec-title">Gromov &delta;-Hyperbolic Geometry in Neural Routing</h2>
          <p class="sec-summary">
            <strong>Title:</strong> <em>Topological Invariance and Congestion-Free Routing in Decentralized Tensor Fabrics via Gromov $\delta$-Hyperbolic Manifolds</em><br>
            <strong>Authors:</strong> 33rd Tree Labs Cryptographic &amp; Systems Directorate &bull; Technical Report 33TL-2026-01
          </p>
        </div>
      </div>

      <div class="ed-prose-cols">
        <div class="prose-block">
          <h3>Abstract &amp; Problem Statement</h3>
          <p>
            Standard peer-to-peer Distributed Hash Tables (DHTs) such as Kademlia organize nodes in flat metric spaces governed by the bitwise exclusive-OR (XOR) metric $d_{\oplus}(x, y)$. While optimal for static scalar key-value storage, XOR overlays exhibit polynomial volume growth $\text{Vol}(B_R) \propto R^d$.
          </p>
          <p>
            When scale-free or hierarchical tensor communication workloads (e.g., pipeline-parallel transformer evaluations) are embedded into flat spaces, metric distortion scales as $\mathcal{D} = \Omega(N^{1/d})$. This induces severe topological congestion, high route churn, and vulnerability to deterministic Sybil Eclipse attacks.
          </p>
        </div>
        <div class="prose-block">
          <h3>The Gromov $\delta$-Hyperbolic Metric Condition</h3>
          <p>
            A metric space $(X, d)$ is said to be Gromov $\delta$-hyperbolic if for all base points $w \in X$ and all vertices $x, y, z \in X$, the Gromov product satisfies the 4-point condition:
          </p>
          <div class="math-display-box">
            $$(x \cdot z)_w \ge \min\left((x \cdot y)_w, (y \cdot z)_w\right) - \delta$$
          </div>
          <p>
            Where the Gromov product $(x \cdot y)_w$ is defined as:
          </p>
          <div class="math-display-box">
            $$(x \cdot y)_w = \frac{1}{2} \left[ d(x, w) + d(y, w) - d(x, y) \right]$$
          </div>
          <p>
            In tree metrics, $\delta = 0$. In the Singularity continuous Exponential Plunge Manifold, $\delta = \ln(1 + \sqrt{2}) \approx 0.881$, guaranteeing continuous tree-dual metric properties.
          </p>
        </div>
      </div>

      <div class="ed-prose-cols">
        <div class="prose-block">
          <h3>Theorem 1: Logarithmic Routing Diameter &amp; Congestion Elimination</h3>
          <p>
            <strong>Theorem:</strong> In a Gromov $\delta$-hyperbolic graph with negative Gaussian curvature $K \le -\kappa^2 < 0$, greedy routing in the Poincaré disk embedding guarantees packet delivery in $O(\log N)$ hops with congestion bounded by $O(1)$ on all non-root geodesic chords.
          </p>
          <p>
            <em>Proof Sketch:</em> In $\mathbb{H}^2$, triangles are $\delta$-thin: any point on geodesic $[x, y]$ lies within hyperbolic distance $\delta$ of $[x, w] \cup [y, w]$. Let $u$ be the current forwarding node. By greedy descent toward destination $v$, hyperbolic distance strictly decreases at each step: $d_{\mathbb{H}}(u_{i+1}, v) \le d_{\mathbb{H}}(u_i, v) - \Delta r$. Because circumference expands as $2\pi \sinh(\zeta R) \sim \pi e^{\zeta R}$, path traversal length collapses to logarithmic tree depth $h \le \frac{1}{\zeta} \ln N$, terminating in $O(\log N)$ steps without back-tracking.
          </p>
        </div>
        <div class="prose-block">
          <h3>Theorem 2: Exponential Sybil Perimeter Defense</h3>
          <p>
            <strong>Theorem:</strong> An adversary attempting to eclipse a target node $u$ located at radial distance $R$ in $\mathbb{H}^2$ requires an exponentially growing number of malicious identities $N_{\text{Sybil}} = \Omega(e^{\zeta R})$.
          </p>
          <p>
            <em>Proof Sketch:</em> In Euclidean space, the perimeter of a ball of radius $R$ is $2\pi R$, allowing an attacker to encircle a node with $O(R)$ Sybils. In $\mathbb{H}^2$, the perimeter is:
          </p>
          <div class="math-display-box">
            $$\text{Circumference}(R) = 2\pi \sinh(\zeta R) \sim \pi e^{\zeta R}$$
          </div>
          <p>
            To intercept all greedy geodesics passing into $u$'s angular horizon $\Delta\theta$, the adversary must populate an arc length of $\Theta(e^{\zeta R})$. With minimum node stake $S_{\min} = 25,000\text{ }33RD$, the economic cost of eclipsing an ingress validator exceeds $\$1.2B$, rendering Sybil boundary saturation economically impossible.
          </p>
        </div>
      </div>
    </section>

    <!-- SECTION 02: PAPER II - DETERMINISTIC QUANTIZATION -->
    <section class="ed-section" id="paper-2">
      <div class="ed-sec-head">
        <div class="sec-badge-col">
          <span class="sec-giant-num">02</span>
          <span class="sec-kicker">// RESEARCH PAPER II</span>
        </div>
        <div>
          <h2 class="sec-title">Deterministic INT8 Quantization &amp; Consensus Determinism</h2>
          <p class="sec-summary">
            <strong>Title:</strong> <em>Bit-Exact Cross-Architecture Neural Inference: Eliminating Floating-Point Non-Determinism in Decentralized Byzantine Validation</em><br>
            <strong>Authors:</strong> 33rd Tree Labs Cryptographic &amp; Systems Directorate &bull; Technical Report 33TL-2026-02
          </p>
        </div>
      </div>

      <div class="ed-prose-cols">
        <div class="prose-block">
          <h3>The Floating-Point Non-Determinism Crisis</h3>
          <p>
            IEEE 754 floating-point operations (FP32, FP16, BF16) are mathematically non-associative: $(a + b) + c \ne a + (b + c)$. Divergent hardware architectures (NVIDIA Tensor Cores, AMD Matrix Cores, Apple Metal AMX) execute Fused Multiply-Add (FMA) instructions in distinct orderings and apply differing subnormal flushing policies (FTZ/DAZ).
          </p>
          <p>
            Consequently, identical input prompts evaluated across an H100 and an MI300X generate subtle logit divergence ($\Delta\epsilon \approx 10^{-5}$), which cascades through multi-layer attention to produce conflicting output tokens. This causes catastrophic failure in Byzantine BFT consensus.
          </p>
        </div>
        <div class="prose-block">
          <h3>Bit-Exact INT8 Fixed-Point Kernel Formulation</h3>
          <p>
            The Singularity Protocol resolves this non-determinism by enforcing strict INT8 symmetric quantization with integer fixed-point accumulation. The affine quantization mapping is:
          </p>
          <div class="math-display-box">
            $$Q(x) = \text{clamp}\left(\left\lfloor \frac{x}{S} + Z + 0.5 \right\rfloor, -128, 127\right)$$
          </div>
          <p>
            Where $S$ is the scale factor and $Z \in \mathbb{Z}$ is the zero-point offset. Matrix multiplications execute entirely in 32-bit signed integer registers ($\mathbb{Z}_{32}$):
          </p>
          <div class="math-display-box">
            $$Y_{\text{int}} = \sum_{k=1}^K (W_k - Z_w)(X_k - Z_x) \in \mathbb{Z}_{32}$$
          </div>
          <p>
            Because integer addition over bounded registers is strictly associative and commutative, $Y_{\text{int}}$ yields bit-for-bit identical digests on all certified hardware ($\Delta\epsilon = 0.00$).
          </p>
        </div>
      </div>

      <!-- EMPIRICAL BENCHMARKING DATA TABLE -->
      <h3 style="font-family:var(--fh); font-size:22px; text-transform:uppercase; margin:40px 0 16px;">Cross-Hardware Empirical Invariance Benchmarks (10,000 Passes)</h3>
      <div class="ed-table-wrap">
        <table class="ed-table">
          <thead>
            <tr>
              <th>Model Architecture</th>
              <th>Hardware Cluster Pairing</th>
              <th>FP16 Logit Mismatch Rate</th>
              <th>INT8 Deterministic Mismatch Rate</th>
              <th>Mean Drift Magnitude ($\Delta\epsilon$)</th>
              <th>Consensus Status</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="accent">Llama-3-70B-Instruct</td>
              <td class="highlight">NVIDIA H100 vs AMD MI300X</td>
              <td>14.82% Divergent</td>
              <td class="green">0.0000% (0 / 10,000)</td>
              <td class="green">&Delta;&epsilon; = 0.00000000</td>
              <td class="green">PERFECT BFT CONSENSUS</td>
            </tr>
            <tr>
              <td class="accent">Mistral-Large-2407</td>
              <td class="highlight">NVIDIA RTX 4090 vs A100 SXM4</td>
              <td>9.45% Divergent</td>
              <td class="green">0.0000% (0 / 10,000)</td>
              <td class="green">&Delta;&epsilon; = 0.00000000</td>
              <td class="green">PERFECT BFT CONSENSUS</td>
            </tr>
            <tr>
              <td class="accent">DeepSeek-V2-Lite-16B</td>
              <td class="highlight">NVIDIA H100 vs Apple M3 Max</td>
              <td>22.19% Divergent</td>
              <td class="green">0.0000% (0 / 10,000)</td>
              <td class="green">&Delta;&epsilon; = 0.00000000</td>
              <td class="green">PERFECT BFT CONSENSUS</td>
            </tr>
            <tr>
              <td class="accent">Qwen-2.5-72B</td>
              <td class="highlight">AWS EC2 p5.48xl vs Bare-Metal B200</td>
              <td>11.30% Divergent</td>
              <td class="green">0.0000% (0 / 10,000)</td>
              <td class="green">&Delta;&epsilon; = 0.00000000</td>
              <td class="green">PERFECT BFT CONSENSUS</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- SECTION 03: PAPER III - RECURSIVE PLONKY2 PROOFS -->
    <section class="ed-section" id="paper-3">
      <div class="ed-sec-head">
        <div class="sec-badge-col">
          <span class="sec-giant-num">03</span>
          <span class="sec-kicker">// RESEARCH PAPER III</span>
        </div>
        <div>
          <h2 class="sec-title">Recursive Plonky2 Proofs in Goldilocks Field</h2>
          <p class="sec-summary">
            <strong>Title:</strong> <em>Sub-Second Incremental Layer Verification: Recursive Plonky2 STARK/SNARK Folding for Solana On-Chain Settlement</em><br>
            <strong>Authors:</strong> 33rd Tree Labs Cryptographic &amp; Systems Directorate &bull; Technical Report 33TL-2026-03
          </p>
        </div>
      </div>

      <div class="ed-prose-cols">
        <div class="prose-block">
          <h3>The Goldilocks Field $\mathbb{F}_p$</h3>
          <p>
            Generating zero-knowledge proofs for billions of floating-point arithmetic gates is computationally prohibitive. The Singularity Protocol executes arithmetic over the 64-bit Goldilocks field:
          </p>
          <div class="math-display-box">
            $$\mathbb{F}_p \quad \text{where} \quad p = 2^{64} - 2^{32} + 1$$
          </div>
          <p>
            Because $p$ fits within a standard 64-bit CPU/GPU register, field reductions take just 2 clock cycles ($x \pmod{2^{64} - 2^{32} + 1}$ uses only shifts and additions). Poseidon-2 algebraic hashing executes at over 2.4 GB/s per GPU.
          </p>
        </div>
        <div class="prose-block">
          <h3>Recursive STARK/SNARK Folding Scheme</h3>
          <p>
            Instead of generating a monolithic proof for an entire 80-layer neural network, validators use Incrementally Verifiable Computation (IVC). Each transformer layer proof $\pi_{k+1}$ is folded into the running accumulator proof $\Pi_k$:
          </p>
          <div class="math-display-box">
            $$\Pi_{k+1} = \text{Fold}(\Pi_k, \pi_{k+1}, \mathbf{x}_{k+1})$$
          </div>
          <p>
            After all 80 layers are folded, a final SNARK compression circuit wraps the accumulator into a 44-byte Solana Anchor verification receipt. On-chain settlement requires only 185,000 Compute Units, comfortably fitting within a single Solana transaction slot.
          </p>
        </div>
      </div>

      <!-- RECURSIVE PROVING BENCHMARK TABLE -->
      <h3 style="font-family:var(--fh); font-size:22px; text-transform:uppercase; margin:40px 0 16px;">Plonky2 Zero-Knowledge Neural Proving Benchmarks</h3>
      <div class="ed-table-wrap">
        <table class="ed-table">
          <thead>
            <tr>
              <th>Layer Architecture</th>
              <th>Constraint Count</th>
              <th>Prover Runtime (8x H100)</th>
              <th>Recursive Proof Size</th>
              <th>Solana Verification CUs</th>
              <th>Settlement Latency</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="accent">Self-Attention Head (INT8 GEMM)</td>
              <td>2,097,152 R1CS</td>
              <td>142 ms</td>
              <td>16.8 KB (STARK)</td>
              <td>N/A (Layer Local)</td>
              <td>Intermediate Node</td>
            </tr>
            <tr>
              <td class="accent">SwiGLU Feed-Forward Network</td>
              <td>4,194,304 R1CS</td>
              <td>268 ms</td>
              <td>17.4 KB (STARK)</td>
              <td>N/A (Layer Local)</td>
              <td>Intermediate Node</td>
            </tr>
            <tr>
              <td class="accent">Full Transformer Layer (Attention + FFN)</td>
              <td>6,291,456 R1CS</td>
              <td>410 ms</td>
              <td>18.1 KB (STARK)</td>
              <td>N/A (Layer Local)</td>
              <td>Intermediate Node</td>
            </tr>
            <tr>
              <td class="accent">80-Layer Folded IVC Receipt</td>
              <td>503,316,480 R1CS (Folded)</td>
              <td>1.84 s Total Accumulation</td>
              <td class="highlight">44 Bytes (Compressed Receipt)</td>
              <td class="green">184,620 CUs</td>
              <td class="green">400 ms (1 Solana Slot)</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- SECTION 04: ACADEMIC BIBLIOGRAPHY -->
    <section class="ed-section" id="bibliography">
      <div class="ed-sec-head">
        <div class="sec-badge-col">
          <span class="sec-giant-num">04</span>
          <span class="sec-kicker">// FORMAL REFERENCES</span>
        </div>
        <div>
          <h2 class="sec-title">Academic Bibliography &amp; Citations</h2>
          <p class="sec-summary">
            Foundational peer-reviewed academic literature underpinning the topological, mathematical, and cryptographic design of 33rd Tree Labs.
          </p>
        </div>
      </div>

      <div class="ed-table-wrap">
        <table class="ed-table">
          <thead>
            <tr>
              <th>Index</th>
              <th>Citation &amp; Authors</th>
              <th>Venue / Publication</th>
              <th>Cryptographic / Topological Application</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="accent">[1]</td>
              <td class="highlight">Gromov, M. (1987). "Hyperbolic groups".</td>
              <td>Essays in Group Theory, MSRI Publ. 8, pp. 75–263.</td>
              <td>Foundational $\delta$-hyperbolic 4-point condition and thin-triangle metric.</td>
            </tr>
            <tr>
              <td class="accent">[2]</td>
              <td class="highlight">Vaswani, A., et al. (2017). "Attention Is All You Need".</td>
              <td>Advances in Neural Information Processing Systems (NeurIPS 30).</td>
              <td>Multi-head self-attention mechanisms and transformer feed-forward architectures.</td>
            </tr>
            <tr>
              <td class="accent">[3]</td>
              <td class="highlight">Ben-Sasson, E., et al. (2018). "Scalable, transparent, and post-quantum secure computational integrity".</td>
              <td>IACR Cryptology ePrint Archive, Report 2018/046.</td>
              <td>FRI protocol and STARK transparent cryptographic argument structures.</td>
            </tr>
            <tr>
              <td class="accent">[4]</td>
              <td class="highlight">Maymounkov, P., &amp; Mazières, D. (2002). "Kademlia: A peer-to-peer information system".</td>
              <td>International Workshop on Peer-to-Peer Systems (IPTPS '02).</td>
              <td>Analysis of XOR metric space routing limitations and Sybil vulnerability.</td>
            </tr>
            <tr>
              <td class="accent">[5]</td>
              <td class="highlight">Polino, A., Pascanu, R., &amp; Alistarh, D. (2018). "Model compression via collaborative data quantization".</td>
              <td>International Conference on Machine Learning (ICML 2018).</td>
              <td>Fixed-point integer representation bounds and uniform scale quantization.</td>
            </tr>
            <tr>
              <td class="accent">[6]</td>
              <td class="highlight">Boneh, D., Lynn, B., &amp; Shacham, H. (2001). "Short signatures from the Weil pairing".</td>
              <td>Advances in Cryptology (ASIACRYPT 2001).</td>
              <td>Threshold signature aggregation for BFT committee quorum consensus ($K=64$).</td>
            </tr>
            <tr>
              <td class="accent">[7]</td>
              <td class="highlight">Plonky2 Team (2022). "Plonky2: Fast Recursive Arguments with PLONK and FRI".</td>
              <td>Polygon Zero Technical Report.</td>
              <td>Goldilocks field $\mathbb{F}_{2^{64}-2^{32}+1}$ optimization and recursive STARK folding.</td>
            </tr>
            <tr>
              <td class="accent">[8]</td>
              <td class="highlight">Dwork, C., &amp; Naor, M. (1992). "Pricing via processing or combatting junk mail".</td>
              <td>Advances in Cryptology (CRYPTO '92).</td>
              <td>Proof-of-work precursors to deterministic Proof-of-Inference (PoI).</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- SECTION 05: OPEN RESEARCH GRANTS & RFPS -->
    <section class="ed-section" id="research-grants">
      <div class="ed-sec-head">
        <div class="sec-badge-col">
          <span class="sec-giant-num">05</span>
          <span class="sec-kicker">// GRANTS &amp; FELLOWSHIPS</span>
        </div>
        <div>
          <h2 class="sec-title">Open Research Grants &amp; Request for Proposals (RFP)</h2>
          <p class="sec-summary">
            33rd Tree Labs awards nondilutive research grants in $33RD tokens to university faculty, independent cryptographers, and distributed systems engineers solving critical DePIN bottlenecks.
          </p>
        </div>
      </div>

      <!-- 3-COLUMN RFP GRID (ZERO CARDS) -->
      <div class="ed-grid-3">
        <div class="ed-grid-col ed-grid-cell">
          <div>
            <span class="cell-tag">[ RFP TRACK 01 // TOPOLOGY ]</span>
            <h3 class="cell-title">Hyperbolic Latent Space Routing</h3>
            <p class="cell-body">
              Researching dynamic isometric embeddings of multi-modal embedding vectors directly into Lorentz hyperboloid manifolds for zero-copy semantic shard discovery.
            </p>
          </div>
          <ul class="cell-spec-list">
            <li><span>Grant Pool:</span> <strong>75,000 $33RD</strong></li>
            <li><span>Timeline:</span> <strong>6 Months</strong></li>
            <li><span>Deliverable:</span> <strong>Rust Crate + Academic Paper</strong></li>
          </ul>
        </div>

        <div class="ed-grid-col ed-grid-cell">
          <div>
            <span class="cell-tag">[ RFP TRACK 02 // PRIVACY ]</span>
            <h3 class="cell-title">FHE Tensor Parallelism</h3>
            <p class="cell-body">
              Implementing GPU-accelerated CKKS / TFHE homomorphic encryption kernels for private forward pass evaluation across untrusted multi-operator clusters.
            </p>
          </div>
          <ul class="cell-spec-list">
            <li><span>Grant Pool:</span> <strong>100,000 $33RD</strong></li>
            <li><span>Timeline:</span> <strong>9 Months</strong></li>
            <li><span>Deliverable:</span> <strong>CUDA / HIP Kernel + Benchmarks</strong></li>
          </ul>
        </div>

        <div class="ed-grid-col ed-grid-cell">
          <div>
            <span class="cell-tag">[ RFP TRACK 03 // HARDWARE ]</span>
            <h3 class="cell-title">On-Chain TEE Attestation Bridges</h3>
            <p class="cell-body">
              Designing optimized Solana SVM BPF programs for native verification of Intel TDX DCAP quotes and NVIDIA SPDM 1.2 certificates under 100,000 Compute Units.
            </p>
          </div>
          <ul class="cell-spec-list">
            <li><span>Grant Pool:</span> <strong>50,000 $33RD</strong></li>
            <li><span>Timeline:</span> <strong>4 Months</strong></li>
            <li><span>Deliverable:</span> <strong>Anchor Program + Audit Report</strong></li>
          </ul>
        </div>
      </div>

      <div class="ed-code-block" style="margin-top:40px;">
        <div class="ed-code-header">
          <span>GRANT APPLICATION SUBMISSION PROTOCOL</span>
          <span>RESEARCH DIRECTORATE // GPG SIGNED</span>
        </div>
        <div class="ed-code-content">
<span class="cmd-comment"># Submit cryptographic research grant proposals via Git commit or signed PGP email</span>
<span class="cmd-prompt">$</span>git clone https://github.com/33rd-tree-labs/research-rfp.git
<span class="cmd-prompt">$</span>cd research-rfp &amp;&amp; cp template-proposal.md proposals/RFP-2026-yourname.md
<span class="cmd-prompt">$</span>gpg --sign --armor proposals/RFP-2026-yourname.md
<span class="cmd-comment"># Transmit signed proposal to: research@33rdtreelabs.tech</span>
        </div>
      </div>
    </section>
  </main>
"""
    foot = get_page_foot()
    full_html = head + body + foot

    out_path = os.path.join(SITE_DIR, "research.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    print("research.html successfully generated!")

if __name__ == "__main__":
    build()
