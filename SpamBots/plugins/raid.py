
import asyncio
import base64
import os
import random
from telethon import events
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from .. import SPAM-BY-7H, SPAM-BY-7H2, SPAM-BY-7H3, SPAM-BY-7H4, SPAM-BY-7H5, SPAM-BY-7H6, SPAM-BY-7H7, SPAM-BY-7H8, SPAM-BY-7H9, SPAM-BY-7H10, SUDO_USERS, RAID, RRAID

SMEX_USERS = []
for x in SUDO_USERS:
    SMEX_USERS.append(x)

que = {}



@SPAM-BY-7H.on(events.NewMessage(pattern="/raid"))
@SPAM-BY-7H2.on(events.NewMessage(pattern="/raid"))
@SPAM-BY-7H3.on(events.NewMessage(pattern="/raid"))
@SPAM-BY-7H4.on(events.NewMessage(pattern="/raid"))
@SPAM-BY-7H5.on(events.NewMessage(pattern="/raid"))
@SPAM-BY-7H6.on(events.NewMessage(pattern="/raid"))
@SPAM-BY-7H7.on(events.NewMessage(pattern="/raid"))
@SPAM-BY-7H8.on(events.NewMessage(pattern="/raid"))
@SPAM-BY-7H9.on(events.NewMessage(pattern="/raid"))
@SPAM-BY-7H10.on(events.NewMessage(pattern="/raid"))
async def spam(e):  
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        SPAM-BY-7H = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(SPAM-BY-7H) == 2:
            message = str(SPAM-BY-7H[1])
            print(message)
            a = await e.client.get_entity(message)
            g = a.id
            c = a.first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(SPAM-BY-7H[0])
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            c = b.first_name
            counter = int(SPAM-BY-7H[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )



@SPAM-BY-7H.on(events.NewMessage(incoming=True))
@SPAM-BY-7H2.on(events.NewMessage(incoming=True))
@SPAM-BY-7H3.on(events.NewMessage(incoming=True))
@SPAM-BY-7H4.on(events.NewMessage(incoming=True))
@SPAM-BY-7H5.on(events.NewMessage(incoming=True))
@SPAM-BY-7H6.on(events.NewMessage(incoming=True))
@SPAM-BY-7H7.on(events.NewMessage(incoming=True))
@SPAM-BY-7H8.on(events.NewMessage(incoming=True))
@SPAM-BY-7H9.on(events.NewMessage(incoming=True))
@SPAM-BY-7H10.on(events.NewMessage(incoming=True))
async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.3)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(RRAID)),
            reply_to=event.message.id,
        )


@SPAM-BY-7H.on(events.NewMessage(pattern="/replyraid"))
@SPAM-BY-7H2.on(events.NewMessage(pattern="/replyraid"))
@SPAM-BY-7H3.on(events.NewMessage(pattern="/replyraid"))
@SPAM-BY-7H4.on(events.NewMessage(pattern="/replyraid"))
@SPAM-BY-7H5.on(events.NewMessage(pattern="/replyraid"))
@SPAM-BY-7H6.on(events.NewMessage(pattern="/replyraid"))
@SPAM-BY-7H7.on(events.NewMessage(pattern="/replyraid"))
@SPAM-BY-7H8.on(events.NewMessage(pattern="/replyraid"))
@SPAM-BY-7H9.on(events.NewMessage(pattern="/replyraid"))
@SPAM-BY-7H10.on(events.NewMessage(pattern="/replyraid"))
async def _(e):
    global que
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        SPAM-BY-7H = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        await e.get_reply_message()
        if len(e.text) > 11:
            message = str(SPAM-BY-7H[0])
            a = await e.client.get_entity(message)
            g = a.id
            que[g] = []
            qeue = que.get(g)
            appendable = [g]
            qeue.append(appendable)
            text = "ᖇEᑭᒪY ᖇᗩIᗪ [ᗩᑕTIᐯᗩTEᗪ]!!\n           〄 ╔»⟦★𝟳𝗛★⟧«╗ SᑭᗩᗰᗰEᖇ ᗷOT 〄"
            await e.reply(text, parse_mode=None, link_preview=None)
        elif e.reply_to_msg_id:
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            que[g] = []
            qeue = que.get(g)
            appendable = [g]
            qeue.append(appendable)
            text = "ᖇEᑭᒪY ᖇᗩIᗪ [ᗩᑕTIᐯᗩTEᗪ]!!\n           〄 ╔»⟦★𝟳𝗛★⟧«╗ SᑭᗩᗰᗰEᖇ ᗷOT 〄"
            await e.reply(text, parse_mode=None, link_preview=None)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)

@SPAM-BY-7H.on(events.NewMessage(pattern="/dreplyraid"))
@SPAM-BY-7H2.on(events.NewMessage(pattern="/dreplyraid"))
@SPAM-BY-7H3.on(events.NewMessage(pattern="/dreplyraid"))
@SPAM-BY-7H4.on(events.NewMessage(pattern="/dreplyraid"))
@SPAM-BY-7H5.on(events.NewMessage(pattern="/dreplyraid"))
@SPAM-BY-7H6.on(events.NewMessage(pattern="/dreplyraid"))
@SPAM-BY-7H7.on(events.NewMessage(pattern="/dreplyraid"))
@SPAM-BY-7H8.on(events.NewMessage(pattern="/dreplyraid"))
@SPAM-BY-7H9.on(events.NewMessage(pattern="/dreplyraid"))
@SPAM-BY-7H10.on(events.NewMessage(pattern="/dreplyraid"))
async def _(e):
    global que    
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        SPAM-BY-7H = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 12:
            message = str(SPAM-BY-7H[0])
            a = await e.client.get_entity(message)
            g = a.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "𝚁𝙰𝙽𝙳𝙸 𝙺𝙸 𝙲𝙷𝚄𝙳𝙰𝙸 𝙳𝙾𝙽𝙴!! ᖇEᑭᒪY ᖇᗩIᗪ [ᗪE-ᗩᑕTIᐯᗩTEᗪ]\n           〄 ╔»⟦★𝟳𝗛★⟧«╗ SᑭᗩᗰᗰEᖇ ᗷOT 〄"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "𝚁𝙰𝙽𝙳𝙸 𝙺𝙸 𝙲𝙷𝚄𝙳𝙰𝙸 𝙳𝙾𝙽𝙴!! ᖇEᑭᒪY ᖇᗩIᗪ [ᗪE-ᗩᑕTIᐯᗩTEᗪ]\n           〄 ╔»⟦★𝟳𝗛★⟧«╗ SᑭᗩᗰᗰEᖇ ᗷOT 〄"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
    
