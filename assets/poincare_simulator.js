/**
 * 33RD TREE LABS // POINCARÉ HYPERBOLIC TENSOR ARBOR SIMULATOR ENGINE
 *
 * Mathematical Foundations:
 * 1. Poincaré Disc Model: D^2 = { z in C : |z| < 1 } with metric ds^2 = 4 |dz|^2 / (1 - |z|^2)^2
 * 2. Gromov delta-hyperbolic negative curvature (kappa = -1.0, delta = 0.12)
 * 3. Geodesics: circular arcs orthogonal to the boundary circle |z| = 1 and straight diameters
 * 4. K=64 Quorum Committee: Hierarchical Tensor Arbor with Tier 1 (H100), Tier 2 (B200), Tier 3 (RTX 4090)
 * 5. Byzantine Fault Injection: FP16 gradient poisoning, silent tensor drift, equivocation, sybil stall
 * 6. Real-time Geodesic Bypass Routing: Automatic route invalidation and zero-knowledge fallback under Byzantine churn
 *
 * Brutalist Rules: Zero emojis, strictly 33rdtreelabs.tech, 60fps Canvas renderer.
 */

class PoincareHyperbolicSimulator {
  constructor(canvas, options = {}) {
    this.canvas = canvas;
    this.ctx = canvas.getContext('2d');
    this.options = Object.assign({
      k: 64, // Quorum committee size (16 to 64)
      speed: 1.0,
      interactive: true,
      showHud: true,
      attackVector: 'silent-drift', // 'silent-drift', 'gradient-poison', 'equivocation', 'sybil-stall'
      onQuorumChange: null,
      onByzantineEvent: null,
      onRouteBypass: null,
      onLog: null,
      flashBannerElement: null
    }, options);

    this.k = Math.max(16, Math.min(64, this.options.k));
    this.attackVector = this.options.attackVector;
    this.nodes = [];
    this.edges = [];
    this.packets = [];
    this.shockwaves = [];
    this.bypassArcs = [];
    this.invalidatedRoutes = [];
    this.hoveredNode = null;
    this.selectedNode = null;
    this.dpr = typeof window !== 'undefined' ? (window.devicePixelRatio || 1) : 1;
    this.width = 0;
    this.height = 0;
    this.cx = 0;
    this.cy = 0;
    this.radius = 0;
    this.lastTime = typeof performance !== 'undefined' ? performance.now() : 0;
    this.running = true;
    this.paused = false;

    // Flash banner state
    this.bannerText = 'STATE COMMITTED // ANCHOR VERIFIED';
    this.bannerAlpha = 0;
    this.bannerColor = '#FF2424';

    // Telemetry tickers
    this.animTime = 0;
    this.consensusRound = 1048;
    this.lastRoundTime = 0;

    this.initTopology();
    this.initPackets();
    this.resize();
    this.bindEvents();

    this.animate = this.animate.bind(this);
    if (typeof requestAnimationFrame !== 'undefined') {
      requestAnimationFrame(this.animate);
    }
  }

  /* -------------------------------------------------------------------------
     1. TOPOLOGY INITIALIZATION (K=64 QUORUM COMMITTEE)
     ------------------------------------------------------------------------- */
  initTopology() {
    this.nodes = [];
    this.edges = [];
    this.bypassArcs = [];
    this.invalidatedRoutes = [];

    // NODE 0: APEX SINGULARITY ROOT (Canonical Mark #06 Apex Coordinator)
    this.nodes.push({
      id: 0,
      tier: 0,
      name: 'APEX SINGULARITY',
      pubkey: '0x33A0...APEX',
      tierName: 'Mark #06 Apex Singularity Coordinator',
      r: 0.0,
      theta: 0.0,
      parent: -1,
      stake: 1000000,
      initialStake: 1000000,
      drift: 0.00,
      fp16Hex: '0x3C00',
      state: 'honest',
      active: true,
      bypassed: false,
      pulse: 0
    });

    // TIER 1: 8 NODES (H100 SXM5 Primary Coordinators) - r = 0.28
    for (let i = 0; i < 8; i++) {
      const theta = i * (2 * Math.PI / 8);
      const id = this.nodes.length;
      this.nodes.push({
        id: id,
        tier: 1,
        name: `H100-0${i + 1}`,
        pubkey: `0x7F2A...${(1000 + i * 111).toString(16).toUpperCase()}`,
        tierName: 'Tier 1: H100 SXM5 Primary Coordinator',
        r: 0.28,
        theta: theta,
        parent: 0,
        stake: 500000,
        initialStake: 500000,
        drift: 0.00,
        fp16Hex: '0x3C00',
        state: 'honest',
        active: true,
        bypassed: false,
        pulse: Math.random() * Math.PI
      });
      // Geodesic ray from Apex (id 0) to Tier 1
      this.edges.push({ from: 0, to: id, type: 'tree' });
    }

    // TIER 2: 16 NODES (B200 NVL Tensor Reduction Hubs) - r = 0.58
    for (let i = 0; i < 16; i++) {
      const theta = i * (2 * Math.PI / 16) + (Math.PI / 16);
      const parentId = 1 + Math.floor(i / 2); // 2 children per Tier 1 node
      const id = this.nodes.length;
      this.nodes.push({
        id: id,
        tier: 2,
        name: `B200-${String(i + 1).padStart(2, '0')}`,
        pubkey: `0x992B...${(2000 + i * 77).toString(16).toUpperCase()}`,
        tierName: 'Tier 2: B200 Blackwell Tensor Hub',
        r: 0.58,
        theta: theta,
        parent: parentId,
        stake: 250000,
        initialStake: 250000,
        drift: 0.00,
        fp16Hex: '0x3C00',
        state: 'honest',
        active: true,
        bypassed: false,
        pulse: Math.random() * Math.PI
      });
      this.edges.push({ from: parentId, to: id, type: 'tree' });
    }

    // TIER 3: 40 NODES (RTX 4090 Distributed Edge Quorum) - r = 0.84
    for (let i = 0; i < 40; i++) {
      const theta = i * (2 * Math.PI / 40);
      const parentIdx = Math.floor(i * 16 / 40) % 16;
      const parentId = 9 + parentIdx; // one of Tier 2 nodes
      const id = this.nodes.length;
      this.nodes.push({
        id: id,
        tier: 3,
        name: `RTX4090-${String(i + 1).padStart(2, '0')}`,
        pubkey: `0x1A4C...${(3000 + i * 43).toString(16).toUpperCase()}`,
        tierName: 'Tier 3: RTX 4090 Edge Quorum Validator',
        r: 0.84,
        theta: theta,
        parent: parentId,
        stake: 25000,
        initialStake: 25000,
        drift: 0.00,
        fp16Hex: '0x3C00',
        state: 'honest',
        active: true,
        bypassed: false,
        pulse: Math.random() * Math.PI
      });
      this.edges.push({ from: parentId, to: id, type: 'tree' });
    }

    // LATERAL GOSSIP CHORDS (Circular Geodesics within tiers)
    // Tier 1 chords
    for (let i = 1; i <= 8; i++) {
      const next = i === 8 ? 1 : i + 1;
      this.edges.push({ from: i, to: next, type: 'chord' });
    }
    // Tier 2 chords
    for (let i = 9; i <= 24; i++) {
      const next = i === 24 ? 9 : i + 1;
      this.edges.push({ from: i, to: next, type: 'chord' });
    }
    // Tier 3 cross-chords
    for (let i = 25; i <= 64; i += 4) {
      const next = i + 4 > 64 ? 25 : i + 4;
      this.edges.push({ from: i, to: next, type: 'chord' });
    }

    this.applyActiveK();
  }

