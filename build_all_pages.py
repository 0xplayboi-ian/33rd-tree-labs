#!/usr/bin/env python3
import os

SITE_DIR = "/Users/ianmora/Desktop/Projects/33rd-tree-labs-site"
WS_SITE_DIR = "/Users/ianmora/ai stuffs/333rd/site"
DESKTOP_3D = "/Users/ianmora/Desktop/33RD_TREE_LABS_3D"

with open(os.path.join(SITE_DIR, "logo_mark.svg"), "r") as f:
    logo_svg = f.read().strip()

# Base CSS shared across all pages
shared_css = """
:root {
    --orange: #FF4500;
    --orange-bright: #FF5E1E;
    --orange-glow: rgba(255, 69, 0, 0.45);
    --orange-subtle: rgba(255, 69, 0, 0.12);
    --bg: #030306;
    --bg-elevated: #09090E;
    --bg-panel: rgba(14, 14, 20, 0.85);
    --border: #22222E;
    --text-main: #FFFFFF;
    --text-muted: #9CA3AF;
    --text-dark: #6B7280;
    --white: #FFFFFF;
    --green: #00FF66;
}

* { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; background: var(--bg); color: var(--text-main); font-family: 'Space Grotesk', -apple-system, sans-serif; }
body {
    position: relative;
    min-height: 100vh;
    line-height: 1.6;
    background-color: var(--bg);
    background-image: 
        radial-gradient(circle at 50% 0%, rgba(255, 69, 0, 0.15), transparent 45%),
        linear-gradient(to right, rgba(255, 255, 255, 0.02) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
    background-size: 100% 100%, 60px 60px, 60px 60px;
}

/* TOP TELEMETRY BAR */
.telemetry-bar {
    position: fixed; top: 0; left: 0; width: 100%; height: 42px;
    background: rgba(8, 8, 12, 0.94); backdrop-filter: blur(14px);
    border-bottom: 1px solid var(--border); display: flex; align-items: center;
    justify-content: space-between; padding: 0 28px; z-index: 1000;
    font-family: 'JetBrains Mono', monospace; font-size: 11px; letter-spacing: 0.5px;
}
.live-dot {
    display: inline-block; width: 7px; height: 7px; background: var(--green);
    border-radius: 50%; box-shadow: 0 0 10px var(--green); animation: pulse-dot 1.5s infinite;
}
@keyframes pulse-dot { 0%, 100% { opacity: 1; } 50% { opacity: 0.4; } }

/* HEADER */
header.site-nav {
    position: fixed; top: 42px; left: 0; width: 100%; height: 72px;
    display: flex; align-items: center; justify-content: space-between;
    padding: 0 32px; background: rgba(3, 3, 6, 0.85); backdrop-filter: blur(20px);
    border-bottom: 1px solid rgba(255, 255, 255, 0.05); z-index: 990;
}
.brand-logo-wrap { display: flex; align-items: center; gap: 14px; text-decoration: none; color: #FFF; }
.logo-symbol {
    width: 44px; height: 44px; border: 1px solid var(--orange); border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    background: radial-gradient(circle, rgba(255,69,0,0.22), #000);
    box-shadow: 0 0 16px var(--orange-glow); padding: 4px;
}
.logo-symbol svg { width: 100%; height: 100%; }
.brand-name { font-family: 'JetBrains Mono', monospace; font-size: 16px; font-weight: 900; letter-spacing: 1.5px; color: #FFF; white-space: nowrap; }
.brand-sub { font-family: 'JetBrains Mono', monospace; font-size: 9px; font-weight: 700; letter-spacing: 1.5px; color: var(--orange); white-space: nowrap; }

.nav-links {
    display: flex; align-items: center; gap: 24px; list-style: none;
    font-family: 'JetBrains Mono', monospace; font-size: 12px; font-weight: 600;
}
.nav-links a { color: var(--text-muted); text-decoration: none; transition: color 0.2s; position: relative; padding: 6px 0; }
.nav-links a:hover, .nav-links a.active { color: #FFF; }
.nav-links a.active::after { content: ''; position: absolute; bottom: 0; left: 0; width: 100%; height: 2px; background: var(--orange); }

.nav-cta {
    background: var(--orange); color: #000 !important; font-weight: 800;
    padding: 8px 18px !important; border-radius: 6px; box-shadow: 0 0 18px var(--orange-glow);
}
.nav-cta:hover { background: #FFF !important; transform: translateY(-1px); }

/* MAIN CONTENT CONTAINER */
.page-container {
    max-width: 1200px; margin: 0 auto; padding: 150px 6vw 100px;
}
.page-tag { font-family: 'JetBrains Mono', monospace; font-size: 11px; font-weight: 800; letter-spacing: 2px; color: var(--orange); text-transform: uppercase; margin-bottom: 12px; }
.page-title { font-size: clamp(34px, 4.5vw, 56px); font-weight: 900; letter-spacing: -1px; line-height: 1.1; margin-bottom: 20px; color: #FFF; }
.page-lead { font-size: 18px; color: var(--text-muted); line-height: 1.6; max-width: 820px; margin-bottom: 50px; }

/* CARDS & PANELS */
.panel {
    background: #0B0B11; border: 1px solid var(--border); border-radius: 14px;
    padding: 32px; margin-bottom: 24px; position: relative;
}
.panel h2, .panel h3 { font-size: 22px; font-weight: 800; color: #FFF; margin-bottom: 14px; letter-spacing: -0.3px; }
.panel p { font-size: 15px; color: var(--text-muted); line-height: 1.7; margin-bottom: 16px; }
.panel-badge {
    position: absolute; top: 24px; right: 28px; font-family: 'JetBrains Mono', monospace;
    font-size: 11px; font-weight: 800; color: var(--orange);
}

/* CODE / MATH BLOCK */
.math-block {
    background: #050508; border: 1px solid #222230; border-left: 3px solid var(--orange);
    padding: 18px 22px; border-radius: 8px; font-family: 'JetBrains Mono', monospace;
    font-size: 14px; color: #00F0FF; margin: 18px 0; overflow-x: auto;
}
.terminal-block {
    background: #050508; border: 1px solid var(--border); border-radius: 8px;
    padding: 16px 20px; font-family: 'JetBrains Mono', monospace; font-size: 13px;
    color: #A1A1AA; margin: 16px 0; overflow-x: auto;
}

/* TABLES */
.custom-table {
    width: 100%; border-collapse: collapse; font-family: 'JetBrains Mono', monospace;
    font-size: 12.5px; margin: 20px 0;
}
.custom-table th {
    background: #101018; border: 1px solid var(--border); padding: 12px 16px;
    text-align: left; color: var(--orange); font-weight: 800; letter-spacing: 0.5px;
}
.custom-table td {
    border: 1px solid var(--border); padding: 12px 16px; color: #E4E4E7;
}
.custom-table tr:hover td { background: rgba(255, 69, 0, 0.04); }

/* FOOTER */
footer.site-footer {
    border-top: 1px solid var(--border); background: #050508;
    padding: 60px 6vw 40px; position: relative; z-index: 20;
}
.footer-grid { display: grid; grid-template-columns: 2fr 1fr 1fr; gap: 40px; margin-bottom: 40px; }
.footer-desc { font-size: 13px; color: var(--text-muted); line-height: 1.6; margin-top: 14px; max-width: 380px; }
.footer-col-title { font-family: 'JetBrains Mono', monospace; font-size: 11px; font-weight: 800; color: #FFF; letter-spacing: 1.5px; margin-bottom: 14px; text-transform: uppercase; }
.footer-links { list-style: none; display: flex; flex-direction: column; gap: 8px; font-size: 13px; }
.footer-links a { color: var(--text-muted); text-decoration: none; }
.footer-links a:hover { color: var(--orange); }
.footer-bottom { border-top: 1px solid rgba(255,255,255,0.06); padding-top: 24px; display: flex; justify-content: space-between; font-family: 'JetBrains Mono', monospace; font-size: 11px; color: var(--text-dark); }
"""

