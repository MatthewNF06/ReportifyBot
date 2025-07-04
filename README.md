# 🤖 ReportifyBot

Bot do Discord para geração e resumo de relatórios de repositórios GitHub usando o Reportify e a API Gemini (Google AI).

---

## 📌 O que ele faz

- Gera relatórios automáticos com o Reportify ao usar o comando `!rpt`
- Lê os arquivos gerados (como `developer_stats_<nome_do_Dev>.md`)
- Usa a API Gemini para gerar resumos individualizados ao usar `!resumo`
- Também responde perguntas diretas com o comando `!g`

---

## ✅ Pré-requisitos

- Python 3.10 ou superior
- Ambiente Linux/WSL (o Reportify depende disso)
- Um bot do Discord configurado (com token)
- Chave da API Gemini (Google AI Studio)

---

## 🧪 Instalação

1. **Clone o repositório:**


git clone https://github.com/seu-usuario/ReportifyBot.git
cd ReportifyBot


2. Crie e ative um ambiente virtual (recomendado seguir a instalação e configuração no ambiente pela Lib do projeto):
https://pypi.org/project/reportify-ifes/

3. Instale as dependências(se necessario):
 pip install -r requirements.txt
 Se não tiver um requirements.txt, crie um com o seguinte conteúdo:
  discord.py
  python-dotenv
  requests

4. Gere um .env com a seguinte ordem de Montagem
  API's pro Reportify Funcionar:
   GITHUB_TOKEN=seu_token_github
   GITHUB_REPOSITORY=usuario/repositorio

  API's pro DiscordBot Funcionar:
   MY_API_REPORTFY=seu_token_do_bot_discord
   GEMINI_API_KEY=sua_chave_api_do_gemini

5. Links e Tutoriais adicionais
  Token do seu bot no Discord (crie em https://discord.com/developers).
  Chave da API Gemini (pegue em https://makersuite.google.com/app/apikey).
