# Ping From <\ram-ubot/>
# From @lahsiajg <starboy/>

""" rams module containing commands related to the \
    Information Superhighway (yes, Internet). """

import asyncio
import random
import time
from datetime import datetime

from speedtest import Speedtest

from rams import CMD_HANDLER as cmd, DEVS
from rams.utils import edit_or_reply, ram_cmd
from rams import CMD_HELP, BOT_VER, DEVG, REPO_NAME, StartTime, branch
from rams.events import register

gesss = [
    "eh iya hai bang jar",
    "wih kemana aja nih bang?",
    "oi bang jar 😁",
    "woi bang maap telat 🥺",
    "pas banget bang, aku lagi kangen",
    "abangkuhhh jar on juga akhirnya🥵",
]

brb = [
    "Jangan off dong bang.",
    "Bang, mau kemana?",
    "Jangan lama lama bang",
    "Siap bang.",
    "Yah udah off aja bang.",
    "Jangan lupa makan bang.",
    "Yah pasti mao bucin ni.",
    "Jangan off terus lah bang.",
    "Mau nonton bokep kah?",
]

async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "d"]

    while count < 4:
        count += 50
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@register(incoming=True, from_users=DEVG, pattern=r"^p$")
async def _(landak):
    await landak.reply(random.choice(gesss))


@register(incoming=True, from_users=DEVS, pattern=r"^brb$")
async def _(landak):
    await landak.reply(random.choice(brb))

@ram_cmd(pattern="ping$")
async def _(ping):
    """ For.ping command, ping the rams from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await ping.client.get_me()
    await ping.reply(
            f"**♡ ᴘɪɴɢ** `%sms`\n"
            f"**♡ ᴜᴘᴛɪᴍᴇ** `{uptime}`\n"
            f"**♡ —ɪ'ᴍ [{user.first_name}](tg://user?id={user.id})**" % (duration)
    )

@register(pattern=r"^\.jping(?: |$)(.*)", sudo=True)
async def _(ping):
    """ For.ping command, ping the rams from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await ping.client.get_me()
    await ping.client.send_message(
        ping.chat_id, f"**♡ ᴢᴀʀ ᴘɪɴɢ** `%sms`\n"
                    f"**♡ ᴏᴡɴᴇʀ:** [{user.first_name}](tg://user?id={user.id})\n" % (duration), reply_to=ping.reply_to_msg_id)
    await ping.delete()

@ram_cmd(pattern="piw$")
async def _(pong):
    """For .ping command, ping the rams from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    ram = await edit_or_reply(pong, "**pinging...**")
    await ram.edit("** ˗ˏˋ❀ ping ❀ ˎˊ˗ **")
    await ram.edit("** ˗ˏˋ❀❀ ping ❀❀ ˎˊ˗ **")
    await ram.edit("** ˗ˏˋ❀❀❀ ping ❀❀❀ ˎˊ˗ **")
    await ram.edit("** ˗ˏˋ❀❀ ping ❀❀ ˎˊ˗ **")
    await ram.edit("** ˗ˏˋ❀ ping ❀ ˎˊ˗ **")
    await ram.edit("**ꕤ PIW PIW!!**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await pong.client.get_me()
    await pong.reply(
                f"**♡ ᴘɪᴡ :** `%sms`\n"
                f"**├ ᴜᴘᴛɪᴍᴇ :** `{uptime}`\n"
                f"**╰ ᴜꜱᴇʀ :** [{user.first_name}](tg://user?id={user.id})"% (duration)
    )

@ram_cmd(pattern="pong$")
async def redis(pong):
    """For .ping command, ping the rams from any chat."""
    await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    ram = await edit_or_reply(pong, "**✧**")
    await ram.edit("**✧✧**")
    await ram.edit("**✧✧✧**")
    await ram.edit("**✧✧✧✧**")
    await ram.edit("**✧✧✧✧✧**")
    await asyncio.sleep(2)
    await ram.edit("⚡️")
    await asyncio.sleep(2)
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user= await pong.client.get_me()
    await pong.reply(
            f"**♡ [{user.first_name}-ubot](tg://user?id={user.id})**\n\n" 
            f"**♡ ᴘɪɴɢᴇʀ :** `%sms`\n"
            f"**♡ ᴜᴘᴛɪᴍᴇ :** {uptime}" % (duration)
    )

@ram_cmd(pattern="speed$")
async def speedtst(spd):
    """ For .speed command, use SpeedTest to check server speeds. """
    await spd.edit("`Menjalankan Tes Kecepatan Jaringan, Mohon Tunggu...✨`")
    test = Speedtest()

    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()

    await spd.edit("**Kecepatan Jaringan:\n**"
                   "✧ **Dimulai Pada :** "
                   f"`{result['timestamp']}` \n"
                   f" **━━━━━━━━━━━━━━━━━**\n\n"
                   "✧ **Download:** "
                   f"`{speed_convert(result['download'])}` \n"
                   "✧ **Upload:** "
                   f"`{speed_convert(result['upload'])}` \n"
                   "✧ **Signal:** "
                   f"`{result['ping']}` \n"
                   "✧ **ISP:** "
                   f"`{result['client']['isp']}` \n"
                   f"✧ **BOT:** {REPO_NAME}")


def speed_convert(size):
    """
    Hi human, you can't read bytes?
    """
    power = 2**10
    zero = 0
    units = {0: '', 1: 'Kb/s', 2: 'Mb/s', 3: 'Gb/s', 4: 'Tb/s'}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"




CMD_HELP.update({
    "ping": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}ping` or `{cmd}rping` or `{cmd}pink`\
         \n↳ : Untuk Menunjukkan Ping Bot Anda.\
         \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}speed`\
         \n↳ : Untuk Menunjukkan Kecepatan Jaringan Anda.\
         \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}pong`\
         \n↳ : Sama Seperti Perintah {cmd}pink."})
