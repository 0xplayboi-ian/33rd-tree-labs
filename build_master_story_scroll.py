import os

# Python script to generate the complete, pristine index.html for 33rd Tree Labs
# Strict adherence to all user rules & requirements:
# 1. NO TOP MENU BAR / HUD.
# 2. Compelling, deep technical story explaining 33rd Tree Labs.
# 3. Longer than booleansequence.
# 4. Sideways scrolling section (pinned horizontal scroll track).
# 5. Exact booleansequence aesthetic:
#    - Living Generative Matrix / Cellular Automaton Field with cursor repulsion
#    - Pinned Hero kinetic split typography
#    - Chapter 01: The Thesis / Concept with brutalist badges & dual-column
#    - Chapter 02: Pinned Altitude Descent (1208m -> 8m)
#    - Chapter 03: Pinned 4-Instruction Stepper with animated bars & live canvas
#    - Chapter 04: Pinned Horizontal Rail for hardware clusters & tokenomics
#    - Chapter 05: Pinned Expanding Schematic Film with Tensor Arbor wireframe
#    - Chapter 06: Interactive Consensus & Cellular Playground with sliders & export
#    - Chapter 07: Inverted Colorway Finale & Technical Specification Table
#    - Lenis smooth scrolling (lerp: 0.085)
#    - Right hairline scroll rail (.sbar) tracking 000 -> 999 with thumb & ticks
#    - Bottom-right floating interactive minimap preview
#    - ZERO EMOJIS anywhere
#    - NO MADE-UP operational telemetry numbers
#    - Obel Mono fonts & official logo mark

