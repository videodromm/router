# videodromm-router
Server responsible for message routing. 

[![Join the chat at https://gitter.im/videodromm/router](https://badges.gitter.im/videodromm/router.svg)](https://gitter.im/videodromm/router?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
routes messages OSC MIDI websockets to the clients (Python)

Websockets server for OSC, MIDI, etc. made with crossbar (Python)
* Listen for Web Socket connections on port 8080
* Relay incoming messages from a Web Socket client to all other connected clients

## Installation

- Setup Python 3.5 64 bit
- Follow instructions on http://crossbar.io/docs/Local-Installation/ 
- Check with <code>crossbar version</code>
- Optional: Test with <code>crossbar init --template hello:python --appdir $HOME/hello</code>
- Optional: Run <code>crossbar start --cbdir /home/YOURNAME/hello/.crossbar</code>
- Optional: Open http://localhost:8080/ in your browser

## Linux
- sudo apt-get install python3-pip
git clone https://github.com/crossbario/autobahn-python

## Running the router
- 

