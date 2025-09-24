import os
import discord
from discord.ext import commands
import asyncio
from unittest.mock import patch
from pathlib import Path
import requests

# Import do Reportify
from reportify import Report

# Discord
TOKEN = os.getenv("MY_API_REPORTFY")
CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID"))
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Função para ler o último relatório gerado
def ler_ultimo_arquivo_md():
    reports_path = Path("./Reports")
    if not reports_path.exists() or not reports_path.is_dir():
        return None

    report_dirs = sorted(
        [p for p in reports_path.iterdir() if p.is_dir()],
        key=lambda p: p.stat().st_mtime,
        reverse=True
    )

    if not report_dirs:
        return None

    latest_dir = report_dirs[0]
    md_files = list(latest_dir.glob("developer_stats_*.md"))
    if not md_files:
        return None

    contents = []
    for md_file in md_files:
        try:
            with open(md_file, "r", encoding="utf-8") as f:
                contents.append(f"## {md_file.stem}\n\n{f.read()}\n")
        except Exception as e:
            print(f"Erro ao ler {md_file}: {e}")
    return "\n".join(contents) if contents else None

# Função para gerar resumo via Gemini API
def gerar_resposta_gemini(pergunta):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [{"parts":[{"text": pergunta}]}]
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        try:
            return response.json()['candidates'][0]['content']['parts'][0]['text']
        except Exception:
            return "⚠️ Não consegui entender a resposta da IA."
    else:
        print(response.text)
        return f"❌ Erro na API: {response.status_code}"

# Fluxo principal do bot
@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")
    print(f"Procurando canal ID: {CHANNEL_ID}")
    channel = bot.get_channel(CHANNEL_ID)
    try:
        await channel.send("🚀 Iniciando geração de relatório...")

        # === 1️⃣ Gera relatório ===
        def run_report():
            entradas = ['0', '']# '0' para todos, '' para sair
            with patch('builtins.input', side_effect=lambda _: entradas.pop(0) if entradas else ''):
                relatorio = Report()
                try:
                    relatorio.run()
                except SystemExit:  # Reportify chama exit() ao não haver seleção
                    print("⚠️ Nenhuma seleção feita, mas continuando para leitura do relatório...")
                except Exception as e:  # captura qualquer outro erro do run()
                    print(f"⚠️ Erro no Reportify.run(): {e}")
        
        await asyncio.to_thread(run_report)
        await channel.send("📊 Relatório gerado com sucesso!")

        # === 2️⃣ Lê os arquivos gerados ===
        markdown = ler_ultimo_arquivo_md()
        if not markdown:
            await channel.send("⚠️ Nenhum relatório encontrado.")
            await bot.close()
            return

        # === 3️⃣ Cria prompt para Gemini ===
        prompt = (
            "Você receberá estatísticas individuais de desenvolvedores de um projeto. "
            "Para cada desenvolvedor, gere um resumo separado (em Portugues-BR) contendo:\n"
            "- Prometido vs. Realizado (se disponível)\n"
            "- Throughput (quantas issues fechadas)\n"
            "- O nome dentro de uma [] no relatorio, para destacar\n"
            "- Quais issues ele abriu ou está responsável\n"
            "- Observações sobre atividade, papel no projeto ou padrão de contribuição\n\n"
            "Aqui estão os dados:\n\n" + markdown
        )

        await channel.send("📝 Gerando resumo com a IA Gemini...")
        resumo = gerar_resposta_gemini(prompt)

        # === 4️⃣ Envia resumo no Discord ===
        for i in range(0, len(resumo), 2000):  # divide em mensagens menores
            await channel.send(resumo[i:i+2000])

        await channel.send("✅ Processo completo: relatório + resumo enviado!")

    except Exception as e:
        await channel.send(f"❌ Erro durante execução: {e}")
    finally:
        await bot.close()

bot.run(TOKEN)









