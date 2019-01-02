import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio



bot = commands.Bot(command_prefix='l!')
print (discord.__version__)





@bot.event
async def on_ready():
    print ("Ready when you are xd")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: ping!! xSSS")
    print ("user has pinged")



@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here's what I could find.", color=0x00ff00)
    embed.set_author(name="BY:彡★ｲЩ乃★彡 Brahma#1111")
    embed.add_field(name="Nome do servidor", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID do servidor", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Total de roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Quantidade de Membros", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
@commands.has_role("ðŸ˜‚ðŸ‘Œ Friends")
async def kick(ctx, user: discord.Member):
    await bot.say(":boot: Cya, {}. Ya loser!".format(user.name))
    await bot.kick(user)

@bot.command(pass_context=True)
async def ajuda(ctx):
    embed = discord.Embed(title="The World Of Bad 2.0 Bot", description="Meu comandos são", color=0x00ff00)
    embed.set_footer(text="Bot Oficial do servidor da guilda LEGEND•SQUAD")
    embed.set_author(name="Fui criado pelo 彡★ｲЩ乃★彡 Brahma#1111")
    embed.add_field(name="ban", value="bane o usuário", inline=True)
    embed.add_field(name="kick", value="expulsa o usuário", inline=True)
    embed.add_field(name="serverinfo", value="Veja informações do servidor do discord Atual!", inline=True)
    embed.add_field(name="perfil", value="mostra seu perfil!", inline=True)
    embed.add_field(name="ping", value="Veja minha velocidade de resposta!", inline=True)
    await bot.say(embed=embed)
    
    
@bot.command(pass_context=True)
async def rankpts(ctx):
    embed = discord.Embed(title="Rank Pontos Do FREE FIRE (somente membros da guilda)", description="Parabéns ao 1° Lugar", color=0xFF0000)
    embed.set_footer(text="Rank da guilda Legend•Squad")
    embed.set_author(name="Fui criado pelo 彡★ｲЩ乃★彡 Brahma#1111")
    embed.add_field(name="1° Thaiohe", value="3008 Pontos!", inline=True)
    embed.add_field(name="2° DDGames1330F", value="2919 Pontos!", inline=True)
    embed.add_field(name="3° PiTterPoTer", value="2799 Pontos!", inline=True)
    embed.add_field(name="4° Coringa", value="2790 Pontos!", inline=True)
    
    
    
bot.run('NTMwMDk3Mjc2MDczMjc5NDkx.Dw6beg.3EtFKbHl1K7RBTo2rN-RaLgzCb4')
