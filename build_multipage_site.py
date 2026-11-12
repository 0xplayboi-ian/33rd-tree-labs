#!/usr/bin/env python3
"""
33rd Tree Labs - Multi-Page Generator Script
Aesthetic: VRTL WRLD Industrial Brutalism & Retro-Futurism
Hard constraints:
- Zero emojis
- Matrix glitch letters animation on hover, load, and scroll
- Fixed Hero Tensor Arbor schematic cut-off at 100% zoom
- Dedicated pages for Protocol, Simulator, Yield, Nodes, Tokenomics, Research, Whitepaper
"""

import os
import re

SITE_DIR = "/Users/ianmora/Desktop/Projects/33rd-tree-labs-site"

def get_base_css():
    return """
        :root {
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

        /* FLOATING PILL NAVBAR */
        .nav-wrapper {
            position: fixed;
            top: 18px;
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
            gap: 16px;
            background: rgba(11, 11, 14, 0.94);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid var(--border);
            padding: 8px 16px;
            border-radius: 9999px;
            box-shadow: 0 14px 34px rgba(0, 0, 0, 0.7), 0 0 0 1px rgba(255, 255, 255, 0.05);
            transition: border-color 0.25s ease, box-shadow 0.25s ease;
            max-width: 98vw;
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
            flex-shrink: 0;
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
            gap: 10px;
        }
        .nav-link {
            font-family: 'JetBrains Mono', monospace;
            font-size: 10.5px;
            font-weight: 500;
            letter-spacing: 0.06em;
            color: var(--slate);
            text-decoration: none;
            transition: color 0.2s ease, text-shadow 0.2s ease;
            position: relative;
            padding: 4px 4px;
            white-space: nowrap;
        }
        .nav-link:hover, .nav-link.active {
            color: var(--white);
        }
        .nav-link.active {
            color: var(--laser-red);
            font-weight: 700;
            text-shadow: 0 0 10px rgba(255, 41, 44, 0.5);
        }

        .nav-status {
            display: flex;
            align-items: center;
            gap: 7px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 10px;
            letter-spacing: 0.08em;
            color: var(--green);
            padding: 4px 10px;
            background: rgba(0, 230, 118, 0.06);
            border: 1px solid rgba(0, 230, 118, 0.2);
            border-radius: 9999px;
            white-space: nowrap;
        }
        .nav-status-dot {
            width: 6px;
            height: 6px;
            background: var(--green);
            border-radius: 50%;
            box-shadow: 0 0 8px var(--green);
            animation: pulse-dot 1.8s infinite;
        }
        @keyframes pulse-dot {
            0%, 100% { opacity: 1; transform: scale(1); }
            50% { opacity: 0.4; transform: scale(0.85); }
        }

        .nav-cta {
            font-family: 'JetBrains Mono', monospace;
            font-size: 10.5px;
            font-weight: 700;
            letter-spacing: 0.08em;
            color: var(--white);
            background: var(--laser-red);
            text-decoration: none;
            padding: 6px 14px;
            border-radius: 9999px;
            transition: background 0.2s ease, box-shadow 0.2s ease, transform 0.15s ease;
            white-space: nowrap;
            box-shadow: 0 0 14px rgba(255, 41, 44, 0.35);
        }
        .nav-cta:hover {
            background: #FF474A;
            box-shadow: 0 0 22px rgba(255, 41, 44, 0.65);
            transform: translateY(-1px);
        }

        /* VRTL WRLD GLITCH TEXT & CHROMATIC ABERRATION */
        .glitch-active {
            color: var(--laser-red) !important;
            text-shadow: 1.5px 0 0 rgba(255, 41, 44, 0.85), -1.5px 0 0 rgba(0, 230, 118, 0.75) !important;
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
            font-size: clamp(28px, 4.2vw, 48px);
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
            max-width: 680px;
            font-weight: 400;
            margin-bottom: 36px;
        }

        /* PAGE CONTAINER */
        .page-wrap {
            padding-top: 110px;
            padding-bottom: 80px;
            max-width: 1360px;
            margin: 0 auto;
            padding-left: 24px;
            padding-right: 24px;
        }

        /* FOOTER */
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
            font-size: 12px;
            color: var(--slate);
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
            font-family: 'JetBrains Mono', monospace;
            font-size: 10.5px;
            color: var(--slate);
            text-decoration: none;
            transition: color 0.2s;
        }
        .footer-link:hover {
            color: var(--laser-red);
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
    <!-- RETRO-TECH CURSOR -->
    <div id="cursor-dot"></div>
    <div id="cursor-ring"></div>

    <!-- FLOATING PILL NAVBAR -->
    <div class="nav-wrapper">
        <nav class="nav-pill">
            <a href="index.html" class="nav-brand">
                <div class="nav-logo-box">
                    <img src="assets/nav_logo.png" alt="33rd Tree Labs Wireframe">
                </div>
                <span class="nav-title" data-glitch>33RD TREE LABS</span>
            </a>

            <div class="nav-links">
                {links_html}
            </div>

            <div class="nav-status">
                <span class="nav-status-dot"></span>
                <span>MAINNET CANARY</span>
            </div>

            <a href="nodes.html" class="nav-cta" data-glitch>[ DEPLOY GPU ]</a>
        </nav>
    </div>
"""

