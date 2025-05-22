#!/data/data/com.termux/files/usr/bin/bash

# Diretórios principais
BASE_DIR="$HOME/nucleo_gestor"
PROJETOS_DIR="$BASE_DIR/projetos"
BACKUP_DIR="$BASE_DIR/backup_nucleo"

# Criar pastas se não existirem
mkdir -p "$PROJETOS_DIR"
mkdir -p "$BACKUP_DIR"

# Função para salvar todos os projetos como backup
salvar_backup() {
    tar -czf "$BACKUP_DIR/projetos_backup.tar.gz" -C "$PROJETOS_DIR" .
    echo "[Backup] Projetos salvos em $BACKUP_DIR"
}

# Função para restaurar o backup
restaurar_backup_automatico() {
    if [ -f "$BACKUP_DIR/projetos_backup.tar.gz" ]; then
        tar -xzf "$BACKUP_DIR/projetos_backup.tar.gz" -C "$PROJETOS_DIR"
        echo "Backup restaurado com sucesso."
    else
        echo "Nenhum backup encontrado para restaurar."
    fi
}

# Menu do sistema (Controle do Núcleo)
controle_nucleo() {
    clear
    echo "=== CONTROLE DO NÚCLEO GESTOR ==="
    echo "1) Verificar integridade dos arquivos"
    echo "2) Restaurar backup agora"
    echo "3) Agendar backup diário"
    echo "4) Remover inicialização automática"
    echo "5) Atualizar script gestor.sh (em breve)"
    echo "6) Voltar"
    read -p "Escolha uma opção: " escolha

    case $escolha in
        1)
            echo "Verificando integridade..."
            [ -d "$PROJETOS_DIR" ] && echo "Projetos OK." || echo "FALHA: Pasta de projetos não encontrada."
            [ -f "$BACKUP_DIR/projetos_backup.tar.gz" ] && echo "Backup OK." || echo "FALHA: Nenhum backup encontrado."
            ;;
        2)
            restaurar_backup_automatico
            ;;
        3)
            pkg install cronie -y
            echo "0 9 * * * tar -czf $BACKUP_DIR/projetos_backup.tar.gz -C $PROJETOS_DIR ." > "$BASE_DIR/cronjob"
            crontab "$BASE_DIR/cronjob"
            crond
            echo "Backup agendado às 09:00 todos os dias."
            ;;
        4)
            sed -i '/gestor\.sh/d' ~/.bashrc
            echo "Inicialização automática removida."
            ;;
        5)
            echo "Função de atualização automática ainda não disponível."
            ;;
        6)
            return
            ;;
        *)
            echo "Opção inválida."
            ;;
    esac
}

# Função principal
menu_principal() {
    while true; do
        echo ""
        echo "=== Núcleo Gestor de Projetos ==="
        echo "1) Criar novo projeto"
        echo "2) Listar projetos"
        echo "3) Iniciar projeto"
        echo "4) Apagar projeto"
        echo "5) Fazer backup manual"
        echo "6) Restaurar backup"
        echo "7) Sair"
        echo "8) Sistema (Controle do Núcleo)"
        read -p "Escolha uma opção: " opcao

        case $opcao in
            1)
                read -p "Nome do novo projeto: " nome
                if [ -z "$nome" ]; then echo "Nome inválido."; continue; fi
                mkdir -p "$PROJETOS_DIR/$nome"
                echo "Projeto '$nome' criado em $PROJETOS_DIR/$nome"
                salvar_backup
                ;;
            2)
                echo "Projetos disponíveis:"
                ls "$PROJETOS_DIR"
                ;;
            3)
                echo "Projetos disponíveis:"
                ls "$PROJETOS_DIR"
                read -p "Digite o nome do projeto para iniciar (ou 'voltar'): " nome
                [ "$nome" == "voltar" ] && continue
                if [ -d "$PROJETOS_DIR/$nome" ]; then
                    echo "Iniciando projeto '$nome'..."
                    cd "$PROJETOS_DIR/$nome" || exit
                    bash
                    cd "$BASE_DIR"
                else
                    echo "Projeto '$nome' não encontrado."
                fi
                ;;
            4)
                echo "Projetos disponíveis:"
                ls "$PROJETOS_DIR"
                read -p "Digite o nome do projeto para apagar (ou 'voltar' para cancelar): " nome
                [ "$nome" == "voltar" ] && continue
                if [ -d "$PROJETOS_DIR/$nome" ]; then
                    read -p "Tem certeza que deseja apagar o projeto '$nome'? Esta ação é irreversível! (s/n): " confirmacao
                    if [ "$confirmacao" == "s" ]; then
                        rm -rf "$PROJETOS_DIR/$nome"
                        echo "Projeto '$nome' apagado com sucesso."
                        salvar_backup
                    else
                        echo "Ação cancelada."
                    fi
                else
                    echo "Projeto '$nome' não existe."
                fi
                ;;
            5)
                salvar_backup
                ;;
            6)
                restaurar_backup_automatico
                ;;
            7)
                echo "Encerrando Núcleo Gestor..."
                exit 0
                ;;
            8)
                controle_nucleo
                ;;
            *)
                echo "Opção inválida! Tente novamente."
                ;;
        esac
    done
}

# Execução
menu_principal
