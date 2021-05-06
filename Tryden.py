import discord
from discord.ext import commands
from discord import guild
import json
import os
import asyncio
import datetime
import random
random.seed

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="+",
					intents=intents)
####################################
@bot.event
async def on_ready():
	bot.loop.create_task(status_task())
	print("Main-Datei geladen")
###################################
@bot.event
async def on_connect():
	print(f"Ich ({bot.user.name}) bin jetzt online Time : {datetime.datetime.now().strftime('%H:%M')}")
###################################
@bot.event
async def on_disconnect():
	print(f"Ich ({bot.user.name}) bin jetzt offine Time : {datetime.datetime.now().strftime('%H:%M')}")
###################################
@bot.event
async def on_member_join(member):
	print("Willkommensnachricht wurde gesendet")
	print(f"{member.name} ist dem Server {guild.name}") 
	if not member.bot:
		welcome = discord.Embed(title=f"Welcome to {guild.name} {member.name}",
								description="You did it.",
								color=discord.colour.Colour.dark_gold())
		welcome.set_footer(text="Tryden | by GC | The RedCrafter and T-Phase | GLaDOS")
		try:
			await member.send(embed=welcome)
		except discord.errors.Forbidden:
			print("Es konnte keine Willkommensnachricht geschickt werden")
####################################
if __name__ == '__main__':
	for filename in os.listdir("./Cogs"):
		if filename.endswith(".py") and not filename.startswith("_"):
			bot.load_extension(f"Cogs.{filename[:-3]}")
###################################
async def status_task():
	while True:
		await bot.change_presence(activity=discord.Game("type +help for help"), status=discord.Status.online)
		await asyncio.sleep(15)
		await bot.change_presence(activity=discord.Game("made by GC | The RedCrafter and T-Phase | GLaDOS"), status=discord.Status.online)
		await asyncio.sleep(15)
###################################
bot.run("#ZESURED#")
