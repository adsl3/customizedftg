import asyncio
import time
from telethon.tl import functions
from telethon.errors import FloodWaitError
from uniborg.util import admin_cmd
from datetime import datetime
import pendulum

DEL_TIME_OUT = 70

@borg.on(admin_cmd(pattern="ab"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    while True:
        tehran = pendulum.timezone('Asia/Tehran')
        toronto = pendulum.timezone('Canada/Eastern')
        london = pendulum.timezone('UTC')

        th = datetime.now(tehran).strftime('%H:%M')
        tr = datetime.now(toronto).strftime('%H:%M')
        ln = datetime.now(london).strftime('%H:%M')
        
        bio = f"| 🇮🇷Tehran {th} | 🇨🇦Toronto {tr} | 🇬🇧London {ln} | Don't ask how 😂"
        logger.info(bio)
        try:
            await borg(functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                about=bio
            ))
        except FloodWaitError as ex:
            logger.warning(str(e))
            await asyncio.sleep(ex.seconds)
        # else:
            # logger.info(r.stringify())
            # await borg.send_message(  # pylint:disable=E0602
            #     Config.PRIVATE_GROUP_BOT_API_ID,  # pylint:disable=E0602
            #     "Successfully Changed Profile Bio"
            # )
        await asyncio.sleep(DEL_TIME_OUT)

