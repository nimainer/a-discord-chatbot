import discord
import random

#made by nima the code are also can be find at discord.py if you need more information

client = discord.Client()


@client.event
async def on_message(message):
    message.content.lower()
    if message.author.bot:
        return
    if message.content.lower().startswith("hello"):
        await message.channel.send("Hi")

    if message.content.lower().startswith("who is"):
        await message.channel.send("nima#3663 made me")

    if message.content.lower().startswith("hi"):
        await message.channel.send("Hey")

    if message.content.lower().startswith("hey"):
        await message.channel.send("Hi")

    if message.content.lower().startswith("anime"):
        await message.channel.send("wanna watch some anime ?")

    if message.content.lower().startswith("how are you"):
        await message.channel.send("im doing well how are you ?")

    if message.content.lower().startswith("thank you"):
        await message.channel.send("your welcome")

    if message.content.startswith("math"):
        await message.channel.send("i love math")
    else:
        if message.content.startswith("Math"):
            await message.channel.send("i hate math")

        if message.content.startswith("help"):
            await message.channel.send("do you really need help ?")
        elif message.content.startswith("Help"):
            await message.channel.send("uhh i dont think you need help.")
        elif message.content.startswith("HELP"):
            await message.channel.send("oh so you do need help but sorry im a robot i can't help !")

    if message.content.lower().startswith("cya"):
        await message.channel.send("bye")
    elif message.content.lower().startswith("goodbye"):
        await message.channel.send("bye")
    elif message.content.lower().startswith("good bye"):
        await message.channel.send("cya")

    if message.content.lower().startswith("lol"):
        await message.channel.send("what so funny ?")

    if message.content.lower().startswith("hm"):
        await message.channel.send("why are you hmmmm-ing ?")

    if message.content.lower().startswith("anyone know a good movie"):
        await message.channel.send("have you watched spiderman it a good movie!")

    if message.content.lower().startswith("what's a good game to play?"):
        await message.channel.send("you should try minecraft its a really fun game !!!!")

    if message.content.lower().startswith("what food should i eat?"):
        msg = random.choice(
            ["pizza", "chicken nuget", "potato !", "chicken", "egg", "ham?", "idk search it on internet", "steak",
             "mug cake", "soup"])
        await message.channel.send(msg)

    if message.content.lower().startswith("what should i eat?"):
        msg = random.choice(["pizza", "chicken nuget", "potato !", "chicken", "egg", "ham?", "idk search it on internet", "steak",
             "mug cake", "soup"])
        await message.channel.send(msg)


client.run("you bot id here ")





client.run("NzY0NTM0NTk2NzQ5NjIzMzQ2.X4HqVA.pkUi4RUBGrnnfKJC3qxcdOjfjpQ")