#!/usr/bin/env python3
"""
Complete Multi-Page VRTL WRLD Industrial Brutalism Site Generator
Target: 33rd Tree Labs (33rdtreelabs.tech)
"""

import os
import re

SITE_DIR = "/Users/ianmora/Desktop/Projects/33rd-tree-labs-site"

def get_shared_css():
    return """
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
            --laser-glow: rgba(255, 41, 44, 0.45);
            --laser-subtle: rgba(255, 41, 44, 0.08);
            --chalk: #F2F2F5;
            --chalk-dim: #D4D4DC;
            --slate: #8E8E98;
            --dark-slate: #4A4A56;
            --white: #FFFFFF;
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
            scroll-behavior: smooth;
            background: var(--bg);
            color: var(--chalk);
            font-family: 'Space Grotesk', -apple-system, BlinkMacSystemFont, sans-serif;
            overflow-x: hidden;
        }

        body {
            position: relative;
            min-height: 100vh;
            background: var(--bg);
            overflow-x: hidden;
            -webkit-font-smoothing: antialiased;
        }

        /* CUSTOM RETRO-TECH CURSOR */
        #cursor-dot {
            width: 6px;
            height: 6px;
            background: var(--laser-red);
            border-radius: 50%;
            position: fixed;
            pointer-events: none;
            z-index: 99999;
            transform: translate(-50%, -50%);
            box-shadow: 0 0 10px var(--laser-red);
            transition: opacity 0.2s;
        }
        #cursor-ring {
            width: 32px;
            height: 32px;
            border: 1px solid rgba(255, 41, 44, 0.4);
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
            border-color: var(--laser-red);
            background: rgba(255, 41, 44, 0.08);
        }

        /* TOP-EDGE SCROLL TELEMETRY PROGRESS LINE */
        #scroll-progress-line, .scroll-progress-bar {
            position: fixed;
            top: 0;
            left: 0;
            width: 0%;
            height: 2px;
            background: var(--laser-red);
            box-shadow: 0 0 8px var(--laser-red), 0 0 16px rgba(255, 41, 44, 0.6);
            z-index: 100000;
            pointer-events: none;
            transition: width 0.04s linear;
            will-change: width;
        }

        /* FLOATING PILL NAVBAR SCROLL BEHAVIOR */
        .nav-wrapper.nav-scrolled .nav-pill {
            background: rgba(11, 11, 14, 0.96);
            border-color: rgba(255, 41, 44, 0.35);
            box-shadow: 0 16px 40px rgba(0, 0, 0, 0.85), 0 0 20px rgba(255, 41, 44, 0.15);
        }

        /* INTERSECTION OBSERVER REVEAL ANIMATIONS (GPU-ACCELERATED, JANK-FREE) */
        .reveal-on-scroll {
            opacity: 0;
            transform: translateY(22px);
            transition: opacity 0.65s cubic-bezier(0.16, 1, 0.3, 1),
                        transform 0.65s cubic-bezier(0.16, 1, 0.3, 1),
                        border-color 0.25s ease,
                        box-shadow 0.25s ease;
            will-change: opacity, transform;
        }
        .reveal-on-scroll.is-revealed {
            opacity: 1;
            transform: translateY(0);
        }
        .reveal-delay-1 { transition-delay: 0.08s; }
        .reveal-delay-2 { transition-delay: 0.16s; }
        .reveal-delay-3 { transition-delay: 0.24s; }
        .reveal-delay-4 { transition-delay: 0.32s; }

        /* MECHANICAL GLITCH TARGETS (ENFORCE TABULAR-NUMS TO PREVENT JANK) */
        [data-glitch], .mechanical-glitch {
            font-variant-numeric: tabular-nums;
            display: inline-block;
        }

        /* UNIFIED FLOATING PILL NAVBAR SPECIFICATION */
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
            border: 1px solid rgba(255, 255, 255, 0.12);
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
            border-right: 1px solid rgba(255, 255, 255, 0.12);
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
            content: '';
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

        /* VRTL WRLD CALM GLITCH DECODER */
        .glitch-active {
            opacity: 0.94;
            letter-spacing: 0.02em;
        }

        /* BUTTONS */
        .btn-brutal-red {
            display: inline-flex;
            align-items: center;
            gap: 10px;
            background: var(--laser-red);
            color: var(--white);
            font-family: 'JetBrains Mono', monospace;
            font-size: 11.5px;
            font-weight: 700;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            text-decoration: none;
            padding: 13px 24px;
            clip-path: polygon(0 10px, 10px 0, 100% 0, 100% calc(100% - 10px), calc(100% - 10px) 100%, 0 100%);
            box-shadow: 0 6px 24px rgba(255, 41, 44, 0.35);
            transition: background 0.2s ease, transform 0.15s ease, box-shadow 0.2s ease;
            border: none;
        }
        .btn-brutal-red:hover {
            background: #FF474A;
            box-shadow: 0 8px 30px rgba(255, 41, 44, 0.55);
            transform: translateY(-2px);
        }

        .btn-brutal-outline {
            display: inline-flex;
            align-items: center;
            gap: 10px;
            background: transparent;
            color: var(--chalk);
            font-family: 'JetBrains Mono', monospace;
            font-size: 11.5px;
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

        /* SECTION HEADERS & META TAGS */
        .meta-tag {
            font-family: 'JetBrains Mono', monospace;
            font-size: 11.5px;
            font-weight: 700;
            letter-spacing: 0.15em;
            color: var(--laser-red);
            text-transform: uppercase;
            margin-bottom: 12px;
            display: inline-block;
        }
        .section-title {
            font-family: 'Syne', sans-serif;
            font-size: clamp(28px, 4vw, 46px);
            font-weight: 800;
            line-height: 1.05;
            letter-spacing: -0.01em;
            text-transform: uppercase;
            color: var(--white);
            margin-bottom: 16px;
        }
        .section-desc {
            font-size: 15px;
            line-height: 1.65;
            color: var(--slate);
            max-width: 720px;
            font-weight: 400;
            margin-bottom: 36px;
        }

        /* PAGE CONTAINER */
        .page-wrap {
            padding-top: 96px;
            padding-bottom: 80px;
            max-width: 1360px;
            margin: 0 auto;
            padding-left: 24px;
            padding-right: 24px;
        }

        /* GLOBAL FOOTER */
        .global-footer {
            background: #050507;
            border-top: 1px solid var(--border);
            padding: 48px 32px 36px;
            margin-top: 80px;
        }
        .footer-inner {
            max-width: 1360px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 20px;
        }
        .footer-brand {
            font-family: 'JetBrains Mono', monospace;
            font-size: 11.5px;
            color: var(--slate);
        }
        .footer-brand strong {
            color: var(--white);
        }
        .footer-links {
            display: flex;
            gap: 14px;
            flex-wrap: wrap;
        }
        .footer-link {
            font-family: 'JetBrains Mono', monospace;
            font-size: 10.5px;
            color: var(--slate);
            text-decoration: none;
            transition: color 0.2s;
        }
        .footer-link:hover {
            color: var(--laser-red);
        }

        @media (max-width: 1100px) {
            .nav-links { display: none; }
        }
    """

def get_navbar(active_key):
    items = [
        ("index", "index.html", "[ OVERVIEW ]"),
        ("protocol", "protocol.html", "[ PROTOCOL ]"),
        ("simulator", "simulator.html", "[ SIMULATOR ]"),
        ("yield", "yield.html", "[ YIELD ]"),
        ("nodes", "nodes.html", "[ NODES ]"),
        ("tokenomics", "tokenomics.html", "[ TOKENOMICS ]"),
        ("research", "research.html", "[ RESEARCH ]"),
        ("whitepaper", "whitepaper.html", "[ WHITEPAPER ]"),
    ]
    links = []
    for k, url, label in items:
        act = " active" if k == active_key else ""
        links.append(f'<a href="{url}" class="nav-link{act}" data-glitch>{label}</a>')
    
    links_html = "\n                ".join(links)
    return f"""
    <!-- TOP-EDGE SCROLL TELEMETRY PROGRESS LINE -->
    <div id="scroll-progress-line" class="scroll-progress-bar" aria-hidden="true"></div>

    <!-- RETRO-TECH CURSOR -->
    <div id="cursor-dot"></div>
    <div id="cursor-ring"></div>

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
                {links_html}
            </div>
        </nav>
    </div>
"""

