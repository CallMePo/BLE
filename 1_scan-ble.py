import asyncio
from bleak import BleakScanner

async def main():
    device = await BleakScanner.discover()
    for d in device:
        print(d)

asyncio.run(main())
#%%
