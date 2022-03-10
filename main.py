import discord
from discord.ext import commands
import asyncio
import random

bot = commands.Bot(command_prefix="!", description="Bot Q")


# Information server discord
@bot.event
async def on_ready():
    print("Ready !")


@bot.command()
async def coucou(ctx):
    await ctx.send("Coucou !")


@bot.command()
async def serverInfo(ctx):
    server = ctx.guild
    numberOfTextChannels = len(server.text_channels)
    numberOfVoiceChannels = len(server.voice_channels)
    serverDescription = server.description
    numberOfPerson = server.member_count
    serverName = server.name
    message = f"Le serveur **{serverName}** contient *{numberOfPerson}* personnes ! \nLa description du serveur est {serverDescription}. \nCe serveur possède {numberOfTextChannels} salons écrit et {numberOfVoiceChannels} salon vocaux."
    await ctx.send(message)


# Commande !bonjour
@bot.event
async def on_ready():
    print("Ready !")


@bot.command()
async def bonjour(ctx):
    server = ctx.guild
    serverName = server.name
    await ctx.send(
        f"Bonjour jeune *padawan* ! Savais tu que tu te trouvais dans le serveur *{serverName}*, c'est d'ailleurs un super serveur puisque **JE** suis dedans.")


# Commande base !chinese !say
@bot.event
async def on_ready():
    print("Ready !")


@bot.command()
async def say(ctx, *text):
    await ctx.send(" ".join(text))


@bot.command()
async def getInfo(ctx, info):
    server = ctx.guild
    if info == "memberCount":
        await ctx.send(server.member_count)
    elif info == "numberOfChannel":
        await ctx.send(len(server.voice_channels) + len(server.text_channels))
    elif info == "name":
        await ctx.send(server.name)
    else:
        await ctx.send("Etrange... Je ne connais pas cela")


@bot.command()
async def chinese(ctx, *text):
    chineseChar = "丹书匚刀巳下呂廾工丿片乚爪冂口尸Q尺丂丁凵V山乂Y乙"
    chineseText = []
    for word in text:
        for char in word:
            if char.isalpha():
                index = ord(char) - ord("a")
                transformed = chineseChar[index]
                chineseText.append(transformed)
            else:
                chineseText.append(char)
        chineseText.append(" ")
    await ctx.send("".join(chineseText))


# Commande !roulette  La roulette Russe
@bot.event
async def on_ready():
    print("Ready !")


@bot.event
async def on_ready():
    print("Ready !")


@bot.command()
async def roulette(ctx):
    await ctx.send("La roulette commencera dans 10 secondes. Envoyez \"moi\" dans ce channel pour y participer.")

    players = []

    def check(message):
        return message.channel == ctx.message.channel and message.author not in players and message.content == "moi"

    try:
        while True:
            participation = await bot.wait_for('message', timeout=10, check=check)
            players.append(participation.author)
            print("Nouveau participant : ")
            print(participation)
            await ctx.send(f"**{participation.author.name}** participe au tirage ! Le tirage commence dans 10 secondes")
    except:  # Timeout
        print("Demarrage du tirrage")

    gagner = ["ban", "kick", "role personnel", "mute", "gage"]

    await ctx.send("Le tirage va commencer dans 3...")
    await asyncio.sleep(1)
    await ctx.send("2")
    await asyncio.sleep(1)
    await ctx.send("1")
    await asyncio.sleep(1)
    loser = random.choice(players)
    price = random.choice(gagner)
    await ctx.send(f"La personne qui a gagnée un {price} est...")
    await asyncio.sleep(1)
    await ctx.send("**" + loser.name + "**" + " !")


# List utilisateur banni
@bot.event
async def on_ready():
    print("Ready !")


@bot.command()
async def bansId(ctx):
    ids = []
    bans = await ctx.guild.bans()
    for i in bans:
        ids.append(str(i.user.id))
    await ctx.send("La liste des id des utilisateurs bannis du serveur est :")
    await ctx.send("\n".join(ids))


# Administration
@bot.event
async def on_ready():
    print("Ready !")


# Commande !ban
@bot.command()
async def ban(ctx, user: discord.User, *reason):
    reason = " ".join(reason)
    await ctx.guild.ban(user, reason=reason)
    await ctx.send(f"{user} à été ban pour la raison suivante : {reason}.")


# commande !unban
@bot.command()
async def unban(ctx, user, *reason):
    reason = " ".join(reason)
    userName, userId = user.split("#")
    bannedUsers = await ctx.guild.bans()
    for i in bannedUsers:
        if i.user.name == userName and i.user.discriminator == userId:
            await ctx.guild.unban(i.user, reason=reason)
            await ctx.send(f"{user} à été unban.")
            return
    # Ici on sait que lutilisateur na pas ete trouvé
    await ctx.send(f"L'utilisateur {user} n'est pas dans la liste des bans")


# Commande !kick
@bot.command()
async def kick(ctx, user: discord.User, *reason):
    reason = " ".join(reason)
    await ctx.guild.kick(user, reason=reason)
    await ctx.send(f"{user} à été kick.")


# Commande !clear message
@bot.command()
async def clear(ctx, nombre: int):
    messages = await ctx.channel.history(limit=nombre + 1).flatten()
    for message in messages:
        await message.delete()


bot.run(
    "OTM1ODI2NDM0NzU1MjcyNzU1.YfESSA.BiFXUgY_TSVSRPgBajGpsuMg3NY")  # Ceci est le token de mon bot. Changez le avec celui de votre bot
