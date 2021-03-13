import discord
from discord.ext import commands
import json
import time

TOKEN = "ODIwMDM1MDU1MTgyNTQ0OTU2.YEvTKA.eq1DyQIn1WbnTn3_iMzXa5wR_tA"

bot = commands.Bot(command_prefix="&")


def read_json():
    with open("nuggies.json", "r") as f:
        return json.load(f)


def save_json():
    with open("nuggies.json", "w") as f:
        json.dump(accounts, f, sort_keys=True, indent=4)

accounts = read_json()


@bot.event
async def on_ready():
    print("connected to dc")


@bot.command(name="nuggies", help="|Toon het aantal shareboxes iedereen ownt")
async def nuggies(ctx):
    print(accounts)
    for account in accounts:
        await ctx.send(f"{account} > {accounts[account]}")


@bot.command(name="addNuggie", help="(naam) (aantal) |Voeg een shareboxes toe aan een persoon")
async def addNuggie(ctx, name, amount):
    accounts[name] += int(amount)
    save_json()
    time.sleep(1)
    await ctx.send(f"{name} owns {accounts[name]} shareboxes!")

@bot.command(name="addDikzak", help="(naam) |Voeg een deelnemer toe")
async def addDikzak(ctx, name):
    accounts.update({name: 0})
    save_json()
    time.sleep(1)
    await ctx.send(f"dikzak {name} toegevoegd")

@bot.command(name="delNuggie", help="(naam) (aantal) |Verwijder een shareboxes van iemands geweten")
async def delNuggie(ctx, name, amount):
    accounts[name] -= int(amount)
    save_json()
    time.sleep(1)
    await ctx.send(f"{name} owns {accounts[name]} shareboxes!")

bot.run(TOKEN)