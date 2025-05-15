#!/bin/bash
if [[ -n $(git status -s) ]]; then
  echo "[INFO] Mudanças detectadas. Preparando para commit e push..."
  git add .
  git commit -m "Atualização automática em $(date '+%Y-%m-%d %H:%M:%S')"
  git push origin main
  echo "[SUCESSO] Atualização enviada para o GitHub."
else
  echo "[INFO] Nenhuma mudança detectada. Nada a enviar."
fi
