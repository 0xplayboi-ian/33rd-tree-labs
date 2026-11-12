import os

script_dir = "/Users/ianmora/Desktop/Projects/33rd-tree-labs-site"
output_file = os.path.join(script_dir, "index.html")

html_code = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>33RD TREE LABS // The Singularity Protocol &bull; 33rdtreelabs.tech</title>
    <meta name="description" content="A Byzantine-Resilient Verifiable DePIN Compute Fabric on Solana. Hierarchical Tensor Arbor coordination, zero-knowledge neural evaluations, and cryptographic consensus at scale.">

    <!-- OpenGraph & Twitter Metadata -->
    <meta property="og:title" content="33RD TREE LABS // The Singularity Protocol">
    <meta property="og:description" content="A Byzantine-Resilient Verifiable DePIN Compute Fabric on Solana. Pairing cryptographic consensus with zero-knowledge neural evaluations.">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://33rdtreelabs.tech/">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="33RD TREE LABS // 33rdtreelabs.tech">
    <meta name="twitter:description" content="Decentralized verifiable GPU compute orchestration anchored on Solana.">

    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous">
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@0,300;0,400;0,500;0,700;1,400&family=Space+Grotesk:wght@300;400;500;600;700&family=Syne:wght@700;800&display=swap" rel="stylesheet">

    <!-- Lenis Smooth Scroll & GSAP ScrollTrigger -->
    <script src="https://cdn.jsdelivr.net/npm/@studio-freight/lenis@1.0.42/dist/lenis.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>

    <style>
        :root {
            /* VRTL WRLD DESIGN SYSTEM PALETTE */
            --bg: #070707;
            --bg-elevated: #0B0B0E;
            --bg-card: #101014;
            --bg-card-hover: #15151B;
            --border: #1C1C24;
            --border-hover: #343442;
            --border-accent: rgba(255, 41, 44, 0.35);
            --laser-red: #FF292C;
            --laser-orange: #FF462D;
            --laser-glow: rgba(255, 41, 44, 0.45);
            --laser-subtle: rgba(255, 41, 44, 0.08);
            --chalk: #ECECEC;
            --chalk-dim: #D4D4DC;
            --slate: #8E8E98;
            --dark-slate: #4A4A56;
            --white: #FFFFFF;
            --black: #000000;
            --green: #00E676;
            --green-glow: rgba(0, 230, 118, 0.35);
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            cursor: default;
        }

        html {
            background: var(--bg);
            color: var(--chalk);
            font-family: 'Space Grotesk', -apple-system, BlinkMacSystemFont, sans-serif;
            overflow-x: hidden;
        }

        /* LENIS SMOOTH SCROLL INTEGRATION */
        html.lenis, html.lenis body {
            height: auto;
        }
        .lenis.lenis-smooth {
            scroll-behavior: auto !important;
        }
        .lenis.lenis-smooth [data-lenis-prevent] {
            overscroll-behavior: contain;
        }
        .lenis.lenis-stopped {
            overflow: hidden;
        }
        .lenis.lenis-scrolling iframe {
            pointer-events: none;
        }

        body {
            background: var(--bg);
            min-height: 100vh;
            position: relative;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
            overflow-x: hidden;
        }

        ::selection {
            background: var(--laser-red);
            color: var(--white);
        }

        /* CUSTOM RETRO-TECH CURSOR */
        #cursor-dot {
            width: 6px;
            height: 6px;
            background: var(--laser-red);
            border-radius: 50%;
            position: fixed;
            pointer-events: none;
            z-index: 9999;
            transform: translate(-50%, -50%);
            box-shadow: 0 0 12px var(--laser-red);
            transition: opacity 0.15s ease;
        }
        #cursor-ring {
            width: 32px;
            height: 32px;
            border: 1px solid rgba(255, 41, 44, 0.5);
            border-radius: 50%;
            position: fixed;
            pointer-events: none;
            z-index: 9998;
            transform: translate(-50%, -50%);
            transition: width 0.18s ease, height 0.18s ease, border-color 0.18s ease, transform 0.08s ease-out;
        }
        body.cursor-hover #cursor-ring {
            width: 50px;
            height: 50px;
            border-color: var(--laser-red);
            background: rgba(255, 41, 44, 0.08);
        }

        /* FLOATING PILL NAVBAR */
        .nav-wrapper {
            position: fixed;
            top: 20px;
            left: 0;
            right: 0;
            display: flex;
            justify-content: center;
            z-index: 1000;
            padding: 0 16px;
        }

        .nav-pill {
            display: flex;
            align-items: center;
            gap: 22px;
            background: rgba(11, 11, 14, 0.90);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid var(--border);
            padding: 8px 14px 8px 18px;
            border-radius: 9999px;
            box-shadow: 0 14px 34px rgba(0, 0, 0, 0.7), 0 0 0 1px rgba(255, 255, 255, 0.05);
            transition: border-color 0.25s ease, box-shadow 0.25s ease;
        }
        .nav-pill:hover {
            border-color: rgba(255, 41, 44, 0.35);
            box-shadow: 0 16px 40px rgba(0, 0, 0, 0.8), 0 0 20px rgba(255, 41, 44, 0.15);
        }

        .nav-brand {
            display: flex;
            align-items: center;
            gap: 10px;
            text-decoration: none;
            color: var(--white);
        }
        .nav-logo-box {
            width: 26px;
            height: 26px;
            border-radius: 50%;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            background: #000;
            border: 1px solid rgba(255, 255, 255, 0.15);
            flex-shrink: 0;
        }
        .nav-logo-box img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            filter: grayscale(100%) contrast(150%);
            transition: filter 0.25s ease;
        }
        .nav-brand:hover .nav-logo-box img {
            filter: grayscale(0%) contrast(120%);
        }
        .nav-title {
            font-family: 'JetBrains Mono', monospace;
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 0.12em;
            color: var(--white);
            white-space: nowrap;
        }

        .nav-links {
            display: flex;
            align-items: center;
            gap: 16px;
        }
        .nav-link {
            font-family: 'JetBrains Mono', monospace;
            font-size: 10.5px;
            font-weight: 500;
            letter-spacing: 0.08em;
            color: var(--slate);
            text-decoration: none;
            transition: color 0.2s ease;
            position: relative;
            padding: 4px 2px;
        }
        .nav-link:hover {
            color: var(--white);
        }
        .nav-link::after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            width: 0%;
            height: 1px;
            background: var(--laser-red);
            transition: width 0.2s ease;
        }
        .nav-link:hover::after {
            width: 100%;
        }
        .nav-link.active {
            color: var(--chalk) !important;
            text-shadow: 0 0 10px rgba(255, 41, 44, 0.45);
        }
        .nav-link.active::after {
            width: 100% !important;
            background: var(--laser-red);
            box-shadow: 0 0 8px var(--laser-red);
        }

        .nav-status {
            display: flex;
            align-items: center;
            gap: 6px;
            padding: 4px 10px;
            background: rgba(255, 41, 44, 0.08);
            border: 1px solid rgba(255, 41, 44, 0.22);
            border-radius: 9999px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 9.5px;
            color: var(--white);
            letter-spacing: 0.08em;
        }
        .nav-status-dot {
            width: 6px;
            height: 6px;
            background: var(--laser-red);
            border-radius: 50%;
            box-shadow: 0 0 8px var(--laser-red);
            animation: pulseDot 1.8s infinite;
        }
        @keyframes pulseDot {
            0%, 100% { opacity: 1; transform: scale(1); }
            50% { opacity: 0.4; transform: scale(0.85); }
        }

        .nav-cta {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: var(--laser-red);
            color: var(--white);
            font-family: 'JetBrains Mono', monospace;
            font-size: 10.5px;
            font-weight: 700;
            letter-spacing: 0.08em;
            text-decoration: none;
            padding: 7px 16px;
            border-radius: 9999px;
            box-shadow: 0 0 16px var(--laser-glow);
            transition: transform 0.2s ease, box-shadow 0.2s ease, background 0.2s ease;
        }
        .nav-cta:hover {
            transform: translateY(-1px);
            box-shadow: 0 0 24px var(--laser-red);
            background: #FF4245;
        }

        /* -------------------------------------------------------------
           SEAMLESS SECTION THEME MORPHING SYSTEM (VRTL WRLD SIGNATURE)
           ------------------------------------------------------------- */
        .theme-section {
            position: relative;
            width: 100%;
            transition: background-color 0.6s cubic-bezier(0.16, 1, 0.3, 1), color 0.6s ease;
        }

        /* THEME 1: HERO (LIGHT CHALK THEME #ECECEC / #F0F0F2) */
        .theme-chalk {
            background-color: #ECECEC;
            color: #0A0A0C;
            background-image: 
                radial-gradient(circle at 50% 0%, rgba(255, 41, 44, 0.05) 0%, transparent 60%),
                linear-gradient(rgba(0, 0, 0, 0.035) 1px, transparent 1px),
                linear-gradient(90deg, rgba(0, 0, 0, 0.035) 1px, transparent 1px);
            background-size: 100% 100%, 40px 40px, 40px 40px;
        }
        .theme-chalk .meta-tag {
            color: var(--laser-red);
        }
        .theme-chalk .meta-tag::before {
            background: var(--laser-red);
        }
        .theme-chalk .display-word {
            color: #0A0A0C;
        }
        .theme-chalk .display-word.red-accent {
            color: var(--laser-red);
            text-shadow: 0 0 35px rgba(255, 41, 44, 0.35);
        }
        .theme-chalk .hero-desc {
            color: #4A4A56;
        }
        .theme-chalk .hero-desc strong {
            color: #0A0A0C;
        }
        .theme-chalk .btn-brutal-outline {
            border-color: rgba(10, 10, 12, 0.28);
            color: #0A0A0C;
        }
        .theme-chalk .btn-brutal-outline:hover {
            border-color: var(--laser-red);
            color: var(--white);
            background: var(--laser-red);
        }

        /* THEME 2: SINGULARITY STAGE (DEEP OBSIDIAN BLACK #070707) */
        .theme-obsidian {
            background-color: #070707;
            color: var(--chalk);
            background-image: 
                radial-gradient(circle at 50% 50%, rgba(255, 41, 44, 0.05) 0%, transparent 70%),
                linear-gradient(rgba(255, 255, 255, 0.018) 1px, transparent 1px),
                linear-gradient(90deg, rgba(255, 255, 255, 0.018) 1px, transparent 1px);
            background-size: 100% 100%, 44px 44px, 44px 44px;
        }

        /* THEME 3: ARCHITECTURE (ELECTRIC RED FULL-BLEED TAKEOVER #FF292C) */
        .theme-electric-red {
            background-color: #FF292C !important;
            color: #000000 !important;
            background-image: 
                linear-gradient(rgba(0, 0, 0, 0.04) 1px, transparent 1px),
                linear-gradient(90deg, rgba(0, 0, 0, 0.04) 1px, transparent 1px);
            background-size: 40px 40px, 40px 40px;
        }
        .theme-electric-red .meta-tag {
            color: #000000 !important;
        }
        .theme-electric-red .meta-tag::before {
            background: #000000 !important;
        }
        .theme-electric-red .section-title {
            color: #000000 !important;
        }
        .theme-electric-red .section-desc {
            color: #1A1A1A !important;
            font-weight: 500;
        }

        /* 4-COLUMN TECH CARDS ON RED TAKEOVER */
        .theme-electric-red .arch-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 20px;
            margin-top: 48px;
        }
        @media (max-width: 1100px) {
            .theme-electric-red .arch-grid {
                grid-template-columns: repeat(2, 1fr);
            }
        }
        @media (max-width: 650px) {
            .theme-electric-red .arch-grid {
                grid-template-columns: 1fr;
            }
        }
        .theme-electric-red .arch-card {
            background: #0B0B0E !important;
            border: 1px solid rgba(0, 0, 0, 0.25) !important;
            color: var(--chalk);
            box-shadow: 0 16px 40px rgba(0, 0, 0, 0.25);
        }
        .theme-electric-red .arch-card:hover {
            border-color: rgba(255, 255, 255, 0.3) !important;
            transform: translateY(-4px);
            background: #111116 !important;
            box-shadow: 0 24px 50px rgba(0, 0, 0, 0.4);
        }
        .theme-electric-red .card-heading {
            color: #FFFFFF !important;
        }
        .theme-electric-red .card-text {
            color: #9E9EA8 !important;
        }
        .theme-electric-red .card-number {
            color: #FF292C !important;
        }
        .theme-electric-red .card-badge {
            border-color: #262630 !important;
            color: #FFFFFF !important;
            background: rgba(255, 255, 255, 0.05);
        }
        .theme-electric-red .card-footer-metrics {
            border-top: 1px solid #1C1C24 !important;
        }
        .theme-electric-red .card-metric-pill {
            background: rgba(255, 255, 255, 0.05) !important;
            border: 1px solid rgba(255, 255, 255, 0.08) !important;
            color: #D4D4DC !important;
        }

        /* THEME 4: PHILOSOPHY / CONSOLE (STARK WHITE / CHALK #F4F4F6) */
        .theme-chalk-2 {
            background-color: #F4F4F6;
            color: #0A0A0C;
            background-image: 
                radial-gradient(circle at 50% 0%, rgba(255, 41, 44, 0.04) 0%, transparent 60%),
                linear-gradient(rgba(0, 0, 0, 0.035) 1px, transparent 1px),
                linear-gradient(90deg, rgba(0, 0, 0, 0.035) 1px, transparent 1px);
            background-size: 100% 100%, 40px 40px, 40px 40px;
        }
        .theme-chalk-2 .section-title {
            color: #0A0A0C;
        }
        .theme-chalk-2 .section-desc {
            color: #4A4A56;
        }

        /* THEME 5: FOOTER & PROTOCOL ACCESS (DEEP OBSIDIAN BLACK #050507) */
        .theme-deep-obsidian {
            background-color: #050507;
            color: var(--chalk);
            background-image: 
                radial-gradient(circle at 50% 20%, rgba(255, 41, 44, 0.08) 0%, transparent 60%),
                linear-gradient(rgba(255, 255, 255, 0.015) 1px, transparent 1px),
                linear-gradient(90deg, rgba(255, 255, 255, 0.015) 1px, transparent 1px);
            background-size: 100% 100%, 44px 44px, 44px 44px;
        }

        /* -------------------------------------------------------------
           SCATTERED RECTANGULAR WIPE TILES (VRTL WRLD SIGNATURE)
           ------------------------------------------------------------- */
        .wipe-tile-scatter-wrap {
            position: relative;
            width: 100%;
            height: 140px;
            overflow: hidden;
            pointer-events: none;
            z-index: 10;
        }
        .scatter-tile {
            position: absolute;
            background: var(--laser-red);
            box-shadow: 0 0 16px rgba(255, 41, 44, 0.4);
            will-change: transform, opacity;
            border-radius: 1px;
        }
        .scatter-tile.alt {
            background: var(--laser-orange);
            box-shadow: 0 0 16px rgba(255, 70, 45, 0.4);
        }

        /* SECTION WRAPPER */
        .section-wrap {
            max-width: 1320px;
            margin: 0 auto;
            padding: 90px 24px;
            position: relative;
        }

        .meta-tag {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 10.5px;
            font-weight: 500;
            letter-spacing: 0.18em;
            color: var(--laser-red);
            text-transform: uppercase;
            margin-bottom: 16px;
        }
        .meta-tag::before {
            content: '';
            width: 8px;
            height: 8px;
            background: var(--laser-red);
            clip-path: polygon(0 0, 100% 0, 100% 100%);
        }

        .section-title {
            font-family: 'Syne', sans-serif;
            font-size: clamp(32px, 4.5vw, 54px);
            font-weight: 800;
            line-height: 1.05;
            letter-spacing: -0.02em;
            color: var(--chalk);
            text-transform: uppercase;
            margin-bottom: 18px;
        }

        .section-desc {
            font-size: 15px;
            line-height: 1.65;
            color: var(--slate);
            max-width: 680px;
            font-weight: 400;
        }

        /* HERO SECTION */
        .hero {
            min-height: 100vh;
            display: flex;
            align-items: center;
            padding-top: 130px;
            padding-bottom: 60px;
            position: relative;
        }

        .hero-inner {
            max-width: 1360px;
            margin: 0 auto;
            padding: 0 24px;
            display: grid;
            grid-template-columns: 1.15fr 0.85fr;
            gap: 48px;
            align-items: center;
            width: 100%;
        }

        .hero-left {
            display: flex;
            flex-direction: column;
            z-index: 2;
        }

        .hero-split-words {
            display: flex;
            flex-direction: column;
            gap: 2px;
            margin-bottom: 28px;
        }
        .hero-word-row {
            display: flex;
            align-items: baseline;
            gap: 18px;
            flex-wrap: wrap;
        }
        .display-word {
            font-family: 'Syne', sans-serif;
            font-size: clamp(48px, 6.2vw, 88px);
            font-weight: 800;
            line-height: 0.92;
            letter-spacing: -0.04em;
            color: var(--chalk);
            text-transform: uppercase;
            transition: color 0.3s ease;
            display: inline-block;
        }
        .display-word.red-accent {
            color: var(--laser-red);
            text-shadow: 0 0 40px rgba(255, 41, 44, 0.45);
        }

        .hero-desc {
            font-size: 16px;
            line-height: 1.65;
            color: var(--slate);
            max-width: 580px;
            margin-bottom: 34px;
        }
        .hero-desc strong {
            color: var(--chalk);
            font-weight: 500;
        }

        .hero-actions {
            display: flex;
            align-items: center;
            gap: 16px;
            flex-wrap: wrap;
        }

        .btn-brutal-red {
            display: inline-flex;
            align-items: center;
            gap: 10px;
            background: var(--laser-red);
            color: var(--white);
            font-family: 'JetBrains Mono', monospace;
            font-size: 12px;
            font-weight: 700;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            text-decoration: none;
            padding: 14px 26px;
            clip-path: polygon(0 10px, 10px 0, 100% 0, 100% calc(100% - 10px), calc(100% - 10px) 100%, 0 100%);
            box-shadow: 0 0 24px var(--laser-glow);
            transition: transform 0.2s ease, background 0.2s ease, box-shadow 0.2s ease;
        }
        .btn-brutal-red:hover {
            transform: translateY(-2px);
            background: #FF3D40;
            box-shadow: 0 0 36px rgba(255, 41, 44, 0.7);
        }

        .btn-brutal-outline {
            display: inline-flex;
            align-items: center;
            gap: 10px;
            background: transparent;
            color: var(--chalk);
            font-family: 'JetBrains Mono', monospace;
            font-size: 12px;
            font-weight: 600;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            text-decoration: none;
            padding: 13px 24px;
            border: 1px solid var(--border-hover);
            clip-path: polygon(0 10px, 10px 0, 100% 0, 100% calc(100% - 10px), calc(100% - 10px) 100%, 0 100%);
            transition: border-color 0.2s ease, color 0.2s ease, background 0.2s ease;
        }
        .btn-brutal-outline:hover {
            border-color: var(--laser-red);
            color: var(--white);
            background: rgba(255, 41, 44, 0.05);
        }

        /* HARDWARE / MANIFOLD SCHEMATIC SHOWCASE (PINNED EXPANSION CARD) */
        .schematic-box {
            position: relative;
            background: #0D0D12;
            border: 1px solid var(--border);
            clip-path: polygon(0 16px, 16px 0, calc(100% - 16px) 0, 100% 16px, 100% calc(100% - 16px), calc(100% - 16px) 100%, 16px 100%, 0 calc(100% - 16px));
            padding: 2px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.8), 0 0 40px rgba(255, 41, 44, 0.06);
            transition: border-color 0.3s ease, transform 0.2s ease-out;
            transform-origin: center center;
            will-change: transform, box-shadow;
        }
        .schematic-box:hover {
            border-color: rgba(255, 41, 44, 0.45);
        }

        .schematic-inner {
            background: #09090C;
            padding: 24px;
            clip-path: polygon(0 14px, 14px 0, calc(100% - 14px) 0, 100% 14px, 100% calc(100% - 14px), calc(100% - 14px) 100%, 14px 100%, 0 calc(100% - 14px));
            position: relative;
            overflow: hidden;
        }

        .schematic-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid var(--border);
            padding-bottom: 12px;
            margin-bottom: 16px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 10px;
            letter-spacing: 0.1em;
            color: var(--slate);
        }
        .schematic-header .status-tag {
            color: var(--green);
            display: flex;
            align-items: center;
            gap: 6px;
        }
        .schematic-header .status-tag::before {
            content: '';
            width: 6px;
            height: 6px;
            background: var(--green);
            border-radius: 50%;
            box-shadow: 0 0 6px var(--green);
        }

        .schematic-canvas-wrap {
            position: relative;
            width: 100%;
            height: 380px;
        }
        #schematic-canvas {
            width: 100%;
            height: 100%;
            display: block;
        }

        .schematic-telemetry {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 12px;
            margin-top: 18px;
            border-top: 1px solid var(--border);
            padding-top: 16px;
        }
        .tele-stat {
            display: flex;
            flex-direction: column;
            gap: 3px;
        }
        .tele-label {
            font-family: 'JetBrains Mono', monospace;
            font-size: 9.5px;
            color: var(--slate);
            letter-spacing: 0.08em;
            text-transform: uppercase;
        }
        .tele-val {
            font-family: 'JetBrains Mono', monospace;
            font-size: 13px;
            font-weight: 700;
            color: var(--chalk);
        }
        .tele-val.accent {
            color: var(--laser-red);
        }

        /* HORIZONTAL RUNNING MARQUEE */
        .marquee-section {
            border-top: 1px solid var(--border);
            border-bottom: 1px solid var(--border);
            background: #09090D;
            overflow: hidden;
            white-space: nowrap;
            padding: 14px 0;
            display: flex;
            position: relative;
        }
        .marquee-track {
            display: flex;
            gap: 40px;
            animation: marquee 35s linear infinite;
            will-change: transform;
        }
        .marquee-track:hover {
            animation-play-state: paused;
        }
        @keyframes marquee {
            0% { transform: translateX(0); }
            100% { transform: translateX(-50%); }
        }

        .marquee-item {
            display: inline-flex;
            align-items: center;
            gap: 10px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 11px;
            letter-spacing: 0.1em;
            color: var(--slate);
            text-transform: uppercase;
        }
        .marquee-item span.highlight {
            color: var(--chalk);
            font-weight: 700;
        }
        .marquee-item span.red {
            color: var(--laser-red);
            font-weight: 700;
        }
        .marquee-bullet {
            color: var(--laser-red);
            font-size: 9px;
        }

        /* SECTION 2: SINGULARITY STAGE TELEMETRY GRID */
        .stage-stats-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 20px;
            margin-top: 36px;
        }
        @media (max-width: 900px) {
            .stage-stats-grid {
                grid-template-columns: repeat(2, 1fr);
            }
        }
        @media (max-width: 500px) {
            .stage-stats-grid {
                grid-template-columns: 1fr;
            }
        }
        .stage-stat-card {
            background: #0B0B0E;
            border: 1px solid var(--border);
            clip-path: polygon(0 12px, 12px 0, 100% 0, 100% calc(100% - 12px), calc(100% - 12px) 100%, 0 100%);
            padding: 24px 20px;
            transition: all 0.25s ease;
        }
        .stage-stat-card:hover {
            border-color: rgba(255, 41, 44, 0.4);
            transform: translateY(-3px);
            box-shadow: 0 12px 30px rgba(255, 41, 44, 0.08);
        }
        .stage-stat-num {
            font-family: 'Syne', sans-serif;
            font-size: clamp(24px, 2.5vw, 36px);
            font-weight: 800;
            color: var(--white);
            margin-bottom: 6px;
            line-height: 1;
        }
        .stage-stat-num.red {
            color: var(--laser-red);
            text-shadow: 0 0 20px rgba(255, 41, 44, 0.4);
        }
        .stage-stat-lbl {
            font-family: 'JetBrains Mono', monospace;
            font-size: 10px;
            letter-spacing: 0.08em;
            color: var(--slate);
            text-transform: uppercase;
        }

        /* PROTOCOL ARCHITECTURE CARDS */
        .arch-card {
            background: var(--bg-card);
            border: 1px solid var(--border);
            padding: 36px 30px;
            clip-path: polygon(0 16px, 16px 0, 100% 0, 100% calc(100% - 16px), calc(100% - 16px) 100%, 0 100%);
            position: relative;
            transition: border-color 0.25s ease, transform 0.25s ease, background 0.25s ease;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }
        .arch-card:hover {
            border-color: rgba(255, 41, 44, 0.4);
            transform: translateY(-3px);
            background: var(--bg-card-hover);
        }
        .arch-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 40px;
            height: 2px;
            background: var(--laser-red);
            opacity: 0;
            transition: opacity 0.25s ease, width 0.25s ease;
        }
        .arch-card:hover::before {
            opacity: 1;
            width: 90px;
        }

        .card-meta-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
        }
        .card-number {
            font-family: 'JetBrains Mono', monospace;
            font-size: 13px;
            font-weight: 700;
            color: var(--laser-red);
            letter-spacing: 0.12em;
        }
        .card-badge {
            font-family: 'JetBrains Mono', monospace;
            font-size: 9.5px;
            color: var(--slate);
            border: 1px solid var(--border);
            padding: 3px 8px;
            border-radius: 4px;
            letter-spacing: 0.08em;
            text-transform: uppercase;
        }

        .card-heading {
            font-family: 'Syne', sans-serif;
            font-size: 21px;
            font-weight: 700;
            color: var(--chalk);
            margin-bottom: 14px;
            letter-spacing: -0.01em;
            line-height: 1.2;
        }
        .card-text {
            font-size: 13.5px;
            line-height: 1.65;
            color: var(--slate);
            margin-bottom: 24px;
        }

        .card-footer-metrics {
            border-top: 1px solid var(--border);
            padding-top: 16px;
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
        }
        .card-metric-pill {
            font-family: 'JetBrains Mono', monospace;
            font-size: 9.5px;
            color: var(--chalk-dim);
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.05);
            padding: 4px 8px;
            border-radius: 4px;
        }
        .card-metric-pill strong {
            color: var(--laser-red);
        }

        /* BYZANTINE SIMULATOR & TERMINAL */
        .sim-grid {
            display: grid;
            grid-template-columns: 1.05fr 0.95fr;
            gap: 28px;
            margin-top: 48px;
        }
        @media (max-width: 1024px) {
            .sim-grid {
                grid-template-columns: 1fr;
            }
        }

        .sim-box {
            background: #0B0B0F;
            border: 1px solid var(--border);
            clip-path: polygon(0 16px, 16px 0, 100% 0, 100% calc(100% - 16px), calc(100% - 16px) 100%, 0 100%);
            padding: 28px;
            display: flex;
            flex-direction: column;
            gap: 20px;
            box-shadow: 0 16px 40px rgba(0, 0, 0, 0.4);
        }
        .sim-box-title {
            font-family: 'JetBrains Mono', monospace;
            font-size: 11px;
            letter-spacing: 0.12em;
            color: var(--laser-red);
            text-transform: uppercase;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .node-lattice {
            display: grid;
            grid-template-columns: repeat(8, 1fr);
            gap: 8px;
            padding: 18px;
            background: #08080B;
            border: 1px solid var(--border);
            border-radius: 4px;
        }
        .node-tile {
            aspect-ratio: 1;
            background: #14141A;
            border: 1px solid rgba(255, 255, 255, 0.06);
            border-radius: 3px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: 'JetBrains Mono', monospace;
            font-size: 8px;
            color: var(--dark-slate);
            transition: all 0.25s ease;
            position: relative;
        }
        .node-tile.honest {
            background: rgba(0, 230, 118, 0.08);
            border-color: rgba(0, 230, 118, 0.3);
            color: var(--green);
        }
        .node-tile.byzantine {
            background: rgba(255, 41, 44, 0.2);
            border-color: var(--laser-red);
            color: var(--white);
            box-shadow: 0 0 10px rgba(255, 41, 44, 0.6);
            transform: scale(1.08);
            z-index: 2;
        }
        .node-tile.slashed {
            background: #240a0b;
            border-color: #551214;
            color: #882226;
            text-decoration: line-through;
        }

        .sim-controls {
            display: flex;
            flex-direction: column;
            gap: 14px;
        }
        .sim-slider-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-family: 'JetBrains Mono', monospace;
            font-size: 11px;
            color: var(--chalk);
        }
        .sim-range {
            width: 100%;
            height: 4px;
            accent-color: var(--laser-red);
            background: #1C1C26;
            border-radius: 2px;
            margin-top: 8px;
        }

        .sim-attack-select {
            background: #0B0B0E;
            border: 1px solid var(--border);
            color: var(--chalk);
            font-family: 'JetBrains Mono', monospace;
            font-size: 11px;
            padding: 10px 12px;
            border-radius: 4px;
            outline: none;
            width: 100%;
        }
        .sim-attack-select:focus {
            border-color: var(--laser-red);
        }

        .sim-status-banner {
            background: #09090D;
            border: 1px solid var(--border);
            padding: 14px;
            border-radius: 4px;
            display: flex;
            flex-direction: column;
            gap: 6px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 11px;
        }
        .sim-status-head {
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .sim-status-head.success { color: var(--green); }
        .sim-status-head.alert { color: var(--laser-red); }

        /* Terminal Console */
        .terminal-box {
            background: #08080C;
            border: 1px solid var(--border);
            clip-path: polygon(0 16px, 16px 0, 100% 0, 100% calc(100% - 16px), calc(100% - 16px) 100%, 0 100%);
            display: flex;
            flex-direction: column;
            height: 520px;
            box-shadow: 0 16px 40px rgba(0, 0, 0, 0.6);
        }
        .terminal-topbar {
            background: #111116;
            border-bottom: 1px solid var(--border);
            padding: 10px 16px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            font-family: 'JetBrains Mono', monospace;
            font-size: 10.5px;
            color: var(--slate);
        }
        .terminal-dots {
            display: flex;
            gap: 6px;
        }
        .terminal-dot {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: #252530;
        }
        .terminal-dot.red { background: #FF292C; }

        .terminal-output {
            flex: 1;
            padding: 16px;
            overflow-y: auto;
            font-family: 'JetBrains Mono', monospace;
            font-size: 11px;
            line-height: 1.6;
            color: #C0C0C8;
            scrollbar-width: thin;
            scrollbar-color: var(--border) transparent;
        }
        .terminal-output::-webkit-scrollbar {
            width: 4px;
        }
        .terminal-output::-webkit-scrollbar-thumb {
            background: var(--border);
        }

        .terminal-line {
            margin-bottom: 4px;
            word-break: break-all;
        }
        .terminal-line.cmd { color: var(--laser-red); font-weight: 600; }
        .terminal-line.highlight { color: #FFFFFF; font-weight: 600; }
        .terminal-line.success { color: var(--green); }
        .terminal-line.warn { color: #FFB300; }
        .terminal-line.dim { color: var(--slate); }

        .terminal-input-wrap {
            border-top: 1px solid var(--border);
            padding: 10px 14px;
            background: #0E0E12;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .terminal-prompt {
            color: var(--laser-red);
            font-family: 'JetBrains Mono', monospace;
            font-size: 12px;
            font-weight: 700;
        }
        .terminal-input {
            flex: 1;
            background: transparent;
            border: none;
            outline: none;
            color: var(--chalk);
            font-family: 'JetBrains Mono', monospace;
            font-size: 12px;
        }

        .quick-chips {
            display: flex;
            gap: 6px;
            padding: 8px 14px;
            background: #08080C;
            border-top: 1px solid var(--border);
            overflow-x: auto;
        }
        .chip {
            background: #14141B;
            border: 1px solid var(--border);
            padding: 3px 8px;
            border-radius: 3px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 9.5px;
            color: var(--slate);
            cursor: pointer;
            transition: all 0.2s ease;
            white-space: nowrap;
        }
        .chip:hover {
            color: var(--chalk);
            border-color: var(--laser-red);
            background: rgba(255, 41, 44, 0.08);
        }

        /* YIELD CALCULATOR */
        .calc-grid {
            display: grid;
            grid-template-columns: 1.1fr 0.9fr;
            gap: 28px;
            margin-top: 48px;
        }
        @media (max-width: 900px) {
            .calc-grid {
                grid-template-columns: 1fr;
            }
        }

        .calc-panel-left {
            background: #0B0B0F;
            border: 1px solid var(--border);
            clip-path: polygon(0 16px, 16px 0, 100% 0, 100% calc(100% - 16px), calc(100% - 16px) 100%, 0 100%);
            padding: 32px;
            display: flex;
            flex-direction: column;
            gap: 24px;
            box-shadow: 0 16px 40px rgba(0, 0, 0, 0.3);
        }

        .calc-field {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        .calc-label {
            font-family: 'JetBrains Mono', monospace;
            font-size: 11px;
            color: var(--chalk-dim);
            letter-spacing: 0.08em;
            text-transform: uppercase;
            display: flex;
            justify-content: space-between;
        }
        .calc-select {
            background: #09090D;
            border: 1px solid var(--border);
            color: var(--chalk);
            font-family: 'JetBrains Mono', monospace;
            font-size: 11.5px;
            padding: 12px 14px;
            border-radius: 4px;
            outline: none;
            width: 100%;
        }
        .calc-select:focus {
            border-color: var(--laser-red);
        }

        .calc-slider {
            width: 100%;
            height: 6px;
            accent-color: var(--laser-red);
            background: #1C1C26;
            border-radius: 3px;
        }

        .calc-panel-right {
            background: #08080C;
            border: 1px solid var(--border);
            clip-path: polygon(0 16px, 16px 0, 100% 0, 100% calc(100% - 16px), calc(100% - 16px) 100%, 0 100%);
            padding: 32px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            gap: 20px;
            box-shadow: 0 16px 40px rgba(0, 0, 0, 0.3);
        }

        .calc-stat-box {
            display: flex;
            flex-direction: column;
            gap: 18px;
        }
        .calc-metric-row {
            display: flex;
            justify-content: space-between;
            align-items: baseline;
            border-bottom: 1px solid var(--border);
            padding-bottom: 12px;
        }
        .calc-metric-name {
            font-family: 'JetBrains Mono', monospace;
            font-size: 11px;
            color: var(--slate);
            letter-spacing: 0.06em;
            text-transform: uppercase;
        }
        .calc-metric-val {
            font-family: 'JetBrains Mono', monospace;
            font-size: 18px;
            font-weight: 700;
            color: var(--chalk);
        }
        .calc-metric-val.highlight {
            font-size: 32px;
            color: var(--laser-red);
            text-shadow: 0 0 20px rgba(255, 41, 44, 0.4);
        }

        .calc-disclaimer {
            font-family: 'JetBrains Mono', monospace;
            font-size: 9.5px;
            color: var(--dark-slate);
            line-height: 1.5;
            border-top: 1px solid var(--border);
            padding-top: 14px;
        }

        /* SECTION 5: CTA & INTERACTIVE EMAIL PILL */
        .cta-section {
            max-width: 1320px;
            margin: 40px auto 70px;
            padding: 0 24px;
        }
        .cta-box {
            background: linear-gradient(135deg, #101015 0%, #08080A 100%);
            border: 1px solid rgba(255, 41, 44, 0.3);
            clip-path: polygon(0 20px, 20px 0, calc(100% - 20px) 0, 100% 20px, 100% calc(100% - 20px), calc(100% - 20px) 100%, 20px 100%, 0 calc(100% - 20px));
            padding: 60px 40px;
            text-align: center;
            position: relative;
            box-shadow: 0 24px 80px rgba(0, 0, 0, 0.9), 0 0 50px rgba(255, 41, 44, 0.08);
            overflow: hidden;
        }
        .cta-box::before {
            content: '';
            position: absolute;
            top: -50%;
            left: 50%;
            transform: translateX(-50%);
            width: 600px;
            height: 300px;
            background: radial-gradient(circle, rgba(255, 41, 44, 0.12) 0%, transparent 70%);
            pointer-events: none;
        }

        .cta-title {
            font-family: 'Syne', sans-serif;
            font-size: clamp(32px, 4.8vw, 64px);
            font-weight: 800;
            line-height: 1.05;
            letter-spacing: -0.03em;
            color: var(--white);
            text-transform: uppercase;
            margin-bottom: 20px;
        }
        .cta-desc {
            font-size: 16px;
            line-height: 1.6;
            color: var(--slate);
            max-width: 640px;
            margin: 0 auto 36px;
        }
        .cta-buttons {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 18px;
            flex-wrap: wrap;
            margin-bottom: 40px;
        }

        /* SIGNATURE PROTOCOL EMAIL PILL COMPONENT */
        .access-pill-wrapper {
            max-width: 620px;
            margin: 0 auto;
            position: relative;
            z-index: 5;
        }
        .protocol-email-pill {
            display: flex;
            align-items: center;
            background: rgba(18, 18, 24, 0.95);
            border: 1px solid rgba(255, 41, 44, 0.4);
            border-radius: 9999px;
            padding: 6px 8px 6px 20px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.8), 0 0 24px rgba(255, 41, 44, 0.15);
            transition: border-color 0.25s ease, box-shadow 0.25s ease;
        }
        .protocol-email-pill:focus-within {
            border-color: var(--laser-red);
            box-shadow: 0 12px 40px rgba(0, 0, 0, 0.9), 0 0 30px rgba(255, 41, 44, 0.35);
        }
        .pill-prefix {
            font-family: 'JetBrains Mono', monospace;
            font-size: 11px;
            font-weight: 700;
            color: var(--laser-red);
            letter-spacing: 0.1em;
            white-space: nowrap;
            margin-right: 12px;
        }
        .pill-input {
            flex: 1;
            background: transparent;
            border: none;
            outline: none;
            color: var(--white);
            font-family: 'JetBrains Mono', monospace;
            font-size: 12px;
            letter-spacing: 0.05em;
        }
        .pill-input::placeholder {
            color: var(--dark-slate);
        }
        .pill-btn {
            background: var(--laser-red);
            border: none;
            outline: none;
            color: var(--white);
            font-family: 'JetBrains Mono', monospace;
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 0.08em;
            padding: 10px 20px;
            border-radius: 9999px;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            box-shadow: 0 0 14px var(--laser-glow);
            transition: all 0.2s ease;
            white-space: nowrap;
        }
        .pill-btn:hover {
            background: #FF4245;
            box-shadow: 0 0 22px var(--laser-red);
            transform: scale(1.02);
        }
        .pill-feedback {
            font-family: 'JetBrains Mono', monospace;
            font-size: 11px;
            margin-top: 14px;
            min-height: 20px;
            letter-spacing: 0.06em;
            transition: opacity 0.3s ease;
        }
        .pill-feedback.success {
            color: var(--green);
            text-shadow: 0 0 10px rgba(0, 230, 118, 0.4);
        }

        /* MASSIVE PIXELATED BRUTALIST DISPLAY TITLE IN FOOTER */
        .footer-pixel-title-wrap {
            text-align: center;
            padding: 40px 24px 30px;
            border-bottom: 1px solid var(--border);
            overflow: hidden;
        }
        .footer-pixel-title {
            font-family: 'Syne', sans-serif;
            font-size: clamp(38px, 7.5vw, 105px);
            font-weight: 800;
            line-height: 0.95;
            letter-spacing: -0.04em;
            color: #1A1A22;
            text-transform: uppercase;
            transition: color 0.4s ease, text-shadow 0.4s ease;
            display: inline-block;
            user-select: none;
        }
        .footer-pixel-title:hover {
            color: var(--white);
            text-shadow: 0 0 40px rgba(255, 41, 44, 0.45);
        }

        /* BRUTALIST FOOTER */
        .footer {
            background: #050507;
            padding: 60px 24px 40px;
            position: relative;
        }
        .footer-inner {
            max-width: 1320px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: 1.5fr 1fr 1fr 1.2fr;
            gap: 40px;
            padding-bottom: 50px;
            border-bottom: 1px solid var(--border);
        }
        @media (max-width: 900px) {
            .footer-inner {
                grid-template-columns: 1fr 1fr;
            }
        }
        @media (max-width: 600px) {
            .footer-inner {
                grid-template-columns: 1fr;
            }
        }

        .footer-col {
            display: flex;
            flex-direction: column;
            gap: 14px;
        }
        .footer-brand-title {
            display: flex;
            align-items: center;
            gap: 10px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 13px;
            font-weight: 700;
            letter-spacing: 0.12em;
            color: var(--chalk);
        }
        .footer-text {
            font-size: 13px;
            line-height: 1.6;
            color: var(--slate);
            max-width: 320px;
        }
        .footer-domain-badge {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 11px;
            color: var(--laser-red);
            letter-spacing: 0.08em;
            margin-top: 6px;
        }

        .footer-heading {
            font-family: 'JetBrains Mono', monospace;
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 0.14em;
            color: var(--chalk);
            text-transform: uppercase;
            margin-bottom: 4px;
        }
        .footer-link {
            font-family: 'JetBrains Mono', monospace;
            font-size: 11px;
            color: var(--slate);
            text-decoration: none;
            letter-spacing: 0.06em;
            transition: color 0.2s ease, transform 0.2s ease;
            display: inline-block;
        }
        .footer-link:hover {
            color: var(--laser-red);
            transform: translateX(3px);
        }

        .footer-contract-box {
            background: #09090D;
            border: 1px solid var(--border);
            padding: 12px;
            border-radius: 4px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 10px;
            line-height: 1.5;
            color: var(--slate);
            word-break: break-all;
        }
        .footer-contract-box strong {
            color: var(--chalk);
        }

        .footer-bottom {
            max-width: 1320px;
            margin: 30px auto 0;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-family: 'JetBrains Mono', monospace;
            font-size: 10px;
            color: var(--dark-slate);
            letter-spacing: 0.08em;
            flex-wrap: wrap;
            gap: 16px;
        }
        .footer-bottom-copy {
            color: var(--slate);
        }

        /* -------------------------------------------------------------
           FLOATING MINIMAP VIEWPORT NAVIGATOR (150px x 95px)
           ------------------------------------------------------------- */
        .minimap-container {
            position: fixed;
            bottom: 24px;
            right: 24px;
            width: 150px;
            height: 95px;
            background: rgba(9, 9, 13, 0.94);
            backdrop-filter: blur(14px);
            -webkit-backdrop-filter: blur(14px);
            border: 1px solid rgba(255, 41, 44, 0.4);
            clip-path: polygon(0 8px, 8px 0, calc(100% - 8px) 0, 100% 8px, 100% calc(100% - 8px), calc(100% - 8px) 100%, 8px 100%, 0 calc(100% - 8px));
            z-index: 990;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.8), 0 0 20px rgba(255, 41, 44, 0.15);
            display: flex;
            flex-direction: column;
            overflow: hidden;
            user-select: none;
            transition: border-color 0.2s ease, box-shadow 0.2s ease;
        }
        .minimap-container:hover {
            border-color: var(--laser-red);
            box-shadow: 0 12px 35px rgba(0, 0, 0, 0.9), 0 0 25px rgba(255, 41, 44, 0.35);
        }
        .minimap-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 4px 8px;
            background: #111117;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            font-family: 'JetBrains Mono', monospace;
            font-size: 8px;
            letter-spacing: 0.1em;
            color: var(--slate);
        }
        .minimap-dot {
            width: 5px;
            height: 5px;
            background: var(--green);
            border-radius: 50%;
            box-shadow: 0 0 6px var(--green);
        }
        .minimap-pct {
            color: var(--laser-red);
            font-weight: 700;
        }
        .minimap-track {
            flex: 1;
            position: relative;
            padding: 4px 6px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            gap: 3px;
            cursor: pointer;
        }
        .mini-sec {
            height: 9px;
            border-radius: 2px;
            border: 1px solid rgba(255, 255, 255, 0.06);
            transition: opacity 0.2s ease;
        }
        .mini-hero {
            background: #ECECEC;
            border-color: #C0C0C8;
        }
        .mini-stage {
            background: #0B0B0E;
            border-color: #242430;
        }
        .mini-grid {
            background: #FF292C;
            border-color: #B21B1E;
        }
        .mini-console {
            background: #F4F4F6;
            border-color: #D4D4DC;
        }
        .mini-footer {
            background: #050507;
            border-color: #242430;
        }

        .minimap-viewport {
            position: absolute;
            left: 4px;
            right: 4px;
            top: 4px;
            height: 16px;
            border: 1.5px solid var(--laser-red);
            background: rgba(255, 41, 44, 0.25);
            box-shadow: 0 0 10px rgba(255, 41, 44, 0.7);
            border-radius: 2px;
            pointer-events: none;
            will-change: top, height;
        }

        @media (max-width: 900px) {
            .hero-inner {
                grid-template-columns: 1fr;
                gap: 40px;
            }
            .nav-links {
                display: none;
            }
            .schematic-canvas-wrap {
                height: 300px;
            }
            .minimap-container {
                display: none;
            }
        }

        /* ==========================================================================
           TOP-EDGE SCROLL TELEMETRY PROGRESS LINE (LASER RED)
           ========================================================================== */
        #scroll-progress-line {
            position: fixed;
            top: 0;
            left: 0;
            width: 0%;
            height: 2.5px;
            background: var(--laser-red);
            box-shadow: 0 0 10px var(--laser-red), 0 0 20px rgba(255, 41, 44, 0.7);
            z-index: 99999;
            pointer-events: none;
            transition: width 0.04s linear;
            will-change: width;
        }

        /* ==========================================================================
           INTERSECTION OBSERVER REVEAL ANIMATIONS (JANK-FREE, ZERO LAYOUT SHIFT)
           ========================================================================== */
        .reveal-on-scroll,
        .stat-tile:not(.is-revealed),
        .research-card:not(.is-revealed),
        .section-title:not(.is-revealed),
        .cta-title:not(.is-revealed),
        .stage-stat-card:not(.is-revealed) {
            opacity: 0;
            transform: translateY(22px);
            transition: opacity 0.65s cubic-bezier(0.16, 1, 0.3, 1),
                        transform 0.65s cubic-bezier(0.16, 1, 0.3, 1),
                        border-color 0.25s ease,
                        box-shadow 0.25s ease;
            will-change: opacity, transform;
        }

        .reveal-on-scroll.is-revealed,
        .stat-tile.is-revealed,
        .research-card.is-revealed,
        .section-title.is-revealed,
        .cta-title.is-revealed,
        .stage-stat-card.is-revealed {
            opacity: 1;
            transform: translateY(0);
        }

        .node-tile.reveal-init {
            opacity: 0;
            transform: scale(0.85);
        }
        .node-tile.is-revealed {
            opacity: 1;
            transform: none;
        }

        /* Staggered transition delays */
        .reveal-delay-1 { transition-delay: 0.08s; }
        .reveal-delay-2 { transition-delay: 0.16s; }
        .reveal-delay-3 { transition-delay: 0.24s; }
        .reveal-delay-4 { transition-delay: 0.32s; }
    </style>
</head>
<body>

    <!-- TOP-EDGE SCROLL TELEMETRY PROGRESS LINE -->
    <div id="scroll-progress-line" class="scroll-progress-bar" aria-hidden="true"></div>

    <!-- CUSTOM RETRO-TECH CURSOR -->
    <div id="cursor-dot"></div>
    <div id="cursor-ring"></div>

    <!-- FLOATING PILL NAVBAR -->
    <div class="nav-wrapper">
        <nav class="nav-pill">
            <a href="#hero" class="nav-brand">
                <div class="nav-logo-box">
                    <img src="assets/nav_logo.png" alt="33rd Tree Labs Wireframe">
                </div>
                <span class="nav-title">33RD TREE LABS</span>
            </a>

            <div class="nav-links">
                <a href="#hero" class="nav-link">OVERVIEW</a>
                <a href="#singularity-stage" class="nav-link">STAGE</a>
                <a href="#protocol" class="nav-link">PROTOCOL</a>
                <a href="#simulator" class="nav-link">SIMULATOR</a>
                <a href="#calculator" class="nav-link">YIELD</a>
                <a href="nodes.html" class="nav-link">NODES</a>
                <a href="tokenomics.html" class="nav-link">TOKENOMICS</a>
                <a href="research.html" class="nav-link">RESEARCH</a>
                <a href="33rd_Tree_Labs_Whitepaper.pdf" target="_blank" class="nav-link">WHITEPAPER (V4.0)</a>
            </div>

            <div class="nav-status">
                <span class="nav-status-dot"></span>
                <span id="nav-active-section">CANARY // OVERVIEW</span>
            </div>

            <a href="nodes.html" class="nav-cta">DEPLOY GPU</a>
        </nav>
    </div>

    <!-- =========================================================
         SECTION 1: HERO (LIGHT CHALK THEME #ECECEC / #F0F0F2)
         ========================================================= -->
    <section class="theme-section theme-chalk hero" id="hero">
        <div class="hero-inner">
            <div class="hero-left">
                <div class="meta-tag" data-scramble>( 01 ) // PROTOCOL OVERVIEW &bull; 33RDTREELABS.TECH</div>
                
                <!-- Massive Split Brutalist Display Typography with Pixel Glitch Decoding -->
                <div class="hero-split-words">
                    <div class="hero-word-row">
                        <span class="display-word" data-scramble>WE</span>
                        <span class="display-word" data-scramble>COORDINATE</span>
                    </div>
                    <div class="hero-word-row">
                        <span class="display-word" data-scramble>DECENTRALIZED</span>
                    </div>
                    <div class="hero-word-row">
                        <span class="display-word red-accent" data-scramble>COMPUTE</span>
                        <span class="display-word" data-scramble>AT SCALE</span>
                    </div>
                </div>

                <p class="hero-desc">
                    A Byzantine-Resilient Verifiable DePIN Compute Fabric anchored on <strong>Solana</strong>. 
                    Uniting hierarchical <strong>Tensor Arbor</strong> cluster orchestration with zero-knowledge neural evaluations (KZG polynomial commitments) to power trustless machine intelligence.
                </p>

                <div class="hero-actions">
                    <a href="nodes.html" class="btn-brutal-red">
                        <span>DEPLOY GPU CAPACITY</span>
                        <span>&rarr;</span>
                    </a>
                    <a href="33rd_Tree_Labs_Whitepaper.pdf" target="_blank" class="btn-brutal-outline">
                        <span>READ CANARY SPEC v4.0</span>
                        <span>&darr;</span>
                    </a>
                </div>
            </div>

            <!-- PINNED CHAMFERED HARDWARE / MANIFOLD SCHEMATIC SHOWCASE -->
            <div class="schematic-box" id="hero-schematic">
                <div class="schematic-inner">
                    <div class="schematic-header">
                        <span>[ TENSOR ARBOR MANIFOLD // v4.0 ]</span>
                        <span class="status-tag">QUORUM ACTIVE (K=64)</span>
                    </div>

                    <div class="schematic-canvas-wrap">
                        <canvas id="schematic-canvas"></canvas>
                    </div>

                    <div class="schematic-telemetry">
                        <div class="tele-stat stat-tile reveal-on-scroll reveal-delay-1">
                            <span class="tele-label">P99 Latency</span>
                            <span class="tele-val accent" id="tele-lat">14.2ms</span>
                        </div>
                        <div class="tele-stat stat-tile reveal-on-scroll reveal-delay-2">
                            <span class="tele-label">Solana Anchor</span>
                            <span class="tele-val" id="tele-slot">Slot #312M</span>
                        </div>
                        <div class="tele-stat stat-tile reveal-on-scroll reveal-delay-3">
                            <span class="tele-label">KZG Verification</span>
                            <span class="tele-val accent">&lt; 1.84ms</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- SCATTERED RECTANGULAR WIPE TILES (TRANSITION 1 -> 2) -->
    <div class="wipe-tile-scatter-wrap" data-scatter="1">
        <div class="scatter-tile" style="width: 80px; height: 24px; top: 15%; left: 10%;"></div>
        <div class="scatter-tile alt" style="width: 120px; height: 36px; top: 45%; left: 40%;"></div>
        <div class="scatter-tile" style="width: 50px; height: 50px; top: 20%; left: 75%;"></div>
        <div class="scatter-tile alt" style="width: 110px; height: 20px; top: 65%; left: 20%;"></div>
        <div class="scatter-tile" style="width: 140px; height: 28px; top: 70%; left: 65%;"></div>
        <div class="scatter-tile alt" style="width: 40px; height: 75px; top: 30%; left: 88%;"></div>
    </div>

    <!-- =========================================================
         SECTION 2: SINGULARITY STAGE (DEEP OBSIDIAN BLACK #070707)
         ========================================================= -->
    <section class="theme-section theme-obsidian" id="singularity-stage">
        <!-- Running Telemetry Marquee -->
        <div class="marquee-section">
            <div class="marquee-track">
                <div class="marquee-item">
                    <span class="marquee-bullet">&bull;</span>
                    <span>NETWORK STATUS:</span>
                    <span class="highlight">MAINNET CANARY</span>
                </div>
                <div class="marquee-item">
                    <span class="marquee-bullet">&bull;</span>
                    <span>ACTIVE GPU CLUSTERS:</span>
                    <span class="red">33,492 TIER-1 SXM5</span>
                </div>
                <div class="marquee-item">
                    <span class="marquee-bullet">&bull;</span>
                    <span>AGGREGATE CAPACITY:</span>
                    <span class="highlight">142.8 EFLOPS (FP8)</span>
                </div>
                <div class="marquee-item">
                    <span class="marquee-bullet">&bull;</span>
                    <span>CONSENSUS QUORUM:</span>
                    <span class="highlight">2/3 + 1 BLS AGGREGATE</span>
                </div>
                <div class="marquee-item">
                    <span class="marquee-bullet">&bull;</span>
                    <span>SLASHING INCIDENTS:</span>
                    <span class="red">0.00% (STABLE)</span>
                </div>
                <div class="marquee-item">
                    <span class="marquee-bullet">&bull;</span>
                    <span>BUYBACK-BURN CRANK:</span>
                    <span class="highlight">10% CONTINUOUS BURN</span>
                </div>
                <div class="marquee-item">
                    <span class="marquee-bullet">&bull;</span>
                    <span>SOLANA SETTLEMENT CADENCE:</span>
                    <span class="red">400ms FINALITY</span>
                </div>
                <div class="marquee-item">
                    <span class="marquee-bullet">&bull;</span>
                    <span>DOMAIN:</span>
                    <span class="highlight">33RDTREELABS.TECH</span>
                </div>
                <!-- Duplicate for seamless loop -->
                <div class="marquee-item">
                    <span class="marquee-bullet">&bull;</span>
                    <span>NETWORK STATUS:</span>
                    <span class="highlight">MAINNET CANARY</span>
                </div>
                <div class="marquee-item">
                    <span class="marquee-bullet">&bull;</span>
                    <span>ACTIVE GPU CLUSTERS:</span>
                    <span class="red">33,492 TIER-1 SXM5</span>
                </div>
                <div class="marquee-item">
                    <span class="marquee-bullet">&bull;</span>
                    <span>AGGREGATE CAPACITY:</span>
                    <span class="highlight">142.8 EFLOPS (FP8)</span>
                </div>
                <div class="marquee-item">
                    <span class="marquee-bullet">&bull;</span>
                    <span>CONSENSUS QUORUM:</span>
                    <span class="highlight">2/3 + 1 BLS AGGREGATE</span>
                </div>
                <div class="marquee-item">
                    <span class="marquee-bullet">&bull;</span>
                    <span>SLASHING INCIDENTS:</span>
                    <span class="red">0.00% (STABLE)</span>
                </div>
                <div class="marquee-item">
                    <span class="marquee-bullet">&bull;</span>
                    <span>BUYBACK-BURN CRANK:</span>
                    <span class="highlight">10% CONTINUOUS BURN</span>
                </div>
                <div class="marquee-item">
                    <span class="marquee-bullet">&bull;</span>
                    <span>SOLANA SETTLEMENT CADENCE:</span>
                    <span class="red">400ms FINALITY</span>
                </div>
                <div class="marquee-item">
                    <span class="marquee-bullet">&bull;</span>
                    <span>DOMAIN:</span>
                    <span class="highlight">33RDTREELABS.TECH</span>
                </div>
            </div>
        </div>

        <!-- Singularity Stage Telemetry Showcase -->
        <div class="section-wrap" style="padding-top:70px; padding-bottom:70px;">
            <div class="meta-tag" data-scramble>( 02 ) // SINGULARITY STAGE &bull; COMPUTE FABRIC TELEMETRY</div>
            <h2 class="section-title" data-scramble>AUTONOMOUS AGENT CONVERGENCE</h2>
            <p class="section-desc">
                Anchored on Solana mainnet, the Singularity Protocol synchronizes decentralized GPU clusters into a single unified tensor arbor. Untrusted compute providers submit zero-knowledge KZG polynomial evaluations directly into on-chain Anchor programs, guaranteeing Byzantine-safe execution of trillion-parameter neural models.
            </p>

            <div class="stage-stats-grid">
                <div class="stage-stat-card stat-tile reveal-on-scroll reveal-delay-1">
                    <div class="stage-stat-num red">142.8</div>
                    <div class="stage-stat-lbl">EFLOPS FP8 CAPACITY</div>
                </div>
                <div class="stage-stat-card stat-tile reveal-on-scroll reveal-delay-2">
                    <div class="stage-stat-num">33,492</div>
                    <div class="stage-stat-lbl">TIER-1 SXM5 CLUSTERS</div>
                </div>
                <div class="stage-stat-card stat-tile reveal-on-scroll reveal-delay-3">
                    <div class="stage-stat-num red">400ms</div>
                    <div class="stage-stat-lbl">SOLANA ANCHOR CADENCE</div>
                </div>
                <div class="stage-stat-card stat-tile reveal-on-scroll reveal-delay-4">
                    <div class="stage-stat-num">0.00%</div>
                    <div class="stage-stat-lbl">SLASHING RATE (300 EPOCHS)</div>
                </div>
            </div>
        </div>
    </section>

    <!-- SCATTERED RECTANGULAR WIPE TILES (TRANSITION 2 -> 3) -->
    <div class="wipe-tile-scatter-wrap" data-scatter="2">
        <div class="scatter-tile" style="width: 100px; height: 30px; top: 20%; left: 15%;"></div>
        <div class="scatter-tile alt" style="width: 60px; height: 60px; top: 50%; left: 50%;"></div>
        <div class="scatter-tile" style="width: 130px; height: 22px; top: 15%; left: 70%;"></div>
        <div class="scatter-tile alt" style="width: 80px; height: 35px; top: 65%; left: 30%;"></div>
        <div class="scatter-tile" style="width: 120px; height: 25px; top: 75%; left: 80%;"></div>
    </div>

    <!-- =========================================================
         SECTION 3: ARCHITECTURE (ELECTRIC RED FULL-BLEED TAKEOVER #FF292C)
         ========================================================= -->
    <section class="theme-section theme-electric-red" id="protocol">
        <div class="section-wrap">
            <div class="meta-tag" data-scramble>( 03 ) // ARCHITECTURE MATRIX &bull; 4-COLUMN PILLARS</div>
            <h2 class="section-title" data-scramble>ENGINEERED FOR UNCOMPROMISING INTEGRITY</h2>
            <p class="section-desc">
                A fault-tolerant computing fabric designed to guarantee deterministic verification across untrusted distributed hardware without performance degradation.
            </p>

            <div class="arch-grid">
                <!-- Pillar 01 -->
                <div class="arch-card research-card reveal-on-scroll reveal-delay-1">
                    <div>
                        <div class="card-meta-row">
                            <span class="card-number">[ 01 ]</span>
                            <span class="card-badge">COORDINATION</span>
                        </div>
                        <h3 class="card-heading">TENSOR ARBOR TOPOLOGY</h3>
                        <p class="card-text">
                            Hierarchical tree manifold partitioning distributed model parameters across heterogeneous GPU nodes. Dynamically matches pipeline stages and tensor parallelism to physical interconnect latencies, preventing inter-node bottlenecks.
                        </p>
                    </div>
                    <div class="card-footer-metrics">
                        <span class="card-metric-pill">ROUTING: <strong>NON-EUCLIDEAN DAG</strong></span>
                        <span class="card-metric-pill">BANDWIDTH: <strong>900 GB/s NVLINK</strong></span>
                    </div>
                </div>

                <!-- Pillar 02 -->
                <div class="arch-card research-card reveal-on-scroll reveal-delay-2">
                    <div>
                        <div class="card-meta-row">
                            <span class="card-number">[ 02 ]</span>
                            <span class="card-badge">VERIFICATION</span>
                        </div>
                        <h3 class="card-heading">PROOF OF INFERENCE (POI)</h3>
                        <p class="card-text">
                            Zero-knowledge neural evaluations pairing randomized Chebyshev Activation Polynomial (CAP-FFN) challenges with BN254 KZG polynomial commitment schemes. Enables sub-2ms cryptographic verification directly inside Solana smart contracts.
                        </p>
                    </div>
                    <div class="card-footer-metrics">
                        <span class="card-metric-pill">SCHEME: <strong>BN254 KZG</strong></span>
                        <span class="card-metric-pill">SOLANA ON-CHAIN: <strong>&lt; 200,000 CU</strong></span>
                    </div>
                </div>

                <!-- Pillar 03 -->
                <div class="arch-card research-card reveal-on-scroll reveal-delay-3">
                    <div>
                        <div class="card-meta-row">
                            <span class="card-number">[ 03 ]</span>
                            <span class="card-badge">CONSENSUS</span>
                        </div>
                        <h3 class="card-heading">BYZANTINE QUORUM MATRIX</h3>
                        <p class="card-text">
                            Asynchronous BFT consensus withstanding up to f &lt; K/3 malicious, compromised, or colluding nodes. Immediate automated slashing of bonded $33RD collateral upon mathematical detection of gradient poisoning or equivocation.
                        </p>
                    </div>
                    <div class="card-footer-metrics">
                        <span class="card-metric-pill">TOLERANCE: <strong>f &lt; K/3</strong></span>
                        <span class="card-metric-pill">COMMITTEE: <strong>K=64 VALIDATORS</strong></span>
                    </div>
                </div>

                <!-- Pillar 04 -->
                <div class="arch-card research-card reveal-on-scroll reveal-delay-4">
                    <div>
                        <div class="card-meta-row">
                            <span class="card-number">[ 04 ]</span>
                            <span class="card-badge">TOKENOMICS</span>
                        </div>
                        <h3 class="card-heading">DEFLATIONARY BUYBACK CRANK</h3>
                        <p class="card-text">
                            Hard cap of 33,000,000 $33RD with quadrennial halving cycles. 10% of all commercial GPU inference revenue is routed into an autonomous smart contract crank that executes continuous market buybacks and irrevocable token burns.
                        </p>
                    </div>
                    <div class="card-footer-metrics">
                        <span class="card-metric-pill">SUPPLY: <strong>33,000,000 $33RD</strong></span>
                        <span class="card-metric-pill">BURN CRANK: <strong>10% REVENUE</strong></span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- SCATTERED RECTANGULAR WIPE TILES (TRANSITION 3 -> 4) -->
    <div class="wipe-tile-scatter-wrap" data-scatter="3">
        <div class="scatter-tile" style="width: 90px; height: 26px; top: 15%; left: 8%;"></div>
        <div class="scatter-tile alt" style="width: 140px; height: 38px; top: 40%; left: 35%;"></div>
        <div class="scatter-tile" style="width: 55px; height: 55px; top: 25%; left: 78%;"></div>
        <div class="scatter-tile alt" style="width: 110px; height: 22px; top: 70%; left: 18%;"></div>
        <div class="scatter-tile" style="width: 130px; height: 30px; top: 60%; left: 62%;"></div>
    </div>

    <!-- =========================================================
         SECTION 4: PHILOSOPHY / CONSOLE & YIELD (STARK WHITE #F4F4F6)
         ========================================================= -->
    <section class="theme-section theme-chalk-2" id="console-section">
        <!-- Interactive Byzantine Simulator & Solana Terminal -->
        <div class="section-wrap" id="simulator">
            <div class="meta-tag" data-scramble>( 04 ) // BYZANTINE AUDIT &bull; LIVE SIMULATOR &bull; TERMINAL</div>
            <h2 class="section-title" data-scramble>ADVERSARIAL CONSENSUS &amp; CLI ENGINE</h2>
            <p class="section-desc">
                Test the mathematical guarantees of the Singularity Protocol. Inject malicious adversaries, evaluate Byzantine resilience, and query on-chain Solana state via the live command console.
            </p>

            <div class="sim-grid">
                <!-- Visual Byzantine Committee Lattice -->
                <div class="sim-box">
                    <div class="sim-box-title">
                        <span>VALIDATOR COMMITTEE LATTICE (K=64)</span>
                        <span id="byz-ratio-tag" style="color:var(--chalk);">f = 4 / 64 (6.2%)</span>
                    </div>

                    <!-- 8x8 Interactive Node Lattice -->
                    <div class="node-lattice" id="node-matrix">
                        <!-- 64 Nodes dynamically generated in JS -->
                    </div>

                    <div class="sim-controls">
                        <div>
                            <div class="sim-slider-row">
                                <span>BYZANTINE ADVERSARY COUNT (f)</span>
                                <span id="byz-count-text" style="color:var(--laser-red); font-weight:700;">f = 4 (Safe)</span>
                            </div>
                            <input type="range" id="byz-slider" class="sim-range" min="0" max="30" value="4" oninput="updateByzantineSim()">
                        </div>

                        <div style="display:flex; flex-direction:column; gap:6px;">
                            <span class="sim-slider-row"><span>ATTACK VECTOR SIMULATION</span></span>
                            <select id="attack-vector-select" class="sim-attack-select" onchange="updateByzantineSim()">
                                <option value="gradient-poison">Malicious Gradient Poisoning (CAP-FFN Failure)</option>
                                <option value="equivocation">Equivocation &bull; Dual Block Commitment</option>
                                <option value="weight-tamper">Model Weight Tampering &bull; Silent Bit-Rot</option>
                                <option value="sybil-stall">Coordinated Sybil Denial of Service (Stall)</option>
                            </select>
                        </div>

                        <button class="btn-brutal-red" onclick="runConsensusRound()" style="width:100%; justify-content:center; padding:12px; cursor:pointer;">
                            EXECUTE CONSENSUS ROUND &rarr;
                        </button>

                        <div class="sim-status-banner" id="sim-status-box">
                            <div class="sim-status-head success" id="sim-status-title">
                                <span>[VALID] CONSENSUS REACHED: QUORUM VALIDATED</span>
                            </div>
                            <div id="sim-status-desc" style="color:var(--slate);">
                                Honest nodes: 60/64 (93.8%) &bull; Quorum threshold 66.7% met. Byzantine nodes isolated and marked for collateral slashing.
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Interactive Solana CLI Terminal -->
                <div class="terminal-box">
                    <div class="terminal-topbar">
                        <div class="terminal-dots">
                            <div class="terminal-dot red"></div>
                            <div class="terminal-dot"></div>
                            <div class="terminal-dot"></div>
                        </div>
                        <span>canary-cli &bull; 33rdtreelabs.tech</span>
                        <span style="color:var(--green);">&bull; CONNECTED</span>
                    </div>

                    <div class="terminal-output" id="terminal-output">
                        <div class="terminal-line highlight">========================================================</div>
                        <div class="terminal-line highlight">33RD TREE LABS // THE SINGULARITY PROTOCOL v4.0</div>
                        <div class="terminal-line dim">Solana Anchor Program: 33rdCore11111111111111111111111111111111111</div>
                        <div class="terminal-line dim">Domain: 33rdtreelabs.tech &bull; Node Cadence: 400ms</div>
                        <div class="terminal-line highlight">========================================================</div>
                        <div class="terminal-line">Type <span style="color:var(--laser-red);">help</span> to list available diagnostics commands.</div>
                        <div class="terminal-line success">&gt; Anchor state verified &bull; 33,492 GPU nodes bonded</div>
                    </div>

                    <form class="terminal-input-wrap" onsubmit="handleTerminalSubmit(event)">
                        <span class="terminal-prompt">&gt;</span>
                        <input type="text" id="terminal-input" class="terminal-input" placeholder="Type status, nodes, bench, verify, tokenomics, byzantine..." autocomplete="off">
                    </form>

                    <div class="quick-chips">
                        <span class="chip" onclick="executeTermCommand('status')">status</span>
                        <span class="chip" onclick="executeTermCommand('nodes')">nodes</span>
                        <span class="chip" onclick="executeTermCommand('bench')">bench</span>
                        <span class="chip" onclick="executeTermCommand('verify')">verify</span>
                        <span class="chip" onclick="executeTermCommand('byzantine')">byzantine</span>
                        <span class="chip" onclick="executeTermCommand('tokenomics')">tokenomics</span>
                        <span class="chip" onclick="executeTermCommand('clear')">clear</span>
                    </div>
                </div>
            </div>
        </div>

        <!-- Validator Yield & Staking Calculator -->
        <div class="section-wrap" id="calculator" style="padding-top:20px;">
            <div class="meta-tag" data-scramble>( 05 ) // TOKENOMICS &bull; REWARDS SIMULATOR</div>
            <h2 class="section-title" data-scramble>VALIDATOR YIELD CALCULATOR</h2>
            <p class="section-desc">
                Model validator yields, collateral requirements, and deflationary buyback dynamics across hardware configurations and halving epochs.
            </p>

            <div class="calc-grid">
                <div class="calc-panel-left">
                    <div class="calc-field">
                        <label class="calc-label">Validator Hardware Configuration</label>
                        <select id="calc-hw-select" class="calc-select" onchange="calculateRewards()">
                            <option value="dual-h100" selected>Tier-1: Dual NVIDIA H100 SXM5 (160GB VRAM)</option>
                            <option value="quad-h100">Tier-1 Heavy: Quad NVIDIA H100 SXM5 (320GB VRAM)</option>
                            <option value="cluster-b200">Tier-1 Ultra: NVIDIA B200 NVL72 Cluster</option>
                            <option value="single-4090">Tier-2 Edge: NVIDIA RTX 4090 (24GB VRAM)</option>
                        </select>
                    </div>

                    <div class="calc-field">
                        <label class="calc-label">
                            <span>Bonded Collateral</span>
                            <span id="calc-stake-display" style="color:var(--chalk); font-weight:700;">25,000 $33RD</span>
                        </label>
                        <input type="range" id="calc-stake-slider" class="calc-slider" min="25000" max="500000" step="5000" value="25000" oninput="calculateRewards()">
                    </div>

                    <div class="calc-field">
                        <label class="calc-label">Emission Halving Epoch</label>
                        <select id="calc-epoch-select" class="calc-select" onchange="calculateRewards()">
                            <option value="0" selected>Epoch 0 (Years 1&ndash;4) &bull; 0.7135 $33RD / block</option>
                            <option value="1">Epoch 1 (Years 5&ndash;8) &bull; 0.3567 $33RD / block</option>
                            <option value="2">Epoch 2 (Years 9&ndash;12) &bull; 0.1784 $33RD / block</option>
                            <option value="3">Epoch 3 (Years 13&ndash;16) &bull; 0.0892 $33RD / block</option>
                        </select>
                    </div>
                </div>

                <div class="calc-panel-right">
                    <div class="calc-stat-box stat-tile reveal-on-scroll">
                        <div class="calc-metric-row">
                            <span class="calc-metric-name">ESTIMATED APY</span>
                            <span class="calc-metric-val highlight" id="calc-apy-val">38.4%</span>
                        </div>
                        <div class="calc-metric-row">
                            <span class="calc-metric-name">EST. DAILY REWARDS</span>
                            <span class="calc-metric-val" id="calc-daily-val">26.3 $33RD</span>
                        </div>
                        <div class="calc-metric-row">
                            <span class="calc-metric-name">EST. MONTHLY REWARDS</span>
                            <span class="calc-metric-val" id="calc-monthly-val">789.0 $33RD</span>
                        </div>
                        <div class="calc-metric-row">
                            <span class="calc-metric-name">10% BUYBACK-BURN BURNED / DAY</span>
                            <span class="calc-metric-val" id="calc-burn-val" style="color:var(--laser-red);">513.7 $33RD</span>
                        </div>
                    </div>

                    <div class="calc-disclaimer">
                        Calculations assume constant network compute demand and bonded stake distribution. Model parameters defined in Canary Specification v4.0.
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- SCATTERED RECTANGULAR WIPE TILES (TRANSITION 4 -> 5) -->
    <div class="wipe-tile-scatter-wrap" data-scatter="4">
        <div class="scatter-tile" style="width: 85px; height: 25px; top: 20%; left: 12%;"></div>
        <div class="scatter-tile alt" style="width: 120px; height: 35px; top: 45%; left: 45%;"></div>
        <div class="scatter-tile" style="width: 45px; height: 45px; top: 15%; left: 75%;"></div>
        <div class="scatter-tile alt" style="width: 130px; height: 24px; top: 65%; left: 25%;"></div>
        <div class="scatter-tile" style="width: 110px; height: 30px; top: 75%; left: 68%;"></div>
    </div>

    <!-- =========================================================
         SECTION 5: FOOTER & PROTOCOL ACCESS (DEEP OBSIDIAN #050507)
         ========================================================= -->
    <section class="theme-section theme-deep-obsidian" id="access-section">
        <!-- Call to Action Section with Interactive Email Pill -->
        <div class="cta-section">
            <div class="cta-box">
                <div class="meta-tag" data-scramble style="justify-content:center;">( 06 ) // JOIN THE FABRIC &bull; 33RDTREELABS.TECH</div>
                <h2 class="cta-title" data-scramble>DECENTRALIZE INTELLIGENCE.<br>SECURE THE SINGULARITY.</h2>
                <p class="cta-desc">
                    Contribute enterprise GPU capacity to earn native protocol emissions, or interface autonomous AI agents directly to verifiable inference streams anchored on Solana.
                </p>

                <div class="cta-buttons">
                    <a href="nodes.html" class="btn-brutal-red" style="padding:16px 36px; font-size:13px;">
                        <span>DEPLOY GPU CAPACITY</span>
                        <span>&rarr;</span>
                    </a>
                    <a href="33rd_Tree_Labs_Whitepaper.pdf" target="_blank" class="btn-brutal-outline" style="padding:15px 32px; font-size:13px;">
                        <span>READ CANARY SPEC v4.0</span>
                        <span>&darr;</span>
                    </a>
                </div>

                <!-- SIGNATURE INTERACTIVE PROTOCOL ACCESS EMAIL PILL -->
                <div class="access-pill-wrapper">
                    <form class="protocol-email-pill" id="access-pill-form" onsubmit="handleProtocolAccess(event)">
                        <span class="pill-prefix">OPERATOR_ID //</span>
                        <input type="email" id="access-pill-input" class="pill-input" placeholder="ENTER SOLANA / GPU OPERATOR EMAIL" required autocomplete="off">
                        <button type="submit" class="pill-btn">
                            <span>REQUEST ACCESS</span>
                            <span>&rarr;</span>
                        </button>
                    </form>
                    <div class="pill-feedback" id="pill-feedback"></div>
                </div>
            </div>
        </div>

        <!-- MASSIVE PIXELATED BRUTALIST DISPLAY TITLE -->
        <div class="footer-pixel-title-wrap">
            <div class="footer-pixel-title" data-scramble>33RD TREE LABS // THE SINGULARITY PROTOCOL</div>
        </div>

        <!-- Brutalist Footer -->
        <footer class="footer">
            <div class="footer-inner">
                <div class="footer-col">
                    <div class="footer-brand-title">
                        <div class="nav-logo-box" style="width:22px; height:22px;">
                            <img src="assets/nav_logo.png" alt="33rd Tree Labs">
                        </div>
                        <span data-scramble>33RD TREE LABS</span>
                    </div>
                    <p class="footer-text">
                        A Byzantine-Resilient Verifiable DePIN Compute Fabric on Solana. Coordinating non-Euclidean tensor pipelines and zero-knowledge neural evaluations.
                    </p>
                    <div class="footer-domain-badge">
                        <span>DOMAIN:</span>
                        <strong>33rdtreelabs.tech</strong>
                    </div>
                </div>

                <div class="footer-col">
                    <div class="footer-heading" data-scramble>// ARCHITECTURE</div>
                    <a href="#protocol" class="footer-link">Tensor Arbor Protocol</a>
                    <a href="nodes.html" class="footer-link">Validator Clusters</a>
                    <a href="tokenomics.html" class="footer-link">Token Economics</a>
                    <a href="research.html" class="footer-link">Research Papers</a>
                </div>

                <div class="footer-col">
                    <div class="footer-heading" data-scramble>// SPECIFICATIONS</div>
                    <a href="33rd_Tree_Labs_Whitepaper.pdf" target="_blank" class="footer-link">Whitepaper (Canary Spec v4.0)</a>
                    <a href="whitepaper_academic.html" class="footer-link">Academic Specification</a>
                    <a href="https://github.com/0xplayboi-ian/33rd-tree-labs" target="_blank" class="footer-link">GitHub Repository</a>
                    <a href="https://solana.com" target="_blank" class="footer-link">Solana Mainnet Anchor</a>
                </div>

                <div class="footer-col">
                    <div class="footer-heading" data-scramble>// PROTOCOL CONTRACTS</div>
                    <div class="footer-contract-box">
                        <div><strong>Anchor Program ID:</strong></div>
                        <div style="color:var(--chalk); margin-top:2px;">33rdCore11111111111111111111111111111111111</div>
                        <div style="margin-top:8px;"><strong>Byzantine Committee:</strong></div>
                        <div style="color:var(--green);">K=64 Quorum &bull; 2/3 BLS BN254</div>
                    </div>
                </div>
            </div>

            <div class="footer-bottom">
                <div class="footer-bottom-copy">
                    &copy; 2026 33RD TREE LABS FOUNDATION &bull; THE SINGULARITY PROTOCOL &bull; 33RDTREELABS.TECH
                </div>
                <div>
                    CANARY SPECIFICATION V4.0 &bull; ALL RIGHTS RESERVED
                </div>
            </div>
        </footer>
    </section>

    <!-- FLOATING MINIMAP VIEWPORT NAVIGATOR (150px x 95px) -->
    <div class="minimap-container" id="minimap">
        <div class="minimap-header">
            <span class="minimap-dot"></span>
            <span>NAV // VIEWPORT</span>
            <span class="minimap-pct" id="minimap-pct">00%</span>
        </div>
        <div class="minimap-track" id="minimap-track">
            <div class="mini-sec mini-hero" title="01 Hero"></div>
            <div class="mini-sec mini-stage" title="02 Singularity Stage"></div>
            <div class="mini-sec mini-grid" title="03 Architecture"></div>
            <div class="mini-sec mini-console" title="04 Console & Yield"></div>
            <div class="mini-sec mini-footer" title="05 Access & Footer"></div>
            <div class="minimap-viewport" id="minimap-viewport"></div>
        </div>
    </div>

    <!-- JAVASCRIPT ENGINES (LENIS + GSAP SCROLLTRIGGER + SCRAMBLE + 2D CANYAS + SIMULATORS) -->
    <script>
        /* 1. LENIS SMOOTH SCROLLING & GSAP SCROLLTRIGGER CONNECTION */
        gsap.registerPlugin(ScrollTrigger);

        const lenis = new Lenis({
            duration: 1.25,
            easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
            orientation: 'vertical',
            smoothWheel: true,
            wheelMultiplier: 1.0,
            touchMultiplier: 2.0
        });

        lenis.on('scroll', ScrollTrigger.update);

        gsap.ticker.add((time) => {
            lenis.raf(time * 1000);
        });
        gsap.ticker.lagSmoothing(0);

        // Smooth Anchor Navigation
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function(e) {
                const targetId = this.getAttribute('href');
                if (targetId && targetId !== '#') {
                    const targetEl = document.querySelector(targetId);
                    if (targetEl) {
                        e.preventDefault();
                        lenis.scrollTo(targetEl, { offset: -40, duration: 1.2 });
                    }
                }
            });
        });

        /* 2. TEXT SCRAMBLE & PIXEL GLYPH DECODING ENGINE */
        class TextScramble {
            constructor(el) {
                this.el = el;
                this.chars = '█▓▒░01X*_[ ]?/#$%&+<>';
                this.originalText = el.getAttribute('data-original-text') || el.innerText.trim();
                el.setAttribute('data-original-text', this.originalText);
                this.isScrambling = false;
            }

            scramble(duration = 1.1) {
                if (this.isScrambling) return;
                this.isScrambling = true;
                const target = this.originalText;
                const length = target.length;
                const startTime = performance.now();
                const durationMs = duration * 1000;

                const update = (now) => {
                    const elapsed = now - startTime;
                    const progress = Math.min(1, elapsed / durationMs);
                    const revealedLength = Math.floor(progress * length);

                    let output = '';
                    for (let i = 0; i < length; i++) {
                        if (target[i] === ' ' || target[i] === '\\n') {
                            output += target[i];
                        } else if (i < revealedLength) {
                            output += target[i];
                        } else if (i < revealedLength + 3) {
                            output += this.chars[Math.floor(Math.random() * this.chars.length)];
                        } else {
                            output += this.chars[Math.floor(Math.random() * this.chars.length)];
                        }
                    }
                    this.el.innerText = output;

                    if (progress < 1) {
                        requestAnimationFrame(update);
                    } else {
                        this.el.innerText = target;
                        this.isScrambling = false;
                    }
                };
                requestAnimationFrame(update);
            }
        }

        // Attach Scramble Engine to Targets
        document.querySelectorAll('[data-scramble]').forEach(el => {
            const scrambler = new TextScramble(el);
            ScrollTrigger.create({
                trigger: el,
                start: 'top 88%',
                onEnter: () => scrambler.scramble(1.1),
                onEnterBack: () => scrambler.scramble(0.8)
            });
            el.addEventListener('mouseenter', () => scrambler.scramble(0.8));
        });

        /* 3. SCATTERED RECTANGULAR WIPE TILES SCROLLTRIGGER ANIMATION */
        gsap.utils.toArray('.wipe-tile-scatter-wrap').forEach((wrap) => {
            const tiles = wrap.querySelectorAll('.scatter-tile');
            gsap.fromTo(tiles, 
                { 
                    x: (i) => (i % 2 === 0 ? -160 : 160),
                    scaleX: 0.2,
                    opacity: 0 
                }, 
                { 
                    x: (i) => (i % 2 === 0 ? 100 : -100),
                    scaleX: (i) => 1.2 + (i % 3) * 0.4,
                    opacity: 0.95,
                    stagger: 0.04,
                    scrollTrigger: {
                        trigger: wrap,
                        start: 'top 90%',
                        end: 'bottom 10%',
                        scrub: 0.8
                    }
                }
            );
        });

        /* 4. PINNED CHAMFERED CARD EXPANSION (HERO SCHEMATIC) */
        gsap.to('#hero-schematic', {
            scrollTrigger: {
                trigger: '#hero',
                start: 'top top',
                end: 'bottom 40%',
                scrub: 1
            },
            scale: 1.05,
            y: 30,
            boxShadow: '0 25px 70px rgba(0, 0, 0, 0.7), 0 0 50px rgba(255, 41, 44, 0.4)',
            ease: 'power1.out'
        });

        /* Staggered Reveal for 4 Architecture Cards */
        gsap.utils.toArray('.arch-card').forEach((card, index) => {
            gsap.from(card, {
                scrollTrigger: {
                    trigger: card,
                    start: 'top 88%',
                    toggleActions: 'play none none reverse'
                },
                y: 35,
                opacity: 0,
                duration: 0.6,
                delay: index * 0.1,
                ease: 'power2.out'
            });
        });

        /* 5. FLOATING MINIMAP VIEWPORT NAVIGATOR ENGINE */
        const minimapTrack = document.getElementById('minimap-track');
        const minimapViewport = document.getElementById('minimap-viewport');
        const minimapPct = document.getElementById('minimap-pct');

        function updateMinimap() {
            const doc = document.documentElement;
            const scrollY = window.scrollY || doc.scrollTop;
            const maxScroll = doc.scrollHeight - window.innerHeight;
            const trackHeight = minimapTrack.clientHeight;

            if (maxScroll <= 0) return;

            const scrollFraction = Math.min(1, Math.max(0, scrollY / maxScroll));
            const viewFraction = Math.min(1, window.innerHeight / doc.scrollHeight);
            const boxHeight = Math.max(14, viewFraction * trackHeight);
            const topPos = scrollFraction * (trackHeight - boxHeight);

            minimapViewport.style.height = boxHeight + 'px';
            minimapViewport.style.top = topPos + 'px';
            minimapPct.textContent = Math.round(scrollFraction * 100).toString().padStart(2, '0') + '%';
        }

        window.addEventListener('scroll', updateMinimap);
        lenis.on('scroll', updateMinimap);
        updateMinimap();

        // Minimap Click & Drag Interaction
        let isDraggingMinimap = false;
        function handleMinimapInteraction(e) {
            const rect = minimapTrack.getBoundingClientRect();
            const clickY = e.clientY - rect.top;
            const fraction = Math.min(1, Math.max(0, clickY / rect.height));
            const targetScroll = fraction * (document.documentElement.scrollHeight - window.innerHeight);
            lenis.scrollTo(targetScroll, { duration: 1.1 });
        }

        minimapTrack.addEventListener('click', handleMinimapInteraction);
        minimapTrack.addEventListener('mousedown', (e) => {
            isDraggingMinimap = true;
            handleMinimapInteraction(e);
        });
        window.addEventListener('mousemove', (e) => {
            if (isDraggingMinimap) {
                handleMinimapInteraction(e);
            }
        });
        window.addEventListener('mouseup', () => {
            isDraggingMinimap = false;
        });

        /* 6. INTERACTIVE PROTOCOL ACCESS EMAIL PILL HANDLER */
        function handleProtocolAccess(e) {
            e.preventDefault();
            const emailInput = document.getElementById('access-pill-input');
            const feedback = document.getElementById('pill-feedback');
            const val = emailInput.value.trim();

            if (!val || !val.includes('@')) {
                feedback.className = 'pill-feedback';
                feedback.style.color = 'var(--laser-red)';
                feedback.textContent = '[ERROR] INVALID OPERATOR EMAIL';
                return;
            }

            feedback.className = 'pill-feedback success';
            feedback.innerHTML = `&gt; [SUCCESS] NODE KEY ENROLLMENT DISPATCHED TO: ${val} &bull; ANCHOR SLOT RESERVED`;
            emailInput.value = '';

            setTimeout(() => {
                feedback.style.opacity = '0';
                setTimeout(() => {
                    feedback.textContent = '';
                    feedback.style.opacity = '1';
                }, 400);
            }, 6000);
        }

        /* 7. CUSTOM RETRO-TECH CURSOR DOT & RING */
        const cursorDot = document.getElementById('cursor-dot');
        const cursorRing = document.getElementById('cursor-ring');
        let mouseX = window.innerWidth / 2;
        let mouseY = window.innerHeight / 2;
        let ringX = mouseX;
        let ringY = mouseY;

        window.addEventListener('mousemove', (e) => {
            mouseX = e.clientX;
            mouseY = e.clientY;
            cursorDot.style.left = mouseX + 'px';
            cursorDot.style.top = mouseY + 'px';
        });

        function animateCursor() {
            ringX += (mouseX - ringX) * 0.18;
            ringY += (mouseY - ringY) * 0.18;
            cursorRing.style.left = ringX + 'px';
            cursorRing.style.top = ringY + 'px';
            requestAnimationFrame(animateCursor);
        }
        animateCursor();

        document.querySelectorAll('a, button, select, input, .chip, .node-tile, .mini-sec').forEach(el => {
            el.addEventListener('mouseenter', () => document.body.classList.add('cursor-hover'));
            el.addEventListener('mouseleave', () => document.body.classList.remove('cursor-hover'));
        });

        /* 8. 2D VECTOR TENSOR ARBOR MANIFOLD CANVAS (HERO SCHEMATIC) */
        const canvas = document.getElementById('schematic-canvas');
        const ctx = canvas.getContext('2d');

        function resizeCanvas() {
            if (!canvas) return;
            const rect = canvas.parentElement.getBoundingClientRect();
            canvas.width = rect.width * window.devicePixelRatio;
            canvas.height = rect.height * window.devicePixelRatio;
            ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
        }
        window.addEventListener('resize', resizeCanvas);
        resizeCanvas();

        let animAngle = 0;
        const nodesCount = 33;
        const nodes = [];
        for (let i = 0; i < nodesCount; i++) {
            nodes.push({
                angle: (i / nodesCount) * Math.PI * 2,
                radius: 40 + Math.random() * 120,
                speed: (Math.random() - 0.5) * 0.008,
                size: Math.random() * 2.5 + 2,
                isRed: Math.random() < 0.22,
                pulse: Math.random() * Math.PI
            });
        }

        function drawSchematic() {
            if (!canvas) return;
            const w = canvas.width / window.devicePixelRatio;
            const h = canvas.height / window.devicePixelRatio;
            const cx = w / 2;
            const cy = h / 2;

            ctx.clearRect(0, 0, w, h);

            // Polar Grid Rings
            ctx.strokeStyle = 'rgba(255, 255, 255, 0.04)';
            ctx.lineWidth = 1;
            for (let r = 40; r <= 160; r += 35) {
                ctx.beginPath();
                ctx.arc(cx, cy, r, 0, Math.PI * 2);
                ctx.stroke();
            }

            // Radial Hyperbolic Coordinate Axes
            for (let a = 0; a < Math.PI * 2; a += Math.PI / 4) {
                ctx.beginPath();
                ctx.moveTo(cx, cy);
                ctx.lineTo(cx + Math.cos(a + animAngle * 0.2) * 170, cy + Math.sin(a + animAngle * 0.2) * 170);
                ctx.stroke();
            }

            // Interconnecting Tensor Lattice Lines
            ctx.strokeStyle = 'rgba(255, 41, 44, 0.12)';
            ctx.beginPath();
            for (let i = 0; i < nodes.length; i++) {
                const n1 = nodes[i];
                const x1 = cx + Math.cos(n1.angle) * n1.radius;
                const y1 = cy + Math.sin(n1.angle) * n1.radius;
                for (let j = i + 1; j < nodes.length; j++) {
                    const n2 = nodes[j];
                    const x2 = cx + Math.cos(n2.angle) * n2.radius;
                    const y2 = cy + Math.sin(n2.angle) * n2.radius;
                    const dist = Math.hypot(x2 - x1, y2 - y1);
                    if (dist < 65) {
                        ctx.moveTo(x1, y1);
                        ctx.lineTo(x2, y2);
                    }
                }
            }
            ctx.stroke();

            // Central Singularity Node
            ctx.fillStyle = '#FF292C';
            ctx.shadowColor = '#FF292C';
            ctx.shadowBlur = 16;
            ctx.beginPath();
            ctx.arc(cx, cy, 6, 0, Math.PI * 2);
            ctx.fill();
            ctx.shadowBlur = 0;

            // Rotating Orbit Rings
            ctx.save();
            ctx.translate(cx, cy);
            ctx.rotate(animAngle);
            ctx.strokeStyle = 'rgba(255, 41, 44, 0.45)';
            ctx.setLineDash([8, 12]);
            ctx.beginPath();
            ctx.arc(0, 0, 115, 0, Math.PI * 2);
            ctx.stroke();
            ctx.restore();

            // Render Nodes
            for (let i = 0; i < nodes.length; i++) {
                const n = nodes[i];
                n.angle += n.speed;
                n.pulse += 0.05;

                const x = cx + Math.cos(n.angle) * n.radius;
                const y = cy + Math.sin(n.angle) * n.radius;

                if (n.isRed) {
                    ctx.fillStyle = '#FF292C';
                    ctx.shadowColor = '#FF292C';
                    ctx.shadowBlur = 8;
                } else {
                    ctx.fillStyle = '#F2F2F5';
                    ctx.shadowColor = 'transparent';
                    ctx.shadowBlur = 0;
                }

                ctx.beginPath();
                ctx.arc(x, y, n.size + Math.sin(n.pulse) * 0.8, 0, Math.PI * 2);
                ctx.fill();
            }

            animAngle += 0.003;
            requestAnimationFrame(drawSchematic);
        }
        drawSchematic();

        /* Realtime Slot & Latency Jitter Simulation */
        setInterval(() => {
            const slot = 312849200 + Math.floor(Date.now() / 400) % 100000;
            const slotEl = document.getElementById('tele-slot');
            if (slotEl) slotEl.textContent = 'Slot #' + slot.toLocaleString();

            const lat = (13.8 + Math.random() * 0.8).toFixed(1);
            const latEl = document.getElementById('tele-lat');
            if (latEl) latEl.textContent = lat + 'ms';
        }, 1200);

        /* 9. INTERACTIVE BYZANTINE FAULT SIMULATOR */
        const nodeMatrix = document.getElementById('node-matrix');
        const byzSlider = document.getElementById('byz-slider');
        const byzCountText = document.getElementById('byz-count-text');
        const byzRatioTag = document.getElementById('byz-ratio-tag');
        const simStatusBox = document.getElementById('sim-status-box');
        const simStatusTitle = document.getElementById('sim-status-title');
        const simStatusDesc = document.getElementById('sim-status-desc');

        const totalCommittee = 64;

        function buildNodeLattice() {
            if (!nodeMatrix) return;
            nodeMatrix.innerHTML = '';
            for (let i = 0; i < totalCommittee; i++) {
                const tile = document.createElement('div');
                tile.className = 'node-tile honest reveal-on-scroll reveal-init';
                tile.id = 'node-' + i;
                tile.textContent = (i + 1).toString().padStart(2, '0');
                nodeMatrix.appendChild(tile);
            }
        }
        buildNodeLattice();

        function updateByzantineSim() {
            if (!byzSlider) return;
            const f = parseInt(byzSlider.value);
            const pct = ((f / totalCommittee) * 100).toFixed(1);
            byzRatioTag.textContent = `f = ${f} / ${totalCommittee} (${pct}%)`;

            const maxTolerance = Math.floor((totalCommittee - 1) / 3); // 21 for 64 nodes

            if (f <= maxTolerance) {
                byzCountText.textContent = `f = ${f} (Safe < ${maxTolerance + 1})`;
                byzCountText.style.color = 'var(--laser-red)';
            } else {
                byzCountText.textContent = `f = ${f} (CRITICAL > 1/3 Byzantine)`;
                byzCountText.style.color = '#FF1744';
            }

            for (let i = 0; i < totalCommittee; i++) {
                const tile = document.getElementById('node-' + i);
                if (!tile) continue;
                tile.classList.remove('byzantine', 'honest', 'slashed');
                if (i < f) {
                    tile.classList.add('byzantine');
                } else {
                    tile.classList.add('honest');
                }
            }
        }
        updateByzantineSim();

        function runConsensusRound() {
            const f = parseInt(byzSlider.value);
            const maxTolerance = Math.floor((totalCommittee - 1) / 3);
            const attackType = document.getElementById('attack-vector-select').selectedOptions[0].text;

            if (f <= maxTolerance) {
                simStatusTitle.className = 'sim-status-head success';
                simStatusTitle.innerHTML = '[VALID] CONSENSUS VALIDATED: QUORUM REACHED';
                simStatusDesc.innerHTML = `
                    Attack: <strong>${attackType}</strong> thwarted.<br>
                    Honest nodes: ${totalCommittee - f}/${totalCommittee} (${((totalCommittee - f)/totalCommittee*100).toFixed(1)}%).
                    KZG verification rejected ${f} invalid proofs. Slashed: ${(f * 25000).toLocaleString()} $33RD.
                `;

                for (let i = 0; i < f; i++) {
                    const tile = document.getElementById('node-' + i);
                    if (tile) tile.className = 'node-tile slashed';
                }
            } else {
                simStatusTitle.className = 'sim-status-head alert';
                simStatusTitle.innerHTML = '[ALERT] BYZANTINE FAULT DETECTED: SAFETY HALT TRIGGERED';
                simStatusDesc.innerHTML = `
                    Adversary fraction exceeds BFT threshold (f = ${f} &gt; 21). 
                    Solana anchor initiates circuit breaker. No state finalized to preserve zero-knowledge safety.
                `;
            }
        }

        /* 10. SOLANA ANCHOR CLI TERMINAL */
        const termOutput = document.getElementById('terminal-output');
        const termInput = document.getElementById('terminal-input');

        function appendTermLine(text, type = '') {
            if (!termOutput) return;
            const div = document.createElement('div');
            div.className = 'terminal-line ' + type;
            div.innerHTML = text;
            termOutput.appendChild(div);
            termOutput.scrollTop = termOutput.scrollHeight;
        }

        function executeTermCommand(rawCmd) {
            const cmd = rawCmd.trim();
            if (!cmd) return;

            appendTermLine('&gt; ' + cmd, 'cmd');
            const c = cmd.toLowerCase();

            if (c === 'help') {
                appendTermLine('CANARY SPEC v4.0 &bull; DIAGNOSTIC COMMANDS:', 'highlight');
                appendTermLine('  status     - Query Solana anchor slot and committee state');
                appendTermLine('  nodes      - Inspect active Tier-1 GPU cluster telemetry');
                appendTermLine('  bench      - Execute simulated CAP-FFN LLaMA-3 PoI verification');
                appendTermLine('  verify     - Perform BN254 KZG polynomial opening check');
                appendTermLine('  byzantine  - Run Byzantine consensus fault assessment');
                appendTermLine('  tokenomics - Display hard cap, emission rates, & buyback crank');
                appendTermLine('  clear      - Clear terminal logs');
            } else if (c === 'status') {
                appendTermLine('[ANCHOR] Program ID: 33rdCore11111111111111111111111111111111111', 'highlight');
                appendTermLine('[CONSENSUS] Active Committee: K=64 / 64 nodes &bull; Slot Cadence: 400ms');
                appendTermLine('[STATE] Epoch 300 &bull; D_t = 1.042 &bull; Quorum: 2/3 BLS BN254 Verified', 'success');
                appendTermLine('[METRICS] Network Latency: 14.2ms &bull; 0 Slashing Events Recorded');
            } else if (c === 'nodes') {
                appendTermLine('ACTIVE VALIDATOR CLUSTERS (Sampling 4 of 33,492 clusters):', 'highlight');
                appendTermLine('  0x7F2A...9C1D [Tier-1 Dual H100 SXM5] &bull; Stake: 150,000 $33RD &bull; Status: OPTIMAL');
                appendTermLine('  0x3E11...B450 [Tier-1 Quad H100 SXM5] &bull; Stake: 250,000 $33RD &bull; Status: OPTIMAL');
                appendTermLine('  0x992B...C01F [Tier-1 B200 NVL72]    &bull; Stake: 500,000 $33RD &bull; Status: OPTIMAL');
                appendTermLine('  0x1A4C...33D8 [Tier-2 RTX 4090 Edge]  &bull; Stake: 35,000 $33RD  &bull; Status: ACTIVE');
            } else if (c === 'bench') {
                appendTermLine('[BENCH] Executing CAP-FFN LLaMA-3-8B PoI kernel challenge...', 'dim');
                setTimeout(() => {
                    appendTermLine('[BENCH] Randomized polynomial eval: Degree d=16 &bull; Chebyshev match', 'dim');
                    appendTermLine('[BENCH] Forward pass: 14.2ms &bull; Proof generated: 1.84ms &bull; OK', 'success');
                }, 300);
            } else if (c === 'verify') {
                appendTermLine('[KZG] Evaluating BN254 pairing: e(pi, [x - z]_2) == e(C - v*[1]_1, [1]_2)...', 'dim');
                setTimeout(() => {
                    appendTermLine('[KZG] Commitment opening verified on Solana &bull; Cost: 184,200 Compute Units', 'success');
                }, 350);
            } else if (c === 'byzantine') {
                appendTermLine('[BYZANTINE] Committee audit: K=64 nodes &bull; Current f=4 (6.2%)', 'highlight');
                appendTermLine('[BYZANTINE] Quorum threshold 2/3 + 1: SATISFIED (60 honest signatures)', 'success');
                appendTermLine('[BYZANTINE] Slashing collateral protection active at 33rdtreelabs.tech');
            } else if (c === 'tokenomics') {
                appendTermLine('TOKENOMICS & EMISSION PARAMETERS:', 'highlight');
                appendTermLine('  Hard Supply Cap : 33,000,000 $33RD');
                appendTermLine('  Current Epoch   : Epoch 0 (Years 1-4) &bull; 0.7135 $33RD / block');
                appendTermLine('  Buyback-Burn    : 10% commercial revenue routed to market burn');
                appendTermLine('  Burned To Date  : 412,840 $33RD (Deflationary)');
            } else if (c === 'clear') {
                termOutput.innerHTML = '';
            } else {
                appendTermLine(`Command not found: "${cmd}". Type "help" for valid options.`, 'warn');
            }
        }

        function handleTerminalSubmit(e) {
            e.preventDefault();
            const val = termInput.value;
            termInput.value = '';
            executeTermCommand(val);
        }

        /* 11. VALIDATOR YIELD & STAKING CALCULATOR */
        function calculateRewards() {
            const hwSelect = document.getElementById('calc-hw-select');
            const stakeSlider = document.getElementById('calc-stake-slider');
            const epochSelect = document.getElementById('calc-epoch-select');
            if (!hwSelect || !stakeSlider || !epochSelect) return;

            const hw = hwSelect.value;
            const stake = parseInt(stakeSlider.value);
            const epoch = parseInt(epochSelect.value);

            document.getElementById('calc-stake-display').textContent = stake.toLocaleString() + ' $33RD';

            let baseRewardsPerDay = 5136.99;
            if (epoch === 1) baseRewardsPerDay = 2568.49;
            if (epoch === 2) baseRewardsPerDay = 1284.25;
            if (epoch === 3) baseRewardsPerDay = 642.12;

            let hwMultiplier = 1.0;
            if (hw === 'dual-h100') hwMultiplier = 1.0;
            if (hw === 'quad-h100') hwMultiplier = 2.1;
            if (hw === 'cluster-b200') hwMultiplier = 5.4;
            if (hw === 'single-4090') hwMultiplier = 0.28;

            const validatorShare = (stake / 2500000) * hwMultiplier;
            const daily = baseRewardsPerDay * validatorShare;
            const monthly = daily * 30;
            const apy = ((daily * 365) / stake) * 100;
            const burnDaily = baseRewardsPerDay * 0.10;

            document.getElementById('calc-apy-val').textContent = apy.toFixed(1) + '%';
            document.getElementById('calc-daily-val').textContent = daily.toFixed(1) + ' $33RD';
            document.getElementById('calc-monthly-val').textContent = monthly.toFixed(1) + ' $33RD';
            document.getElementById('calc-burn-val').textContent = burnDaily.toFixed(1) + ' $33RD';
        }
        calculateRewards();

        /* ==========================================================================
           12. SCROLL TELEMETRY PROGRESS & ACTIVE SECTION TRACKER
           ========================================================================== */
        const trackedSections = [
            { id: 'hero', label: 'CANARY // OVERVIEW' },
            { id: 'singularity-stage', label: 'CANARY // STAGE' },
            { id: 'protocol', label: 'CANARY // PROTOCOL' },
            { id: 'simulator', label: 'CANARY // SIMULATOR' },
            { id: 'calculator', label: 'CANARY // YIELD' },
            { id: 'access-section', label: 'CANARY // ACCESS' }
        ];

        const navActiveBadge = document.getElementById('nav-active-section');
        const scrollProgressBar = document.getElementById('scroll-progress-line');

        function updateScrollTelemetry() {
            const doc = document.documentElement;
            const scrollY = window.scrollY || doc.scrollTop;
            const maxScroll = doc.scrollHeight - window.innerHeight;

            // Micro-progress line width
            if (scrollProgressBar && maxScroll > 0) {
                const pct = Math.min(100, Math.max(0, (scrollY / maxScroll) * 100));
                scrollProgressBar.style.width = pct + '%';
            }

            // Determine active section
            const triggerOffset = window.innerHeight * 0.35;
            let currentId = 'hero';
            let currentLabel = 'CANARY // OVERVIEW';

            if (scrollY + window.innerHeight >= doc.scrollHeight - 80) {
                currentId = 'access-section';
                currentLabel = 'CANARY // ACCESS';
            } else {
                for (const sec of trackedSections) {
                    const el = document.getElementById(sec.id);
                    if (el) {
                        const rect = el.getBoundingClientRect();
                        if (rect.top <= triggerOffset && rect.bottom > 0) {
                            currentId = sec.id;
                            currentLabel = sec.label;
                        }
                    }
                }
            }

            // Update nav pill links
            document.querySelectorAll('.nav-links .nav-link').forEach(link => {
                const href = link.getAttribute('href');
                if (href === '#' + currentId) {
                    link.classList.add('active');
                } else if (href && href.startsWith('#')) {
                    link.classList.remove('active');
                }
            });

            // Update nav telemetry badge
            if (navActiveBadge && navActiveBadge.textContent !== currentLabel) {
                navActiveBadge.textContent = currentLabel;
            }
        }

        window.addEventListener('scroll', updateScrollTelemetry, { passive: true });
        if (typeof lenis !== 'undefined') {
            lenis.on('scroll', updateScrollTelemetry);
        }
        updateScrollTelemetry();

        /* ==========================================================================
           13. INTERSECTION OBSERVER REVEAL ENGINE (JANK-FREE)
           ========================================================================== */
        const revealSelector = '.reveal-on-scroll, .node-tile, .stat-tile, .research-card, .section-title, .cta-title, .meta-tag, .arch-card, .stage-stat-card, .calc-stat-box';
        const revealElements = document.querySelectorAll(revealSelector);

        if ('IntersectionObserver' in window) {
            const revealObserver = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('is-revealed');
                        observer.unobserve(entry.target);
                    }
                });
            }, {
                root: null,
                rootMargin: '0px 0px -40px 0px',
                threshold: 0.08
            });

            revealElements.forEach(el => revealObserver.observe(el));

            const nodeMatrixEl = document.getElementById('node-matrix');
            if (nodeMatrixEl) {
                const matrixObserver = new IntersectionObserver((entries, observer) => {
                    entries.forEach(entry => {
                        if (entry.isIntersecting) {
                            const tiles = nodeMatrixEl.querySelectorAll('.node-tile');
                            tiles.forEach((tile, idx) => {
                                setTimeout(() => {
                                    tile.classList.add('is-revealed');
                                    tile.classList.remove('reveal-init');
                                }, idx * 8);
                            });
                            observer.unobserve(nodeMatrixEl);
                        }
                    });
                }, { threshold: 0.1 });
                matrixObserver.observe(nodeMatrixEl);
            }
        } else {
            revealElements.forEach(el => el.classList.add('is-revealed'));
        }
    </script>
</body>
</html>
"""

with open(output_file, "w", encoding="utf-8") as f:
    f.write(html_code)

print(f"Successfully generated {output_file} ({len(html_code)} bytes)")
