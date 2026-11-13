/**
 * 33RD TREE LABS // POINCARÉ HYPERBOLIC TENSOR ARBOR SIMULATOR
 * Visualizing Gromov delta-hyperbolic manifold (kappa = -1.414)
 * Deterministic INT8 consensus, Byzantine fault tolerance, and geodesic routing.
 * Zero emojis. Strictly high-performance HTML5 Canvas (60fps).
 */

class PoincareHyperbolicSimulator {
  constructor(canvas, options = {}) {
    this.canvas = canvas;
    this.ctx = canvas.getContext('2d');
    this.options = Object.assign({
      k: 64, // Active committee size: 16 to 64
      speed: 1.0,
      interactive: true,
      showHud: true,
      onQuorumChange: null,
      onByzantineEvent: null,
      onLog: null,
      flashBannerElement: null
    }, options);

    this.k = Math.max(16, Math.min(64, this.options.k));
    this.nodes = [];
    this.edges = [];
    this.packets = [];
    this.shockwaves = [];
    this.bypassArcs = [];
    this.hoveredNode = null;
    this.selectedNode = null;
    this.dpr = window.devicePixelRatio || 1;
    this.width = 0;
    this.height = 0;
    this.cx = 0;
    this.cy = 0;
    this.radius = 0;
    this.lastTime = performance.now();
    this.running = true;

    // Flash notification state
    this.bannerText = 'STATE COMMITTED // ANCHOR VERIFIED';
    this.bannerAlpha = 0;
    this.bannerColor = '#FF2424';

    this.initTopology();
    this.initPackets();
    this.resize();
    this.bindEvents();

    this.animate = this.animate.bind(this);
    requestAnimationFrame(this.animate);
  }

  initTopology() {
    this.nodes = [];
    this.edges = [];

    // NODE 0: APEX SINGULARITY ROOT
    this.nodes.push({
      id: 0,
      tier: 0,
      name: 'APEX SINGULARITY',
      tierName: 'Mark #06 Apex Root',
      r: 0.0,
      theta: 0.0,
      parent: -1,
      stake: 1000000,
      initialStake: 1000000,
      drift: 0.00,
      state: 'honest',
      active: true,
      bypassed: false,
      pulse: 0
    });

    // TIER 1: 8 NODES (H100 SXM5 Primary Coordinators) - r = 0.28
    for (let i = 0; i < 8; i++) {
      const theta = i * (2 * Math.PI / 8);
      this.nodes.push({
        id: this.nodes.length,
        tier: 1,
        name: `H100-0${i + 1}`,
        tierName: 'Tier 1: H100 SXM5 Primary Coordinator',
        r: 0.28,
        theta: theta,
        parent: 0,
        stake: 500000,
        initialStake: 500000,
        drift: 0.00,
        state: 'honest',
        active: true,
        bypassed: false,
        pulse: Math.random() * Math.PI
      });
      // Edge from Apex to Tier 1
      this.edges.push({ from: 0, to: this.nodes.length - 1, type: 'tree' });
    }

    // TIER 2: 16 NODES (B200 Blackwell Tensor Reduction Hubs) - r = 0.58
    for (let i = 0; i < 16; i++) {
      const theta = i * (2 * Math.PI / 16) + (Math.PI / 16);
      const parentId = 1 + Math.floor(i / 2); // 2 children per Tier 1 node
      this.nodes.push({
        id: this.nodes.length,
        tier: 2,
        name: `B200-${String(i + 1).padStart(2, '0')}`,
        tierName: 'Tier 2: B200 Blackwell Tensor Hub',
        r: 0.58,
        theta: theta,
        parent: parentId,
        stake: 250000,
        initialStake: 250000,
        drift: 0.00,
        state: 'honest',
        active: true,
        bypassed: false,
        pulse: Math.random() * Math.PI
      });
      this.edges.push({ from: parentId, to: this.nodes.length - 1, type: 'tree' });
    }

    // TIER 3: 40 NODES (RTX 4090 Distributed Edge Quorum) - r = 0.84
    for (let i = 0; i < 40; i++) {
      const theta = i * (2 * Math.PI / 40);
      const parentIdx = Math.floor(i * 16 / 40) % 16;
      const parentId = 9 + parentIdx; // one of Tier 2 nodes
      this.nodes.push({
        id: this.nodes.length,
        tier: 3,
        name: `RTX4090-${String(i + 1).padStart(2, '0')}`,
        tierName: 'Tier 3: RTX 4090 Distributed Edge',
        r: 0.84,
        theta: theta,
        parent: parentId,
        stake: 50000,
        initialStake: 50000,
        drift: 0.00,
        state: 'honest',
        active: true,
        bypassed: false,
        pulse: Math.random() * Math.PI
      });
      this.edges.push({ from: parentId, to: this.nodes.length - 1, type: 'tree' });
    }

    // PEER CHORDAL GEODESICS (Inter-tier gossip connections)
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

    this.applyActiveK();
  }

