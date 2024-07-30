import discord
from model import get_class
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{file_name}")
            await ctx.send(f"Imagen guardada en ./{file_url}")
            try:
                clase = get_class(model_path = "keras_model.h5", labels_path = "labels.txt", image_path = f"./{file_name}"  )
                if clase[0] == "Palomas":
                    await ctx.send("Es posiblemente una paloma paloma, pueden comer todo tipo de granos como trigo")
                elif clase[0] == "Gorriones":
                    await ctx.send("Es posiblemente un gorrión, pueden comer todo tipo de granos como arroz")
            except:
                await ctx.send("No se pudo identificar la imagen")
    else:
        await ctx.send("No subiste una imagen :(")

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run("TOKEN")