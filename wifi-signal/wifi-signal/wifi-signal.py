#!/usr/bin/env python3.7

import asyncio
import iterm2
import os
import subprocess

class clr:
    NA = '\033[38;5;196m'
    LOW = '\033[38;5;166m'
    OK = '\033[38;5;106m'
    GOOD = '\033[38;5;34m'
    GREAT = '\033[38;5;46m'
    ENDC = '\033[0m'

def GetIcon(val):
    symbol = (clr.NA + "􀙥" + clr.ENDC);
    if (0 > val > -25):
        symbol = (clr.LOW + "􀙇" + clr.ENDC)
    elif (-26 > val > -50):
        symbol = (clr.OK + "􀙇" + clr.ENDC)
    elif (-51 > val > -75):
        symbol = (clr.GOOD + "􀙇" + clr.ENDC)
    elif (-76 > val > -100):
        symbol = (clr.GREAT + "􀙇" + clr.ENDC)

    return symbol


def GetWiFiStrength():
    p = subprocess.Popen(
        "/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I | grep CtlRSSI | awk '{print $2}'", 
        shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    )
    s = ((p.stdout.readlines()[0]).decode("utf-8").strip())
    val = int(s)
    return GetIcon(val)

async def main(connection):
    app = await iterm2.async_get_app(connection)

    component = iterm2.StatusBarComponent(
        short_description="WiFi Signal Strength",
        detailed_description="Display WiFi signal strength",
        knobs=[],
        exemplar=GetWiFiStrength(),
        update_cadence=10,
        identifier="com.iterm2.wifi-strength")

    # This function gets called once per second.
    @iterm2.StatusBarRPC
    async def coro(knobs, space=iterm2.Reference("iterm2.user.wifi-sterngth?")):
        return str(GetWiFiStrength())

    # Register the component.
    await component.async_register(connection, coro)

# This instructs the script to run the "main" coroutine and to keep running even after it returns.
iterm2.run_forever(main)