from pyrogram import Client, filters

# Replace these with your own values
api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'

app = Client("my_account", api_id=api_id, api_hash=api_hash)

@app.on_message(filters.group)
async def get_group_id(client, message):
    print(f"Group Name: {message.chat.title} | Group ID: {message.chat.id}")

async def main():
    await app.start()
    print("Bot started")
    while True:
        await asyncio.sleep(10)

if __name__ == "__main__":
    import asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
