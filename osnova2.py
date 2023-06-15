import discord
from discord.components import SelectOption
from discord.ext import commands
import time
from time import sleep

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
Token = 'MTExNjM3NjYyNjE1MDc4MTAzOA.GIyBTQ.Dki2SrWyNdXIFS1pdPEOUXKDmE8_HkrvXtFIOg'

role1 = 1115674790058016879
role2 = 1115674851588456552

b = 1118545740306841711
n = 1118545917319073812
y = 1118546069085765702



@bot.event
async def on_ready():
    print("Я капибара клубничная")

@bot.command()
async def selectmenu(ctx):

    options = [
        discord.SelectOption(label='Бампер', emoji='🔮', description='помочь серверу в развитии', value='b'),
        discord.SelectOption(label='Новостика', emoji='🤔', description='получать новости сервера', value='n'),
        discord.SelectOption(label='Участник мероприятий', emoji='💫', description='Получать новости о мероприятиях', value='y'),
        discord.SelectOption(label='Убрать все роли', emoji='❌', description='Удаление всех ролей, выбранных из списка', value='del')
    ]

    select = discord.ui.Select(
        placeholder='Выбери себе роль',
        options=options,
        min_values=0,
        max_values=4
    )

    view = discord.ui.View()
    view.add_item(select)

    async def call(interaction: discord.Interaction):
        member = interaction.user
        br = discord.utils.get(ctx.guild.roles, id=b)
        nr = discord.utils.get(ctx.guild.roles, id=n)
        yr = discord.utils.get(ctx.guild.roles, id=y)
        if select.values == ['b']:
                await member.add_roles(br)
                await interaction.response.send_message("Вы получили роль", ephemeral=True)
        elif select.values == ['n']:
                await member.add_roles(nr)
                await interaction.response.send_message("Вы получили роль", ephemeral=True)
        elif select.values == ['y']:
                await member.add_roles(yr)
                await interaction.response.send_message("Вы получили роль", ephemeral=True)
        elif select.values == ['b', 'n']:
                await member.add_roles(br, nr)
                await interaction.response.send_message("Вы получили роли", ephemeral=True)
        elif select.values == ['b', 'y']:
                await member.add_roles(br, yr)
                await interaction.response.send_message("Вы получили роли", ephemeral=True)
        elif select.values == ['n', 'y']:
                await member.add_roles(nr, yr)
                await interaction.response.send_message("Вы получили роли", ephemeral=True)
        elif select.values == ['b', 'n', 'y']:
                await member.add_roles(br, nr, yr)
                await interaction.response.send_message("Вы получили роли", ephemeral=True)
        elif select.values == ['del']:
               await member.remove_roles(br, nr, yr)
               await interaction.response.send_message("Вы убрали все роли", ephemeral=True)
        elif select.values == ['b', 'del']:
               await member.remove_roles(br)
               await interaction.response.send_message("Вы убрали роль", ephemeral=True)
        elif select.values == ['b', 'n', 'del']:
               await member.remove_roles(br, nr)
               await interaction.response.send_message("Вы убрали роли", ephemeral=True)
        elif select.values == ['b', 'n', 'y', 'del']:
               await member.remove_roles(br, nr, yr)
               await interaction.response.send_message("Вы убрали роли", ephemeral=True)
        elif select.values == ['b', 'y', 'del']:
               await member.remove_roles(br, yr)
               await interaction.response.send_message("Вы убрали роли", ephemeral=True)
        elif select.values == ['n', 'y', 'del']:
               await member.remove_roles(nr, yr)
               await interaction.response.send_message("Вы убрали роли", ephemeral=True)
        elif select.values == ['n', 'del']:
               await member.remove_roles(nr)
               await interaction.response.send_message("Вы убрали роль", ephemeral=True)
        elif select.values == ['y', 'del']:
               await member.remove_roles(yr)
               await interaction.response.send_message("Вы убрали роль", ephemeral=True)
        else:
               await interaction.response.send_message("Вы убрали все варианты списка", ephemeral=True)

        

    rb = discord.utils.get(ctx.guild.roles, id=b)
    rn = discord.utils.get(ctx.guild.roles, id=n)
    ry = discord.utils.get(ctx.guild.roles, id=y)

    embed = discord.Embed(
        title='**На чьей стороне ты?**', 
        description=f'**{rb.mention} – помогает серверу, прописывая в канале  команду «/bump»**\n\n**{rn.mention} – первым узнаёт о всех новостях сервера**\n\n**{ry.mention} – первый узнаёт о проведении мероприятий на сервере**',
        color=discord.Color(value=0x4B0076)
    )

    select.callback = call
    await ctx.send(embed=embed, view=view)

bot.run(Token)