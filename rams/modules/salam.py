from rams import CMD_HELP, BLACKLIST_CHAT, CMD_HANDLER as cmd
from rams.events import register
from rams.utils import ram_cmd
# ================= CONSTANT =================
#                FROM RAM-UBOT
# ============================================

@register(outgoing=True, pattern='^P(?: |$)(.*)')
async def _(typew):
    await typew.client.send_message(
        typew.chat_id, "𝐀𝐬𝐬𝐚𝐥𝐚𝐦𝐮'𝐚𝐥𝐚𝐢𝐤𝐮𝐦...", reply_to=typew.reply_to_msg_id)
    await typew.delete()

@register(outgoing=True, pattern='^L(?: |$)(.*)')
async def _(typew):
    await typew.client.send_message(
        typew.chat_id, "𝐖𝐚'𝐚𝐥𝐚𝐢𝐤𝐮𝐦𝐬𝐚𝐥𝐚𝐦...", reply_to=typew.reply_to_msg_id)
    await typew.delete()

@ram_cmd(pattern="ast(?: |$)(.*)")
async def _(typew):
    await typew.client.send_message(
        typew.chat_id, "𝐀𝐒𝐓𝐀𝐆𝐇𝐅𝐈𝐑𝐔𝐋𝐋𝐀𝐇......", reply_to=typew.reply_to_msg_id)
    await typew.delete()

CMD_HELP.update({
    "salam":
   f"P or `{cmd}p`\
\nUsage: Untuk Memberi salam.\
\n\nL or `{cmd}l`\
\nUsage: Untuk Menjawab Salam."
})
