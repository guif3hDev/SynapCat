import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(".", intents=intents)

@bot.event
async def on_ready():
    print("Bot inicialiado com sucesso!")

@bot.event
async def on_message(msg:discord.message):
    if msg.author.bot:
        return
    await msg.reply(f"O usuário {msg.author.mention} enviou uma mensagem!")

@bot.event
async def on_member_join(membro:discord.Member):
    canal = bot.get_channel(1485411749980012574)
    await canal.send(f"{membro.mention} entrou no servidor!")

@bot.event
async def on_member_remove(membro):
    canal = bot.get_channel(1485416699615514726)
    await canal.send(f"{membro.mention} saiu do servidor!")

@bot.command()
async def ola(ctx: commands.Context):
    nome = ctx.author.name
    await ctx.reply(f"Olá, {nome}! Tudo bem?")

