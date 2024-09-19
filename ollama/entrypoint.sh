#!/bin/bash

set -e  # Faz o script falhar em caso de erro

# Configurações
OLLAMA_URL="http://localhost:11434"
TIMEOUT=30
CHECK_INTERVAL=5

# Função para esperar que o serviço Ollama esteja disponível
wait_for_service() {
  local start_time=$(date +%s)

  while [[ $(($(date +%s) - start_time)) -lt TIMEOUT ]]; do
    if curl -s "$OLLAMA_URL" > /dev/null; then
      echo "Ollama está disponível."
      return 0
    fi
    echo "Esperando pelo Ollama..."
    sleep $CHECK_INTERVAL
  done

  echo "Tempo limite para conectar ao Ollama excedido."
  exit 1
}

# Função para verificar o sucesso dos comandos
check_command_success() {
  local exit_code=$1
  local message=$2
  if [[ $exit_code -ne 0 ]]; then
    echo "Erro: $message. Código de saída: $exit_code"
    exit $exit_code
  fi
}

# Verificar se o Ollama está instalado
if ! command -v /usr/bin/ollama &> /dev/null; then
  echo "Ollama não está instalado. Saindo."
  exit 1
fi

# Iniciar o serviço Ollama em segundo plano
/usr/bin/ollama start &

# Baixar os modelos necessários
echo "Baixando modelos Ollama..."
wait_for_service

# Array de modelos a serem baixados
declare -a models=("llama3.1" "nomic-embed-text")

for model in "${models[@]}"; do
  echo "Puxando o modelo $model..."
  /usr/bin/ollama pull "$model"
  check_command_success $? "Falha ao puxar o modelo $model"
done

# Aguardar um momento para garantir que o serviço esteja completamente iniciado
sleep 10

# Capturar SIGTERM para encerrar o serviço corretamente
trap 'echo "Encerrando..."; /usr/bin/ollama stop; exit' SIGTERM

# Manter o script em execução
wait

# Executar o comando padrão do contêiner, se houver
exec "$@"