def generate_header(active_page):
    links = [
        ("index.html", "HOME", active_page == "home"),
        ("whitepaper.html", "WHITEPAPER", active_page == "whitepaper"),
        ("nodes.html", "NODE RUNNERS", active_page == "nodes"),
        ("tokenomics.html", "TOKENOMICS", active_page == "tokenomics"),
        ("research.html", "RESEARCH", active_page == "research"),
    ]
    links_html = "".join([f'<li><a href="{href}" class="{"active" if is_act else ""}">{label}</a></li>' for href, label, is_act in links])
    
    return f"""
    <div class="telemetry-bar">
        <div style="display:flex; align-items:center; gap:20px;">
            <span><span class="live-dot"></span> <b>SINGULARITY MAINNET</b>: CANARY ONLINE</span>
            <span style="color:var(--text-muted);">// EPOCH 338,912</span>
            <span style="color:var(--orange);">// 142.8 PFLOPS VERIFIED</span>
        </div>
        <div>
            <span style="color:var(--text-muted); font-family:JetBrains Mono,monospace;">SCRAMJET NATIVE PROTOCOL</span>
        </div>
    </div>

    <header class="site-nav">
        <a href="index.html" class="brand-logo-wrap">
            <div class="logo-symbol">
                {logo_svg}
            </div>
            <div class="brand-text">
                <span class="brand-name">33RD TREE LABS</span>
                <span class="brand-sub">SINGULARITY PROTOCOL</span>
            </div>
        </a>

        <ul class="nav-links">
            {links_html}
            <li><a href="nodes.html" class="nav-cta">CONNECT NODE</a></li>
        </ul>
    </header>
    """