  applyActiveK() {
    const activeT2 = Math.min(16, Math.max(0, this.k - 8));
    const activeT3 = Math.max(0, this.k - 24);

    for (let i = 1; i <= 64; i++) {
      const node = this.nodes[i];
      if (node.tier === 1) {
        node.active = true;
      } else if (node.tier === 2) {
        node.active = (i - 9) < activeT2;
      } else if (node.tier === 3) {
        node.active = (i - 25) < activeT3;
      }
    }

    this.updateRouteInvalidations();

    if (this.options.onQuorumChange) {
      this.options.onQuorumChange(this.getMetrics());
    }
  }

  /* -------------------------------------------------------------------------
     2. TRUE POINCARÉ DISC GEODESIC MATHEMATICS
     Circle orthogonal to unit circle |z| = 1 passing through P1 and P2
     ------------------------------------------------------------------------- */
  calculateGeodesic(u1, v1, u2, v2) {
    const cross = u1 * v2 - u2 * v1;
    // If collinear with origin or extremely close, geodesic is straight diameter
    if (Math.abs(cross) < 1e-6) {
      return {
        type: 'line',
        interpolate: (t) => ({
          u: (1 - t) * u1 + t * u2,
          v: (1 - t) * v1 + t * v2
        })
      };
    }

    const D = 2 * cross;
    const s1 = 1 + u1 * u1 + v1 * v1;
    const s2 = 1 + u2 * u2 + v2 * v2;
    const cu = (s1 * v2 - s2 * v1) / D;
    const cv = (u1 * s2 - u2 * s1) / D;
    const R2 = cu * cu + cv * cv - 1;

    if (R2 <= 0) {
      return {
        type: 'line',
        interpolate: (t) => ({
          u: (1 - t) * u1 + t * u2,
          v: (1 - t) * v1 + t * v2
        })
      };
    }

    const R = Math.sqrt(R2);
    const th1 = Math.atan2(v1 - cv, u1 - cu);
    const th2 = Math.atan2(v2 - cv, u2 - cu);
    let dTh = th2 - th1;
    while (dTh > Math.PI) dTh -= 2 * Math.PI;
    while (dTh < -Math.PI) dTh += 2 * Math.PI;

    return {
      type: 'arc',
      cu: cu,
      cv: cv,
      R: R,
      th1: th1,
      th2: th2,
      dTh: dTh,
      anticlockwise: dTh < 0,
      interpolate: (t) => {
        const th = th1 + t * dTh;
        return {
          u: cu + R * Math.cos(th),
          v: cv + R * Math.sin(th)
        };
      }
    };
  }

  getNodeNorm(node) {
    const r = node.r;
    return {
      u: Math.cos(node.theta) * r,
      v: Math.sin(node.theta) * r
    };
  }

  getNodePos(node) {
    const norm = this.getNodeNorm(node);
    return {
      x: this.cx + norm.u * this.radius,
      y: this.cy + norm.v * this.radius
    };
  }

  /* -------------------------------------------------------------------------
     3. TENSOR PACKETS & ZERO-KNOWLEDGE GEODESIC ROUTING
     ------------------------------------------------------------------------- */
  initPackets() {
    this.packets = [];
    const symbols = ['⊗', '∇', 'λ', 'Δ', 'Σ'];
    for (let i = 0; i < 20; i++) {
      this.packets.push(this.spawnPacket(symbols[i % symbols.length]));
    }
  }

