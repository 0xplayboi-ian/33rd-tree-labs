import os

file_path = "/Users/ianmora/Desktop/Projects/33rd-tree-labs-site/build_master_story_scroll.py"

with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Ensure script tag is present before closing body
script_tag = '<script src="assets/poincare_simulator.js"></script>'
if "assets/poincare_simulator.js" not in text:
    text = text.replace("<!-- JAVASCRIPT ENGINES", script_tag + "\n  <!-- JAVASCRIPT ENGINES")

# 2. Update Chapter 07 Section HTML
old_section_start = '    <!-- ===================================================================\n         CHAPTER 07: OVERHAULED LIVE TENSOR REDUCTION & BYZANTINE SIMULATOR'
old_section_end = '    <!-- ===================================================================\n         CHAPTER 08: INVERTED COLORWAY FINALE'

p1 = text.find(old_section_start)
p2 = text.find(old_section_end)
assert p1 != -1 and p2 != -1, f"Section 07 markers not found: {p1}, {p2}"

new_section = """    <!-- ===================================================================
         CHAPTER 07: POINCARÉ HYPERBOLIC TENSOR ARBOR SIMULATOR
         =================================================================== -->
    <section class="play" id="playground">
      <div class="play__inner">
        <div>
          <div class="play__canvas-box" style="position: relative; height: 500px; background: #050508; border: 1px solid var(--border); border-radius: 8px; overflow: hidden; box-shadow: 0 25px 70px rgba(0, 0, 0, 0.85), 0 0 35px rgba(255, 36, 36, 0.2);">
            <!-- INTEGRATED LIVE CONSENSUS TELEMETRY HUD -->
            <div class="consensus-hud">
              <div class="consensus-hud__header">
                <span class="consensus-hud__title">
                  <span class="hud-live-dot"></span>
                  <span>CONSENSUS TELEMETRY HUD // REAL-TIME ANCHOR MONITOR</span>
                </span>
                <span id="hud-status" class="hud-status-badge">SUPERMAJORITY ATTAINED</span>
              </div>
              <div class="consensus-hud__grid">
                <div class="hud-metric">
                  <span class="hud-label">ACTIVE QUORUM CONVERGENCE</span>
                  <span class="hud-value" id="hud-quorum">64 / 64 Nodes Converged</span>
                  <span class="hud-sub" id="hud-quorum-sub">&gt; 2/3 Supermajority Attained</span>
                </div>
                <div class="hud-metric">
                  <span class="hud-label">BIT-EXACT INFERENCE PRECISION</span>
                  <span class="hud-value" id="hud-invariant" style="color: var(--t);">&Delta;&epsilon; = 0.00 INT8</span>
                  <span class="hud-sub">cuBLAS/FMA Invariant Guaranteed</span>
                </div>
                <div class="hud-metric">
                  <span class="hud-label">SOLANA ANCHOR SETTLEMENT</span>
                  <span class="hud-value" id="hud-slot">Sub-second Commit</span>
                  <span class="hud-sub">Slot Finality: 400ms Speculative</span>
                </div>
                <div class="hud-metric">
                  <span class="hud-label">SOLANA INCINERATOR BURN</span>
                  <span class="hud-value" style="color: var(--t);">10% Fee Burned</span>
                  <span class="hud-sub">1nc1nerator...1111 Permanent</span>
                </div>
              </div>
            </div>

            <canvas id="playground-canvas"></canvas>
            <div id="play-flash-banner" style="position: absolute; top: 90px; left: 50%; transform: translateX(-50%); background: rgba(255, 36, 36, 0.2); border: 1px solid #FF2424; color: #FFFFFF; font-family: var(--fm); font-size: 10.5px; font-weight: 700; letter-spacing: 0.12em; padding: 4px 16px; border-radius: 4px; pointer-events: none; opacity: 0; transition: opacity 0.25s; z-index: 12;">STATE COMMITTED // ANCHOR VERIFIED</div>
          </div>

          <!-- PROTOCOL CONTEXT EXPLANATORY CALLOUT CARDS -->
          <div class="node-context-grid">
            <div class="node-legend-card crimson">
              <div class="legend-badge">TIER 1 &amp; 2 // H100 SXM5 &amp; B200 BLACKWELL HUBS</div>
              <div class="legend-title">COORDINATORS &amp; REDUCTION HUBS</div>
              <p>
                Inner and middle hyperbolic horocycles (&rho; = 0.29, &rho; = 0.66). Primary coordinators and tensor reduction hubs executing bit-exact INT8 matrix consensus (&Delta;&epsilon; = 0.00) with sub-second Solana anchor settlement.
              </p>
            </div>
            <div class="node-legend-card obsidian">
              <div class="legend-badge">TIER 3 // RTX 4090 DISTRIBUTED EDGE QUORUM</div>
              <div class="legend-title">GROMOV GEODESIC EDGE MANIFOLD</div>
              <p>
                Outer hyperbolic perimeter (&rho; = 1.25, K=64). Edge compute nodes routing tensor packets (&otimes;, &nabla;, &lambda;, &Delta;) along Gromov geodesics (&le; 8 hops). Automatic Byzantine isolation and tree bypass routing.
              </p>
            </div>
          </div>
        </div>

        <div class="play__controls">
          <div class="kicker">CHAPTER 07 // POINCARÉ HYPERBOLIC SIMULATOR</div>
          <h3>POINCARÉ DISK MODEL // GROMOV &delta;-HYPERBOLIC ARBOR</h3>
          <p style="font-size: 13px; color: var(--dim); line-height: 1.55; margin-bottom: 6px;">
            Circular Poincaré disk model of Gromov &delta;-hyperbolic geometry (&kappa; = -1.414). Scale the quorum committee from K=16 to 64, inject Byzantine floating-point drift, and watch traffic route around rogue nodes via geodesic bypass!
          </p>
          
          <div class="play__row">
            <div class="play__row-head">
              <span>QUORUM COMMITTEE SLIDER (K=16 TO 64)</span>
              <span id="k-out">64</span>
            </div>
            <input type="range" id="k-slider" min="16" max="64" value="64" step="1">
            <span class="play__row-desc">Controls committee size. Agreement threshold &gt; 2/3 K triggers crimson pulse: STATE COMMITTED // ANCHOR VERIFIED.</span>
          </div>

          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; font-family: var(--fm); font-size: 10px; margin-top: 4px;">
            <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); padding: 8px 10px; border-radius: 4px;">
              <div style="color: var(--slate); font-size: 8.5px;">ROUTING DIAMETER</div>
              <div style="color: #FFFFFF; font-weight: 700; margin-top: 2px;">&le; 8 Hops (Geodesic)</div>
            </div>
            <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); padding: 8px 10px; border-radius: 4px;">
              <div style="color: var(--slate); font-size: 8.5px;">CONSENSUS INVARIANT</div>
              <div id="play-invariant-tag" style="color: #00E676; font-weight: 700; margin-top: 2px;">&Delta;&epsilon; = 0.00 INT8</div>
            </div>
            <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); padding: 8px 10px; border-radius: 4px;">
              <div style="color: var(--slate); font-size: 8.5px;">SOLANA SETTLEMENT</div>
              <div style="color: #FFFFFF; font-weight: 700; margin-top: 2px;">Sub-second Anchor</div>
            </div>
            <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); padding: 8px 10px; border-radius: 4px;">
              <div style="color: var(--slate); font-size: 8.5px;">CUMULATIVE BURN</div>
              <div style="color: var(--t); font-weight: 700; margin-top: 2px;">10% to 1nc1nerator</div>
            </div>
          </div>

          <div style="display: flex; gap: 10px; margin-top: 14px; flex-wrap: wrap;">
            <button type="button" id="btn-play-fault" class="btn-action" style="background: #FF2424; color: #000; border-color: #FF2424; font-weight: 700;">[ INJECT BYZANTINE FAULT ]</button>
            <button type="button" id="btn-play-reset" class="btn-action" style="background: transparent; color: #FFF; border-color: rgba(255,255,255,0.4); font-weight: 700;">[ RESET / SYNC QUORUM ]</button>
            <a href="simulator.html" class="btn-action primary">FULL SIMULATOR SUITE &rarr;</a>
          </div>
        </div>
      </div>
    </section>

"""

