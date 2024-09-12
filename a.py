from transformers import LLaMAForCausalLM, LLaMATokenizer

# Carregar o tokenizador e o modelo
tokenizer = LLaMATokenizer.from_pretrained('meta/llama-3.1')
model = LLaMAForCausalLM.from_pretrained('meta/llama-3.1')

# Texto de entrada
input_text = "Qual é a capital da França?"

# Tokenizar e gerar resposta
inputs = tokenizer(input_text, return_tensors='pt')
outputs = model.generate(inputs['input_ids'])

# Decodificar a resposta
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(response)
