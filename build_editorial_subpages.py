#!/usr/bin/env python3
"""
33rd Tree Labs - Editorial Brutalist Subpage Generator
Dramatically expands nodes.html, tokenomics.html, and research.html:
- Eliminates boxed card containers in favor of open brutalist layouts with hairlines
- Packed with deep technical architecture and mathematical proofs
- Lenis smooth inertia with lerp: 0.14, wheelMultiplier: 1.25 for snappy scrolling
- Zero emojis, official domain 33rdtreelabs.tech
"""

import os

SITE_DIR = "/Users/ianmora/Desktop/Projects/33rd-tree-labs-site"

def get_shared_head(title, description, active_page="nodes"):
    return f"""<!doctype html>
<html lang="en" class="lenis" style="--t: #FF2424; --f: #070707;">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta name="theme-color" content="#070707">

  <!-- OpenGraph & Twitter Metadata -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://33rdtreelabs.tech/{active_page}.html">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{description}">

  <!-- Core Fonts & CDN Engines -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous">
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;600;700&family=Space+Grotesk:wght@300;400;500;600;700&family=Syne:wght@700;800;900&display=swap" rel="stylesheet">
  
  <!-- Fast Snappy Lenis & KaTeX -->
  <script src="https://cdn.jsdelivr.net/npm/@studio-freight/lenis@1.0.42/dist/lenis.min.js"></script>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body, {{delimiters: [{{left: '$$', right: '$$', display: true}}, {{left: '$', right: '$', display: false}}]}});"></script>

  <style>
    :root {{
      --t: #FF2424; /* Primary Laser Crimson */
      --t-glow: rgba(255, 36, 36, 0.45);
      --t-subtle: rgba(255, 36, 36, 0.08);
      --f: #070707; /* Pure Obsidian Background */
      --chalk: #F2F2F5;
      --chalk-dim: #C8C8D2;
      --dim: #8E8E98;
      --slate: #7B7B86;
      --border: #1C1C24;
      --border-accent: rgba(255, 36, 36, 0.35);
      --fd: 'Space Grotesk', -apple-system, BlinkMacSystemFont, sans-serif;
      --fm: 'JetBrains Mono', ui-monospace, monospace;
      --fh: 'Syne', sans-serif;
      --green: #00E676;
    }}

    *, *:before, *:after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    html {{
      -webkit-text-size-adjust: 100%;
      scrollbar-width: none;
      background: var(--f);
      color: var(--chalk);
      font-family: var(--fd);
      overflow-x: clip;
    }}
    html::-webkit-scrollbar {{ display: none; }}
    html.lenis, html.lenis body {{ height: auto; }}
    .lenis.lenis-smooth {{ scroll-behavior: auto !important; }}
    .lenis.lenis-stopped {{ overflow: hidden; }}

    body {{
      margin: 0;
      background: var(--f);
      color: var(--chalk);
      font-family: var(--fd);
      font-size: 15.5px;
      line-height: 1.55;
      overflow-x: clip;
      -webkit-font-smoothing: antialiased;
    }}

    /* TOP-EDGE SCROLL PROGRESS BAR */
    #scroll-progress-line {{
      position: fixed;
      top: 0;
      left: 0;
      width: 0%;
      height: 2px;
      background: var(--t);
      box-shadow: 0 0 10px var(--t), 0 0 20px var(--t-glow);
      z-index: 100000;
      pointer-events: none;
      transition: width 0.03s linear;
      will-change: width;
    }}

    /* RIGHT TELEMETRY RAIL */
    .sbar {{
      position: fixed;
      top: 0;
      right: 0;
      bottom: 0;
      z-index: 1000;
      width: 14px;
      background: rgba(7, 7, 7, 0.85);
      border-left: 1px solid rgba(255, 36, 36, 0.25);
      touch-action: none;
      cursor: pointer;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      align-items: center;
      padding: 60px 0 20px;
    }}
    .sbar__ticks {{
      display: flex;
      flex-direction: column;
      gap: 5px;
      font-family: var(--fm);
      font-size: 8px;
      color: var(--dim);
      user-select: none;
    }}
    .sbar__ticks span {{ line-height: 1; }}
    .sbar__ticks span.active {{ color: var(--t); font-weight: 700; }}
    .sbar__coord {{
      font-family: var(--fm);
      font-size: 9px;
      color: var(--dim);
      writing-mode: vertical-rl;
      letter-spacing: 0.1em;
      user-select: none;
    }}
    .sbar i {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      background: var(--t);
      box-shadow: 0 0 12px rgba(255, 36, 36, 0.85);
      will-change: transform;
      border-radius: 1px;
    }}
    @media (hover: none) {{ .sbar {{ display: none; }} }}

    /* UNIFIED FLOATING PILL NAVBAR */
    .nav-wrapper {{
      position: fixed;
      top: 24px;
      left: 0;
      width: 100%;
      display: flex;
      justify-content: center;
      z-index: 999;
      pointer-events: none;
    }}
    .nav-pill {{
      pointer-events: auto;
      display: flex;
      align-items: center;
      gap: 32px;
      padding: 10px 24px;
      background: rgba(11, 11, 14, 0.92);
      border: 1px solid var(--border);
      border-radius: 100px;
      backdrop-filter: blur(14px);
      box-shadow: 0 12px 32px rgba(0, 0, 0, 0.8), 0 0 20px rgba(255, 36, 36, 0.12);
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .nav-brand {{
      display: flex;
      align-items: center;
      gap: 12px;
      text-decoration: none;
      color: var(--chalk);
    }}
    .nav-logo-box {{
      width: 24px;
      height: 24px;
      display: flex;
      align-items: center;
      justify-content: center;
    }}
    .nav-title {{
      font-family: var(--fh);
      font-weight: 800;
      font-size: 13.5px;
      letter-spacing: 0.12em;
      color: #FFFFFF;
      text-transform: uppercase;
    }}
    .nav-links {{
      display: flex;
      gap: 16px;
    }}
    .nav-link {{
      font-family: var(--fm);
      font-size: 11px;
      font-weight: 500;
      color: var(--dim);
      text-decoration: none;
      letter-spacing: 0.08em;
      transition: color 0.2s, text-shadow 0.2s;
    }}
    .nav-link:hover, .nav-link.active {{
      color: var(--t);
      text-shadow: 0 0 12px rgba(255, 36, 36, 0.6);
    }}
    @media (max-width: 1080px) {{
      .nav-links {{ display: none; }}
    }}

    /* MAIN CONTAINER & EDITORIAL LAYOUT (NO BOXED CARDS) */
    .page-wrap {{
      max-width: 1400px;
      margin: 0 auto;
      padding: 140px clamp(20px, 4vw, 60px) 100px;
    }}

    /* EDITORIAL HEADER / HERO */
    .ed-hero {{
      margin-bottom: 70px;
      position: relative;
    }}
    .ed-kicker {{
      font-family: var(--fm);
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.16em;
      color: var(--t);
      margin-bottom: 16px;
      text-transform: uppercase;
    }}
    .ed-headline {{
      font-family: var(--fh);
      font-weight: 900;
      font-size: clamp(38px, 6vw, 84px);
      letter-spacing: -0.04em;
      text-transform: uppercase;
      line-height: 0.95;
      color: var(--chalk);
      margin-bottom: 24px;
    }}
    .ed-headline .accent {{
      color: var(--t);
      text-shadow: 0 0 40px rgba(255, 36, 36, 0.45);
    }}
    .ed-lead {{
      font-size: clamp(16px, 1.3vw, 19px);
      line-height: 1.6;
      max-width: 880px;
      color: var(--chalk-dim);
      margin-bottom: 40px;
    }}

    /* TELEMETRY STRIP (NO CARD CONTAINERS) */
    .telemetry-strip {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      border-top: 1px solid var(--border);
      border-bottom: 1px solid var(--border);
      margin-bottom: 80px;
    }}
    .telemetry-cell {{
      padding: 24px 28px;
      border-right: 1px solid var(--border);
      display: flex;
      flex-direction: column;
      gap: 8px;
    }}
    .telemetry-cell:last-child {{
      border-right: none;
    }}
    .telemetry-lbl {{
      font-family: var(--fm);
      font-size: 10.5px;
      text-transform: uppercase;
      letter-spacing: 0.12em;
      color: var(--dim);
    }}
    .telemetry-val {{
      font-family: var(--fm);
      font-size: 20px;
      font-weight: 700;
      color: var(--chalk);
      letter-spacing: -0.02em;
    }}
    .telemetry-val.accent {{ color: var(--t); }}
    .telemetry-val.green {{ color: var(--green); }}

    /* OPEN EDITORIAL SECTIONS (NO BOXED CARDS) */
    .ed-section {{
      border-top: 1px solid var(--border);
      padding: 80px 0;
      position: relative;
    }}
    .ed-sec-head {{
      display: grid;
      grid-template-columns: 280px 1fr;
      gap: 40px;
      margin-bottom: 48px;
    }}
    @media (max-width: 860px) {{
      .ed-sec-head {{ grid-template-columns: 1fr; gap: 16px; }}
    }}
    .sec-badge-col {{
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}
    .sec-giant-num {{
      font-family: var(--fh);
      font-size: clamp(48px, 6vw, 72px);
      font-weight: 900;
      line-height: 0.85;
      color: rgba(255, 36, 36, 0.25);
      user-select: none;
    }}
    .sec-kicker {{
      font-family: var(--fm);
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.14em;
      color: var(--t);
      text-transform: uppercase;
    }}
    .sec-title {{
      font-family: var(--fh);
      font-weight: 800;
      font-size: clamp(28px, 3.2vw, 44px);
      letter-spacing: -0.03em;
      text-transform: uppercase;
      line-height: 1.1;
      color: var(--chalk);
      margin-bottom: 16px;
    }}
    .sec-summary {{
      font-size: 16px;
      line-height: 1.65;
      color: var(--chalk-dim);
      max-width: 820px;
    }}

    /* MULTI-COLUMN COMPARISON GRIDS (OPEN BRUTALIST LINES, ZERO CARDS) */
    .ed-grid-4 {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      border-top: 1px solid var(--border);
      border-left: 1px solid var(--border);
      margin: 40px 0;
    }}
    .ed-grid-3 {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      border-top: 1px solid var(--border);
      border-left: 1px solid var(--border);
      margin: 40px 0;
    }}
    .ed-grid-2 {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      border-top: 1px solid var(--border);
      border-left: 1px solid var(--border);
      margin: 40px 0;
    }}
    @media (max-width: 1024px) {{
      .ed-grid-4 {{ grid-template-columns: repeat(2, 1fr); }}
      .ed-grid-3 {{ grid-template-columns: 1fr; }}
    }}
    @media (max-width: 640px) {{
      .ed-grid-4, .ed-grid-2 {{ grid-template-columns: 1fr; }}
    }}
    .ed-grid-cell {{
      border-right: 1px solid var(--border);
      border-bottom: 1px solid var(--border);
      padding: 36px 30px;
      background: transparent;
      transition: background 0.25s ease;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}
    .ed-grid-cell:hover {{
      background: rgba(255, 36, 36, 0.025);
    }}
    .cell-tag {{
      font-family: var(--fm);
      font-size: 10px;
      font-weight: 700;
      letter-spacing: 0.12em;
      color: var(--t);
      margin-bottom: 14px;
      text-transform: uppercase;
    }}
    .cell-title {{
      font-family: var(--fh);
      font-weight: 800;
      font-size: 22px;
      letter-spacing: -0.02em;
      color: #FFFFFF;
      margin-bottom: 14px;
      text-transform: uppercase;
    }}
    .cell-body {{
      font-size: 14px;
      line-height: 1.6;
      color: var(--dim);
      margin-bottom: 24px;
    }}
    .cell-spec-list {{
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 10px;
      font-family: var(--fm);
      font-size: 11.5px;
      border-top: 1px solid rgba(255, 255, 255, 0.06);
      padding-top: 18px;
    }}
    .cell-spec-list li {{
      display: flex;
      justify-content: space-between;
      color: var(--chalk-dim);
    }}
    .cell-spec-list li strong {{
      color: #FFFFFF;
    }}

    /* STARK MONOSPACE TELEMETRY TABLES */
    .ed-table-wrap {{
      width: 100%;
      overflow-x: auto;
      border: 1px solid var(--border);
      margin: 32px 0 48px;
    }}
    .ed-table {{
      width: 100%;
      border-collapse: collapse;
      font-family: var(--fm);
      font-size: 12.5px;
      text-align: left;
    }}
    .ed-table th {{
      background: rgba(255, 36, 36, 0.05);
      color: var(--t);
      padding: 16px 20px;
      border: 1px solid var(--border);
      font-size: 11px;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      font-weight: 700;
    }}
    .ed-table td {{
      padding: 15px 20px;
      border: 1px solid var(--border);
      color: var(--chalk-dim);
    }}
    .ed-table tr:hover td {{
      background: rgba(255, 255, 255, 0.02);
    }}
    .ed-table .highlight {{
      color: #FFFFFF;
      font-weight: 600;
    }}
    .ed-table .accent {{
      color: var(--t);
      font-weight: 700;
    }}
    .ed-table .green {{
      color: var(--green);
      font-weight: 700;
    }}

    /* CODE & COMMAND TERMINAL BLOCKS */
    .ed-code-block {{
      border: 1px solid var(--border);
      background: #030306;
      margin: 28px 0;
      font-family: var(--fm);
    }}
    .ed-code-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 12px 20px;
      background: rgba(255, 255, 255, 0.03);
      border-bottom: 1px solid var(--border);
      font-size: 11px;
      color: var(--dim);
      letter-spacing: 0.08em;
    }}
    .ed-code-content {{
      padding: 22px 24px;
      overflow-x: auto;
      font-size: 13px;
      line-height: 1.65;
      color: #E2E2E8;
    }}
    .cmd-prompt {{ color: var(--t); user-select: none; margin-right: 10px; }}
    .cmd-flag {{ color: #79C0FF; }}
    .cmd-val {{ color: #A5D6FF; }}
    .cmd-comment {{ color: var(--slate); font-style: italic; }}

    /* FORMULA & MATH CALLOUT */
    .math-callout {{
      border-left: 2px solid var(--t);
      background: rgba(255, 36, 36, 0.02);
      padding: 24px 28px;
      margin: 28px 0;
      font-size: 15px;
      line-height: 1.7;
    }}
    .math-callout-title {{
      font-family: var(--fm);
      font-size: 11px;
      font-weight: 700;
      color: var(--t);
      letter-spacing: 0.12em;
      text-transform: uppercase;
      margin-bottom: 10px;
    }}

    /* FOOTER */
    .foot {{
      border-top: 1px solid var(--border);
      background: var(--f);
      padding: 60px 0 40px;
      margin-top: 100px;
    }}
    .foot__marquee {{
      overflow: hidden;
      white-space: nowrap;
      border-bottom: 1px solid var(--border);
      padding-bottom: 24px;
      margin-bottom: 32px;
      font-family: var(--fm);
      font-size: 11px;
      color: var(--dim);
      letter-spacing: 0.15em;
    }}
    .foot__grid {{
      max-width: 1400px;
      margin: 0 auto;
      padding: 0 clamp(20px, 4vw, 60px);
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 20px;
      font-family: var(--fm);
      font-size: 11.5px;
      color: var(--slate);
    }}
    .foot__top {{
      color: var(--t);
      text-decoration: none;
      font-weight: 700;
      letter-spacing: 0.08em;
    }}
    .foot__top:hover {{
      text-decoration: underline;
    }}
  </style>
</head>
<body>

  <!-- TOP-EDGE SCROLL PROGRESS BAR -->
  <div id="scroll-progress-line" aria-hidden="true"></div>

  <!-- RIGHT TELEMETRY RAIL -->
  <div class="sbar" id="telemetry-rail">
    <div class="sbar__ticks">
      <span>00</span>
      <span>25</span>
      <span>50</span>
      <span>75</span>
      <span class="active">99</span>
    </div>
    <div class="sbar__coord">33RDTREELABS // DEPIN // SOLANA</div>
    <div style="font-family:var(--fm); font-size:9px; color:var(--t);" id="telemetry-scroll-pct">00%</div>
    <i id="sbar-thumb" style="height:35px; top:0;"></i>
  </div>

  <!-- UNIFIED FLOATING PILL NAVBAR -->
  <div class="nav-wrapper">
    <nav class="nav-pill">
      <a href="index.html" class="nav-brand">
        <div class="nav-logo-box">
          <svg viewBox="0 0 24 24" width="24" height="24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <ellipse cx="12" cy="4" rx="8.5" ry="2" stroke="#FFFFFF" stroke-width="0.9" fill="none"/>
            <ellipse cx="12" cy="20" rx="8.5" ry="2" stroke="#FFFFFF" stroke-width="0.9" fill="none"/>
            <path d="M 3.5 4 C 8.5 7, 10.5 10, 10.5 12 C 10.5 14, 8.5 17, 3.5 20" stroke="#FFFFFF" stroke-width="1.1" fill="none" stroke-linecap="round"/>
            <path d="M 20.5 4 C 15.5 7, 13.5 10, 13.5 12 C 13.5 14, 15.5 17, 20.5 20" stroke="#FFFFFF" stroke-width="1.1" fill="none" stroke-linecap="round"/>
            <line x1="12" y1="2" x2="12" y2="22" stroke="#FF292C" stroke-width="1.1" stroke-dasharray="1.5 1.5"/>
            <circle cx="12" cy="12" r="1.8" fill="#FF292C"/>
          </svg>
        </div>
        <span class="nav-title" data-glitch>33RD TREE LABS</span>
      </a>

      <div class="nav-links">
        <a href="index.html" class="nav-link {'active' if active_page == 'index' else ''}" data-glitch>[ OVERVIEW ]</a>
        <a href="protocol.html" class="nav-link {'active' if active_page == 'protocol' else ''}" data-glitch>[ PROTOCOL ]</a>
        <a href="simulator.html" class="nav-link {'active' if active_page == 'simulator' else ''}" data-glitch>[ SIMULATOR ]</a>
        <a href="yield.html" class="nav-link {'active' if active_page == 'yield' else ''}" data-glitch>[ YIELD ]</a>
        <a href="nodes.html" class="nav-link {'active' if active_page == 'nodes' else ''}" data-glitch>[ NODES ]</a>
        <a href="tokenomics.html" class="nav-link {'active' if active_page == 'tokenomics' else ''}" data-glitch>[ TOKENOMICS ]</a>
        <a href="research.html" class="nav-link {'active' if active_page == 'research' else ''}" data-glitch>[ RESEARCH ]</a>
        <a href="whitepaper.html" class="nav-link {'active' if active_page == 'whitepaper' else ''}" data-glitch>[ WHITEPAPER ]</a>
      </div>
    </nav>
  </div>
"""

