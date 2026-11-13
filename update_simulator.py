import os

site_dir = "/Users/ianmora/Desktop/Projects/33rd-tree-labs-site"
sim_path = os.path.join(site_dir, "simulator.html")

with open(sim_path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Add script tag for assets/poincare_simulator.js
script_tag = '<script src="assets/poincare_simulator.js"></script>'
if "assets/poincare_simulator.js" not in text:
    text = text.replace("<!-- Lenis & GSAP -->", script_tag + "\n    <!-- Lenis & GSAP -->")

# 2. Replace sim-box HTML
start_marker = "<!-- Visual Byzantine Committee Lattice -->"
end_marker = "<!-- Interactive Solana CLI Terminal -->"

new_sim_box = """<!-- Visual Poincaré Hyperbolic Tensor Arbor -->
            <div class="sim-box">
                <div class="sim-box-title">
                    <span data-glitch>POINCARÉ HYPERBOLIC TENSOR ARBOR (&kappa; = -1.414)</span>
                    <span id="byz-ratio-tag" style="color:var(--chalk);">COMMITTEE: K=64 // QUORUM VALIDATED</span>
                </div>

                <!-- POINCARÉ HYPERBOLIC MANIFOLD CANVAS CONTAINER -->
                <div class="poincare-canvas-wrap" style="position:relative; width:100%; aspect-ratio:1; max-height:480px; background:#050508; border:1px solid var(--border); border-radius:6px; overflow:hidden; margin-bottom:16px;">
                    <canvas id="poincare-canvas" style="width:100%; height:100%; display:block;"></canvas>
                    <div id="sim-flash-banner" style="position:absolute; top:12px; left:50%; transform:translateX(-50%); background:rgba(255,36,36,0.18); border:1px solid #FF2424; color:#FFFFFF; font-family:'JetBrains Mono',monospace; font-size:10px; font-weight:700; letter-spacing:0.12em; padding:4px 14px; border-radius:3px; pointer-events:none; opacity:0; transition:opacity 0.25s; z-index:10;">STATE COMMITTED // ANCHOR VERIFIED</div>
                </div>

                <!-- GPU TIER CLUSTER LEGEND -->
                <div class="tier-legend" style="display:grid; grid-template-columns: repeat(3, 1fr); gap:8px; margin-bottom:16px; font-family:'JetBrains Mono',monospace; font-size:9.5px;">
                    <div style="background:#101016; border:1px solid #282835; padding:6px 8px; border-radius:4px;">
                        <div style="display:flex; align-items:center; gap:5px; color:#FF2424; font-weight:700;">
                            <span style="width:6px; height:6px; border-radius:50%; background:#FF2424; display:inline-block; box-shadow:0 0 6px #FF2424;"></span>
                            TIER 1 (INNER)
                        </div>
                        <div style="color:var(--chalk-dim); margin-top:2px;">H100 SXM5 Coordinators (8)</div>
                    </div>
                    <div style="background:#101016; border:1px solid #282835; padding:6px 8px; border-radius:4px;">
                        <div style="display:flex; align-items:center; gap:5px; color:#FFFFFF; font-weight:700;">
                            <span style="width:6px; height:6px; border-radius:50%; background:#FFFFFF; display:inline-block;"></span>
                            TIER 2 (MID)
                        </div>
                        <div style="color:var(--chalk-dim); margin-top:2px;">B200 NVL Hubs (16)</div>
                    </div>
                    <div style="background:#101016; border:1px solid #282835; padding:6px 8px; border-radius:4px;">
                        <div style="display:flex; align-items:center; gap:5px; color:var(--slate); font-weight:700;">
                            <span style="width:6px; height:6px; border-radius:50%; background:var(--slate); display:inline-block;"></span>
                            TIER 3 (EDGE)
                        </div>
                        <div style="color:var(--chalk-dim); margin-top:2px;">RTX 4090 Quorum (40)</div>
                    </div>
                </div>

                <div class="sim-controls">
                    <!-- Quorum Committee Slider (K=16 to 64) -->
                    <div>
                        <div class="sim-slider-row">
                            <span>QUORUM COMMITTEE SLIDER (K=16 TO 64)</span>
                            <span id="k-slider-val" style="color:var(--laser-red); font-weight:700;">K = 64 (Threshold: f &le; 21)</span>
                        </div>
                        <input type="range" id="k-slider" class="sim-range" min="16" max="64" value="64" step="1">
                    </div>

                    <!-- Action Buttons: Inject Byzantine Fault & Reset/Sync Quorum -->
                    <div style="display:grid; grid-template-columns: 1fr 1fr; gap:10px;">
                        <button type="button" id="btn-inject-fault" class="btn-brutal-red" style="width:100%; justify-content:center; padding:10px 14px; cursor:pointer; font-size:10.5px; font-weight:700;" data-glitch>
                            [ INJECT BYZANTINE FAULT ]
                        </button>
                        <button type="button" id="btn-reset-quorum" class="btn-brutal-outline" style="width:100%; justify-content:center; padding:10px 14px; cursor:pointer; font-size:10.5px; font-weight:700;" data-glitch>
                            [ RESET / SYNC QUORUM ]
                        </button>
                    </div>

                    <div style="display:flex; flex-direction:column; gap:6px;">
                        <span class="sim-slider-row"><span>ATTACK VECTOR SIMULATION</span></span>
                        <select id="attack-vector-select" class="sim-attack-select">
                            <option value="drift">Floating-Point Drift (&Delta;&epsilon; &gt; 0.00 FP16 Mismatch)</option>
                            <option value="gradient-poison">Malicious Gradient Poisoning (CAP-FFN Failure)</option>
                            <option value="equivocation">Equivocation &bull; Dual Block Commitment</option>
                            <option value="weight-tamper">Model Weight Tampering &bull; Silent Bit-Rot</option>
                            <option value="sybil-stall">Coordinated Sybil Denial of Service (Stall)</option>
                        </select>
                    </div>

                    <!-- Live Protocol Telemetry HUD Cards -->
                    <div style="display:grid; grid-template-columns: repeat(2, 1fr); gap:8px; margin-top:2px;">
                        <div style="background:#09090D; border:1px solid #1E1E28; padding:8px 10px; border-radius:3px;">
                            <div style="font-family:'JetBrains Mono',monospace; font-size:9px; color:var(--slate);">ROUTING DIAMETER</div>
                            <div id="hud-diameter" style="font-family:'JetBrains Mono',monospace; font-size:11px; color:#FFFFFF; font-weight:700;">&le; 8 Hops (Gromov Geodesic)</div>
                        </div>
                        <div style="background:#09090D; border:1px solid #1E1E28; padding:8px 10px; border-radius:3px;">
                            <div style="font-family:'JetBrains Mono',monospace; font-size:9px; color:var(--slate);">CONSENSUS INVARIANT</div>
                            <div id="hud-invariant" style="font-family:'JetBrains Mono',monospace; font-size:11px; color:var(--green); font-weight:700;">&Delta;&epsilon; = 0.00 INT8</div>
                        </div>
                        <div style="background:#09090D; border:1px solid #1E1E28; padding:8px 10px; border-radius:3px;">
                            <div style="font-family:'JetBrains Mono',monospace; font-size:9px; color:var(--slate);">SOLANA SETTLEMENT</div>
                            <div id="hud-settlement" style="font-family:'JetBrains Mono',monospace; font-size:11px; color:#FFFFFF; font-weight:700;">Sub-second Anchor Commit</div>
                        </div>
                        <div style="background:#09090D; border:1px solid #1E1E28; padding:8px 10px; border-radius:3px;">
                            <div style="font-family:'JetBrains Mono',monospace; font-size:9px; color:var(--slate);">CUMULATIVE EPOCH BURN</div>
                            <div id="hud-burn" style="font-family:'JetBrains Mono',monospace; font-size:11px; color:#FF2424; font-weight:700;">10% to 1nc1nerator...1111</div>
                        </div>
                    </div>

                    <div class="sim-status-banner" id="sim-status-box">
                        <div class="sim-status-head success" id="sim-status-title">
                            <span>[VALID] STATE COMMITTED // ANCHOR VERIFIED</span>
                        </div>
                        <div id="sim-status-desc" style="color:var(--slate);">
                            Active Quorum: 64/64 validators. Deterministic INT8 consensus invariant satisfied (&Delta;&epsilon; = 0.00). Geodesic diameter &le; 8 hops.
                        </div>
                    </div>
                </div>
            </div>

            """

p1 = text.find(start_marker)
p2 = text.find(end_marker)
assert p1 != -1 and p2 != -1, f"Markers not found: {p1}, {p2}"
text = text[:p1] + new_sim_box + text[p2:]

# 3. Replace JavaScript engine
js_start = "// BYZANTINE LATTICE ENGINE"
js_end = "// SOLANA ANCHOR CLI TERMINAL"

new_js = """// POINCARÉ HYPERBOLIC SIMULATOR INTEGRATION
        const pCanvas = document.getElementById('poincare-canvas');
        const flashBanner = document.getElementById('sim-flash-banner');
        const kSlider = document.getElementById('k-slider');
        const kSliderVal = document.getElementById('k-slider-val');
        const byzRatioTag = document.getElementById('byz-ratio-tag');
        const hudInvariant = document.getElementById('hud-invariant');
        const statusBox = document.getElementById('sim-status-box');
        const statusTitle = document.getElementById('sim-status-title');
        const statusDesc = document.getElementById('sim-status-desc');

        let sim = null;
        if (pCanvas && typeof PoincareHyperbolicSimulator !== 'undefined') {
            sim = new PoincareHyperbolicSimulator(pCanvas, {
                k: 64,
                speed: 1.0,
                interactive: true,
                flashBannerElement: flashBanner,
                onQuorumChange: (m) => updateSimulatorUI(m),
                onByzantineEvent: (node, m) => {
                    updateSimulatorUI(m);
                    appendTermLine(`[BYZANTINE] Node ${node.name} (${node.tierName}) injected drift error: Δε = +${node.drift} FP16`, 'warn');
                    appendTermLine(`[HASH-CHECK] Deterministic INT8 invariant failed. Polynomial KZG proof mismatch.`, 'dim');
                    appendTermLine(`[SLASH-CRANK] Confiscated 100% stake -> Solana Incinerator (1nc1nerator...1111)`, 'highlight');
                    appendTermLine(`[GROMOV-BYPASS] Geodesic tree bypass active. Traffic rerouted with 0 packet loss.`, 'success');
                },
                onLog: (msg) => {
                    if (typeof appendTermLine === 'function') {
                        const type = msg.includes('[BYZANTINE]') ? 'warn' : msg.includes('[SLASH') ? 'highlight' : msg.includes('[QUORUM') ? 'success' : 'dim';
                        appendTermLine(msg, type);
                    }
                }
            });
        }

        function updateSimulatorUI(m) {
            if (!m) return;
            if (kSliderVal) {
                kSliderVal.textContent = `K = ${m.k} (Threshold: f ≤ ${m.maxFaults})`;
            }
            if (byzRatioTag) {
                byzRatioTag.textContent = `COMMITTEE: K=${m.k} // ${m.isQuorum ? 'QUORUM VALIDATED' : 'CRITICAL BREACH'}`;
                byzRatioTag.style.color = m.isQuorum ? 'var(--chalk)' : 'var(--laser-red)';
            }
            if (hudInvariant) {
                hudInvariant.textContent = m.faultCount === 0 ? 'Δε = 0.00 INT8' : `Δε = +0.47 FP16 (BYPASS ENGAGED)`;
                hudInvariant.style.color = m.faultCount === 0 ? 'var(--green)' : '#FFAA00';
            }
            if (statusTitle && statusDesc) {
                if (m.isQuorum) {
                    statusTitle.className = 'sim-status-head success';
                    statusTitle.textContent = '[VALID] STATE COMMITTED // ANCHOR VERIFIED';
                    statusDesc.textContent = `Active Quorum: ${m.honestCount}/${m.totalActive} validators (> 66.7%). Deterministic INT8 consensus invariant satisfied (Δε = 0.00). Geodesic diameter ≤ 8 hops.`;
                } else {
                    statusTitle.className = 'sim-status-head danger';
                    statusTitle.textContent = '[CRITICAL] BYZANTINE FAULT: SAFETY BREACH';
                    statusDesc.textContent = `Fault count ${m.faultCount} exceeds threshold f ≤ ${m.maxFaults}. Solana anchor circuit breaker engaged. No state finalized to preserve zero-knowledge integrity.`;
                }
            }
        }

        if (kSlider) {
            kSlider.addEventListener('input', (e) => {
                const val = parseInt(e.target.value);
                if (sim) sim.setK(val);
            });
        }

        const btnInject = document.getElementById('btn-inject-fault');
        if (btnInject) {
            btnInject.addEventListener('click', () => {
                if (sim) {
                    const node = sim.injectByzantineFault();
                    if (node) {
                        appendTermLine(`> Injected Byzantine floating-point drift into ${node.name}...`, 'warn');
                    }
                }
            });
        }

        const btnReset = document.getElementById('btn-reset-quorum');
        if (btnReset) {
            btnReset.addEventListener('click', () => {
                if (sim) {
                    sim.resetQuorum();
                    appendTermLine(`> Executing full quorum resync across active validators...`, 'dim');
                    appendTermLine(`[SYNC] All validator nodes re-aligned to deterministic INT8 invariants (Δε = 0.00)`, 'success');
                    appendTermLine(`[SOLANA] Anchor commitment verified in slot • Sub-second settlement`, 'success');
                }
            });
        }

        """

jp1 = text.find(js_start)
jp2 = text.find(js_end)
assert jp1 != -1 and jp2 != -1, f"JS markers not found: {jp1}, {jp2}"
text = text[:jp1] + new_js + text[jp2:]

# Replace initMatrix call
text = text.replace("initMatrix();", "// PoincareHyperbolicSimulator initialized")

with open(sim_path, "w", encoding="utf-8") as f:
    f.write(text)

print("simulator.html updated successfully!")
