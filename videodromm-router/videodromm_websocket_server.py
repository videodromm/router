#!/usr/bin/env python

#
#  videodromm_websocket_server.py
# websockets server from https://github.com/aaugustin/websockets
import argparse
import asyncio
import websockets

# Parse the command line arguments
parser = argparse.ArgumentParser(description='Videodromm websocket server')
parser.add_argument("--ip", default="127.0.0.1", help="The websocket ip to listen on")
parser.add_argument("--wsport", type=int, default=8765, help="The websocket port to listen on")

args = parser.parse_args()
print("Listening websocket clients on ip:{} port:{}".format(args.ip, args.wsport))
ip = args.ip
wsport = int(args.wsport)

async def process_message(websocket, path):
    received = await websocket.recv()
    print("received: {}".format(received))

    message_to_route = "{}".format(received)
    await websocket.send(message_to_route)
    print("routed: {}".format(message_to_route))
    await websocket.send(message_to_route)
    print("routed2: {}".format(message_to_route))

start_server = websockets.serve(process_message, ip, wsport)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
