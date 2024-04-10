import asyncio
import websockets

async def test():
    uri = "ws://192.168.15.7:8000/messaging" #MUDAR DE ACORDO COM A MÁQUINA
    async with websockets.connect(uri) as websocket:
        await websocket.send("Que engraçado esse servidor hein, Maravilha")
        response = await websocket.recv()
        print(response)

asyncio.run(test())