  applyActiveK() {
    // Exactly K validator nodes (1..64) are active
    // Tier 1 (1..8): always active (8 nodes)
    // Tier 2 (9..24): active up to min(K-8, 16)
    // Tier 3 (25..64): active up to max(0, K-24)
    const activeT2 = Math.min(16, Math.max(0, this.k - 8));
    const activeT3 = Math.max(0, this.k - 24);

    for (let i = 1; i <= 64; i++) {
      const node = this.nodes[i];
      if (node.tier === 1) {
        node.active = true;
      } else if (node.tier === 2) {
        const relIdx = i - 9;
        node.active = relIdx < activeT2;
      } else if (node.tier === 3) {
        const relIdx = i - 25;
        node.active = relIdx < activeT3;
      }
    }

    if (this.options.onQuorumChange) {
      this.options.onQuorumChange(this.getMetrics());
    }
  }

  initPackets() {
    this.packets = [];
    const symbols = ['⊗', '∇', 'λ', 'Δ'];
    for (let i = 0; i < 16; i++) {
      this.packets.push(this.spawnPacket(symbols[i % symbols.length]));
    }
  }

  spawnPacket(symbol = '⊗') {
    // Generate valid path
    const activeNodes = this.nodes.filter(n => n.id > 0 && n.active && n.state !== 'slashed');
    if (activeNodes.length === 0) {
      return { path: [0, 1], step: 0, progress: 0, speed: 0.02, symbol: symbol, trail: [] };
    }

    const type = Math.random();
    let path = [];

    if (type < 0.45) {
      // Inward Tensor Reduction: Tier 3 -> Tier 2 -> Tier 1 -> Apex
      const t3Nodes = this.nodes.filter(n => n.tier === 3 && n.active && n.state !== 'slashed');
      const startNode = t3Nodes.length > 0 ? t3Nodes[Math.floor(Math.random() * t3Nodes.length)] : activeNodes[Math.floor(Math.random() * activeNodes.length)];
      path = [startNode.id];
      let curr = startNode;
      while (curr.parent >= 0) {
        path.push(curr.parent);
        curr = this.nodes[curr.parent];
      }
    } else if (type < 0.8) {
      // Outward Broadcast: Apex -> Tier 1 -> Tier 2 -> Tier 3
      const t1Nodes = this.nodes.filter(n => n.tier === 1 && n.active && n.state !== 'slashed');
      const t1 = t1Nodes[Math.floor(Math.random() * t1Nodes.length)];
      path = [0, t1.id];
      // pick a child in Tier 2
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
      // Lateral Gossip chord
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
      speed: 0.012 + Math.random() * 0.018,
      symbol: symbol,
      trail: []
    };
  }

  resize() {
    const rect = this.canvas.getBoundingClientRect();
    this.width = rect.width;
    this.height = rect.height;
    this.dpr = window.devicePixelRatio || 1;
    this.canvas.width = Math.round(this.width * this.dpr);
    this.canvas.height = Math.round(this.height * this.dpr);
    this.ctx.resetTransform?.();
    this.ctx.scale(this.dpr, this.dpr);

    this.cx = this.width / 2;
    this.cy = this.height / 2;
    this.radius = Math.min(this.width, this.height) * 0.44;
  }

