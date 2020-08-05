from discord.ext import commands
import random
import asyncio
import config as cfg  # get config data

bot = commands.Bot(command_prefix='~', description='Post a message at random intervals picking at random from set channels')  # initiate bot


async def random_spam():
    await bot.wait_until_ready()  # only start when ready

    channels = [channel for channel in bot.get_server(cfg.id).channels if channel.id in cfg.whitelist]  # get list of allowed existing channels

    while True:
        channel = random.choice(channels)
        random_message = random.choice(cfg.messages)
        wait_time = random.uniform(cfg.time_min, cfg.time_max)
        name = ''.join(letter for letter in channel.name if letter.isalnum())

        print(f'Trying to post "{random_message}" in {name} then wait {wait_time}')

        await bot.send_message(channel, random_message)  # say random message from list in random channel from server
        await asyncio.sleep(wait_time)  # wait for random seconds between minimum and maximum amount


if __name__ == "__main__":
    bot.loop.create_task(random_spam())  # multithreading

    bot.run(cfg.token)  # start script
