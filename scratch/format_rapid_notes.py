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
    
    # Identificar si es una captura rápida (por el campo procesamiento, tipo_nota o etiqueta)
    is_rapid = "CAPTURA-RAPIDA" in frontmatter or "captura_rapida" in frontmatter or "#captura-rapida" in body
    if not is_rapid:
        return

    lines = frontmatter.split('\n')
    fm_dict = {}
    for line in lines:
        if ':' in line:
            k, v = line.split(':', 1)
            fm_dict[k.strip()] = v.strip()
            
    # Ajustes clave para notas por estudiar
    fm_dict['tipo_nota'] = fm_dict.get('tipo_nota', 'captura_rapida').strip('"\' ')
    fm_dict['status'] = '🔴 Por procesar'
    
    # Forzamos nivel de comprensión a ❓ para que destaque en los dashboards
    val_nivel = fm_dict.get('nivel-comprension', '').strip('"\' ')
    if not val_nivel or val_nivel == '':
        fm_dict['nivel-comprension'] = '"❓"'
        
    if 'asignatura' in fm_dict and not fm_dict.get('area'):
        fm_dict['area'] = fm_dict['asignatura']
        
    # Limpiamos campos obsoletos
    for k in ['fecha-examen', 'tiempo-estimado', 'asignatura']:
        fm_dict.pop(k, None)
        
    # Orden unificado
    unified_keys = [
        'created', 'modified', 'area', 'tipo_nota', 'status', 
        'nivel-comprension', 'proxima-revision', 'ultima-revision', 
        'veces-revisado', 'tiempo-repaso', 'cards-deck',
        'procesamiento', 'prioridad', 'tipo-captura', 'complejidad', 
        'origen', 'urgente'
    ]
    
    new_fm_lines = []
    
    for k in unified_keys:
        if k in fm_dict:
            new_fm_lines.append(f"{k}: {fm_dict[k]}")
        else:
            if k in ['area', 'proxima-revision', 'ultima-revision', 'tiempo-repaso', 'cards-deck']:
                new_fm_lines.append(f'{k}: ""')
            elif k == 'veces-revisado':
                new_fm_lines.append(f'{k}: 0')
                
    # Otros campos que tuviera
    for k, v in fm_dict.items():
        if k not in unified_keys:
            new_fm_lines.append(f"{k}: {v}")
            
    new_frontmatter = "\n".join(new_fm_lines)
    
    if new_frontmatter != frontmatter:
        new_content = f"---\n{new_frontmatter}\n---{body}"
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Reformulada: {filepath}")

for root, dirs, files in os.walk(root_dir):
    dirs[:] = [d for d in dirs if d not in ignore_dirs]
    for file in files:
        if file.endswith('.md'):
            process_file(os.path.join(root, file))
