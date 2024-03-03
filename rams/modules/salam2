# Gausah kesini ngentot!!
# NGEDIT CMD YG BENER KONTOL!!!
# YANG HAPUS KREDIT GUA TANDAIN REPO LO

from rams import CMD_HELP, BLACKLIST_CHAT, OWNDEV, CMD_HANDLER as cmd
from rams.utils import edit_or_reply, ram_cmd

# ================= WELCOME ==================
#       HAYO YANG HAPUS KREDIT GUA JITAK
#                FROM RAM-UBOT
# ============================================

@ram_cmd(pattern="p(?: |$)(.*)")
async def _(event):
    if event.chat_id in BLACKLIST_CHAT:
        return await edit_or_reply(event, "JANGAN PAKE DISINI SALAM LO HARAM HEHEHE")
    await event.client.send_message(
        event.chat_id, "**𝐀ssalamu'alaikum ahli neraka**", reply_to=event.reply_to_msg_id)
    await event.delete()

@ram_cmd(pattern="l(?: |$)(.*)")
async def _(event):
    if event.chat_id in BLACKLIST_CHAT:
        return await edit_or_reply(event, "JANGAN DISINI DI NGENTOD SALAM LO HARAM!!")
    await event.client.send_message(
        event.chat_id, "**Wa'alaikumsalam kaum dajjal...**", reply_to=event.reply_to_msg_id)
    await event.delete()

CMD_HELP.update({
    "salam2":
    f"{cmd}p\
\nUsage: salam\
\n\n{cmd}l\
\nUsage: jawab salam"
})
