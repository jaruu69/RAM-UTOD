# modul ini dibuat oleh coco a.k.a garamijo
# tolong dihargai dan jangan dihapus kreditnya
# ram-ubot emang toxic
# tapi ga lupa caranya berterima kasih
# yang hapus credit sama nyolong docker, lu GAY !!!

import random
from rams import CMD_HANDLER as cmd, CMD_HELP
from rams.utils import edit_or_reply, ram_cmd
from session.pyrogRam import *

eor = edit_or_reply

@ram_cmd(pattern="1(?: |$)(.*)")
async def _(e):
    txt = ram_ab
    await eor(e, txt)
    
@ram_cmd(pattern="2(?: |$)(.*)")
async def _(e):
    txt = ram_bc
    await eor(e, txt)
    
    
@ram_cmd(pattern="3(?: |$)(.*)")
async def _(e):
    txt = ram_cd
    await eor(e, txt)    
    
    
@ram_cmd(pattern="4(?: |$)(.*)")
async def _(e):
    txt = ram_de
    await eor(e, txt)
    
@ram_cmd(pattern="5(?: |$)(.*)")
async def _(e):
    txt = ram_ef
    await eor(e, txt)    
    
    
@ram_cmd(pattern="6(?: |$)(.*)")
async def _(e):
    txt = ram_fg
    await eor(e, txt)

@ram_cmd(pattern="7(?: |$)(.*)")
async def _(e):
    txt = ram_hi
    await eor(e, txt)
    
@ram_cmd(pattern="8(?: |$)(.*)")
async def _(e):
    txt = ram_ij
    await eor(e, txt)
    
    
@ram_cmd(pattern="9(?: |$)(.*)")
async def _(e):
    txt = ram_jk
    await eor(e, txt)    
    
    
@ram_cmd(pattern="10(?: |$)(.*)")
async def _(e):
    txt = ram_kl
    await eor(e, txt)
    
@ram_cmd(pattern="11(?: |$)(.*)")
async def _(e):
    txt = ram_lm
    await eor(e, txt)    
    
    
@ram_cmd(pattern="12(?: |$)(.*)")
async def _(e):
    txt = ram_mn
    await eor(e, txt)

@ram_cmd(pattern="13(?: |$)(.*)")
async def _(e):
    txt = ram_no
    await eor(e, txt)    
    
    
@ram_cmd(pattern="14(?: |$)(.*)")
async def _(e):
    txt = ram_op
    await eor(e, txt)
    
@ram_cmd(pattern="15(?: |$)(.*)")
async def _(e):
    txt = ram_pq
    await eor(e, txt)    
    
    
@ram_cmd(pattern="16(?: |$)(.*)")
async def _(e):
    txt = ram_qr
    await eor(e, txt)


@ram_cmd(pattern="17(?: |$)(.*)")
async def _(e):
    txt = ram_rs
    await eor(e, txt)
    
@ram_cmd(pattern="18(?: |$)(.*)")
async def _(e):
    txt = ram_st
    await eor(e, txt)    
    
    
@ram_cmd(pattern="19(?: |$)(.*)")
async def _(e):
    txt = ram_tu
    await eor(e, txt)

@ram_cmd(pattern="20(?: |$)(.*)")
async def _(e):
    txt = ram_uv
    await eor(e, txt)    
    
    
@ram_cmd(pattern="21(?: |$)(.*)")
async def _(e):
    txt = ram_vw
    await eor(e, txt)


@ram_cmd(pattern="22(?: |$)(.*)")
async def _(e):
    txt = ram_wx
    await eor(e, txt)
    
@ram_cmd(pattern="23(?: |$)(.*)")
async def _(e):
    txt = ram_xy
    await eor(e, txt)    
    
    
@ram_cmd(pattern="24(?: |$)(.*)")
async def _(e):
    txt = ram_yz
    await eor(e, txt)

@ram_cmd(pattern="25(?: |$)(.*)")
async def _(e):
    txt = ram_z1
    await eor(e, txt)


CMD_HELP.update(
    {
        "ramwords": f"**Plugin : **`gombal`\
        \n\n  𝘾𝙤𝙢𝙢𝙖𝙣𝙙 :** `{cmd}1 sampai {cmd}25\
        \n  ❍▸ : **kata kata gombalan.\
        \n\n  𝘾𝙤𝙢𝙢𝙖𝙣𝙙 :** `{cmd}ab atau {cmd}eb`\
        \n  ❍▸ :** random kalimat gombal.\
       "
    })
