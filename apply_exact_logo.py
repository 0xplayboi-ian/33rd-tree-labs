#!/usr/bin/env python3
import os

with open("/Users/ianmora/Desktop/Projects/33rd-tree-labs-site/logo_mark.svg", "r") as f:
    exact_svg = f.read().strip()

destinations = [
    "/Users/ianmora/Desktop/Projects/33rd-tree-labs-site/index.html",
    "/Users/ianmora/ai stuffs/333rd/site/index.html",
    "/Users/ianmora/.gemini/antigravity/brain/7181fab3-5a37-4ef0-b178-38c7996ef3ea/33rd_tree_labs_website.html",
    "/Users/ianmora/Desktop/33RD_TREE_LABS_3D/33rd_Tree_Labs_Website.html"
]

for d in destinations:
    if not os.path.exists(d): continue
    with open(d, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace the old placeholder SVG inside .logo-symbol
    # Old SVG: <svg viewBox="0 0 24 24" fill="none" stroke-width="1.8">...
    import re
    # Match any <svg viewBox="0 0 24 24" ... </svg> inside logo-symbol
    new_content = re.sub(
        r'<div class="logo-symbol">\s*<svg[^>]*>.*?</svg>\s*</div>',
        f'<div class="logo-symbol" style="width:44px; height:44px; padding:3px; background:radial-gradient(circle, rgba(255,69,0,0.22), #000); border:1px solid #FF4500; box-shadow:0 0 16px rgba(255,69,0,0.5);">{exact_svg}</div>',
        content,
        flags=re.DOTALL
    )
    
    # Also ensure brand-text has 33RD TREE LABS with TREE in bold and proper sizing
    new_content = new_content.replace(
        '<span class="brand-name">33RD TREE LABS</span>',
        '<span class="brand-name" style="letter-spacing:1px; white-space:nowrap;">33RD TREE LABS</span>'
    )
    
    with open(d, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Updated logo in:", d)