  spawnPacket(symbol = '⊗') {
    const activeNodes = this.nodes.filter(n => n.id > 0 && n.active && n.state !== 'slashed');
    if (activeNodes.length === 0) {
      return { path: [0, 1], step: 0, progress: 0, speed: 0.02, symbol: symbol, trail: [], isBypassing: false };
    }

    const mode = Math.random();
    let path = [];

    if (mode < 0.45) {
      // Inward Tensor Reduction: Tier 3 -> Tier 2 -> Tier 1 -> Apex
      const t3Nodes = this.nodes.filter(n => n.tier === 3 && n.active && n.state !== 'slashed');
      const startNode = t3Nodes.length > 0 ? t3Nodes[Math.floor(Math.random() * t3Nodes.length)] : activeNodes[0];
      path = [startNode.id];
      let curr = startNode;
      while (curr.parent >= 0) {
        path.push(curr.parent);
        curr = this.nodes[curr.parent];
      }
    } else if (mode < 0.80) {
      // Outward Broadcast: Apex -> Tier 1 -> Tier 2 -> Tier 3
      const t1Nodes = this.nodes.filter(n => n.tier === 1 && n.active && n.state !== 'slashed');
      const t1 = t1Nodes.length > 0 ? t1Nodes[Math.floor(Math.random() * t1Nodes.length)] : this.nodes[1];
      path = [0, t1.id];
      const t2Children = this.nodes.filter(n => n.parent === t1.id && n.active && n.state !== 'slashed');
      if (t2Children.length > 0) {
        const t2 = t2Children[Math.floor(Math.random() * t2Children.length)];
        path.push(t2.id);
        const t3Children = this.nodes.filter(n => n.parent === t2.id && n.active && n.state !== 'slashed');
        if (t3Children.length > 0) {
          path.push(t3Children[Math.floor(Math.random() * t3Children.length)].id);
        }
      }
    } else {
      // Lateral Gossip Chord
      const tier = Math.random() < 0.5 ? 1 : 2;
      const tierNodes = this.nodes.filter(n => n.tier === tier && n.active && n.state !== 'slashed');
      if (tierNodes.length >= 2) {
        const idx = Math.floor(Math.random() * tierNodes.length);
        const nextIdx = (idx + 1) % tierNodes.length;
        path = [tierNodes[idx].id, tierNodes[nextIdx].id];
      } else {
        path = [0, 1];
      }
    }

    return {
      path: path,
      step: 0,
      progress: 0,
      speed: 0.015 + Math.random() * 0.022,
      symbol: symbol,
      trail: [],
      isBypassing: false
    };
  }

  /* -------------------------------------------------------------------------
     4. BYZANTINE FAULT INJECTION & GEODESIC BYPASS ENGINE
     ------------------------------------------------------------------------- */
  injectByzantineFault(targetId = null) {
    let node = null;
    if (targetId !== null) {
      node = this.nodes[targetId];
    } else {
      const candidates = this.nodes.filter(n => n.id > 0 && n.active && n.state === 'honest');
      if (candidates.length === 0) return null;
      node = candidates[Math.floor(Math.random() * candidates.length)];
    }

    if (!node || node.id === 0) return null;

    node.state = 'byzantine';
    node.pulse = 1.0;

    // Apply specific Byzantine attack vector semantics
    if (this.attackVector === 'gradient-poison') {
      node.drift = +(1.480 + Math.random() * 2.500).toFixed(3);
      node.fp16Hex = '0x7C00 (NaN)';
      this.log(`[ATTACK-VECTOR] Malicious FP16 Gradient Poisoning on ${node.name} &bull; Sign bit flipped: Δε = +${node.drift} FP16`, 'warn');
    } else if (this.attackVector === 'silent-drift') {
      node.drift = +(0.120 + Math.random() * 0.450).toFixed(3);
      node.fp16Hex = `0x3C${Math.floor(Math.random() * 80 + 10)}`;
      this.log(`[ATTACK-VECTOR] Silent Tensor Drift on ${node.name} &bull; Exponent crept past Gromov envelope: Δε = +${node.drift} FP16`, 'warn');
    } else if (this.attackVector === 'equivocation') {
      node.drift = 0.999;
      node.fp16Hex = '0xDUAL_FORK';
      this.log(`[ATTACK-VECTOR] Equivocation on ${node.name} &bull; Conflicting block headers proposed at slot ${this.consensusRound}`, 'warn');
    } else {
      // sybil-stall
      node.drift = 0.00;
      node.fp16Hex = '0xSTALL_DROP';
      this.log(`[ATTACK-VECTOR] Sybil Denial-of-Service on ${node.name} &bull; Partial BLS signatures withheld`, 'warn');
    }

    // Real-time Route Invalidation: invalidate all edges touching this node
    this.updateRouteInvalidations();

    // After evaluation delay (280ms), protocol slashing crank activates
    setTimeout(() => {
      if (node.state === 'byzantine') {
        node.state = 'slashed';
        node.stake = 0;
        node.bypassed = true;

        // Establish Zero-Knowledge Geodesic Fallback Detour
        const peer = this.nodes.find(n => n.id !== node.id && n.tier === node.tier && n.active && n.state === 'honest');
        if (peer) {
          const fromId = node.parent >= 0 ? node.parent : 0;
          this.bypassArcs.push({
            from: fromId,
            to: peer.id,
            bypassedNode: node.id,
            life: 1.0,
            symbol: 'λ'
          });
          if (this.options.onRouteBypass) {
            this.options.onRouteBypass({
              corruptedNode: node,
              bypassFrom: fromId,
              bypassTo: peer.id
            });
          }
        }

        this.shockwaves.push({
          r: 0,
          maxR: this.radius * 0.5,
          color: 'rgba(255, 36, 36, 0.85)',
          alpha: 1.0
        });

        this.triggerFlash(`NODE ${node.name} SLASHED // ZK-FALLBACK ENGAGED`, '#FF2424');
        this.log(`[BN254-KZG-CHECK] Opening verification failed on ${node.name} &bull; Pairing mismatch`, 'highlight');
        this.log(`[SOLANA-SLASH] 25,000 $33RD bonded collateral confiscated -> 1nc1nerator...1111`, 'highlight');
        this.log(`[GEODESIC-BYPASS] Alternate hyperbolic geodesic active &bull; Hop diameter preserved (≤ 8 hops)`, 'success');

        this.updateRouteInvalidations();

        if (this.options.onByzantineEvent) {
          this.options.onByzantineEvent(node, this.getMetrics());
        }
      }
    }, 280);

    if (this.options.onQuorumChange) {
      this.options.onQuorumChange(this.getMetrics());
    }

    return node;
  }

  cureNode(id) {
    const node = this.nodes[id];
    if (!node || node.id === 0) return;
    node.state = 'honest';
    node.stake = node.initialStake;
    node.drift = 0.00;
    node.fp16Hex = '0x3C00';
    node.bypassed = false;
    this.bypassArcs = this.bypassArcs.filter(b => b.bypassedNode !== id);
    this.updateRouteInvalidations();
    this.log(`[SYNC] Node ${node.name} restored to deterministic INT8 invariant.`, 'success');

    if (this.options.onQuorumChange) {
      this.options.onQuorumChange(this.getMetrics());
    }
  }

