import discord
from discord.ext import commands
import requests
import keep_alive
import os
import asyncio
import time
client = commands.Bot(command_prefix = "!")

startTime = time.time()
total_seconds = 0
minutes = 0
hours = 0
@client.event
async def on_ready():
    print("Online and Ready")
    status = discord.Activity(type=discord.ActivityType.watching, name="!help | made by mistxbrain#1234")
    await client.change_presence(activity=status)


@client.command()
async def say(ctx, *, arg):
  await ctx.message.delete()
  await ctx.send(arg)

@client.command()
async def extract(ctx, *, arg):
  embed = discord.Embed(title="Extract", color=0x00ff00)
  embed.set_image(url=f"https://benbotfn.tk/api/v1/exportAsset?path={arg}&lang=en&noVariants=false&rawIcon=false")
  embed.set_footer(text="Made by mistxbrain#1234")
  await ctx.send(embed=embed)

@client.command()
async def icon(ctx, *, arg):
  data = requests.get(f"https://benbotfn.tk/api/v1/cosmetics/br/search/all?name={arg}&matchMethod=starts").json()
  if data == []:
    embed = discord.Embed(color=0xFF0000)
    embed.add_field(name="Error", value="Please enter a valid cosmetic.", inline=False)
  else:
    embed = discord.Embed(title=data[0]["name"], color=0x00ff00)
    embed.set_image(url=f"https://benbotfn.tk/api/v1/exportAsset?path={data[0]['path']}&lang=en&noVariants=false&rawIcon=false")
  embed.set_footer(text="Made by mistxbrain#1234")
  await ctx.send(embed=embed)
  

@client.command()
async def ping(ctx):
    await ctx.send(client.latency)

@client.command()
async def cosmetic(ctx, *, arg):
    data = requests.get(f"https://benbotfn.tk/api/v1/cosmetics/br/search/all?name={arg}&matchMethod=contains").json()
    if data == []:
        embed = discord.Embed(color=0xFF0000)
        embed.add_field(name="Error", value="Please enter a valid skin.", inline=False)
        embed.set_footer(text="Made by mistxbrain#1234")
        await ctx.send(embed=embed)
    else:
        if data[0]["variants"]:
            channel = data[0]["variants"][0]["channel"]
        else:
            channel = None
        if len(data) != 1:
          embed = discord.Embed(title="Please choose one.", color=0x00ff00)
          a = 0
          for x in data:
            a += 1
            embed.add_field(name=str(a) + ". " + x["name"], value=x["id"], inline=False)
          embed.set_footer(text="Made by mistxbrain#1234")
          await ctx.send(embed=embed)
          
          def check(m):
            
            return m.content.isdigit() and m.channel == ctx.channel and m.author == ctx.author
          try:
            value = await client.wait_for('message', check=check, timeout=20)
            value = int(value.content) - 1
            name = data[value]["name"]
            embed = discord.Embed(title=name, description=data[value]["description"], color=0x00ff00)
            embed.add_field(name="ID", value=data[value]["id"], inline=False)
            embed.add_field(name="Rarity", value=data[value]["rarity"], inline=False)
            embed.add_field(name="Variants", value=channel, inline=False)
            embed.add_field(name="BackendType", value=data[value]["backendType"], inline=False)
            embed.add_field(name="Path", value=data[value]["path"], inline=False)
            embed.set_thumbnail(url=data[value]["icons"]["icon"])
            embed.set_footer(text="Made by mistxbrain#1234")
            await ctx.send(embed=embed)
          except asyncio.exceptions.TimeoutError:
            await ctx.send("You took to long to reply")
          except:
            ctx.send("You entered an invalid response.")
        else:
          value = 0
          name = data[value]["name"]
          embed = discord.Embed(title=name, description=data[value]["description"], color=0x00ff00)
          embed.add_field(name="ID", value=data[value]["id"], inline=False)
          embed.add_field(name="Rarity", value=data[value]["rarity"], inline=False)
          embed.add_field(name="Variants", value=channel, inline=False)
          embed.add_field(name="BackendType", value=data[value]["backendType"], inline=False)
          embed.add_field(name="Path", value=data[value]["path"], inline=False)
          embed.set_thumbnail(url=data[value]["icons"]["icon"])
          embed.set_footer(text="Made by mistxbrain#1234")
          await ctx.send(embed=embed)