  bindEvents() {
    window.addEventListener('resize', () => this.resize());

    if (!this.options.interactive) return;

    this.canvas.addEventListener('mousemove', (e) => {
      const rect = this.canvas.getBoundingClientRect();
      const mx = e.clientX - rect.left;
      const my = e.clientY - rect.top;

      let closest = null;
      let minDist = 18;

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

    this.canvas.addEventListener('click', (e) => {
      if (this.hoveredNode && this.hoveredNode.id > 0) {
        if (this.hoveredNode.state === 'honest') {
          this.injectByzantineFault(this.hoveredNode.id);
        } else {
          this.cureNode(this.hoveredNode.id);
        }
      }
    });
  }

  getNodePos(node) {
    const rad = node.r * this.radius;
    const x = this.cx + Math.cos(node.theta) * rad;
    const y = this.cy + Math.sin(node.theta) * rad;
    return { x, y };
  }

  getControlPoint(p1, p2, tier1, tier2) {
    // Hyperbolic Bézier: midpoint vector pulled inward toward center (cx, cy)
    const mx = (p1.x + p2.x) / 2;
    const my = (p1.y + p2.y) / 2;
    const vx = mx - this.cx;
    const vy = my - this.cy;
    // Pull factor depends on radii
    let lambda = 0.68;
    if (tier1 === 0 || tier2 === 0) {
      lambda = 1.0; // Straight line from Apex
    } else if (tier1 === tier2) {
      lambda = tier1 === 1 ? 0.72 : 0.80; // Lateral chords bow inward
    } else {
      lambda = 0.65; // Tree branches
    }
    return { x: this.cx + vx * lambda, y: this.cy + vy * lambda };
  }

  setK(newK) {
    this.k = Math.max(16, Math.min(64, parseInt(newK)));
    this.applyActiveK();
    const metrics = this.getMetrics();
    if (metrics.honestRatio >= 0.667) {
      this.triggerFlash('STATE COMMITTED // ANCHOR VERIFIED', '#FF2424');
      this.shockwaves.push({ r: 0, maxR: this.radius, color: 'rgba(255, 36, 36, 0.6)', alpha: 1 });
    }
  }

  injectByzantineFault(targetId = null) {
    let node = null;
    if (targetId !== null) {
      node = this.nodes[targetId];
    } else {
      // Pick random honest active node
      const candidates = this.nodes.filter(n => n.id > 0 && n.active && n.state === 'honest');
      if (candidates.length === 0) return null;
      node = candidates[Math.floor(Math.random() * candidates.length)];
    }

    if (!node) return null;

    node.state = 'byzantine';
    node.drift = +(0.250 + Math.random() * 0.680).toFixed(3);
    node.pulse = 1.0;

    const driftLabel = `+${node.drift} FP16`;
    this.log(`[BYZANTINE] Node ${node.name} (${node.tierName}) injected drift error: Δε = ${driftLabel}`);

    // Evaluation delay: after 350ms, Byzantine consensus detects error and slashes
    setTimeout(() => {
      if (node.state === 'byzantine') {
        node.state = 'slashed';
        node.stake = 0;
        node.bypassed = true;

        // Find sibling/peer for geodesic bypass arc
        const peer = this.nodes.find(n => n.id !== node.id && n.tier === node.tier && n.active && n.state === 'honest');
        if (peer) {
          this.bypassArcs.push({ from: node.parent >= 0 ? node.parent : 0, to: peer.id, bypassedNode: node.id, life: 1.0 });
        }

        this.shockwaves.push({ r: 0, maxR: this.radius * 0.4, color: 'rgba(255, 36, 36, 0.8)', alpha: 1 });
        this.triggerFlash(`NODE ${node.name} SLASHED // BYPASS ENGAGED`, '#FF2424');

        this.log(`[HASH-MISMATCH] INT8 invariant failed on ${node.name}. Proof rejected by 2/3 BLS committee.`);
        this.log(`[SLASH-CRANK] Confiscated 100% stake -> Solana 1nc1nerator...1111`);
        this.log(`[GEODESIC-BYPASS] Dynamic tree routing bypass active. Diameter ≤ 8 hops preserved.`);

        if (this.options.onByzantineEvent) {
          this.options.onByzantineEvent(node, this.getMetrics());
        }
      }
    }, 350);

    return node;
  }

  cureNode(id) {
    const node = this.nodes[id];
    if (!node) return;
    node.state = 'honest';
    node.stake = node.initialStake;
    node.drift = 0.00;
    node.bypassed = false;
    this.bypassArcs = this.bypassArcs.filter(b => b.bypassedNode !== id);
    this.log(`[SYNC] Node ${node.name} restored to deterministic INT8 invariant.`);
  }

  resetQuorum() {
    for (let i = 1; i <= 64; i++) {
      const node = this.nodes[i];
      node.state = 'honest';
      node.stake = node.initialStake;
      node.drift = 0.00;
      node.bypassed = false;
    }
    this.bypassArcs = [];
    this.shockwaves.push({ r: 0, maxR: this.radius, color: 'rgba(0, 230, 118, 0.8)', alpha: 1 });
    this.triggerFlash('STATE COMMITTED // ANCHOR VERIFIED', '#FF2424');

    this.log(`[QUORUM-SYNC] All K=${this.k} validators synchronized to INT8 invariant Δε = 0.00.`);
    this.log(`[SOLANA-ANCHOR] Zero-knowledge polynomial opening verified in slot.`);

    if (this.options.onQuorumChange) {
      this.options.onQuorumChange(this.getMetrics());
    }
  }

  triggerFlash(text, color = '#FF2424') {
    this.bannerText = text;
    this.bannerColor = color;
    this.bannerAlpha = 1.0;

    if (this.options.flashBannerElement) {
      this.options.flashBannerElement.textContent = text;
      this.options.flashBannerElement.style.opacity = '1';
      setTimeout(() => {
        if (this.options.flashBannerElement) {
          this.options.flashBannerElement.style.opacity = '0';
        }
      }, 1800);
    }
  }

  log(msg) {
    if (this.options.onLog) {
      this.options.onLog(msg);
    }
  }

  getMetrics() {
    const active = this.nodes.filter(n => n.id > 0 && n.active);
    const honest = active.filter(n => n.state === 'honest');
    const byzantine = active.filter(n => n.state === 'byzantine');
    const slashed = active.filter(n => n.state === 'slashed');
    const threshold = Math.ceil((2 / 3) * active.length);
    const maxF = Math.floor((active.length - 1) / 3);
    const isQuorum = honest.length >= threshold;

    return {
      k: this.k,
      totalActive: active.length,
      honestCount: honest.length,
      byzantineCount: byzantine.length,
      slashedCount: slashed.length,
      faultCount: byzantine.length + slashed.length,
      threshold: threshold,
      maxFaults: maxF,
      isQuorum: isQuorum,
      honestRatio: active.length > 0 ? honest.length / active.length : 1,
      routingDiameter: 8,
      consensusInvariant: (byzantine.length === 0 && slashed.length === 0) ? '0.00 INT8' : '+0.47 FP16 (BYPASS ENGAGED)',
      solanaFinality: '382ms'
    };
  }

  animate(now) {
    if (!this.running) return;
    const dt = (now - this.lastTime) / 1000;
    this.lastTime = now;

    this.update(dt);
    this.render();

    requestAnimationFrame(this.animate);
  }

  update(dt) {
    // Pulse animation on nodes
    for (let i = 0; i < this.nodes.length; i++) {
      this.nodes[i].pulse += dt * 2;
    }

    // Flash banner fade
    if (this.bannerAlpha > 0) {
      this.bannerAlpha = Math.max(0, this.bannerAlpha - dt * 0.7);
    }

    // Shockwaves
    for (let i = this.shockwaves.length - 1; i >= 0; i--) {
      const sw = this.shockwaves[i];
      sw.r += dt * 260;
      sw.alpha -= dt * 0.9;
      if (sw.alpha <= 0 || sw.r >= sw.maxR) {
        this.shockwaves.splice(i, 1);
      }
    }

    // Packets
    const symbols = ['⊗', '∇', 'λ', 'Δ'];
    for (let i = 0; i < this.packets.length; i++) {
      const p = this.packets[i];
      p.progress += p.speed * (this.options.speed || 1.0);

      // Record trail
      if (p.path.length > 1 && p.step < p.path.length - 1) {
        const n1 = this.nodes[p.path[p.step]];
        const n2 = this.nodes[p.path[p.step + 1]];
        if (n1 && n2) {
          const pt1 = this.getNodePos(n1);
          const pt2 = this.getNodePos(n2);
          const cp = this.getControlPoint(pt1, pt2, n1.tier, n2.tier);
          const t = Math.min(1, Math.max(0, p.progress));
          const px = (1 - t) * (1 - t) * pt1.x + 2 * (1 - t) * t * cp.x + t * t * pt2.x;
          const py = (1 - t) * (1 - t) * pt1.y + 2 * (1 - t) * t * cp.y + t * t * pt2.y;
          p.trail.unshift({ x: px, y: py });
          if (p.trail.length > 5) p.trail.pop();
        }
      }

      if (p.progress >= 1.0) {
        p.progress = 0;
        p.step++;
        // If reached next step and it's slashed, bypass!
        if (p.step < p.path.length) {
          const nextNode = this.nodes[p.path[p.step]];
          if (nextNode && nextNode.state === 'slashed') {
            // Find alternate peer
            const alt = this.nodes.find(n => n.id !== nextNode.id && n.tier === nextNode.tier && n.active && n.state === 'honest');
            if (alt) {
              p.path[p.step] = alt.id;
            }
          }
        }
        if (p.step >= p.path.length - 1) {
          // Re-spawn packet
          this.packets[i] = this.spawnPacket(symbols[Math.floor(Math.random() * symbols.length)]);
        }
      }
    }
  }

  render() {
    const ctx = this.ctx;
    ctx.clearRect(0, 0, this.width, this.height);

    // 1. Deep Obsidian Radial Vignette
    const bgGrad = ctx.createRadialGradient(this.cx, this.cy, 10, this.cx, this.cy, this.radius * 1.08);
    bgGrad.addColorStop(0, '#07070B');
    bgGrad.addColorStop(0.7, '#040407');
    bgGrad.addColorStop(1, '#020204');
    ctx.fillStyle = bgGrad;
    ctx.fillRect(0, 0, this.width, this.height);

    // 2. Poincaré Disk Absolute Horizon Boundary (r = R)
    ctx.save();
    ctx.beginPath();
    ctx.arc(this.cx, this.cy, this.radius, 0, 2 * Math.PI);
    ctx.strokeStyle = '#22222E';
    ctx.lineWidth = 1.4;
    ctx.stroke();

    // Subtle dark outer glow ring
    ctx.strokeStyle = 'rgba(255, 36, 36, 0.12)';
    ctx.lineWidth = 4;
    ctx.stroke();

    // Perimeter Graduation Ticks (64 ticks around Poincaré disc)
    for (let i = 0; i < 64; i++) {
      const angle = i * (2 * Math.PI / 64);
      const isMajor = i % 8 === 0;
      const tLen = isMajor ? 7 : 3.5;
      const x1 = this.cx + Math.cos(angle) * (this.radius - tLen);
      const y1 = this.cy + Math.sin(angle) * (this.radius - tLen);
      const x2 = this.cx + Math.cos(angle) * this.radius;
      const y2 = this.cy + Math.sin(angle) * this.radius;

      ctx.beginPath();
      ctx.moveTo(x1, y1);
      ctx.lineTo(x2, y2);
      ctx.strokeStyle = isMajor ? 'rgba(255, 255, 255, 0.45)' : 'rgba(255, 255, 255, 0.15)';
      ctx.lineWidth = isMajor ? 1.2 : 0.8;
      ctx.stroke();
    }

    // 3. Concentric Hyperbolic Distance Rings (Horocycles)
    const rings = [
      { r: 0.28, label: 'ρ = 0.29 [TIER 1 H100]' },
      { r: 0.58, label: 'ρ = 0.66 [TIER 2 B200]' },
      { r: 0.84, label: 'ρ = 1.25 [TIER 3 4090]' }
    ];

    ctx.setLineDash([2, 4]);
    for (let i = 0; i < rings.length; i++) {
      const ring = rings[i];
      const rad = ring.r * this.radius;
      ctx.beginPath();
      ctx.arc(this.cx, this.cy, rad, 0, 2 * Math.PI);
      ctx.strokeStyle = i === 0 ? 'rgba(255, 36, 36, 0.22)' : 'rgba(255, 255, 255, 0.10)';
      ctx.lineWidth = 0.9;
      ctx.stroke();
    }
    ctx.setLineDash([]);

    // 4. Hyperbolic Coordinate Axes (Crosshair reticle)
    ctx.beginPath();
    ctx.moveTo(this.cx - this.radius, this.cy);
    ctx.lineTo(this.cx + this.radius, this.cy);
    ctx.moveTo(this.cx, this.cy - this.radius);
    ctx.lineTo(this.cx, this.cy + this.radius);
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.04)';
    ctx.lineWidth = 0.8;
    ctx.stroke();

    // 5. Geodesic Connections (Curved hyperbolic rays)
    for (let i = 0; i < this.edges.length; i++) {
      const e = this.edges[i];
      const n1 = this.nodes[e.from];
      const n2 = this.nodes[e.to];
      if (!n1 || !n2) continue;

      const p1 = this.getNodePos(n1);
      const p2 = this.getNodePos(n2);
      const cp = this.getControlPoint(p1, p2, n1.tier, n2.tier);

      const isBothActive = (n1.active || n1.id === 0) && (n2.active || n2.id === 0);
      const isSlashed = n1.state === 'slashed' || n2.state === 'slashed';

      ctx.beginPath();
      ctx.moveTo(p1.x, p1.y);
      if (n1.id === 0) {
        ctx.lineTo(p2.x, p2.y); // Straight radial ray from Apex
      } else {
        ctx.quadraticCurveTo(cp.x, cp.y, p2.x, p2.y);
      }

      if (isSlashed) {
        ctx.strokeStyle = 'rgba(255, 36, 36, 0.18)';
        ctx.setLineDash([2, 4]);
        ctx.lineWidth = 0.8;
        ctx.stroke();
        ctx.setLineDash([]);
      } else if (!isBothActive) {
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.04)';
        ctx.lineWidth = 0.6;
        ctx.stroke();
      } else if (e.type === 'chord') {
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.07)';
        ctx.lineWidth = 0.7;
        ctx.stroke();
      } else {
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.16)';
        ctx.lineWidth = 1.0;
        ctx.stroke();
      }
    }

    // 6. Active Geodesic Bypass Detours
    for (let i = 0; i < this.bypassArcs.length; i++) {
      const b = this.bypassArcs[i];
      const n1 = this.nodes[b.from];
      const n2 = this.nodes[b.to];
      if (!n1 || !n2) continue;
      const p1 = this.getNodePos(n1);
      const p2 = this.getNodePos(n2);
      const cp = this.getControlPoint(p1, p2, n1.tier, n2.tier);

      ctx.save();
      ctx.beginPath();
      ctx.moveTo(p1.x, p1.y);
      ctx.quadraticCurveTo(cp.x, cp.y, p2.x, p2.y);
      ctx.strokeStyle = '#FFAA00';
      ctx.lineWidth = 1.6;
      ctx.setLineDash([4, 4]);
      ctx.stroke();
      ctx.restore();
    }

    // 7. Shockwaves
    for (let i = 0; i < this.shockwaves.length; i++) {
      const sw = this.shockwaves[i];
      ctx.save();
      ctx.beginPath();
      ctx.arc(this.cx, this.cy, sw.r, 0, 2 * Math.PI);
      ctx.strokeStyle = sw.color;
      ctx.globalAlpha = sw.alpha;
      ctx.lineWidth = 2.0;
      ctx.stroke();
      ctx.restore();
    }

    // 8. Animated Tensor Packets (⊗, ∇, λ, Δ)
    for (let i = 0; i < this.packets.length; i++) {
      const p = this.packets[i];
      if (p.path.length <= 1 || p.step >= p.path.length - 1) continue;

      const n1 = this.nodes[p.path[p.step]];
      const n2 = this.nodes[p.path[p.step + 1]];
      if (!n1 || !n2) continue;

      const pt1 = this.getNodePos(n1);
      const pt2 = this.getNodePos(n2);
      const cp = this.getControlPoint(pt1, pt2, n1.tier, n2.tier);
      const t = Math.min(1, Math.max(0, p.progress));

      const px = (1 - t) * (1 - t) * pt1.x + 2 * (1 - t) * t * cp.x + t * t * pt2.x;
      const py = (1 - t) * (1 - t) * pt1.y + 2 * (1 - t) * t * cp.y + t * t * pt2.y;

      // Draw packet trail
      for (let j = 0; j < p.trail.length; j++) {
        const tr = p.trail[j];
        ctx.beginPath();
        ctx.arc(tr.x, tr.y, 2.0 * (1 - j / p.trail.length), 0, 2 * Math.PI);
        ctx.fillStyle = j % 2 === 0 ? 'rgba(255, 36, 36, 0.45)' : 'rgba(255, 255, 255, 0.4)';
        ctx.fill();
      }

      // Draw glyph
      ctx.save();
      ctx.font = '11px "JetBrains Mono", monospace';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';

      // Glow halo
      ctx.shadowColor = '#FF2424';
      ctx.shadowBlur = 8;
      ctx.fillStyle = '#FFFFFF';
      ctx.fillText(p.symbol, px, py);
      ctx.restore();
    }

    // 9. Render Nodes
    for (let i = 0; i < this.nodes.length; i++) {
      const n = this.nodes[i];
      const pt = this.getNodePos(n);
      const isHovered = this.hoveredNode && this.hoveredNode.id === n.id;

      if (n.id === 0) {
        // APEX SINGULARITY (Mark #06 Root Node)
        // Two white canopy rim nodes
        ctx.beginPath();
        ctx.arc(pt.x - 7, pt.y - 4, 2.2, 0, 2 * Math.PI);
        ctx.arc(pt.x + 7, pt.y - 4, 2.2, 0, 2 * Math.PI);
        ctx.fillStyle = '#FFFFFF';
        ctx.fill();

        // Connecting wireframe
        ctx.beginPath();
        ctx.moveTo(pt.x - 7, pt.y - 4);
        ctx.lineTo(pt.x, pt.y);
        ctx.lineTo(pt.x + 7, pt.y - 4);
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.5)';
        ctx.lineWidth = 1;
        ctx.stroke();

        // Crimson Throat Singularity Core
        const apexPulse = 1 + Math.sin(n.pulse * 2) * 0.15;
        ctx.save();
        ctx.shadowColor = '#FF2424';
        ctx.shadowBlur = 14;
        ctx.beginPath();
        ctx.arc(pt.x, pt.y, 5 * apexPulse, 0, 2 * Math.PI);
        ctx.fillStyle = '#FF2424';
        ctx.fill();
        ctx.restore();

        // White needle center
        ctx.beginPath();
        ctx.arc(pt.x, pt.y, 1.8, 0, 2 * Math.PI);
        ctx.fillStyle = '#FFFFFF';
        ctx.fill();

        // Apex label
        ctx.font = '9px "JetBrains Mono", monospace';
        ctx.fillStyle = 'rgba(255, 255, 255, 0.7)';
        ctx.textAlign = 'center';
        ctx.fillText('APEX // ROOT', pt.x, pt.y + 14);
        continue;
      }

      // Validator Nodes (Tiers 1, 2, 3)
      let radius = n.tier === 1 ? 5.2 : n.tier === 2 ? 3.8 : 2.6;
      if (isHovered) radius += 2.0;

      if (!n.active) {
        // Inactive / Standby node
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
        // Byzantine Fault: Jittering Amber/Crimson Glitch
        const jx = (Math.random() - 0.5) * 2.5;
        const jy = (Math.random() - 0.5) * 2.5;

        ctx.save();
        ctx.shadowColor = '#FFAA00';
        ctx.shadowBlur = 12;
        ctx.beginPath();
        ctx.arc(pt.x + jx, pt.y + jy, radius + 2, 0, 2 * Math.PI);
        ctx.fillStyle = '#FFAA00';
        ctx.fill();
        ctx.restore();

        ctx.beginPath();
        ctx.arc(pt.x, pt.y, radius, 0, 2 * Math.PI);
        ctx.fillStyle = '#FFFFFF';
        ctx.fill();
      } else if (n.state === 'slashed') {
        // Slashed Node: Red slashed tombstone badge
        ctx.save();
        ctx.beginPath();
        ctx.arc(pt.x, pt.y, radius + 1, 0, 2 * Math.PI);
        ctx.strokeStyle = '#FF2424';
        ctx.lineWidth = 1.4;
        ctx.stroke();

        // Diagonal slash
        ctx.beginPath();
        ctx.moveTo(pt.x - radius, pt.y - radius);
        ctx.lineTo(pt.x + radius, pt.y + radius);
        ctx.strokeStyle = '#FF2424';
        ctx.lineWidth = 1.4;
        ctx.stroke();
        ctx.restore();
      } else {
        // Honest Active Validator
        ctx.save();
        if (n.tier === 1) {
          // Tier 1: Crimson aura + stark white core
          ctx.shadowColor = '#FF2424';
          ctx.shadowBlur = 8;
          ctx.beginPath();
          ctx.arc(pt.x, pt.y, radius, 0, 2 * Math.PI);
          ctx.fillStyle = '#FF2424';
          ctx.fill();

          ctx.beginPath();
          ctx.arc(pt.x, pt.y, radius * 0.55, 0, 2 * Math.PI);
          ctx.fillStyle = '#FFFFFF';
          ctx.fill();
        } else if (n.tier === 2) {
          // Tier 2: Crisp white core + subtle ring
          ctx.beginPath();
          ctx.arc(pt.x, pt.y, radius, 0, 2 * Math.PI);
          ctx.fillStyle = '#FFFFFF';
          ctx.fill();
          ctx.strokeStyle = 'rgba(255, 41, 44, 0.4)';
          ctx.lineWidth = 1.0;
          ctx.stroke();
        } else {
          // Tier 3: Sleek slate-white perimeter dot
          ctx.beginPath();
          ctx.arc(pt.x, pt.y, radius, 0, 2 * Math.PI);
          ctx.fillStyle = 'rgba(255, 255, 255, 0.85)';
          ctx.fill();
        }
        ctx.restore();
      }

      // Node labels for Tier 1 & hovered nodes
      if (n.tier === 1 || isHovered) {
        ctx.font = '8.5px "JetBrains Mono", monospace';
        ctx.fillStyle = isHovered ? '#FFFFFF' : 'rgba(255, 255, 255, 0.65)';
        ctx.textAlign = 'center';
        const labelY = pt.y > this.cy ? pt.y + radius + 9 : pt.y - radius - 5;
        ctx.fillText(n.name, pt.x, labelY);
      }
    }

    // 10. Hover Tooltip Overlay
    if (this.hoveredNode && this.hoveredNode.id > 0) {
      const hn = this.hoveredNode;
      const pt = this.getNodePos(hn);

      const ttWidth = 190;
      const ttHeight = 78;
      let tx = pt.x + 12;
      let ty = pt.y - 40;
      if (tx + ttWidth > this.width - 10) tx = pt.x - ttWidth - 12;
      if (ty < 10) ty = 10;
      if (ty + ttHeight > this.height - 10) ty = this.height - ttHeight - 10;

      ctx.save();
      ctx.fillStyle = 'rgba(8, 8, 12, 0.94)';
      ctx.strokeStyle = hn.state === 'slashed' ? '#FF2424' : hn.state === 'byzantine' ? '#FFAA00' : '#444455';
      ctx.lineWidth = 1.0;
      ctx.fillRect(tx, ty, ttWidth, ttHeight);
      ctx.strokeRect(tx, ty, ttWidth, ttHeight);

      ctx.font = 'bold 9.5px "JetBrains Mono", monospace';
      ctx.fillStyle = '#FFFFFF';
      ctx.textAlign = 'left';
      ctx.fillText(hn.name + ' // ' + (hn.tier === 1 ? 'H100' : hn.tier === 2 ? 'B200' : 'RTX4090'), tx + 8, ty + 15);

      ctx.font = '8.5px "JetBrains Mono", monospace';
      ctx.fillStyle = 'rgba(255, 255, 255, 0.7)';
      ctx.fillText(`TIER: ${hn.tierName}`, tx + 8, ty + 28);
      ctx.fillText(`STAKE: ${hn.stake.toLocaleString()} $33RD`, tx + 8, ty + 41);
      ctx.fillText(`INVARIANT: Δε = ${hn.state === 'honest' ? '0.00 INT8' : `+${hn.drift} FP16`}`, tx + 8, ty + 54);

      const statusColor = hn.state === 'honest' ? '#00E676' : hn.state === 'byzantine' ? '#FFAA00' : '#FF2424';
      ctx.fillStyle = statusColor;
      ctx.fillText(`STATUS: [${hn.state.toUpperCase()}]`, tx + 8, ty + 68);
      ctx.restore();
    }

    // 11. Live On-Canvas Telemetry HUD (Top-Left & Top-Right)
    if (this.options.showHud) {
      ctx.save();
      ctx.font = '9px "JetBrains Mono", monospace';
      ctx.fillStyle = 'rgba(255, 255, 255, 0.45)';
      ctx.textAlign = 'left';
      ctx.fillText('MANIFOLD: POINCARÉ DISK MODEL (κ = -1.414)', 14, 18);
      ctx.fillText('TOPOLOGY: GROMOV δ-HYPERBOLIC TENSOR ARBOR', 14, 30);
      ctx.fillText('MAX DIAMETER: ≤ 8 HOPS // SUB-SECOND CONVERGENCE', 14, 42);

      const metrics = this.getMetrics();
      ctx.textAlign = 'right';
      ctx.fillStyle = metrics.isQuorum ? '#00E676' : '#FF2424';
      ctx.fillText(`QUORUM: ${metrics.honestCount}/${metrics.totalActive} VALIDATORS (${metrics.isQuorum ? 'VALIDATED' : 'BREACH'})`, this.width - 14, 18);
      ctx.fillStyle = 'rgba(255, 255, 255, 0.45)';
      ctx.fillText(`INVARIANT: ${metrics.consensusInvariant}`, this.width - 14, 30);
      ctx.fillText(`SOLANA SETTLEMENT: ${metrics.solanaFinality} ANCHOR COMMIT`, this.width - 14, 42);
      ctx.restore();
    }

    // 12. On-Canvas Flash Banner
    if (this.bannerAlpha > 0.01) {
      ctx.save();
      ctx.globalAlpha = this.bannerAlpha;
      const bw = 320;
      const bh = 28;
      const bx = this.cx - bw / 2;
      const by = 54;

      ctx.fillStyle = 'rgba(10, 10, 14, 0.90)';
      ctx.fillRect(bx, by, bw, bh);
      ctx.strokeStyle = this.bannerColor;
      ctx.lineWidth = 1.2;
      ctx.strokeRect(bx, by, bw, bh);

      ctx.font = 'bold 10px "JetBrains Mono", monospace';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.fillStyle = '#FFFFFF';
      ctx.shadowColor = this.bannerColor;
      ctx.shadowBlur = 6;
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