text = text[:p1] + new_section + text[p2:]

# 3. Update JavaScript initialization for playground-canvas
old_js_start = "    // Initialize Playground Field\n    const playCanvas = document.getElementById('playground-canvas');"
old_js_end = "    // Global Animation Render Loop"

jp1 = text.find(old_js_start)
jp2 = text.find(old_js_end)
assert jp1 != -1 and jp2 != -1, f"JS initialization markers not found: {jp1}, {jp2}"

new_js = """    // Initialize Poincaré Hyperbolic Tensor Arbor Simulator on playground-canvas
    const playCanvas = document.getElementById('playground-canvas');
    let playSim = null;
    const hudQuorum = document.getElementById('hud-quorum');
    const hudQuorumSub = document.getElementById('hud-quorum-sub');
    const hudStatus = document.getElementById('hud-status');
    const hudSlot = document.getElementById('hud-slot');
    const hudInvariant = document.getElementById('hud-invariant');
    const playInvariantTag = document.getElementById('play-invariant-tag');
    const kOut = document.getElementById('k-out');
    let simulatedSlot = 318492040;

    function updatePlaygroundHUD(m) {
      if (!m) return;
      if (kOut) kOut.textContent = `${m.k} (${m.honestCount}/${m.totalActive} Honest)`;
      if (hudQuorum) hudQuorum.textContent = `${m.honestCount} / ${m.totalActive} Nodes Converged`;
      if (hudQuorumSub) {
        const pct = Math.round(m.honestRatio * 100);
        hudQuorumSub.textContent = `${pct}% Agreement (> 66.7% Required)`;
      }
      if (hudInvariant) {
        hudInvariant.textContent = m.faultCount === 0 ? 'Δε = 0.00 INT8' : 'Δε = +0.47 FP16 (BYPASS)';
        hudInvariant.style.color = m.faultCount === 0 ? 'var(--t)' : '#FFAA00';
      }
      if (playInvariantTag) {
        playInvariantTag.textContent = m.faultCount === 0 ? 'Δε = 0.00 INT8' : 'Δε = +0.47 FP16 (BYPASS)';
        playInvariantTag.style.color = m.faultCount === 0 ? '#00E676' : '#FFAA00';
      }
      if (hudStatus) {
        if (m.isQuorum) {
          hudStatus.textContent = 'SUPERMAJORITY ATTAINED';
          hudStatus.style.color = '#FF2424';
          hudStatus.style.borderColor = 'rgba(255, 36, 36, 0.4)';
          hudStatus.style.background = 'rgba(255, 36, 36, 0.15)';
        } else {
          hudStatus.textContent = 'PARTITION RECONCILING';
          hudStatus.style.color = '#FFAA00';
          hudStatus.style.borderColor = 'rgba(255, 170, 0, 0.4)';
          hudStatus.style.background = 'rgba(255, 170, 0, 0.15)';
        }
      }
      if (hudSlot && Math.random() < 0.1) {
        simulatedSlot += 1;
        hudSlot.textContent = `Slot #${simulatedSlot} Commit`;
      }
    }

    if (playCanvas && typeof PoincareHyperbolicSimulator !== 'undefined') {
      playSim = new PoincareHyperbolicSimulator(playCanvas, {
        k: 64,
        speed: 1.0,
        interactive: true,
        flashBannerElement: document.getElementById('play-flash-banner'),
        onQuorumChange: (m) => updatePlaygroundHUD(m),
        onByzantineEvent: (node, m) => updatePlaygroundHUD(m)
      });
    }

    const kSlider = document.getElementById('k-slider');
    if (kSlider) {
      kSlider.addEventListener('input', (e) => {
        const val = parseInt(e.target.value, 10);
        if (playSim) playSim.setK(val);
      });
    }

    const btnPlayFault = document.getElementById('btn-play-fault');
    if (btnPlayFault) {
      btnPlayFault.addEventListener('click', () => {
        if (playSim) playSim.injectByzantineFault();
      });
    }

    const btnPlayReset = document.getElementById('btn-play-reset');
    if (btnPlayReset) {
      btnPlayReset.addEventListener('click', () => {
        if (playSim) playSim.resetQuorum();
      });
    }

"""

text = text[:jp1] + new_js + text[jp2:]

# In renderLoop, remove if (playField) playField.frame(dt);
text = text.replace("if (playField) playField.frame(dt);", "// PoincareHyperbolicSimulator animates via its own loop")
text = text.replace("updateConsensusTelemetry();", "// Consensus telemetry managed by PoincareHyperbolicSimulator")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(text)

print("build_master_story_scroll.py updated successfully!")
