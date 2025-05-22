#!/data/data/com.termux/files/usr/bin/bash

while true; do
    echo "[INFO] Verificando mudanças - $(date)" >> ~/nucleo_gestor/git_log.txt

    cd ~/nucleo_gestor || exit

    if [[ -n $(git status --porcelain) ]]; then
        echo "[INFO] Mudanças detectadas. Preparando para commit e push..." >> ~/nucleo_gestor/git_log.txt

        git add .
        git commit -m "Atualização automática em $(date '+%Y-%m-%d %H:%M:%S')"
        git push origin main

        echo "[SUCESSO] Atualização enviada para o GitHub." >> ~/nucleo_gestor/git_log.txt
    else
        echo "[INFO] Nenhuma mudança detectada." >> ~/nucleo_gestor/git_log.txt
    fi

    sleep 3600
done