footer_html = f"""
    <footer class="site-footer">
        <div class="footer-grid">
            <div>
                <a href="index.html" class="brand-logo-wrap">
                    <div class="logo-symbol" style="width:36px; height:36px;">
                        {logo_svg}
                    </div>
                    <div class="brand-text">
                        <span class="brand-name" style="font-size:14px;">33RD TREE LABS</span>
                        <span class="brand-sub" style="font-size:8.5px;">SINGULARITY PROTOCOL</span>
                    </div>
                </a>
                <p class="footer-desc">
                    33rd Tree Labs is building the decentralized compute fabric for post-AGI coordination. Cryptographic consensus, zero-knowledge inference, and Proof of Intelligence.
                </p>
            </div>
            <div>
                <h5 class="footer-col-title">Protocol Pages</h5>
                <ul class="footer-links">
                    <li><a href="index.html">Home &amp; Terminal</a></li>
                    <li><a href="whitepaper.html">Technical Whitepaper</a></li>
                    <li><a href="nodes.html">Node Operators</a></li>
                    <li><a href="tokenomics.html">Tokenomics &amp; Emission</a></li>
                    <li><a href="research.html">Cryptographic Research</a></li>
                </ul>
            </div>
            <div>
                <h5 class="footer-col-title">Ecosystem</h5>
                <ul class="footer-links">
                    <li><a href="#">Scramjet Launchpad</a></li>
                    <li><a href="https://x.com" target="_blank">X (Twitter)</a></li>
                    <li><a href="https://github.com" target="_blank">GitHub</a></li>
                    <li><a href="#">Solana Explorer</a></li>
                </ul>
            </div>
        </div>
        <div class="footer-bottom">
            <div>© 2026 33RD TREE LABS FOUNDATION. ALL RIGHTS RESERVED.</div>
            <div>CONTRACT: 0x3333333333333333333333333333333333333333</div>
        </div>
    </footer>
"""

# ----------------- PAGE 1: WHITEPAPER.HTML -----------------
whitepaper_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>33RD TREE LABS // Technical Whitepaper v3.3</title>
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700;800;900&family=Space+Grotesk:wght@400;500;700&display=swap" rel="stylesheet">
    <style>{shared_css}</style>
