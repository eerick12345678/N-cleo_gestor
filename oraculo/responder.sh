#!/data/data/com.termux/files/usr/bin/bash
while true; do
  echo ""
  read -p "[VOCÊ PERGUNTA] > " pergunta
  if [[ "$pergunta" == "sair" ]]; then break; fi
  resposta=$(grep -i "${pergunta:0:4}" memoria.txt | shuf -n1)
  [[ -z "$resposta" ]] && resposta="Não sei ainda... ensine-me."
  echo "[ORÁCULO RESPONDE] $resposta"
  bash fala.sh "$resposta"
done
