# Lil Boc by Ski Mask
import asyncio
import typing
from discord.ext.commands import MissingPermissions
from discord.ext import commands
from discord.ext.commands import has_permissions
import random
import os
import discord
import praw


dothething = {}

messages = joined = 0

intents = discord.Intents.default() # or .all() if you ticked all, that is easier
intents.members = True # If you ticked the SERVER MEMBERS INTENT

#client = commands.client(command_prefix=".", intents=intents) # "Import" the intents
 
client = commands.Bot(command_prefix=".", intents=intents)


alfabets = {'pisi pats xDDDDD', 'AAAAAAAAAAAAAAAAA','es jau tur' , 'BAMBUZO :angry:', 'Uzsuc silto ;)'}

viensdesmit = {'1','2','3','4','5','6','7','8','9','10'}

bumba = {'kā es to redzu, jā.','vēlāk jautā vēlreiz.','labāk tagad nestāsti.','tagad nevar paredzēt.','koncentrējies un jautā vēlreiz.','ar to nerēķinies.','tas ir skaidrs.','tā noteikti ir.','visticamāk.','mana atbilde ir nē.','mani avoti saka nē.','perspektīva nav tik laba.','perspektīva laba.','atbilde miglaina, mēģini vēlreiz.','zīmes norāda uz jā.','ļoti apšaubāmi.','bez šaubām.','jā.','jā - noteikti.','vari paļauties uz to.'}

uzraksti = {'Atkal bambuzo raksta! XD', 'Nu tak beidz sudu rakstit!', 'BEIIIIIIIIIIIIIIIIDZ! :@'}

dabi = {'https://media1.tenor.com/images/3d71b1a0775e998514b124285613984b/tenor.gif?itemid=12276072','https://media.giphy.com/media/3oKIP6AYztSrFZ0AoM/giphy.gif', 'https://media.giphy.com/media/26uTt19akcFxRFCy4/giphy.gif', 'https://media.giphy.com/media/3h5VTO6F1i2gU/giphy.gif', 'https://media.giphy.com/media/26FPpIxroCqzJzi7K/giphy.gif'}

plikimeiteni = {'RealGirls','NSFW','BoltedOnTits', 'ass', 'bigasses', 'SpreadEm', 'booty', 'thick', 'ShinyPorn', 'seethru', 'gonewild', 'Blonde', 'redheads','shorthairchicks','HappyEmbarrassedGirls','palegirls','SexyFrex','flexi','LegalTeens','theratio','milf','Hotchickswithtattoos','piercedtits','pussy','rearpussy','HairyPussy','simps','SexyGirlsInBoots','boobs','Boobies'}

carcrash = {'https://images.carscoops.com/2017/05/crash-civic.gif', 'https://media2.giphy.com/media/PWGti9oEnobni/giphy.gif?cid=790b7611e251c3496c37ea81b847ff2a43c38d7bc891f436&rid=giphy.gif','https://thumbs.gfycat.com/ColorlessBrownGrackle-max-1mb.gif','https://media.giphy.com/media/12yMUVLcImY5a0/giphy.gif','https://images.carscoops.com/2019/10/98df3fbf-accidents-civic-brake-checks-hummer.gif'}

wiiiiiiiiizijs = {'https://media1.tenor.com/images/33f03dc04994af47305189d5da00f13c/tenor.gif?itemid=14638153','https://media1.tenor.com/images/fe3788c68a25911c139c027034e2f88a/tenor.gif?itemid=13936491','https://media.giphy.com/media/h8HmN0UcEKR0xWnv3R/giphy.gif','https://media.giphy.com/media/LkxWvkmpy2uznXth6A/giphy.gif'}

colors = [0XFF0000,0X008000,0X0000FF,0x00FF00,0xFFFFFF,0x000000,0xFFFF00,0x00FFFF,0xFF00FF,0xC0C0C0,0x808080,0x800000,0x808000,0x800080,0x008080,0x000080]

newUserMessage = 'skrt'

#client.remove_command("help")

guild_id = "215848568064311296"

reddit = praw.Reddit(client_id='AbfIbqf0tsxxKg', 
                     client_secret='vfsDGc7PLAvzENjRYMVpLpJVLUg',
                     user_agent='Discord client',
                     username='Jezups',
                     password='hagisons112')
 
@client.event
async def on_ready():
    client.loop.create_task(status_task())
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('--------')

async def status_task():
    while True:
        await client.change_presence(activity=discord.Game(name='.commands'))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game(name='pis nahuj'))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game(name='turi muti'))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game(name='woof'))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game(name='pis pa muti/pis prom'))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game(name='atpisies ble'))
        await asyncio.sleep(10)