</head>
<body>
    {generate_header("whitepaper")}
    <div class="page-container">
        <div class="page-tag">// TECHNICAL SPECIFICATION // VERSION 3.3-CANARY</div>
        <h1 class="page-title">THE SINGULARITY PROTOCOL WHITEPAPER</h1>
        <p class="page-lead">A comprehensive mathematical formulation for decentralized tensor compute, verifiable zero-knowledge inference, and Byzantine-resistant Proof of Intelligence consensus.</p>

        <div class="panel">
            <span class="panel-badge">[SECTION 01]</span>
            <h2>1. The Post-AGI Compute Dilemma</h2>
            <p>Artificial Intelligence inference is projected to consume over 18% of global silicon compute capacity by 2028. Currently, 94% of advanced tensor accelerators are centralized within four corporate entities. This centralization introduces three systemic vulnerabilities:</p>
            <ul style="color:var(--text-muted); margin-left:24px; margin-bottom:16px;">
                <li><strong>Censorship &amp; Model Gating:</strong> Arbitrary API throttling and selective output manipulation.</li>
                <li><strong>Weight Extraction &amp; Privacy Leakage:</strong> Inability to evaluate proprietary weights on remote silicon without complete parameter exposure.</li>
                <li><strong>Sybil &amp; Proof-of-Waste Bottlenecks:</strong> Existing cryptographic proof-of-work consumes gigawatts on useless hash calculations without generating AI utility.</li>
            </ul>
        </div>

        <div class="panel">
            <span class="panel-badge">[SECTION 02]</span>
            <h2>2. The Exponential Plunge Hyperboloid Topology</h2>
            <p>To eliminate inter-cluster routing latency, 33rd Tree Labs models the validator communication fabric as an exponential double-curved surface of revolution:</p>
            <div class="math-block">
                r(y) = r_throat + (R_canopy - r_throat) * [ e^(k * |y| / H) - 1 ] / [ e^k - 1 ]
            </div>
            <p>Where <code>H = 2.4</code>, <code>R_canopy = 1.5</code>, <code>r_throat = 0.09</code>, and curvature stiffness <code>k = 3.8</code>. This non-Euclidean routing topology bounds maximum gossip diameter to <code>O(log_k N)</code>, guaranteeing sub-10ms packet delivery across 33,000 global nodes.</p>
        </div>

        <div class="panel">
            <span class="panel-badge">[SECTION 03]</span>
            <h2>3. Proof of Intelligence (PoI) Consensus Engine</h2>
            <p>Proof of Intelligence replaces SHA-256 brute forcing with verifiable transformer tensor operations. During each block epoch (12 seconds):</p>
            <ol style="color:var(--text-muted); margin-left:24px; margin-bottom:16px;">
                <li>The coordinator beacon selects a verifiable pseudorandom matrix evaluation task <code>W_seed · X = Y</code>.</li>
                <li>Validators execute the batch forward-pass inference across quantized transformer layers.</li>
                <li>Validators compile a succinct Halo2 zk-SNARK proof verifying arithmetic constraint satisfaction over the BN254 elliptic curve.</li>
                <li>The proof is verified by the network in <code>O(1)</code> time (approx 1.42 ms), sealing block validity.</li>
            </ol>
            <div class="math-block">
                e(π_A, π_B) = e(π_C, G_2) · e(VK_public, H_challenge)
            </div>
        </div>

        <div class="panel">
            <span class="panel-badge">[SECTION 04]</span>
            <h2>4. Byzantine Slashing &amp; Game Theoretic Security</h2>
            <p>Every validator must stake collateral in $33RD tokens. If any validator submits an altered inference tensor or fabricated ZK proof:</p>
            <table class="custom-table">
                <thead>
                    <tr><th>Infraction Type</th><th>Detection Window</th><th>Slashing Penalty</th><th>Validator Action</th></tr>
                </thead>
                <tbody>
                    <tr><td>Weight Poisoning (Byzantine)</td><td>1 Block (Immediate)</td><td>100% of Staked Collateral</td><td>Permanent Node Exclusion</td></tr>
                    <tr><td>Invalid ZK-Proof</td><td>Instant (BN254 Pairing)</td><td>25% of Staked Collateral</td><td>Epoch Ban</td></tr>
                    <tr><td>Liveness Failure (&gt;3 Epochs)</td><td>36 Seconds</td><td>2% of Staked Collateral</td><td>Jail state until unjailed</td></tr>
                </tbody>
            </table>
        </div>
    </div>
    {footer_html}
