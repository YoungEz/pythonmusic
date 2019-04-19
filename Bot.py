import discord, time, datetime
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
import asyncio
import time
import colorsys
import sys
import subprocess
import os
import json
import traceback
import random
from random import choice
import request


start_time = time.time()


bot = commands.Bot('s!')
print (discord.__version__)
bot.remove_command('help')
COLOUR = 0xFFFF00
COR = 0x00ff00
amounts = {}
n = "O Motivo Não Foi Definido."

@bot.event
async def on_ready():
	while True:
		await bot.change_presence(game=discord.Game(name='Fui criado pelo El_Brähmäᶠᶸᶜᵏᵧₒᵤ#9911| s!ajuda'.format(len(bot.servers)), type=2))
		await asyncio.sleep(20)
		await bot.change_presence(game=discord.Game(name='para ' + str(len(set(bot.get_all_members())))+ ' usuários!👥', type=1))
		await asyncio.sleep(20)
		await bot.change_presence(game=discord.Game(name='Sendo Desenvolvido 📱💻'))
		await asyncio.sleep(20)
		await bot.change_presence(game=discord.Game(name='s!vote - Me Ajude Dando Um Upvote | s!invite - Me Adicione Em Seu Servidor!', type=3))
		await asyncio.sleep(20)
		await bot.change_presence(game=discord.Game(name='Estou Em {} Servidores'.format(len(bot.servers)), type=2))
		await asyncio.sleep(20)
		await bot.change_presence(game=discord.Game(name='Minha Nova Versão 2.0 Já esta disponivel!', type=1))
		await asyncio.sleep(30)



		



    
@bot.event
async def on_message(message):
	await bot.process_commands(message)
	if message.content.lower().startswith('s!shippar'):
		try:
			nome = message.mentions[0].name
			nome2 = message.mentions[1].name
			nome3 = len(nome2)
			nome4 = nome3 - 4
			nome5 = nome[0:4]
			nome6 = nome2[nome4:nome3]
			nome7 = nome5 + nome6
			pessoa = message.author.name
			porcentagem = random.randint(10, 100)
			voce = message.author.mention
			voce1= message.author.name
			shippar = discord.Embed(title='Será que essa "Shippada" vai ser o Futuro?',
			description='**O(a) {} Shippou {} com {}! \n {} % de chance de ser VERDADE.\n Junção dos nomes: {}** '.format(voce,message.mentions[0].mention,message.mentions[1].mention,porcentagem, nome7), color=COLOUR,
			timestamp=datetime.datetime.utcnow())
			shippar.set_image(url="https://media.giphy.com/media/eBb2guj7V5I5M5lL3t/giphy.gif")
			shippar.set_author(name=pessoa, icon_url=message.author.avatar_url)
			shippar.set_thumbnail(url='https://i.imgur.com/743dfAe.png')
			shippar.set_footer(text='comando realizado por {} | Shiryu Bot Oficial'.format(voce1))
			await bot.send_message(message.channel, embed=shippar)
		except IndexError:
			await bot.send_message(message.channel, "{} Você não mencionou dois usuarios".format(message.author.mention))


		





    