  setFaultCount(targetFaults) {
    const f = Math.max(0, Math.min(32, parseInt(targetFaults)));
    const activeNodes = this.nodes.filter(n => n.id > 0 && n.active);
    const currentFaults = activeNodes.filter(n => n.state === 'byzantine' || n.state === 'slashed').length;

    if (f > currentFaults) {
      const needed = f - currentFaults;
      const honestList = activeNodes.filter(n => n.state === 'honest');
      for (let i = 0; i < Math.min(needed, honestList.length); i++) {
        this.injectByzantineFault(honestList[i].id);
      }
    } else if (f < currentFaults) {
      const removeCount = currentFaults - f;
      const faultyList = activeNodes.filter(n => n.state === 'byzantine' || n.state === 'slashed');
      for (let i = 0; i < Math.min(removeCount, faultyList.length); i++) {
        this.cureNode(faultyList[i].id);
      }
    }
  }

  setAttackVector(v) {
    this.attackVector = v;
    this.log(`[ATTACK-VECTOR] Set to ${v.toUpperCase()}`);
  }

  updateRouteInvalidations() {
    this.invalidatedRoutes = [];
    const faultyIds = new Set(
      this.nodes.filter(n => n.state === 'byzantine' || n.state === 'slashed').map(n => n.id)
    );

    for (let i = 0; i < this.edges.length; i++) {
      const e = this.edges[i];
      if (faultyIds.has(e.from) || faultyIds.has(e.to)) {
        this.invalidatedRoutes.push(i);
      }
    }
  }

  resetQuorum() {
    for (let i = 1; i <= 64; i++) {
      const node = this.nodes[i];
      node.state = 'honest';
      node.stake = node.initialStake;
      node.drift = 0.00;
      node.fp16Hex = '0x3C00';
      node.bypassed = false;
    }
    this.bypassArcs = [];
    this.invalidatedRoutes = [];
    this.shockwaves.push({
      r: 0,
      maxR: this.radius,
      color: 'rgba(0, 230, 118, 0.75)',
      alpha: 1.0
    });
    this.triggerFlash('QUORUM SYNCHRONIZED // 64 HONEST NODES', '#00E676');
    this.log(`[QUORUM-SYNC] All K=${this.k} validators synchronized to INT8 invariant Δε = 0.00.`, 'success');
    this.log(`[SOLANA-ANCHOR] Zero-knowledge polynomial opening verified in slot ${this.consensusRound}.`, 'success');

    if (this.options.onQuorumChange) {
      this.options.onQuorumChange(this.getMetrics());
    }
  }

  executeConsensusChallenge() {
    this.consensusRound++;
    this.log(`> Executing simulated consensus challenge round [Slot ${this.consensusRound}]...`, 'dim');
    const m = this.getMetrics();
    if (m.isQuorum) {
      this.triggerFlash('CONSENSUS ROUND VALIDATED // 2/3 BLS OK', '#00E676');
      this.shockwaves.push({
        r: 0,
        maxR: this.radius * 0.8,
        color: 'rgba(0, 230, 118, 0.55)',
        alpha: 0.9
      });
      this.log(`[CONSENSUS] Round ${this.consensusRound} verified in 1.418ms &bull; ${m.honestCount}/${m.totalActive} BLS signatures matched &bull; OK`, 'success');
    } else {
      this.triggerFlash('QUORUM BREACH // CIRCUIT BREAKER HALT', '#FF2424');
      this.shockwaves.push({
        r: 0,
        maxR: this.radius,
        color: 'rgba(255, 36, 36, 0.9)',
        alpha: 1.0
      });
      this.log(`[ALERT] BFT Quorum failure: f = ${m.faultCount} > ${m.maxFaults} (1/3 threshold exceeded) &bull; Execution halted`, 'highlight');
    }
  }

  setK(newK) {
    this.k = Math.max(16, Math.min(64, parseInt(newK)));
    this.applyActiveK();
    const metrics = this.getMetrics();
    if (metrics.isQuorum) {
      this.triggerFlash(`COMMITTEE K=${this.k} // QUORUM VALIDATED`, '#FF2424');
    }
  }

  triggerFlash(text, color = '#FF2424') {
    this.bannerText = text;
    this.bannerColor = color;
    this.bannerAlpha = 1.0;

    if (this.options.flashBannerElement) {
      this.options.flashBannerElement.textContent = text;
      this.options.flashBannerElement.style.opacity = '1';
      this.options.flashBannerElement.style.borderColor = color;
      setTimeout(() => {
        if (this.options.flashBannerElement) {
          this.options.flashBannerElement.style.opacity = '0';
        }
      }, 1800);
    }
  }

  log(msg, type = 'dim') {
    if (this.options.onLog) {
      this.options.onLog(msg, type);
    }
  }

  getMetrics() {
    const active = this.nodes.filter(n => n.id > 0 && n.active);
    const honest = active.filter(n => n.state === 'honest');
    const byzantine = active.filter(n => n.state === 'byzantine');
    const slashed = active.filter(n => n.state === 'slashed');
    const faultCount = byzantine.length + slashed.length;
    const threshold = Math.ceil((2 / 3) * active.length);
    const maxFaults = Math.floor((active.length - 1) / 3);
    const isQuorum = honest.length >= threshold;
    const totalSlashedStake = slashed.reduce((acc, n) => acc + (n.initialStake || 25000), 0);

    return {
      k: this.k,
      totalActive: active.length,
      honestCount: honest.length,
      byzantineCount: byzantine.length,
      slashedCount: slashed.length,
      faultCount: faultCount,
      threshold: threshold,
      maxFaults: maxFaults,
      isQuorum: isQuorum,
      honestRatio: active.length > 0 ? honest.length / active.length : 1,
      routingDiameter: 8,
      consensusInvariant: faultCount === 0 ? '0.00 INT8' : `+0.47 FP16 (BYPASS ENGAGED)`,
      solanaFinality: '382ms',
      totalSlashedStake: totalSlashedStake,
      curvature: -1.0,
      deltaHyperbolic: 0.12,
      activeBypasses: this.bypassArcs.length
    };
  }