@client.command()
async def skin(ctx, *, arg):
    data = requests.get(f"https://benbotfn.tk/api/v1/cosmetics/br/search/all?name={arg}&matchMethod=contains&backendType=AthenaCharacter").json()
    if data == []:
        embed = discord.Embed(color=0xFF0000)
        embed.add_field(name="Error", value="Please enter a valid skin.", inline=False)
        embed.set_footer(text="Made by mistxbrain#1234")
        await ctx.send(embed=embed)
    else:
        if data[0]["variants"]:
            channel = data[0]["variants"][0]["channel"]
        else:
            channel = None
        if len(data) != 1:
          embed = discord.Embed(title="Please choose one.", color=0x00ff00)
          a = 0
          for x in data:
            a += 1
            embed.add_field(name=str(a) + ". " + x["name"], value=x["id"], inline=False)
          embed.set_footer(text="Made by mistxbrain#1234")
          await ctx.send(embed=embed)
          
          def check(m):
            
            return m.content.isdigit() and m.channel == ctx.channel and m.author == ctx.author
          try:
            value = await client.wait_for('message', check=check, timeout=20)
            value = int(value.content) - 1
            name = data[value]["name"]
            embed = discord.Embed(title=name, description=data[value]["description"], color=0x00ff00)
            embed.add_field(name="ID", value=data[value]["id"], inline=False)
            embed.add_field(name="Rarity", value=data[value]["rarity"], inline=False)
            embed.add_field(name="Variants", value=channel, inline=False)
            embed.add_field(name="BackendType", value=data[value]["backendType"], inline=False)
            embed.add_field(name="Path", value=data[value]["path"], inline=False)
            embed.set_thumbnail(url=data[value]["icons"]["icon"])
            embed.set_footer(text="Made by mistxbrain#1234")
            await ctx.send(embed=embed)
          except asyncio.exceptions.TimeoutError:
            await ctx.send("You took to long to reply")
          except:
            await ctx.send("You entered an invalid response.")
        else:
          value = 0
          name = data[value]["name"]
          embed = discord.Embed(title=name, description=data[value]["description"], color=0x00ff00)
          embed.add_field(name="ID", value=data[value]["id"], inline=False)
          embed.add_field(name="Rarity", value=data[value]["rarity"], inline=False)
          embed.add_field(name="Variants", value=channel, inline=False)
          embed.add_field(name="BackendType", value=data[value]["backendType"], inline=False)
          embed.add_field(name="Path", value=data[value]["path"], inline=False)
          embed.set_thumbnail(url=data[value]["icons"]["icon"])
          embed.set_footer(text="Made by mistxbrain#1234")
          await ctx.send(embed=embed)

@client.command()
async def uptime(ctx):
  embed = discord.Embed(title="Uptime", color=0x00ff00)
  total_seconds = int(time.time() - startTime)
  minutes = int(total_seconds/60)
  hours = int(minutes/60)
  if minutes > 0:
    total_seconds = total_seconds - minutes*60
  if hours > 0:
    minutes = minutes - hours*60
  embed.add_field(name="Hours:", value=hours)
  embed.add_field(name="Minutes:", value=minutes)
  embed.add_field(name="Seconds:", value=total_seconds)
  embed.set_footer(text="Made by mistxbrain#1234")
  await ctx.send(embed=embed)


@client.command()
async def news(ctx):
    data = requests.get("https://fortnite-api.com/v2/news").json()
    embed = discord.Embed(title="News", color=0x00ff00)
    embed.set_image(url=data["data"]["br"]["image"])
    embed.set_footer(text="Made by mistxbrain#1234")
    await ctx.send(embed=embed)

@client.command()
async def invite(ctx):
  embed = discord.Embed(title="Invite", description="Click [here](https://www.youtube.com/watch?v=dQw4w9WgXcQ) to invite this bot to your Discord.", color=0x00ff00)
  msg = await ctx.send(embed=embed)
  await asyncio.sleep(10)
  embed = discord.Embed(title="Hah", color=0x00ff00)
  embed.set_image(url="https://media.tenor.com/images/5b61a360d83b8fccc05f5060b048c6e1/tenor.gif")
  embed.set_footer(text="Made by mistxbrain#1234")
  await msg.edit(embed=embed)

