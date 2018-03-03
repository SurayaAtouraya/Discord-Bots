import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_member_join(user):
    role = discord.utils.get(client.get_server('247923889697587200').roles, name = "Arkha (Guest)")
    await client.send_message(client.get_channel('247923889697587200'), 'Shlama ' + user.name + "! Welcome to Assyria, you have been assigned a guest role, earn my trust, and you shall have freedom.")
    await client.add_roles(user, role)
    

client.run('ENTER_BOT_TOKEN_HERE')