  /* -------------------------------------------------------------------------
     5. LIFECYCLE & EVENT LISTENERS
     ------------------------------------------------------------------------- */
  resize() {
    const rect = this.canvas.getBoundingClientRect();
    this.width = rect.width || 600;
    this.height = rect.height || 600;
    this.dpr = typeof window !== 'undefined' ? (window.devicePixelRatio || 1) : 1;
    this.canvas.width = Math.round(this.width * this.dpr);
    this.canvas.height = Math.round(this.height * this.dpr);
    if (this.ctx.resetTransform) {
      this.ctx.resetTransform();
    }
    this.ctx.scale(this.dpr, this.dpr);

    this.cx = this.width / 2;
    this.cy = this.height / 2;
    this.radius = Math.min(this.width, this.height) * 0.44;
  }

  bindEvents() {
    if (typeof window === 'undefined') return;
    window.addEventListener('resize', () => this.resize());

    if (!this.options.interactive) return;

    this.canvas.addEventListener('mousemove', (e) => {
      const rect = this.canvas.getBoundingClientRect();
      const mx = e.clientX - rect.left;
      const my = e.clientY - rect.top;

      let closest = null;
      let minDist = 22;

      for (let i = 0; i < this.nodes.length; i++) {
        const n = this.nodes[i];
        if (!n.active && n.id !== 0) continue;
        const pt = this.getNodePos(n);
        const dist = Math.hypot(pt.x - mx, pt.y - my);
        if (dist < minDist) {
          minDist = dist;
          closest = n;
        }
      }

      this.hoveredNode = closest;
      this.canvas.style.cursor = closest ? 'crosshair' : 'default';
    });

    this.canvas.addEventListener('mouseleave', () => {
      this.hoveredNode = null;
    });

    this.canvas.addEventListener('click', () => {
      if (this.hoveredNode && this.hoveredNode.id > 0) {
        if (this.hoveredNode.state === 'honest') {
          this.injectByzantineFault(this.hoveredNode.id);
        } else {
          this.cureNode(this.hoveredNode.id);
        }
      }
    });
  }

  /* -------------------------------------------------------------------------
     6. ANIMATION & 60FPS RENDERING ENGINE
     ------------------------------------------------------------------------- */
  animate(now) {
    if (!this.running) return;
    const dt = Math.min(0.06, (now - this.lastTime) / 1000);
    this.lastTime = now;

    if (!this.paused) {
      this.update(dt);
    }
    this.render();

    if (typeof requestAnimationFrame !== 'undefined') {
      requestAnimationFrame(this.animate);
    }
  }

  update(dt) {
    this.animTime += dt;

    // Node internal clock
    for (let i = 0; i < this.nodes.length; i++) {
      this.nodes[i].pulse += dt * 2.5;
    }

    // Flash banner fade
    if (this.bannerAlpha > 0) {
      this.bannerAlpha = Math.max(0, this.bannerAlpha - dt * 0.75);
    }

    // Shockwaves
    for (let i = this.shockwaves.length - 1; i >= 0; i--) {
      const sw = this.shockwaves[i];
      sw.r += dt * 280;
      sw.alpha -= dt * 0.95;
      if (sw.alpha <= 0 || sw.r >= sw.maxR) {
        this.shockwaves.splice(i, 1);
      }
    }

    // Tensor Packets
    const symbols = ['⊗', '∇', 'λ', 'Δ', 'Σ'];
    for (let i = 0; i < this.packets.length; i++) {
      const p = this.packets[i];
      p.progress += p.speed * (this.options.speed || 1.0);

      if (p.path.length > 1 && p.step < p.path.length - 1) {
        const n1 = this.nodes[p.path[p.step]];
        const n2 = this.nodes[p.path[p.step + 1]];
        if (n1 && n2) {
          const u1 = this.getNodeNorm(n1).u, v1 = this.getNodeNorm(n1).v;
          const u2 = this.getNodeNorm(n2).u, v2 = this.getNodeNorm(n2).v;
          const geo = this.calculateGeodesic(u1, v1, u2, v2);
          const t = Math.min(1, Math.max(0, p.progress));
          const ptNorm = geo.interpolate(t);
          const px = this.cx + ptNorm.u * this.radius;
          const py = this.cy + ptNorm.v * this.radius;

          p.trail.unshift({ x: px, y: py });
          if (p.trail.length > 6) p.trail.pop();
        }
      }

      if (p.progress >= 1.0) {
        p.progress = 0;
        p.step++;

        // Route Invalidation & Zero-Knowledge Fallback Rerouting
        if (p.step < p.path.length) {
          const nextNode = this.nodes[p.path[p.step]];
          if (nextNode && (nextNode.state === 'byzantine' || nextNode.state === 'slashed')) {
            // Find alternate honest peer in same tier
            const alt = this.nodes.find(n => n.id !== nextNode.id && n.tier === nextNode.tier && n.active && n.state === 'honest');
            if (alt) {
              p.path[p.step] = alt.id;
              p.isBypassing = true;
            }
          }
        }

        if (p.step >= p.path.length - 1) {
          this.packets[i] = this.spawnPacket(symbols[Math.floor(Math.random() * symbols.length)]);
        }
      }
    }
  }

  render() {
    const ctx = this.ctx;
    ctx.clearRect(0, 0, this.width, this.height);

    // 1. Deep Obsidian Radial Vignette Background (#070707 Base)
    const bgGrad = ctx.createRadialGradient(this.cx, this.cy, 12, this.cx, this.cy, this.radius * 1.15);
    bgGrad.addColorStop(0, '#070707');
    bgGrad.addColorStop(0.65, '#050505');
    bgGrad.addColorStop(1, '#000000');
    ctx.fillStyle = bgGrad;
    ctx.fillRect(0, 0, this.width, this.height);

    // 2. Poincaré Disc Absolute Horizon Boundary (|z| = 1)
    ctx.save();
    ctx.beginPath();
    ctx.arc(this.cx, this.cy, this.radius, 0, 2 * Math.PI);
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.12)';
    ctx.lineWidth = 1.0;
    ctx.stroke();

    // Subtle Crimson Horizon Accent Hairline
    ctx.beginPath();
    ctx.arc(this.cx, this.cy, this.radius + 1.5, 0, 2 * Math.PI);
    ctx.strokeStyle = 'rgba(255, 36, 36, 0.22)';
    ctx.lineWidth = 1.0;
    ctx.stroke();

