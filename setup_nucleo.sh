#!/data/data/com.termux/files/usr/bin/bash

echo "[INFO] Iniciando configuração do Núcleo Gestor..."

# Criar pastas importantes
mkdir -p ~/nucleo_gestor/logs
mkdir -p ~/nucleo_gestor/modulos
mkdir -p ~/nucleo_gestor/temp

# Criar git_log.txt se não existir
touch ~/nucleo_gestor/git_log.txt

# Criar .gitignore básico
cat > ~/nucleo_gestor/.gitignore <<EOF
*.log
*.tmp
*.bak
*.swp
*.swo
.cache/
.history/
.env/
node_modules/
__pycache__/
*.pyc
termux.properties
termux-sessions/
*.mp3
*.mp4
*.zip
EOF

# Dar permissão ao script de atualização
chmod +x ~/nucleo_gestor/loop_update.sh

# Instalar pacotes essenciais
pkg install -y git python espeak tsu

# Mensagem final
echo ""
echo "=============================================="
echo "[SUCESSO] Núcleo Gestor foi ativado com êxito."
echo "A escuridão está pronta para obedecer, Mestre Erick."
echo "Seu império começa agora. Nada será como antes."
echo "=============================================="