@client.command()
async def meme(ctx):
    memes_submissions = reddit.subreddit('memes').hot()
    post_to_pick = random.randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)
     
    embed = discord.Embed(title = submission.title ,color = random.choice(colors))
      
    embed.set_image(url = submission.url)
    
    await ctx.send(embed = embed)
    
@client.command()
async def dmeme(ctx):
    memes_submissions = reddit.subreddit('RealOffensiveMemes').hot()
    post_to_pick = random.randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)
    embed = discord.Embed(title = submission.title ,color = random.choice(colors))   
      
    embed.set_image(url = submission.url)
    
    await ctx.send(embed = embed)
       
@client.command()
async def adab(ctx):
    memes_submissions = reddit.subreddit('animegirlsdabbing').hot()
    post_to_pick = random.randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)
     
    embed = discord.Embed(title = submission.title ,color = random.choice(colors))

    embed.set_image(url = submission.url)
    
    await ctx.send(embed = embed) 
  
@client.command()  
async def nsfw(ctx):    

     id = client.get_guild(646362943063326720)
     channels = ["nsfw"]   
     plikimeiteni_copy = plikimeiteni.copy()
     for n in [1]:
        cs = random.sample(plikimeiteni_copy , k=n)
        plikimeiteni_copy -= set(cs)
     
        nsfwpick = reddit.subreddit(", ".join(cs)).hot()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submission = next(x for x in nsfwpick if not x.stickied)
     
        embed = discord.Embed(title = submission.title ,color = random.choice(colors))

        embed.set_image(url = submission.url)  
        
        if str(ctx.channel) in channels:
            await ctx.send(embed = embed)
        else:
            await ctx.send(":exclamation: Wrong channel :exclamation:")
  
@client.command()  
async def dab(ctx):
  dabi_copy = dabi.copy()
  for n in [1]:
      cs = random.sample(dabi_copy , k=n)
      dabi_copy -= set(cs)
       
  embed = discord.Embed(color = random.choice(colors))
      
  embed.set_image(url = ", ".join(cs))
    
  await ctx.send(embed = embed)
  

@client.command()
async def civic(ctx):
  carcrash_copy = carcrash.copy()
  for n in [1]:
      cs = random.sample(carcrash_copy , k=n)
      carcrash_copy -= set(cs)
       
  embed = discord.Embed(color = random.choice(colors))
      
  embed.set_image(url = ", ".join(cs))
    
  await ctx.send(embed = embed)
  

    
@client.command()
async def wizijs(ctx):
  wiiiiiiiiizijs_copy = wiiiiiiiiizijs.copy()
  for n in [1]:
      cs = random.sample(wiiiiiiiiizijs_copy , k=n)
      wiiiiiiiiizijs_copy -= set(cs)
       
  embed = discord.Embed(title = 'WIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIZIJS XD')
      
  embed.set_image(url = ", ".join(cs))
    
  await ctx.send(embed = embed)
  
  

@client.event
async def on_member_join(user: discord.Member):
    channel = discord.utils.get(user.guild.channels, name="welcome")
    await channel.send("Hello {}".format(user.mention))
    role = discord.utils.get(user.guild.roles, name="guest")
    await user.add_roles(role)


role2 = "viesis"    

@client.event
async def on_member_join(member):
    role = get(member.server.roles, name=role2)
    await member.add_roles(role)   
   
@client.command()
async def stoopid(ctx):
    embed = discord.Embed(color = random.choice(colors))
    embed.set_image(url = "https://media1.tenor.com/images/76b4e35b06010302b771f0aef61db29e/tenor.gif?itemid=12783140")   
    await ctx.send(embed = embed) 

@client.command()
async def itis(ctx):
    await ctx.send("https://www.youtube.com/watch?v=KpXsfimrkFo&feature=youtu.be&t=5")      
    
@client.command()
async def pisies(ctx):
    embed = discord.Embed(color = random.choice(colors))
    embed.set_image(url = "https://i.imgur.com/xH9qksp.gif")   
    await ctx.send(embed = embed)  
    
@client.command()
async def hang(ctx):
    embed = discord.Embed(color = random.choice(colors))
    embed.set_image(url = "https://media1.tenor.com/images/90e0b360ad8620b005123076ca7e6aa9/tenor.gif?itemid=12409027")   
    await ctx.send(embed = embed)  

@client.command()
@has_permissions(manage_roles=True, ban_members=True)  
async def kick(ctx, members : commands.Greedy[discord.Member], *,reason=None):
    if not members:
      await ctx.send("** You need to name someone to kick **")
      return
    
    for member in members:
        if member == client.user:
            embed = discord.Embed(title = "You can't kick me, I'm an almighty client")
            await ctx.send(embed=embed)   
        else:
            await member.kick(reason=reason)

    
