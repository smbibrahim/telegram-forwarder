from telethon import TelegramClient, events
import os

# API credentials (use environment variables for security)
api_id = 14738233
api_hash = 'c709fe6024d2b8138f9c1dae88779fc2'

# Channel IDs (replace these with actual values)
source_channel = "Always_Win_Premium"  # Source channel username
destination_channel = "@neusignal"    # Destination channel username

# Initialize Telegram client
client = TelegramClient("session", api_id, api_hash)

@client.on(events.NewMessage(chats=source_channel))
async def forward_messages(event):
    message_text = event.message.text
    
    # Check if message contains the word "Leverage"
    if message_text and "Leverage" in message_text:
        await client.send_message(destination_channel, message_text)

# Start the bot
print("Bot is running...")
client.start()
client.run_until_disconnected()
