# videodromm-router
Server responsible for message routing. 

[![Join the chat at https://gitter.im/videodromm/router](https://badges.gitter.im/videodromm/router.svg)](https://gitter.im/videodromm/router?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
routes messages OSC MIDI websockets to the clients (Python)

Websockets server for OSC, MIDI, etc. made with crossbar (Python)
* Listen for Web Socket connections on port 8765
* Relay incoming messages from a Web Socket client to all other connected clients

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


## Running the router
- python or python3 videodromm_router.py

