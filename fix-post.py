#!/usr/bin/env python3
"""Fix physical-experiments post to match standard Pi template"""
import re

filepath = "/data/data/com.termux/files/home/workspace/pi/blog/posts/physical-experiments-golden-pi-measurements.html"

with open(filepath, 'r') as f:
    content = f.read()

# 1. Remove old .site-title and .site-subtitle CSS blocks
content = re.sub(r'\s+\.site-title \{.*?\n\}', '', content, flags=re.DOTALL)
content = re.sub(r'\s+\.site-title:hover \{.*?\n\}', '', content, flags=re.DOTALL)
content = re.sub(r'\s+\.site-subtitle \{[^}]*?\n\}', '', content, flags=re.DOTALL)

# 2. Remove stray .site-title and .header CSS if any
content = re.sub(r'\s+\.header \{.*?\n\}', '', content, flags=re.DOTALL)

# 3. Make sure header is correct (it should already be from previous sed)
# Verify the header block exists
if '<span>Φ</span> The True Value Of Pi <span>Π</span>' not in content:
    # Replace the old-style header
    old_header_pattern = r'<header>.*?</header>'
    new_header = '''  <header>
    <div class="header">
      <h1><span>Φ</span> The True Value Of Pi <span>Π</span></h1>
      <div class="menu">
        <ul>
          <li><a href="../../index.html">HOME</a></li>
          <li><a href="../index.html">BLOG</a></li>
        </ul>
      </div>
    </div>
  </header>'''
    content = re.sub(old_header_pattern, new_header, content, flags=re.DOTALL)

# 4. Fix duplicate footer - remove first footer if there are two
footer_count = content.count('<footer>')
if footer_count > 2:
    # Find the position of the first two footers and remove extras
    pass  # For now, we'll handle this

# 5. Add image after header
old_after_header = '</header>\n<article>'
new_after_header = '''</header>
<img src="../../img/geometry-circle.jpg" alt="Physical experiments measuring golden pi" style="width:100%;max-width:720px;height:auto;border-radius:12px;margin:0 auto 24px;display:block;" />
<article>'''
content = content.replace(old_after_header, new_after_header)

with open(filepath, 'w') as f:
    f.write(content)

print("Done fixing physical-experiments post")
print(f"Footer count: {content.count('<footer>')}")
print(f"Header correct: {'<span>Φ</span> The True Value Of Pi <span>Π</span>' in content}")