</body>
</html>
"""

# ----------------- PAGE 2: NODES.HTML -----------------
nodes_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>33RD TREE LABS // Node Operator &amp; Validator Guide</title>
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700;800;900&family=Space+Grotesk:wght@400;500;700&display=swap" rel="stylesheet">
    <style>{shared_css}</style>
</head>
<body>
    {generate_header("nodes")}
    <div class="page-container">
        <div class="page-tag">// INFRASTRUCTURE OPERATORS</div>
        <h1 class="page-title">NODE RUNNER &amp; VALIDATOR PORTAL</h1>
        <p class="page-lead">Monetize your GPU hardware by powering the decentralized tensor fabric. Earn continuous $33RD rewards for running verified zero-knowledge inference.</p>

        <div class="panel">
            <span class="panel-badge">[TIER SPECIFICATIONS]</span>
            <h2>Hardware Requirements &amp; Reward Tiers</h2>
            <table class="custom-table">
                <thead>
                    <tr><th>Tier</th><th>Hardware Minimum</th><th>Min VRAM</th><th>Staking Requirement</th><th>Est. Rewards</th></tr>
                </thead>
                <tbody>
                    <tr><td><strong>Tier-1 (Canary)</strong></td><td>1x RTX 4090 / RTX 3090</td><td>24 GB GDDR6X</td><td>1,000 $33RD</td><td>~18 $33RD / day</td></tr>
                    <tr><td><strong>Tier-2 (Validator)</strong></td><td>4x RTX 4090 or 1x H100 SXM5</td><td>80 GB HBM3</td><td>5,000 $33RD</td><td>~94 $33RD / day</td></tr>
                    <tr><td><strong>Tier-3 (Supernode)</strong></td><td>8x H100 / B200 SXM5 NVLink</td><td>640 GB HBM3e</td><td>25,000 $33RD</td><td>~640 $33RD / day</td></tr>
                </tbody>
            </table>
        </div>

        <div class="panel">
            <span class="panel-badge">[QUICK SETUP]</span>
            <h2>Step-by-Step CLI Daemon Deployment</h2>
            <p>Run the official 33rd Tree Labs validator worker in less than 2 minutes using Docker or bare-metal Linux:</p>
            <div class="terminal-block">
# 1. Pull the official Singularity Node image
docker pull ghcr.io/33rd-tree-labs/node-daemon:v3.3.0

# 2. Initialize your node wallet &amp; Ed25519 identity key
docker run --rm -v ~/.33rd:/root/.33rd ghcr.io/33rd-tree-labs/node-daemon init

# 3. Start the compute worker with GPU acceleration
docker run -d --gpus all \
  --name 33rd-node \
  -v ~/.33rd:/root/.33rd \
  -e RPC_ENDPOINT="wss://canary.33rdtreelabs.ai:8443" \
  -e TIER="TIER_2" \
  ghcr.io/33rd-tree-labs/node-daemon start
            </div>
            <p style="font-size:12.5px; color:var(--orange);">✓ CUDA 12.4+ and NVIDIA driver 535.104+ required. Proof of Intelligence automatically runs local self-check benchmarks.</p>
        </div>

        <div class="panel">
            <span class="panel-badge">[CALCULATOR]</span>
            <h2>Interactive Compute Yield Estimator</h2>
            <p>Select your hardware configuration to calculate estimated daily and monthly protocol rewards:</p>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:20px; margin-top:20px;">
                <div style="background:#050508; padding:20px; border-radius:10px; border:1px solid var(--border);">
                    <div style="font-family:'JetBrains Mono',monospace; font-size:11px; color:var(--text-muted); margin-bottom:8px;">SELECT HARDWARE SPECIFICATION:</div>
                    <select id="calc-gpu" style="width:100%; padding:10px; background:#111118; border:1px solid #333; color:#FFF; font-family:'JetBrains Mono',monospace; border-radius:6px;" onchange="updateYield()">
                        <option value="18">1x NVIDIA RTX 4090 (24GB) - Tier 1</option>
                        <option value="94" selected>1x NVIDIA H100 SXM5 (80GB) - Tier 2</option>
                        <option value="640">8x NVIDIA H100 SXM (640GB) - Tier 3</option>
                    </select>
                </div>
                <div style="background:#050508; padding:20px; border-radius:10px; border:1px solid var(--border); display:flex; flex-direction:column; justify-content:center;">
                    <div style="font-family:'JetBrains Mono',monospace; font-size:11px; color:var(--text-muted);">ESTIMATED REWARD:</div>
                    <div id="calc-output" style="font-family:'JetBrains Mono',monospace; font-size:26px; font-weight:900; color:var(--orange); margin-top:4px;">94 $33RD / day (~2,820 / mo)</div>
                </div>
            </div>
            <script>
                function updateYield() {{
                    const val = parseInt(document.getElementById('calc-gpu').value);
                    const mo = val * 30;
                    document.getElementById('calc-output').textContent = val + ' $33RD / day (~' + mo.toLocaleString() + ' / mo)';
                }}
            </script>
        </div>
    </div>
    {footer_html}
</body>
</html>
"""

