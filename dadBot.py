# Gamer Dad Bot
import os
import discord
from dotenv import load_dotenv
import random
import time
import asyncio

load_dotenv()

client = discord.Client()

dad_jokes = ["I\'m afraid for the calendar. Its days are numbered.", "OSU players need hand therapy", "Owls have horns",
             "You can game on a Mac", "The Fortnite Team Captain is really cool", "We should emulate the french more, down with the presidency!",
             "Singing in the shower is fun until you get soap in your mouth. Then it's a soap opera.", "How do you follow Will Smith in the snow?" "You follow the fresh prints.",
             "What did the ocean say to the beach?" "Nothing, it just waved.", "I only know 25 letters of the alphabet. I don't know y."]

''' E-sports food channel ID: 754131940243931199 
    Test server food channel ID: 846089092281401354
    Cole's ID: 223820544909246464
    '''


async def background_task():
    await client.wait_until_ready()

    while not client.is_closed():
        try:
            gmt = time.gmtime()     # NOTE: GMT time zone
            if {gmt.tm_hour, gmt.tm_min, gmt.tm_sec} == {8, 20, 0}:  # Bison Time is 8:20 GMT
                if gmt.tm_min == 20:
                    response = "It's Bison Time!"
                    channel = client.get_channel(754131940243931199)
                    await channel.send(response)
            await asyncio.sleep(1)
        except Exception as e:
            print(str(e))
            await asyncio.sleep(5)


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # "Commands"
    if message.content.startswith("d!joke"):
        response = random.choice(dad_jokes)
        await message.channel.send(response)

    # Misc
    if "shut up" in message.content.lower():
        person = str(message.author.display_name)
        response = f"Hey {person}, that wasn\'t very nice, so please apologize to the whole serve and then \
                    take your own advice and \"shut the **** up\"."
        await message.channel.send(response)
    elif "play" in message.content.lower():
        response = "Are ya winning son?"
        await message.channel.send(response)
    elif "owl" in message.content.lower():
        response = "Did you know that the Great Horned Owl doesn't actually have horns?"
        await message.channel.send(response)
    elif "lost" in message.content.lower():
        response = "Don't worry, I'm sure you will do better next time."
        await message.channel.send(response)
    elif "jyro" in message.content.lower():
        if "president" in message.content.lower():
            response = "Someday I will overthrow this government..."
        else:
            response = "That's Mr. Club President Jyro to you!"
        await message.channel.send(response)

    # Dad specific Responses
    elif "dad" in message.content.lower():
        # Defending being the only dad
        if "im dad" in message.content.lower():
            person = str(message.author.display_name)
            response = f"No you're {person}, I'm Dad!"
            await message.channel.send(response)
        elif "i'm dad" in message.content.lower():
            person = str(message.author.display_name)
            response = f"No you're {person}, I'm Dad!"
            await message.channel.send(response)
        # Respond to a hello
        elif "hi dad" in message.content.lower():
            person = str(message.author.display_name)
            response = f"Hi {person}, have a good day!"
            await message.channel.send(response)
        elif "hello dad" in message.content.lower():
            person = str(message.author.display_name)
            response = f"Hello {person}, keep up the great work!"
            await message.channel.send(response)
        else:
            response = "Someone mention me?"
            await message.channel.send(response)

    # Infamous "Hi __ , I'm Dad!"
    else:
        if "im" in message.content:
            new_message = message.content[message.content.find("im") + 3:]
            await message.channel.send(f"Hi {new_message}, I'm Dad!")

        elif "Im" in message.content:
            new_message = message.content[message.content.find("Im") + 3:]
            await message.channel.send(f"Hi {new_message}, I'm Dad!")

        elif "i'm" in message.content:
            new_message = message.content[message.content.find("i'm") + 4:]
            await message.channel.send(f"Hi {new_message}, I'm Dad!")

        elif "I'm" in message.content:
            new_message = message.content[message.content.find("I'm") + 4:]
            await message.channel.send(f"Hi {new_message}, I'm Dad!")

        elif "i am" in message.content:
            new_message = message.content[message.content.find("i am") + 5:]
            await message.channel.send(f"Hi {new_message}, I'm Dad!")

        elif "I am" in message.content:
            new_message = message.content[message.content.find("I am") + 5:]
            await message.channel.send(f"Hi {new_message}, I'm Dad!")

        elif "lm" in message.content:
            new_message = message.content[message.content.find("lm") + 3:]
            await message.channel.send(f"Hi {new_message}, I'm Dad!")


client.loop.create_task(background_task())
client.run(os.getenv('DISCORD_TOKEN'))
