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

## 1. **Clone o repositório:**

- git clone https://github.com/MatthewNF06/ReportifyBot.git
- cd ReportifyBot

## 2. Crie e ative um ambiente virtual para Rodar o BOT (recomendado seguir a instalação e configuração no ambiente pela Lib do projeto):
https://pypi.org/project/reportify-ifes/
Execute o bot no terminal do ambiente do projeto (o nome é de exemplo, altere o nome do arquivo conforme a aplicação):
 python DiscordBot.py


## 3. Instale as dependências(se necessario):
 - pip install -r requirements.txt
 Se não tiver um requirements.txt, crie um com o seguinte conteúdo:
  - discord.py
  - python-dotenv
  - requests

## 4. Gere um .env com a seguinte ordem de Montagem
  API's pro Reportify Funcionar:
   - GITHUB_TOKEN=seu_token_github
   - GITHUB_REPOSITORY=usuario/repositorio

  API's pro DiscordBot Funcionar:
   - MY_API_REPORTFY=seu_token_do_bot_discord
   - GEMINI_API_KEY=sua_chave_api_do_gemini

## 5. Links e Tutoriais adicionais
  - Token do seu bot no Discord (crie em https://discord.com/developers).
  - Chave da API Gemini (pegue em https://makersuite.google.com/app/apikey).

---
# COMO FUNCIONA?
Quando o Bot iniciar (rodando localmente)
 - Ao executar o bot, ele leva alguns segundos para ser inicializado, se tudo correr bem com a instalação e configuração, ele ficará online e totalmente operacional, basta configurar um chat para ele, e ao digitar !rpt, ele vai conferir todas as permissões e tokens do .env e fará a busca, dependendo do repositório que for, pode levar cerca de 2 a 7minutos, e após isso, ele emitirá uma mensagem de que o relatorio foi feito (atravaes de uma captura de exceção que finaliza a busca ao encontrar todas as issues)
 
 - Ao terminar de gerar os relatorios, basta digitar !resumo para que ele faça os resumos de cada Dev que reportou/fez/abriu/fechou as issues.
 
 - ***Extra:*** !g fucniona como uma I.A propria do gemini, para agilizar ou funções basicas da IA no proprio discord, mais para praticidade e agilidade.
