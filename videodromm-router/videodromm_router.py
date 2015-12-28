#!/usr/bin/env python

import asyncio
import websockets
import argparse
import logging

logger = logging.getLogger('websockets')
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())

"""
parse command line arguments
"""
print("Pass arguments --ip yourIpAddress --port yourPort")
parser = argparse.ArgumentParser()
parser.add_argument("--ip",
      default="127.0.0.1", help="The ip to listen on")
parser.add_argument("--port",
      type=int, default=8765, help="The port to listen on")
args = parser.parse_args()

print("Listening on ip:{} port:{}".format(args.ip, args.port))
"""
websockets server from https://github.com/aaugustin/websockets
"""
async def hello(websocket, path):
    name = await websocket.recv()
    print("< {}".format(name))

    greeting = "Hello {}!".format(name)
    await websocket.send(greeting)
    print("> {}".format(greeting))

start_server = websockets.serve(hello, args.ip, args.port)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()


"""
client
#!/usr/bin/env python

import asyncio
import websockets

async def hello():
    async with websockets.connect('ws://192.168.0.17:8765') as websocket:

        name = input("What's your name? ")
        await websocket.send(name)
        print("> {}".format(name))

        greeting = await websocket.recv()
        print("< {}".format(greeting))

asyncio.get_event_loop().run_until_complete(hello())
"""


"""
https://pypi.python.org/pypi/python-osc
client
This program sends 10 random values between 0.0 and 1.0 to the /filter address,
waiting for 1 seconds between each value.

import argparse
import random
import time

from pythonosc import osc_message_builder
from pythonosc import udp_client


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip", default="127.0.0.1",
      help="The ip of the OSC server")
  parser.add_argument("--port", type=int, default=8000,
      help="The port the OSC server is listening on")
  args = parser.parse_args()

  client = udp_client.UDPClient(args.ip, args.port)

  for x in range(10):
    msg = osc_message_builder.OscMessageBuilder(address = "/filter")
    msg.add_arg(random.random())
    msg = msg.build()
    client.send(msg)
    time.sleep(1)"""
"""
server

    import argparse
import math

from pythonosc import dispatcher
from pythonosc import osc_server

def print_volume_handler(unused_addr, args, volume):
  print("[{0}] ~ {1}".format(args[0], volume))

def print_compute_handler(unused_addr, args, volume):
  try:
    print("[{0}] ~ {1}".format(args[0], args[1](volume)))
  except ValueError: pass

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip",
      default="127.0.0.1", help="The ip to listen on")
  parser.add_argument("--port",
      type=int, default=5005, help="The port to listen on")
  args = parser.parse_args()

  dispatcher = dispatcher.Dispatcher()
  dispatcher.map("/debug", print)
  dispatcher.map("/volume", print_volume_handler, "Volume")
  dispatcher.map("/logvolume", print_compute_handler, "Log volume", math.log)

  server = osc_server.ThreadingOSCUDPServer(
      (args.ip, args.port), dispatcher)
  print("Serving on {}".format(server.server_address))
  server.serve_forever()"""