import asyncio
import websockets

# This async function will handle messages from clients
async def echo(websocket, path):
    async for message in websocket:
        print(f"Received: {message}")
        reply = f"Server says: You said '{message}'"
        await websocket.send(reply)

# Start WebSocket server on port 8765
start_server = websockets.serve(echo, "localhost", 8765)

print("🚀 WebSocket Server started at ws://localhost:8765")
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()