@bot.command(pass_context=True)
async def ping(ctx):
	channel = ctx.message.channel
	t1 = time.perf_counter()
	await bot.send_typing(channel)
	t2 = time.perf_counter()
	embed=discord.Embed(title="Pong!", description='Meu Ping {}ms.'.format(round((t2-t1)*1000)), color=0x76FF03)
	embed.set_footer(text ='Comando pedido por: {} | Shiryu Bot Oficial'.format(ctx.message.author.name))
	await bot.say(embed=embed)
	print('comando ping digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))
	
@bot.command(pass_context=True)
async def servers(ctx):
	servers = list(bot.servers)
	await bot.say("Estou conectado em " + str(len(bot.servers)) + " servers:")
	for x in range(len(servers)):
		await bot.say(" "+servers[x-1].name)

@bot.command(pass_context = True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member=None, *, motivo: str = None):
    motivo = motivo or n
    if not member:
        return await bot.say('{} Você não especificou o usuário. Exemplo: ``s!ban <@usuário> <motivo>``'.format(ctx.message.author.mention))
    else:
        await bot.ban(member)

        horario = datetime.datetime.now().strftime("%H:%M:%S")	
        embed = discord.Embed(title='Ação | Ban', description='{} usuário banido com sucesso'.format(ctx.message.author.mention), color=0xff0Ab)
        embed.add_field(name='👮 Executor', value=ctx.message.author)
        embed.add_field(name='👥 Usuário', value=member.name)
        embed.add_field(name='💻 Id', value=member.id)
        embed.add_field(name='📝 Motivo', value=motivo)
        embed.add_field(name='🕒 Hora', value=horario)
        embed.set_footer(text='Comando Realizado Por: {}| Shiryu Bot ★'.format(ctx.message.author.name))
        await bot.say(embed=embed)
        embedpv = discord.Embed(title='Ação | Ban'.format(ctx.message.author.mention), color=0xff0Ab)
        embedpv.add_field(name='Executor', value=ctx.message.author)
        embedpv.add_field(name='Servidor', value=ctx.message.server.name)
        embedpv.add_field(name='Motivo', value=motivo)
        embedpv.set_thumbnail(url=ctx.message.server.icon_url)
        await bot.send_message(member, embed=embedpv)
        print('comando ban digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))
							
@bot.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.User=None, *, motivo: str = None):
    motivo = motivo or n
    if not user:
        return await bot.say('{} Você não especificou o usuário. Exemplo: ``s!kick <@usuário> <motivo>``'.format(ctx.message.author.mention))
    else:
        await bot.kick(user)
        embed = discord.Embed(title='Ação | Kick!', description='{} usuário expulso com sucesso'.format(ctx.message.author.mention), color=0xff0Ab)
        embed.add_field(name='👮 Autor', value=ctx.message.author)
        embed.add_field(name='👥 usuário', value=user)
        embed.add_field(name='💻 Id', value=user.id)
        embed.add_field(name='📝 Motivo', value=motivo)
        embed.set_footer(text='Comando Realizado Por: {}| Shiryu Bot ★'.format(ctx.message.author.name))
        await bot.say(embed=embed)
        embedpv = discord.Embed(title='Ação | Kick'.format(ctx.message.author.mention), color=0xff0Ab)
        embedpv.add_field(name='👮 Executor', value=ctx.message.author)
        embedpv.add_field(name='💻 Servidor', value=ctx.message.server.name)
        embedpv.add_field(name='💻 id', value=ctx.message.author.id)
        embedpv.add_field(name='📝 Motivo', value=motivo)
        embedpv.set_thumbnail(url=ctx.message.server.icon_url)
        await bot.send_message(user, embed=embedpv)
        print('comando kick digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))
		
@bot.command()
async def vote():
    embed = discord.Embed(description='**Olá! Poderia Me Ajudar Votando Em Mim? clique [aqui](https://discordbots.org/bot/539468157291855903/vote)**', color=0x00ffbb)
    await bot.say(embed=embed)
	
@bot.command(pass_context=True)
async def votar(ctx, *, mensagem: str= None):
	if not mensagem:
		return await bot.say('Você precisa falar algo para votar')
	else:
			vote = await bot.say(embed=discord.Embed(color=0xff0000, description=mensagem))
			await bot.add_reaction(vote, "✅")
			await bot.add_reaction(vote, "❌")
	print('comando votar digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))
	
	
@bot.command()
async def attlogs():
	embed = discord.Embed(title='Atualizações do bot', color=0xB0ffA0)
	embed.add_field(name='02/02/2018', value='Bot Aprovado Na Discord Bot List')
	embed.add_field(name='01/02/2018', value='Correções de bugs')
	embed.add_field(name='01/02/2018', value='Adicionado Motivo No Ban e Kick, O Bot tambem envia uma mensagem no PV do usuário banido')
	embed.add_field(name='01/02/2018', value= 'Novo comando de diversão ``s!chorar``')
	embed.add_field(name='31/02/3018', value='Novos comandos ``s!votar`` e ``s!pergunta``')
	await bot.say(embed=embed)
	print('comando attlogs digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))
			
					
import datetime	
	
@bot.command(pass_context=True)
async def userinfo(ctx, user: discord.User=None):
    user = user or ctx.message.author
    embed = discord.Embed(title="informações de {}".format(user.name), color=0x00ff00)
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="👨 Nome", value=user.name, inline=True)
    embed.add_field(name="🎭 Apelido", value=user.nick)
    embed.add_field(name="💻 ID", value=user.id, inline=True)
    embed.add_field(name="📱 Status", value=user.status, inline=True)
    embed.add_field(name="🎮 Jogando", value=user.game)
    embed.add_field(name="🔝 Melhor cargo", value=user.top_role)
    embed.add_field(name="📆 Entrou aqui em", value=user.joined_at.strftime("%d %b %Y ás %H:%M"))
    embed.set_footer(text ='Comando pedido por: {} | Shiryu Bot Oficial'.format(ctx.message.author.name))
    await bot.say(embed=embed)
    print('comando attlogs digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))
	
@bot.command(pass_context=True)
async def invite(ctx):
    e = discord.Embed(description='{} **Olá Para Me Adicionar Em Seu Servidor Clique [aqui](https://discordapp.com/oauth2/authorize?client_id=539468157291855903&permissions=8&scope=bot) | Poderia Me Ajudar Dando Um Upvote? Clique [aqui](https://discordbots.org/bot/539468157291855903/vote)**'.format(ctx.message.author.mention), color=0xff0f00)
    await bot.say(embed=e)
    print('comando invite digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))
	
@bot.command(pass_context=True)
async def serverinfo(ctx):
	embed = discord.Embed(name="{}' Serverinfo".format(ctx.message.server.name), color=0x00fA00)
	embed.add_field(name="📄 Nome do Servidor", value=ctx.message.server.name, inline=True)
	embed.add_field(name = '👑 Dono', value = str(ctx.message.server.owner));
	embed.add_field(name="💻 ID do servidor", value=ctx.message.server.id, inline=True)
	embed.add_field(name="🎓 Total de roles", value=len(ctx.message.server.roles), inline=True)
	embed.add_field(name="👥 Total de Membros", value=len(ctx.message.server.members))
	embed.add_field(name='🌎 Região', value=ctx.message.server.region)
	embed.add_field(name='👮Cargo Max', value=ctx.message.server.role_hierarchy[0])
	embed.set_thumbnail(url=ctx.message.server.icon_url)
	await bot.say(embed=embed)
	print('comando serverinfo digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))

@bot.command(pass_context=True)
async def avatar(ctx, user: discord.User=None):
	user = user or ctx.message.author
	
	list = (user.avatar_url), (user.avatar_url)
	hug = random.choice(list)
	hugemb = discord.Embed(title='Avatar de {}'.format(user.name), color=0x6A1B9A)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text ='Comando pedido por: {} | Shiryu Bot Oficial'.format(ctx.message.author.name))
	await bot.say(embed=hugemb)
	print('comando avatar digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))
	

	
	

	
@bot.command(pass_context=True)
async def kepiada(ctx):
	a = 'https://cdn.discordapp.com/attachments/514045065929162764/539758537245589504/Piada_mulher_de_tpm_cafe.jpg', 'https://cdn.discordapp.com/attachments/514045065929162764/539758537245589505/images_6.jpeg', 'https://cdn.discordapp.com/attachments/514045065929162764/539758537245589506/images_4.jpeg', 'https://cdn.discordapp.com/attachments/514045065929162764/539758537711026177/o_rapaz_apaixonado_diz_a_sua_amada.jpg', 'https://cdn.discordapp.com/attachments/514045065929162764/539758538214604810/images_5.jpeg', 'https://cdn.discordapp.com/attachments/514045065929162764/539758538214604812/ladrao-em-casa-3684XBr1G1DBAQ.jpg', 'https://cdn.discordapp.com/attachments/514045065929162764/539758538734567424/Passa_Passa_Passa.jpg', 'https://cdn.discordapp.com/attachments/514045065929162764/539758538734567425/na_delegacia_seu_delegado_meu_marido_saiu_de_casa.jpg'
	hug = random.choice(a)
	hugemb = discord.Embed(title='Piadas', color=0x6A1B9A)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text ='Comando pedido por: {} | Shiryu Bot Oficial'.format(ctx.message.author.name))
	await bot.say(embed=hugemb)
	print('comando kepiada digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))
	
@bot.command(pass_context=True)
async def meme(ctx):
	a = 'https://cdn.discordapp.com/attachments/514045065929162764/539763086895349760/images_9.jpeg', 'https://cdn.discordapp.com/attachments/514045065929162764/539763086895349761/cara-mano-tatuei-o-nome-da-minha-namora-e-ela-20426746.png', 'https://cdn.discordapp.com/attachments/514045065929162764/539763087474032640/images_7.jpeg', 'https://cdn.discordapp.com/attachments/514045065929162764/539763087474032641/images_10.jpeg', 'https://cdn.discordapp.com/attachments/514045065929162764/539763088002383883/images_11.jpeg', 'https://cdn.discordapp.com/attachments/514045065929162764/539763088455630855/3d6dcd431d328b82ac2bc8edf5f754ee--kawaii.jpg'
	hug = random.choice(a)
	hugemb = discord.Embed(title='SO MEME DE QUALIDADE MONSTRA', color=0x6A1B9A)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text ='Comando pedido por: {} | Shiryu Bot Oficial'.format(ctx.message.author.name))
	await bot.say(embed=hugemb)
	print('comando meme digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))

	

	
@bot.command(pass_context = True)
@commands.has_permissions(manage_nicknames=True)     
async def setnick(ctx, user: discord.Member, *, nickname: str=None):
    await bot.change_nickname(user, nickname)
    emb = discord.Embed(title='Ação | Setnick')
    emb.add_field(name='usuário', value =user.name)
    emb.add_field(name='Autor', value =ctx.message.author.name)
    emb.add_field(name='Novo Apelido', value=nickname)
    
    await bot.say(embed=emb)
    print('comando setnick digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))
    
@bot.command(pass_context = True)
@commands.has_permissions(ban_members=True)
async def avisar(ctx, member: discord.Member, *, content: str):
	embed = discord.Embed(description='{} foi avisado com sucesso! por {}'.format(member.mention, ctx.message.author.mention), color=0x7a00bb)
	embedpv = discord.Embed(title='Aviso', color=0x00AB70)
	embedpv.add_field(name='Aviso Do servidor', value=ctx.message.server.name)
	embedpv.add_field(name='Autor', value=ctx.message.author)
	embedpv.add_field(name='Motivo', value=content)
	embedpv.set_thumbnail(url=ctx.message.server.icon_url)
	await bot.send_message(member, embed=embedpv)
	
	await bot.say(embed=embed)  
	print('comando avisar digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))	

	
@bot.command(pass_context=True)
@commands.has_permissions(manage_roles=True)
async def setcargo(ctx, role: discord.Role=None, member: discord.Member=None, *, motivo: str=None):
    member = member or ctx.message.author
    motivo = motivo or n
    if not role:
        await bot.say('{} Você Precisa Mencionar Um Cargo Para Adicionar'.format(ctx.message.author.mention))
    else:
        await bot.remove_roles(member, role)
    embed = discord.Embed(title='Ação | Adicionar Cargo', color=0xff0000)
    embed.add_field(name='👮 Autor', value=ctx.message.author)
    embed.add_field(name='💻 Id', value=ctx.message.author.id)
    embed.add_field(name='👥 Usuário', value=member)
    embed.add_field(name='💻 Id', value=member.id)
    embed.add_field(name='📝 Motivo', value=motivo)            
    await bot.say(embed=embed)
    print('comando removerole digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))
  	


@bot.command(pass_context=True)
@commands.has_permissions(manage_roles=True)
async def removercargo(ctx, role: discord.Role=None, member: discord.Member=None, *, motivo: str=None):
    member = member or ctx.message.author
    motivo = motivo or n
    if not role:
        await bot.say('{} Você Precisa Mencionar Um Cargo Para Remover'.format(ctx.message.author.mention))
    else:
        await bot.remove_roles(member, role)
    embed = discord.Embed(title='Ação | Remover Cargo', color=0xff0000)
    embed.add_field(name='👮 Autor', value=ctx.message.author)
    embed.add_field(name='💻 Id', value=ctx.message.author.id)
    embed.add_field(name='👥 Usuário', value=member)
    embed.add_field(name='💻 Id', value=member.id)
    embed.add_field(name='📝 Motivo', value=motivo)            
    await bot.say(embed=embed)
    print('comando removerole digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))
  
    
@bot.command(pass_context=True)
async def falar(ctx, *, arg: str=None):
    if not arg:
        return await bot.say('{} Você Precisa Escrever Algo Para Eu Falar.'.format(ctx.message.author.mention))
    else:
        await bot.say("{} Me Forçou A Falar...{}".format(arg))
        print('comando falar digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))

	
@bot.command(pass_context=True)
async def tapa(ctx, user: discord.User=None):
    if not user:
        return await bot.say('{} Você Não Especificou Um Usuário'.format(ctx.message.author.mention))
    else:
        list = 'https://cdn.discordapp.com/attachments/514045065929162764/539494352112713760/giphy.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/539494352112713760/giphy.gif'
        hug = random.choice(list)
        hugemb = discord.Embed(title='Ação | Tapa🔥', description=':scream:| **{}** Deu Um tapa em **{}**! Que Tapa!'.format(ctx.message.author.name, user.name), color=0xA7ffbb)
        hugemb.set_image(url=hug)
        hugemb.set_footer(text ='Comando realizado por: {} | Shiryu Bot Oficial'.format(ctx.message.author.name))
        await bot.say(embed=hugemb)
        print('comando slap digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))
	
@bot.command(pass_context=True)
async def brigar(ctx, user: discord.User=None):
    if not user:
        return await bot.say('{} Você Não Especificou Um Usuário'.format(ctx.message.author.mention))
    else:
        list = 'https://cdn.discordapp.com/attachments/514045065929162764/539516094273290240/300px-DarkCureFight.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/539733424185802763/source.gif'
        hug = random.choice(list)
        hugemb = discord.Embed(title='Ação | Briga 👊',  description=':scream:| **{}** Brigou com **{}**!'.format(ctx.message.author.name, user.name), color=0xA7ffbb)
        hugemb.set_image(url=hug)
        hugemb.set_footer(text ='Comando realizado por: {} | Shiryu Bot Oficial'.format(ctx.message.author.name))
        await bot.say(embed=hugemb)
        print('comando brigar digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))	
	
@bot.command(pass_context=True)
async def dance(ctx, user: discord.User=None):
    if not user:
        return await bot.say('{} Você Não Especificou Um Usuário'.format(ctx.message.author.mention))
    else:
        list = 'https://cdn.discordapp.com/attachments/514045065929162764/539516095900418104/fanfiction-naruto-ao-seu-lado-2635515231020140950.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/539516093593550868/ed8964dd9fb2f90e5eb4b19c577bec74.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/539516093593550869/Akatsuki28.gif'
        hug = random.choice(list)
        hugemb = discord.Embed(title='Ação | Dançar',  description=':man_dancing:| **{}** Esta dançando com **{}**! Passinho dos Maloka 😎'.format(ctx.message.author.name, user.name), color=0xA7ffbb)
        hugemb.set_image(url=hug)
        hugemb.set_footer(text ='Comando pedido por: {} | Shiryu Bot Oficial'.format(ctx.message.author.name))
        await bot.say(embed=hugemb)
        print('comando ping digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))
		

@bot.command(pass_context=True)
async def matar(ctx, user: discord.User=None):
    if not user:
        return await bot.say('{} Você Não Especificou Um Usuário'.format(ctx.message.author.mention))
    else:
        list = 'https://cdn.discordapp.com/attachments/514045065929162764/539733424185802762/b19b70f5c546ec7c67c2f0b4e61c21f743a5acaf_hq.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/539733902097645568/tumblr_m6rerquar01qd4f2uo1_500.gif'
        hug = random.choice(list)
        hugemb = discord.Embed(title='Ação | Matar',  description='👮| **{}** Matou **{}**! ASSASINO!'.format(ctx.message.author.name, user.name), color=0xA7ffbb)
        hugemb.set_image(url=hug)
        hugemb.set_footer(text ='Comando pedido por: {} | Shiryu Bot Oficial'.format(ctx.message.author.name))
        await bot.say(embed=hugemb)
	

	
	
@bot.command(pass_context=True)
async def atacar(ctx, user: discord.User=None):
    if not user:
        return await bot.say('{} Você Não Especificou Um Usuário'.format(ctx.message.author.mention))
    else:
        list = 'https://cdn.discordapp.com/attachments/514045065929162764/539494351030452238/tumblr_mzh5vtuEIC1rm4wgqo4_r2_500.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/539494352926277633/01_Rikka.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/539494350053310475/G4dfvA5.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/539733423418376194/large.gif'
        hug = random.choice(list)
        hugemb = discord.Embed(title='Ação | Atack!',  description='💥| **{}** Atacou **{}**! Como ousas me atacar!'.format(ctx.message.author.name, user.name), color=0xA7ffbb)
        hugemb.set_image(url=hug)
        hugemb.set_footer(text ='Comando pedido por: {} | Shiryu Bot Oficial'.format(ctx.message.author.name))
        await bot.say(embed=hugemb)
	
@bot.command(pass_context=True)
async def suicidio(ctx):
	list = 'https://cdn.discordapp.com/attachments/514045065929162764/533344634576044052/tumblr_nee9xjzaxR1r3rdh2o1_500-1.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/533344635247001602/47892bb88afc132a3afb775988208240.gif'
	
	
	
	hug = random.choice(list)
	hugemb = discord.Embed(title='Suicidio 💔',  description='**{}** se suicidou!'.format(ctx.message.author.name), color=0xA7ffbb)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text ='Comando pedido por: {} | Shiryu Bot Oficial'.format(ctx.message.author.name))
	await bot.say(embed=hugemb)
	
@bot.command(pass_context=True)
async def voadora(ctx, user: discord.User=None):
    if not user:
        return await bot.say('{} Você Não Especificou Um Usuário'.format(ctx.message.author.mention))
    else:
        list = 'https://cdn.discordapp.com/attachments/514045065929162764/539733422621589504/giphy_6.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/539733422621589504/giphy_6.gif'
        hug = random.choice(list)
        hugemb = discord.Embed(title='Voadora',  description='**{}** Deu uma voadora em **{}** EITA!'.format(ctx.message.author.name, user.name), color=0xA7ffbb)
        hugemb.set_image(url=hug)
        hugemb.set_footer(text ='Comando pedido por: {} | Shiryu Bot Oficial'.format(ctx.message.author.name))
        await bot.say(embed=hugemb)

nc = "Parada Cardiaca"		
@bot.command(pass_context=True)
async def deathnote(ctx, user: discord.User=None,*, causa: str=None):
    causa = causa or nc
    if not user:
        return await bot.say('{} Você Não Especificou Um Usuário'.format(ctx.message.author.mention))
    else:
        list = 'https://cdn.discordapp.com/attachments/514045065929162764/534806488531599380/14ae937e622c452bc45e509ed43c8e38a410fc0b_hq.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/533615190273425409/67dc6ce11c0ebe1c723983f18d7f68a8b0d11887_hq.gif'
        hug = random.choice(list)
        hugemb = discord.Embed(title='Ação | Death Note',  description='**{}** escreveu o nome de **{}** em seu Death Note'.format(ctx.message.author.name, user.name), color=0xA7ffbb)
        hugemb.set_image(url=hug)
        hugemb.set_footer(text='Bot Oficial Shiryu')
        await bot.say(embed=hugemb)
        await asyncio.sleep(5)
        hugemb = discord.Embed(title='Faliceu',  description='**{}** morreu Apos 30 segundos\n'
        'seu nome escrito no Death Note de **{}**\n'
        'Causa Da Morte: **{}**'.format(user.name, ctx.message.author.name, causa), color=0xA7ffbb)
        hugemb.set_footer(text ='Comando pedido por: {} | Shiryu Bot Oficial'.format(ctx.message.author.name))
        await bot.say(embed=hugemb)

@bot.command(pass_context=True)
async def beijar(ctx, user: discord.User=None):
    if not user:
        return await bot.say("{} Você Não Marcou Um Usuário Para Beijar")
    else:
        list = 'https://cdn.discordapp.com/attachments/514045065929162764/533253217883258890/tumblr_mie2frAdXc1rfj82jo2_500.gif','https://cdn.discordapp.com/attachments/514045065929162764/533253218860269577/86d4a046c8a32a28341353fc95bedc82.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/539494353694097438/feliz-aniversario-6224237-140820161718.gif'
        hug = random.choice(list)
        hugemb = discord.Embed(title='Beijo! ❤',  description='**{}** recebeu um beijo de **{}**! Casal Fofo! :heart_eyes:'.format(user.name, ctx.message.author.name), color=0xA7ffbb)
        hugemb.set_image(url=hug)
        hugemb.set_footer(text ='Comando pedido por: {} | Shiryu Bot Oficial'.format(ctx.message.author.name))
        await bot.say(embed=hugemb)
        print('comando kiss digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))	
			
@bot.command(pass_context=True)
async def abraçar(ctx, user: discord.User=None):
    if not user:
        return await bot.say('{} Você Não Especificou Um Usuário'.format(ctx.message.author.mention))
    else:
        list = 'https://cdn.discordapp.com/attachments/531090629715951629/532667673943736351/action.gif','https://cdn.discordapp.com/attachments/531090629715951629/532672938596368393/action.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/539494351555002379/tumblr_mdi1l8AaDi1rcm8d4o1_500.gif'
        hug = random.choice(list)
        hugemb = discord.Embed(title='Ação | Abraço',  description='**{}** Ele(a) recebeu um abraço de **{}**!! :heart_eyes:'.format(user.name, ctx.message.author.name), color=0x00ffbb)
        hugemb.set_image(url=hug)
        hugemb.set_footer(text ='Comando pedido por: {} | Shiryu Bot Oficial'.format(ctx.message.author.name))
        await bot.say(embed=hugemb)  
	
@bot.command()
async def flipcoin():
	list = 'tapa na **CARA**', 'Rei perdeu a **COROA**'
	await bot.say(random.choice(list))
	
			
@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def voiceunmute(ctx, member: discord.Member=None):
    if not member:
        return await bot.say('{} Você Não Especificou Um Usuário'.format(ctx.message.author.mention))
    else:
        await bot.server_voice_state(member,mute=True)
        await bot.say('{} O Usuário {} Foi desmutado com sucesso'.format(ctx.message.author.mention, member.mention)) 

@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def voicemute(ctx, member: discord.Member=None):
    if not member:
        return await bot.say('{} Você Não Especificou Um Usuário'.format(ctx.message.author.mention))
    else:
        await bot.server_voice_state(member,mute=False)
        await bot.say('{} O Usuário {} Foi mutado com sucesso'.format(ctx.message.author.mention, member.mention))

@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def clear(ctx, limit: int=100):
    async for msg in bot.logs_from(ctx.message.channel, limit=limit):
            try:
                await bot.delete_message (msg)
            except:
                pass
    await bot.say ("Chat Limpo por {}".format(ctx.message.author.mention))
    print('comando clear digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))
    
@bot.command(pass_context = True)
async def help(ctx):
    author = ctx.message.author
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    
   
    
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name='Ajuda')
    embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
    embed.add_field(name = 's!modajuda ',value ='Comandos de moderação',inline = False)
    embed.add_field(name = 's!diversaoajuda ',value ='Comandos de diversão e que todos podem usar!',inline = False)
    embed.set_footer(text='comando realizado por {}| Bot Oficial Shiryu'.format(ctx.message.author.name))
    await bot.send_message(author,embed=embed)
    await bot.say('{} Enviei mensagens em sua DM'.format(ctx.message.author.mention))
    print('comando help digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))    
    
    
@bot.command(pass_context = True)
async def ajuda(ctx):
    author = ctx.message.author
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    
   
    
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name='Ajuda')
    embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
    embed.add_field(name = 's!modajuda ',value ='Comandos de moderação',inline = False)
    embed.add_field(name = 's!diversaoajuda ',value ='Comandos de diversão e que todos podem usar!',inline = False)
    embed.set_footer(text='comando realizado por {}| Bot Oficial Shiryu'.format(ctx.message.author.name))
    await bot.send_message(author,embed=embed)
    await bot.say('{} Enviei mensagens em sua DM'.format(ctx.message.author.mention))
    print('comando ajuda digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))
    
@bot.command(pass_context = True)
async def modajuda(ctx):
    author = ctx.message.author
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name='Comandos Moderação Help')
    embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
    embed.add_field(name = 's!kick ',value ='como usar ``s!kick @usuário <motivo>`` Expulsa o usuário marcado',inline = False)
    embed.add_field(name = 's!ban ',value ='Como usar ``s!ban @usuário <motivo>`` bane o usuário marcado',inline = False)
    embed.add_field(name = 's!addrole ',value ='Como usar ``s!setcargo @cargo @usuário`` adiciona um determinado cargo ao usuário marcado',inline = False)
    embed.add_field(name = 's!removerole',value ='Como usar ``s!removercargo @cargo @usuário`` remove um determinado cargo do usuário marcado ',inline = False)
    embed.add_field(name = 's!clear',value ='Como usar ``s!clear <quantidade>`` apaga as mensagens do canal de texto atual ',inline = False)
    embed.add_field(name = 's!avisar',value ='Como usar ``s!avisar @usuário <mensagem>`` avisa um usuário no PV ',inline = False)


    await bot.send_message(author,embed=embed)
    await bot.say('{} Enviei mensagens em sua DM'.format(ctx.message.author.mention))
    print('comando modajuda digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))
    
@bot.command(pass_context=True)
async def roleta(ctx, *, pergunta: str = None):
    if not pergunta:
        return await bot.say("Você precisa perguntar alguma coisa.")
    else:
        resposta = choice(['Sim', 'Não', 'Talvez', 'Nunca', 'Claro'])
        embed = discord.Embed(color=0xFF0000)
        embed.add_field(name="Pergunta:", value='{}'.format(pergunta), inline=False)
        embed.add_field(name="Resposta:", value=resposta, inline=False)
        await bot.say(embed=embed)
        print('comando roleta digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))
    
    
   
   
@bot.command(pass_context=True)
async def diversaoajuda(ctx):
    author = ctx.message.author
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name = 's!dance ',value ='Como usar ``s!dance`` dance com algum usuário',inline = False)
    embed.add_field(name = 's!beijar ',value ='Como usar ``s!beijar @usuário`` O amor esta no ar! beije determinado usuário!',inline = False)
    embed.add_field(name = 's!abraçar ',value ='Como usar ``s!abraçar @usuário`` abrace seu/sua melhor amigo(a).',inline = False)
    embed.add_field(name = 's!flipcoin ',value ='Como usar ``s!flipcoin`` Cara ou coroa?',inline = False)
    embed.add_field(name = 's!deathnote ',value ='Como usar ``s!deathnote @usuário <causa da morte>`` Escreva o nome de determinado usuário em seu Death Note ',inline = False)
    embed.add_field(name = 's!avatar ',value ='Como usar ``s!avatar @usuário`` Veja o avatar do usuário',inline = False)
    embed.add_field(name="s!meme", value="como usar ``s!meme`` que tal ver alguns memes?!", inline=False)
    embed.add_field(name="s!ping", value="como usar ``s!ping`` Veja meu tempo de resposta!", inline=False)
    embed.add_field(name="s!userinfo", value="como usar ``s!userinfo @usuário`` Veja o perfil de um determinado usuário!", inline=True)
    embed.add_field(name="s!voadora", value="como usar ``s!voadora @usuário`` de uma voadora em alguem!", inline=True)
    embed.add_field(name="s!brigar", value="como usar ``s!brigar @usuário`` Use esse comando se alguem estiver merecendo apanhar!", inline=True)  	
    embed.add_field(name="s!matar", value="como usar ``s!matar @usuário`` Use esse comando se alguem estiver merecendo!", inline=True)
    embed.add_field(name="s!tapa", value="como usar ``s!tapa @usuário`` Use esse comando se alguem estiver merecendo levar uns tapa cabuloso", inline=True)
    embed.add_field(name="s!falar", value="como usar ``s!falar <mensagem>`` Faça eu falae alguma coisa!", inline=True)
    embed.add_field(name="s!suicidio", value="como usar ``s!suicidio`` Se Suicida", inline=True)
    embed.add_field(name="s!kepiada", value="como usar ``s!kepiada`` Que tal uma piada?!", inline=True)
    embed.add_field(name="s!atacar", value="como usar ``s!atack @usuário`` use este comando para atacar alguem!", inline=True)
    embed.add_field(name="s!chorar", value="como usar ``s!chorar`` Chorar faz bem para os olhos...", inline=True)
    embed.add_field(name="s!votar", value="como usar ``s!votar`` Faça uma votação em seu servidor", inline=True)
    embed.add_field(name="s!pergunta", value="como usar ``s!pergunta`` me faça uma pergunta!", inline=True)
    embed.add_field(name="s!shippar", value="como usar ``s!shippar <user> <user>`` Veja Se Um Casal Daria certo!", inline=True)
        
    await bot.send_message(author,embed=embed)
    await bot.say('{} Enviei mensagens em sua DM'.format(ctx.message.author.mention))
    print('comando diversaoajuda digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))  
      
@bot.command(pass_context=True)
async def chorar(ctx):
	list = 'https://cdn.discordapp.com/attachments/514045065929162764/540913648453943338/tumblr_mchb17x02w1r5patso2_500.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/540913648453943336/0319d0c4d6ce1750c2fc7b3c5d383723db18d37dr1-500-284_00.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/540913648034643972/86a31db739b7f40d576c90f1ff9329ab254958f0_hq.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/540913647610757130/cfd934eac0f14d3f43284b16ec0a902b.gif'
	
	
	
	hug = random.choice(list)
	hugemb = discord.Embed(title='Ação | Chorar',  description='😭|**{}** Esta chorando...'.format(ctx.message.author.name), color=0xA7ffbb)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text ='Comando realizado por {} | Shiryu Bot Oficial'.format(ctx.message.author.name))
	await bot.say(embed=hugemb)
	print('comando chorar digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))    
	


bot.run(str(os.environ.get('BOT_TOKEN')))
