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
    await msg.reply(f"Miaauu! O usuário {msg.author.mention} enviou uma mensagem!")
    await bot.process_commands(msg)

@bot.event
async def on_member_join(membro:discord.Member):
    canal = bot.get_channel(1485411749980012574)
    await canal.send(f"Miaaau... {membro.mention} entrou no servidor!")

    role_id = 1485975376978247811
    role = membro.guild.get_role(role_id)
    if role is None:
        print("cargo não encontrado")
        return
    
    try:
        await membro.add_roles(role)
        print(f"Miaaau! Cargo adicionado para {membro.name}")
    except discord.Forbidden:
        print("Miauu... Não tenho permissão para adicionar cargos.")
    except Exception as e:
        print(f"erro: {e}")

@bot.event
async def on_member_remove(membro):
    canal = bot.get_channel(1485416699615514726)
    await canal.send(f"Miaauu! {membro.mention} saiu do servidor!")

@bot.command()
async def ola(ctx: commands.Context):
    nome = ctx.author.name
    await ctx.reply(f"Miaauu! Olá, {nome}! Tudo bem?")