def get_shared_foot():
    return """
  <footer class="foot">
    <div class="foot__marquee">
      0/1 33RD TREE LABS // THE SINGULARITY PROTOCOL // SOLANA INCINERATOR VERIFIED // ZERO-KNOWLEDGE PROOF ANCHOR // 0/1 33RD TREE LABS // THE SINGULARITY PROTOCOL // SOLANA INCINERATOR VERIFIED //
    </div>
    <div class="foot__grid">
      <div>&copy; 2026 33RD TREE LABS. THE SINGULARITY PROTOCOL. ALL RIGHTS RESERVED.</div>
      <div>OFFICIAL DOMAIN: 33RDTREELABS.TECH &bull; SOLANA INCINERATOR LP LOCKED</div>
      <a href="#top" class="foot__top" id="back-to-top">START OVER &uarr;</a>
    </div>
  </footer>

  <!-- FAST SNAPPY LENIS SCRIPT & TELEMETRY PROGRESS -->
  <script>
    const lenis = new Lenis({
      lerp: 0.14,
      wheelMultiplier: 1.25,
      smoothWheel: true,
      smoothTouch: false
    });

    function raf(time) {
      lenis.raf(time);
      requestAnimationFrame(raf);
    }
    requestAnimationFrame(raf);

    // Scroll progress & telemetry rail updates
    lenis.on('scroll', (e) => {
      const scrollTotal = document.documentElement.scrollHeight - window.innerHeight;
      const progress = scrollTotal > 0 ? (e.scroll / scrollTotal) * 100 : 0;
      
      const bar = document.getElementById('scroll-progress-line');
      if (bar) bar.style.width = progress + '%';

      const pct = document.getElementById('telemetry-scroll-pct');
      if (pct) pct.innerText = Math.round(progress).toString().padStart(2, '0') + '%';

      const thumb = document.getElementById('sbar-thumb');
      if (thumb) {
        const thumbMax = window.innerHeight - 80;
        thumb.style.transform = `translateY(${(progress / 100) * thumbMax}px)`;
      }
    });

    document.getElementById('back-to-top')?.addEventListener('click', (e) => {
      e.preventDefault();
      lenis.scrollTo(0, { duration: 0.8 });
    });

    // GLITCH SCRAMBLE EFFECT
    const GLYPHS = "01010101_//<>[]!#$*+=-";
    class GlitchScramble {
      constructor(el) {
        this.el = el;
        this.original = el.innerText;
        this.isGlitching = false;
        this.animId = null;
      }
      scramble(speed = 4.0) {
        if (this.isGlitching) return;
        this.isGlitching = true;
        const target = this.original;
        const len = target.length;
        const start = performance.now();
        const duration = Math.min(600, Math.max(250, len * 20));

        const tick = (now) => {
          const elapsed = now - start;
          const progress = Math.min(1, elapsed / duration);
          const revealedCount = Math.floor(progress * len);
          let result = '';
          for (let i = 0; i < len; i++) {
            const ch = target[i];
            if (ch === ' ' || ch === '\\n' || ch === '\\t') {
              result += ch;
            } else if (i < revealedCount) {
              result += ch;
            } else {
              result += GLYPHS[Math.floor(Math.random() * GLYPHS.length)];
            }
          }
          this.el.innerText = result;
          if (progress < 1) {
            this.animId = requestAnimationFrame(tick);
          } else {
            this.el.innerText = target;
            this.isGlitching = false;
          }
        };
        this.animId = requestAnimationFrame(tick);
      }
    }
    document.querySelectorAll('[data-glitch]').forEach(el => {
      const g = new GlitchScramble(el);
      el.addEventListener('mouseenter', () => g.scramble(3.5));
    });
  </script>
</body>
</html>
"""

print("Writing generator script core...")