html_template = """<!doctype html>
<html lang="en" class="lenis" style="--t: #FF292C; --f: #070707;">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>33RD TREE LABS // The Singularity Protocol &bull; 33rdtreelabs.tech</title>
  <meta name="description" content="A Byzantine-Resilient Verifiable DePIN Compute Fabric on Solana. Hierarchical Tensor Arbor coordination, zero-knowledge neural evaluations, and deterministic consensus at scale.">
  <meta name="theme-color" content="#070707">

  <!-- OpenGraph & Twitter Metadata -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://33rdtreelabs.tech/">
  <meta property="og:title" content="33RD TREE LABS // The Singularity Protocol">
  <meta property="og:description" content="Byzantine-Resilient Verifiable DePIN Compute Fabric on Solana. Pairing cryptographic consensus with zero-knowledge neural evaluations.">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="33RD TREE LABS // 33rdtreelabs.tech">
  <meta name="twitter:description" content="Decentralized verifiable GPU compute orchestration anchored on Solana.">

  <!-- Core Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous">
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@0,300;0,400;0,500;0,700;1,400&family=Space+Grotesk:wght@300;400;500;600;700;800&family=Syne:wght@700;800;900&display=swap" rel="stylesheet">
  
  <!-- Animation Engines -->
  <script src="https://cdn.jsdelivr.net/npm/@studio-freight/lenis@1.0.42/dist/lenis.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>

  <style>
    /* BRAND TYPOGRAPHY: OBEL MONO + FALLBACKS */
    @font-face {
      font-family: 'Obel Mono';
      src: url('assets/fonts/ObelMono.ttf') format('truetype');
      font-weight: 400;
      font-style: normal;
      font-display: swap;
    }
    @font-face {
      font-family: 'Obel Mono';
      src: url('assets/fonts/ObelMono-Italic.ttf') format('truetype');
      font-weight: 400;
      font-style: italic;
      font-display: swap;
    }
    @font-face {
      font-family: 'Obel Mono Masked';
      src: url('assets/fonts/ObelMonoMasked.ttf') format('truetype');
      font-weight: 400;
      font-style: normal;
      font-display: swap;
    }

    :root {
      --t: #FF292C; /* Crimson Accent */
      --t-glow: rgba(255, 36, 36, 0.45);
      --f: #070707; /* Pure Obsidian */
      --chalk: #F2F2F5;
      --dim: #8E8E98;
      --border: #1C1C24;
      --border-accent: rgba(255, 36, 36, 0.35);
      --card-bg: rgba(11, 11, 14, 0.92);
      --fd: 'Space Grotesk', -apple-system, BlinkMacSystemFont, sans-serif;
      --fm: 'Obel Mono', 'JetBrains Mono', ui-monospace, monospace;
      --fh: 'Obel Mono Masked', 'Syne', -apple-system, sans-serif;
      --pad: clamp(20px, 3.5vw, 60px);
    }

    *, *:before, *:after { box-sizing: border-box; margin: 0; padding: 0; }
    html {
      -webkit-text-size-adjust: 100%;
      scrollbar-width: none;
      background: var(--f);
      color: var(--chalk);
      font-family: var(--fd);
      overflow-x: clip;
    }
    html::-webkit-scrollbar { display: none; }
    html.lenis, html.lenis body { height: auto; }
    .lenis.lenis-smooth { scroll-behavior: auto !important; }
    .lenis.lenis-stopped { overflow: hidden; }

    body {
      margin: 0;
      background: var(--f);
      color: var(--chalk);
      font-family: var(--fd);
      font-size: 16px;
      line-height: 1.5;
      overflow-x: clip;
      -webkit-font-smoothing: antialiased;
      transition: background 0.7s cubic-bezier(0.16, 1, 0.3, 1), color 0.7s cubic-bezier(0.16, 1, 0.3, 1);
    }

    /* RIGHT TELEMETRY RAIL & SCROLLBAR */
    .sbar {
      position: fixed;
      top: 0;
      right: 0;
      bottom: 0;
      z-index: 1000;
      width: 14px;
      background: rgba(7, 7, 7, 0.90);
      border-left: 1px solid rgba(255, 36, 36, 0.22);
      touch-action: none;
      cursor: pointer;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      align-items: center;
      padding: 30px 0 20px;
      user-select: none;
    }
    .sbar__ticks {
      display: flex;
      flex-direction: column;
      gap: 7px;
      font-family: var(--fm);
      font-size: 8px;
      color: #3A3A48;
      pointer-events: none;
    }
    .sbar__ticks span { line-height: 1; transition: color 0.2s ease; }
    .sbar__ticks span.active { color: var(--t); font-weight: 700; }
    .sbar__coord {
      font-family: var(--fm);
      font-size: 9px;
      color: var(--dim);
      writing-mode: vertical-rl;
      letter-spacing: 0.12em;
      pointer-events: none;
    }
    .sbar i {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      background: var(--t);
      box-shadow: 0 0 14px rgba(255, 36, 36, 0.9);
      will-change: transform;
      border-radius: 1px;
    }
    .sbar:hover i, .sbar.is-drag i {
      background: #FF5555;
      box-shadow: 0 0 20px rgba(255, 36, 36, 1);
    }
    @media (hover: none) { .sbar { display: none; } }

    /* FLOATING BOTTOM-RIGHT MINIMAP */
    .minimap-hud {
      position: fixed;
      bottom: 24px;
      right: 28px;
      z-index: 990;
      width: 130px;
      height: 80px;
      background: rgba(4, 4, 6, 0.88);
      border: 1px solid var(--border);
      border-radius: 4px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      box-shadow: 0 14px 34px rgba(0, 0, 0, 0.85);
      backdrop-filter: blur(12px);
      user-select: none;
      cursor: pointer;
      transition: border-color 0.25s ease;
    }
    .minimap-hud:hover {
      border-color: var(--t);
    }
    .minimap-header {
      font-family: var(--fm);
      font-size: 8px;
      padding: 4px 6px;
      background: rgba(255, 255, 255, 0.04);
      display: flex;
      justify-content: space-between;
      color: var(--dim);
      border-bottom: 1px solid var(--border);
    }
    .minimap-header span:last-child { color: var(--t); font-weight: 700; }
    .minimap-preview {
      flex: 1;
      position: relative;
      background: #020204;
    }
    .minimap-sections {
      position: absolute;
      inset: 0;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      padding: 3px;
      pointer-events: none;
    }
    .minimap-dot {
      height: 3px;
      width: 100%;
      background: rgba(255, 255, 255, 0.08);
      border-radius: 1px;
    }
    .minimap-viewport-indicator {
      position: absolute;
      left: 0;
      right: 0;
      top: 0;
      height: 14px;
      background: rgba(255, 36, 36, 0.2);
      border-top: 1px solid var(--t);
      border-bottom: 1px solid var(--t);
      pointer-events: none;
      will-change: transform;
    }

    /* CHAPTER HEADINGS & BRUTALIST BADGES */
    .kicker {
      font-family: var(--fm);
      font-size: 11px;
      font-weight: 700;
      color: var(--t);
      letter-spacing: 0.18em;
      text-transform: uppercase;
      margin-bottom: 20px;
      display: inline-flex;
      align-items: center;
      gap: 10px;
    }
    .kicker::before {
      content: '';
      display: inline-block;
      width: 8px;
      height: 8px;
      background: var(--t);
      border-radius: 50%;
      box-shadow: 0 0 8px var(--t);
    }
    .badge-fill {
      background: var(--chalk);
      color: #070707;
      padding: 2px 14px;
      display: inline-block;
      border-radius: 2px;
      font-weight: 800;
    }
    .badge-box {
      border: 1.5px solid var(--chalk);
      padding: 1px 14px;
      display: inline-block;
      border-radius: 2px;
      font-weight: 800;
    }
    .badge-crimson {
      background: var(--t);
      color: #FFFFFF;
      padding: 2px 14px;
      display: inline-block;
      border-radius: 2px;
      font-weight: 800;
      box-shadow: 0 0 16px rgba(255, 36, 36, 0.5);
    }

    /* WORD READING ILLUMINATION */
    [data-words] .word {
      display: inline-block;
      margin-right: 0.28em;
      transition: opacity 0.12s ease, color 0.12s ease;
      will-change: opacity;
    }

    /* =====================================================================
       CHAPTER 00: PINNED HERO WITH MASSIVE KINETIC SPLIT TYPOGRAPHY
       ===================================================================== */
    .hero {
      position: relative;
      height: 100vh;
      min-height: 640px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      padding: clamp(36px, 6vh, 64px) var(--pad) clamp(28px, 4vh, 48px);
      overflow: hidden;
      box-sizing: border-box;
      background: var(--f);
    }
    .hero__field-canvas {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      z-index: 1;
      opacity: 0.84;
    }
    .hero__content {
      position: relative;
      z-index: 2;
      display: flex;
      flex-direction: column;
      justify-content: center;
      flex: 1;
      width: 100%;
      max-width: 1440px;
      margin: 0 auto;
      pointer-events: none;
    }
    .hero__top-meta {
      display: flex;
      justify-content: space-between;
      align-items: center;
      width: 100%;
      max-width: 1440px;
      margin: 0 auto;
      position: relative;
      z-index: 2;
      font-family: var(--fm);
      font-size: 11px;
      color: var(--dim);
      letter-spacing: 0.12em;
    }
    .hero__protocol-tag {
      color: var(--t);
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .hero__protocol-tag::before {
      content: '';
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: var(--t);
      box-shadow: 0 0 10px var(--t);
      animation: pulse-dot 2s infinite;
    }
    @keyframes pulse-dot { 0%, 100% { opacity: 1; transform: scale(1); } 50% { opacity: 0.4; transform: scale(0.85); } }

    .hero__split {
      display: flex;
      flex-direction: column;
      line-height: 0.88;
      margin: 24px 0 32px;
      user-select: none;
    }
    .hero__line {
      font-family: var(--fh);
      font-weight: 900;
      font-size: clamp(52px, 12vw, 175px);
      letter-spacing: -0.045em;
      text-transform: uppercase;
      white-space: nowrap;
      will-change: transform;
      color: var(--chalk);
    }
    .hero__line.red-accent {
      color: var(--t);
      text-shadow: 0 0 45px rgba(255, 36, 36, 0.55);
    }
    .hero__aside {
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      gap: 36px;
      width: 100%;
      max-width: 1440px;
      margin: 0 auto;
      position: relative;
      z-index: 2;
      pointer-events: auto;
    }
    .hero__scroll-indicator {
      display: inline-flex;
      align-items: center;
      gap: 14px;
      background: rgba(11, 11, 15, 0.92);
      border: 1px solid rgba(255, 36, 36, 0.35);
      padding: 10px 18px;
      border-radius: 4px;
      backdrop-filter: blur(14px);
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.6);
      transition: border-color 0.25s ease;
    }
    .hero__scroll-indicator:hover {
      border-color: var(--t);
    }
    .hero__scroll-pulse {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: var(--t);
      box-shadow: 0 0 12px var(--t);
      animation: pulseGlow 1.8s infinite ease-in-out;
    }
    @keyframes pulseGlow {
      0%, 100% { opacity: 0.4; transform: scale(0.9); }
      50% { opacity: 1; transform: scale(1.15); box-shadow: 0 0 16px var(--t); }
    }
    .hero__scroll-text-group {
      display: flex;
      flex-direction: column;
      gap: 2px;
    }
    .hero__scroll-action {
      font-family: var(--fm);
      font-size: 11px;
      font-weight: 700;
      color: var(--chalk);
      letter-spacing: 0.16em;
    }
    .hero__scroll-sub {
      font-family: var(--fm);
      font-size: 9px;
      color: var(--dim);
      letter-spacing: 0.12em;
    }
    .hero__foot-badges {
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      font-family: var(--fm);
      font-size: 11px;
      color: var(--dim);
    }
    .hero__badge-tag {
      background: rgba(11, 11, 14, 0.88);
      border: 1px solid var(--border);
      padding: 7px 14px;
      border-radius: 4px;
      backdrop-filter: blur(10px);
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .hero__badge-tag strong { color: var(--chalk); font-weight: 700; }

    /* =====================================================================
       CHAPTER 01: THE THESIS & CONCEPT SECTION (BRUTALIST STROKE & FILL)
       ===================================================================== */
    .concept {
      padding: clamp(100px, 16vh, 180px) var(--pad);
      background: var(--f);
      position: relative;
      z-index: 3;
      border-top: 1px solid var(--border);
    }
    .concept__inner {
      max-width: 1320px;
      margin: 0 auto;
    }
    .concept__headline {
      font-family: var(--fh);
      font-size: clamp(36px, 5.8vw, 88px);
      font-weight: 900;
      line-height: 1.04;
      letter-spacing: -0.035em;
      text-transform: uppercase;
      margin-bottom: 40px;
    }
    /* ARCHITECTURAL MANIFESTO CARD (HIGH-CONTRAST DEDICATED GLASS PLATE) */
    .manifesto-card {
      background: linear-gradient(145deg, rgba(16, 16, 24, 0.96) 0%, rgba(8, 8, 12, 0.98) 100%);
      border: 1px solid rgba(255, 36, 36, 0.35);
      border-left: 4px solid var(--t);
      border-radius: 6px;
      padding: clamp(32px, 4vw, 56px);
      margin: 0 0 clamp(48px, 6vh, 72px);
      position: relative;
      box-shadow: 0 24px 60px rgba(0, 0, 0, 0.85), inset 0 1px 0 rgba(255, 255, 255, 0.06);
      overflow: hidden;
    }
    .manifesto-card::before {
      content: '';
      position: absolute;
      top: 0;
      right: 0;
      width: 280px;
      height: 280px;
      background: radial-gradient(circle at top right, rgba(255, 36, 36, 0.10), transparent 70%);
      pointer-events: none;
    }
    .manifesto-card__header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 14px;
      padding-bottom: 20px;
      margin-bottom: 26px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      font-family: var(--fm);
      font-size: 11px;
      letter-spacing: 0.14em;
    }
    .manifesto-card__tag {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      color: var(--t);
      font-weight: 700;
    }
    .manifesto-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: var(--t);
      box-shadow: 0 0 10px var(--t);
      animation: pulseGlow 2s infinite ease-in-out;
    }
    .manifesto-card__meta {
      color: var(--dim);
      font-family: var(--fm);
    }
    .manifesto-card__body {
      font-family: var(--fd);
      font-size: clamp(20px, 2.2vw, 32px);
      line-height: 1.48;
      color: #FFFFFF;
      font-weight: 400;
      letter-spacing: -0.015em;
      max-width: 1240px;
      margin-bottom: 32px;
    }
    .manifesto-card__body strong {
      color: #FFFFFF;
      font-weight: 700;
      text-decoration: underline;
      text-decoration-color: rgba(255, 36, 36, 0.65);
      text-underline-offset: 6px;
    }
    .manifesto-card__footer {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 20px;
      padding-top: 24px;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
    }
    .manifesto-metric {
      display: flex;
      flex-direction: column;
      gap: 4px;
      font-family: var(--fm);
    }
    .manifesto-metric__label {
      font-size: 10px;
      color: var(--dim);
      letter-spacing: 0.12em;
    }
    .manifesto-metric__val {
      font-size: 13px;
      font-weight: 700;
      color: var(--chalk);
    }
    .concept__cols {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: clamp(36px, 5.5vw, 76px);
      font-family: var(--fm);
      font-size: 14.5px;
      line-height: 1.75;
      color: var(--dim);
      border-top: 1px solid var(--border);
      padding-top: 40px;
    }
    .concept__col h3 {
      font-family: var(--fh);
      font-size: 20px;
      font-weight: 800;
      color: var(--chalk);
      letter-spacing: -0.01em;
      text-transform: uppercase;
      margin-bottom: 16px;
    }
    .concept__col p {
      margin-bottom: 20px;
    }
    .concept__callout {
      background: rgba(17, 17, 24, 0.6);
      border-left: 2px solid var(--t);
      padding: 14px 18px;
      border-radius: 0 4px 4px 0;
      color: var(--chalk);
      font-size: 13.5px;
    }

    /* =====================================================================
       CHAPTER 02: PINNED ALTITUDE DESCENT (1208 M -> 0008 M)
       ===================================================================== */
    .above {
      position: relative;
      height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      background: #040406;
      z-index: 4;
      overflow: hidden;
    }
    .above__canvas-bg {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      z-index: 1;
      opacity: 0.55;
    }
    .above__pin {
      position: relative;
      z-index: 2;
      width: 100%;
      max-width: 1320px;
      margin: 0 auto;
      padding: 0 var(--pad);
      display: grid;
      grid-template-columns: 1fr 1.15fr;
      gap: clamp(36px, 6vw, 80px);
      align-items: center;
    }
    .above__metric-box {
      background: var(--card-bg);
      border: 1px solid var(--border);
      padding: clamp(28px, 4vw, 52px);
      border-radius: 8px;
      box-shadow: 0 25px 70px rgba(0, 0, 0, 0.85), 0 0 35px rgba(255, 36, 36, 0.12);
      position: relative;
      overflow: hidden;
      backdrop-filter: blur(14px);
    }
    .above__metric-box::before {
      content: '';
      position: absolute;
      top: 0; left: 0; width: 4px; height: 100%;
      background: var(--t);
    }
    .above__counter-wrap {
      display: flex;
      align-items: baseline;
      gap: 12px;
      margin-bottom: 6px;
    }
    .above__counter {
      font-family: var(--fh);
      font-size: clamp(60px, 9.5vw, 120px);
      font-weight: 900;
      line-height: 0.9;
      color: var(--t);
      letter-spacing: -0.04em;
    }
    .above__unit {
      font-family: var(--fm);
      font-size: clamp(16px, 2.5vw, 32px);
      font-weight: 700;
      color: var(--dim);
    }
    .above__label {
      font-family: var(--fm);
      font-size: 11px;
      color: var(--dim);
      letter-spacing: 0.14em;
      text-transform: uppercase;
      margin-bottom: 24px;
    }
    .above__copy h2 {
      font-family: var(--fh);
      font-size: clamp(34px, 4.5vw, 62px);
      font-weight: 800;
      line-height: 1.02;
      text-transform: uppercase;
      letter-spacing: -0.03em;
      margin-bottom: 24px;
    }
    .above__copy p {
      font-size: 16.5px;
      line-height: 1.65;
      color: var(--dim);
      margin-bottom: 28px;
    }
    .above__telemetry-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 16px;
      padding-top: 20px;
      border-top: 1px solid var(--border);
      font-family: var(--fm);
    }
    .above__telemetry-item span:first-child {
      display: block;
      font-size: 10px;
      color: var(--dim);
      letter-spacing: 0.1em;
      text-transform: uppercase;
      margin-bottom: 4px;
    }
    .above__telemetry-item span:last-child {
      font-size: 16px;
      font-weight: 700;
      color: var(--chalk);
    }

    /* =====================================================================
       CHAPTER 03: PINNED 4-INSTRUCTION BEHAVIOUR STEPPER
       ===================================================================== */
    .rule {
      position: relative;
      height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      background: #08080C;
      z-index: 5;
      overflow: hidden;
      border-top: 1px solid var(--border);
    }
    .rule__pin {
      width: 100%;
      max-width: 1320px;
      margin: 0 auto;
      padding: 0 var(--pad);
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: clamp(36px, 5.5vw, 70px);
      align-items: center;
    }
    .rule__steps {
      display: flex;
      flex-direction: column;
      gap: 16px;
    }
    .step {
      background: rgba(16, 16, 22, 0.7);
      border: 1px solid var(--border);
      padding: 20px 24px;
      border-radius: 6px;
      transition: border-color 0.3s ease, background 0.3s ease, transform 0.3s ease;
      position: relative;
    }
    .step.is-active {
      border-color: var(--t);
      background: rgba(255, 36, 36, 0.08);
      transform: translateX(8px);
    }
    .step.is-done {
      border-color: rgba(255, 36, 36, 0.35);
      opacity: 0.65;
    }
    .step__header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 8px;
    }
    .step__nr {
      font-family: var(--fm);
      font-size: 11px;
      font-weight: 700;
      color: var(--t);
    }
    .step__verb {
      font-family: var(--fm);
      font-size: 12.5px;
      font-weight: 700;
      letter-spacing: 0.1em;
      color: var(--chalk);
    }
    .step__desc {
      font-size: 14px;
      color: var(--dim);
      line-height: 1.5;
    }
    .step__bar {
      height: 2px;
      width: 100%;
      background: rgba(255, 255, 255, 0.08);
      margin-top: 14px;
      overflow: hidden;
      border-radius: 1px;
    }
    .step__bar i {
      display: block;
      height: 100%;
      width: 100%;
      background: var(--t);
      transform-origin: left center;
      transform: scaleX(0);
      will-change: transform;
    }
    .rule__interactive-preview {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 30px;
      box-shadow: 0 25px 70px rgba(0, 0, 0, 0.8);
      backdrop-filter: blur(14px);
    }
    .rule__canvas-box {
      width: 100%;
      height: 300px;
      background: #000000;
      border: 1px solid var(--border);
      border-radius: 6px;
      position: relative;
      overflow: hidden;
      margin-bottom: 20px;
    }
    #rule-canvas { width: 100%; height: 100%; }
    .rule__preview-foot {
      font-family: var(--fm);
      font-size: 11px;
      color: var(--dim);
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-top: 1px solid var(--border);
      padding-top: 14px;
    }

    /* =====================================================================
       CHAPTER 04: PINNED HORIZONTAL RAIL (SIDEWAYS SCROLLING SECTION)
       ===================================================================== */
    .pairs-section {
      position: relative;
      height: 100vh;
      overflow: hidden;
      background: #030305;
      z-index: 6;
      border-top: 1px solid var(--border);
    }
    .pairs-track-wrap {
      height: 100%;
      display: flex;
      align-items: center;
      padding-left: clamp(24px, 8vw, 140px);
      padding-right: 140px;
    }
    .pairs-track {
      display: flex;
      gap: clamp(28px, 4vw, 56px);
      align-items: center;
      will-change: transform;
    }
    .pair-intro {
      flex: 0 0 clamp(300px, 30vw, 420px);
    }
    .pair-intro h2 {
      font-family: var(--fh);
      font-size: clamp(38px, 4.8vw, 68px);
      font-weight: 900;
      line-height: 0.98;
      text-transform: uppercase;
      letter-spacing: -0.03em;
      margin-bottom: 20px;
    }
    .pair-intro p {
      font-size: 15px;
      color: var(--dim);
      line-height: 1.65;
    }
    .pair-card {
      flex: 0 0 clamp(320px, 34vw, 460px);
      background: var(--card-bg);
      border: 1px solid var(--border);
      padding: clamp(26px, 3.2vw, 40px);
      border-radius: 8px;
      box-shadow: 0 25px 60px rgba(0, 0, 0, 0.75);
      will-change: transform, rotate;
      transition: border-color 0.3s ease, box-shadow 0.3s ease;
      position: relative;
      overflow: hidden;
    }
    .pair-card:hover {
      border-color: var(--t);
      box-shadow: 0 25px 70px rgba(255, 36, 36, 0.15);
    }
    .pair-card::after {
      content: '';
      position: absolute;
      top: 0; left: 0; right: 0; height: 2px;
      background: linear-gradient(90deg, transparent, var(--t), transparent);
      opacity: 0;
      transition: opacity 0.3s ease;
    }
    .pair-card:hover::after { opacity: 1; }
    .pair-card__tag {
      font-family: var(--fm);
      font-size: 11px;
      color: var(--t);
      letter-spacing: 0.14em;
      margin-bottom: 14px;
      text-transform: uppercase;
      font-weight: 700;
    }
    .pair-card__title {
      font-family: var(--fh);
      font-size: 24px;
      font-weight: 800;
      margin-bottom: 12px;
      text-transform: uppercase;
      letter-spacing: -0.02em;
    }
    .pair-card__desc {
      font-size: 14px;
      color: var(--dim);
      line-height: 1.6;
      margin-bottom: 26px;
    }
    .pair-card__stat-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 16px;
      border-top: 1px solid var(--border);
      padding-top: 18px;
    }
    .pair-card__stat-val {
      font-family: var(--fm);
      font-size: 16px;
      font-weight: 700;
      color: var(--chalk);
    }
    .pair-card__stat-lbl {
      font-family: var(--fm);
      font-size: 9.5px;
      color: var(--dim);
      letter-spacing: 0.12em;
      text-transform: uppercase;
      margin-top: 2px;
    }

    /* =====================================================================
       CHAPTER 05: MATHEMATICAL INVARIANTS & FORMAL VERIFICATION
       ===================================================================== */
    .invariants {
      padding: clamp(90px, 14vh, 160px) var(--pad);
      background: #040407;
      position: relative;
      z-index: 5;
      border-top: 1px solid var(--border);
    }
    .invariants__inner {
      max-width: 1320px;
      margin: 0 auto;
    }
    .invariants__headline {
      font-family: var(--fh);
      font-size: clamp(34px, 5.2vw, 80px);
      font-weight: 900;
      line-height: 1.05;
      letter-spacing: -0.035em;
      text-transform: uppercase;
      margin-bottom: 24px;
    }
    .invariants__lead {
      font-family: var(--fm);
      font-size: 15px;
      line-height: 1.7;
      color: var(--dim);
      max-width: 900px;
      margin-bottom: 48px;
    }
    .invariants__pillars {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 20px;
      margin-bottom: 48px;
    }
    .invariant-card {
      background: #09090E;
      border: 1px solid var(--border);
      padding: 28px 24px;
      border-radius: 4px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      min-height: 280px;
      transition: border-color 0.25s ease, transform 0.25s ease;
    }
    .invariant-card:hover {
      border-color: var(--t);
      transform: translateY(-2px);
    }
    .invariant-card__tag {
      font-family: var(--fm);
      font-size: 10px;
      font-weight: 700;
      letter-spacing: 0.14em;
      color: var(--t);
      margin-bottom: 12px;
      text-transform: uppercase;
    }
    .invariant-card__title {
      font-family: var(--fh);
      font-size: 19px;
      font-weight: 800;
      text-transform: uppercase;
      color: var(--chalk);
      margin-bottom: 12px;
      line-height: 1.25;
    }
    .invariant-card__formula {
      font-family: var(--fm);
      font-size: 11.5px;
      font-weight: 700;
      color: #FFFFFF;
      background: rgba(255, 36, 36, 0.12);
      border-left: 2px solid var(--t);
      padding: 8px 12px;
      margin-bottom: 14px;
      letter-spacing: 0.04em;
    }
    .invariant-card__desc {
      font-family: var(--fm);
      font-size: 13px;
      line-height: 1.6;
      color: var(--dim);
    }
    .invariant-card__foot {
      border-top: 1px solid rgba(255, 255, 255, 0.06);
      padding-top: 14px;
      margin-top: 20px;
      font-family: var(--fm);
      font-size: 10.5px;
      font-weight: 700;
      letter-spacing: 0.08em;
      color: var(--dim);
    }
    .slashing-table-wrap {
      border: 1px solid var(--border);
      background: #08080C;
      border-radius: 4px;
      overflow: hidden;
      margin-top: 32px;
    }
    .slashing-table-header {
      background: #0E0E14;
      padding: 14px 20px;
      font-family: var(--fm);
      font-size: 11px;
      font-weight: 700;
      color: var(--dim);
      display: flex;
      justify-content: space-between;
      letter-spacing: 0.1em;
      border-bottom: 1px solid var(--border);
    }
    .slashing-table-grid {
      display: grid;
    }
    .slashing-row {
      display: grid;
      grid-template-columns: 2.2fr 1fr 1.2fr 1.8fr 2.8fr;
      padding: 14px 20px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.05);
      font-family: var(--fm);
      font-size: 12.5px;
      align-items: center;
      gap: 12px;
    }
    .slashing-row:last-child {
      border-bottom: none;
    }
    .slashing-row.header {
      background: rgba(255, 255, 255, 0.02);
      font-size: 11px;
      font-weight: 700;
      color: var(--chalk);
      letter-spacing: 0.08em;
      text-transform: uppercase;
    }
    .slashing-val-crimson {
      color: var(--t);
      font-weight: 700;
    }
    @media (max-width: 960px) {
      .invariants__pillars { grid-template-columns: 1fr; }
      .slashing-row { grid-template-columns: 1fr; gap: 6px; }
      .slashing-row.header { display: none; }
    }

    /* =====================================================================
       CHAPTER 06: PINNED EXPANDING SCHEMATIC FILM (TENSOR ARBOR WIREFRAME)
       ===================================================================== */
    .film-section {
      position: relative;
      height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      background: #000000;
      z-index: 7;
      overflow: hidden;
      border-top: 1px solid var(--border);
    }
    .film-clip {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      clip-path: inset(32% 38% 32% 38%);
      will-change: clip-path;
      display: flex;
      align-items: center;
      justify-content: center;
      background: #040407;
      border: 1px solid var(--border);
    }
    #film-canvas { width: 100%; height: 100%; }
    .film-overlay-text {
      position: absolute;
      bottom: clamp(30px, 6vh, 60px);
      left: clamp(24px, 5vw, 64px);
      z-index: 2;
      font-family: var(--fm);
      font-size: 12px;
      color: var(--chalk);
      background: rgba(0, 0, 0, 0.88);
      padding: 10px 18px;
      border-radius: 4px;
      border: 1px solid rgba(255, 36, 36, 0.35);
      backdrop-filter: blur(10px);
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .film-overlay-text .dot {
      width: 8px;
      height: 8px;
      background: var(--t);
      border-radius: 50%;
      box-shadow: 0 0 10px var(--t);
    }

    /* =====================================================================
       CHAPTER 07: INTERACTIVE CONSENSUS & CELLULAR PLAYGROUND
       ===================================================================== */
    .play {
      padding: clamp(90px, 14vh, 160px) var(--pad);
      background: var(--f);
      z-index: 8;
      position: relative;
      border-top: 1px solid var(--border);
    }
    .play__inner {
      max-width: 1320px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: 1.15fr 0.85fr;
      gap: clamp(36px, 5vw, 64px);
      align-items: center;
    }
    .play__canvas-box {
      width: 100%;
      height: 420px;
      background: #000000;
      border: 1px solid var(--border);
      border-radius: 8px;
      overflow: hidden;
      position: relative;
      box-shadow: 0 25px 70px rgba(0, 0, 0, 0.85), 0 0 35px rgba(255, 36, 36, 0.2);
    }
    #playground-canvas { width: 100%; height: 100%; cursor: crosshair; }
    .play__canvas-badge {
      position: absolute;
      top: 14px;
      left: 14px;
      font-family: var(--fm);
      font-size: 9.5px;
      color: var(--chalk);
      background: rgba(0, 0, 0, 0.75);
      padding: 4px 10px;
      border-radius: 4px;
      border: 1px solid var(--border);
      pointer-events: none;
    }
    .play__controls {
      display: flex;
      flex-direction: column;
      gap: 20px;
      background: var(--card-bg);
      border: 1px solid var(--border);
      padding: clamp(26px, 3.2vw, 40px);
      border-radius: 8px;
      backdrop-filter: blur(14px);
    }
    .play__controls h3 {
      font-family: var(--fh);
      font-size: 26px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: -0.02em;
    }
    .play__row {
      display: flex;
      flex-direction: column;
      gap: 8px;
    }
    .play__row-head {
      display: flex;
      justify-content: space-between;
      font-family: var(--fm);
      font-size: 11px;
      color: var(--dim);
    }
    .play__row-head span:last-child { color: var(--t); font-weight: 700; }
    input[type=range] {
      -webkit-appearance: none;
      width: 100%;
      background: rgba(255, 255, 255, 0.1);
      height: 4px;
      border-radius: 2px;
      outline: none;
    }
    input[type=range]::-webkit-slider-thumb {
      -webkit-appearance: none;
      width: 14px;
      height: 14px;
      border-radius: 50%;
      background: var(--t);
      cursor: pointer;
      box-shadow: 0 0 10px var(--t);
    }
    .play__charset-grid {
      display: flex;
      gap: 8px;
    }
    .play__charset-btn {
      flex: 1;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border);
      color: var(--dim);
      font-family: var(--fm);
      font-size: 11px;
      font-weight: 700;
      padding: 8px;
      border-radius: 4px;
      cursor: pointer;
      transition: all 0.2s ease;
    }
    .play__charset-btn:hover { color: var(--chalk); border-color: rgba(255, 255, 255, 0.3); }
    .play__charset-btn.active {
      background: var(--t);
      color: #FFFFFF;
      border-color: var(--t);
      box-shadow: 0 0 12px rgba(255, 36, 36, 0.45);
    }
    .play__btn-row {
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
      margin-top: 6px;
    }
    .btn-action {
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--border);
      color: var(--chalk);
      font-family: var(--fm);
      font-size: 10.5px;
      font-weight: 700;
      padding: 9px 16px;
      border-radius: 4px;
      cursor: pointer;
      text-decoration: none;
      transition: all 0.2s ease;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }
    .btn-action:hover {
      border-color: var(--t);
      color: var(--t);
    }
    .btn-action.primary {
      background: var(--t);
      color: #FFFFFF;
      border-color: var(--t);
      box-shadow: 0 0 16px rgba(255, 36, 36, 0.4);
    }
    .btn-action.primary:hover {
      background: #FF4444;
      box-shadow: 0 0 24px rgba(255, 36, 36, 0.6);
      color: #FFFFFF;
    }

    /* =====================================================================
       CHAPTER 08: INVERTED COLORWAY FINALE & TECHNICAL SPECIFICATION TABLE
       ===================================================================== */
    .finale {
      padding: clamp(90px, 14vh, 160px) var(--pad) clamp(60px, 10vh, 100px);
      background: #F4F4F6;
      color: #070707;
      z-index: 9;
      position: relative;
      transition: background 0.7s cubic-bezier(0.16, 1, 0.3, 1), color 0.7s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .finale__inner {
      max-width: 1320px;
      margin: 0 auto;
    }
    .finale .kicker {
      color: #FF292C;
    }
    .finale .kicker::before {
      background: #FF292C;
      box-shadow: 0 0 8px rgba(255, 36, 36, 0.6);
    }
    .finale__headline {
      font-family: var(--fh);
      font-size: clamp(38px, 6vw, 92px);
      font-weight: 900;
      line-height: 1.02;
      letter-spacing: -0.04em;
      text-transform: uppercase;
      margin-bottom: 48px;
      color: #070707;
    }
    .spec-table-wrap {
      border: 2px solid #070707;
      background: #FFFFFF;
      border-radius: 4px;
      overflow: hidden;
      margin-bottom: 48px;
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.08);
    }
    .spec-table-head {
      background: #070707;
      color: #FFFFFF;
      padding: 14px 24px;
      font-family: var(--fm);
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.16em;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .spec-table-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
    }
    .spec-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 18px 24px;
      border-bottom: 1px solid #E5E5EB;
      font-family: var(--fm);
      font-size: 13.5px;
    }
    .spec-row:nth-child(odd) { border-right: 1px solid #E5E5EB; }
    .spec-key {
      color: #6E6E78;
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 0.08em;
    }
    .spec-val {
      font-weight: 700;
      color: #070707;
      text-align: right;
    }
    .spec-val.crimson {
      color: #FF292C;
    }
    .spec-val code {
      font-size: 12px;
      background: #EEEEF2;
      padding: 2px 6px;
      border-radius: 3px;
    }
    .finale__actions {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 20px;
      padding-top: 24px;
      border-top: 1px solid #D5D5DF;
    }
    .finale__links {
      display: flex;
      gap: 14px;
      flex-wrap: wrap;
    }
    .btn-finale {
      background: #070707;
      color: #FFFFFF;
      font-family: var(--fm);
      font-size: 11px;
      font-weight: 700;
      padding: 12px 24px;
      border-radius: 4px;
      text-decoration: none;
      letter-spacing: 0.08em;
      transition: all 0.2s ease;
      display: inline-flex;
      align-items: center;
      gap: 8px;
    }
    .btn-finale:hover {
      background: #FF292C;
      box-shadow: 0 0 20px rgba(255, 36, 36, 0.45);
      color: #FFFFFF;
    }
    .btn-finale.outline {
      background: transparent;
      color: #070707;
      border: 1.5px solid #070707;
    }
    .btn-finale.outline:hover {
      background: #070707;
      color: #FFFFFF;
    }
    .start-over {
      font-family: var(--fm);
      font-size: 11px;
      font-weight: 700;
      color: #070707;
      text-decoration: none;
      padding: 10px 18px;
      border: 1px solid #070707;
      border-radius: 9999px;
      transition: all 0.2s ease;
    }
    .start-over:hover {
      background: #FF292C;
      border-color: #FF292C;
      color: #FFFFFF;
    }

    /* FOOTER */
    .foot {
      padding: clamp(40px, 6vh, 60px) var(--pad);
      background: #020204;
      border-top: 1px solid var(--border);
      position: relative;
      z-index: 10;
      font-family: var(--fm);
      font-size: 11px;
      color: var(--dim);
    }
    .foot__grid {
      max-width: 1320px;
      margin: 0 auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 20px;
    }
    .foot__brand {
      display: flex;
      align-items: center;
      gap: 10px;
      color: var(--chalk);
      text-decoration: none;
      font-weight: 700;
    }
    .foot__brand img {
      width: 22px;
      height: 22px;
      object-fit: contain;
      border-radius: 3px;
    }

    /* RESPONSIVE DESIGN */
    @media (max-width: 960px) {
      .concept__cols { grid-template-columns: 1fr; }
      .above__pin { grid-template-columns: 1fr; }
      .rule__pin { grid-template-columns: 1fr; }
      .play__inner { grid-template-columns: 1fr; }
      .spec-table-grid { grid-template-columns: 1fr; }
      .spec-row:nth-child(odd) { border-right: none; }
      .hero__aside { flex-direction: column; align-items: flex-start; }
    }

    /* ===================================================================
       FLOATING PILL NAVIGATION (UNIFIED VRTL WRLD SYSTEM)
       =================================================================== */
    .nav-wrapper {
      position: fixed;
      top: 20px;
      left: 50%;
      transform: translateX(-50%);
      z-index: 9999;
      width: fit-content;
      max-width: 98vw;
      pointer-events: none;
    }
    .nav-pill {
      display: flex;
      align-items: center;
      padding: 6px 14px 6px 10px;
      border-radius: 9999px;
      background: rgba(11, 11, 14, 0.85);
      backdrop-filter: blur(16px) saturate(180%);
      -webkit-backdrop-filter: blur(16px) saturate(180%);
      border: 1px solid #1C1C24;
      box-shadow: 0 8px 32px rgba(0, 0, 0, 0.65), 0 0 0 1px rgba(255, 41, 44, 0.15);
      pointer-events: auto;
      white-space: nowrap;
    }
    .nav-brand {
      display: flex;
      align-items: center;
      gap: 10px;
      text-decoration: none;
      color: #FFFFFF;
      border-right: 1px solid #1C1C24;
      padding-right: 12px;
      margin-right: 12px;
      flex-shrink: 0;
    }
    .nav-logo-box {
      width: 24px;
      height: 24px;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }
    .nav-title {
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.12em;
      color: #FFFFFF;
      white-space: nowrap;
    }
    .nav-links {
      display: flex;
      align-items: center;
      gap: 4px;
      list-style: none;
    }
    .nav-link {
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      font-weight: 600;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: rgba(255, 255, 255, 0.60);
      text-decoration: none;
      padding: 6px 10px;
      border-radius: 9999px;
      border: 1px solid transparent;
      transition: all 0.18s cubic-bezier(0.16, 1, 0.3, 1);
      position: relative;
      white-space: nowrap;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }
    .nav-link:hover {
      color: #FFFFFF;
      background: rgba(255, 255, 255, 0.06);
      border-color: rgba(255, 255, 255, 0.18);
    }
    .nav-link.active {
      color: #FFFFFF;
      background: rgba(255, 41, 44, 0.14);
      border-color: #FF292C;
      box-shadow: 0 0 10px rgba(255, 41, 44, 0.35);
    }
    .nav-link.active::before {
      content: "";
      width: 4px;
      height: 4px;
      border-radius: 50%;
      background: #FF292C;
      box-shadow: 0 0 6px #FF292C;
      display: inline-block;
    }
    @media (max-width: 900px) {
      .nav-wrapper {
        top: 10px;
        max-width: 96vw;
        overflow-x: auto;
        -webkit-overflow-scrolling: touch;
      }
      .nav-pill {
        padding: 4px 8px;
      }
      .nav-link {
        font-size: 9.5px;
        padding: 4px 6px;
      }
    }
    .glitch-active {
      opacity: 0.94;
      letter-spacing: 0.02em;
    }

  </style>
</head>
<body id="top">
  <!-- FLOATING PILL NAVBAR -->
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
        <a href="index.html" class="nav-link active" data-glitch>[ OVERVIEW ]</a>
        <a href="protocol.html" class="nav-link" data-glitch>[ PROTOCOL ]</a>
        <a href="simulator.html" class="nav-link" data-glitch>[ SIMULATOR ]</a>
        <a href="yield.html" class="nav-link" data-glitch>[ YIELD ]</a>
        <a href="nodes.html" class="nav-link" data-glitch>[ NODES ]</a>
        <a href="tokenomics.html" class="nav-link" data-glitch>[ TOKENOMICS ]</a>
        <a href="research.html" class="nav-link" data-glitch>[ RESEARCH ]</a>
        <a href="whitepaper.html" class="nav-link" data-glitch>[ WHITEPAPER ]</a>
      </div>
    </nav>
  </div>


  <!-- RIGHT HAIRLINE SCROLLBAR & TELEMETRY RAIL -->
  <div class="sbar" id="sbar" aria-hidden="true">
    <div class="sbar__ticks" id="sbar-ticks">
      <span class="active">00</span>
      <span>01</span>
      <span>02</span>
      <span>03</span>
      <span>04</span>
      <span>05</span>
      <span>06</span>
      <span>07</span>
      <span>08</span>
    </div>
    <div class="sbar__coord" id="sbar-coord">S_POS // 000</div>
    <i></i>
  </div>

  <!-- FLOATING BOTTOM-RIGHT MINIMAP PREVIEW -->
  <div class="minimap-hud" id="minimap" title="Click to scrub viewport">
    <div class="minimap-header">
      <span>TOPOLOGY</span>
      <span id="minimap-pct">0%</span>
    </div>
    <div class="minimap-preview">
      <div class="minimap-sections">
        <div class="minimap-dot"></div>
        <div class="minimap-dot"></div>
        <div class="minimap-dot"></div>
        <div class="minimap-dot"></div>
        <div class="minimap-dot"></div>
        <div class="minimap-dot"></div>
        <div class="minimap-dot"></div>
        <div class="minimap-dot"></div>
        <div class="minimap-dot"></div>
      </div>
      <div class="minimap-viewport-indicator" id="minimap-indicator"></div>
    </div>
  </div>

  <main>
    <!-- ===================================================================
         CHAPTER 00: PINNED HERO WITH MASSIVE KINETIC SPLIT TYPOGRAPHY
         =================================================================== -->
    <section class="hero" id="hero">
      <canvas class="hero__field-canvas" id="hero-field-canvas"></canvas>
      
      <div class="hero__top-meta">
        <div class="hero__protocol-tag">33RD TREE LABS // THE SINGULARITY PROTOCOL</div>
        <div>SOLANA MAINNET-BETA // 33RDTREELABS.TECH</div>
      </div>

      <div class="hero__content">
        <div class="hero__split">
          <div class="hero__line">33RD TREE</div>
          <div class="hero__line red-accent">SINGULARITY</div>
        </div>
      </div>

      <div class="hero__aside">
        <div class="hero__scroll-indicator">
          <div class="hero__scroll-pulse"></div>
          <div class="hero__scroll-text-group">
            <span class="hero__scroll-action">[ SCROLL TO COMMENCE CONSENSUS ]</span>
            <span class="hero__scroll-sub">VERIFIABLE TENSOR ARBOR &bull; CANARY V4.0</span>
          </div>
        </div>
        <div class="hero__foot-badges">
          <span class="hero__badge-tag">TOPOLOGY: <strong>GROMOV &delta;-HYPERBOLIC</strong></span>
          <span class="hero__badge-tag">PRECISION: <strong>&Delta;&epsilon; = 0.00 INT8</strong></span>
          <span class="hero__badge-tag">CONSENSUS: <strong>K=64 QUORUM</strong></span>
        </div>
      </div>
    </section>

    <!-- ===================================================================
         CHAPTER 01: THE THESIS & CONCEPT (BRUTALIST STROKE & FILL)
         =================================================================== -->
    <section class="concept" id="concept">
      <div class="concept__inner">
        <div class="kicker">CHAPTER 01 // ARCHITECTURAL THESIS</div>
        <h2 class="concept__headline">
          COORDINATING <span class="badge-fill">HETEROGENEOUS COMPUTE</span> INTO <span class="badge-box">DETERMINISTIC FINALITY</span>
        </h2>
        
        <!-- DEDICATED HIGH-CONTRAST ARCHITECTURAL MANIFESTO CARD -->
        <div class="manifesto-card">
          <div class="manifesto-card__header">
            <div class="manifesto-card__tag">
              <span class="manifesto-dot"></span>
              <span>CORE ARCHITECTURAL MANIFESTO // SINGULARITY PROTOCOL</span>
            </div>
            <div class="manifesto-card__meta">ANCHOR: SOLANA // BIT-EXACT FINALITY</div>
          </div>
          <p class="manifesto-card__body">
            A <strong>Byzantine-Resilient Verifiable DePIN Compute Fabric</strong> anchored on Solana. Hierarchical <strong>Tensor Arbor coordination</strong>, zero-knowledge neural evaluations, and <strong>deterministic consensus</strong> across heterogeneous GPU clusters.
          </p>
          <div class="manifesto-card__footer">
            <div class="manifesto-metric">
              <span class="manifesto-metric__label">CONSENSUS ARCHITECTURE</span>
              <span class="manifesto-metric__val">K=64 BYZANTINE QUORUM</span>
            </div>
            <div class="manifesto-metric">
              <span class="manifesto-metric__label">ROUTING MANIFOLD</span>
              <span class="manifesto-metric__val">GROMOV &delta;-HYPERBOLIC (&le; 8 HOPS)</span>
            </div>
            <div class="manifesto-metric">
              <span class="manifesto-metric__label">EVALUATION TOLERANCE</span>
              <span class="manifesto-metric__val">&Delta;&epsilon; = 0.00 INT8 INVARIANT</span>
            </div>
          </div>
        </div>
        
        <div class="concept__cols">
          <div class="concept__col">
            <h3>THE DEPIN COMPUTE TRILEMMA</h3>
            <p data-words>
              Decentralized AI inference faces a silent mathematical catastrophe: floating-point non-determinism. Two distinct GPU architectures (e.g. Hopper H100 vs Blackwell B200) executing identical FP32 weights generate divergent lower-order bits due to fused multiply-add (FMA) reordering and divergent compiler kernels.
            </p>
            <p data-words>
              Under standard Byzantine fault-tolerant consensus, bit divergence makes majority voting mathematically impossible. Without bit-exact consensus, verifiers cannot slash rogue nodes or validate execution integrity without re-running the entire neural network from scratch—destroying scalability.
            </p>
            <div class="concept__callout">
              <strong>CANARY PRINCIPLE:</strong> "Execution without bit-exact determinism is not consensus—it is merely statistical guesswork."
            </div>
          </div>

          <div class="concept__col">
            <h3>THE TENSOR ARBOR SOLUTION</h3>
            <p data-words>
              33rd Tree Labs solves the trilemma through three foundational cryptographic and mathematical primitives:
            </p>
            <p data-words>
              <strong>1. Gromov &delta;-Hyperbolic Routing:</strong> Mapping cluster coordinates into negative-curvature hyperbolic spaces, guaranteeing maximum packet routing diameter &le; 8 hops across planet-scale topologies.
            </p>
            <p data-words>
              <strong>2. INT8 Quantized Invariants (&Delta;&epsilon; = 0.00):</strong> Enforcing cross-architecture integer quantization so execution produces identical tensor matrices down to the lowest bit on all verified hardware.
            </p>
            <p data-words>
              <strong>3. Succinct ZK Commitments:</strong> Generating recursive Plonky2 validity proofs of neural states anchored on Solana with sub-second finality.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- ===================================================================
         CHAPTER 02: PINNED ALTITUDE DESCENT (1208 M -> 0008 M)
         =================================================================== -->
    <section class="above" id="above">
      <canvas class="above__canvas-bg" id="above-canvas"></canvas>
      <div class="above__pin">
        <div class="above__metric-box">
          <div class="above__counter-wrap">
            <div class="above__counter" id="altitude-counter">1208</div>
            <div class="above__unit">M</div>
          </div>
          <div class="above__label">[ TOPOLOGICAL RADIAL ALTITUDE // DESCENT TO SINGULARITY ]</div>
          <p data-words style="color: var(--chalk); font-size: 15px; line-height: 1.65;">
            Seen from above, the network unfolds as a living neural lattice. As the observer descends through hyperbolic coordinate layers, individual tensor clusters resolve into deterministic validator nodes.
          </p>
          <div class="above__telemetry-grid">
            <div class="above__telemetry-item">
              <span>CURVATURE (&kappa;)</span>
              <span>-1.414</span>
            </div>
            <div class="above__telemetry-item">
              <span>MAX DIAMETER</span>
              <span>&le; 8 HOPS</span>
            </div>
            <div class="above__telemetry-item">
              <span>QUORUM COMMITTEE</span>
              <span>K = 64</span>
            </div>
          </div>
        </div>

        <div class="above__copy">
          <div class="kicker">CHAPTER 02 // NETWORK TOPOLOGY</div>
          <h2>SEEN FROM ABOVE,<br>IT LOOKS LIKE A<br>NEURAL LATTICE.</h2>
          <p data-words>
            Traditional peer-to-peer compute networks degrade exponentially with scale: $O(N^2)$ communication complexity suffocates latency. By embedding cluster nodes into a Poincaré disk model of Gromov hyperbolic geometry, routing paths follow geodesics that plunge toward the center and branch outward with logarithmic efficiency.
          </p>
          <div style="display: flex; gap: 14px; flex-wrap: wrap;">
            <a href="whitepaper.html" class="btn-action primary">[ READ WHITEPAPER ]</a>
            <a href="research.html" class="btn-action">[ MATHEMATICAL PROOFS ]</a>
          </div>
        </div>
      </div>
    </section>

    <!-- ===================================================================
         CHAPTER 03: PINNED 4-INSTRUCTION BEHAVIOUR STEPPER
         =================================================================== -->
    <section class="rule" id="rule">
      <div class="rule__pin">
        <div class="rule__steps">
          <div class="kicker">CHAPTER 03 // EXECUTION PIPELINE</div>
          <h2 style="font-family: var(--fh); font-size: clamp(32px, 4.2vw, 54px); font-weight: 900; text-transform: uppercase; margin-bottom: 20px;">
            ONE PROTOCOL.<br>FOUR INSTRUCTIONS.
          </h2>
          
          <div class="step is-active" data-step="0">
            <div class="step__header">
              <span class="step__nr">INSTRUCTION 01</span>
              <span class="step__verb">DISPATCH</span>
            </div>
            <div class="step__desc">Inference tasks mapped into hyperbolic arbor coordinates; neural weights quantized to deterministic INT8 invariants.</div>
            <div class="step__bar"><i style="transform: scaleX(1);"></i></div>
          </div>

          <div class="step" data-step="1">
            <div class="step__header">
              <span class="step__nr">INSTRUCTION 02</span>
              <span class="step__verb">CONSENSUS</span>
            </div>
            <div class="step__desc">K=64 Byzantine validator committee evaluates execution output hashes with bit-exact zero delta verification.</div>
            <div class="step__bar"><i></i></div>
          </div>

          <div class="step" data-step="2">
            <div class="step__header">
              <span class="step__nr">INSTRUCTION 03</span>
              <span class="step__verb">COMMITMENT</span>
            </div>
            <div class="step__desc">Plonky2 / KZG zero-knowledge validity proof generated and anchored directly to Solana blockchain state.</div>
            <div class="step__bar"><i></i></div>
          </div>

          <div class="step" data-step="3">
            <div class="step__header">
              <span class="step__nr">INSTRUCTION 04</span>
              <span class="step__verb">SETTLE & BURN</span>
            </div>
            <div class="step__desc">75% hardware yield distributed, 15% R&D multisig, 10% perpetually burned to Solana Incinerator.</div>
            <div class="step__bar"><i></i></div>
          </div>
        </div>

        <div class="rule__interactive-preview">
          <div class="rule__canvas-box">
            <canvas id="rule-canvas"></canvas>
          </div>
          <div class="rule__preview-foot">
            <span>STATE MACHINE VERIFIER</span>
            <span id="active-step-name" style="color: var(--t); font-weight: 700;">INSTRUCTION 01 // DISPATCH</span>
          </div>
        </div>
      </div>
    </section>

    <!-- ===================================================================
         CHAPTER 04: PINNED HORIZONTAL RAIL (SIDEWAYS SCROLLING SECTION)
         =================================================================== -->
    <section class="pairs-section" id="clusters">
      <div class="pairs-track-wrap">
        <div class="pairs-track" id="pairs-track">
          <div class="pair-intro">
            <div class="kicker">CHAPTER 04 // CLUSTERS & HARDWARE</div>
            <h2>VERIFIED<br>COMPUTE<br>FABRIC</h2>
            <p data-words>
              High-throughput accelerator hardware bonded via Anchor smart contracts on Solana. Explore cluster tiers, memory bandwidth, and economic guarantees.
            </p>
          </div>

          <!-- Card 1: H100 -->
          <div class="pair-card">
            <div class="pair-card__tag">CLUSTER 01 // H100 SXM5 80GB HBM3</div>
            <div class="pair-card__title">FRONTIER DEEP LEARNING</div>
            <div class="pair-card__desc">Ultra-high bandwidth NVLink clusters dedicated to large MoE inference, multi-billion parameter checkpoint evaluations, and parallel tensor reduction.</div>
            <div class="pair-card__stat-grid">
              <div>
                <div class="pair-card__stat-val">3,350 GB/s</div>
                <div class="pair-card__stat-lbl">Memory Bandwidth</div>
              </div>
              <div>
                <div class="pair-card__stat-val">25,000 $33RD</div>
                <div class="pair-card__stat-lbl">Min Node Bond</div>
              </div>
            </div>
          </div>

          <!-- Card 2: B200 -->
          <div class="pair-card">
            <div class="pair-card__tag">CLUSTER 02 // B200 BLACKWELL</div>
            <div class="pair-card__title">NEXT-GEN QUANTUM-RESILIENT</div>
            <div class="pair-card__desc">Dedicated FP4 / FP8 neural pipeline accelerators executing live real-time KZG polynomial commitments and recursive STARK verification.</div>
            <div class="pair-card__stat-grid">
              <div>
                <div class="pair-card__stat-val">8,000 GB/s</div>
                <div class="pair-card__stat-lbl">Memory Bandwidth</div>
              </div>
              <div>
                <div class="pair-card__stat-val">&lt; 1.84ms</div>
                <div class="pair-card__stat-lbl">KZG Opening Time</div>
              </div>
            </div>
          </div>

          <!-- Card 3: 4090 / 5090 -->
          <div class="pair-card">
            <div class="pair-card__tag">CLUSTER 03 // RTX 4090 & 5090 EDGE</div>
            <div class="pair-card__title">DECENTRALIZED WORKERS</div>
            <div class="pair-card__desc">Dense consumer-tier GPU clusters providing distributed edge inference and zero-knowledge batch proof generation across sovereign nodes.</div>
            <div class="pair-card__stat-grid">
              <div>
                <div class="pair-card__stat-val">24GB - 32GB</div>
                <div class="pair-card__stat-lbl">VRAM Capacity</div>
              </div>
              <div>
                <div class="pair-card__stat-val">75% Yield</div>
                <div class="pair-card__stat-lbl">Hardware Reward Pool</div>
              </div>
            </div>
          </div>

          <!-- Card 4: Tokenomics -->
          <div class="pair-card">
            <div class="pair-card__tag">TOKENOMICS // VERIFIED IMMUTABLE</div>
            <div class="pair-card__title">33,333,333 HARD CAP</div>
            <div class="pair-card__desc">Strict deflationary mechanics with 100% of initial LP tokens sent directly to Solana Incinerator. Protocol burns fees perpetually on every compute cycle.</div>
            <div class="pair-card__stat-grid">
              <div>
                <div class="pair-card__stat-val">33,333,333</div>
                <div class="pair-card__stat-lbl">Fixed Hard Cap</div>
              </div>
              <div>
                <div class="pair-card__stat-val">100% LP Burn</div>
                <div class="pair-card__stat-lbl">To 1nc1nerator</div>
              </div>
            </div>
          </div>

          <!-- Card 5: Gromov Metric -->
          <div class="pair-card">
            <div class="pair-card__tag">GEOMETRY // TOPOLOGY</div>
            <div class="pair-card__title">POINCARÉ DISK EMBEDDING</div>
            <div class="pair-card__desc">Nodes mapped to negative curvature coordinates. Packets navigate along geodesic hyperbolas, preventing mesh congestion and network partitioning.</div>
            <div class="pair-card__stat-grid">
              <div>
                <div class="pair-card__stat-val">&le; 8 Hops</div>
                <div class="pair-card__stat-lbl">Max Global Diameter</div>
              </div>
              <div>
                <div class="pair-card__stat-val">&kappa; = -1.414</div>
                <div class="pair-card__stat-lbl">Negative Curvature</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ===================================================================
         CHAPTER 05: MATHEMATICAL INVARIANTS & BYZANTINE SLASHING
         =================================================================== -->
    <section class="invariants" id="invariants">
      <div class="invariants__inner">
        <div class="kicker">CHAPTER 05 // MATHEMATICAL INVARIANTS &amp; FORMAL VERIFICATION</div>
        <h2 class="invariants__headline">
          FORMAL VERIFICATION &amp; <span class="badge-fill">BYZANTINE SLASHING</span>
        </h2>
        
        <p class="invariants__lead" data-words>
          Decentralized execution security cannot rely on probabilistic trust or statistical convergence. 33rd Tree Labs enforces five deterministic invariants encoded directly into Solana Anchor programs, mathematically binding staked hardware collateral to bit-exact neural verification.
        </p>

        <!-- 3 Invariant Pillar Cards -->
        <div class="invariants__pillars">
          <div class="invariant-card">
            <div>
              <div class="invariant-card__tag">INVARIANT 01 // PRECISION</div>
              <div class="invariant-card__title">DETERMINISTIC INT8 REDUCTION</div>
              <div class="invariant-card__formula">&Delta;&epsilon; = 0.00 &bull; BIT-EXACT</div>
              <div class="invariant-card__desc" data-words>
                Eliminating floating-point divergence (FMA reordering) across heterogeneous hardware backends (Hopper, Blackwell, Ada) via bit-exact integer reduction trees. Execution produces identical tensor outputs across all verified architectures.
              </div>
            </div>
            <div class="invariant-card__foot">
              <span>BOUND: ABSOLUTE ZERO DELTA</span>
            </div>
          </div>

          <div class="invariant-card">
            <div>
              <div class="invariant-card__tag">INVARIANT 02 // GAME THEORY</div>
              <div class="invariant-card__title">QUADRATIC SLASHING ESCALATION</div>
              <div class="invariant-card__formula">S_penal(n) = min(1.0, k &bull; n&sup2; &bull; S_base)</div>
              <div class="invariant-card__desc" data-words>
                Correlated Byzantine faults within an unbonding epoch trigger quadratic capital destruction. Sybil cartels attempting coordinated state divergence suffer total staked collateral annihilation.
              </div>
            </div>
            <div class="invariant-card__foot">
              <span>UNBONDING: 7 DAYS (10,080 BLOCKS)</span>
            </div>
          </div>

          <div class="invariant-card">
            <div>
              <div class="invariant-card__tag">INVARIANT 03 // VALUE ACCRUAL</div>
              <div class="invariant-card__title">10% INCINERATOR BURN FLOOR</div>
              <div class="invariant-card__formula">1nc1nerator...1111 &bull; DEFLATIONARY</div>
              <div class="invariant-card__desc" data-words>
                10% of every inference micro-fee is atomically routed to the Solana Incinerator for permanent destruction. When daily volume exceeds 51,370 RD, burn exceeds emissions, locking in strict monetary deflation.
              </div>
            </div>
            <div class="invariant-card__foot">
              <span>TIPPING POINT: &gt; 51,370 RD / DAY</span>
            </div>
          </div>
        </div>

        <!-- Slashing Penalty Matrix Table -->
        <div class="slashing-table-wrap">
          <div class="slashing-table-header">
            <span>BYZANTINE SLASHING PENALTY MATRIX // SOLANA ANCHOR ESCROW</span>
            <span>MIN STAKE: 25,000 RD</span>
          </div>
          <div class="slashing-table-grid">
            <div class="slashing-row header">
              <span>VIOLATION TYPE</span>
              <span>SEVERITY</span>
              <span>SLASHED STAKE</span>
              <span>ALLOCATION</span>
              <span>PROTOCOL ACTION</span>
            </div>
            
            <div class="slashing-row">
              <span style="color: var(--chalk); font-weight: 700;">Dual-Signing / Equivocation</span>
              <span class="slashing-val-crimson">CRITICAL</span>
              <span class="slashing-val-crimson">100%</span>
              <span>50% Burned, 50% Bounty</span>
              <span>Permanent ban of Node ID &amp; Hardware Key</span>
            </div>

            <div class="slashing-row">
              <span style="color: var(--chalk); font-weight: 700;">Invalid INT8 Tensor Output</span>
              <span class="slashing-val-crimson">CRITICAL</span>
              <span class="slashing-val-crimson">50%</span>
              <span>50% Burned to Incinerator</span>
              <span>Node disqualified from epoch; slot rolled back</span>
            </div>

            <div class="slashing-row">
              <span style="color: var(--chalk); font-weight: 700;">Failed Halo2-KZG Proof Challenge</span>
              <span style="color: #FF9800; font-weight: 700;">HIGH</span>
              <span class="slashing-val-crimson">25%</span>
              <span>25% Burned to Incinerator</span>
              <span>Challenger rewarded with 5,000 RD bounty</span>
            </div>

            <div class="slashing-row">
              <span style="color: var(--chalk); font-weight: 700;">TEE Attestation Mismatch</span>
              <span style="color: #FF9800; font-weight: 700;">HIGH</span>
              <span class="slashing-val-crimson">30%</span>
              <span>100% Burned to Incinerator</span>
              <span>Silicon attestation revoked; node deregistered</span>
            </div>

            <div class="slashing-row">
              <span style="color: var(--chalk); font-weight: 700;">Liveness Failure (&gt;10 Omitted Slots)</span>
              <span style="color: #00E676; font-weight: 700;">MEDIUM</span>
              <span>5%</span>
              <span>Protocol Treasury</span>
              <span>Node demoted to standby queue</span>
            </div>

            <div class="slashing-row">
              <span style="color: var(--chalk); font-weight: 700;">Tier-1 Speculative Fraud Execution</span>
              <span style="color: #FF9800; font-weight: 700;">HIGH</span>
              <span class="slashing-val-crimson">50,000 RD</span>
              <span>100% Proposer Bond Slashed</span>
              <span>Client awarded 10x refund; slot slashed</span>
            </div>
          </div>
        </div>

      </div>
    </section>

    <!-- ===================================================================
         CHAPTER 06: PINNED EXPANDING SCHEMATIC FILM (TENSOR ARBOR WIREFRAME)
         =================================================================== -->
    <section class="film-section" id="film">
      <div class="film-clip" id="film-clip">
        <canvas id="film-canvas"></canvas>
      </div>
      <div class="film-overlay-text">
        <span class="dot"></span>
        <span>EXPONENTIAL PLUNGE TENSOR ARBOR WIREFRAME // MARK #06 SINGULARITY SPECIFICATION</span>
      </div>
    </section>

    <!-- ===================================================================
         CHAPTER 07: INTERACTIVE CONSENSUS & CELLULAR PLAYGROUND
         =================================================================== -->
    <section class="play" id="playground">
      <div class="play__inner">
        <div class="play__canvas-box">
          <canvas id="playground-canvas"></canvas>
          <div class="play__canvas-badge">CELLULAR TENSOR MATRIX // INTERACTIVE FIELD</div>
        </div>

        <div class="play__controls">
          <div class="kicker">CHAPTER 07 // PROTOCOL SIMULATION</div>
          <h3>CONSENSUS PLAYGROUND</h3>
          
          <div class="play__row">
            <div class="play__row-head">
              <span>BYZANTINE QUORUM COMMITTEE (K)</span>
              <span id="k-out">64</span>
            </div>
            <input type="range" id="k-slider" min="16" max="64" value="64" step="8">
          </div>

          <div class="play__row">
            <div class="play__row-head">
              <span>CELL RESOLUTION</span>
              <span id="res-out">32</span>
            </div>
            <input type="range" id="res-slider" min="16" max="64" value="32" step="4">
          </div>

          <div class="play__row">
            <div class="play__row-head">
              <span>MANIFOLD VELOCITY</span>
              <span id="speed-out">0.6</span>
            </div>
            <input type="range" id="speed-slider" min="0.1" max="2.5" value="0.6" step="0.1">
          </div>

          <div class="play__row">
            <div class="play__row-head">
              <span>TENSOR SYMBOL FIELD SWITCHER</span>
              <span id="mode-out">TENSOR [⊗ / ∇]</span>
            </div>
            <div class="play__charset-grid">
              <button type="button" class="play__charset-btn active" data-mode="tensor">&otimes; / &nabla;</button>
              <button type="button" class="play__charset-btn" data-mode="hyperbolic">&lambda; / &Delta;</button>
              <button type="button" class="play__charset-btn" data-mode="lattice">&#9532; / &middot;</button>
              <button type="button" class="play__charset-btn" data-mode="reduction">&Sigma; / T</button>
            </div>
          </div>

          <div class="play__btn-row">
            <button type="button" id="btn-pause" class="btn-action">PAUSE</button>
            <button type="button" id="btn-random" class="btn-action">RANDOM SEED</button>
            <button type="button" id="btn-save-png" class="btn-action">EXPORT PNG</button>
            <a href="simulator.html" class="btn-action primary">FULL SIMULATOR &rarr;</a>
          </div>
        </div>
      </div>
    </section>

    <!-- ===================================================================
         CHAPTER 08: INVERTED COLORWAY FINALE & TECHNICAL SPECIFICATION TABLE
         =================================================================== -->
    <section class="finale" id="finale">
      <div class="finale__inner">
        <div class="kicker">CHAPTER 08 // PROTOCOL SPECIFICATIONS</div>
        <h2 class="finale__headline">
          VERIFIABLE <span class="badge-crimson">DEPIN COMPUTE</span> ON SOLANA
        </h2>

        <div class="spec-table-wrap">
          <div class="spec-table-head">
            <span>TECHNICAL SPECIFICATION MATRIX // CANARY V4.0</span>
            <span>DOMAIN: 33RDTREELABS.TECH</span>
          </div>
          <div class="spec-table-grid">
            <div class="spec-row">
              <span class="spec-key">PROTOCOL NAME</span>
              <span class="spec-val">33RD TREE LABS // THE SINGULARITY</span>
            </div>
            <div class="spec-row">
              <span class="spec-key">SETTLEMENT LAYER</span>
              <span class="spec-val">SOLANA MAINNET-BETA</span>
            </div>
            <div class="spec-row">
              <span class="spec-key">HARD CAP TOKEN SUPPLY</span>
              <span class="spec-val crimson">33,333,333 $33RD</span>
            </div>
            <div class="spec-row">
              <span class="spec-key">LP LIQUIDITY STATUS</span>
              <span class="spec-val crimson">100% BURNED TO INCINERATOR</span>
            </div>
            <div class="spec-row">
              <span class="spec-key">INCINERATOR ADDRESS</span>
              <span class="spec-val"><code>1nc1nerator11111111111111111111111111111111</code></span>
            </div>
            <div class="spec-row">
              <span class="spec-key">MINIMUM NODE STAKE</span>
              <span class="spec-val">25,000 $33RD</span>
            </div>
            <div class="spec-row">
              <span class="spec-key">BYZANTINE QUORUM SIZE</span>
              <span class="spec-val">K = 64 NODES</span>
            </div>
            <div class="spec-row">
              <span class="spec-key">MAX ROUTING DIAMETER</span>
              <span class="spec-val">&le; 8 HOPS (GROMOV HYPERBOLIC)</span>
            </div>
            <div class="spec-row">
              <span class="spec-key">EVALUATION PRECISION</span>
              <span class="spec-val">&Delta;&epsilon; = 0.00 DETERMINISTIC INT8</span>
            </div>
            <div class="spec-row">
              <span class="spec-key">ZK VALIDITY PROOFS</span>
              <span class="spec-val">RECURSIVE PLONKY2 / KZG</span>
            </div>
            <div class="spec-row">
              <span class="spec-key">HARDWARE YIELD ALLOCATION</span>
              <span class="spec-val">75% OPERATORS / 15% R&D / 10% BURN</span>
            </div>
            <div class="spec-row">
              <span class="spec-key">CANONICAL DOMAIN</span>
              <span class="spec-val"><code>33rdtreelabs.tech</code></span>
            </div>
          </div>
        </div>

        <div class="finale__actions">
          <div class="finale__links">
            <a href="whitepaper.html" class="btn-finale">[ READ FULL WHITEPAPER ]</a>
            <a href="protocol.html" class="btn-finale outline">[ PROTOCOL SPECS ]</a>
            <a href="nodes.html" class="btn-finale outline">[ JOIN NODE NETWORK ]</a>
          </div>
          <a href="#top" class="start-over">[ START OVER &uarr; ]</a>
        </div>
      </div>
    </section>
  </main>

  <!-- FOOTER -->
  <footer class="foot">
    <div class="foot__grid">
      <div class="foot__brand">
        <img src="assets/official_logo_mark.jpg" alt="33rd Tree Labs Logo" width="22" height="22">
        <span>33RD TREE LABS // THE SINGULARITY PROTOCOL</span>
      </div>
      <div>OFFICIAL DOMAIN: 33RDTREELABS.TECH &bull; IMMUTABLE ANCHOR STATE</div>
      <div>&copy; 2026 33RD TREE LABS. ALL RIGHTS RESERVED.</div>
    </div>
  </footer>

  <!-- ===================================================================
       JAVASCRIPT ENGINE & GENERATIVE FIELD SYSTEM
       =================================================================== -->
  <script>
    /* A. PERLIN SIMPLEX NOISE ENGINE */
    const Noise = (() => {
      const d = new Uint8Array(512);
      function e(t) {
        let i = t >>> 0;
        const o = () => {
          i |= 0; i = i + 1831565813 | 0;
          let s = Math.imul(i ^ i >>> 15, 1 | i);
          return s = s + Math.imul(s ^ s >>> 7, 61 | s) ^ s, ((s ^ s >>> 14) >>> 0) / 4294967296;
        };
        const r = Array.from({ length: 256 }, (s, l) => l);
        for (let s = 255; s > 0; s--) {
          const l = Math.floor(o() * (s + 1));
          [r[s], r[l]] = [r[l], r[s]];
        }
        for (let s = 0; s < 512; s++) d[s] = r[s & 255];
      }
      const h = t => t * t * t * (t * (t * 6 - 15) + 10);
      const c = (t, i, o) => i + t * (o - i);
      function n(t, i, o, r) {
        t &= 15;
        const s = t < 8 ? i : o;
        const l = t < 4 ? o : t === 12 || t === 14 ? i : r;
        return (t & 1 ? -s : s) + (t & 2 ? -l : l);
      }
      function p(t, i, o) {
        const r = Math.floor(t) & 255, s = Math.floor(i) & 255, l = Math.floor(o) & 255;
        t -= Math.floor(t); i -= Math.floor(i); o -= Math.floor(o);
        const u = h(t), M = h(i), R = h(o);
        const g = d[r] + s, k = d[g] + l, v = d[g + 1] + l;
        const a = d[r + 1] + s, b = d[a] + l, m = d[a + 1] + l;
        return c(R, c(M, c(u, n(d[k], t, i, o), n(d[b], t - 1, i, o)), c(u, n(d[v], t, i - 1, o), n(d[m], t - 1, i - 1, o))), c(M, c(u, n(d[k + 1], t, i, o - 1), n(d[b + 1], t - 1, i, o - 1)), c(u, n(d[v + 1], t, i - 1, o - 1), n(d[m + 1], t - 1, i - 1, o - 1))));
      }
      function f(t, i, o) {
        let r = 0, s = 0.5, l = 1;
        for (let M = 0; M < 4; M++) {
          r += s * p(t * l, i * l, o * l);
          s *= 0.5; l *= 2;
        }
        const u = 0.5 + r * 0.82;
        return u < 0 ? 0 : u > 1 ? 1 : u;
      }
      e(42);
      return { noise: f, seed: e };
    })();

    /* B. GENERATIVE TENSOR & HYPERBOLIC FIELD MODES */
    const MODES = {
      tensor:     { key: "tensor",     t: "⊗", f: "∇", tc: "#FF292C", fc: "#383846", scale: 0.015, label: "TENSOR [⊗ / ∇]" },
      hyperbolic: { key: "hyperbolic", t: "λ", f: "Δ", tc: "#FF292C", fc: "#383846", scale: 0.014, label: "HYPERBOLIC [λ / Δ]" },
      lattice:    { key: "lattice",    t: "┼", f: "·", tc: "#F2F2F5", fc: "#2B2B38", scale: 0.018, label: "LATTICE [┼ / ·]" },
      reduction:  { key: "reduction",  t: "Σ", f: "T", tc: "#FF292C", fc: "#383846", scale: 0.013, label: "REDUCTION [Σ / T]" }
    };
    let currentMode = "tensor";

    /* C. INTERACTIVE GENERATIVE FIELD CLASS WITH CURSOR REPULSION */
    class MatrixField {
      constructor(canvas, opts = {}) {
        this.c = canvas;
        this.ctx = canvas.getContext("2d", { alpha: false });
        this.cell = opts.cell || 30;
        this.mode = opts.mode || "tensor";
        this.t = 0;
        this.speed = opts.speed ?? 0.6;
        this.paused = false;
        this.mouseX = -1000;
        this.mouseY = -1000;
        this.mouseRadius = 140;
        this.tiles = new Map();
        
        this.resize();
        window.addEventListener('resize', () => this.resize());
        
        // Interactive cursor repulsion
        this.c.addEventListener('mousemove', (e) => {
          const rect = this.c.getBoundingClientRect();
          this.mouseX = (e.clientX - rect.left) * this.dpr;
          this.mouseY = (e.clientY - rect.top) * this.dpr;
        });
        this.c.addEventListener('mouseleave', () => {
          this.mouseX = -1000;
          this.mouseY = -1000;
        });
      }

      resize() {
        const r = this.c.parentElement.getBoundingClientRect();
        this.dpr = Math.min(window.devicePixelRatio || 1, 2);
        this.w = r.width || window.innerWidth;
        this.h = r.height || window.innerHeight;
        this.c.width = Math.round(this.w * this.dpr);
        this.c.height = Math.round(this.h * this.dpr);
        this.grid();
      }

      grid() {
        this.cp = Math.max(6, Math.round(this.cell * this.dpr));
        this.cw = this.ch = this.cp / this.dpr;
        this.cols = Math.ceil(this.w / this.cw);
        this.rows = Math.ceil(this.h / this.ch);
        this.tiles.clear();
      }

      setCell(c) {
        if (Math.round(c) !== this.cell) {
          this.cell = Math.max(10, Math.round(c));
          this.grid();
        }
      }

      tile(m, val, excited = false) {
        const key = m.key + '_' + (val ? '1' : '0') + '_' + this.cp + (excited ? '_ex' : '');
        if (this.tiles.has(key)) return this.tiles.get(key);
        const can = document.createElement("canvas");
        can.width = this.cp;
        can.height = this.cp;
        const ctx = can.getContext("2d");
        const s = this.cp;

        if (excited) {
          // Cursor hover excitement: brilliant crimson pulse with stark white tensor symbol
          ctx.fillStyle = "#FF292C";
          ctx.fillRect(0, 0, s, s);
          ctx.strokeStyle = "#FFFFFF";
          ctx.lineWidth = Math.max(1, s * 0.05);
          ctx.strokeRect(0.5, 0.5, s - 1, s - 1);
          ctx.fillStyle = "#FFFFFF";
          ctx.font = `700 ${Math.max(9, Math.round(s * 0.52))}px "JetBrains Mono", "Obel Mono", monospace`;
          ctx.textAlign = "center";
          ctx.textBaseline = "middle";
          ctx.fillText(val ? m.t : m.f, s / 2, s / 2);
        } else if (val) {
          // Active Tensor Node: Deep obsidian background, razor-sharp hairline frame, crimson symbol
          ctx.fillStyle = "#0c0607";
          ctx.fillRect(0, 0, s, s);
          ctx.strokeStyle = "rgba(255, 36, 36, 0.28)";
          ctx.lineWidth = 1;
          ctx.strokeRect(0.5, 0.5, s - 1, s - 1);
          ctx.fillStyle = m.tc || "#FF292C";
          ctx.font = `700 ${Math.max(9, Math.round(s * 0.52))}px "JetBrains Mono", "Obel Mono", monospace`;
          ctx.textAlign = "center";
          ctx.textBaseline = "middle";
          ctx.fillText(m.t, s / 2, s / 2);
        } else {
          // Quiescent Lattice State: Pure obsidian plate, faint hairline border, muted vector glyph
          ctx.fillStyle = "#050507";
          ctx.fillRect(0, 0, s, s);
          ctx.strokeStyle = "rgba(255, 255, 255, 0.035)";
          ctx.lineWidth = 1;
          ctx.strokeRect(0.5, 0.5, s - 1, s - 1);
          ctx.fillStyle = m.fc || "#32323E";
          ctx.font = `500 ${Math.max(9, Math.round(s * 0.48))}px "JetBrains Mono", "Obel Mono", monospace`;
          ctx.textAlign = "center";
          ctx.textBaseline = "middle";
          ctx.fillText(m.f, s / 2, s / 2);
        }
        
        this.tiles.set(key, can);
        return can;
      }

      frame(delta) {
        if (!this.paused) {
          this.t += delta * this.speed;
        }
        const m = MODES[this.mode];
        const ctx = this.ctx;
        const radSq = (this.mouseRadius * this.dpr) * (this.mouseRadius * this.dpr);

        for (let r = 0; r < this.rows; r++) {
          const cy = (r + 0.5) * this.ch;
          const py = r * this.cp;
          for (let c = 0; c < this.cols; c++) {
            const cx = (c + 0.5) * this.cw;
            const px = c * this.cp;
            
            // Check cursor proximity
            const dx = px - this.mouseX;
            const dy = py - this.mouseY;
            const distSq = dx * dx + dy * dy;
            const isExcited = distSq < radSq;

            const n = Noise.noise(cx * m.scale, cy * m.scale, this.t) > 0.5;
            const tImg = this.tile(m, n ? 1 : 0, isExcited);
            ctx.drawImage(tImg, px, py);
          }
        }
      }
    }

    // Initialize Hero Field
    const heroCanvas = document.getElementById('hero-field-canvas');
    let heroField = null;
    if (heroCanvas) {
      heroField = new MatrixField(heroCanvas, { cell: 32, mode: currentMode, speed: 0.5 });
    }

    // Initialize Altitude Field
    const aboveCanvas = document.getElementById('above-canvas');
    let aboveField = null;
    if (aboveCanvas) {
      aboveField = new MatrixField(aboveCanvas, { cell: 38, mode: "hyperbolic", speed: 0.3 });
    }

    // Initialize Playground Field
    const playCanvas = document.getElementById('playground-canvas');
    let playField = null;
    if (playCanvas) {
      playField = new MatrixField(playCanvas, { cell: 32, mode: currentMode, speed: 0.6 });
    }

    // Global Animation Render Loop
    let lastTime = performance.now();
    function renderLoop(now) {
      const dt = Math.min((now - lastTime) / 1000, 0.1);
      lastTime = now;
      if (heroField) heroField.frame(dt);
      if (aboveField) aboveField.frame(dt);
      if (playField) playField.frame(dt);
      requestAnimationFrame(renderLoop);
    }
    requestAnimationFrame(renderLoop);

    /* D. LENIS SMOOTH INERTIA SCROLLING (LERP: 0.085) */
    gsap.registerPlugin(ScrollTrigger);

    const lenis = new Lenis({
      lerp: 0.085, // Signature fluid booleansequence inertia
      wheelMultiplier: 1.0,
      touchMultiplier: 1.3,
      smoothWheel: true,
      smoothTouch: false
    });
    lenis.on('scroll', ScrollTrigger.update);
    gsap.ticker.add((time) => {
      lenis.raf(time * 1000);
    });
    gsap.ticker.lagSmoothing(0);
    window.__lenis = lenis;

    /* E. RIGHT HAIRLINE SCROLLBAR & TELEMETRY RAIL */
    const sbar = document.getElementById('sbar');
    const sbarThumb = sbar.querySelector('i');
    const sbarCoord = document.getElementById('sbar-coord');
    const sbarTicks = document.querySelectorAll('#sbar-ticks span');
    const docEl = document.documentElement;
    let isDrag = false;
    let dragY = null;

    function updateSbar() {
      const max = docEl.scrollHeight - window.innerHeight;
      if (max <= 1) { sbar.hidden = true; return; }
      sbar.hidden = false;
      const h = Math.max(38, window.innerHeight * window.innerHeight / docEl.scrollHeight);
      sbarThumb.style.height = h + 'px';
      const sy = window.scrollY || docEl.scrollTop;
      const progress = Math.min(1, Math.max(0, sy / max));
      sbarThumb.style.transform = `translateY(${progress * (window.innerHeight - h)}px)`;
      
      // Update coordinates (000 -> 999)
      const coordVal = Math.round(progress * 999);
      const coordStr = coordVal < 10 ? '00' + coordVal : coordVal < 100 ? '0' + coordVal : '' + coordVal;
      if (sbarCoord) sbarCoord.textContent = `S_POS // ${coordStr}`;

      // Update tick activation
      const activeTick = Math.min(8, Math.floor(progress * 9));
      sbarTicks.forEach((t, idx) => {
        t.classList.toggle('active', idx === activeTick);
      });
      const miniDots = document.querySelectorAll('.minimap-dot');
      miniDots.forEach((dot, idx) => {
        dot.classList.toggle('active', idx === activeTick);
      });

      // Update Minimap indicator
      const minimapIndicator = document.getElementById('minimap-indicator');
      const minimapPct = document.getElementById('minimap-pct');
      if (minimapIndicator) {
        const miniHeight = 60; // preview inner height approx
        const indH = Math.max(8, (window.innerHeight / docEl.scrollHeight) * miniHeight);
        minimapIndicator.style.height = indH + 'px';
        minimapIndicator.style.transform = `translateY(${progress * (miniHeight - indH)}px)`;
      }
      if (minimapPct) {
        minimapPct.textContent = Math.round(progress * 100) + '%';
      }
    }

    window.addEventListener('scroll', updateSbar, { passive: true });
    window.addEventListener('resize', updateSbar);
    lenis.on('scroll', updateSbar);
    updateSbar();

    sbar.addEventListener('pointerdown', (e) => {
      const rect = sbarThumb.getBoundingClientRect();
      dragY = e.target === sbarThumb ? e.clientY - rect.top : rect.height / 2;
      sbar.setPointerCapture(e.pointerId);
      sbar.classList.add('is-drag');
      scrubSbar(e.clientY);
    });
    sbar.addEventListener('pointermove', (e) => { if (dragY !== null) scrubSbar(e.clientY); });
    function endDrag() { dragY = null; sbar.classList.remove('is-drag'); }
    sbar.addEventListener('pointerup', endDrag);
    sbar.addEventListener('pointercancel', endDrag);

    function scrubSbar(clientY) {
      const max = docEl.scrollHeight - window.innerHeight;
      const h = sbarThumb.offsetHeight;
      const frac = Math.min(1, Math.max(0, (clientY - dragY) / (window.innerHeight - h)));
      lenis.scrollTo(frac * max, { immediate: true });
    }

    // Minimap click scrubbing
    const minimap = document.getElementById('minimap');
    if (minimap) {
      minimap.addEventListener('click', (e) => {
        const rect = minimap.getBoundingClientRect();
        const frac = Math.min(1, Math.max(0, (e.clientY - rect.top - 20) / (rect.height - 24)));
        const max = docEl.scrollHeight - window.innerHeight;
        lenis.scrollTo(frac * max, { duration: 1.0 });
      });
    }

    /* F. CHAPTER 00: PINNED HERO KINETIC TYPOGRAPHY & FIELD ZOOM */
    const heroTl = gsap.timeline({
      scrollTrigger: {
        trigger: '.hero',
        start: 'top top',
        end: '+=85%',
        pin: true,
        scrub: 0.6,
        onUpdate: (self) => {
          if (heroField) {
            heroField.setCell(32 * (1 + self.progress * 2.8));
          }
        }
      }
    });

    heroTl
      .to('.hero__line:first-child', { xPercent: -18, ease: 'none' }, 0)
      .to('.hero__line.red-accent', { xPercent: 16, ease: 'none' }, 0)
      .to('.hero__aside', { autoAlpha: 0, y: -45, ease: 'power1.in' }, 0);

    /* G. CHAPTER 02: PINNED ALTITUDE DESCENT (1208 M -> 0008 M) */
    const altitudeCounter = document.getElementById('altitude-counter');
    ScrollTrigger.create({
      trigger: '.above',
      start: 'top top',
      end: '+=150%',
      pin: '.above__pin',
      scrub: true,
      onUpdate: (self) => {
        if (altitudeCounter) {
          // Altitude descent from 1208 meters down to 0008 meters
          const alt = Math.round(1208 - self.progress * 1200);
          const formatted = alt < 10 ? '000' + alt : alt < 100 ? '00' + alt : alt < 1000 ? '0' + alt : '' + alt;
          altitudeCounter.textContent = formatted;
        }
        if (aboveField) {
          aboveField.setCell(40 - self.progress * 20);
        }
      }
    });

    /* H. CHAPTER 03: PINNED 4-INSTRUCTION STEPPER */
    const steps = document.querySelectorAll('.step');
    const activeStepName = document.getElementById('active-step-name');
    const stepLabels = [
      'INSTRUCTION 01 // DISPATCH',
      'INSTRUCTION 02 // CONSENSUS',
      'INSTRUCTION 03 // COMMITMENT',
      'INSTRUCTION 04 // SETTLE & BURN'
    ];

    // Mini-matrix step canvas
    const ruleCanvas = document.getElementById('rule-canvas');
    let ruleCtx = ruleCanvas ? ruleCanvas.getContext('2d') : null;
    let currentStepIndex = 0;

    function drawRuleVisual(stepIdx, frac) {
      if (!ruleCanvas || !ruleCtx) return;
      ruleCanvas.width = ruleCanvas.offsetWidth;
      ruleCanvas.height = ruleCanvas.offsetHeight;
      const w = ruleCanvas.width;
      const h = ruleCanvas.height;
      const cx = w / 2;
      const cy = h / 2;

      ruleCtx.fillStyle = '#050508';
      ruleCtx.fillRect(0, 0, w, h);

      if (stepIdx === 0) {
        // Step 1: Dispatch routing particles
        ruleCtx.strokeStyle = 'rgba(255, 36, 36, 0.4)';
        ruleCtx.lineWidth = 1;
        for (let i = 0; i < 20; i++) {
          const rad = (i / 20) * Math.PI * 2 + frac * 2;
          ruleCtx.beginPath();
          ruleCtx.moveTo(cx, cy);
          ruleCtx.lineTo(cx + Math.cos(rad) * (w * 0.4), cy + Math.sin(rad) * (h * 0.4));
          ruleCtx.stroke();
        }
        ruleCtx.fillStyle = '#FF292C';
        ruleCtx.beginPath();
        ruleCtx.arc(cx, cy, 6, 0, Math.PI * 2);
        ruleCtx.fill();
      } else if (stepIdx === 1) {
        // Step 2: Consensus Quorum Rings
        ruleCtx.strokeStyle = 'rgba(255, 36, 36, 0.7)';
        ruleCtx.lineWidth = 1.5;
        for (let r = 1; r <= 4; r++) {
          ruleCtx.beginPath();
          ruleCtx.arc(cx, cy, r * 28 + (frac * 12), 0, Math.PI * 2);
          ruleCtx.stroke();
        }
        for (let i = 0; i < 16; i++) {
          const ang = (i / 16) * Math.PI * 2;
          ruleCtx.fillStyle = i % 2 === 0 ? '#FFFFFF' : '#FF292C';
          ruleCtx.beginPath();
          ruleCtx.arc(cx + Math.cos(ang) * 84, cy + Math.sin(ang) * 84, 4, 0, Math.PI * 2);
          ruleCtx.fill();
        }
      } else if (stepIdx === 2) {
        // Step 3: Commitment ZK Polynomial Curve
        ruleCtx.strokeStyle = '#FFFFFF';
        ruleCtx.lineWidth = 2;
        ruleCtx.beginPath();
        for (let x = 0; x < w; x += 4) {
          const y = cy + Math.sin((x / 30) + frac * 4) * 40 * Math.cos(x / 60);
          if (x === 0) ruleCtx.moveTo(x, y);
          else ruleCtx.lineTo(x, y);
        }
        ruleCtx.stroke();
        ruleCtx.fillStyle = '#FF292C';
        ruleCtx.fillText("KZG_OPENING_PROOF // VERIFIED", 16, 24);
      } else {
        // Step 4: Settle & Burn Flare
        ruleCtx.fillStyle = 'rgba(255, 36, 36, 0.15)';
        ruleCtx.beginPath();
        ruleCtx.arc(cx, cy, 70 + Math.sin(frac * 8) * 15, 0, Math.PI * 2);
        ruleCtx.fill();
        ruleCtx.strokeStyle = '#FF292C';
        ruleCtx.lineWidth = 2;
        ruleCtx.stroke();
        ruleCtx.fillStyle = '#FFFFFF';
        ruleCtx.font = '700 12px "Obel Mono", monospace';
        ruleCtx.textAlign = 'center';
        ruleCtx.fillText("100% LP BURNED TO INCINERATOR", cx, cy + 4);
      }
    }

    ScrollTrigger.create({
      trigger: '.rule',
      start: 'top top',
      end: '+=250%',
      pin: '.rule__pin',
      scrub: true,
      onUpdate: (self) => {
        const raw = self.progress * 3.99;
        const idx = Math.min(3, Math.floor(raw));
        currentStepIndex = idx;
        const currentFrac = raw - idx;

        steps.forEach((st, i) => {
          st.classList.toggle('is-active', i === idx);
          st.classList.toggle('is-done', raw > i + 1);
          const bar = st.querySelector('.step__bar i');
          if (bar) {
            const frac = Math.min(1, Math.max(0, raw - i));
            bar.style.transform = `scaleX(${frac})`;
          }
        });

        if (activeStepName) activeStepName.textContent = stepLabels[idx];
        drawRuleVisual(idx, currentFrac);
      }
    });

    /* I. CHAPTER 04: PINNED HORIZONTAL RAIL */
    const pairsTrack = document.getElementById('pairs-track');
    if (pairsTrack) {
      const getScrollDist = () => pairsTrack.scrollWidth - window.innerWidth + 200;
      
      const horizTl = gsap.to(pairsTrack, {
        x: () => -getScrollDist(),
        ease: 'none',
        scrollTrigger: {
          trigger: '.pairs-section',
          start: 'top top',
          end: () => '+=' + getScrollDist(),
          pin: true,
          scrub: 0.8,
          invalidateOnRefresh: true
        }
      });

      // 3D card tilt & parallax during horizontal glide
      document.querySelectorAll('.pair-card').forEach((card) => {
        gsap.fromTo(card, 
          { y: 35, rotate: 1.5 },
          {
            y: -35,
            rotate: -1.5,
            ease: 'none',
            scrollTrigger: {
              trigger: card,
              containerAnimation: horizTl,
              start: 'left right',
              end: 'right left',
              scrub: true
            }
          }
        );
      });
    }

    /* J. CHAPTER 05: MATHEMATICAL INVARIANTS ANIMATION */
    gsap.from('.invariant-card', {
      scrollTrigger: {
        trigger: '.invariants',
        start: 'top 75%',
        end: 'top 30%',
        scrub: 0.5
      },
      y: 35,
      opacity: 0.4,
      stagger: 0.15
    });

    /* K. CHAPTER 06: PINNED EXPANDING SCHEMATIC FILM */
    gsap.timeline({
      scrollTrigger: {
        trigger: '.film-section',
        start: 'top top',
        end: '+=140%',
        pin: true,
        scrub: 0.6
      }
    }).fromTo('#film-clip', 
      { clipPath: 'inset(32% 38% 32% 38%)' }, 
      { clipPath: 'inset(0% 0% 0% 0%)', ease: 'power2.inOut' }
    );

    // Official logo & schematic wireframe on film canvas
    const filmCanvas = document.getElementById('film-canvas');
    if (filmCanvas) {
      const fctx = filmCanvas.getContext('2d');
      const logoImg = new Image();
      logoImg.src = 'assets/official_logo_mark.jpg';

      function drawFilmCanvas() {
        filmCanvas.width = window.innerWidth;
        filmCanvas.height = window.innerHeight;
        fctx.fillStyle = '#030305';
        fctx.fillRect(0, 0, filmCanvas.width, filmCanvas.height);
        
        const cx = filmCanvas.width / 2;
        const cy = filmCanvas.height / 2;

        // Render official logo mark centered
        if (logoImg.complete && logoImg.naturalWidth > 0) {
          const aspect = logoImg.naturalWidth / logoImg.naturalHeight;
          const targetH = Math.min(filmCanvas.height * 0.72, 540);
          const targetW = targetH * aspect;
          fctx.drawImage(logoImg, cx - targetW / 2, cy - targetH / 2, targetW, targetH);
        }

        // Concentric geometric hyperbolic ellipses
        fctx.strokeStyle = 'rgba(255, 36, 36, 0.45)';
        fctx.lineWidth = 1.2;
        for (let i = 1; i <= 14; i++) {
          const r = i * 26;
          fctx.beginPath();
          fctx.ellipse(cx, cy, r * 1.6, r * 0.8, 0, 0, Math.PI * 2);
          fctx.stroke();
        }

        // Crosshairs & telemetry marks
        fctx.strokeStyle = 'rgba(255, 255, 255, 0.18)';
        fctx.beginPath();
        fctx.moveTo(cx - 300, cy); fctx.lineTo(cx + 300, cy);
        fctx.moveTo(cx, cy - 200); fctx.lineTo(cx, cy + 200);
        fctx.stroke();
      }

      logoImg.onload = drawFilmCanvas;
      drawFilmCanvas();
      window.addEventListener('resize', drawFilmCanvas);
    }

    /* L. CHAPTER 07: PLAYGROUND CONTROLS */
    const kSlider = document.getElementById('k-slider');
    const kOut = document.getElementById('k-out');
    if (kSlider) {
      kSlider.addEventListener('input', (e) => {
        kOut.textContent = e.target.value;
      });
    }

    const resSlider = document.getElementById('res-slider');
    const resOut = document.getElementById('res-out');
    if (resSlider) {
      resSlider.addEventListener('input', (e) => {
        resOut.textContent = e.target.value;
        if (playField) playField.setCell(e.target.value);
      });
    }

    const speedSlider = document.getElementById('speed-slider');
    const speedOut = document.getElementById('speed-out');
    if (speedSlider) {
      speedSlider.addEventListener('input', (e) => {
        speedOut.textContent = e.target.value;
        if (playField) playField.speed = parseFloat(e.target.value);
      });
    }

    // Charset switchers
    const modeOut = document.getElementById('mode-out');
    document.querySelectorAll('.play__charset-btn').forEach(btn => {
      btn.addEventListener('click', function() {
        document.querySelectorAll('.play__charset-btn').forEach(b => b.classList.remove('active'));
        this.classList.add('active');
        const m = this.getAttribute('data-mode');
        currentMode = m;
        if (playField) playField.mode = m;
        if (heroField) heroField.mode = m;
        if (aboveField) aboveField.mode = m;
        if (modeOut && MODES[m]) modeOut.textContent = MODES[m].label;
        document.documentElement.style.setProperty('--t', MODES[m].tc);
      });
    });

    // Pause / Play
    const btnPause = document.getElementById('btn-pause');
    if (btnPause) {
      btnPause.addEventListener('click', () => {
        if (playField) {
          playField.paused = !playField.paused;
          btnPause.textContent = playField.paused ? 'PLAY' : 'PAUSE';
        }
      });
    }

    // Random Seed
    const btnRandom = document.getElementById('btn-random');
    if (btnRandom) {
      btnRandom.addEventListener('click', () => {
        Noise.seed(Math.floor(Math.random() * 100000));
      });
    }

    // Export PNG
    const btnSavePng = document.getElementById('btn-save-png');
    if (btnSavePng && playCanvas) {
      btnSavePng.addEventListener('click', () => {
        const link = document.createElement('a');
        link.download = '33rd-tree-labs-tensor-matrix.png';
        link.href = playCanvas.toDataURL('image/png');
        link.click();
      });
    }

    /* M. WORDS READING ILLUMINATION ([data-words]) */
    document.querySelectorAll('[data-words]').forEach((el) => {
      const words = el.textContent.trim().split(/\\s+/);
      el.innerHTML = words.map(w => `<span class="word" style="opacity: 0.22;">${w}</span>`).join(' ');
      gsap.fromTo(el.querySelectorAll('.word'), 
        { opacity: 0.22 },
        {
          opacity: 1,
          ease: 'none',
          stagger: 0.08,
          scrollTrigger: {
            trigger: el,
            start: 'top 82%',
            end: 'bottom 50%',
            scrub: true
          }
        }
      );
    });

    /* N. SMOOTH SCROLL ANCHORS */
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', function(e) {
        const id = this.getAttribute('href');
        if (id && id !== '#') {
          const el = document.querySelector(id);
          if (el) {
            e.preventDefault();
            lenis.scrollTo(id === '#top' ? 0 : el, { duration: 1.2 });
          }
        }
      });
    });

    // VRTL WRLD Glitch Letters & Matrix Scramble Engine (Calibrated Deliberate Rate)
    class GlitchScramble {
      constructor(el) {
        this.el = el;
        this.chars = '01X_/*+-[]#';
        this.originalText = el.getAttribute('data-glitch-text') || el.innerText.trim();
        el.setAttribute('data-glitch-text', this.originalText);
        this.isGlitching = false;
        this.animId = null;
        this.lastTickTime = 0;
        this.tickInterval = 250; // 160ms throttle: calm, deliberate, readable (~6fps)
      }

      scramble(duration = 3.5) {
        if (this.isGlitching) return;
        this.isGlitching = true;
        this.el.classList.add('glitch-active');
        const target = this.originalText;
        const len = target.length;
        const startTime = performance.now();
        const durationMs = duration * 1000;
        let activeGlyphs = new Array(len);
        for (let i = 0; i < len; i++) {
          const ch = target[i];
          activeGlyphs[i] = (ch === ' ' || ch === '
' || ch === '	')
            ? ch
            : this.chars[Math.floor(Math.random() * this.chars.length)];
        }

        const tick = (now) => {
          const elapsed = now - startTime;
          const progress = Math.min(1, elapsed / durationMs);
          const revealedCount = Math.floor(progress * len);

          if (now - this.lastTickTime > this.tickInterval) {
            this.lastTickTime = now;
            for (let i = revealedCount; i < len; i++) {
              const ch = target[i];
              if (ch === ' ' || ch === '
' || ch === '	') {
                activeGlyphs[i] = ch;
              } else if (Math.random() < 0.4) {
                activeGlyphs[i] = this.chars[Math.floor(Math.random() * this.chars.length)];
              }
            }
          }

          let result = '';
          for (let i = 0; i < len; i++) {
            const ch = target[i];
            if (ch === ' ' || ch === '
' || ch === '	') {
              result += ch;
            } else if (i < revealedCount) {
              result += ch;
            } else {
              result += activeGlyphs[i] || ch;
            }
          }
          this.el.innerText = result;

          if (progress < 1) {
            this.animId = requestAnimationFrame(tick);
          } else {
            this.el.innerText = target;
            this.el.classList.remove('glitch-active');
            this.isGlitching = false;
          }
        };
        this.animId = requestAnimationFrame(tick);
      }
    }

    document.querySelectorAll('[data-glitch], .nav-link').forEach(el => {
      const inst = new GlitchScramble(el);
      el.addEventListener('mouseenter', () => inst.scramble(3.5));
    });

  </script>
</body>
</html>
"""

output_path = "/Users/ianmora/Desktop/Projects/33rd-tree-labs-site/index.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_template)

print(f"Master story scroll successfully generated at {output_path} ({len(html_template)} bytes)")