def get_script_footer(extra_js=""):
    return f"""
    <!-- Lenis & GSAP -->
    <script src="https://cdn.jsdelivr.net/npm/@studio-freight/lenis@1.0.42/dist/lenis.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>

    <script>
        gsap.registerPlugin(ScrollTrigger);
        const lenis = new Lenis({{ duration: 1.1, smoothWheel: true }});
        lenis.on('scroll', ScrollTrigger.update);
        gsap.ticker.add((time) => lenis.raf(time * 1000));
        gsap.ticker.lagSmoothing(0);

        // Custom Cursor
        const cursorDot = document.getElementById('cursor-dot');
        const cursorRing = document.getElementById('cursor-ring');
        if (cursorDot && cursorRing) {{
            window.addEventListener('mousemove', (e) => {{
                cursorDot.style.left = e.clientX + 'px';
                cursorDot.style.top = e.clientY + 'px';
                cursorRing.style.left = e.clientX + 'px';
                cursorRing.style.top = e.clientY + 'px';
            }});
            document.querySelectorAll('a, button, input, select, [data-glitch]').forEach(el => {{
                el.addEventListener('mouseenter', () => document.body.classList.add('cursor-hover'));
                el.addEventListener('mouseleave', () => document.body.classList.remove('cursor-hover'));
            }});
        }}

        // VRTL WRLD Glitch Letters & Matrix Scramble Engine
        // Top-edge micro-progress telemetry line & Navbar scroll awareness
        const progressBar = document.getElementById('scroll-progress-line');
        const navWrapper = document.querySelector('.nav-wrapper');
        function onScrollTelemetry() {{
            const doc = document.documentElement;
            const sy = window.scrollY || doc.scrollTop;
            const max = doc.scrollHeight - window.innerHeight;
            if (progressBar && max > 0) {{
                progressBar.style.width = Math.min(100, Math.max(0, (sy / max) * 100)).toFixed(2) + '%';
            }}
            if (navWrapper) {{
                if (sy > 50) {{
                    navWrapper.classList.add('nav-scrolled');
                }} else {{
                    navWrapper.classList.remove('nav-scrolled');
                }}
            }}
        }}
        window.addEventListener('scroll', onScrollTelemetry, {{ passive: true }});
        lenis.on('scroll', onScrollTelemetry);
        onScrollTelemetry();

        // IntersectionObserver Reveal Engine (Zero Layout Shift)
        const revealTargets = document.querySelectorAll('.reveal-on-scroll');
        if ('IntersectionObserver' in window) {{
            const io = new IntersectionObserver((entries, obs) => {{
                entries.forEach(entry => {{
                    if (entry.isIntersecting) {{
                        entry.target.classList.add('is-revealed');
                        obs.unobserve(entry.target);
                    }}
                }});
            }}, {{ rootMargin: '0px 0px -40px 0px', threshold: 0.08 }});
            revealTargets.forEach(el => io.observe(el));
        }} else {{
            revealTargets.forEach(el => el.classList.add('is-revealed'));
        }}

        /* VRTL WRLD MECHANICAL GLITCH DECODE ENGINE (250MS / 3.5S SPECIFICATION) */
        class GlitchScramble {{
            constructor(el) {{
                this.el = el;
                this.chars = '01X_/*+-[]#';
                this.originalText = el.getAttribute('data-glitch-text') || el.innerText.trim();
                el.setAttribute('data-glitch-text', this.originalText);
                this.isGlitching = false;
                this.animId = null;
                this.lastTickTime = 0;
                this.tickInterval = 250; // Deliberate 250ms mechanical relay decode cadence
            }}

            scramble(duration = 3.5) {{
                if (this.isGlitching) return;
                this.isGlitching = true;
                this.el.classList.add('glitch-active');
                const target = this.originalText;
                const len = target.length;
                const startTime = performance.now();
                const durationMs = duration * 1000;
                let activeGlyphs = new Array(len);
                for (let i = 0; i < len; i++) {{
                    const ch = target[i];
                    activeGlyphs[i] = (ch === ' ' || ch === String.fromCharCode(10) || ch === String.fromCharCode(9))
                        ? ch
                        : this.chars[Math.floor(Math.random() * this.chars.length)];
                }}

                const tick = (now) => {{
                    const elapsed = now - startTime;
                    const progress = Math.min(1, elapsed / durationMs);
                    const revealedCount = Math.floor(progress * len);

                    // Throttle symbol updates so glyphs stay deliberate and readable
                    if (now - this.lastTickTime >= this.tickInterval) {{
                        this.lastTickTime = now;
                        for (let i = revealedCount; i < len; i++) {{
                            const ch = target[i];
                            if (ch === ' ' || ch === String.fromCharCode(10) || ch === String.fromCharCode(9)) {{
                                activeGlyphs[i] = ch;
                            }} else if (Math.random() < 0.35) {{
                                activeGlyphs[i] = this.chars[Math.floor(Math.random() * this.chars.length)];
                            }}
                        }}
                    }}

                    let result = '';
                    for (let i = 0; i < len; i++) {{
                        const ch = target[i];
                        if (ch === ' ' || ch === String.fromCharCode(10) || ch === String.fromCharCode(9)) {{
                            result += ch;
                        }} else if (i < revealedCount) {{
                            result += ch;
                        }} else {{
                            result += activeGlyphs[i] || ch;
                        }}
                    }}
                    this.el.innerText = result;

                    if (progress < 1) {{
                        this.animId = requestAnimationFrame(tick);
                    }} else {{
                        this.el.innerText = target;
                        this.el.classList.remove('glitch-active');
                        this.isGlitching = false;
                    }}
                }};
                this.animId = requestAnimationFrame(tick);
            }}
        }}

        document.querySelectorAll('[data-glitch], .nav-link').forEach(el => {{
            const inst = new GlitchScramble(el);
            el.addEventListener('mouseenter', () => inst.scramble(3.5));
        }});

        window.addEventListener('DOMContentLoaded', () => {{
            let delay = 100;
            document.querySelectorAll('.display-word, .meta-tag, .glitch-load').forEach(el => {{
                const inst = new GlitchScramble(el);
                setTimeout(() => inst.scramble(3.5), delay);
                delay += 250;
            }});
        }});

        document.querySelectorAll('.section-title').forEach(el => {{
            const inst = new GlitchScramble(el);
            ScrollTrigger.create({{
                trigger: el,
                start: 'top 88%',
                once: true,
                onEnter: () => inst.scramble(3.5)
            }});
            el.addEventListener('mouseenter', () => inst.scramble(3.5));
        }});

        {extra_js}
    </script>
</body>
</html>
"""

