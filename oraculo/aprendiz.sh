#!/data/data/com.termux/files/usr/bin/bash
echo "[ORÁCULO] Digite algo para o Oráculo aprender:"
while true; do
  read -p "> " entrada
  if [[ "$entrada" == "sair" ]]; then break; fi
  echo "$entrada" >> memoria.txt
  echo "[MEMÓRIA] Aprendido e salvo."
done