# ----------------- PAGE 3: TOKENOMICS.HTML -----------------
tokenomics_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>33RD TREE LABS // Tokenomics &amp; Singularity Economy</title>
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700;800;900&family=Space+Grotesk:wght@400;500;700&display=swap" rel="stylesheet">
    <style>{shared_css}</style>
</head>
<body>
    {generate_header("tokenomics")}
    <div class="page-container">
        <div class="page-tag">// TOKEN ARCHITECTURE &amp; VALUE CAPTURE</div>
        <h1 class="page-title">$33RD TOKENOMICS</h1>
        <p class="page-lead">A fixed-supply, deflationary utility token engineered to capture the economic output of decentralized tensor compute and zero-knowledge inference.</p>

        <div class="panel">
            <span class="panel-badge">[SUPPLY METRICS]</span>
            <h2>Core Supply Parameters</h2>
            <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:20px; margin-top:16px;">
                <div style="background:#050508; padding:18px; border-radius:8px; border:1px solid var(--border);">
                    <div style="font-family:'JetBrains Mono',monospace; font-size:11px; color:var(--text-muted);">TOTAL MAX SUPPLY</div>
                    <div style="font-family:'JetBrains Mono',monospace; font-size:22px; font-weight:900; color:#FFF; margin-top:4px;">33,333,333 $33RD</div>
                </div>
                <div style="background:#050508; padding:18px; border-radius:8px; border:1px solid var(--border);">
                    <div style="font-family:'JetBrains Mono',monospace; font-size:11px; color:var(--text-muted);">INITIAL CIRCULATING</div>
                    <div style="font-family:'JetBrains Mono',monospace; font-size:22px; font-weight:900; color:var(--orange); margin-top:4px;">15.0% (Bonding Pool)</div>
                </div>
                <div style="background:#050508; padding:18px; border-radius:8px; border:1px solid var(--border);">
                    <div style="font-family:'JetBrains Mono',monospace; font-size:11px; color:var(--text-muted);">DEPLOYMENT VENUE</div>
                    <div style="font-family:'JetBrains Mono',monospace; font-size:22px; font-weight:900; color:#00F0FF; margin-top:4px;">Scramjet Launchpad</div>
                </div>
            </div>
        </div>

        <div class="panel">
            <span class="panel-badge">[ALLOCATION]</span>
            <h2>Distribution Breakdown</h2>
            <table class="custom-table">
                <thead>
                    <tr><th>Allocation Bucket</th><th>Share</th><th>Tokens</th><th>Vesting / Emission Schedule</th></tr>
                </thead>
                <tbody>
                    <tr><td><strong>Compute Mining Emissions (PoI)</strong></td><td>45.0%</td><td>15,000,000</td><td>Decaying emission over 6 years with annual halving</td></tr>
                    <tr><td><strong>Validator Staking &amp; Security Pool</strong></td><td>20.0%</td><td>6,666,666</td><td>Locked for node collateral rewards and slash insurance</td></tr>
                    <tr><td><strong>Public Bonding &amp; Liquidity (Scramjet)</strong></td><td>15.0%</td><td>5,000,000</td><td>100% unlocked at fair launch bonding curve</td></tr>
                    <tr><td><strong>Research &amp; Protocol Treasury</strong></td><td>10.0%</td><td>3,333,333</td><td>6-month cliff, 36-month linear monthly vest</td></tr>
                    <tr><td><strong>Core Contributors &amp; Foundation</strong></td><td>10.0%</td><td>3,333,334</td><td>12-month cliff, 24-month linear vest</td></tr>
                </tbody>
            </table>
        </div>

        <div class="panel">
            <span class="panel-badge">[VALUE FLYWHEEL]</span>
            <h2>Deflationary Buyback &amp; Burn Engine</h2>
            <p>Every commercial zero-knowledge inference call on 33rd Tree Labs generates protocol fees:</p>
            <ul style="color:var(--text-muted); margin-left:24px; margin-bottom:16px;">
                <li><strong>75% to Compute Providers:</strong> Distributed directly to the GPU nodes that calculated the forward pass.</li>
                <li><strong>15% Staker Yield:</strong> Distributed to token holders who stake to validate PoI proofs.</li>
                <li><strong>10% Permanent Buyback &amp; Burn:</strong> Automatically purchases $33RD tokens off the open market and burns them on-chain forever, decreasing the circulating supply.</li>
            </ul>
        </div>
    </div>
    {footer_html}
