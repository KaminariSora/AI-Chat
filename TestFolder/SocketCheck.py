import asyncio
import websockets
import json

async def request_authentication_token(plugin_name, developer_name):
    async with websockets.connect("ws://localhost:8001") as websocket:
        auth_token_request = {
            "apiName": "VTubeStudioPublicAPI",
            "apiVersion": "1.0",
            "requestID": "authTokenRequest",
            "messageType": "AuthenticationTokenRequest",
            "data": {
                "pluginName": plugin_name,
                "pluginDeveloper": developer_name
            }
        }

        await websocket.send(json.dumps(auth_token_request))
        response = await websocket.recv()
        response_data = json.loads(response)
        
        if response_data['messageType'] == "APIError":
            print(f"Error: {response_data['data']['message']}")
        else:
            print("Authentication Token Request Sent. Please check VTube Studio to approve the request.")
            print(f"Response: {response_data}")

# Example of requesting an authentication token
asyncio.run(request_authentication_token("MyVTuberPlugin", "KaminariSora"))
