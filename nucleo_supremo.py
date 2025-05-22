#!/data/data/com.termux/files/usr/bin/bash

# Script para iniciar Núcleo Supremo Inteligente - versão completa

echo "[INFO] Iniciando Núcleo Supremo Inteligente..."

# Verifica e instala dependências essenciais
pkg update -y && pkg upgrade -y
pkg install -y python espeak

# Arquivo Python único e autoexplicativo, cria se não existir
cat > ~/nucleo_gestor/nucleo_supremo.py << 'EOF'
import os
import sys
import time

MEMORIA = os.path.expanduser('~/nucleo_gestor/memoria.txt')

def falar(texto):
    os.system(f'espeak -v pt "{texto}"')

def carregar_memoria():
    if not os.path.exists(MEMORIA):
        return {}
    with open(MEMORIA, 'r', encoding='utf-8') as f:
        linhas = f.readlines()
    dados = {}
    for linha in linhas:
        if ':' in linha:
            chave, valor = linha.strip().split(':',1)
            dados[chave.lower()] = valor
    return dados

def salvar_memoria(dados):
    with open(MEMORIA, 'w', encoding='utf-8') as f:
        for k,v in dados.items():
            f.write(f"{k}:{v}\n")

def main():
    memoria = carregar_memoria()
    print("NÚCLEO SUPREMO ATIVO. Digite seu comando ou 'sair' para encerrar.")
    falar("Núcleo Supremo ativado. Estou pronto para ajudar, mestre Erick.")
    
    while True:
        try:
            comando = input(">> ").strip().lower()
            if comando == 'sair':
                falar("Encerrando sessão. Até logo, mestre.")
                print("Sessão encerrada.")
                break

            if comando == '':
                falar("Não entendi, por favor repita.")
                continue

            # Comando para ensinar nova resposta
            if comando.startswith('ensinar '):
                try:
                    pergunta_resposta = comando[8:].split('|')
                    if len(pergunta_resposta) != 2:
                        falar("Use o formato correto: ensinar pergunta | resposta")
                        continue
                    pergunta = pergunta_resposta[0].strip()
                    resposta = pergunta_resposta[1].strip()
                    memoria[pergunta.lower()] = resposta
                    salvar_memoria(memoria)
                    falar("Memória atualizada com sucesso.")
                    print("[Memória atualizada]")
                    continue
                except Exception as e:
                    falar("Erro ao ensinar nova resposta.")
                    print(f"Erro: {e}")
                    continue

            # Responder se souber
            if comando in memoria:
                resposta = memoria[comando]
                falar(resposta)
                print(resposta)
                continue

            # Respostas padrão
            if comando == 'ajuda':
                texto = ("Comandos disponíveis: sair, ajuda, ensinar pergunta | resposta. "
                         "Para ensinar algo novo, use: ensinar [pergunta] | [resposta]")
                falar(texto)
                print(texto)
                continue

            # Resposta padrão para desconhecido
            falar("Não sei a resposta para isso, mas vou aprender se você me ensinar.")
            print("Resposta desconhecida. Use 'ensinar pergunta | resposta' para me ensinar.")

        except KeyboardInterrupt:
            falar("Interrupção detectada. Estou aqui quando precisar, mestre.")
            print("\nSessão interrompida pelo usuário.")
            break
        except Exception as e:
            falar("Ocorreu um erro inesperado.")
            print(f"Erro: {e}")
            break

if __name__ == "__main__":
    main()
EOF

echo "[SUCESSO] Núcleo Supremo Inteligente instalado com sucesso."
echo "Para iniciar, execute: python ~/nucleo_gestor/nucleo_supremo.py"
