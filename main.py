from pyrogram import Client, filters
import os
import requests

API_ID = 23304838
API_HASH = "43766ff63d4ba848aea17f0cc1423a4dc"
BOT_TOKEN = os.environ.get("BOT_TOKEN")

bot = Client("airdropbot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

WEB_URL = "https://solid-bedecked-walrus.glitch.me"

@bot.on_message(filters.command("start"))
async def start(client, message):
    uid = str(message.from_user.id)
    ref_link = f"https://t.me/{client.me.username}?start={uid}"
    await message.reply(
        f"👋 Hello {message.from_user.first_name}!\n\n"
        f"🎯 Earn points by watching ads.\n"
        f"💰 Use your referral link to earn more:\n{ref_link}"
    )

@bot.on_message(filters.command("points"))
async def points(client, message):
    uid = str(message.from_user.id)
    try:
        r = requests.get(f"{WEB_URL}/points?uid={uid}")
        await message.reply(r.text)
    except:
        await message.reply("⚠️ Error fetching points")

@bot.on_message(filters.command("bonus"))
async def bonus(client, message):
    uid = str(message.from_user.id)
    try:
        r = requests.get(f"{WEB_URL}/bonus?uid={uid}")
        await message.reply(r.text)
    except:
        await message.reply("⚠️ Error claiming bonus")

bot.run()
