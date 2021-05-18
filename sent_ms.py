import discord
import os

def main():
    client = discord.Client()
    discord_token = os.environ.get('discord_token')

if __name__ == '__main__':
    main()