</body>
</html>
"""

# ----------------- PAGE 4: RESEARCH.HTML -----------------
research_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>33RD TREE LABS // Cryptographic &amp; AI Research</title>
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700;800;900&family=Space+Grotesk:wght@400;500;700&display=swap" rel="stylesheet">
    <style>{shared_css}</style>
</head>
<body>
    {generate_header("research")}
    <div class="page-container">
        <div class="page-tag">// OPEN-SOURCE RESEARCH &amp; PAPERS</div>
        <h1 class="page-title">CRYPTOGRAPHIC PAPERS &amp; BENCHMARKS</h1>
        <p class="page-lead">Technical publications authored by 33rd Tree Labs researchers on succinct zero-knowledge verification, topological network routing, and Byzantine-safe AI.</p>

        <div class="panel">
            <span class="panel-badge">[PAPER 01]</span>
            <h2>Sub-Millisecond ZK Proofs for 70B Parameter LLMs</h2>
            <p>Authors: <em>33rd Tree Labs Research Group (October 2026)</em></p>
            <p>We present a novel Plonky3 polynomial commitment scheme optimized for quantized transformer weights (W4A16). By folding arithmetic cross-terms over Goldilocks fields, we achieve 1.418ms proof verification time on consumer mobile clients without revealing model weight checkpoints.</p>
            <div class="terminal-block">
Verification Benchmark (70B Model, Batch Size 16):
- Baseline Halo2 verification: 42.8 ms
- 33rd Plonky3 Tensor Fold: 1.418 ms (30.1x speedup)
- Proof Size: 4.8 KB (fits inside standard Solana transaction MTU)
            </div>
        </div>

        <div class="panel">
            <span class="panel-badge">[PAPER 02]</span>
            <h2>Topological Routing over Non-Euclidean Hyperboloid Manifolds</h2>
            <p>Authors: <em>33rd Tree Labs Distributed Systems Team (August 2026)</em></p>
            <p>Traditional overlay networks fail under sudden compute load spikes due to Euclidean distance bottlenecks. We demonstrate that mapping node address spaces to a continuous hyperboloid tensor arbor reduces P99 tail latency from 240ms down to 8.4ms during 10x traffic surges.</p>
        </div>

        <div class="panel">
            <span class="panel-badge">[PAPER 03]</span>
            <h2>Byzantine Weight Poisoning Prevention in Decentralized LLM Checkpoints</h2>
            <p>Authors: <em>33rd Tree Labs Security &amp; Cryptography (July 2026)</em></p>
            <p>Decentralized model training and inference are vulnerable to adversarial weight manipulation. We introduce Proof of Intelligence Merkle checkouts, where every tensor shard is signed by multi-validator Schnorr aggregation, preventing model backdoor injection with 99.9999% cryptographic certainty.</p>
        </div>
    </div>
    {footer_html}
</body>
</html>
"""

# Write all pages
pages = [
    ("whitepaper.html", whitepaper_content),
    ("nodes.html", nodes_content),
    ("tokenomics.html", tokenomics_content),
    ("research.html", research_content)
]

for fname, content in pages:
    dest_site = os.path.join(SITE_DIR, fname)
    dest_ws = os.path.join(WS_SITE_DIR, fname)
    dest_desk = os.path.join(DESKTOP_3D, fname)
    
    with open(dest_site, "w", encoding="utf-8") as f: f.write(content)
    with open(dest_ws, "w", encoding="utf-8") as f: f.write(content)
    with open(dest_desk, "w", encoding="utf-8") as f: f.write(content)
    print(f"Built multi-page: {dest_site}")

