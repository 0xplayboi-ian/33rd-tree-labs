import os
import re

SITE_DIR = "/Users/ianmora/Desktop/Projects/33rd-tree-labs-site"

yield_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>33RD TREE LABS // Yield Architecture &amp; Protocol Economics &bull; 33rdtreelabs.tech</title>
    <meta name="description" content="Formal economic specification of the 75% Hardware Node Reward Pool, stake-weighted tensor multipliers (H100 SXM5, H200, B200, RTX 4090, CDNA3), 25,000 $33RD validator stake bond, and Solana Incinerator automated 10% fee burn deflation proof.">
    <meta name="theme-color" content="#070707">

    <!-- OpenGraph & Twitter Metadata -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://33rdtreelabs.tech/yield.html">
    <meta property="og:title" content="33RD TREE LABS // Yield Architecture &amp; Protocol Economics &bull; 33rdtreelabs.tech">
    <meta property="og:description" content="Formal economic specification of the 75% Hardware Node Reward Pool, stake-weighted tensor multipliers, 25,000 $33RD validator stake bond, and Solana Incinerator automated fee burn proofs.">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="33RD TREE LABS // Yield Architecture &amp; Protocol Economics &bull; 33rdtreelabs.tech">
    <meta name="twitter:description" content="Formal economic specification of the 75% Hardware Node Reward Pool, stake-weighted tensor multipliers, 25,000 $33RD validator stake bond, and Solana Incinerator automated fee burn proofs.">

    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous">
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=Space+Grotesk:wght@300;400;500;600;700&family=Syne:wght@700;800;900&display=swap" rel="stylesheet">

    <!-- KaTeX for Bit-Exact Mathematical Notation -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>

    <!-- Snappy Lenis & GSAP Engine -->
    <script src="https://cdn.jsdelivr.net/npm/@studio-freight/lenis@1.0.42/dist/lenis.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>

    <style>
        :root {
            /* 33RD TREE LABS DESIGN SYSTEM TOKENS */
            --f: #070707;
            --f-void: #000000;
            --f-elevated: #0B0B0E;
            --t: #FF2424;
            --t-glow: rgba(255, 36, 36, 0.45);
            --t-subtle: rgba(255, 36, 36, 0.08);
            --chalk: #F2F2F5;
            --chalk-dim: #D4D4DC;
            --dim: #8E8E98;
            --muted: #5A5A66;
            --white: #FFFFFF;
            --border: rgba(255, 255, 255, 0.12);
            --border-accent: rgba(255, 36, 36, 0.35);
            --green: #00E676;
            --green-glow: rgba(0, 230, 118, 0.35);

            --fd: 'Space Grotesk', -apple-system, BlinkMacSystemFont, sans-serif;
            --fm: 'JetBrains Mono', ui-monospace, monospace;
            --fh: 'Syne', -apple-system, sans-serif;
        }

        /* TYPOGRAPHY: OBEL MONO & MONO MASKED LOCAL FALLBACKS */
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

        *, *:before, *:after {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            cursor: default;
        }

        html {
            scroll-behavior: smooth;
            background: var(--f);
            color: var(--chalk);
            font-family: var(--fd);
            overflow-x: hidden;
            -webkit-text-size-adjust: 100%;
        }

        body {
            position: relative;
            min-height: 100vh;
            background: var(--f);
            color: var(--chalk);
            font-family: var(--fd);
            font-size: 15px;
            line-height: 1.6;
            overflow-x: hidden;
            -webkit-font-smoothing: antialiased;
        }

        /* CUSTOM RETRO-TECH CURSOR */
        #cursor-dot {
            width: 6px;
            height: 6px;
            background: var(--t);
            border-radius: 50%;
            position: fixed;
            pointer-events: none;
            z-index: 99999;
            transform: translate(-50%, -50%);
            box-shadow: 0 0 10px var(--t);
            transition: opacity 0.2s;
        }
        #cursor-ring {
            width: 32px;
            height: 32px;
            border: 1px solid rgba(255, 36, 36, 0.4);
            border-radius: 50%;
            position: fixed;
            pointer-events: none;
            z-index: 99998;
            transform: translate(-50%, -50%);
            transition: width 0.18s ease, height 0.18s ease, border-color 0.18s ease;
        }
        body.cursor-hover #cursor-ring {
            width: 48px;
            height: 48px;
            border-color: var(--t);
            background: var(--t-subtle);
        }

        /* TOP-EDGE SCROLL TELEMETRY PROGRESS LINE */
        #scroll-progress-line {
            position: fixed;
            top: 0;
            left: 0;
            width: 0%;
            height: 2px;
            background: var(--t);
            box-shadow: 0 0 10px var(--t), 0 0 20px var(--t-glow);
            z-index: 100000;
            pointer-events: none;
            transition: width 0.04s linear;
            will-change: width;
        }

        /* RIGHT TELEMETRY RAIL (SBAR) */
        .sbar {
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
        }
        .sbar__ticks {
            display: flex;
            flex-direction: column;
            gap: 5px;
            font-family: var(--fm);
            font-size: 8px;
            color: var(--dim);
            user-select: none;
        }
        .sbar__ticks span { line-height: 1; }
        .sbar__ticks span.active { color: var(--t); font-weight: 700; }
        .sbar__coord {
            font-family: var(--fm);
            font-size: 9px;
            color: var(--dim);
            writing-mode: vertical-rl;
            letter-spacing: 0.1em;
            user-select: none;
        }
        .sbar i {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            background: var(--t);
            box-shadow: 0 0 12px rgba(255, 36, 36, 0.85);
            will-change: transform;
            border-radius: 1px;
        }
        @media (hover: none) { .sbar { display: none; } }

        /* UNIFIED FLOATING PILL NAVBAR */
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
            background: rgba(11, 11, 14, 0.88);
            backdrop-filter: blur(16px) saturate(180%);
            -webkit-backdrop-filter: blur(16px) saturate(180%);
            border: 1px solid var(--border);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.75), 0 0 0 1px var(--t-subtle);
            pointer-events: auto;
            white-space: nowrap;
        }
        .nav-brand {
            display: flex;
            align-items: center;
            gap: 10px;
            text-decoration: none;
            color: #FFFFFF;
            border-right: 1px solid var(--border);
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
            font-family: var(--fm);
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
            font-family: var(--fm);
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
            background: rgba(255, 36, 36, 0.14);
            border-color: var(--t);
            box-shadow: 0 0 10px rgba(255, 36, 36, 0.35);
        }
        .nav-link.active::before {
            content: '';
            width: 4px;
            height: 4px;
            border-radius: 50%;
            background: var(--t);
            box-shadow: 0 0 6px var(--t);
            display: inline-block;
        }

        @media (max-width: 900px) {
            .nav-wrapper {
                top: 10px;
                left: 0;
                right: 0;
                transform: none;
                width: 100%;
                padding: 0 12px;
                box-sizing: border-box;
                display: flex;
                justify-content: center;
                pointer-events: auto;
            }
            .nav-pill {
                padding: 4px 8px;
                width: auto;
                max-width: calc(100vw - 24px);
                overflow-x: auto;
                -webkit-overflow-scrolling: touch;
                scrollbar-width: none;
                justify-content: flex-start;
            }
            .nav-pill::-webkit-scrollbar { display: none; }
            .nav-brand {
                position: sticky;
                left: 0;
                background: rgba(11, 11, 14, 0.95);
                z-index: 2;
                padding-right: 8px;
                margin-right: 8px;
            }
            .nav-title { display: none; }
            .nav-link {
                font-size: 10px;
                padding: 4px 8px;
                flex-shrink: 0;
            }
        }

        /* TABULAR NUMERICS ACROSS STATS, METRICS & CODE */
        table, td, th, code, pre, .mono, [data-mono], .terminal-text, .metric-value, .stat-value, .token-val, .sbar__coord, .telemetry-val, .calc-num {
            font-variant-numeric: tabular-nums;
            font-feature-settings: "tnum" 1;
        }

        /* GLOBAL RESPONSIVE CONTAINMENT ON SUBPAGES */
        .page-wrap {
            max-width: 1400px;
            margin: 0 auto;
            padding: 120px 32px 80px 32px;
            box-sizing: border-box;
            width: 100%;
        }
        @media (max-width: 900px) {
            .page-wrap {
                padding-top: 88px !important;
                padding-bottom: 48px;
                padding-left: 16px;
                padding-right: 16px;
            }
        }

        /* EDITORIAL HEADER / HERO */
        .hero-kicker {
            font-family: var(--fm);
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 0.18em;
            color: var(--t);
            text-transform: uppercase;
            margin-bottom: 14px;
            display: inline-block;
        }
        .hero-title {
            font-family: var(--fh);
            font-size: clamp(32px, 5.2vw, 68px);
            font-weight: 900;
            line-height: 0.98;
            letter-spacing: -0.03em;
            text-transform: uppercase;
            color: var(--white);
            margin-bottom: 22px;
        }
        .hero-title .accent {
            color: var(--t);
            text-shadow: 0 0 35px var(--t-glow);
        }
        .hero-desc {
            font-size: clamp(15px, 1.25vw, 18px);
            line-height: 1.65;
            color: var(--chalk-dim);
            max-width: 860px;
            font-weight: 400;
            margin-bottom: 44px;
        }

        /* TELEMETRY STRIP - OPEN EDITORIAL HAIRLINE GRID */
        .telemetry-strip {
            display: grid;
            grid-template-columns: repeat(6, 1fr);
            border-top: 1px solid var(--border);
            border-bottom: 1px solid var(--border);
            margin-bottom: 72px;
            background: transparent;
        }
        @media (max-width: 1100px) {
            .telemetry-strip { grid-template-columns: repeat(3, 1fr); }
        }
        @media (max-width: 640px) {
            .telemetry-strip { grid-template-columns: repeat(2, 1fr); }
        }
        .telemetry-cell {
            padding: 20px 18px;
            border-right: 1px solid var(--border);
            display: flex;
            flex-direction: column;
            gap: 6px;
            background: transparent;
        }
        .telemetry-cell:last-child {
            border-right: none;
        }
        @media (max-width: 1100px) {
            .telemetry-cell:nth-child(3) { border-right: none; }
        }
        @media (max-width: 640px) {
            .telemetry-cell:nth-child(2), .telemetry-cell:nth-child(4) { border-right: none; }
        }
        .telemetry-label {
            font-family: var(--fm);
            font-size: 10px;
            color: var(--dim);
            text-transform: uppercase;
            letter-spacing: 0.12em;
        }
        .telemetry-value {
            font-family: var(--fm);
            font-size: 14.5px;
            font-weight: 700;
            color: var(--chalk);
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }
        .telemetry-value.accent {
            color: var(--t);
        }
        .telemetry-value.green {
            color: var(--green);
        }

        /* OPEN BRUTALIST SECTIONS (ZERO CARDS, DELINEATED BY HAIRLINES) */
        .ed-section {
            border-top: 1px solid var(--border);
            padding: 72px 0;
            position: relative;
        }
        .ed-section:last-of-type {
            border-bottom: 1px solid var(--border);
        }
        .ed-sec-header {
            margin-bottom: 36px;
        }
        .ed-sec-num {
            font-family: var(--fm);
            font-size: 11px;
            font-weight: 700;
            color: var(--t);
            letter-spacing: 0.16em;
            text-transform: uppercase;
            margin-bottom: 10px;
            display: block;
        }
        .ed-sec-title {
            font-family: var(--fh);
            font-size: clamp(24px, 3.4vw, 38px);
            font-weight: 800;
            letter-spacing: -0.02em;
            color: var(--white);
            text-transform: uppercase;
            margin-bottom: 14px;
            line-height: 1.1;
        }
        .ed-sec-lede {
            font-family: var(--fd);
            font-size: 15.5px;
            line-height: 1.68;
            color: var(--dim);
            max-width: 880px;
        }

        /* ==================================================================== */
        /* OPEN MATHEMATICAL PARAMETRIC YIELD CALCULATOR                        */
        /* (ZERO BOXED PANELS - STARK OPEN TWO-COLUMN EDITORIAL DIVISION)        */
        /* ==================================================================== */
        .calc-workbench {
            border-top: 1px solid var(--border);
            border-bottom: 1px solid var(--border);
            margin-top: 36px;
            margin-bottom: 72px;
            background: transparent;
        }
        .calc-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid var(--border);
            padding: 12px 0;
            font-family: var(--fm);
            font-size: 10.5px;
            letter-spacing: 0.12em;
            color: var(--dim);
            text-transform: uppercase;
        }
        .calc-bar .status-live {
            color: var(--green);
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }
        .calc-bar .status-live::before {
            content: '';
            width: 6px;
            height: 6px;
            border-radius: 50%;
            background: var(--green);
            box-shadow: 0 0 8px var(--green-glow);
        }

        .calc-split-grid {
            display: grid;
            grid-template-columns: 1.15fr 0.85fr;
            background: transparent;
        }
        @media (max-width: 1024px) {
            .calc-split-grid {
                grid-template-columns: 1fr;
            }
        }

        /* LEFT COLUMN: PARAMETER INPUTS */
        .calc-inputs-pane {
            padding: 36px 40px 36px 0;
            border-right: 1px solid var(--border);
            display: flex;
            flex-direction: column;
            gap: 28px;
            background: transparent;
        }
        @media (max-width: 1024px) {
            .calc-inputs-pane {
                border-right: none;
                border-bottom: 1px solid var(--border);
                padding: 28px 0;
            }
        }

        .calc-field {
            display: flex;
            flex-direction: column;
            gap: 8px;
        }
        .calc-field-head {
            display: flex;
            justify-content: space-between;
            align-items: baseline;
            font-family: var(--fm);
            font-size: 11px;
            color: var(--dim);
            text-transform: uppercase;
            letter-spacing: 0.1em;
        }
        .calc-field-head .val-tag {
            font-family: var(--fm);
            font-weight: 700;
            color: var(--white);
            font-size: 12.5px;
        }
        .calc-field-head .val-tag.bond-secure {
            color: var(--green);
        }
        .calc-field-head .val-tag.bond-alert {
            color: var(--t);
        }

        .calc-select {
            width: 100%;
            background: #000000;
            border: 1px solid var(--border);
            color: var(--white);
            font-family: var(--fm);
            font-size: 12px;
            padding: 12px 14px;
            outline: none;
            transition: border-color 0.2s ease, box-shadow 0.2s ease;
            border-radius: 0;
            -webkit-appearance: none;
            appearance: none;
            cursor: pointer;
            background-image: url("data:image/svg+xml;charset=UTF-8,%3Csvg width='10' height='6' viewBox='0 0 10 6' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M1 1L5 5L9 1' stroke='%23FF2424' stroke-width='1.5' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E");
            background-repeat: no-repeat;
            background-position: right 14px center;
            background-size: 10px 6px;
        }
        .calc-select:focus, .calc-select:hover {
            border-color: var(--t);
            box-shadow: 0 0 12px rgba(255, 36, 36, 0.25);
        }

        .calc-slider {
            width: 100%;
            -webkit-appearance: none;
            appearance: none;
            background: #141419;
            height: 4px;
            border-radius: 0;
            outline: none;
            cursor: pointer;
            margin: 6px 0;
        }
        .calc-slider::-webkit-slider-thumb {
            -webkit-appearance: none;
            appearance: none;
            width: 16px;
            height: 16px;
            background: var(--t);
            cursor: pointer;
            box-shadow: 0 0 12px var(--t);
            border: 1px solid var(--white);
            border-radius: 0;
            transition: transform 0.1s ease;
        }
        .calc-slider::-webkit-slider-thumb:hover {
            transform: scale(1.15);
        }
        .calc-slider-scale {
            display: flex;
            justify-content: space-between;
            font-family: var(--fm);
            font-size: 9.5px;
            color: var(--muted);
            letter-spacing: 0.05em;
        }

        /* RIGHT COLUMN: MATHEMATICAL TELEMETRY & RESULTS */
        .calc-telemetry-pane {
            padding: 36px 0 36px 40px;
            background: transparent;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }
        @media (max-width: 1024px) {
            .calc-telemetry-pane {
                padding: 28px 0;
            }
        }

        .calc-hero-metric {
            padding-bottom: 24px;
            border-bottom: 1px solid var(--border);
            margin-bottom: 24px;
        }
        .calc-hero-label {
            font-family: var(--fm);
            font-size: 11px;
            color: var(--dim);
            text-transform: uppercase;
            letter-spacing: 0.14em;
            margin-bottom: 8px;
            display: block;
        }
        .calc-hero-num {
            font-family: var(--fh);
            font-size: clamp(48px, 5.5vw, 76px);
            font-weight: 900;
            line-height: 0.9;
            letter-spacing: -0.04em;
            color: var(--t);
            text-shadow: 0 0 32px var(--t-glow);
            font-variant-numeric: tabular-nums;
            margin-bottom: 6px;
        }
        .calc-hero-sub {
            font-family: var(--fm);
            font-size: 11px;
            color: var(--chalk-dim);
        }

        .calc-rows-stack {
            display: flex;
            flex-direction: column;
        }
        .calc-row {
            display: flex;
            justify-content: space-between;
            align-items: baseline;
            padding: 10px 0;
            border-bottom: 1px solid rgba(255, 255, 255, 0.06);
            background: transparent;
        }
        .calc-row:last-child {
            border-bottom: none;
        }
        .calc-row-label {
            font-family: var(--fm);
            font-size: 11px;
            color: var(--dim);
            text-transform: uppercase;
            letter-spacing: 0.08em;
        }
        .calc-row-val {
            font-family: var(--fm);
            font-size: 15px;
            font-weight: 700;
            color: var(--white);
            font-variant-numeric: tabular-nums;
        }
        .calc-row-val.accent {
            color: var(--t);
        }
        .calc-row-val.green {
            color: var(--green);
        }

        .calc-diagnostic-terminal {
            margin-top: 28px;
            padding-top: 16px;
            border-top: 1px solid var(--border);
            font-family: var(--fm);
            font-size: 10.5px;
            line-height: 1.55;
            color: var(--dim);
            background: transparent;
        }
        .calc-diagnostic-terminal pre {
            white-space: pre-wrap;
            word-break: break-all;
            margin: 0;
            font-family: var(--fm);
        }

        /* ==================================================================== */
        /* OPEN MATHEMATICAL PROOF & FORMULATION BLOCKS                        */
        /* ==================================================================== */
        .math-open-block {
            border-top: 1px solid var(--border);
            border-bottom: 1px solid var(--border);
            padding: 32px 0;
            margin: 32px 0;
            background: transparent;
        }
        .math-formula-lead {
            font-family: var(--fm);
            font-size: 11px;
            color: var(--t);
            letter-spacing: 0.14em;
            text-transform: uppercase;
            margin-bottom: 12px;
        }
        .math-formula-raw {
            font-size: 18px;
            color: var(--white);
            margin: 20px 0;
            padding: 16px 0;
            border-top: 1px solid rgba(255, 255, 255, 0.06);
            border-bottom: 1px solid rgba(255, 255, 255, 0.06);
            overflow-x: auto;
            text-align: center;
        }
        .math-vars-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 16px 36px;
            margin-top: 20px;
            font-family: var(--fm);
            font-size: 11.5px;
            line-height: 1.6;
            color: var(--chalk-dim);
        }
        @media (max-width: 800px) {
            .math-vars-grid { grid-template-columns: 1fr; }
        }
        .math-vars-grid .var-sym {
            color: var(--t);
            font-weight: 700;
        }

        /* OPEN EDITORIAL SPECIFICATION TABLES */
        .open-table-container {
            width: 100%;
            overflow-x: auto;
            -webkit-overflow-scrolling: touch;
            margin: 32px 0 48px 0;
            border-top: 1px solid var(--border);
            border-bottom: 1px solid var(--border);
            background: transparent;
        }
        .open-ed-table {
            width: 100%;
            border-collapse: collapse;
            font-family: var(--fm);
            font-size: 12px;
            text-align: left;
            background: transparent;
        }
        .open-ed-table th {
            padding: 14px 18px;
            color: var(--dim);
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            border-bottom: 1px solid var(--border);
            border-right: 1px solid rgba(255, 255, 255, 0.06);
            background: transparent;
            white-space: nowrap;
        }
        .open-ed-table th:last-child {
            border-right: none;
        }
        .open-ed-table td {
            padding: 14px 18px;
            color: var(--chalk);
            border-bottom: 1px solid rgba(255, 255, 255, 0.06);
            border-right: 1px solid rgba(255, 255, 255, 0.06);
            background: transparent;
            white-space: nowrap;
        }
        .open-ed-table td:last-child {
            border-right: none;
        }
        .open-ed-table tr:last-child td {
            border-bottom: none;
        }
        .open-ed-table tr:hover td {
            background: rgba(255, 36, 36, 0.03);
            color: #FFFFFF;
        }
        .open-ed-table td.highlight {
            color: var(--t);
            font-weight: 700;
        }
        .open-ed-table td.green {
            color: var(--green);
            font-weight: 700;
        }
        .open-ed-table td.code-cell {
            font-size: 11px;
            color: var(--chalk-dim);
        }

        /* OPEN EDITORIAL SPLIT GRID */
        .open-split-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            border-top: 1px solid var(--border);
            border-bottom: 1px solid var(--border);
            margin: 36px 0;
            background: transparent;
        }
        @media (max-width: 860px) {
            .open-split-grid { grid-template-columns: 1fr; }
        }
        .open-split-col {
            padding: 32px 36px 32px 0;
            border-right: 1px solid var(--border);
            background: transparent;
        }
        .open-split-col:last-child {
            padding: 32px 0 32px 36px;
            border-right: none;
        }
        @media (max-width: 860px) {
            .open-split-col {
                padding: 24px 0 !important;
                border-right: none;
                border-bottom: 1px solid var(--border);
            }
            .open-split-col:last-child {
                border-bottom: none;
            }
        }
        .open-col-kicker {
            font-family: var(--fm);
            font-size: 11px;
            font-weight: 700;
            color: var(--t);
            letter-spacing: 0.12em;
            text-transform: uppercase;
            margin-bottom: 12px;
            display: block;
        }
        .open-col-title {
            font-family: var(--fh);
            font-size: 20px;
            font-weight: 800;
            color: var(--white);
            text-transform: uppercase;
            margin-bottom: 14px;
            letter-spacing: -0.01em;
        }
        .open-col-text {
            font-family: var(--fd);
            font-size: 14px;
            line-height: 1.65;
            color: var(--dim);
            margin-bottom: 14px;
        }

        /* OPEN HORIZONTAL TIMELINE STRIP */
        .open-timeline-strip {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            border-top: 1px solid var(--border);
            border-bottom: 1px solid var(--border);
            margin: 36px 0;
            background: transparent;
        }
        @media (max-width: 900px) {
            .open-timeline-strip { grid-template-columns: 1fr; }
        }
        .open-timeline-cell {
            padding: 24px 20px;
            border-right: 1px solid var(--border);
            background: transparent;
            display: flex;
            flex-direction: column;
            gap: 8px;
        }
        .open-timeline-cell:last-child {
            border-right: none;
        }
        @media (max-width: 900px) {
            .open-timeline-cell {
                border-right: none;
                border-bottom: 1px solid var(--border);
                padding: 20px 0;
            }
            .open-timeline-cell:last-child { border-bottom: none; }
        }
        .timeline-step-tag {
            font-family: var(--fm);
            font-size: 10px;
            font-weight: 700;
            color: var(--t);
            letter-spacing: 0.14em;
            text-transform: uppercase;
        }
        .timeline-step-title {
            font-family: var(--fm);
            font-size: 12.5px;
            font-weight: 700;
            color: var(--white);
            text-transform: uppercase;
        }
        .timeline-step-desc {
            font-family: var(--fd);
            font-size: 12.5px;
            line-height: 1.55;
            color: var(--dim);
        }

        /* OPEN RAW ASCII FLOW DIAGRAM */
        .open-ascii-block {
            border-top: 1px solid var(--border);
            border-bottom: 1px solid var(--border);
            padding: 24px 0;
            margin: 32px 0;
            overflow-x: auto;
            font-family: var(--fm);
            font-size: 11px;
            line-height: 1.45;
            color: #C0C0D0;
            background: transparent;
        }
        .open-ascii-block .accent {
            color: var(--t);
            font-weight: 700;
        }
        .open-ascii-block .green {
            color: var(--green);
            font-weight: 700;
        }
        .open-ascii-block .dim {
            color: var(--muted);
        }

        /* OPEN BRUTALIST CODE EXHIBIT */
        .open-code-exhibit {
            border-top: 1px solid var(--border);
            border-bottom: 1px solid var(--border);
            margin: 32px 0 48px 0;
            background: var(--f-void);
        }
        .open-code-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px 16px;
            border-bottom: 1px solid var(--border);
            font-family: var(--fm);
            font-size: 11px;
            color: var(--dim);
            letter-spacing: 0.08em;
            background: transparent;
        }
        .open-code-header .file-path {
            color: var(--white);
            font-weight: 700;
        }
        .open-code-content {
            padding: 24px 20px;
            overflow-x: auto;
            font-family: var(--fm);
            font-size: 11.5px;
            line-height: 1.65;
            color: #C4C4D4;
            background: transparent;
        }
        .open-code-content code {
            font-family: inherit;
        }
        .open-code-content .kw { color: var(--t); font-weight: 700; }
        .open-code-content .ty { color: #64B5F6; }
        .open-code-content .fn { color: #81C784; }
        .open-code-content .cm { color: #626274; font-style: italic; }
        .open-code-content .str { color: #FFD54F; }

        /* GLOBAL FOOTER */
        .global-footer {
            background: var(--f-void);
            border-top: 1px solid var(--border);
            padding: 56px 32px 48px;
            margin-top: 80px;
        }
        .footer-inner {
            max-width: 1400px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 24px;
        }
        .footer-brand {
            font-family: var(--fm);
            font-size: 11.5px;
            color: var(--dim);
            letter-spacing: 0.08em;
        }
        .footer-brand strong {
            color: var(--white);
        }
        .footer-links {
            display: flex;
            gap: 16px;
            flex-wrap: wrap;
        }
        .footer-link {
            font-family: var(--fm);
            font-size: 11px;
            color: var(--dim);
            text-decoration: none;
            letter-spacing: 0.08em;
            transition: color 0.18s ease;
        }
        .footer-link:hover {
            color: var(--t);
        }
        .footer-link.active {
            color: var(--t);
            font-weight: 700;
        }

        /* REVEAL ON SCROLL INTERSECTION ANIMATION */
        .reveal-on-scroll {
            opacity: 0;
            transform: translateY(18px);
            transition: opacity 0.6s cubic-bezier(0.16, 1, 0.3, 1), transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
            will-change: opacity, transform;
        }
        .reveal-on-scroll.is-revealed {
            opacity: 1;
            transform: translateY(0);
        }
    </style>
</head>
<body>

    <!-- TOP-EDGE SCROLL TELEMETRY PROGRESS LINE -->
    <div id="scroll-progress-line" aria-hidden="true"></div>

    <!-- RIGHT TELEMETRY RAIL (SBAR) -->
    <aside class="sbar" id="telemetryRail" aria-hidden="true">
        <div class="sbar__ticks">
            <span class="active">00</span>
            <span>01</span>
            <span>02</span>
            <span>03</span>
            <span>04</span>
            <span>05</span>
            <span>06</span>
            <span>07</span>
        </div>
        <div class="sbar__coord" id="railYCoord">Y: +0000PX</div>
        <i id="sbarThumb"></i>
    </aside>

    <!-- CUSTOM RETRO-TECH CURSOR -->
    <div id="cursor-dot"></div>
    <div id="cursor-ring"></div>

    <!-- UNIFIED FLOATING PILL NAVBAR -->
    <div class="nav-wrapper">
        <nav class="nav-pill">
            <a href="index.html" class="nav-brand">
                <div class="nav-logo-box">
                    <svg viewBox="0 0 24 24" width="22" height="22" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <ellipse cx="12" cy="4" rx="8.5" ry="2" stroke="#FFFFFF" stroke-width="0.9" fill="none"/>
                        <ellipse cx="12" cy="20" rx="8.5" ry="2" stroke="#FFFFFF" stroke-width="0.9" fill="none"/>
                        <path d="M 3.5 4 C 8.5 7, 10.5 10, 10.5 12 C 10.5 14, 8.5 17, 3.5 20" stroke="#FFFFFF" stroke-width="1.1" fill="none" stroke-linecap="round"/>
                        <path d="M 20.5 4 C 15.5 7, 13.5 10, 13.5 12 C 13.5 14, 15.5 17, 20.5 20" stroke="#FFFFFF" stroke-width="1.1" fill="none" stroke-linecap="round"/>
                        <line x1="12" y1="2" x2="12" y2="22" stroke="#FF2424" stroke-width="1.1" stroke-dasharray="1.5 1.5"/>
                        <circle cx="12" cy="12" r="1.8" fill="#FF2424"/>
                    </svg>
                </div>
                <span class="nav-title" data-glitch>33RD TREE LABS</span>
            </a>

            <div class="nav-links">
                <a href="index.html" class="nav-link" data-glitch>[ OVERVIEW ]</a>
                <a href="protocol.html" class="nav-link" data-glitch>[ PROTOCOL ]</a>
                <a href="simulator.html" class="nav-link" data-glitch>[ SIMULATOR ]</a>
                <a href="yield.html" class="nav-link active" data-glitch>[ YIELD ]</a>
                <a href="nodes.html" class="nav-link" data-glitch>[ NODES ]</a>
                <a href="tokenomics.html" class="nav-link" data-glitch>[ TOKENOMICS ]</a>
                <a href="research.html" class="nav-link" data-glitch>[ RESEARCH ]</a>
            </div>
        </nav>
    </div>

    <!-- MAIN PAGE WRAPPER -->
    <main class="page-wrap">

        <!-- EDITORIAL HERO / HEADER -->
        <header class="ed-hero">
            <span class="hero-kicker" data-glitch>[ PROTOCOL ECONOMICS // SECTION 03 &bull; CANARY SPECIFICATION v4.2 ]</span>
            <h1 class="hero-title" data-glitch>VALIDATOR REWARDS &amp; <span class="accent">QUANTITATIVE YIELD</span></h1>
            <p class="hero-desc">
                Mathematical specifications of the 75% Hardware Node Reward Pool, exact accelerator multipliers (H100 SXM5, H200, B200, RTX 4090, CDNA3), the canonical 25,000 $33RD validator stake bond requirement, and formal proof of net token deflation via the Solana Incinerator.
            </p>
        </header>

        <!-- TELEMETRY STRIP -->
        <div class="telemetry-strip">
            <div class="telemetry-cell">
                <span class="telemetry-label">Canonical Hard Cap</span>
                <span class="telemetry-value">33,333,333 $33RD</span>
            </div>
            <div class="telemetry-cell">
                <span class="telemetry-label">Compute Subsidy Pool</span>
                <span class="telemetry-value">15,000,000 $33RD</span>
            </div>
            <div class="telemetry-cell">
                <span class="telemetry-label">Epoch Slot Cadence</span>
                <span class="telemetry-value">12.0 Seconds</span>
            </div>
            <div class="telemetry-cell">
                <span class="telemetry-label">Minimum Validator Bond</span>
                <span class="telemetry-value accent">25,000 $33RD</span>
            </div>
            <div class="telemetry-cell">
                <span class="telemetry-label">Protocol Fee Routing</span>
                <span class="telemetry-value">75% / 15% / 10%</span>
            </div>
            <div class="telemetry-cell">
                <span class="telemetry-label">Canonical Target</span>
                <span class="telemetry-value">33rdtreelabs.tech</span>
            </div>
        </div>

        <!-- ==================================================================== -->
        <!-- INTERACTIVE PARAMETRIC YIELD & DEFLATION ENGINE                      -->
        <!-- ==================================================================== -->
        <section class="ed-section" style="border-top:none; padding-top:0;">
            <div class="ed-sec-header">
                <span class="ed-sec-num">[ ENGINE 00 // LIVE PARAMETRIC SIMULATOR ]</span>
                <h2 class="ed-sec-title">PARAMETRIC VALIDATOR YIELD &amp; DEFLATION CALCULATOR</h2>
                <p class="ed-sec-lede">
                    Simulate validator rewards and network deflation velocity under real protocol parameters. Adjust accelerator architectures, active cluster size, bonded collateral, verified compute utilization, emission halving eras, and aggregate fee volumes.
                </p>
            </div>

            <div class="calc-workbench">
                <div class="calc-bar">
                    <span>[ LIVE INSTRUMENT: QUANTITATIVE YIELD v4.2 ]</span>
                    <span class="status-live">SOLANA ANCHOR STATE: SYNCHRONIZED</span>
                </div>

                <div class="calc-split-grid">
                    <!-- CONTROLS PANE -->
                    <div class="calc-inputs-pane">
                        <!-- HARDWARE TIER SELECT -->
                        <div class="calc-field">
                            <div class="calc-field-head">
                                <span>Accelerator Architecture Tier</span>
                                <span class="val-tag" id="sim-hw-multiplier-tag">4.8x WEIGHT</span>
                            </div>
                            <select id="sim-hw" class="calc-select" onchange="calculateValidatorYield()">
                                <option value="b200">NVIDIA Blackwell B200 (192GB HBM3e, 8.0 TB/s NVLink) [8.2x Multiplier]</option>
                                <option value="cdna3">AMD CDNA3 MI300X (192GB HBM3, 5.3 TB/s Infinity Fabric) [6.8x Multiplier]</option>
                                <option value="h200">NVIDIA Hopper H200 (141GB HBM3e, 4.8 TB/s NVLink 4.0) [6.0x Multiplier]</option>
                                <option value="h100" selected>NVIDIA Hopper H100 SXM5 (80GB HBM3, 3.35 TB/s NVLink 4.0) [4.8x Multiplier]</option>
                                <option value="rtx4090">NVIDIA GeForce RTX 4090 (24GB GDDR6X, PCIe Gen4 x16) [1.0x Edge Base]</option>
                            </select>
                        </div>

                        <!-- NODE COUNT SLIDER -->
                        <div class="calc-field">
                            <div class="calc-field-head">
                                <span>Active Cluster Validator Nodes (N)</span>
                                <span class="val-tag" id="sim-nodes-val">4 NODES</span>
                            </div>
                            <input type="range" id="sim-nodes" class="calc-slider" min="1" max="32" step="1" value="4" oninput="calculateValidatorYield()">
                            <div class="calc-slider-scale">
                                <span>1 Node (Solo)</span>
                                <span>8 Nodes</span>
                                <span>16 Nodes</span>
                                <span>32 Nodes (Data Center)</span>
                            </div>
                        </div>

                        <!-- BONDED COLLATERAL SLIDER -->
                        <div class="calc-field">
                            <div class="calc-field-head">
                                <span>Bonded Collateral ($33RD)</span>
                                <span class="val-tag bond-secure" id="sim-stake-val">100,000 $33RD (SECURED)</span>
                            </div>
                            <input type="range" id="sim-stake" class="calc-slider" min="25000" max="1000000" step="5000" value="100000" oninput="calculateValidatorYield()">
                            <div class="calc-slider-scale">
                                <span id="sim-stake-min-label">Min: 100,000 $33RD (25k / node)</span>
                                <span>500,000 $33RD</span>
                                <span>1,000,000 $33RD</span>
                            </div>
                        </div>

                        <!-- UTILIZATION & UPTIME SLIDER -->
                        <div class="calc-field">
                            <div class="calc-field-head">
                                <span>Compute Utilization &amp; Proof Attestation (U_i)</span>
                                <span class="val-tag" id="sim-util-val">85%</span>
                            </div>
                            <input type="range" id="sim-util" class="calc-slider" min="20" max="100" step="5" value="85" oninput="calculateValidatorYield()">
                            <div class="calc-slider-scale">
                                <span>20% (Idle Standby)</span>
                                <span>60%</span>
                                <span>85% (Standard)</span>
                                <span>100% (Peak Saturation)</span>
                            </div>
                        </div>

                        <!-- EMISSION HALVING ERA SELECT -->
                        <div class="calc-field">
                            <div class="calc-field-head">
                                <span>Emission Halving Era</span>
                                <span class="val-tag" id="sim-era-val">5,136.99 $33RD / DAY</span>
                            </div>
                            <select id="sim-era" class="calc-select" onchange="calculateValidatorYield()">
                                <option value="1" selected>Era 1 (Years 1&ndash;4) &bull; 5,136.986 $33RD / day (0.7135 / block)</option>
                                <option value="2">Era 2 (Years 5&ndash;8) &bull; 2,568.493 $33RD / day (0.3567 / block)</option>
                                <option value="3">Era 3 (Years 9&ndash;12) &bull; 1,284.246 $33RD / day (0.1784 / block)</option>
                                <option value="4">Era 4 (Years 13&ndash;16) &bull; 642.123 $33RD / day (0.0892 / block)</option>
                            </select>
                        </div>

                        <!-- DAILY INVOICED FEE VOLUME SLIDER -->
                        <div class="calc-field">
                            <div class="calc-field-head">
                                <span>Daily Invoiced Fee Volume</span>
                                <span class="val-tag" id="sim-fees-val">65,000 $33RD / DAY</span>
                            </div>
                            <input type="range" id="sim-fees" class="calc-slider" min="5000" max="250000" step="5000" value="65000" oninput="calculateValidatorYield()">
                            <div class="calc-slider-scale">
                                <span>5,000 $33RD</span>
                                <span>51,370 (Burn Floor)</span>
                                <span>150,000</span>
                                <span>250,000 $33RD</span>
                            </div>
                        </div>
                    </div>

                    <!-- TELEMETRY READOUTS PANE -->
                    <div class="calc-telemetry-pane">
                        <div class="calc-hero-metric">
                            <span class="calc-hero-label">Estimated Validator APY (Annualized)</span>
                            <div class="calc-hero-num" id="res-apy">791.7%</div>
                            <div class="calc-hero-sub">Based on verified PoI power share, scheduled emissions, and 75% fee distribution.</div>
                        </div>

                        <div class="calc-rows-stack">
                            <div class="calc-row">
                                <span class="calc-row-label">Per-Epoch Reward (12.0s Slot)</span>
                                <span class="calc-row-val" id="res-epoch">0.3013 $33RD</span>
                            </div>
                            <div class="calc-row">
                                <span class="calc-row-label">Projected Daily Rewards</span>
                                <span class="calc-row-val" id="res-daily">2,169.09 $33RD</span>
                            </div>
                            <div class="calc-row">
                                <span class="calc-row-label">Projected Monthly Rewards (30D)</span>
                                <span class="calc-row-val" id="res-monthly">65,072.7 $33RD</span>
                            </div>
                            <div class="calc-row">
                                <span class="calc-row-label">Projected Annual Rewards (365D)</span>
                                <span class="calc-row-val" id="res-annual">791,718 $33RD</span>
                            </div>
                            <div class="calc-row">
                                <span class="calc-row-label">Effective Cluster Power</span>
                                <span class="calc-row-val" id="res-cluster-weight">19.2x (4.8x * 4)</span>
                            </div>
                            <div class="calc-row">
                                <span class="calc-row-label">Network PoI Power Share</span>
                                <span class="calc-row-val" id="res-network-share">4.025%</span>
                            </div>
                            <div class="calc-row">
                                <span class="calc-row-label">Solana Incinerator Daily Burn (10%)</span>
                                <span class="calc-row-val accent" id="res-burn-daily">6,500.0 $33RD</span>
                            </div>
                            <div class="calc-row">
                                <span class="calc-row-label">Treasury R&amp;D Multisig (15%)</span>
                                <span class="calc-row-val" id="res-treasury-daily">9,750.0 $33RD</span>
                            </div>
                            <div class="calc-row">
                                <span class="calc-row-label">Network Supply Trajectory</span>
                                <span class="calc-row-val green" id="res-deflation-status">NET DEFLATIONARY (-1,363.0 / DAY)</span>
                            </div>
                        </div>

                        <div class="calc-diagnostic-terminal">
                            <pre id="res-diagnostic-log"></pre>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- ==================================================================== -->
        <!-- SECTION 01: 75% HARDWARE NODE REWARD POOL SPECIFICATION             -->
        <!-- ==================================================================== -->
        <section class="ed-section">
            <div class="ed-sec-header">
                <span class="ed-sec-num">[ SECTION 01 // PROTOCOL ECONOMICS ]</span>
                <h2 class="ed-sec-title">75% HARDWARE NODE REWARD POOL</h2>
                <p class="ed-sec-lede">
                    The Singularity Protocol allocates 75% of aggregate protocol revenue directly to active compute node operators. Payouts are computed deterministically per 12.0s consensus slot based on verified tensor execution, hardware throughput weighting, and TEE zero-knowledge proof validity.
                </p>
            </div>

            <div class="math-open-block">
                <div class="math-formula-lead">FORMULATION: DETERMINISTIC EPOCH REWARD DISTRIBUTION</div>
                <div class="math-formula-raw">
                    $$R_{\text{epoch}}(i) = \frac{W_i \cdot U_i}{\sum_{j=1}^{N} (W_j \cdot U_j)} \times \mathcal{Y}_{\text{pool}}$$
                </div>
                <div class="math-vars-grid">
                    <div>
                        <span class="var-sym">R_{\text{epoch}}(i)</span> : Reward in $33RD credited to validator $i$ for each committed 12.0s slot.
                    </div>
                    <div>
                        <span class="var-sym">W_i</span> : Hardware architecture weight multiplier verified on-chain via TEE quotes and bit-exact GEMM benchmarks.
                    </div>
                    <div>
                        <span class="var-sym">U_i</span> : Attested uptime coefficient ($0.0 \le U_i \le 1.0$), verified via interactive bisection activations and KZG latency.
                    </div>
                    <div>
                        <span class="var-sym">\sum (W_j \cdot U_j)</span> : Aggregate dynamic compute power denominator across all active committee nodes.
                    </div>
                    <div>
                        <span class="var-sym">\mathcal{Y}_{\text{pool}}</span> : Total epoch pool reward: base scheduled emission ($\mathcal{E}_{\text{epoch}}$) plus 75% of network inference fees.
                    </div>
                    <div>
                        <span class="var-sym">N</span> : Active stake-bonded validator count satisfying the canonical 25,000 $33RD bond in the Anchor escrow PDA.
                    </div>
                </div>
            </div>

            <h3 style="font-family:var(--fh); font-size:18px; color:var(--white); text-transform:uppercase; margin:36px 0 16px 0; letter-spacing:0.04em;">
                CANONICAL HARDWARE ARCHITECTURE WEIGHTING MULTIPLIERS (W_i)
            </h3>
            <p style="font-family:var(--fd); font-size:14.5px; line-height:1.65; color:var(--dim); margin-bottom:20px;">
                Unlike legacy Proof-of-Stake protocols that reward idle liquid capital, the 33rd Tree Labs Singularity Protocol ties reward distribution to real physical compute capacity. Hardware tiers are verified on-chain through hardware TEE attestations (NVIDIA NV-CC / AMD SEV-SNP) and deterministic integer reduction trees.
            </p>

            <div class="open-table-container">
                <table class="open-ed-table">
                    <thead>
                        <tr>
                            <th>Hardware Tier</th>
                            <th>Accelerator Specification</th>
                            <th>Memory Architecture</th>
                            <th>Interconnect Bandwidth</th>
                            <th>FP8 Tensor Compute</th>
                            <th>Multiplier ($W_i$)</th>
                            <th>Quorum Specialization</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="highlight">Tier-1 Ultra</td>
                            <td>NVIDIA Blackwell B200</td>
                            <td>192 GB HBM3e (8.0 TB/s)</td>
                            <td>1.8 TB/s NVLink 5.0</td>
                            <td>2,250 TFLOPS</td>
                            <td class="highlight">8.2x</td>
                            <td>Primary Model Sharding &bull; Deep MoE Aggregation</td>
                        </tr>
                        <tr>
                            <td class="highlight">Tier-1 HPC</td>
                            <td>AMD CDNA3 (Instinct MI300X)</td>
                            <td>192 GB HBM3 (5.3 TB/s)</td>
                            <td>896 GB/s Infinity Fabric</td>
                            <td>1,307 TFLOPS</td>
                            <td class="highlight">6.8x</td>
                            <td>Bit-Exact Integer Reduction &bull; Unified Tensor Pods</td>
                        </tr>
                        <tr>
                            <td class="highlight">Tier-1 Enterprise+</td>
                            <td>NVIDIA Hopper H200</td>
                            <td>141 GB HBM3e (4.8 TB/s)</td>
                            <td>900 GB/s NVLink 4.0</td>
                            <td>989 TFLOPS</td>
                            <td class="highlight">6.0x</td>
                            <td>Core Proposal Committee &bull; Large Context Window KV Cache</td>
                        </tr>
                        <tr>
                            <td class="highlight">Tier-1 Enterprise</td>
                            <td>NVIDIA Hopper H100 SXM5</td>
                            <td>80 GB HBM3 (3.35 TB/s)</td>
                            <td>900 GB/s NVLink 4.0</td>
                            <td>989 TFLOPS</td>
                            <td class="highlight">4.8x</td>
                            <td>BFT Consensus Proposals &bull; Halo2-KZG Recursive Proofs</td>
                        </tr>
                        <tr>
                            <td>Tier-2 Edge Quorum</td>
                            <td>NVIDIA GeForce RTX 4090</td>
                            <td>24 GB GDDR6X (1.008 TB/s)</td>
                            <td>64 GB/s PCIe Gen4 x16</td>
                            <td>330 TFLOPS</td>
                            <td>1.0x (Base)</td>
                            <td>Edge Verification &bull; Interactive Bisection Challenger</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </section>

        <!-- ==================================================================== -->
        <!-- SECTION 02: CANONICAL 25,000 $33RD VALIDATOR STAKE BOND             -->
        <!-- ==================================================================== -->
        <section class="ed-section">
            <div class="ed-sec-header">
                <span class="ed-sec-num">[ SECTION 02 // SECURITY &amp; COLLATERAL ]</span>
                <h2 class="ed-sec-title">CANONICAL 25,000 $33RD VALIDATOR STAKE BOND</h2>
                <p class="ed-sec-lede">
                    Node operators must deposit a non-custodial stake bond into the Solana Anchor Staking Program before receiving cryptographic authorization to join the active consensus committee.
                </p>
            </div>

            <div class="open-split-grid">
                <div class="open-split-col">
                    <span class="open-col-kicker">Sybil Barrier &amp; Capital Commitment</span>
                    <h3 class="open-col-title">Byzantine Quorum Resistance</h3>
                    <p class="open-col-text">
                        A malicious adversary attempting to flood the network with virtual identities faces an immutable economic gate of 25,000 $33RD per validator node. In the canonical $K=64$ committee, seizing the Byzantine fault tolerance threshold ($f \ge 22$) requires locking over 550,000 $33RD.
                    </p>
                    <p class="open-col-text">
                        This capital requirement guarantees that the cost of mounting a Byzantine or state withholding attack strictly dwarfs the maximum extractable value of any given inference execution batch.
                    </p>
                </div>
                <div class="open-split-col">
                    <span class="open-col-kicker">Collateral Protection</span>
                    <h3 class="open-col-title">Zero Tolerance for Tensor Corruption</h3>
                    <p class="open-col-text">
                        Distributed neural network inference is susceptible to gradient poisoning and silent bit-flipping attacks. By holding 25,000 $33RD in non-custodial escrow, the protocol maintains a 100% slashable bond against deliberate arithmetic corruption.
                    </p>
                    <p class="open-col-text">
                        If a node injects non-deterministic noise into intermediate activation states, the bond is seized on-chain through automated verification, eliminating the financial incentives for compute fraud.
                    </p>
                </div>
            </div>

            <h3 style="font-family:var(--fh); font-size:18px; color:var(--white); text-transform:uppercase; margin:36px 0 16px 0; letter-spacing:0.04em;">
                7-DAY UNBONDING COOLDOWN PERIOD (50,400 SOLANA SLOTS / 10,080 BLOCKS)
            </h3>
            <p style="font-family:var(--fd); font-size:14.5px; line-height:1.65; color:var(--dim); margin-bottom:20px;">
                Validators initiating capital withdrawal must undergo a mandatory 7-day cooldown window. During this period, collateral remains locked in the Anchor PDA escrow account:
            </p>

            <div class="open-timeline-strip">
                <div class="open-timeline-cell">
                    <span class="timeline-step-tag">PHASE 01 // SLOT 0</span>
                    <span class="timeline-step-title">Unbonding Requested</span>
                    <p class="timeline-step-desc">
                        Node signals unbonding on-chain. Node is removed immediately from the active proposal pool, stopping new reward accruals.
                    </p>
                </div>
                <div class="open-timeline-cell">
                    <span class="timeline-step-tag">PHASE 02 // SLOTS 1&ndash;64</span>
                    <span class="timeline-step-title">Dispute Window</span>
                    <p class="timeline-step-desc">
                        All previous slot proposals committed during the node's active tenure remain subject to recursive verification by edge verifiers.
                    </p>
                </div>
                <div class="open-timeline-cell">
                    <span class="timeline-step-tag">PHASE 03 // HOURS 1&ndash;48</span>
                    <span class="timeline-step-title">Interactive Bisection</span>
                    <p class="timeline-step-desc">
                        If an activation hash is disputed, the protocol executes an interactive binary search across intermediate tensor activations.
                    </p>
                </div>
                <div class="open-timeline-cell">
                    <span class="timeline-step-tag">PHASE 04 // DAY 7</span>
                    <span class="timeline-step-title">Principal Release</span>
                    <p class="timeline-step-desc">
                        If zero cryptographic slashing events are recorded, the complete 25,000 $33RD principal is released to the operator's wallet.
                    </p>
                </div>
            </div>
        </section>

        <!-- ==================================================================== -->
        <!-- SECTION 03: PROTOCOL FEE SPLIT & THE SOLANA INCINERATOR             -->
        <!-- ==================================================================== -->
        <section class="ed-section">
            <div class="ed-sec-header">
                <span class="ed-sec-num">[ SECTION 03 // ATOMIC VALUE ROUTING ]</span>
                <h2 class="ed-sec-title">PROTOCOL FEE ROUTING &amp; SOLANA INCINERATOR</h2>
                <p class="ed-sec-lede">
                    Every inference query, compute reservation, and verification fee paid across the network is split atomically on-chain via the Anchor Settlement Program.
                </p>
            </div>

            <div class="open-ascii-block">
<span class="dim">+-------------------------------------------------------------------------------------------------------------------------+</span>
|                                     <span class="accent">INCOMING INFERENCE FEE TRANSACTION (100.0%)</span>                                         |
<span class="dim">+-------------------------------------------------------------------------------------------------------------------------+</span>
                                                             |
                                  +--------------------------+--------------------------+
                                  |                                                     |
                                  v                                                     v
                    <span class="green">[ 75.0% HARDWARE NODE POOL ]</span>                         <span class="accent">[ 25.0% PROTOCOL RETENTION ]</span>
                    Distributed to active K=64                                          |
                    committee nodes weighted by                                +--------+--------+
                    verified W_i * U_i power share                             |                 |
                                                                               v                 v
                                                                   <span class="accent">[ 15.0% TREASURY ]</span>    <span class="accent">[ 10.0% INCINERATOR ]</span>
                                                                   Squads v4 Multisig    Automated Solana Burn
                                                                   R&D, Audits, Core     1nc1nerator...1111
                                                                   Non-Custodial Escrow  PERMANENT DESTRUCTION
<span class="dim">+-------------------------------------------------------------------------------------------------------------------------+</span>
            </div>

            <div class="open-table-container">
                <table class="open-ed-table">
                    <thead>
                        <tr>
                            <th>Fee Destination</th>
                            <th>Split Share</th>
                            <th>On-Chain Execution</th>
                            <th>Target Recipient / Pubkey</th>
                            <th>Governance Control</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="green">Active Hardware Node Pool</td>
                            <td class="green">75.0%</td>
                            <td>Atomic CPI Transfer per Slot</td>
                            <td class="code-cell">Epoch Vault PDA (Deterministic Settlement)</td>
                            <td>Algorithmic (PoI Consensus)</td>
                        </tr>
                        <tr>
                            <td>Protocol Treasury (R&amp;D)</td>
                            <td>15.0%</td>
                            <td>Direct SPL Token-2022 Transfer</td>
                            <td class="code-cell">Squads v4 Multisig Escrow (3-of-5 Cryptographic Quorum)</td>
                            <td>Multisig Quorum Governance</td>
                        </tr>
                        <tr>
                            <td class="highlight">Permanent Incinerator Burn</td>
                            <td class="highlight">10.0%</td>
                            <td>spl_token_2022::instruction::burn</td>
                            <td class="code-cell highlight">1nc1nerator11111111111111111111111111111111</td>
                            <td>Immutable &bull; Irrevocable Supply Removal</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </section>

        <!-- ==================================================================== -->
        <!-- SECTION 04: DEFLATIONARY BURN FLOOR MECHANICS                       -->
        <!-- ==================================================================== -->
        <section class="ed-section">
            <div class="ed-sec-header">
                <span class="ed-sec-num">[ SECTION 04 // MATHEMATICAL PROOF ]</span>
                <h2 class="ed-sec-title">DEFLATIONARY BURN FLOOR MATHEMATICS</h2>
                <p class="ed-sec-lede">
                    Rigorous mathematical proof that the $33RD token transitions from disinflationary to permanently deflationary when daily inference fee volume exceeds the scheduled emission threshold.
                </p>
            </div>

            <div class="math-open-block">
                <div class="math-formula-lead">THEOREM: PROTOCOL NET MONETARY DEFLATION TIPPING POINT</div>
                <p style="font-family:var(--fd); font-size:14px; line-height:1.65; color:var(--chalk-dim); margin-bottom:12px;">
                    Let circulating token supply at time $t$ be $S(t)$, governed by continuous scheduled emissions $\mathcal{E}(t)$ and fee-driven incinerator burns $\mathcal{B}(t)$:
                </p>
                <div class="math-formula-raw">
                    $$\frac{dS}{dt} = \mathcal{E}_{\text{daily}}(t) - \mathcal{B}_{\text{daily}}(t)$$
                </div>
                <p style="font-family:var(--fd); font-size:14px; line-height:1.65; color:var(--chalk-dim); margin-bottom:12px;">
                    In Emission Era 1 (Years 1&ndash;4), maximum daily compute subsidy emission is fixed at:
                </p>
                <div class="math-formula-raw">
                    $$\mathcal{E}_{\text{daily}}(1) = \frac{7,500,000\text{ }33RD}{4 \times 365\text{ days}} = 5,136.986\text{ }33RD/\text{day}$$
                </div>
                <p style="font-family:var(--fd); font-size:14px; line-height:1.65; color:var(--chalk-dim); margin-bottom:12px;">
                    Daily fee burn $\mathcal{B}_{\text{daily}}$ is defined by the automated 10% routing over total daily invoiced fee volume $\mathcal{V}_{\text{fee}}$ sent to the Solana Incinerator:
                </p>
                <div class="math-formula-raw">
                    $$\mathcal{B}_{\text{daily}} = 0.10 \times \mathcal{V}_{\text{fee}}$$
                </div>
                <p style="font-family:var(--fd); font-size:14px; line-height:1.65; color:var(--chalk-dim); margin-bottom:12px;">
                    Net monetary deflation strictly occurs when $\frac{dS}{dt} < 0$, which requires:
                </p>
                <div class="math-formula-raw">
                    $$\mathcal{B}_{\text{daily}} > \mathcal{E}_{\text{daily}}(1) \iff 0.10 \times \mathcal{V}_{\text{fee}} > 5,136.986 \iff \mathcal{V}_{\text{fee}} > 51,369.86\text{ }33RD/\text{day}$$
                </div>
                <p style="font-family:var(--fd); font-size:14.5px; line-height:1.65; color:var(--chalk);">
                    <strong style="color:var(--white);">Q.E.D.</strong> When daily inference volume exceeds <strong style="color:var(--t);">51,370 $33RD</strong>, the daily burn rate exceeds maximum protocol emission. Circulating supply permanently contracts with every subsequent tensor execution.
                </p>
            </div>

            <h3 style="font-family:var(--fh); font-size:18px; color:var(--white); text-transform:uppercase; margin:36px 0 16px 0; letter-spacing:0.04em;">
                DEFLATIONARY TIPPING POINTS ACROSS HALVING ERAS
            </h3>
            <p style="font-family:var(--fd); font-size:14.5px; line-height:1.65; color:var(--dim); margin-bottom:20px;">
                Because compute emission subsidies halve every 4 years, the required fee volume to maintain absolute net supply contraction drops by 50% with each era:
            </p>

            <div class="open-table-container">
                <table class="open-ed-table">
                    <thead>
                        <tr>
                            <th>Halving Era</th>
                            <th>Calendar Window</th>
                            <th>Daily Scheduled Emission</th>
                            <th>Deflationary Fee Threshold</th>
                            <th>Burn Acceleration Factor</th>
                            <th>Monetary Policy Phase</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="highlight">Era 1</td>
                            <td>Years 1&ndash;4</td>
                            <td>5,136.986 $33RD / day</td>
                            <td class="highlight">51,370 $33RD / day</td>
                            <td>1.0x (Baseline)</td>
                            <td>Bootstrapping &bull; Disinflationary Transition</td>
                        </tr>
                        <tr>
                            <td>Era 2</td>
                            <td>Years 5&ndash;8</td>
                            <td>2,568.493 $33RD / day</td>
                            <td class="highlight">25,685 $33RD / day</td>
                            <td>2.0x Acceleration</td>
                            <td>Structural Scarcity &bull; Supply Contraction</td>
                        </tr>
                        <tr>
                            <td>Era 3</td>
                            <td>Years 9&ndash;12</td>
                            <td>1,284.246 $33RD / day</td>
                            <td class="highlight">12,842 $33RD / day</td>
                            <td>4.0x Acceleration</td>
                            <td>Deep Deflationary Convergence</td>
                        </tr>
                        <tr>
                            <td>Era 4</td>
                            <td>Years 13&ndash;16</td>
                            <td>642.123 $33RD / day</td>
                            <td class="highlight">6,421 $33RD / day</td>
                            <td>8.0x Acceleration</td>
                            <td>Asymptotic Supply Floor</td>
                        </tr>
                        <tr>
                            <td class="green">Tail Era</td>
                            <td>Year 17+</td>
                            <td>0.000 $33RD / day</td>
                            <td class="green">&gt; 0 $33RD / day</td>
                            <td>Pure Deflation</td>
                            <td>100% Fee-Driven Ultra-Sound Supply</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </section>

        <!-- ==================================================================== -->
        <!-- SECTION 05: SLASHING PENALTY REDISTRIBUTION & CHALLENGER GAME       -->
        <!-- ==================================================================== -->
        <section class="ed-section">
            <div class="ed-sec-header">
                <span class="ed-sec-num">[ SECTION 05 // BYZANTINE FAULT TOLERANCE ]</span>
                <h2 class="ed-sec-title">SLASHING PENALTY REDISTRIBUTION</h2>
                <p class="ed-sec-lede">
                    Cryptographic fraud and liveness violations are penalized through automated on-chain slashing. Slashed funds are split between permanent destruction via the Solana Incinerator and whistleblower challenger bounties.
                </p>
            </div>

            <div class="open-table-container">
                <table class="open-ed-table">
                    <thead>
                        <tr>
                            <th>Infraction Type</th>
                            <th>Cryptographic Proof</th>
                            <th>Slashed Stake</th>
                            <th>Challenger Bounty</th>
                            <th>Incinerator Destruction</th>
                            <th>Validator Penalty</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="highlight">Equivocation / Double Signing</td>
                            <td>Dual-Signed Slot Headers / Divergent State</td>
                            <td class="highlight">100% (25,000+ $33RD)</td>
                            <td class="highlight">50% Bounty to Challenger</td>
                            <td>50% Burned to Incinerator</td>
                            <td>Permanent Hardware Pubkey Revocation</td>
                        </tr>
                        <tr>
                            <td class="highlight">Failed Halo2-KZG Proof</td>
                            <td>Invalid Polynomial Evaluation Point</td>
                            <td class="highlight">25% (6,250 $33RD)</td>
                            <td class="highlight">5,000 $33RD Flat Bounty</td>
                            <td>1,250 $33RD Burned</td>
                            <td>Epoch Disqualification &bull; Standby Queue</td>
                        </tr>
                        <tr>
                            <td>Invalid INT8 Tensor Output</td>
                            <td>CAP-FFN Arithmetic Mismatch Verification</td>
                            <td>50% (12,500 $33RD)</td>
                            <td>20% Bounty (2,500 $33RD)</td>
                            <td>80% Burned (10,000 $33RD)</td>
                            <td>Slot Rollback &bull; Score Reset</td>
                        </tr>
                        <tr>
                            <td>TEE Attestation Mismatch</td>
                            <td>Quote Signature Failure (SEV / CC)</td>
                            <td>30% (7,500 $33RD)</td>
                            <td>0% (Automated Anchor Check)</td>
                            <td>100% Burned (7,500 $33RD)</td>
                            <td>Silicon Certificate Blacklisted</td>
                        </tr>
                        <tr>
                            <td>Liveness Failure (&gt;10 Slots)</td>
                            <td>Anchor Slot Proposal Timeout</td>
                            <td>5% (1,250 $33RD)</td>
                            <td>0%</td>
                            <td>0% (Sent to Treasury)</td>
                            <td>Standby Demotion for 24 Hours</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h3 style="font-family:var(--fh); font-size:18px; color:var(--white); text-transform:uppercase; margin:36px 0 16px 0; letter-spacing:0.04em;">
                THE CRYPTOGRAPHIC CHALLENGER GAME &bull; 5,000 $33RD FLAT REWARD
            </h3>
            <p style="font-family:var(--fd); font-size:14.5px; line-height:1.65; color:var(--dim); margin-bottom:20px;">
                The protocol incentivizes third-party verifiers (including consumer RTX 4090 operators) to challenge invalid slot commitments. When a challenger identifies an arithmetic discrepancy, the dispute pipeline executes:
            </p>

            <div class="open-timeline-strip">
                <div class="open-timeline-cell">
                    <span class="timeline-step-tag">STEP 01 // DETECTION</span>
                    <span class="timeline-step-title">Discrepancy Isolated</span>
                    <p class="timeline-step-desc">
                        Challenger recomputes tensor layer activations and isolates divergent commitment hash $\mathcal{H}(A) \ne \mathcal{H}(B)$.
                    </p>
                </div>
                <div class="open-timeline-cell">
                    <span class="timeline-step-tag">STEP 02 // BISECTION</span>
                    <span class="timeline-step-title">Interactive Bisection</span>
                    <p class="timeline-step-desc">
                        Anchor coordinates a binary search over the computation tree, narrowing the dispute down to a single instruction.
                    </p>
                </div>
                <div class="open-timeline-cell">
                    <span class="timeline-step-tag">STEP 03 // KZG PROOF</span>
                    <span class="timeline-step-title">On-Chain Pairing Check</span>
                    <p class="timeline-step-desc">
                        The Solana Anchor program executes pairing checks over BN254/BLS12-381 curves to mathematically confirm fraud.
                    </p>
                </div>
                <div class="open-timeline-cell">
                    <span class="timeline-step-tag">STEP 04 // BOUNTY</span>
                    <span class="timeline-step-title">Instant Settlement</span>
                    <p class="timeline-step-desc">
                        The dishonest node is slashed. The challenger automatically receives the 5,000 $33RD flat bounty in the same slot.
                    </p>
                </div>
            </div>
        </section>

        <!-- ==================================================================== -->
        <!-- SECTION 06: ON-CHAIN SOLANA ANCHOR CODE ARCHITECTURE                -->
        <!-- ==================================================================== -->
        <section class="ed-section">
            <div class="ed-sec-header">
                <span class="ed-sec-num">[ SECTION 06 // CODE SPECIFICATION ]</span>
                <h2 class="ed-sec-title">SOLANA ANCHOR SMART CONTRACT INTERFACES</h2>
                <p class="ed-sec-lede">
                    On-chain implementation of the 25,000 $33RD validator staking bond, epoch yield calculation, and atomic Solana Incinerator fee burning.
                </p>
            </div>

            <div class="open-code-exhibit">
                <div class="open-code-header">
                    <span class="file-path">programs/singularity_consensus/src/yield_engine.rs</span>
                    <span>ANCHOR v0.30 &bull; SOLANA MAINNET-BETA</span>
                </div>
                <pre class="open-code-content"><code><span class="kw">use</span> anchor_lang::prelude::*;
<span class="kw">use</span> anchor_spl::token_interface::{<span class="kw">self</span>, Mint, TokenAccount, TokenInterface, Burn};

<span class="cm">/// Canonical Solana Incinerator address for permanent token destruction</span>
<span class="kw">pub const</span> <span class="ty">SOLANA_INCINERATOR</span>: Pubkey = pubkey!(<span class="str">"1nc1nerator11111111111111111111111111111111"</span>);
<span class="kw">pub const</span> <span class="ty">MINIMUM_VALIDATOR_STAKE</span>: u64 = 25_000_000_000_000; <span class="cm">// 25,000 $33RD (9 decimals)</span>
<span class="kw">pub const</span> <span class="ty">UNBONDING_COOLDOWN_SLOTS</span>: u64 = 50_400; <span class="cm">// 7 Days @ 12.0s block sync</span>

<span class="cm">/// Evaluates and credits validator node rewards for committed consensus epoch</span>
<span class="kw">pub fn</span> <span class="fn">claim_epoch_yield</span>(ctx: Context&lt;ClaimEpochYield&gt;, epoch_index: u64) -&gt; Result&lt;()&gt; {
    <span class="kw">let</span> validator = &amp;<span class="kw">mut</span> ctx.accounts.validator_record;
    <span class="kw">let</span> epoch_pool = &amp;ctx.accounts.epoch_yield_pool;

    <span class="cm">// Verify canonical 25,000 $33RD minimum stake bond remains active</span>
    require!(validator.bonded_stake &gt;= MINIMUM_VALIDATOR_STAKE, YieldError::InsufficientBond);
    require!(!validator.is_slashed, YieldError::ValidatorSlashed);

    <span class="cm">// Compute node weighted contribution: W_i * U_i</span>
    <span class="kw">let</span> node_power = (validator.hardware_weight <span class="kw">as</span> u128)
        .checked_mul(validator.validated_uptime_bps <span class="kw">as</span> u128)
        .ok_or(YieldError::MathOverflow)?;

    <span class="cm">// Calculate proportional reward: R_epoch = (W_i * U_i / sum(W_j * U_j)) * Y_pool</span>
    <span class="kw">let</span> reward_amount = node_power
        .checked_mul(epoch_pool.total_pool_reward <span class="kw">as</span> u128)
        .ok_or(YieldError::MathOverflow)?
        .checked_div(epoch_pool.aggregate_network_power)
        .ok_or(YieldError::ZeroNetworkPower)? <span class="kw">as</span> u64;

    <span class="cm">// Transfer reward from Epoch Vault to Validator Token Account</span>
    token_interface::transfer_checked(
        ctx.accounts.into_reward_transfer_context(),
        reward_amount,
        9, <span class="cm">// Decimals</span>
    )?;

    emit!(EpochRewardClaimed {
        validator: validator.key(),
        epoch: epoch_index,
        payout_amount: reward_amount,
        hardware_multiplier: validator.hardware_weight,
    });

    Ok(())
}

<span class="cm">/// Atomically routes inference fee: 75% Nodes, 15% Treasury, 10% Solana Incinerator</span>
<span class="kw">pub fn</span> <span class="fn">settle_protocol_fee</span>(ctx: Context&lt;SettleFee&gt;, total_fee: u64) -&gt; Result&lt;()&gt; {
    <span class="kw">let</span> node_share = total_fee.checked_mul(75).unwrap().checked_div(100).unwrap();
    <span class="kw">let</span> treasury_share = total_fee.checked_mul(15).unwrap().checked_div(100).unwrap();
    <span class="kw">let</span> incinerator_burn = total_fee.checked_sub(node_share).unwrap().checked_sub(treasury_share).unwrap();

    <span class="cm">// 1. Credit 75% to Active Epoch Reward Pool</span>
    token_interface::transfer_checked(ctx.accounts.into_node_pool_context(), node_share, 9)?;

    <span class="cm">// 2. Route 15% to Protocol R&amp;D Multisig Treasury</span>
    token_interface::transfer_checked(ctx.accounts.into_treasury_context(), treasury_share, 9)?;

    <span class="cm">// 3. Permanently incinerate 10% via SPL Token-2022 burn</span>
    token_interface::burn(
        CpiContext::new(
            ctx.accounts.token_program.to_account_info(),
            Burn {
                mint: ctx.accounts.token_mint.to_account_info(),
                from: ctx.accounts.fee_escrow.to_account_info(),
                authority: ctx.accounts.authority.to_account_info(),
            },
        ),
        incinerator_burn,
    )?;

    Ok(())
}</code></pre>
            </div>
        </section>

        <!-- ==================================================================== -->
        <!-- SECTION 07: VALIDATOR ONBOARDING & RUNBOOK                          -->
        <!-- ==================================================================== -->
        <section class="ed-section">
            <div class="ed-sec-header">
                <span class="ed-sec-num">[ SECTION 07 // OPERATOR RUNBOOK ]</span>
                <h2 class="ed-sec-title">VALIDATOR ONBOARDING &amp; CLI PROCEDURES</h2>
                <p class="ed-sec-lede">
                    Deploy the official 33rd Tree Labs validator daemon on verified bare-metal hardware. Complete hardware attestation, deposit the 25,000 $33RD bond, and participate in consensus.
                </p>
            </div>

            <div class="open-code-exhibit">
                <div class="open-code-header">
                    <span class="file-path">terminal // bash</span>
                    <span>33RD-CLI v4.1.2 &bull; LINUX x86_64</span>
                </div>
                <pre class="open-code-content"><code><span class="cm"># 1. Install official 33rd Tree Labs validator daemon</span>
curl -sSf https://33rdtreelabs.tech/install.sh | bash
export PATH="$HOME/.33rd/bin:$PATH"

<span class="cm"># 2. Benchmark GPU accelerator and generate confidential compute attestation</span>
33rd-node benchmark --gpu auto --enable-confidential-compute
<span class="cm"># Output: [SUCCESS] Verified NVIDIA Hopper H100 SXM5 (80GB). Multiplier: 4.8x.</span>

<span class="cm"># 3. Deposit the canonical 25,000 $33RD validator stake bond</span>
33rd-cli validator deposit-stake \
  --amount 25000 \
  --node-keypair ~/.config/33rd/validator-key.json \
  --network mainnet-beta \
  --rpc-url https://api.mainnet-beta.solana.com

<span class="cm"># 4. Start the continuous PoI consensus worker daemon</span>
33rd-daemon \
  --committee-size 64 \
  --slot-cadence 12.0s \
  --proof-engine kzg-hypernova \
  --tee-attestation enabled \
  --metrics-port 9100

<span class="cm"># 5. Monitor real-time epoch reward accrual and incinerator burn velocity</span>
33rd-cli validator status --live-telemetry</code></pre>
            </div>
        </section>

    </main>

    <!-- GLOBAL FOOTER -->
    <footer class="global-footer">
        <div class="footer-inner">
            <div class="footer-brand">
                <strong>33RD TREE LABS</strong> &bull; THE SINGULARITY PROTOCOL &bull; <code>33rdtreelabs.tech</code>
            </div>
            <div class="footer-links">
                <a href="index.html" class="footer-link">[ OVERVIEW ]</a>
                <a href="protocol.html" class="footer-link">[ PROTOCOL ]</a>
                <a href="simulator.html" class="footer-link">[ SIMULATOR ]</a>
                <a href="yield.html" class="footer-link active">[ YIELD ]</a>
                <a href="nodes.html" class="footer-link">[ NODES ]</a>
                <a href="tokenomics.html" class="footer-link">[ TOKENOMICS ]</a>
                <a href="research.html" class="footer-link">[ RESEARCH ]</a>
                <a href="33rd_Tree_Labs_Whitepaper.pdf" target="_blank" class="footer-link">[ WHITEPAPER PDF ]</a>
            </div>
        </div>
    </footer>

    <!-- INTERACTIVE JAVASCRIPT & QUANTITATIVE ENGINE -->
    <script>
        // Lenis Smooth Scroll Configuration strictly adhering to design-tokens.json motion contract
        const lenis = new Lenis({
            lerp: 0.14,
            wheelMultiplier: 1.15,
            touchMultiplier: 1.5,
            smoothWheel: true
        });

        if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
            gsap.registerPlugin(ScrollTrigger);
            lenis.on('scroll', ScrollTrigger.update);
            gsap.ticker.add((time) => lenis.raf(time * 1000));
            gsap.ticker.lagSmoothing(0);
        } else {
            function raf(time) {
                lenis.raf(time);
                requestAnimationFrame(raf);
            }
            requestAnimationFrame(raf);
        }

        // Custom Retro-Tech Cursor
        const cursorDot = document.getElementById('cursor-dot');
        const cursorRing = document.getElementById('cursor-ring');
        if (cursorDot && cursorRing) {
            window.addEventListener('mousemove', (e) => {
                cursorDot.style.left = e.clientX + 'px';
                cursorDot.style.top = e.clientY + 'px';
                cursorRing.style.left = e.clientX + 'px';
                cursorRing.style.top = e.clientY + 'px';
            });
            document.querySelectorAll('a, button, input, select, [data-glitch]').forEach(el => {
                el.addEventListener('mouseenter', () => document.body.classList.add('cursor-hover'));
                el.addEventListener('mouseleave', () => document.body.classList.remove('cursor-hover'));
            });
        }

        // Top-Edge Scroll Telemetry Progress Line & Right Rail
        const progressBar = document.getElementById('scroll-progress-line');
        const sbarThumb = document.getElementById('sbarThumb');
        const railYCoord = document.getElementById('railYCoord');
        const sbarTicks = document.querySelectorAll('.sbar__ticks span');

        function onScrollTelemetry() {
            const doc = document.documentElement;
            const sy = window.scrollY || doc.scrollTop;
            const max = doc.scrollHeight - window.innerHeight;
            const progress = max > 0 ? Math.min(1, Math.max(0, sy / max)) : 0;

            if (progressBar) {
                progressBar.style.width = (progress * 100).toFixed(2) + '%';
            }

            if (sbarThumb && railYCoord) {
                const sbarHeight = window.innerHeight - 80;
                const thumbHeight = 35;
                const travel = sbarHeight - thumbHeight;
                sbarThumb.style.transform = 'translateY(' + (progress * travel) + 'px)';
                sbarThumb.style.height = thumbHeight + 'px';

                railYCoord.textContent = 'Y: +' + Math.round(sy).toString().padStart(4, '0') + 'PX';

                const tickIdx = Math.min(sbarTicks.length - 1, Math.floor(progress * sbarTicks.length));
                sbarTicks.forEach((t, i) => {
                    if (i === tickIdx) {
                        t.classList.add('active');
                    } else {
                        t.classList.remove('active');
                    }
                });
            }
        }
        window.addEventListener('scroll', onScrollTelemetry, { passive: true });
        lenis.on('scroll', onScrollTelemetry);
        onScrollTelemetry();

        // Mechanical Glitch Decoder
        class MechanicalGlitch {
            constructor(el) {
                this.el = el;
                this.chars = '01X_/*+-[]#';
                this.originalText = el.getAttribute('data-glitch-text') || el.textContent.trim();
                el.setAttribute('data-glitch-text', this.originalText);
                this.tickInterval = 250;
                this.totalDuration = 3500;
                this.totalTicks = Math.round(this.totalDuration / this.tickInterval);
                this.currentTick = 0;
                this.timer = null;
                this.isRunning = false;
            }
            start() {
                if (this.isRunning) return;
                this.isRunning = true;
                this.currentTick = 0;
                clearInterval(this.timer);
                this.timer = setInterval(() => {
                    this.currentTick++;
                    const progress = this.currentTick / this.totalTicks;
                    const resolvedChars = Math.floor(progress * this.originalText.length);
                    let out = '';
                    for (let i = 0; i < this.originalText.length; i++) {
                        const ch = this.originalText[i];
                        if (ch === ' ' || ch === String.fromCharCode(10) || ch === String.fromCharCode(9)) {
                            out += ch;
                        } else if (i < resolvedChars) {
                            out += ch;
                        } else {
                            out += this.chars[Math.floor(Math.random() * this.chars.length)];
                        }
                    }
                    this.el.textContent = out;
                    if (this.currentTick >= this.totalTicks) {
                        clearInterval(this.timer);
                        this.el.textContent = this.originalText;
                        this.isRunning = false;
                    }
                }, this.tickInterval);
            }
        }

        document.querySelectorAll('[data-glitch]').forEach(el => {
            const mg = new MechanicalGlitch(el);
            el.addEventListener('mouseenter', () => mg.start());
        });

        // KaTeX Auto-Render Initializer
        window.addEventListener('DOMContentLoaded', () => {
            if (typeof renderMathInElement === 'function') {
                renderMathInElement(document.body, {
                    delimiters: [
                        { left: '$$', right: '$$', display: true },
                        { left: '$', right: '$', display: false }
                    ],
                    throwOnError: false
                });
            }
        });

        // ====================================================================
        // QUANTITATIVE YIELD & DEFLATION ENGINE (BIT-EXACT MATHEMATICS)
        // ====================================================================
        function calculateValidatorYield() {
            const hwSelect = document.getElementById('sim-hw');
            const nodesSlider = document.getElementById('sim-nodes');
            const stakeSlider = document.getElementById('sim-stake');
            const utilSlider = document.getElementById('sim-util');
            const eraSelect = document.getElementById('sim-era');
            const feesSlider = document.getElementById('sim-fees');

            if (!hwSelect || !nodesSlider || !stakeSlider || !utilSlider || !eraSelect || !feesSlider) return;

            const hwTier = hwSelect.value;
            const nodeCount = parseInt(nodesSlider.value, 10);
            let rawStake = parseInt(stakeSlider.value, 10);
            const utilizationPct = parseInt(utilSlider.value, 10);
            const era = parseInt(eraSelect.value, 10);
            const dailyFeeVolume = parseInt(feesSlider.value, 10);

            // Canonical 25,000 $33RD validator stake bond requirement
            const minRequiredStake = nodeCount * 25000;
            const stakeMinLabel = document.getElementById('sim-stake-min-label');
            if (stakeMinLabel) {
                stakeMinLabel.textContent = 'Min: ' + minRequiredStake.toLocaleString() + ' $33RD (25k / node)';
            }
            stakeSlider.min = minRequiredStake;

            if (rawStake < minRequiredStake) {
                rawStake = minRequiredStake;
                stakeSlider.value = rawStake;
            }

            // Stake compliance status
            const stakeValEl = document.getElementById('sim-stake-val');
            if (stakeValEl) {
                if (rawStake >= minRequiredStake) {
                    stakeValEl.className = 'val-tag bond-secure';
                    stakeValEl.textContent = rawStake.toLocaleString() + ' $33RD (' + (rawStake / nodeCount).toLocaleString() + ' / node &bull; SECURED)';
                } else {
                    stakeValEl.className = 'val-tag bond-alert';
                    stakeValEl.textContent = rawStake.toLocaleString() + ' $33RD (BELOW 25,000 MINIMUM)';
                }
            }

            document.getElementById('sim-nodes-val').textContent = nodeCount + (nodeCount === 1 ? ' NODE' : ' NODES');
            document.getElementById('sim-util-val').textContent = utilizationPct + '%';
            document.getElementById('sim-fees-val').textContent = dailyFeeVolume.toLocaleString() + ' $33RD / DAY';

            // Hardware Weight Multipliers (W_i)
            // H100 SXM5: 4.8x, H200: 6.0x, B200: 8.2x, RTX 4090: 1.0x, CDNA3: 6.8x
            const hwDatabase = {
                'b200': { weight: 8.2, name: 'NVIDIA Blackwell B200 (192GB HBM3e)', tierTag: '8.2x WEIGHT' },
                'cdna3': { weight: 6.8, name: 'AMD CDNA3 MI300X (192GB HBM3)', tierTag: '6.8x WEIGHT' },
                'h200': { weight: 6.0, name: 'NVIDIA Hopper H200 (141GB HBM3e)', tierTag: '6.0x WEIGHT' },
                'h100': { weight: 4.8, name: 'NVIDIA Hopper H100 SXM5 (80GB HBM3)', tierTag: '4.8x WEIGHT' },
                'rtx4090': { weight: 1.0, name: 'NVIDIA GeForce RTX 4090 (24GB GDDR6X)', tierTag: '1.0x WEIGHT' }
            };

            const hwData = hwDatabase[hwTier] || hwDatabase['h100'];
            const hwWeight = hwData.weight;
            const hwSpecName = hwData.name;

            const hwMultiplierTag = document.getElementById('sim-hw-multiplier-tag');
            if (hwMultiplierTag) {
                hwMultiplierTag.textContent = hwData.tierTag;
            }

            const clusterWeight = nodeCount * hwWeight;
            const effectiveUptime = utilizationPct / 100.0;
            const operatorPower = clusterWeight * effectiveUptime;

            // Network power baseline denominator (128 nodes @ average 3.8x weight, 80% uptime)
            const baselineNetworkPower = 128 * 3.8 * 0.80;
            const totalNetworkPower = baselineNetworkPower + operatorPower;
            const operatorShare = operatorPower / totalNetworkPower;

            // Daily Base Emission by Halving Era
            // Era 1 (Y1-4): 5,136.986 $33RD/day (7,500,000 / 1460 days)
            // Era 2 (Y5-8): 2,568.493 $33RD/day
            // Era 3 (Y9-12): 1,284.246 $33RD/day
            // Era 4 (Y13-16): 642.123 $33RD/day
            const eraEmissions = {
                1: 5136.986,
                2: 2568.493,
                3: 1284.246,
                4: 642.123
            };
            const dailyBaseEmission = eraEmissions[era] || eraEmissions[1];

            const eraValEl = document.getElementById('sim-era-val');
            if (eraValEl) {
                eraValEl.textContent = dailyBaseEmission.toFixed(2) + ' $33RD / DAY';
            }

            // Atomic Protocol Fee Routing: 75% Nodes, 15% Treasury, 10% Solana Incinerator
            const dailyFeeNodePool = dailyFeeVolume * 0.75;
            const dailyTreasury = dailyFeeVolume * 0.15;
            const dailyIncineratorBurn = dailyFeeVolume * 0.10;

            // Total Node Reward Pool per day
            const totalDailyRewardPool = dailyBaseEmission + dailyFeeNodePool;

            // Operator Projected Payouts
            const operatorDailyReward = operatorShare * totalDailyRewardPool;
            const operatorEpochReward = operatorDailyReward / 7200.0; // 7,200 12.0s slots per day
            const operatorMonthlyReward = operatorDailyReward * 30.0;
            const operatorAnnualReward = operatorDailyReward * 365.0;

            const apy = (operatorAnnualReward / rawStake) * 100.0;

            // Net Monetary Supply Trajectory: Emission - Incinerator Burn
            const netSupplyDelta = dailyBaseEmission - dailyIncineratorBurn;

            // Render Results to UI
            document.getElementById('res-apy').textContent = apy.toFixed(1) + '%';
            document.getElementById('res-epoch').textContent = operatorEpochReward.toFixed(4) + ' $33RD';
            document.getElementById('res-daily').textContent = operatorDailyReward.toFixed(2) + ' $33RD';
            document.getElementById('res-monthly').textContent = operatorMonthlyReward.toFixed(1) + ' $33RD';
            document.getElementById('res-annual').textContent = Math.round(operatorAnnualReward).toLocaleString() + ' $33RD';
            document.getElementById('res-cluster-weight').textContent = clusterWeight.toFixed(1) + 'x (' + hwWeight.toFixed(1) + 'x * ' + nodeCount + ')';
            document.getElementById('res-network-share').textContent = (operatorShare * 100).toFixed(3) + '%';
            document.getElementById('res-burn-daily').textContent = dailyIncineratorBurn.toFixed(1) + ' $33RD / DAY';
            document.getElementById('res-treasury-daily').textContent = dailyTreasury.toFixed(1) + ' $33RD / DAY';

            const statusEl = document.getElementById('res-deflation-status');
            if (statusEl) {
                if (netSupplyDelta < 0) {
                    statusEl.className = 'calc-row-val green';
                    statusEl.textContent = 'NET DEFLATIONARY (-' + Math.abs(netSupplyDelta).toFixed(1) + ' $33RD / DAY CONTRACTION)';
                } else {
                    statusEl.className = 'calc-row-val accent';
                    statusEl.textContent = 'DISINFLATIONARY (+' + netSupplyDelta.toFixed(1) + ' $33RD / DAY NET INFLOW)';
                }
            }

            // Real-time Diagnostic Telemetry Log
            const logEl = document.getElementById('res-diagnostic-log');
            if (logEl) {
                logEl.textContent =
                    "[QUANTITATIVE TELEMETRY LOG]\\n" +
                    ">> Target Cluster: " + nodeCount + "x " + hwSpecName + "\\n" +
                    ">> PoI Power Quotient: (W_i=" + hwWeight.toFixed(1) + " * N=" + nodeCount + " * U=" + utilizationPct + "%) = " + operatorPower.toFixed(2) + " / Total=" + totalNetworkPower.toFixed(2) + "\\n" +
                    ">> Validator Bond: " + rawStake.toLocaleString() + " $33RD [Mandatory Canonical Gate: " + minRequiredStake.toLocaleString() + " $33RD]\\n" +
                    ">> Pool Formula: Base(" + dailyBaseEmission.toFixed(1) + ") + 75% Fees(" + dailyFeeNodePool.toFixed(1) + ") = " + totalDailyRewardPool.toFixed(1) + " $33RD / day\\n" +
                    ">> Solana Incinerator (10%): " + dailyIncineratorBurn.toFixed(1) + " $33RD burned to 1nc1nerator...1111 (Floor: 51,370 $33RD fee vol)";
            }
        }

        // Initialize on load
        window.addEventListener('DOMContentLoaded', () => {
            calculateValidatorYield();
        });
    </script>
</body>
</html>
"""

# Write out yield.html
output_path = os.path.join(SITE_DIR, "yield.html")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(yield_html)

print(f"yield.html written successfully ({len(yield_html)} bytes, {len(yield_html.splitlines())} lines).")
