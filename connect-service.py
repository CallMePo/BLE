import asyncio
from bleak import BleakClient
import sys

async def get_services(mac):
    async with BleakClient(mac) as client:
        print(f"Connected: {client.is_connected}")

        svcs = await client.get_services()
        print("Services:", svcs)
        for service in client.services:
            print("Services: ")
            print(service)

            print("\nCharacteristic: ")
            for char in service.characteristics:
                print(char)
                print("\nProperties: ")
                print(char.properties)
        await client.disconnect()
try:
    asyncio.run(get_services("57:68:C5:FE:4C:0C"))
except KeyboardInterrupt:
    print("User stopped the program")
    sys.exit(0)
