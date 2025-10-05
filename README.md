# Minha IA Proprietária com Phi-3 Mini

Esta é minha assistente personalizada baseada no Phi-3 Mini da Microsoft (licença MIT). Focada em chat, estudos e explicações em português.

## Instalação
1. Clone o repo: `git clone https://github.com/guririu/MinhaIA_Phi3_Proprietaria.git`
2. Ative venv: `python3 -m venv phi3_env && source phi3_env/bin/activate`
3. Instale: `pip install -r requirements.txt`
4. Rode: `python3 phi3_chat.py`

## Recursos
- Chat interativo com histórico de conversa.
- Suporte a LaTeX para matemática (ex.: \$ \int x \, dx = \frac{x^2}{2} + C \$).
- Personalizada: Respostas motivadoras em PT-BR.

## Próximos Passos
- Fine-tuning: Adicione dataset em `dados_meus.json`.
- Licença: MIT (modificações são proprietárias minhas).

Baseado em: microsoft/Phi-3-mini-4k-instruct
