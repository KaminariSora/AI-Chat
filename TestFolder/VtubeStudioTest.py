import asyncio
import websockets
import json

async def send_message(websocket, message):
    await websocket.send(json.dumps(message))
    response = await websocket.recv()
    return json.loads(response)

async def authenticate(websocket):
    auth_request = {
        "apiName": "VTubeStudioPublicAPI",
        "apiVersion": "1.0",
        "requestID": "authenticate",
        "messageType": "AuthenticationRequest",
        "data": {
            "pluginName": "MyVTuberPlugin",  # Replace with your plugin's name
            "pluginDeveloper": "KaminariSora",   # Replace with your name or organization
            "authenticationToken": "86faa398b3ceb04b80bc10c32a4d0572ce7d27d1e41df4b99217faa5cbf124f0"  # Provide your auth token if required
        }
    }
    response = await send_message(websocket, auth_request)
    if response['messageType'] == "APIError":
        print(f"Authentication failed: {response['data']['message']}")
        return False
    print("Authentication successful")
    return True

async def send_to_vtube_studio(text: str):
    async with websockets.connect("ws://localhost:8001") as websocket:
        # Authenticate with the VTube Studio API
        if not await authenticate(websocket):
            return

        # Send text to VTube Studio for lip-sync
        lip_sync_request = {
            "apiName": "VTubeStudioPublicAPI",
            "apiVersion": "1.0",
            "requestID": "lipSync",
            "messageType": "LipSyncRequest",  # Replace with the correct message type
            "data": {
                "text": text
            }
        }
        response = await send_message(websocket, lip_sync_request)
        if response['messageType'] == "APIError":
            print(f"Lip-sync error: {response['data']['message']}")
        else:
            print(f"Lip-sync response: {response}")

# Test the WebSocket and Authentication
async def main():
    text = "Hello, I am your AI VTuber!"
    await send_to_vtube_studio(text)

# Run the test
asyncio.run(main())