@kick.error
async def kick_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send("** You don't have permission to kick users! **")
 
@client.command()
@has_permissions(manage_roles=True, ban_members=True)  
async def ban(ctx, members : commands.Greedy[discord.Member], *,reason=None):
    if not members:
      await ctx.send("** You need to name someone to ban **")
      return
    
    for member in members:
        if member == client.user:
            embed = discord.Embed(title = "You can't ban me, I'm an almighty client")
            await ctx.send(embed=embed)   
        else:
            await member.ban(reason=reason)

    
@ban.error
async def ban_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send("** You don't have permission to ban users! **") 
 
@client.command()
@has_permissions(manage_roles=True, kick_members=True)
async def mute(ctx, members: commands.Greedy[discord.Member], mute_minutes: typing.Optional[int],*,reason: str = "none"):
    if not members:
        await ctx.send("** You need to name someone to mute **")
        return
    
    mute_role = discord.utils.get(ctx.guild.roles, name="Muted")
    
    for member in members:
        if client.user == member:
            embed = discord.Embed(title = "You can't mute me, I'm an almighty client")
            await ctx.send(embed=embed)
        else:
            await member.add_roles(mute_role, reason = reason)
            await ctx.send("{0.mention} has been muted by {1.mention} for **{2}**".format(member, ctx.author, reason))
    
    if mute_minutes > 0:
        await asyncio.sleep(mute_minutes * 60)
        for member in members:
            await member.remove_roles(mute_role)
            await ctx.send("{0.mention} time's up" .format(member))
 
@mute.error
async def mute_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send("** You don't have permission to mute users! **")
 
@client.command()
@commands.has_permissions(kick_members=True)
async def unmute(ctx, member: discord.Member=None):
    if not member:
        await ctx.send("You need to name someone to unmute")
        return
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.remove_roles(role)
    await ctx.send("{} has been unmuted by {}" .format(member.mention,ctx.author.mention))    
 
@client.command()
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in channel.history(limit=amount):
              messages.append(message)
    await channel.delete_messages(messages)
    
@client.command()
async def ziema(ctx):
    embed = discord.Embed(title='IET NAHUJ',color = random.choice(colors))
    embed.set_image(url = "https://media1.tenor.com/images/d130d7cf6763d5ccd8e3b6031149a897/tenor.gif?itemid=4710140")   
    await ctx.send(embed = embed)  
    
@client.command()
async def slap(ctx):
    embed = discord.Embed(color = random.choice(colors))
    embed.set_image(url = "https://media.giphy.com/media/UWEDYsbeVCHFCYwUsC/giphy.gif")   
    await ctx.send(embed = embed)   
    
@client.command()
async def pisaks(ctx):
    embed = discord.Embed(color = random.choice(colors))
    embed.set_image(url = "https://media1.tenor.com/images/54d3f822d3c1a25cf159915358ee3e11/tenor.gif?itemid=12718081")   
    await ctx.send(embed = embed)      
    
@client.command()
async def pranks(ctx):
    embed = discord.Embed(color = random.choice(colors))
    embed.set_image(url = "https://media1.tenor.com/images/2c292ec6e2de70d012d40213f0441bce/tenor.gif?itemid=5623249")   
    await ctx.send(embed = embed)      
	
    
@client.command()
async def say(ctx, *, mg = None):    
   await ctx.send(mg) 
   
@client.command()
async def mock(ctx,*, mg = None): 
    result_string = ""
    index = 0;
    for c in mg:
        if(index%2 == 0):
            result_string += c.lower()
        else:
            result_string += c.upper()
        index+=1
    await ctx.send(result_string)   
   
@client.command()
async def ping(ctx):
    await ctx.send(f':ping_pong: Pong! In {round(client.latency * 1000)}ms')

@client.command()  
async def ball(ctx,*, message):
  bumba_copy = bumba.copy()
  for n in [1]:
      cs = random.sample(bumba_copy , k=n)
      bumba_copy -= set(cs)
      await ctx.send(", ".join(cs))
      
      
      
@client.command()  
async def pisisuni(ctx):
  alfabets_copy = alfabets.copy()
  for n in [1]:
      cs = random.sample(alfabets_copy , k=n)
      alfabets_copy -= set(cs)
      await ctx.send(", ".join(cs))
      
@client.command()  
async def mad(ctx,*, message):
  viensdesmit_copy = viensdesmit.copy()
  for n in [1]:
      cs = random.sample(viensdesmit_copy , k=n)
      viensdesmit_copy -= set(cs)
      await ctx.send(", ".join(cs))	     

@client.command()
async def vissslikti(ctx):
    await ctx.send("Viss Labi :angel:")

