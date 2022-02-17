

from .. import SPAM-BY-7H, SPAM-BY-7H2, SPAM-BY-7H3, SPAM-BY-7H4, SPAM-BY-7H5, SPAM-BY-7H6, SPAM-BY-7H7, SPAM-BY-7H8, SPAM-BY-7H9, SPAM-BY-7H10, SUDO_USERS
from telethon import events
from time import time
from datetime import datetime

SMEX_USERS = []
for x in SUDO_USERS:
    SMEX_USERS.append(x)

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

@SPAM-BY-7H.on(events.NewMessage(pattern="/ping"))
@SPAM-BY-7H2.on(events.NewMessage(pattern="/ping"))
@SPAM-BY-7H3.on(events.NewMessage(pattern="/ping"))
@SPAM-BY-7H4.on(events.NewMessage(pattern="/ping"))
@SPAM-BY-7H5.on(events.NewMessage(pattern="/ping"))
@SPAM-BY-7H6.on(events.NewMessage(pattern="/ping"))
@SPAM-BY-7H7.on(events.NewMessage(pattern="/ping"))
@SPAM-BY-7H8.on(events.NewMessage(pattern="/ping"))
@SPAM-BY-7H9.on(events.NewMessage(pattern="/ping"))
@SPAM-BY-7H10.on(events.NewMessage(pattern="/ping"))
async def ping(e):
    if e.sender_id in SMEX_USERS:
        start = datetime.now()
        text = "Pong!"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"🤖 🇵 🇴 🇳 🇬 !\n`{ms}` 𝗺𝘀       〄 ╔»⟦★𝟳𝗛★⟧«╗ SᑭᗩᗰᗰEᖇ ᗷOT 〄")                       
