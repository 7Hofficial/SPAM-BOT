async def gifspam(e, smex):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=smex.media.document.access_hash,
                    file_reference=smex.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception:
        pass

import asyncio
import base64
import os
from telethon import events
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from .. import SPAM-BY-7H, SPAM-BY-7H2, SPAM-BY-7H3, SPAM-BY-7H4, SPAM-BY-7H5, SPAM-BY-7H6, SPAM-BY-7H7, SPAM-BY-7H8, SPAM-BY-7H9, SPAM-BY-7H10, SUDO_USERS

SMEX_USERS = []
for x in SUDO_USERS:
    SMEX_USERS.append(x)



@SPAM-BY-7H.on(events.NewMessage(pattern="/spam"))
@SPAM-BY-7H2.on(events.NewMessage(pattern="/spam"))
@SPAM-BY-7H3.on(events.NewMessage(pattern="/spam"))
@SPAM-BY-7H4.on(events.NewMessage(pattern="/spam"))
@SPAM-BY-7H5.on(events.NewMessage(pattern="/spam"))
@SPAM-BY-7H6.on(events.NewMessage(pattern="/spam"))
@SPAM-BY-7H7.on(events.NewMessage(pattern="/spam"))
@SPAM-BY-7H8.on(events.NewMessage(pattern="/spam"))
@SPAM-BY-7H9.on(events.NewMessage(pattern="/spam"))
@SPAM-BY-7H10.on(events.NewMessage(pattern="/spam"))
async def spam(e):
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        SPAM-BY-7H = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(SPAM-BY-7H) == 2:
            message = str(SPAM-BY-7H[1])
            counter = int(SPAM-BY-7H[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None)
            await asyncio.wait([e.respond(message) for i in range(counter)])
        elif e.reply_to_msg_id and smex.media:
            counter = int(SPAM-BY-7H[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None)
            for _ in range(counter):
                smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                await gifspam(e, smex)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(SPAM-BY-7H[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None)
            await asyncio.wait([e.respond(message) for i in range(counter)])
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)
