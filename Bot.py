import discord
import asyncio
import youtube_dl
from discord.ext import commands



client = commands.Bot(command_prefix = 't!')


@client.event
async def on_ready():
    while True:
        await client.change_presence(game=discord.Game(name='Karaoke no The World Of Bad'))
        await asyncio.sleep(20)
        await client.change_presence(game=discord.Game(name="🎉 Fui desenvolvido pelo 彡★ｲЩ乃★彡 Brahma#1111👑", type=1))
        await asyncio.sleep(20)
        await client.change_presence(game=discord.Game(name='Musica com meu criador!', type=2))
        await asyncio.sleep(20)
        await client.change_presence(game=discord.Game(name='Quer ser staff? chame o meu criador 彡★ｲЩ乃★彡 Brahma#1111 No Pv!', type=3))
        await asyncio.sleep(20)
print('Bot online')
	
@client.event
async def on_member_join(member):
  canal = client.get_channel("495700015801434122")
  regras = client.get_channel("495700015801434122")
  msg = "{} entrou no servidor! Leia nossas regras e divirta-se em nossos chats".format(member.mention, regras.mention)
  await client.send_message(canal, msg) 

@client.event
async def on_member_remove(member):
   canal = client.get_channel("495700015801434122")
   msg = "Adeus,Te vejo no paraiso! {}".format(member.mention)
   await client.send_message(canal, msg)
	
@client.command(pass_context=True)
async def clear(ctx, limit: int=100):
    async for msg in client.logs_from(ctx.message.channel, limit= 10):
 
            try:
                await client.delete_message (msg)
            except:
                pass
    embed = discord.Embed(description=" As mensagens foram deletadas com sucesso! :smile:", color=0x00ff00)
    await client.say (embed=embed)
@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, userName: discord.User):
	await client.kick(userName)
	print ("user has kicked")
   
 
@client.command(pass_context = True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, userName: discord.User):
	await client.ban(userName)
	print("user has banned")

@client.event
async def on_server_join(server):
	stay = False
	admin = None
	channel = bot.get_channel("495747382051602433")
	for member.id in config.client_admin:
		admin = member.mention

        
        

	


@client.command(context_pass=True)
async def entrar(ctx):
	channel = ctx.message.author.voice.voice_channel
	await client.join_voice_channel(channel)
	
@client.command(context_pass=True)
async def sair(ctx):
	server = ctx.message.server
	voice_client = client.voice_server_in(server)
	await voice_client.disconnect()
	
@client.command(context_pass=True)
async def tocar(ctx, url):
	server = ctx.message.server
	voice_client = client.voice_in(server)
	player = await voice_client.create_ytdl_player(url)
	players[serverid] = player
	player.start()
	

	
client.run('BOT_TOKEN')