@client.command()
async def aes(ctx):
  try:
    data = requests.get("https://benbotfn.tk/api/v1/aes").json()
    embed = discord.Embed(title="AES Keys", description=f"Version: {data['version']}", color=0x00ff00)
    embed.add_field(name="1", value="Main")
    d = 1
    keylist = {}
    for x in data["dynamicKeys"]:
      d += 1
      keylist.update({d: x})
      embed.add_field(name=d, value=x, inline=False)
    await ctx.send(embed=embed)
    def check(m):
      return m.content.isdigit() and m.channel == ctx.channel and m.author == ctx.author
    value = await client.wait_for('message', check=check, timeout=20)
    if int(value.content) == 1:
      embed.set_footer(text="Made by mistxbrain#1234")
      await ctx.send(data["mainKey"])
    else:
      location = keylist[int(value.content)]
      embed.set_footer(text="Made by mistxbrain#1234")
      await ctx.send(data["dynamicKeys"][location])
  except asyncio.exceptions.TimeoutError:
    await ctx.send("You took too long.")
  except:
    await ctx.send("Please enter a valid option.")

@client.command()
async def new(ctx):
  data = requests.get("https://benbotfn.tk/api/v1/newCosmetics").json()["items"]
  embed = discord.Embed(title="New Cosmetics", color=0x00ff00)
  wraps = ""
  skins = ""
  sprays = ""
  contrails = ""
  emotes = ""
  pickaxe = ""
  backpacks = ""
  for x in data:
    if x["backendType"] == "AthenaSpray":
      sprays = sprays + x["name"] + "\n"
    elif x["backendType"] == "AthenaCharacter":
      skins = skins + x["name"] + "\n"
    elif x["backendType"] == "AthenaSkyDiveContrail":
      contrails = contrails + x["name"] + "\n"
    elif x["backendType"] == "AthenaItemWrap":
      wraps = wraps + x["name"] + "\n"
    elif x["backendType"] == "AthenaDance":
      emotes = emotes + x["name"] + "\n"
    elif x["backendType"] == "AthenaPickaxe":
      pickaxe = pickaxe + x["name"] + "\n"
    elif x["backendType"] == "AthenaBackpack":
      backpacks = backpacks + x["name"] + "\n"
  if contrails == "":
    contrails = "None"
  if sprays == "":
    sprays = "None"
  if skins == "":
    skins = "None"
  if wraps == "":
    wraps = "None"
  if emotes == "":
    emotes = "None"
  if pickaxe == "":
    pickaxe = "None"
  if backpacks == "":
    backpacks = "None"
  embed.add_field(name="Skins", value=skins)
  embed.add_field(name="Emotes", value=emotes)
  embed.add_field(name="Pickaxes", value=pickaxe)
  embed.add_field(name="Backpacks", value=backpacks)
  embed.add_field(name="Sprays", value=sprays)
  embed.add_field(name="Contrails", value=contrails)
  embed.add_field(name="Wraps", value=wraps)
  embed.set_footer(text="Made by mistxbrain#1234")
  await ctx.send(embed=embed)

@client.command()
async def find(ctx, *, arg):
  data = requests.get(f"https://fortnite-api.com/v2/cosmetics/br/{arg}").json()
  data = data["data"]
  embed = discord.Embed(title=data["name"], description=data["description"], color=0x00ff00)
  embed.add_field(name="ID", value=data["id"], inline=False)
  embed.add_field(name="Rarity", value=data["rarity"]["displayValue"], inline=False)
  embed.add_field(name="Variants", value=data["variants"][0]["channel"], inline=False)
  embed.add_field(name="BackendType", value=data["type"]["backendValue"], inline=False)
  embed.add_field(name="Path", value=data["path"])
  embed.set_thumbnail(url=data["images"]["icon"])
  embed.set_footer(text="Made by mistxbrain#1234")
  await ctx.send(embed=embed)

@client.command()
async def map(ctx):
  embed = discord.Embed(title="Map", color=0x00ff00)
  embed.set_image(url="https://cbn.media.fortniteapi.io/images/map.png")
  await ctx.send(embed=embed)

@client.command()
async def rules(ctx):
  await ctx.message.delete()
  embed = discord.Embed(color=0x00ff00)
  embed.add_field(name="Rules:", value="1. Be respectful to other server members (no homophobia, racism, etc).\n2. No NSFW content.\n3. No excessive swearing.\n4. Do not advertise.\n5. No ghost pings.\n6. Use each channel for their purposes.\n7. No hate/spam.\n8. Don't ping any of the owners unless it is necessary.")
  embed.set_footer(text="By being a member of this discord you agree to all of these rules. If you fail to do so you it will result in consequences.")
  await ctx.send(embed=embed)


keep_alive.index()
client.run(os.environ["token"])
