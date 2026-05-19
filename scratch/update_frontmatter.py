import os
import re

root_dir = "/home/gabriel/Documents/Segundo_Cerebro"
ignore_dirs = {".git", ".obsidian", ".trash", "Templates", "scratch"}

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    match = re.match(r'^---\n(.*?)\n---(.*)', content, re.DOTALL)
    if not match:
        return
        
    frontmatter = match.group(1)
    body = match.group(2)
    
    # Rename asignatura to area
    frontmatter = re.sub(r'^asignatura:', 'area:', frontmatter, flags=re.MULTILINE)
    
    keys_to_ensure = [
        ('nivel-comprension', '""'),
        ('proxima-revision', '""'),
        ('ultima-revision', '""'),
        ('veces-revisado', '0'),
        ('tiempo-repaso', '""'),
        ('cards-deck', '""')
    ]
    
    new_frontmatter = frontmatter
    modified = False
    
    if frontmatter != match.group(1):
        modified = True
        
    for key, default_val in keys_to_ensure:
        if not re.search(rf'^{key}:', new_frontmatter, flags=re.MULTILINE):
            new_frontmatter += f"\n{key}: {default_val}"
            modified = True
            
    if modified:
        new_content = f"---\n{new_frontmatter}\n---{body}"
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")

for root, dirs, files in os.walk(root_dir):
    dirs[:] = [d for d in dirs if d not in ignore_dirs]
    for file in files:
        if file.endswith('.md'):
            process_file(os.path.join(root, file))