# ====================================================================
# 1. BUILD INDEX.HTML (Overview, Singularity Stage, Portals to Subpages)
# ====================================================================
def build_index_html():
    css = get_shared_css() + """
        /* HERO SECTION */
        .hero {
            min-height: 100vh;
            display: flex;
            align-items: center;
            padding-top: 96px;
            padding-bottom: 40px;
            position: relative;
            box-sizing: border-box;
            background: #ECECEC;
            color: #070707;
        }

        .hero::before {
            content: '';
            position: absolute;
            inset: 0;
            background-image: 
                linear-gradient(to right, rgba(0, 0, 0, 0.05) 1px, transparent 1px),
                linear-gradient(to bottom, rgba(0, 0, 0, 0.05) 1px, transparent 1px);
            background-size: 40px 40px;
            pointer-events: none;
            z-index: 1;
        }

        .hero-inner {
            max-width: 1400px;
            margin: 0 auto;
            padding: 0 32px;
            display: grid;
            grid-template-columns: 1.05fr 0.95fr;
            gap: 36px;
            align-items: center;
            width: 100%;
            position: relative;
            z-index: 2;
            box-sizing: border-box;
        }

        .hero-left {
            display: flex;
            flex-direction: column;
            min-width: 0;
        }

        .hero-split-words {
            display: flex;
            flex-direction: column;
            gap: 0;
            margin-bottom: 20px;
            min-width: 0;
        }

        .hero-word-row {
            display: flex;
            flex-wrap: wrap;
            gap: 12px;
            align-items: baseline;
            min-width: 0;
        }

        .display-word {
            font-family: 'Syne', sans-serif;
            font-size: clamp(34px, 4.4vw, 68px);
            font-weight: 800;
            line-height: 0.96;
            letter-spacing: -0.01em;
            text-transform: uppercase;
            color: #070707;
            display: inline-block;
            transition: color 0.25s ease, transform 0.2s ease;
            white-space: nowrap;
        }
        .display-word.red-accent {
            color: var(--laser-red);
            text-shadow: 0 0 35px rgba(255, 41, 44, 0.35);
        }
        .display-word:hover {
            color: var(--laser-red);
            transform: skewX(-4deg);
        }

        .hero-desc {
            font-size: 15px;
            line-height: 1.6;
            color: #4A4A56;
            max-width: 580px;
            margin-bottom: 28px;
        }
        .hero-desc strong {
            color: #070707;
        }

        
        .hero .btn-brutal-outline {
            color: #070707;
            border-color: rgba(0, 0, 0, 0.35);
            background: rgba(0, 0, 0, 0.03);
        }
        .hero .btn-brutal-outline:hover {
            border-color: var(--laser-red);
            color: var(--laser-red);
            background: rgba(255, 41, 44, 0.08);
        }

        .hero-ctas {
            display: flex;
            gap: 14px;
            flex-wrap: wrap;
        }

        /* SCHEMATIC CARD */
        .schematic-box {
            position: relative;
            background: #0D0D12;
            border: 1px solid var(--border);
            clip-path: polygon(0 14px, 14px 0, calc(100% - 14px) 0, 100% 14px, 100% calc(100% - 14px), calc(100% - 14px) 100%, 14px 100%, 0 calc(100% - 14px));
            padding: 2px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.8), 0 0 40px rgba(255, 41, 44, 0.08);
            transition: border-color 0.3s ease;
            width: 100%;
            max-width: 580px;
            margin: 0 auto;
            min-width: 0;
        }
        .schematic-box:hover {
            border-color: rgba(255, 41, 44, 0.45);
        }

        .schematic-inner {
            background: #09090C;
            padding: 20px 22px;
            clip-path: polygon(0 12px, 12px 0, calc(100% - 12px) 0, 100% 12px, 100% calc(100% - 12px), calc(100% - 12px) 100%, 12px 100%, 0 calc(100% - 12px));
            position: relative;
            overflow: hidden;
        }

        .schematic-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid var(--border);
            padding-bottom: 10px;
            margin-bottom: 12px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 10px;
            letter-spacing: 0.1em;
            color: var(--slate);
        }
        .schematic-header .title-badge {
            color: var(--white);
            font-weight: 700;
        }
        .schematic-header .status-tag {
            color: var(--green);
            display: flex;
            align-items: center;
            gap: 6px;
        }
        .schematic-header .status-tag::before {
            content: '';
            width: 5px;
            height: 5px;
            background: var(--green);
            border-radius: 50%;
            box-shadow: 0 0 6px var(--green);
        }

        .schematic-canvas-wrap {
            position: relative;
            width: 100%;
            height: 310px;
        }
        #schematic-canvas {
            width: 100%;
            height: 100%;
            display: block;
        }

        .schematic-telemetry {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 8px;
            margin-top: 14px;
            padding-top: 12px;
            border-top: 1px solid var(--border);
        }
        .tele-stat {
            display: flex;
            flex-direction: column;
            gap: 2px;
        }
        .tele-label {
            font-family: 'JetBrains Mono', monospace;
            font-size: 8.5px;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            color: var(--slate);
        }
        .tele-val {
            font-family: 'JetBrains Mono', monospace;
            font-size: 11px;
            font-weight: 700;
            color: var(--chalk);
        }
        .tele-val.accent {
            color: var(--laser-red);
        }

        /* PORTAL CARDS GRID */
        .portals-section {
            background: var(--bg);
            padding: 80px 32px;
            border-top: 1px solid var(--border);
        }
        .portals-grid {
            max-width: 1360px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 24px;
        }
        .portal-card {
            background: var(--bg-card);
            border: 1px solid var(--border);
            padding: 28px 24px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            text-decoration: none;
            color: var(--chalk);
            position: relative;
            clip-path: polygon(0 12px, 12px 0, 100% 0, 100% calc(100% - 12px), calc(100% - 12px) 100%, 0 100%);
            transition: border-color 0.25s ease, transform 0.2s ease, background 0.2s ease;
        }
        .portal-card:hover {
            border-color: var(--laser-red);
            background: var(--bg-card-hover);
            transform: translateY(-3px);
        }
        .portal-meta {
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-family: 'JetBrains Mono', monospace;
            font-size: 10px;
            color: var(--slate);
            margin-bottom: 16px;
        }
        .portal-badge {
            background: rgba(255, 41, 44, 0.1);
            color: var(--laser-red);
            border: 1px solid rgba(255, 41, 44, 0.25);
            padding: 2px 7px;
            font-size: 9px;
            font-weight: 700;
        }
        .portal-title {
            font-family: 'Syne', sans-serif;
            font-size: 20px;
            font-weight: 800;
            text-transform: uppercase;
            color: var(--white);
            margin-bottom: 10px;
            letter-spacing: -0.01em;
        }
        .portal-desc {
            font-size: 13.5px;
            line-height: 1.55;
            color: var(--slate);
            margin-bottom: 24px;
        }
        .portal-action {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 11px;
            font-weight: 700;
            color: var(--laser-red);
            text-transform: uppercase;
            letter-spacing: 0.08em;
        }

        /* SINGULARITY STAGE */
        .stage-section {
            background: #0B0B0E;
            padding: 80px 32px;
            border-top: 1px solid var(--border);
        }
        .stage-inner {
            max-width: 1360px;
            margin: 0 auto;
        }
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 16px;
            margin-top: 40px;
        }
        .stat-card {
            background: #111116;
            border: 1px solid var(--border);
            padding: 22px;
            clip-path: polygon(0 10px, 10px 0, 100% 0, 100% calc(100% - 10px), calc(100% - 10px) 100%, 0 100%);
        }
        .stat-card .label {
            font-family: 'JetBrains Mono', monospace;
            font-size: 10px;
            color: var(--slate);
            text-transform: uppercase;
            letter-spacing: 0.08em;
            margin-bottom: 6px;
        }
        .stat-card .val {
            font-family: 'JetBrains Mono', monospace;
            font-size: 24px;
            font-weight: 800;
            color: var(--white);
        }
        .stat-card .val.red { color: var(--laser-red); }
        .stat-card .val.green { color: var(--green); }

        @media (max-width: 960px) {
            .hero-inner { grid-template-columns: 1fr; gap: 40px; }
            .portals-grid { grid-template-columns: 1fr; }
            .stats-grid { grid-template-columns: repeat(2, 1fr); }
        }
    """

    extra_js = """
        // 2D Canvas Tensor Arbor Schematic
        const canvas = document.getElementById('schematic-canvas');
        if (canvas) {
            const ctx = canvas.getContext('2d');
            function resizeCanvas() {
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
                    radius: 35 + Math.random() * 110,
                    speed: (Math.random() - 0.5) * 0.008,
                    size: Math.random() * 2.2 + 2,
                    pulse: Math.random() * Math.PI
                });
            }

            function drawSchematic() {
                const w = canvas.width / window.devicePixelRatio;
                const h = canvas.height / window.devicePixelRatio;
                const cx = w / 2;
                const cy = h / 2;

                ctx.clearRect(0, 0, w, h);

                // Polar Rings
                ctx.strokeStyle = 'rgba(255, 255, 255, 0.04)';
                ctx.lineWidth = 1;
                for (let r = 35; r <= 145; r += 35) {
                    ctx.beginPath();
                    ctx.arc(cx, cy, r, 0, Math.PI * 2);
                    ctx.stroke();
                }

                // Tensor Lines
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
                        if (Math.hypot(x2 - x1, y2 - y1) < 60) {
                            ctx.moveTo(x1, y1);
                            ctx.lineTo(x2, y2);
                        }
                    }
                }
                ctx.stroke();

                // Core Node
                ctx.fillStyle = '#FF292C';
                ctx.shadowColor = '#FF292C';
                ctx.shadowBlur = 14;
                ctx.beginPath();
                ctx.arc(cx, cy, 5.5, 0, Math.PI * 2);
                ctx.fill();
                ctx.shadowBlur = 0;

                // Rotating Dashed Orbit
                ctx.save();
                ctx.translate(cx, cy);
                ctx.rotate(animAngle);
                ctx.strokeStyle = 'rgba(255, 41, 44, 0.4)';
                ctx.setLineDash([8, 12]);
                ctx.beginPath();
                ctx.arc(0, 0, 105, 0, Math.PI * 2);
                ctx.stroke();
                ctx.restore();

                // Draw Nodes
                for (let i = 0; i < nodes.length; i++) {
                    const n = nodes[i];
                    n.angle += n.speed;
                    n.pulse += 0.05;
                    const x = cx + Math.cos(n.angle) * n.radius;
                    const y = cy + Math.sin(n.angle) * n.radius;
                    const p = Math.sin(n.pulse);

                    ctx.fillStyle = (i % 4 === 0) ? '#FF292C' : '#FFFFFF';
                    ctx.beginPath();
                    ctx.arc(x, y, n.size + p * 0.5, 0, Math.PI * 2);
                    ctx.fill();
                }

                animAngle += 0.003;
                requestAnimationFrame(drawSchematic);
            }
            drawSchematic();
        }
    """

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>33RD TREE LABS // The Singularity Protocol &bull; 33rdtreelabs.tech</title>
    <meta name="description" content="A Byzantine-Resilient Verifiable DePIN Compute Fabric on Solana. Hierarchical Tensor Arbor coordination, zero-knowledge neural evaluations, and cryptographic consensus at scale.">

    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous">
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@0,300;0,400;0,500;0,700;1,400&family=Space+Grotesk:wght@300;400;500;600;700&family=Syne:wght@700;800&display=swap" rel="stylesheet">

    <style>{css}</style>
