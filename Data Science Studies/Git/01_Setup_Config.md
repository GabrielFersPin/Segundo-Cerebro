# 🔵 Setup & Configuración

## Inicializar
```bash
git init                 # Nuevo repo
git clone <url>          # Clonar existente
```

## Configurar Identidad
```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"
```

## Configurar Herramientas
```bash
git config --global core.editor "code --wait"
git config --global core.editor "vim"
```

## Ver Configuración
```bash
git config --list        # Toda la config
git config user.name     # Config específica
```

## Remotos
```bash
git remote add origin <url>
git remote -v            # Ver remotos
git remote set-url origin <nueva-url>
```

---

**Usar**: Primera vez con repo  
**Frecuencia**: Una vez por proyecto/máquina