@client.command()
async def fakti(ctx):
    await ctx.send(":regional_indicator_l: :regional_indicator_i: :regional_indicator_e: :regional_indicator_l: :regional_indicator_i:    :regional_indicator_f: :regional_indicator_a: :regional_indicator_k: :regional_indicator_t: :regional_indicator_i:")
	
@client.command()
async def mamma(ctx):
    await ctx.send("Nasasal! xD :joy:")

@client.command()
async def whodat(ctx, user: discord.Member):
    await ctx.send("The user {} is gay XDD".format(user.name))

@client.command()
async def pazors(ctx,*, message):
    await ctx.send("man par {} pazora būtu nosaukties".format(message))  
    
@client.command()
async def celies(ctx, user: discord.Member):
    await ctx.send("{}, Wake the FUCK UP! :joy:".format(user.mention),tts=True)  
    
@client.command()
async def vecit(ctx, user: discord.Member):
    await ctx.send("eu nu aizpis muti {}, sita catina iebliezt. es gaidij gaidij kadu huinu tu te vel uzrakstis. reali tev pa galvu vajadzetu iedot satiktu tev istaja dzive tiesam. neka personiga vecit ej atpusties, naksi no fake accountiem tpt baninu, neka personigi vecit bet nu sita dirst, nu cmon. nee nu viens te tads viens te tads te tads stipri divains, ilgi.. ilgi sists nav izskatas cilveks. lieta jau pa visam vienkars, ienakat izaicinat uz huin, nu ka huin i notikusi tad te visi gudri sak dirst, nu esam reali vechi. nu kka ta smiekligi nu. vinam ir loti sudiga geografija pat nemak atskirt kur ir imanta un piltene. vinam ir uzmanibas trukuma deficits un tamlidzigi ja".format(user.mention))       
   
@client.event
async def on_message(message):
    global messages
    messages += 1
    id = client.get_guild(215848568064311296)
    bad_words = [".say", ".vecit", ".celies", ".mock"]

    for word in bad_words:
        if message.content.count(word) > 0 and message.content.count(word) < 100:
            print("repeating command deleted!")
            await message.channel.purge(limit=1)    
    await client.process_commands(message)    

@client.command()
async def commands(ctx):
    embed = discord.Embed(title='Lil Boc',color = 0XFF0000)
 
    embed.add_field(name=".dab", value="dab", inline=True)
    embed.add_field(name=".adab", value="Anime Dab", inline=True)  
    embed.add_field(name=".dmeme", value="Dark Meme", inline=True)
    embed.add_field(name=".meme", value="MEME", inline=True)       
    embed.add_field(name=".civic", value="Nolocīts", inline=True)
    embed.add_field(name=".wizijs", value="Dumb", inline=True)   
    embed.add_field(name=".say", value="Repeat Message", inline=True)   
    embed.add_field(name=".ziema", value="FUCK ZIEMU", inline=True) 
    embed.add_field(name=".stoopid", value="Dumbdurumdum", inline=True)  
    embed.add_field(name=".slap", value="Slap That Bitch", inline=True)  
    embed.add_field(name=".pranks", value="Get Pranked", inline=True)
    embed.add_field(name=".pisaks", value="3hunna Combo", inline=True)
    embed.add_field(name=".fakti", value="Lieli Fakti", inline=True)
    embed.add_field(name=".pazors", value="Paazors ble", inline=True)
    embed.add_field(name=".whodat", value="Gay", inline=True)
    embed.add_field(name=".celies", value="HALLO", inline=True)
    embed.add_field(name=".vecit", value="Labs teksts", inline=True)
    embed.add_field(name=".mock", value="Mock's Your Text", inline=True)      
    embed.add_field(name=".mamma", value="Nasasal XD", inline=True)
    embed.add_field(name=".pisisuni", value="PAC", inline=True)
    embed.add_field(name=".clear", value="clear messages", inline=True)
    embed.add_field(name=".mute", value=".mute {user} {time(optional)} {reason}", inline=True)
    embed.add_field(name=".unmute", value=".unmute {user}", inline=True)
    embed.add_field(name=".vissslikti", value="VissLabi", inline=True)
    embed.add_field(name=".nsfw", value="NSFW", inline=True)      
    embed.add_field(name=".hang", value="KYS", inline=True)
    embed.add_field(name=".pisies", value="Pisies", inline=True)
    embed.add_field(name=".itis", value="It is what it is", inline=True)
    embed.add_field(name=".ping", value="Pong", inline=True)
    
    
    embed.set_footer(text=ctx.author.name, icon_url = ctx.author.avatar_url)
    await ctx.send(embed=embed)        
    
client.run(os.environ['dkey'])
         