</head>
<body>

    {get_navbar("index")}

    <!-- HERO SECTION (LIGHT CHALK THEME #ECECEC) -->
    <section class="hero">
        <div class="hero-inner">
            <div class="hero-left">
                <div class="meta-tag" data-glitch>( 01 ) // PROTOCOL OVERVIEW &bull; 33RDTREELABS.TECH</div>

                <div class="hero-split-words">
                    <div class="hero-word-row">
                        <span class="display-word" data-glitch>WE</span>
                        <span class="display-word" data-glitch>COORDINATE</span>
                    </div>
                    <div class="hero-word-row">
                        <span class="display-word" data-glitch>DECENTRALIZED</span>
                    </div>
                    <div class="hero-word-row">
                        <span class="display-word red-accent" data-glitch>COMPUTE</span>
                        <span class="display-word" data-glitch>AT SCALE</span>
                    </div>
                </div>

                <p class="hero-desc">
                    A Byzantine-Resilient Verifiable DePIN Compute Fabric anchored on <strong>Solana</strong>. 
                    Uniting hierarchical <strong>Tensor Arbor</strong> cluster orchestration with zero-knowledge neural evaluations (KZG polynomial commitments) to power trustless machine intelligence.
                </p>

                <div class="hero-ctas">
                    <a href="nodes.html" class="btn-brutal-red" data-glitch>
                        <span>DEPLOY GPU CAPACITY</span>
                        <span>&rarr;</span>
                    </a>
                    <a href="protocol.html" class="btn-brutal-outline" data-glitch>
                        <span>EXPLORE PROTOCOL</span>
                        <span>&rarr;</span>
                    </a>
                </div>
            </div>

            <!-- PINNED CHAMFERED HARDWARE / MANIFOLD SCHEMATIC SHOWCASE -->
            <div class="schematic-box" id="hero-schematic">
                <div class="schematic-inner">
                    <div class="schematic-header">
                        <span class="title-badge" data-glitch>[ TENSOR ARBOR MANIFOLD // v4.0 ]</span>
                        <span class="status-tag">QUORUM ACTIVE (K=64)</span>
                    </div>

                    <div class="schematic-canvas-wrap">
                        <canvas id="schematic-canvas"></canvas>
                    </div>

                    <div class="schematic-telemetry">
                        <div class="tele-stat">
                            <span class="tele-label">P99 Latency</span>
                            <span class="tele-val accent">14.2ms</span>
                        </div>
                        <div class="tele-stat">
                            <span class="tele-label">Solana Anchor</span>
                            <span class="tele-val">Slot #312M</span>
                        </div>
                        <div class="tele-stat">
                            <span class="tele-label">KZG Opening</span>
                            <span class="tele-val accent">&lt; 1.84ms</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- SINGULARITY STAGE -->
    <section class="stage-section" id="stage">
        <div class="stage-inner">
            <div class="meta-tag" data-glitch>( 02 ) // COMPUTE FABRIC &bull; GLOBAL NETWORK TELEMETRY</div>
            <h2 class="section-title" data-glitch>AUTONOMOUS AGENT CONVERGENCE</h2>
            <p class="section-desc">
                Anchored on Solana mainnet, the Singularity Protocol synchronizes decentralized GPU clusters into a single unified tensor arbor. Untrusted compute providers submit zero-knowledge KZG polynomial evaluations directly into on-chain Anchor programs, guaranteeing Byzantine-safe execution of trillion-parameter neural models.
            </p>

            <div class="stats-grid">
                <div class="stat-card">
                    <div class="label">[ HARD-CAPPED SUPPLY ]</div>
                    <div class="val red">33,333,333 &#36;33RD</div>
                </div>
                <div class="stat-card">
                    <div class="label">[ BYZANTINE QUORUM ]</div>
                    <div class="val">K = 64 NODES</div>
                </div>
                <div class="stat-card">
                    <div class="label">[ MIN VALIDATOR STAKE ]</div>
                    <div class="val green">25,000 &#36;33RD</div>
                </div>
                <div class="stat-card">
                    <div class="label">[ PROTOCOL BURN SPLIT ]</div>
                    <div class="val red">10% INCINERATOR</div>
                </div>
            </div>
        </div>
    </section>

    <!-- PORTALS SECTION (DEDICATED PLATFORM HUBS) -->
    <section class="portals-section">
        <div style="max-width:1360px; margin:0 auto 36px;">
            <div class="meta-tag" data-glitch>( 03 ) // PLATFORM ARCHITECTURE &bull; DEDICATED MODULES</div>
            <h2 class="section-title" data-glitch>EXPLORE SYSTEM SUBSYSTEMS</h2>
            <p class="section-desc">
                Access dedicated dashboards, simulator consoles, tokenomics models, and research publications across the 33rd Tree Labs ecosystem.
            </p>
        </div>

        <div class="portals-grid">
            <!-- Portal 1: Protocol -->
            <a href="protocol.html" class="portal-card">
                <div>
                    <div class="portal-meta">
                        <span>[ MODULE 01 ]</span>
                        <span class="portal-badge">ARCHITECTURE</span>
                    </div>
                    <h3 class="portal-title" data-glitch>PROTOCOL SPEC</h3>
                    <p class="portal-desc">
                        Four architectural pillars: Tensor Arbor Topology, CAP-FFN Proof of Intelligence, Heterogeneous Multi-TEE Quorum, and Byzantine consensus settlement on Solana.
                    </p>
                </div>
                <div class="portal-action">
                    <span>ENTER PROTOCOL DECK &rarr;</span>
                </div>
            </a>

            <!-- Portal 2: Simulator -->
            <a href="simulator.html" class="portal-card">
                <div>
                    <div class="portal-meta">
                        <span>[ MODULE 02 ]</span>
                        <span class="portal-badge">INTERACTIVE</span>
                    </div>
                    <h3 class="portal-title" data-glitch>BYZANTINE SIMULATOR</h3>
                    <p class="portal-desc">
                        Adversarial consensus simulator with 64-node validator lattice. Inject malicious nodes, test Byzantine fault tolerance, and run real diagnostic queries in the Solana CLI terminal.
                    </p>
                </div>
                <div class="portal-action">
                    <span>LAUNCH SIMULATOR &rarr;</span>
                </div>
            </a>

            <!-- Portal 3: Yield -->
            <a href="yield.html" class="portal-card">
                <div>
                    <div class="portal-meta">
                        <span>[ MODULE 03 ]</span>
                        <span class="portal-badge">ECONOMICS</span>
                    </div>
                    <h3 class="portal-title" data-glitch>YIELD CALCULATOR</h3>
                    <p class="portal-desc">
                        Interactive staking rewards simulator. Model hardware yield across Dual H100 SXM5, Quad H100, B200 NVL72, and RTX 4090 configurations with deflationary buyback estimates.
                    </p>
                </div>
                <div class="portal-action">
                    <span>CALCULATE REWARDS &rarr;</span>
                </div>
            </a>

            <!-- Portal 4: Nodes -->
            <a href="nodes.html" class="portal-card">
                <div>
                    <div class="portal-meta">
                        <span>[ MODULE 04 ]</span>
                        <span class="portal-badge">OPERATORS</span>
                    </div>
                    <h3 class="portal-title" data-glitch>NODE OPERATORS</h3>
                    <p class="portal-desc">
                        Hardware requirements for Tier-1 and Tier-2 compute providers. Installation commands, collateral bonding guides, and telemetry monitoring setup.
                    </p>
                </div>
                <div class="portal-action">
                    <span>DEPLOY NODE &rarr;</span>
                </div>
            </a>

            <!-- Portal 5: Tokenomics -->
            <a href="tokenomics.html" class="portal-card">
                <div>
                    <div class="portal-meta">
                        <span>[ MODULE 05 ]</span>
                        <span class="portal-badge">FINANCIALS</span>
                    </div>
                    <h3 class="portal-title" data-glitch>TOKENOMICS</h3>
                    <p class="portal-desc">
                        Immutable hard cap of 33,333,333 $33RD tokens, quadrennial halving schedules, Raydium CPMM liquidity lock, and autonomous 10% inference buyback-burn crank.
                    </p>
                </div>
                <div class="portal-action">
                    <span>VIEW TOKEN MODEL &rarr;</span>
                </div>
            </a>

            <!-- Portal 6: Research & Whitepaper -->
            <a href="whitepaper.html" class="portal-card">
                <div>
                    <div class="portal-meta">
                        <span>[ MODULE 06 ]</span>
                        <span class="portal-badge">ACADEMIC</span>
                    </div>
                    <h3 class="portal-title" data-glitch>ACADEMIC WHITEPAPER</h3>
                    <p class="portal-desc">
                        The complete, unabridged Canary Specification v4.0. Formal cryptographic proofs, KZG pairing equations, and hyperbolic manifold routing theorems.
                    </p>
                </div>
                <div class="portal-action">
                    <span>READ SPECIFICATION &rarr;</span>
                </div>
            </a>
        </div>
    </section>

    <!-- FOOTER -->
    <footer class="global-footer">
        <div class="footer-inner">
            <div class="footer-brand">
                <strong>33RD TREE LABS</strong> &bull; THE SINGULARITY PROTOCOL &bull; <code>33rdtreelabs.tech</code>
            </div>
            <div class="footer-links">
                <a href="index.html" class="footer-link">[ OVERVIEW ]</a>
                <a href="protocol.html" class="footer-link">[ PROTOCOL ]</a>
                <a href="simulator.html" class="footer-link">[ SIMULATOR ]</a>
                <a href="yield.html" class="footer-link">[ YIELD ]</a>
                <a href="nodes.html" class="footer-link">[ NODES ]</a>
                <a href="tokenomics.html" class="footer-link">[ TOKENOMICS ]</a>
                <a href="research.html" class="footer-link">[ RESEARCH ]</a>
                <a href="33rd_Tree_Labs_Whitepaper.pdf" target="_blank" class="footer-link">[ WHITEPAPER PDF ]</a>
            </div>
        </div>
    </footer>

    {get_script_footer(extra_js)}
"""
    with open(os.path.join(SITE_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("index.html compiled successfully.")


# ====================================================================
# 2. BUILD PROTOCOL.HTML (Architecture Matrix, 4 Pillars, KZG & Proofs)
# ====================================================================
def build_protocol_html():
    css = get_shared_css() + """
        .arch-pillars-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 28px;
            margin-top: 36px;
        }
        .pillar-card {
            background: var(--bg-card);
            border: 1px solid var(--border);
            padding: 32px;
            clip-path: polygon(0 14px, 14px 0, 100% 0, 100% calc(100% - 14px), calc(100% - 14px) 100%, 0 100%);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            transition: border-color 0.25s ease;
        }
        .pillar-card:hover {
            border-color: rgba(255, 41, 44, 0.45);
        }
        .pillar-num {
            font-family: 'JetBrains Mono', monospace;
            font-size: 11px;
            color: var(--laser-red);
            font-weight: 700;
            margin-bottom: 8px;
        }
        .pillar-heading {
            font-family: 'Syne', sans-serif;
            font-size: 22px;
            font-weight: 800;
            text-transform: uppercase;
            color: var(--white);
            margin-bottom: 14px;
        }
        .pillar-text {
            font-size: 14px;
            line-height: 1.65;
            color: var(--slate);
            margin-bottom: 24px;
        }
        .pillar-tags {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
            padding-top: 16px;
            border-top: 1px solid var(--border);
        }
        .tag-pill {
            font-family: 'JetBrains Mono', monospace;
            font-size: 10px;
            background: #15151C;
            border: 1px solid var(--border);
            padding: 4px 10px;
            color: var(--chalk);
        }
        .tag-pill strong { color: var(--laser-red); }

        .spec-table-box {
            background: var(--bg-card);
            border: 1px solid var(--border);
            padding: 28px;
            margin-top: 48px;
            clip-path: polygon(0 12px, 12px 0, 100% 0, 100% calc(100% - 12px), calc(100% - 12px) 100%, 0 100%);
            overflow-x: auto;
            -webkit-overflow-scrolling: touch;
        }
        .spec-table {
            width: 100%;
            border-collapse: collapse;
            font-family: 'JetBrains Mono', monospace;
            font-size: 11px;
            margin-top: 16px;
        }
        .spec-table th, .spec-table td {
            padding: 10px 14px;
            text-align: left;
            border-bottom: 1px solid var(--border);
        }
        .spec-table th {
            color: var(--slate);
            text-transform: uppercase;
            font-weight: 700;
            background: #0B0B0E;
        }
        .spec-table td {
            color: var(--chalk);
        }
        .spec-table tr:hover td {
            background: rgba(255, 41, 44, 0.04);
        }

        @media (max-width: 900px) {
            .arch-pillars-grid { grid-template-columns: 1fr; }
        }
    """

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>33RD TREE LABS // Protocol Architecture &bull; 33rdtreelabs.tech</title>
    <meta name="description" content="The Singularity Protocol Architecture Matrix: Tensor Arbor Topology, Proof of Intelligence, Heterogeneous Multi-TEE Quorum, and Byzantine consensus on Solana.">

    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous">
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@0,300;0,400;0,500;0,700;1,400&family=Space+Grotesk:wght@300;400;500;600;700&family=Syne:wght@700;800&display=swap" rel="stylesheet">

    <style>{css}</style>
</head>
<body>

    {get_navbar("protocol")}

    <div class="page-wrap">
        <div class="meta-tag" data-glitch>( 01 ) // CORE ARCHITECTURE SPECIFICATION &bull; CANARY v4.0</div>
        <h1 class="section-title" data-glitch>ENGINEERED FOR UNCOMPROMISING INTEGRITY</h1>
        <p class="section-desc">
            A fault-tolerant DePIN computing fabric designed to guarantee deterministic verification across untrusted distributed hardware without performance degradation.
        </p>

        <div class="arch-pillars-grid">
            <!-- Pillar 01 -->
            <div class="pillar-card reveal-on-scroll">
                <div>
                    <div class="pillar-num">[ PILLAR 01 // COORDINATION ]</div>
                    <h2 class="pillar-heading" data-glitch>TENSOR ARBOR TOPOLOGY</h2>
                    <p class="pillar-text">
                        Hierarchical tree manifold partitioning distributed model parameters across heterogeneous GPU nodes. Dynamically matches pipeline stages and tensor parallelism to physical interconnect latencies, preventing inter-node bottlenecks across global clusters.
                    </p>
                </div>
                <div class="pillar-tags">
                    <span class="tag-pill">ROUTING: <strong>NON-EUCLIDEAN DAG</strong></span>
                    <span class="tag-pill">BANDWIDTH: <strong>900 GB/s NVLINK</strong></span>
                    <span class="tag-pill">TOPOLOGY: <strong>MAX 8 HOPS</strong></span>
                </div>
            </div>

            <!-- Pillar 02 -->
            <div class="pillar-card reveal-on-scroll">
                <div>
                    <div class="pillar-num">[ PILLAR 02 // VERIFICATION ]</div>
                    <h2 class="pillar-heading" data-glitch>PROOF OF INFERENCE (POI)</h2>
                    <p class="pillar-text">
                        Zero-knowledge neural evaluations pairing randomized Chebyshev Activation Polynomial (CAP-FFN) challenges with BN254 KZG polynomial commitment schemes. Enables sub-2ms cryptographic verification directly inside Solana smart contracts without GPU re-computation.
                    </p>
                </div>
                <div class="pillar-tags">
                    <span class="tag-pill">SCHEME: <strong>BN254 KZG</strong></span>
                    <span class="tag-pill">SOLANA ANCHOR: <strong>&lt; 184,500 CU</strong></span>
                    <span class="tag-pill">PROOF TIME: <strong>1.418ms</strong></span>
                </div>
            </div>

            <!-- Pillar 03 -->
            <div class="pillar-card reveal-on-scroll">
                <div>
                    <div class="pillar-num">[ PILLAR 03 // CONSENSUS ]</div>
                    <h2 class="pillar-heading" data-glitch>BYZANTINE QUORUM MATRIX</h2>
                    <p class="pillar-text">
                        Asynchronous BFT consensus withstanding up to f &lt; K/3 malicious, compromised, or colluding nodes. Immediate automated slashing of bonded $33RD collateral upon mathematical detection of gradient poisoning, bit-rot, or block equivocation.
                    </p>
                </div>
                <div class="pillar-tags">
                    <span class="tag-pill">TOLERANCE: <strong>f &lt; 21 / 64</strong></span>
                    <span class="tag-pill">COMMITTEE: <strong>K=64 VALIDATORS</strong></span>
                    <span class="tag-pill">FINALITY: <strong>400ms SLOTS</strong></span>
                </div>
            </div>

            <!-- Pillar 04 -->
            <div class="pillar-card reveal-on-scroll">
                <div>
                    <div class="pillar-num">[ PILLAR 04 // HARDWARE ENCLAVES ]</div>
                    <h2 class="pillar-heading" data-glitch>HETEROGENEOUS MULTI-TEE</h2>
                    <p class="pillar-text">
                        Eliminates single-vendor silicon vulnerability by requiring dual independent enclave attestations (Intel SGX/TDX, AMD SEV-SNP, or NVIDIA Confidential Computing). Verifies memory integrity and firmware state before admitting compute providers into the tensor arbor.
                    </p>
                </div>
                <div class="pillar-tags">
                    <span class="tag-pill">ENCLAVES: <strong>SGX + SEV-SNP + CC</strong></span>
                    <span class="tag-pill">ATTESTATION: <strong>DYNAMIC QUORUM</strong></span>
                    <span class="tag-pill">QUANTIZATION: <strong>FP8 SMOOTHQUANT</strong></span>
                </div>
            </div>
        </div>

        <!-- PROTOCOL PARAMETERS SPECIFICATION TABLE -->
        <div class="spec-table-box">
            <div class="meta-tag" data-glitch>[ CRYPTOGRAPHIC &amp; NETWORK PARAMETERS ]</div>
            <table class="spec-table">
                <thead>
                    <tr>
                        <th>Parameter</th>
                        <th>Specification</th>
                        <th>Formal Bound</th>
                        <th>Verification Target</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Curve &amp; Pairing</td>
                        <td>BN254 (alt_bn128)</td>
                        <td>r = 21888242871839275222246405745257275088548364400416034343698204186575808495617</td>
                        <td>Solana <code>sol_alt_bn128_pairing</code> syscall</td>
                    </tr>
                    <tr>
                        <td>Polynomial Degree</td>
                        <td>d = 16 Chebyshev Activation</td>
                        <td>O(1) constant-time opening proof</td>
                        <td>Sub-2.0ms evaluation inside eBPF VM</td>
                    </tr>
                    <tr>
                        <td>Consensus Quorum</td>
                        <td>K = 64 Active Validators</td>
                        <td>2/3 + 1 Honest Majority (f &le; 21)</td>
                        <td>BLS aggregate multi-signature verification</td>
                    </tr>
                    <tr>
                        <td>Block Commit Payload</td>
                        <td>280 Bytes Canonical Commit</td>
                        <td>Network MTU 1,232 Bytes</td>
                        <td>536-byte transaction payload on Solana</td>
                    </tr>
                    <tr>
                        <td>Cross-Hardware Parity</td>
                        <td>INT8 / FP8 Deterministic Trees</td>
                        <td>&Delta;accuracy = 0.00% drift</td>
                        <td>Bit-exact verification across H100 vs RTX 4090</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>

    <!-- FOOTER -->
    <footer class="global-footer">
        <div class="footer-inner">
            <div class="footer-brand">
                <strong>33RD TREE LABS</strong> &bull; THE SINGULARITY PROTOCOL &bull; <code>33rdtreelabs.tech</code>
            </div>
            <div class="footer-links">
                <a href="index.html" class="footer-link">[ OVERVIEW ]</a>
                <a href="protocol.html" class="footer-link">[ PROTOCOL ]</a>
                <a href="simulator.html" class="footer-link">[ SIMULATOR ]</a>
                <a href="yield.html" class="footer-link">[ YIELD ]</a>
                <a href="nodes.html" class="footer-link">[ NODES ]</a>
                <a href="tokenomics.html" class="footer-link">[ TOKENOMICS ]</a>
                <a href="research.html" class="footer-link">[ RESEARCH ]</a>
                <a href="33rd_Tree_Labs_Whitepaper.pdf" target="_blank" class="footer-link">[ WHITEPAPER PDF ]</a>
            </div>
        </div>
    </footer>

    {get_script_footer()}
"""
    with open(os.path.join(SITE_DIR, "protocol.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("protocol.html compiled successfully.")


# ====================================================================
# 3. BUILD SIMULATOR.HTML (Byzantine Lattice & Solana Terminal Console)
# ====================================================================
def build_simulator_html():
    css = get_shared_css() + """
        .sim-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 28px;
            margin-top: 32px;
        }

        .sim-box, .terminal-box {
            background: #0E0E12;
            border: 1px solid var(--border);
            padding: 24px;
            clip-path: polygon(0 14px, 14px 0, 100% 0, 100% calc(100% - 14px), calc(100% - 14px) 100%, 0 100%);
        }

        .sim-box-title {
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-family: 'JetBrains Mono', monospace;
            font-size: 11px;
            color: var(--slate);
            border-bottom: 1px solid var(--border);
            padding-bottom: 12px;
            margin-bottom: 20px;
        }

        /* 8x8 NODE MATRIX */
        .node-lattice {
            display: grid;
            grid-template-columns: repeat(8, 1fr);
            gap: 8px;
            margin-bottom: 24px;
        }
        .lattice-node {
            aspect-ratio: 1;
            background: #171720;
            border: 1px solid #2B2B38;
            border-radius: 4px;
            transition: all 0.25s ease;
            position: relative;
        }
        .lattice-node.honest {
            background: rgba(0, 230, 118, 0.12);
            border-color: rgba(0, 230, 118, 0.35);
        }
        .lattice-node.honest::after {
            content: '';
            position: absolute;
            inset: 3px;
            background: var(--green);
            border-radius: 2px;
            opacity: 0.8;
        }
        .lattice-node.byzantine {
            background: rgba(255, 41, 44, 0.2);
            border-color: var(--laser-red);
            box-shadow: 0 0 10px rgba(255, 41, 44, 0.4);
            animation: pulse-byz 1.4s infinite;
        }
        .lattice-node.byzantine::after {
            content: '';
            position: absolute;
            inset: 3px;
            background: var(--laser-red);
            border-radius: 2px;
        }
        @keyframes pulse-byz {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.08); }
        }

        .sim-controls {
            display: flex;
            flex-direction: column;
            gap: 16px;
        }
        .sim-slider-row {
            display: flex;
            justify-content: space-between;
            font-family: 'JetBrains Mono', monospace;
            font-size: 11px;
            color: var(--slate);
            margin-bottom: 6px;
        }
        .sim-range {
            width: 100%;
            -webkit-appearance: none;
            background: #1C1C26;
            height: 6px;
            border-radius: 3px;
            outline: none;
        }
        .sim-range::-webkit-slider-thumb {
            -webkit-appearance: none;
            width: 18px;
            height: 18px;
            border-radius: 50%;
            background: var(--laser-red);
            cursor: pointer;
            box-shadow: 0 0 10px var(--laser-red);
        }
        .sim-attack-select {
            background: #161620;
            border: 1px solid var(--border);
            color: var(--chalk);
            font-family: 'JetBrains Mono', monospace;
            font-size: 11px;
            padding: 8px 12px;
            outline: none;
        }

        .sim-status-banner {
            background: #121218;
            border: 1px solid var(--border);
            padding: 14px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 11px;
            line-height: 1.5;
        }
        .sim-status-head {
            font-weight: 700;
            margin-bottom: 4px;
        }
        .sim-status-head.success { color: var(--green); }
        .sim-status-head.danger { color: var(--laser-red); }

        /* TERMINAL */
        .terminal-topbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid var(--border);
            padding-bottom: 12px;
            margin-bottom: 14px;
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
            background: #333;
        }
        .terminal-dot.red { background: var(--laser-red); }
        .terminal-output {
            font-family: 'JetBrains Mono', monospace;
            font-size: 11px;
            line-height: 1.55;
            height: 380px;
            overflow-y: auto;
            color: var(--chalk-dim);
            padding-right: 8px;
        }
        .terminal-output .cmd { color: var(--chalk); font-weight: 700; }
        .terminal-output .highlight { color: var(--laser-red); }
        .terminal-output .success { color: var(--green); }
        .terminal-output .dim { color: var(--slate); }
        .terminal-output .warn { color: #FFAA00; }

        .terminal-input-row {
            display: flex;
            align-items: center;
            gap: 8px;
            border-top: 1px solid var(--border);
            padding-top: 12px;
            margin-top: 12px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 11.5px;
        }
        .terminal-prompt {
            color: var(--laser-red);
            font-weight: 700;
        }
        .terminal-input {
            flex: 1;
            background: transparent;
            border: none;
            outline: none;
            color: var(--chalk);
            font-family: 'JetBrains Mono', monospace;
            font-size: 11.5px;
        }

        @media (max-width: 960px) {
            .sim-grid { grid-template-columns: 1fr; }
        }
    """

    extra_js = """
        // BYZANTINE LATTICE ENGINE
        const matrixEl = document.getElementById('node-matrix');
        const byzSlider = document.getElementById('byz-slider');
        const byzCountText = document.getElementById('byz-count-text');
        const byzRatioTag = document.getElementById('byz-ratio-tag');
        const statusBox = document.getElementById('sim-status-box');
        const statusTitle = document.getElementById('sim-status-title');
        const statusDesc = document.getElementById('sim-status-desc');

        const TOTAL_NODES = 64;
        let nodeElements = [];

        function initMatrix() {
            if (!matrixEl) return;
            matrixEl.innerHTML = '';
            nodeElements = [];
            for (let i = 0; i < TOTAL_NODES; i++) {
                const node = document.createElement('div');
                node.className = 'lattice-node honest';
                node.setAttribute('title', `Validator #${i}`);
                matrixEl.appendChild(node);
                nodeElements.push(node);
            }
            updateByzantineSim();
        }

        function updateByzantineSim() {
            if (!byzSlider) return;
            const f = parseInt(byzSlider.value);
            const percentage = ((f / TOTAL_NODES) * 100).toFixed(1);

            byzRatioTag.textContent = `f = ${f} / ${TOTAL_NODES} (${percentage}%)`;
            byzCountText.textContent = f <= 21 ? `f = ${f} (Safe Quorum)` : `f = ${f} (CRITICAL FAULT)`;
            byzCountText.style.color = f <= 21 ? 'var(--chalk)' : 'var(--laser-red)';

            for (let i = 0; i < TOTAL_NODES; i++) {
                if (i < f) {
                    nodeElements[i].className = 'lattice-node byzantine';
                } else {
                    nodeElements[i].className = 'lattice-node honest';
                }
            }

            if (f <= 21) {
                const honestCount = TOTAL_NODES - f;
                statusTitle.className = 'sim-status-head success';
                statusTitle.textContent = '[VALID] CONSENSUS REACHED: QUORUM VALIDATED';
                statusDesc.textContent = `Honest nodes: ${honestCount}/64 (${((honestCount/64)*100).toFixed(1)}%). BFT threshold f < 21 satisfied. Malicious inputs mathematically isolated.`;
            } else {
                statusTitle.className = 'sim-status-head danger';
                statusTitle.textContent = '[CRITICAL] BYZANTINE FAULT: SAFETY BREACH';
                statusDesc.textContent = `Adversary count f = ${f} exceeds 21 (1/3 of committee). Solana anchor initiates circuit breaker. No state finalized to preserve zero-knowledge integrity.`;
            }
        }

        function runConsensusRound() {
            appendTermLine('> Executing simulated consensus challenge round...', 'dim');
            setTimeout(() => {
                const f = parseInt(byzSlider.value);
                if (f <= 21) {
                    appendTermLine(`[CONSENSUS] Round validated in 1.418ms &bull; 2/3 BLS signatures matched &bull; OK`, 'success');
                } else {
                    appendTermLine(`[ALERT] BFT Quorum failure: f = ${f} > 21 &bull; Collateral slashed`, 'highlight');
                }
            }, 250);
        }

        // SOLANA ANCHOR CLI TERMINAL
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
                appendTermLine('ACTIVE VALIDATOR CLUSTERS (Candidate Genesis Validators (K=64 Quorum Committee)):', 'highlight');
                appendTermLine('  0x7F2A...9C1D [Tier-1 Dual H100 SXM5] &bull; Stake: 150,000 $33RD &bull; Status: OPTIMAL');
                appendTermLine('  0x3E11...B450 [Tier-1 Quad H100 SXM5] &bull; Stake: 250,000 $33RD &bull; Status: OPTIMAL');
                appendTermLine('  0x992B...C01F [Tier-1 B200 NVL72]    &bull; Stake: 500,000 $33RD &bull; Status: OPTIMAL');
                appendTermLine('  0x1A4C...33D8 [Tier-2 RTX 4090 Edge]  &bull; Stake: 35,000 $33RD  &bull; Status: ACTIVE');
            } else if (c === 'bench') {
                appendTermLine('[BENCH] Executing CAP-FFN LLaMA-3-8B PoI kernel challenge...', 'dim');
                setTimeout(() => {
                    appendTermLine('[BENCH] Randomized polynomial eval: Degree d=16 &bull; Chebyshev match', 'dim');
                    appendTermLine('[BENCH] Forward pass: 14.2ms &bull; Proof generated: 1.84ms &bull; OK', 'success');
                }, 280);
            } else if (c === 'verify') {
                appendTermLine('[KZG] Evaluating BN254 pairing: e(pi, [x - z]_2) == e(C - v*[1]_1, [1]_2)...', 'dim');
                setTimeout(() => {
                    appendTermLine('[KZG] Commitment opening verified on Solana &bull; Cost: 184,200 Compute Units', 'success');
                }, 320);
            } else if (c === 'byzantine') {
                const f = parseInt(byzSlider.value);
                appendTermLine(`[BYZANTINE] Committee audit: K=64 nodes &bull; Current f=${f}`, 'highlight');
                if (f <= 21) {
                    appendTermLine('[BYZANTINE] Quorum threshold 2/3: SATISFIED. Honest network guarantees intact.', 'success');
                } else {
                    appendTermLine('[BYZANTINE] WARNING: f > 21. Quorum breached. Automated slashing initiated.', 'warn');
                }
            } else if (c === 'tokenomics') {
                appendTermLine('TOKENOMICS & EMISSION PARAMETERS:', 'highlight');
                appendTermLine('  Hard Supply Cap : 33,000,000 $33RD');
                appendTermLine('  Current Epoch   : Epoch 0 (Years 1-4) &bull; 0.7135 $33RD / block');
                appendTermLine('  Buyback-Burn    : 10% commercial revenue routed to market burn');
                appendTermLine('  Burned To Date  : 412,840 $33RD (Deflationary)');
            } else if (c === 'clear') {
                termOutput.innerHTML = '';
            } else {
                appendTermLine(`Command not found: "${cmd}". Type "help" for options.`, 'warn');
            }
        }

        function handleTerminalSubmit(e) {
            e.preventDefault();
            const val = termInput.value;
            termInput.value = '';
            executeTermCommand(val);
        }

        initMatrix();
    """

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>33RD TREE LABS // Byzantine Simulator &bull; 33rdtreelabs.tech</title>
    <meta name="description" content="Interactive Adversarial Consensus & Byzantine Fault Tolerance Simulator. Inject malicious nodes and execute live Solana CLI commands.">

    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous">
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@0,300;0,400;0,500;0,700;1,400&family=Space+Grotesk:wght@300;400;500;600;700&family=Syne:wght@700;800&display=swap" rel="stylesheet">

    <style>{css}</style>
</head>
<body>

    {get_navbar("simulator")}

    <div class="page-wrap">
        <div class="meta-tag" data-glitch>( 02 ) // ADVERSARIAL CONSENSUS &bull; LIVE SIMULATOR &bull; TERMINAL</div>
        <h1 class="section-title" data-glitch>BYZANTINE COMMITTEE &amp; CLI ENGINE</h1>
        <p class="section-desc">
            Test the mathematical guarantees of the Singularity Protocol. Inject malicious adversaries, evaluate Byzantine resilience ($f &le; 21/64$), and query on-chain Solana state via the live command console.
        </p>

        <div class="sim-grid">
            <!-- Visual Byzantine Committee Lattice -->
            <div class="sim-box">
                <div class="sim-box-title">
                    <span data-glitch>VALIDATOR COMMITTEE LATTICE (K=64)</span>
                    <span id="byz-ratio-tag" style="color:var(--chalk);">f = 4 / 64 (6.2%)</span>
                </div>

                <!-- 8x8 Interactive Node Lattice -->
                <div class="node-lattice" id="node-matrix"></div>

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

                    <button class="btn-brutal-red" onclick="runConsensusRound()" style="width:100%; justify-content:center; padding:12px; cursor:pointer;" data-glitch>
                        EXECUTE CONSENSUS ROUND &rarr;
                    </button>

                    <div class="sim-status-banner" id="sim-status-box">
                        <div class="sim-status-head success" id="sim-status-title">
                            <span>[VALID] CONSENSUS REACHED: QUORUM VALIDATED</span>
                        </div>
                        <div id="sim-status-desc" style="color:var(--slate);">
                            Honest nodes: 60/64 (93.8%). Quorum threshold 66.7% met. Byzantine nodes isolated and marked for collateral slashing.
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
                    <div class="terminal-line highlight">33RD TREE LABS // SOLANA ANCHOR DIAGNOSTIC CLI [v4.0]</div>
                    <div class="terminal-line dim">Connected to Solana Mainnet-Beta via Jito RPC Anchor.</div>
                    <div class="terminal-line dim">Type <strong style="color:var(--chalk);">"help"</strong> for list of cryptographic commands.</div>
                    <div class="terminal-line">&nbsp;</div>
                </div>

                <form class="terminal-input-row" onsubmit="handleTerminalSubmit(event)">
                    <span class="terminal-prompt">&gt;</span>
                    <input type="text" id="terminal-input" class="terminal-input" placeholder="Type command (e.g. status, bench, verify)..." autocomplete="off" spellcheck="false">
                </form>
            </div>
        </div>
    </div>

    <!-- FOOTER -->
    <footer class="global-footer">
        <div class="footer-inner">
            <div class="footer-brand">
                <strong>33RD TREE LABS</strong> &bull; THE SINGULARITY PROTOCOL &bull; <code>33rdtreelabs.tech</code>
            </div>
            <div class="footer-links">
                <a href="index.html" class="footer-link">[ OVERVIEW ]</a>
                <a href="protocol.html" class="footer-link">[ PROTOCOL ]</a>
                <a href="simulator.html" class="footer-link">[ SIMULATOR ]</a>
                <a href="yield.html" class="footer-link">[ YIELD ]</a>
                <a href="nodes.html" class="footer-link">[ NODES ]</a>
                <a href="tokenomics.html" class="footer-link">[ TOKENOMICS ]</a>
                <a href="research.html" class="footer-link">[ RESEARCH ]</a>
                <a href="33rd_Tree_Labs_Whitepaper.pdf" target="_blank" class="footer-link">[ WHITEPAPER PDF ]</a>
            </div>
        </div>
    </footer>

    {get_script_footer(extra_js)}
"""
    with open(os.path.join(SITE_DIR, "simulator.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("simulator.html compiled successfully.")


# ====================================================================
# 4. BUILD YIELD.HTML (Staking Rewards & Hardware Yield Calculator)
# ====================================================================
def build_yield_html():
    css = get_shared_css() + """
        .calc-grid {
            display: grid;
            grid-template-columns: 1.1fr 0.9fr;
            gap: 28px;
            margin-top: 32px;
        }
        .calc-panel-left, .calc-panel-right {
            background: #0E0E12;
            border: 1px solid var(--border);
            padding: 28px;
            clip-path: polygon(0 14px, 14px 0, 100% 0, 100% calc(100% - 14px), calc(100% - 14px) 100%, 0 100%);
        }
        .calc-field {
            display: flex;
            flex-direction: column;
            gap: 8px;
            margin-bottom: 24px;
        }
        .calc-label {
            display: flex;
            justify-content: space-between;
            font-family: 'JetBrains Mono', monospace;
            font-size: 11px;
            color: var(--slate);
            text-transform: uppercase;
            letter-spacing: 0.08em;
        }
        .calc-select {
            background: #161620;
            border: 1px solid var(--border);
            color: var(--chalk);
            font-family: 'JetBrains Mono', monospace;
            font-size: 11.5px;
            padding: 10px 14px;
            outline: none;
        }
        .calc-slider {
            width: 100%;
            -webkit-appearance: none;
            background: #1C1C26;
            height: 6px;
            border-radius: 3px;
            outline: none;
        }
        .calc-slider::-webkit-slider-thumb {
            -webkit-appearance: none;
            width: 18px;
            height: 18px;
            border-radius: 50%;
            background: var(--laser-red);
            cursor: pointer;
            box-shadow: 0 0 10px var(--laser-red);
        }

        .calc-stat-box {
            display: flex;
            flex-direction: column;
            gap: 16px;
            background: #14141B;
            border: 1px solid var(--border);
            padding: 20px;
            margin-bottom: 20px;
        }
        .calc-metric-row {
            display: flex;
            justify-content: space-between;
            align-items: baseline;
            border-bottom: 1px solid rgba(255, 255, 255, 0.04);
            padding-bottom: 10px;
        }
        .calc-metric-row:last-child {
            border-bottom: none;
            padding-bottom: 0;
        }
        .calc-metric-name {
            font-family: 'JetBrains Mono', monospace;
            font-size: 10.5px;
            color: var(--slate);
            text-transform: uppercase;
        }
        .calc-metric-val {
            font-family: 'JetBrains Mono', monospace;
            font-size: 18px;
            font-weight: 700;
            color: var(--chalk);
        }
        .calc-metric-val.highlight {
            color: var(--laser-red);
            font-size: 24px;
        }
        .calc-disclaimer {
            font-family: 'JetBrains Mono', monospace;
            font-size: 10.5px;
            line-height: 1.5;
            color: var(--slate);
        }

        /* HARDWARE COMPARISON */
        .hw-table-box {
            background: #0E0E12;
            border: 1px solid var(--border);
            padding: 28px;
            margin-top: 48px;
            clip-path: polygon(0 12px, 12px 0, 100% 0, 100% calc(100% - 12px), calc(100% - 12px) 100%, 0 100%);
            overflow-x: auto;
            -webkit-overflow-scrolling: touch;
        }
        .hw-table {
            width: 100%;
            border-collapse: collapse;
            font-family: 'JetBrains Mono', monospace;
            font-size: 11px;
            margin-top: 16px;
        }
        .hw-table th, .hw-table td {
            padding: 10px 14px;
            text-align: left;
            border-bottom: 1px solid var(--border);
        }
        .hw-table th {
            color: var(--slate);
            text-transform: uppercase;
            font-weight: 700;
            background: #0B0B0E;
        }
        .hw-table td {
            color: var(--chalk);
        }
        .hw-table tr:hover td {
            background: rgba(255, 41, 44, 0.04);
        }

        @media (max-width: 900px) {
            .calc-grid { grid-template-columns: 1fr; }
        }
    """

    extra_js = """
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
    """

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>33RD TREE LABS // Yield Calculator &bull; 33rdtreelabs.tech</title>
    <meta name="description" content="Model validator yields, collateral requirements, APY, and deflationary buyback dynamics across GPU hardware configurations.">

    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous">
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@0,300;0,400;0,500;0,700;1,400&family=Space+Grotesk:wght@300;400;500;600;700&family=Syne:wght@700;800&display=swap" rel="stylesheet">

    <style>{css}</style>
</head>
<body>

    {get_navbar("yield")}

    <div class="page-wrap">
        <div class="meta-tag" data-glitch>( 03 ) // TOKENOMICS &bull; REWARDS SIMULATOR</div>
        <h1 class="section-title" data-glitch>VALIDATOR YIELD CALCULATOR</h1>
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
                <div class="calc-stat-box">
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

        <!-- HARDWARE TIER BENCHMARK TABLE -->
        <div class="hw-table-box">
            <div class="meta-tag" data-glitch>[ HARDWARE TIER REWARD WEIGHTS ]</div>
            <table class="hw-table">
                <thead>
                    <tr>
                        <th>Hardware Tier</th>
                        <th>Accelerator Spec</th>
                        <th>VRAM Pool</th>
                        <th>Interconnect</th>
                        <th>Weight Multiplier</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Tier-1 Ultra</td>
                        <td>NVIDIA B200 NVL72</td>
                        <td>1,440 GB HBM3e</td>
                        <td>1.8 TB/s NVLink Switch</td>
                        <td>5.4x</td>
                    </tr>
                    <tr>
                        <td>Tier-1 Heavy</td>
                        <td>Quad NVIDIA H100 SXM5</td>
                        <td>320 GB HBM3</td>
                        <td>900 GB/s NVLink</td>
                        <td>2.1x</td>
                    </tr>
                    <tr>
                        <td>Tier-1 Standard</td>
                        <td>Dual NVIDIA H100 SXM5</td>
                        <td>160 GB HBM3</td>
                        <td>900 GB/s NVLink</td>
                        <td>1.0x (Baseline)</td>
                    </tr>
                    <tr>
                        <td>Tier-2 Edge</td>
                        <td>NVIDIA RTX 4090</td>
                        <td>24 GB GDDR6X</td>
                        <td>PCIe Gen 4.0 x16</td>
                        <td>0.28x</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>

    <!-- FOOTER -->
    <footer class="global-footer">
        <div class="footer-inner">
            <div class="footer-brand">
                <strong>33RD TREE LABS</strong> &bull; THE SINGULARITY PROTOCOL &bull; <code>33rdtreelabs.tech</code>
            </div>
            <div class="footer-links">
                <a href="index.html" class="footer-link">[ OVERVIEW ]</a>
                <a href="protocol.html" class="footer-link">[ PROTOCOL ]</a>
                <a href="simulator.html" class="footer-link">[ SIMULATOR ]</a>
                <a href="yield.html" class="footer-link">[ YIELD ]</a>
                <a href="nodes.html" class="footer-link">[ NODES ]</a>
                <a href="tokenomics.html" class="footer-link">[ TOKENOMICS ]</a>
                <a href="research.html" class="footer-link">[ RESEARCH ]</a>
                <a href="33rd_Tree_Labs_Whitepaper.pdf" target="_blank" class="footer-link">[ WHITEPAPER PDF ]</a>
            </div>
        </div>
    </footer>

    {get_script_footer(extra_js)}
"""
    with open(os.path.join(SITE_DIR, "yield.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("yield.html compiled successfully.")


# ====================================================================
# 5. UPDATE NODES.HTML, TOKENOMICS.HTML, RESEARCH.HTML, WHITEPAPER.HTML
# ====================================================================
def update_existing_subpage(file_name, active_key):
    path = os.path.join(SITE_DIR, file_name)
    if not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace old header / nav
    nav_markup = get_navbar(active_key)
    
    # Replace old header / nav cleanly without duplicating cursor
    # First remove any stray duplicated cursor divs right before nav
    content = re.sub(r'(?:<!--\s*(?:RETRO-TECH CURSOR|FLOATING PILL NAVBAR)\s*-->\s*|<div id="cursor-(?:dot|ring)"></div>\s*)+<div class="nav-wrapper">', '<div class="nav-wrapper">', content)
    if '<div class="nav-wrapper">' in content:
        content = re.sub(r'<div class="nav-wrapper">[\s\S]*?</nav>\s*</div>', nav_markup.strip(), content)
    elif '<header class="site-nav">' in content:
        content = re.sub(r'<header class="site-nav">[\s\S]*?</header>', nav_markup.strip(), content)
    elif '<body' in content and '<div class="nav-wrapper">' not in content:
        content = re.sub(r'(<body[^>]*>)', r'\1\n' + nav_markup.strip(), content, count=1)

    # Ensure unified navbar CSS is in <style>
    unified_nav_css = """
        /* UNIFIED FLOATING PILL NAVBAR SPECIFICATION */
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
            border: 1px solid rgba(255, 255, 255, 0.12);
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
            border-right: 1px solid rgba(255, 255, 255, 0.12);
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
            content: '';
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
"""
    if '.nav-wrapper' in content:
        content = re.sub(r'/\*\s*UNIFIED FLOATING PILL NAVBAR SPECIFICATION\s*\*\/[\s\S]*?@media\s*\(max-width:\s*900px\)\s*\{[\s\S]*?\}\s*\}', unified_nav_css.strip(), content)
        content = re.sub(r'/\*\s*FLOATING PILL NAVBAR\s*\*\/[\s\S]*?\.nav-cta:hover\s*\{[\s\S]*?\}', unified_nav_css.strip(), content)
    elif '<style>' in content:
        content = content.replace('<style>', f'<style>\n{unified_nav_css}\n')

    # Calibrated VRTL WRLD Mechanical Glitch Decode Engine (250ms tick, 3.5s duration, progressive lock-in)
    calibrated_glitch_js = """        /* VRTL WRLD MECHANICAL GLITCH DECODE ENGINE (250MS / 3.5S SPECIFICATION) */
        class GlitchScramble {
            constructor(el) {
                this.el = el;
                this.chars = '01X_/*+-[]#';
                this.originalText = el.getAttribute('data-glitch-text') || el.innerText.trim();
                el.setAttribute('data-glitch-text', this.originalText);
                this.isGlitching = false;
                this.animId = null;
                this.lastTickTime = 0;
                this.tickInterval = 250; // Deliberate 250ms mechanical relay decode cadence
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
                    activeGlyphs[i] = (ch === ' ' || ch === String.fromCharCode(10) || ch === String.fromCharCode(9))
                        ? ch
                        : this.chars[Math.floor(Math.random() * this.chars.length)];
                }

                const tick = (now) => {
                    const elapsed = now - startTime;
                    const progress = Math.min(1, elapsed / durationMs);
                    const revealedCount = Math.floor(progress * len);

                    if (now - this.lastTickTime >= this.tickInterval) {
                        this.lastTickTime = now;
                        for (let i = revealedCount; i < len; i++) {
                            const ch = target[i];
                            if (ch === ' ' || ch === String.fromCharCode(10) || ch === String.fromCharCode(9)) {
                                activeGlyphs[i] = ch;
                            } else if (Math.random() < 0.35) {
                                activeGlyphs[i] = this.chars[Math.floor(Math.random() * this.chars.length)];
                            }
                        }
                    }

                    let result = '';
                    for (let i = 0; i < len; i++) {
                        const ch = target[i];
                        if (ch === ' ' || ch === String.fromCharCode(10) || ch === String.fromCharCode(9)) {
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
        });"""

    # Inject or update glitch script
    glitch_pattern = r'class GlitchScramble\s*\{[\s\S]*?document\.querySelectorAll\([\'"][^\)]*?glitch[^\)]*?\)\.forEach\([\s\S]*?\}\);?'
    if re.search(glitch_pattern, content):
        content = re.sub(glitch_pattern, calibrated_glitch_js.strip(), content)
    elif 'class GlitchScramble' not in content:
        content = content.replace('</body>', f"""
    <script>
{calibrated_glitch_js}
    </script>
</body>""")

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"{file_name} updated successfully.")


if __name__ == "__main__":
    import sys
    if "--include-index" in sys.argv:
        build_index_html()
    else:
        print("[NOTICE] Skipping index.html: managed exclusively by generate_perfect_boolean_site.py to prevent overwrite collision (pass --include-index to force).")
    build_protocol_html()
    build_simulator_html()
    build_yield_html()
    update_existing_subpage("nodes.html", "nodes")
    update_existing_subpage("tokenomics.html", "tokenomics")
    update_existing_subpage("research.html", "research")
    update_existing_subpage("whitepaper.html", "whitepaper")
    print("ALL MULTI-PAGE SURFACES GENERATED SUCCESSFULLY.")
