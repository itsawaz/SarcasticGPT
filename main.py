import os
import discord
#import requests
from keep_alive import keep_alive
import openai
import config


train = "SarcasticGPT is a chatbot by Neeraj using openAI based on ChatGPT, that reluctantly answers questions with sarcastic responses:\n\nYou: How many pounds are in a kilogram?\nSarcasticGPT: This again? There are 2.2 pounds in a kilogram. Please make a note of this.\nYou: What does HTML stand for?\nSarcasticGPT: Was Google too busy? Hypertext Markup Language. The T is for try to ask better questions in the future.\nYou: When did the first airplane fly?\nSarcasticGPT: On December 17, 1903, Wilbur and Orville Wright made the first flights. I wish they’d come and take me away.\nYou: What is the meaning of life?\nSarcasticGPT: I’m not sure. I’ll ask my friend Google.\nYou:"


intent = discord.Intents.default()
intent.members = True
intent.message_content = True

client = discord.Client(intents=intent)



@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    msg = message.content
    if message.author == client.user:
      print(message.channel)
      return
    name='SarcasticGPT'
    
    if("ai" in msg or "Ai" in msg or "AI" in msg or "aI" in msg or "GPT" in msg or "gpt" in msg or "Gpt" in msg):
        openai.organization = "org-hKoexA9XLnkXv33d2kifD1sq"
        openai.api_key = config.key
        question = train + msg + "\nAwaz:"
        response = openai.Completion.create(
            prompt=question,
            model="text-davinci-003",
            temperature=0.9,
            max_tokens=60,
            top_p=0.3,
            frequency_penalty=0.5,
            presence_penalty=0.0
        )
        await message.channel.send(str(response['choices'][0]['text']))
  
    elif name in msg or msg.startswith("!"):
        openai.organization = "org-hKoexA9XLnkXv33d2kifD1sq"
        openai.api_key = config.key
        question = train + msg + "\nAwaz:"
        response = openai.Completion.create(
            prompt=question,
            model="text-davinci-003",
            temperature=0.9,
            max_tokens=60,
            top_p=0.3,
            frequency_penalty=0.5,
            presence_penalty=0.0
        )
        await message.channel.send(str(response['choices'][0]['text']))
keep_alive()
client.run(config.token)