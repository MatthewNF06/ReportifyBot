import discord
import os
import requests
import asyncio
from dotenv import load_dotenv
from unittest.mock import patch
from pathlib import Path
from datetime import datetime
import glob
# Supondo que sua classe Report esteja aqui mesmo no WSL
from reportify import Report  # ou from reportify.report import Report, se estiver em arquivo separado

load_dotenv()

API_TOKEN = os.getenv('MY_API_REPORTFY')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

intents = discord.Intents.default()
intents.message_content = True

# Caminho da pasta base do seu projeto, ajuste se precisar
BASE_PATH = os.path.join(os.getcwd(), "Reports")  # ./Reports

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def send_long_message(self, channel, message):
        for i in range(0, len(message), 2000):
            await channel.send(message[i:i+2000])

    async def on_message(self, message):
        if message.author == self.user:
            return

        print(f'Message from {message.author}: {message.content}')

        if message.content.startswith('!g'):
            pergunta = message.content.removeprefix('!g').strip()
            if pergunta == '':
                await message.channel.send('❌ Você precisa fazer uma pergunta. Ex: `!g explique IA`')
                return

            await message.channel.send('🤖 Processando sua pergunta com a IA...')
            try:
                resposta = gerar_resposta_gemini(pergunta)
                await self.send_long_message(message.channel, resposta)
            except Exception as e:
                print(e)
                await message.channel.send('❌ Ocorreu um erro ao processar sua pergunta.')

        elif message.content.startswith('!rpt'):
            await message.channel.send("⏳ Gerando relatório, aguarde...")
            try:
                entradas = ['0', '']  # '0' para todos, '' para sair
                def run_report():
                    with patch('builtins.input', side_effect=lambda _: entradas.pop(0) if entradas else ''):
                        relatorio = Report()
                        relatorio.run()

                await asyncio.to_thread(run_report)
            except Exception as e:
                print(e)
                await message.channel.send('Relatorio Gerado com sucesso! e Prompt de comando reiniciada!')

        elif message.content.startswith('!resumo'):
            try:
                markdown = ler_ultimo_arquivo_md()
                if not markdown:
                    await message.channel.send("⚠️ Nenhum relatório encontrado.")
                    return

                await message.channel.send("📄 Gerando resumo com a IA...")
                resposta = gerar_resposta_gemini(
                    "Você receberá estatísticas individuais de desenvolvedores de um projeto. "
                    "Para cada desenvolvedor, gere um resumo separado (em Portugues-BR) contendo:\n"
                    "- Prometido vs. Realizado (se disponível)\n"
                    "- Throughput (quantas issues fechadas)\n"
                    "- O nome dentro de uma [] no relatorio, para destacar\n"
                    "- Quais issues ele abriu ou está responsável\n"
                    "- Observações sobre atividade, papel no projeto ou padrão de contribuição\n\n"
                    "Aqui estão os dados:\n\n" + markdown
                )
                await self.send_long_message(message.channel, resposta)
                await message.channel.send("RESUMO GERADO! 📄🤖")
            except Exception as e:
                await message.channel.send(f"❌ Erro ao gerar resumo: {e}")


# Função para encontrar a pasta mais recente na pasta Reports
def ler_ultimo_arquivo_md():
    reports_path = Path("./Reports")
    if not reports_path.exists() or not reports_path.is_dir():
        return None

    # Ordena as pastas pela última modificação (mais recente primeiro)
    report_dirs = sorted(
        [p for p in reports_path.iterdir() if p.is_dir()],
        key=lambda p: p.stat().st_mtime,
        reverse=True
    )

    if not report_dirs:
        return None

    latest_dir = report_dirs[0]

    # Encontra todos os arquivos terminados com _stats.md
    md_files = list(latest_dir.glob("developer_stats_*.md"))
    if not md_files:
        return None

    # Lê e junta todos os arquivos encontrados
    contents = []
    for md_file in md_files:
        try:
            with open(md_file, "r", encoding="utf-8") as f:
                contents.append(f"## {md_file.stem}\n\n{f.read()}\n")

        except Exception as e:
            print(f"Erro ao ler {md_file}: {e}")

    return "\n".join(contents) if contents else None
# 🔥 Função para conversar com o Gemini via API REST
def gerar_resposta_gemini(pergunta):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": pergunta
                    }
                ]
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        resposta = response.json()
        try:
            texto = resposta['candidates'][0]['content']['parts'][0]['text']
            return texto
        
        except Exception:
            return '⚠️ Não consegui entender a resposta da IA.'
    else:
        print(response.text)
        return f'❌ Erro na API: {response.status_code}'

client = MyClient(intents=intents)
client.run(API_TOKEN)
