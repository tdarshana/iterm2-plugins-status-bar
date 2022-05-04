#!/usr/bin/env python3.7

import asyncio
import iterm2
import os

def FormatBytes(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f %s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f %s%s" % (num, 'Yi', suffix)

def GetFreeSpace():
    statvfs = os.statvfs('/')
    return FormatBytes(statvfs.f_frsize * statvfs.f_bavail)

async def main(connection):
    app = await iterm2.async_get_app(connection)

    component = iterm2.StatusBarComponent(
        short_description="Free Space",
        detailed_description="Shows the amount of free disk space",
        knobs=[],
        exemplar="􀥾 " + GetFreeSpace(),
        update_cadence=10,
        identifier="com.iterm2.disk-space")

    # This function gets called once per second.
    @iterm2.StatusBarRPC
    async def coro(knobs, space=iterm2.Reference("iterm2.user.diskspace?")):
        return str("􀥾 " + GetFreeSpace())

    # Register the component.
    await component.async_register(connection, coro)

# This instructs the script to run the "main" coroutine and to keep running even after it returns.
iterm2.run_forever(main)

