from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import torch

# Nome do modelo Phi-3 Mini (versão para chat/instruções)
model_name = "microsoft/Phi-3-mini-4k-instruct"

print("Carregando tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir="./model_cache")

print("Carregando o modelo Phi-3 Mini (primeira vez: ~2.3GB, 5-15 min)...")
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
    device_map="auto",  # Usa GPU se disponível
    trust_remote_code=True,
    cache_dir="./model_cache"  # Salva localmente para reuso rápido
)

print("Configurando o gerador de respostas...")
generator = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=300,  # Tamanho máximo da resposta (aumente para mais detalhes)
    temperature=0.7,  # 0.1 para respostas factuais (estudos), 1.0 para criativo
    do_sample=True,
    pad_token_id=tokenizer.eos_token_id
)

# Histórico para conversas coerentes (personalização proprietária)
historico = []

def perguntar_phi(pergunta):
    # Inclui instrução personalizada: Foco em português e estudos
    prompt = f"<|system|>\nVocê é minha assistente IA proprietária, sempre responda em português, motivadora para estudos.\n"
    prompt += "\n".join(historico[-2:]) + f"\n<|user|>\n{pergunta}<|end|>\n<|assistant|>\n"  # Últimas 2 trocas
    resposta = generator(prompt)[0]["generated_text"]
    resposta_limpa = resposta.split("<|assistant|>\n")[-1].strip()
    
    # Adiciona ao histórico
    historico.append(f"<|user|>\n{pergunta}<|end|>\n<|assistant|>\n{resposta_limpa}")
    return resposta_limpa

print("\nSua IA proprietária Phi-3 Mini está pronta! Digite 'sair' para parar.")
print("Exemplo: 'Explique o teorema de Pitágoras com LaTeX em português.'\n")

# Loop de chat interativo
while True:
    user_input = input("Você: ")
    if user_input.lower() == 'sair':
        break
    resposta = perguntar_phi(user_input)
    print("Phi-3: " + resposta)
    print()  # Espaçamento
