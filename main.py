import discord
from keep_alive import keep_alive
import openai
import config

# Initialize the list to store the last 50 messages
last_50_messages = []

train = config.dataset


intent = discord.Intents.default()
intent.members = True
intent.message_content = True

client = discord.Client(intents=intent)
  

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  #get the bot-spam channel
  bot_spam_channel = discord.utils.get(client.get_all_channels(), name='bot-spam')
  #send message to the bot-spam channel
  await bot_spam_channel.send("SarcasticGPT is now up and running")


name='SarcasticGPT'
@client.event
async def on_message(message):
    msg = message.content
    if message.author == client.user:
      print(message.channel)
      print(last_50_messages)
      return
    
    # Append the current message to the list of last 50 messages
    last_50_messages.append(msg)
    if len(last_50_messages) > 50:
        last_50_messages.pop(0)

    name='SarcasticGPT'
    
    if msg.startswith("--update"):
        await message.channel.send("Exciting news @everyone, folks! The SarcasticGPT has just received a major upgrade and is now better than ever! With the latest version, v0.1, you'll be able to enjoy these fantastic new features:\n\n1. You can now directly message the chat bot and engage in conversation without the need for trigger sentences or keywords in personal DMs and bot-spam.\n2. If you're feeling particularly chatty, you can also engage with the bot in the 'Bot-Spam' channel.\n3. And for those of you who prefer a more direct approach, simply tag the bot and it will be at your beck and call.\n4. And the best part? You can now have continued conversation with the AI!\n\nSo what are you waiting for? Get ready to experience the sassiest chat bot on the market with SarcasticGPT v0.1!")
        return


      
    if msg.startswith("--learn"):
        await message.channel.send("Welcome to SarcasticGPT, the AI with a wicked sense of humor! With the latest version, v0.1, you can now enjoy a range of new features for a more interactive and engaging experience. Here's what you need to know:\n\n1. Start a conversation: Simply type '!prefix' to start chatting with SarcasticGPT. The bot will provide sarcastic responses to any questions you ask.\n2. Check for updates: Type '--update' to stay informed of recent changes and improvements to SarcasticGPT.\n3. Learn about the bot: Type '--learn' to find out more about the capabilities and background of the bot.\n\nAnd now, with v0.1, you can enjoy these additional features:\n1. Direct messaging: You can now directly message the bot in personal DMs or the 'Bot-Spam' channel.\n2. Direct tagging: Simply tag the bot to start a conversation.\n3. Continued conversation: Engage in continued conversation with SarcasticGPT for a more seamless experience.\n\nGet ready to experience the sassiest chat bot on the market with SarcasticGPT v0.1!")
        return

    if msg.startswith("--code"):
      await message.channel.send("Here you can find the code fo the project.\n\nhttps://github.com/itsawaz/SarcasticGPT")
      
    if message.guild is None or message.channel.name == 'bot-spam':
        openai.organization = "org-hKoexA9XLnkXv33d2kifD1sq"
        openai.api_key = config.key
        question = train + msg + "\nSarcasticGPT:"
        response = openai.Completion.create(
            prompt=question,
            model="text-davinci-002",
            temperature=1,
            max_tokens=1024,
            top_p=0.1,
            frequency_penalty=1,
            presence_penalty=1
        )
        await message.channel.send(str(response['choices'][0]['text']))
        last_50_messages.append(str(response['choices'][0]['text']))
        if len(last_50_messages) > 50:
          last_50_messages.pop(0)
        return

      
    if client.user in message.mentions:
        openai.organization = "org-hKoexA9XLnkXv33d2kifD1sq"
        openai.api_key = config.key
        question = train + msg + "\nSarcasticGPT:"
        response = openai.Completion.create(
            prompt=question,
            model="text-davinci-002",
            temperature=1,
            max_tokens=1024,
            top_p=0.1,
            frequency_penalty=1,
            presence_penalty=1
        )
        await message.channel.send(str(response['choices'][0]['text']))
        last_50_messages.append(str(response['choices'][0]['text']))
        if len(last_50_messages) > 50:
          last_50_messages.pop(0)
    elif name in msg or msg.startswith("!"):
        openai.organization = "org-hKoexA9XLnkXv33d2kifD1sq"
        openai.api_key = config.key
        question = train + msg + "\nSarcasticGPT:"
        response = openai.Completion.create(
            prompt=question,
            model="text-davinci-002",
            temperature=1,
            max_tokens=1024,
            top_p=0.1,
            frequency_penalty=1,
            presence_penalty=1
        )
        await message.channel.send(str(response['choices'][0]['text']))
        last_50_messages.append(str(response['choices'][0]['text']))
        if len(last_50_messages) > 50:
          last_50_messages.pop(0)
keep_alive()
client.run(config.token)
