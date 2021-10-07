from pyppeteer import launch
from time import sleep
import discord
import creds
from discord.ext import commands
from os import remove

bot = commands.Bot(command_prefix='*', description='Your Description')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('Future is loading ...')
    print('----------------------------------------------------------')
    await bot.change_presence(status=discord.Status.online,activity=discord.Game(name='*help || YOPI'))


@bot.command()
async def pooler(ctx):
    author = ctx.message.author.id
    if len(ctx.message.content.split()) == 2:
        browser = await launch()
        page = await browser.newPage()
        user = ctx.message.content.split(" ")[1]
        await page.setViewport({'width': 1, 'height': 1})
        await page.goto('https://1337-readme.vercel.app/api/profile?cursus=c-piscine&dark=true&login={0}'.format(user))
        sleep(1)
        await page.screenshot({'path': 'example.png', 'fullPage': 'false'})
        await browser.close()
        file = discord.File("example.png")
        remove("example.png")
        await ctx.send(file=file, content="<@{0.author.id}>".format(ctx))
    else:
        yopi = discord.Embed(title = 'Syntax_error', description = f'Sorry <@{author}> Please enter pooler login, Example : ***pooler login**',color = ctx.author.color)
        await ctx.send(embed = yopi)


@bot.command()
async def student(ctx):
    author = ctx.message.author.id
    if len(ctx.message.content.split()) == 2:
        browser = await launch()
        page = await browser.newPage()
        user = ctx.message.content.split(" ")[1]
        await page.setViewport({'width': 1, 'height': 1})
        await page.goto('https://1337-readme.vercel.app/api/profile?cursus=42&dark=true&login={0}'.format(user))
        sleep(1)
        await page.screenshot({'path': 'example.png', 'fullPage': 'false'})
        await browser.close()
        file = discord.File("example.png")
        remove("example.png")
        await ctx.send(file=file, content="<@{0.author.id}>".format(ctx))
    else:
        yopi = discord.Embed(title = 'Syntax_error', description = f'Sorry <@{author}> Please enter student login, Example : ***student login**',color = ctx.author.color)
        await ctx.send(embed = yopi)


@bot.group()
async def owner(ctx):
        yopi = discord.Embed(title = 'Owned by YOPI', description = f'Check out my **[twitter](https://twitter.com/YONINUX)** and **[github](https://github.com/YOPll)** ',color = discord.Colour.teal())
        await ctx.send(embed = yopi)


bot.run(creds.token)
