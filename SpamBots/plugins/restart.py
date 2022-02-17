from .. import SPAM-BY-7H, SPAM-BY-7H2, SPAM-BY-7H3, SPAM-BY-7H4, SPAM-BY-7H5, SPAM-BY-7H6, SPAM-BY-7H7, SPAM-BY-7H8, SPAM-BY-7H9, SPAM-BY-7H10, SUDO_USERS
from telethon import events
import os
import random
import sys

SMEX_USERS = []
for x in SUDO_USERS:
    SMEX_USERS.append(x)

@SPAM-BY-7H.on(events.NewMessage(pattern="/restart"))
@SPAM-BY-7H2.on(events.NewMessage(pattern="/restart"))
@SPAM-BY-7H3.on(events.NewMessage(pattern="/restart"))
@SPAM-BY-7H4.on(events.NewMessage(pattern="/restart"))
@SPAM-BY-7H5.on(events.NewMessage(pattern="/restart"))
@SPAM-BY-7H6.on(events.NewMessage(pattern="/restart"))
@SPAM-BY-7H7.on(events.NewMessage(pattern="/restart"))
@SPAM-BY-7H8.on(events.NewMessage(pattern="/restart"))
@SPAM-BY-7H9.on(events.NewMessage(pattern="/restart"))
@SPAM-BY-7H10.on(events.NewMessage(pattern="/restart"))
async def restart(e):
    if e.sender_id in SMEX_USERS:
        text = " 🤖𝐑𝐄𝐒𝐓𝐀𝐑𝐓𝐄𝐃🤖\n🔰𝐏𝐋𝐄𝐀𝐒𝐄 𝐖𝐀𝐈𝐓 𝐓𝐈𝐋𝐋 𝐈𝐓 𝐑𝐄𝐁𝐎𝐎𝐓𝐒...."
        await e.reply(text, parse_mode=None, link_preview=None)
        try:
            await SPAM-BY-7H.disconnect()
        except Exception:
            pass
        try:
            await SPAM-BY-7H2.disconnect()
        except Exception:
            pass
        try:
            await SPAM-BY-7H3.disconnect()
        except Exception:
            pass
        try:
            await SPAM-BY-7H4.disconnect()
        except Exception:
            pass
        try:
            await SPAM-BY-7H5.disconnect()
        except Exception:
            pass
        try:
            await SPAM-BY-7H6.disconnect()
        except Exception:
            pass
        try:
            await SPAM-BY-7H7.disconnect()
        except Exception:
            pass
        try:
            await SPAM-BY-7H8.disconnect()
        except Exception:
            pass
        try:
            await SPAM-BY-7H9.disconnect()
        except Exception:
            pass
        try:
            await SPAM-BY-7H10.disconnect()
        except Exception:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()