    // Perimeter Graduation Ticks (64 slots around Poincaré horizon)
    for (let i = 0; i < 64; i++) {
      const angle = i * (2 * Math.PI / 64);
      const isMajor = i % 8 === 0;
      const tLen = isMajor ? 8 : 4;
      const x1 = this.cx + Math.cos(angle) * (this.radius - tLen);
      const y1 = this.cy + Math.sin(angle) * (this.radius - tLen);
      const x2 = this.cx + Math.cos(angle) * this.radius;
      const y2 = this.cy + Math.sin(angle) * this.radius;

      ctx.beginPath();
      ctx.moveTo(x1, y1);
      ctx.lineTo(x2, y2);
      ctx.strokeStyle = isMajor ? '#FF2424' : 'rgba(255, 255, 255, 0.15)';
      ctx.lineWidth = isMajor ? 1.2 : 0.8;
      ctx.stroke();
    }

    // 3. Exponential Plunge Hyperboloid Horocycles (Metric ds^2 Plunge)
    const horocycles = [
      { r: 0.28, label: 'ρ = 0.29 [TIER 1 H100]' },
      { r: 0.58, label: 'ρ = 0.66 [TIER 2 B200]' },
      { r: 0.84, label: 'ρ = 1.25 [TIER 3 4090]' }
    ];

    ctx.setLineDash([2, 5]);
    for (let i = 0; i < horocycles.length; i++) {
      const hc = horocycles[i];
      const rad = hc.r * this.radius;
      ctx.beginPath();
      ctx.arc(this.cx, this.cy, rad, 0, 2 * Math.PI);
      ctx.strokeStyle = i === 0 ? 'rgba(255, 36, 36, 0.30)' : 'rgba(255, 255, 255, 0.08)';
      ctx.lineWidth = 0.8;
      ctx.stroke();
    }
    ctx.setLineDash([]);

