#!/bin/bash

# Inicie o serviço Ollama em segundo plano
/usr/bin/ollama start &

# Função para esperar que o serviço Ollama esteja disponível
wait_for_service() {
  local url="http://localhost:11434"
  local timeout=30
  local start_time=$(date +%s)

  while [[ $(($(date +%s) - start_time)) -lt timeout ]]; do
    if curl -s "$url" > /dev/null; then
      echo "Ollama está disponível."
      return 0
    fi
    echo "Esperando pelo Ollama..."
    sleep 5
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

# Baixar os modelos necessários
echo "Baixando modelos Ollama..."

# Esperar o serviço Ollama ficar disponível
wait_for_service

# Execute os comandos para baixar os modelos
# /usr/bin/ollama download llama3.1
# check_command_success $? "Falha ao baixar o modelo llama3.1"

# /usr/bin/ollama download nomic-embed-text
# check_command_success $? "Falha ao baixar o modelo nomic-embed-text"

# Alternativamente, você pode usar `ollama pull` se `download` não funcionar
/usr/bin/ollama pull llama3.1
#check_command_success $? "Falha ao puxar o modelo llama3.1"
/usr/bin/ollama pull nomic-embed-text
#check_command_success $? "Falha ao puxar o modelo nomic-embed-text"



# Aguardar um momento para garantir que o serviço esteja completamente iniciado
sleep 10

#echo "passou aqui"
#/usr/bin/ollama stop

# Executar o comando padrão do contêiner, se houver
#exec "$@"
