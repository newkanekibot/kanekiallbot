# Voics Chatbot Module Credits Pranav Ajay 🐰Github = Red-Aura 🐹 Telegram= @madepranav
# @lyciachatbot support Now
import os
import aiofiles
import aiohttp
from random import randint
from pyrogram import filters
from kaneki import pbot as Kaneki


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            try:
                data = await resp.json()
            except:
                data = await resp.text()
    return data


async def ai_Kaneki(url):
    ai_name = "Kaneki.mp3"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                f = await aiofiles.open(ai_name, mode="wb")
                await f.write(await resp.read())
                await f.close()
    return ai_name


@Kaneki.on_message(filters.command("voice"))
async def Kaneki(_, message):
    if len(message.command) < 2:
        await message.reply_text("Kaneki AI Voice Chatbot")
        return
    text = message.text.split(None, 1)[1]
    Kaneki = text.replace(" ", "%20")
    m = await message.reply_text("Kaneki Is Best...")
    try:
        L = await fetch(
            f"https://api.affiliateplus.xyz/api/chatbot?message={lycia}&botname=@KanekiMusicbot&ownername=@Cyberhunt27&user=1"
        )
        chatbot = L["message"]
        VoiceAi = f"https://lyciavoice.herokuapp.com/lycia?text={chatbot}&lang=id"
        name = "kaneki"
    except Exception as e:
        await m.edit(str(e))
        return
    await m.edit("Made By @Cyberhunt27...")
    KanekiVoice = await ai_Kaneki(VoiceAi)
    await m.edit("Appling...")
    await message.reply_audio(audio=KanekiVoice, title=chatbot, performer=name)
    os.remove(KanekiVoice)
    await m.delete()
