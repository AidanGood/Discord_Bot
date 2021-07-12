# Gamer Dad Bot
import os
import discord
from dotenv import load_dotenv
import random
import time
import asyncio

load_dotenv()

client = discord.Client()

dad_jokes = ["I\'m afraid for the calendar. Its days are numbered.",
             "Owls have horns",
             "We should emulate the french more, down with the presidency!",
             "Singing in the shower is fun until you get soap in your mouth. Then it's a soap opera.",
             "How do you follow Will Smith in the snow? You follow the fresh prints.",
             "What did the ocean say to the beach? Nothing, it just waved.",
             "I only know 25 letters of the alphabet. I don't know y.",
             "What did one wall say to the other? I'll meet you at the corner.",
             "What did the zero say to the eight? That belt looks good on you.",
             "I asked my dog what's two minus two. He said nothing.",
             "Want to know why nurses like red crayons? Sometimes they have to draw blood.",
             "What would the Terminator be called in his retirement? The Exterminator.",
             "My wife asked me to go get 6 cans of Sprite from the grocery store. I realized when I got home that I had picked 7 up.",
             "What’s the most detail-oriented ocean? The Pacific.",
             "Did you hear about the kidnapping at school? It’s fine, he woke up."]

good_mornings = ["https://tenor.com/view/good-morning-jules-dogs-run-fat-pugs-gif-12882778",
                 "https://tenor.com/view/kisses-pugs-cute-dogs-good-morning-gif-12772901",
                 "https://tenor.com/view/good-morning-jules-pugs-and-money-rich-make-it-rain-funny-animals-gif-12922098",
                 "https://tenor.com/view/bacon-pug-hop-dogs-cute-gif-13564097",
                 "https://tenor.com/view/pug-toilet-trap-good-morning-jules-gif-12863777"
                 ]

''' E-sports food channel ID: 754131940243931199 
    Test server food channel ID: 846089092281401354,
    Cole's ID: 223820544909246464
    Pet channel ID: 781689646883012609
    '''
global cooldown
cooldown = 0


async def background_task():
    global cooldown
    await client.wait_until_ready()

    while not client.is_closed():
        try:
            gmt = time.gmtime()  # NOTE: GMT time zone
            if {gmt.tm_hour, gmt.tm_min} == {8, 20}:  # Bison Time is 8:20 GMT
                if gmt.tm_min == 20:
                    if gmt.tm_hour == 8:
                        response = "Bison Time!"
                        channel = client.get_channel(754131940243931199)
                        await channel.send(response)
            await asyncio.sleep(1)
            cooldown = 0
        except Exception as e:
            print(str(e))
            await asyncio.sleep(5)


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    global cooldown
    if cooldown == 1:
        return

    if message.author == client.user:
        return

    # "Commands"
    if message.content.startswith("d!joke"):
        random_index = random.randint(0, len(dad_jokes) - 1)
        response = dad_jokes[random_index]
        await message.channel.send(response)

    if message.content.startswith("d!help"):
        response = "Type `d!help` to see a list of words that I will respond to!"
        await message.channel.send(response)

    if message.content.startswith("d!version"):
        response = "I am Gamer Dad Bot running dadBot V1.1.7"
        await message.channel.send(response)

    if message.content.startswith("d!advice"):
        if message.author.id == 402538937631113227:
            response = ""
            await message.channel.send(response)

    message_list = message.content.split()
    if "walter" in message_list:
        # if message.author.id == 402538937631113227:
        # channel = client.get_channel(781689646883012609)

        response = "Sorry, no can do kiddo"
        await message.channel.send(response)

    if "morning" in message_list and "jules" in message_list:
        random_index = random.randint(0, len(good_mornings) - 1)
        response = good_mornings[random_index]
        await message.channel.send(response)

    if "bison" in message.content.lower():
        if message.channel.name == "food":
            gmt = time.gmtime()  # NOTE: GMT time zone
            if {gmt.tm_hour, gmt.tm_min} == {8, 20}:  # Bison Time is 8:20 GMT
                if gmt.tm_min == 20:
                    if gmt.tm_hour == 8:
                        response = "Bison Time!"
                        channel = client.get_channel(754131940243931199)
                        await channel.send(response)

    # Misc
    if "shut" in message_list:
        if "up" in message_list:
            person = str(message.author.display_name)
            response = f"Hey {person}, that wasn\'t very nice, so please apologize to the whole server and then take your own advice and \"shut the \*\*\*\* up\"."
            await message.channel.send(response)
    elif "stfu" in message_list:
        person = str(message.author.display_name)
        response = f"Hey {person}, that wasn\'t very nice, so please apologize to the whole server and then take your own advice and \"shut the \*\*\*\* up\"."
        await message.channel.send(response)
    elif "play" in message_list:
        response = "Are ya winning son?"
        await message.channel.send(response)
    # elif "owl" in message.content.lower():
    #     response = "Did you know that the Great Horned Owl doesn't actually have horns?"
    #     await message.channel.send(response)
    elif "lost" in message_list:
        response = "Don't worry, I'm sure you will do better next time."
        await message.channel.send(response)
    elif "jyro" in message_list:
        if "president" in message_list:
            response = "Not my president"
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
        elif "i am dad" in message.content.lower():
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
        elif "thanks dad" in message.content.lower():
            response = "No problem!"
            await message.channel.send(response)
        elif "dad bot best bot" in message.content.lower():
            person = str(message.author.display_name)
            response = f"{person} best person"
            await message.channel.send(response)
        else:
            rand_int = random.random()
            if rand_int > 0.90:
                response = "Someone mention me?"
                await message.channel.send(response)

    # Infamous "Hi __ , I'm Dad!"

    else:
        if "im" in message_list:
            new_message = message.content[message.content.find("im") + 2:]
            await message.channel.send(f"Hi{new_message}, I'm Dad!")

        elif "Im" in message_list:
            new_message = message.content[message.content.find("Im") + 2:]
            await message.channel.send(f"Hi{new_message}, I'm Dad!")

        elif "i'm" in message_list:
            new_message = message.content[message.content.find("i'm") + 3:]
            await message.channel.send(f"Hi{new_message}, I'm Dad!")

        elif "I'm" in message_list:
            new_message = message.content[message.content.find("I'm") + 3:]
            await message.channel.send(f"Hi{new_message}, I'm Dad!")

        elif "i am" in message_list:
            new_message = message.content[message.content.find("i am") + 4:]
            await message.channel.send(f"Hi{new_message}, I'm Dad!")

        elif "I am" in message_list:
            new_message = message.content[message.content.find("I am") + 4:]
            await message.channel.send(f"Hi{new_message}, I'm Dad!")

        elif "lm" in message_list:
            new_message = message.content[message.content.find("lm") + 2:]
            await message.channel.send(f"Hi{new_message}, I'm Dad!")



# client.loop.create_task(background_task())
client.run(os.getenv('DISCORD_TOKEN'))
