import pandas as pd

# Função para ler e processar o CSV
def process_csv(file_path: str):
    # Ler o arquivo CSV para um DataFrame
    df = pd.read_csv(file_path)

    # Verificar se as colunas 'transcript' e 'uuid' estão presentes
    if not {'transcript', 'uuid'}.issubset(df.columns):
        raise ValueError("CSV deve conter as colunas 'transcript' e 'uuid'.")

    # Exibir o DataFrame para verificar o conteúdo
    print("Conteúdo do DataFrame:")
    print(df)

    # Acessar dados específicos
    transcripts = df['transcript']
    uuids = df['uuid']

    # Exibir os dados das colunas
    print("\nTranscripts:")
    print(transcripts)

    print("\nUUIDs:")
    print(uuids)

    # Converter o DataFrame em um dicionário para uso posterior
    data_dict = df.to_dict(orient='records')
    return data_dict

# Exemplo de uso da função
if __name__ == "__main__":
    # Caminho para o arquivo CSV
    file_path = '/home/alysson/a.csv'
    
    # Processar o arquivo CSV
    data = process_csv(file_path)
    
    # Exibir o conteúdo do dicionário resultante
    print("\nDados convertidos em dicionário:")
    print(data)
