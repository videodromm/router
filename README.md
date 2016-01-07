# videodromm-router
Server responsible for message routing. 

[![Join the chat at https://gitter.im/videodromm/router](https://badges.gitter.im/videodromm/router.svg)](https://gitter.im/videodromm/router?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
routes messages OSC MIDI websockets to the clients (Python)

Websockets server for OSC, MIDI, etc.
* Listen for Web Socket connections on port 8765
* Relay incoming messages from a Web Socket client to all other connected clients

Most-Pixels-Ever router for multiple clients communication

![Windows](https://raw.github.com/videodromm/router/master/assets/vd-python-win.jpg)
![Linux](https://raw.github.com/videodromm/router/master/assets/vd-python-lnx.jpg)

## Installation

- Setup Python 3.5 64 bit
- pip install argparse 
- pip install websockets
- pip install asyncio
- pip install python-osc


## Linux
- sudo apt-get install python3-pip
- pip3 install argparse
- pip3 install websockets
- pip3 install asyncio
- pip3 install python-osc
- pip3 install zope.interface

## twisted
- svn checkout svn://svn.twistedmatrix.com/svn/Twisted/tags/releases/twisted-13.1.0
- cd twisted-13.1.0
- python3 setup3.py install

## Running the router
Determine the ip address of the videodrömm websocket server
1 first launch the websocket server: python3 videodromm_websocket_server.py
2 then launch the router: python3 videodromm_router.py --ip websocketserverip --port websocketserverport