    // 4. Hyperbolic Crosshair Reticle (Coordinate Axes)
    ctx.beginPath();
    ctx.moveTo(this.cx - this.radius, this.cy);
    ctx.lineTo(this.cx + this.radius, this.cy);
    ctx.moveTo(this.cx, this.cy - this.radius);
    ctx.lineTo(this.cx, this.cy + this.radius);
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.05)';
    ctx.lineWidth = 0.8;
    ctx.stroke();

    // 5. True Poincaré Geodesic Connections
    const invalidSet = new Set(this.invalidatedRoutes);

    for (let i = 0; i < this.edges.length; i++) {
      const e = this.edges[i];
      const n1 = this.nodes[e.from];
      const n2 = this.nodes[e.to];
      if (!n1 || !n2) continue;

      const u1 = this.getNodeNorm(n1).u, v1 = this.getNodeNorm(n1).v;
      const u2 = this.getNodeNorm(n2).u, v2 = this.getNodeNorm(n2).v;
      const geo = this.calculateGeodesic(u1, v1, u2, v2);

      const isBothActive = (n1.active || n1.id === 0) && (n2.active || n2.id === 0);
      const isInvalidated = invalidSet.has(i);

      ctx.beginPath();
      if (geo.type === 'line') {
        const p1 = this.getNodePos(n1);
        const p2 = this.getNodePos(n2);
        ctx.moveTo(p1.x, p1.y);
        ctx.lineTo(p2.x, p2.y);
      } else {
        const canvasCx = this.cx + geo.cu * this.radius;
        const canvasCy = this.cy + geo.cv * this.radius;
        const canvasR = geo.R * this.radius;
        ctx.arc(canvasCx, canvasCy, canvasR, geo.th1, geo.th2, geo.anticlockwise);
      }

      if (isInvalidated) {
        // Corrupted Geodesic: Flickering dashed crimson hairline
        ctx.save();
        ctx.strokeStyle = '#FF2424';
        ctx.lineWidth = 1.0;
        ctx.setLineDash([3, 4]);
        ctx.stroke();
        ctx.restore();
      } else if (!isBothActive) {
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.04)';
        ctx.lineWidth = 0.6;
        ctx.stroke();
      } else if (e.type === 'chord') {
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.08)';
        ctx.lineWidth = 0.7;
        ctx.stroke();
      } else {
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.16)';
        ctx.lineWidth = 1.0;
        ctx.stroke();
      }
    }

    // 6. Active Zero-Knowledge Geodesic Fallback Detours (Amber/Crimson Bypass Arcs)
    for (let i = 0; i < this.bypassArcs.length; i++) {
      const b = this.bypassArcs[i];
      const n1 = this.nodes[b.from];
      const n2 = this.nodes[b.to];
      if (!n1 || !n2) continue;

      const u1 = this.getNodeNorm(n1).u, v1 = this.getNodeNorm(n1).v;
      const u2 = this.getNodeNorm(n2).u, v2 = this.getNodeNorm(n2).v;
      const geo = this.calculateGeodesic(u1, v1, u2, v2);

      ctx.save();
      ctx.beginPath();
      if (geo.type === 'line') {
        const p1 = this.getNodePos(n1);
        const p2 = this.getNodePos(n2);
        ctx.moveTo(p1.x, p1.y);
        ctx.lineTo(p2.x, p2.y);
      } else {
        const canvasCx = this.cx + geo.cu * this.radius;
        const canvasCy = this.cy + geo.cv * this.radius;
        const canvasR = geo.R * this.radius;
        ctx.arc(canvasCx, canvasCy, canvasR, geo.th1, geo.th2, geo.anticlockwise);
      }
      ctx.strokeStyle = '#FFAA00';
      ctx.lineWidth = 1.6;
      ctx.setLineDash([5, 4]);
      ctx.lineDashOffset = -this.animTime * 20;
      ctx.stroke();
      ctx.restore();
    }

    // 7. Slashing Shockwaves
    for (let i = 0; i < this.shockwaves.length; i++) {
      const sw = this.shockwaves[i];
      ctx.save();
      ctx.beginPath();
      ctx.arc(this.cx, this.cy, sw.r, 0, 2 * Math.PI);
      ctx.strokeStyle = sw.color;
      ctx.globalAlpha = sw.alpha;
      ctx.lineWidth = 1.6;
      ctx.stroke();
      ctx.restore();
    }

    // 8. Animated Tensor Packets along Geodesics
    for (let i = 0; i < this.packets.length; i++) {
      const p = this.packets[i];
      if (p.path.length <= 1 || p.step >= p.path.length - 1) continue;

      const n1 = this.nodes[p.path[p.step]];
      const n2 = this.nodes[p.path[p.step + 1]];
      if (!n1 || !n2) continue;

      const u1 = this.getNodeNorm(n1).u, v1 = this.getNodeNorm(n1).v;
      const u2 = this.getNodeNorm(n2).u, v2 = this.getNodeNorm(n2).v;
      const geo = this.calculateGeodesic(u1, v1, u2, v2);
      const t = Math.min(1, Math.max(0, p.progress));
      const ptNorm = geo.interpolate(t);
      const px = this.cx + ptNorm.u * this.radius;
      const py = this.cy + ptNorm.v * this.radius;

      // Draw packet trail
      for (let j = 0; j < p.trail.length; j++) {
        const tr = p.trail[j];
        ctx.beginPath();
        ctx.arc(tr.x, tr.y, 2.0 * (1 - j / p.trail.length), 0, 2 * Math.PI);
        ctx.fillStyle = p.isBypassing ? 'rgba(255, 170, 0, 0.4)' : (j % 2 === 0 ? 'rgba(255, 36, 36, 0.45)' : 'rgba(255, 255, 255, 0.4)');
        ctx.fill();
      }

      // Draw tensor glyph
      ctx.save();
      ctx.font = '10px "JetBrains Mono", monospace';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.fillStyle = p.isBypassing ? '#FFAA00' : '#FFFFFF';
      ctx.fillText(p.symbol, px, py);
      ctx.restore();
    }

    // 9. Committee Quorum Nodes
    for (let i = 0; i < this.nodes.length; i++) {
      const n = this.nodes[i];
      const pt = this.getNodePos(n);
      const isHovered = this.hoveredNode && this.hoveredNode.id === n.id;

      if (n.id === 0) {
        // APEX ROOT (Mark #06 Apex Singularity Coordinator)
        // Two canopy white rim points
        ctx.beginPath();
        ctx.arc(pt.x - 7, pt.y - 4, 2.2, 0, 2 * Math.PI);
        ctx.arc(pt.x + 7, pt.y - 4, 2.2, 0, 2 * Math.PI);
        ctx.fillStyle = '#FFFFFF';
        ctx.fill();

        // Canopy wireframe
        ctx.beginPath();
        ctx.moveTo(pt.x - 7, pt.y - 4);
        ctx.lineTo(pt.x, pt.y);
        ctx.lineTo(pt.x + 7, pt.y - 4);
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.45)';
        ctx.lineWidth = 1;
        ctx.stroke();

        // Crimson Throat Singularity Core
        const apexPulse = 1 + Math.sin(n.pulse * 2) * 0.12;
        ctx.save();
        ctx.beginPath();
        ctx.arc(pt.x, pt.y, 5 * apexPulse, 0, 2 * Math.PI);
        ctx.fillStyle = '#FF2424';
        ctx.fill();
        ctx.restore();

        // Stark white center dot
        ctx.beginPath();
        ctx.arc(pt.x, pt.y, 1.8, 0, 2 * Math.PI);
        ctx.fillStyle = '#FFFFFF';
        ctx.fill();

        ctx.font = '8.5px "JetBrains Mono", monospace';
        ctx.fillStyle = 'rgba(255, 255, 255, 0.65)';
        ctx.textAlign = 'center';
        ctx.fillText('APEX // ROOT', pt.x, pt.y + 14);
        continue;
      }

      // Validator Nodes (Tiers 1, 2, 3)
      let radius = n.tier === 1 ? 5.2 : (n.tier === 2 ? 3.8 : 2.6);
      if (isHovered) radius += 2.0;

      if (!n.active) {
        // Inactive / Standby Quorum Node
        ctx.beginPath();
        ctx.arc(pt.x, pt.y, radius, 0, 2 * Math.PI);
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.12)';
        ctx.lineWidth = 0.8;
        ctx.setLineDash([1.5, 1.5]);
        ctx.stroke();
        ctx.setLineDash([]);
        continue;
      }

      if (n.state === 'byzantine') {
        // Byzantine Fault: Jittering Amber/Crimson Glitch Strobe
        const jx = (Math.random() - 0.5) * 3.0;
        const jy = (Math.random() - 0.5) * 3.0;

        ctx.save();
        ctx.beginPath();
        ctx.arc(pt.x + jx, pt.y + jy, radius + 2.5, 0, 2 * Math.PI);
        ctx.fillStyle = '#FF2424';
        ctx.fill();

        ctx.beginPath();
        ctx.arc(pt.x, pt.y, radius, 0, 2 * Math.PI);
        ctx.fillStyle = '#FFFFFF';
        ctx.fill();
        ctx.restore();
      } else if (n.state === 'slashed') {
        // Slashed Node: Red slashed perimeter
        ctx.save();
        ctx.beginPath();
        ctx.arc(pt.x, pt.y, radius + 1.2, 0, 2 * Math.PI);
        ctx.strokeStyle = '#FF2424';
        ctx.lineWidth = 1.4;
        ctx.stroke();

        ctx.beginPath();
        ctx.moveTo(pt.x - radius, pt.y - radius);
        ctx.lineTo(pt.x + radius, pt.y + radius);
        ctx.strokeStyle = '#FF2424';
        ctx.lineWidth = 1.4;
        ctx.stroke();
        ctx.restore();
      } else {
        // Honest Active Validator Node
        ctx.save();
        if (n.tier === 1) {
          // Tier 1: Crimson core with stark white center
          ctx.beginPath();
          ctx.arc(pt.x, pt.y, radius, 0, 2 * Math.PI);
          ctx.fillStyle = '#FF2424';
          ctx.fill();

          ctx.beginPath();
          ctx.arc(pt.x, pt.y, radius * 0.55, 0, 2 * Math.PI);
          ctx.fillStyle = '#FFFFFF';
          ctx.fill();
        } else if (n.tier === 2) {
          // Tier 2: Crisp white core with subtle hairline
          ctx.beginPath();
          ctx.arc(pt.x, pt.y, radius, 0, 2 * Math.PI);
          ctx.fillStyle = '#FFFFFF';
          ctx.fill();
          ctx.strokeStyle = 'rgba(255, 36, 36, 0.45)';
          ctx.lineWidth = 1.0;
          ctx.stroke();
        } else {
          // Tier 3: Sleek stark white dot
          ctx.beginPath();
          ctx.arc(pt.x, pt.y, radius, 0, 2 * Math.PI);
          ctx.fillStyle = '#FFFFFF';
          ctx.fill();
        }
        ctx.restore();
      }

      // Labels for Tier 1 and hovered nodes
      if (n.tier === 1 || isHovered) {
        ctx.font = '8px "JetBrains Mono", monospace';
        ctx.fillStyle = isHovered ? '#FFFFFF' : 'rgba(255, 255, 255, 0.65)';
        ctx.textAlign = 'center';
        const labelY = pt.y > this.cy ? pt.y + radius + 9 : pt.y - radius - 5;
        ctx.fillText(n.name, pt.x, labelY);
      }
    }

    // 10. Hover Telemetry Overlay Card (Zero Cards, Brutalist Hairline Panel)
    if (this.hoveredNode && this.hoveredNode.id > 0) {
      const hn = this.hoveredNode;
      const pt = this.getNodePos(hn);

      const ttWidth = 205;
      const ttHeight = 84;
      let tx = pt.x + 12;
      let ty = pt.y - 42;
      if (tx + ttWidth > this.width - 10) tx = pt.x - ttWidth - 12;
      if (ty < 10) ty = 10;
      if (ty + ttHeight > this.height - 10) ty = this.height - ttHeight - 10;

      ctx.save();
      // Pure Obsidian brutalist hairline box
      ctx.fillStyle = '#070707';
      ctx.fillRect(tx, ty, ttWidth, ttHeight);
      ctx.strokeStyle = hn.state === 'slashed' ? '#FF2424' : (hn.state === 'byzantine' ? '#FF2424' : 'rgba(255, 255, 255, 0.2)');
      ctx.lineWidth = 1.0;
      ctx.strokeRect(tx, ty, ttWidth, ttHeight);

      ctx.font = 'bold 9.5px "JetBrains Mono", monospace';
      ctx.fillStyle = '#FFFFFF';
      ctx.textAlign = 'left';
      ctx.fillText(`${hn.name} // ${hn.pubkey}`, tx + 8, ty + 15);

      ctx.font = '8.5px "JetBrains Mono", monospace';
      ctx.fillStyle = 'rgba(255, 255, 255, 0.65)';
      ctx.fillText(`TIER: ${hn.tierName}`, tx + 8, ty + 28);
      ctx.fillText(`STAKE: ${hn.stake.toLocaleString()} $33RD`, tx + 8, ty + 41);
      ctx.fillText(`FP16 DRIFT: Δε = ${hn.state === 'honest' ? '0.00 INT8' : `+${hn.drift} (${hn.fp16Hex})`}`, tx + 8, ty + 54);

      const statusColor = hn.state === 'honest' ? '#00E676' : '#FF2424';
      ctx.fillStyle = statusColor;
      ctx.fillText(`STATUS: [${hn.state.toUpperCase()}] ${hn.bypassed ? '// ROUTE_BYPASS ACTIVE' : ''}`, tx + 8, ty + 68);
      ctx.restore();
    }

    // 11. On-Canvas Telemetry Heads-Up Reticle
    if (this.options.showHud) {
      ctx.save();
      ctx.font = '9px "JetBrains Mono", monospace';
      ctx.fillStyle = 'rgba(255, 255, 255, 0.45)';
      ctx.textAlign = 'left';
      ctx.fillText('MANIFOLD: POINCARÉ HYPERBOLIC TENSOR ARBOR (κ = -1.0)', 14, 18);
      ctx.fillText('TOPOLOGY: GROMOV δ-HYPERBOLIC EXPONENTIAL PLUNGE', 14, 30);
      ctx.fillText('GEODESIC DIAMETER: ≤ 8 HOPS // ZK-FALLBACK READY', 14, 42);

      const m = this.getMetrics();
      ctx.textAlign = 'right';
      ctx.fillStyle = m.isQuorum ? '#00E676' : '#FF2424';
      ctx.fillText(`COMMITTEE: ${m.honestCount}/${m.totalActive} VALIDATORS [${m.isQuorum ? 'QUORUM VALIDATED' : 'CIRCUIT BREAKER'}]`, this.width - 14, 18);
      ctx.fillStyle = 'rgba(255, 255, 255, 0.45)';
      ctx.fillText(`BYZANTINE DRIFT: ${m.consensusInvariant}`, this.width - 14, 30);
      ctx.fillText(`ANCHOR SETTLEMENT: 382ms SOLANA MAINNET`, this.width - 14, 42);
      ctx.restore();
    }

    // 12. On-Canvas Flash Banner
    if (this.bannerAlpha > 0.01) {
      ctx.save();
      ctx.globalAlpha = this.bannerAlpha;
      const bw = 340;
      const bh = 28;
      const bx = this.cx - bw / 2;
      const by = 52;

      ctx.fillStyle = '#070707';
      ctx.fillRect(bx, by, bw, bh);
      ctx.strokeStyle = this.bannerColor;
      ctx.lineWidth = 1.0;
      ctx.strokeRect(bx, by, bw, bh);

      ctx.font = 'bold 9.5px "JetBrains Mono", monospace';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.fillStyle = '#FFFFFF';
      ctx.fillText(this.bannerText, this.cx, by + bh / 2);
      ctx.restore();
    }

    ctx.restore();
  }
}

// Make globally accessible
if (typeof window !== 'undefined') {
  window.PoincareHyperbolicSimulator = PoincareHyperbolicSimulator;
}
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { PoincareHyperbolicSimulator };
}
