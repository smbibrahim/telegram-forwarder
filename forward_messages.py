from telethon import TelegramClient, events
import os

# API credentials (provided)
api_id = 14738233  # Your API ID
api_hash = 'c709fe6024d2b8138f9c1dae88779fc2'  # Your API Hash

# Channel IDs
source_channel = -1001288549616  # Always_Win_Premium's channel ID
destination_channel = "@neusignal"  # Your destination channel

# Initialize Telethon Client
client = TelegramClient("session", api_id, api_hash)

@client.on(events.NewMessage(chats=source_channel))
async def forward_messages(event):
    message_text = event.message.text

    # Check if message contains "Leverage"
    if message_text and "Leverage" in message_text:
        await client.send_message(destination_channel, message_text)

# Start the bot
print("Bot is running...")
client.start()
client.run_until_disconnected()
