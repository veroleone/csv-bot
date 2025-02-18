import discord
import csv
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")
GUILD_ID = int(os.getenv("GUILD_ID"))
OG_ROLE_NAME = "🏆 | OG‘s"

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}')
        
        print(f"🔍 Debug: Using GUILD_ID = {GUILD_ID}")
        guild = self.get_guild(GUILD_ID)
        if guild is None:
            print(f"ERROR: Could not find the server with ID {GUILD_ID}. Make sure the bot is in the correct server.")
            return

        members = guild.members
        print(f"✅ Found {len(members)} members in the server.")


        with open('discord_members.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Discord Name", "Join Date", "Server Booster", "OG Member", "Roles"])

            for member in members:
                is_booster = "Yes" if member.premium_since else "No"
                is_og = "Yes" if any(role.name == OG_ROLE_NAME for role in member.roles) else "No"
                roles = ", ".join([role.name for role in member.roles])

                writer.writerow([member.name, member.joined_at.strftime('%Y-%m-%d'), is_booster, is_og, roles])

        print("CSV file successfully created: discord_members.csv")
        await self.close()

intents = discord.Intents.default()
intents.members = True

client = MyClient(intents=intents)
client.run(TOKEN)
