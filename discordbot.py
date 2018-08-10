import random

from discord.ext.commands import Bot
BOT_PREFIX = ("?", "!")

TOKEN="NDY2NzU3MzU0MDA5MTMzMDk2.Dk5KRQ.wceTI9pweETfGwo9G-I0Ya4Qf_g"

client=Bot(command_prefix=BOT_PREFIX)

@client.command (name='motivationalunicorn',
                 description="Motivational quotes.",
                  brief="A unicorn that helps you navigate through life.")
async def motivational_unicorn ():
    possible_responses = [
        'Virtual huggie!',
        'Who is the best? You are!',
        'YOU CAN DO IT!',
        'You are so close! You got this!',
        'You will never know if you do not try',
        'You have come so far! Do not give up!',
        'You got this!',
        'Hang in there!',
        'You are unstoppable!',
        'You will take the world by storm!',
        'I am so proud of you!',
        'You are creating something out of nothing and that is a huge deal!',
        'No matter what happens, you started something big and no one can take that away!',
     
        
    ]
    await client.say(random.choice (possible_responses) )



client.run(TOKEN)
