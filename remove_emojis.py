#!/usr/bin/env python3
import os, re

files = [
    "/Users/ianmora/Desktop/Projects/33rd-tree-labs-site/index.html",
    "/Users/ianmora/ai stuffs/333rd/site/index.html",
    "/Users/ianmora/.gemini/antigravity/brain/7181fab3-5a37-4ef0-b178-38c7996ef3ea/33rd_tree_labs_website.html",
    "/Users/ianmora/Desktop/33RD_TREE_LABS_3D/33rd_Tree_Labs_Website.html"
]

# Emojis in the cards: ⚡, 🛡️, 🌐, 🌀
replacements = {
    '<div class="card-icon">⚡</div>': '<div class="card-icon" style="font-size:12px; font-weight:800; font-family:JetBrains Mono, monospace; color:var(--orange);">POI</div>',
    '<div class="card-icon">🛡️</div>': '<div class="card-icon" style="font-size:11px; font-weight:800; font-family:JetBrains Mono, monospace; color:var(--orange);">ZK-TI</div>',
    '<div class="card-icon">🌐</div>': '<div class="card-icon" style="font-size:11px; font-weight:800; font-family:JetBrains Mono, monospace; color:var(--orange);">MESH</div>',
    '<div class="card-icon">🌀</div>': '<div class="card-icon" style="font-size:11px; font-weight:800; font-family:JetBrains Mono, monospace; color:var(--orange);">LEDGER</div>',
}

for path in files:
    if not os.path.exists(path): continue
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    for old, new in replacements.items():
        content = content.replace(old, new)
    
    # Also check for any remaining emojis
    emoji_pattern = re.compile(r'[\U00010000-\U0010ffff]|[\u2600-\u27ff]|[\u2300-\u23ff]', flags=re.UNICODE)
    content = emoji_pattern.sub('', content)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Stripped all emojis from:", path)

