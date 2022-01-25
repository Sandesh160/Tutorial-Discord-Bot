import os
from dotenv import load_dotenv
from nextcord.ext import commands

def main():
    client = commands.Bot(command_prefix="?")

    load_dotenv()

    @client.event
    async def on_ready():
        print(f"{client.user.name} has connected to Discord.")

    # load all cogs
    for folder in os.listdir("modules"):
        if os.path.exists(os.path.join("modules", folder, "cog.py")):
            client.load_extension(f"modules.{folder}.cog")

    client.run(os.getenv("OTM1NTU4ODU2NDQzMDY4NDE2.YfAZFQ.vGv4gDbXzH9RKwDetFf0WMci5yk"))

if __name__ == '__main__':
    main()
