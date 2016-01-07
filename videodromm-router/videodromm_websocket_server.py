#!/usr/bin/env python

#
#  videodromm_websocket_server.py
# websockets server from https://github.com/aaugustin/websockets
# coroutines from http://stackoverflow.com/questions/32054066/python-how-to-run-multiple-coroutines-concurrently-using-asyncio
import argparse
import asyncio
import websockets

# here we'll store all active connections
connections = []

# Parse the command line arguments
parser = argparse.ArgumentParser(description='Videodromm websocket server')
parser.add_argument("--ip", default="127.0.0.1", help="The websocket ip to listen on")
parser.add_argument("--wsport", type=int, default=8765, help="The websocket port to listen on")

args = parser.parse_args()
print("Listening websocket clients on ip:{} port:{}".format(args.ip, args.wsport))
ip = args.ip
wsport = int(args.wsport)

@asyncio.coroutine
def connection_handler(connection, path):
    connections.append(connection)  # add connection to pool
    print('new connection {}'.format(connection.host))
    while True:
        message_to_route = yield from connection.recv()
        if message_to_route is None:  # connection lost
            connections.remove(connection)  # remove connection from pool, when client disconnects
            break
        else:
            print('< {}'.format(message_to_route))
            yield from connection.send(message_to_route)
            print('> {}'.format(message_to_route))

@asyncio.coroutine
def send_periodically():
    while True:
        yield from asyncio.sleep(5)  # switch to other code and continue execution in 5 seconds
        for connection in connections:
            print('> Periodic event happened.')
            yield from connection.send('Periodic event happened.')  # send message to each connected client
"""
async def process_message(websocket, path):
    received = await websocket.recv()
    print("received: {}".format(received))

    message_to_route = "{}".format(received)
    await websocket.send(message_to_route)
    print("routed: {}".format(message_to_route))
    await websocket.send(message_to_route)
    print("routed2: {}".format(message_to_route))
"""
start_server = websockets.serve(connection_handler, ip, wsport)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.async(send_periodically())  # before blocking call we schedule our coroutine for sending periodic messages

asyncio.get_event_loop().run_forever()