def get_script_footer():
    return """
    <!-- Lenis & GSAP -->
    <script src="https://cdn.jsdelivr.net/npm/@studio-freight/lenis@1.0.42/dist/lenis.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>

    <script>
        gsap.registerPlugin(ScrollTrigger);
        const lenis = new Lenis({ duration: 1.1, smoothWheel: true });
        lenis.on('scroll', ScrollTrigger.update);
        gsap.ticker.add((time) => lenis.raf(time * 1000));
        gsap.ticker.lagSmoothing(0);

        // Custom Cursor
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

        // VRTL WRLD Authentic Glitch Letters Scramble Engine
        class GlitchScramble {
            constructor(el) {
                this.el = el;
                this.chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_/[#]=+*?<>~!$%&';
                this.originalText = el.getAttribute('data-glitch-text') || el.innerText.trim();
                el.setAttribute('data-glitch-text', this.originalText);
                this.isGlitching = false;
                this.animId = null;
            }

            scramble(duration = 0.5) {
                if (this.isGlitching) return;
                this.isGlitching = true;
                this.el.classList.add('glitch-active');
                const target = this.originalText;
                const len = target.length;
                const startTime = performance.now();
                const durationMs = duration * 1000;

                const tick = (now) => {
                    const elapsed = now - startTime;
                    const progress = Math.min(1, elapsed / durationMs);
                    const revealedCount = Math.floor(progress * len);

                    let result = '';
                    for (let i = 0; i < len; i++) {
                        const ch = target[i];
                        if (ch === ' ' || ch === '\\n' || ch === '\\t') {
                            result += ch;
                        } else if (i < revealedCount) {
                            result += ch;
                        } else if (i < revealedCount + 3) {
                            result += this.chars[Math.floor(Math.random() * this.chars.length)];
                        } else {
                            result += this.chars[Math.floor(Math.random() * this.chars.length)];
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

        document.querySelectorAll('[data-glitch]').forEach(el => {
            const inst = new GlitchScramble(el);
            el.addEventListener('mouseenter', () => inst.scramble(0.45));
        });

        window.addEventListener('DOMContentLoaded', () => {
            let delay = 80;
            document.querySelectorAll('.display-word, .meta-tag, .glitch-load').forEach(el => {
                const inst = new GlitchScramble(el);
                setTimeout(() => inst.scramble(0.7), delay);
                delay += 110;
            });
        });

        document.querySelectorAll('.section-title').forEach(el => {
            const inst = new GlitchScramble(el);
            ScrollTrigger.create({
                trigger: el,
                start: 'top 88%',
                onEnter: () => inst.scramble(0.6),
                onEnterBack: () => inst.scramble(0.45)
            });
            el.addEventListener('mouseenter', () => inst.scramble(0.45));
        });
    </script>
</body>
</html>
"""

print("Base setup ready.")
