# Croutera [![PyPI version](https://badge.fury.io/py/croutera.svg)](https://badge.fury.io/py/croutera) [![Build Status](https://travis-ci.org/cristianoliveira/croutera.svg)](https://travis-ci.org/cristianoliveira/croutera)
Simple Cli Router Admin (*CR*outer*A*).

The missing CLI for common Routers actions like login, restart , list clientes, log, etc.

## Motivation
Almost all of tools I am used to use have a CLI to handle their functionality
but my WiFi router haven't. Croutera comes to supply this missing CLI for this
kind of WiFi routers/modems.

## Installing
```bash
pip install croutera
```

### From Source
Clone this repo and inside this folder do:
```bash
make setup && make install
```

## Using
```bash
croutera -h
```

## Commands
The current commands

#### Show models available
```bash
croutera -list-models
```

#### Restart
```bash
croutera -restart [model] [username] [password]
```

#### Show Wifi Password
```bash
croutera -wifi-pass [model] [username] [password]
```

You can set this params in Environment Variables:
```
ROUTER_MODEL=dlink-dir610
ROUTER_IP=10.0.0.1
ROUTER_USERNAME=admin
ROUTER_PASSWORD=admin
```
# Contributing

 - Suggesting new routers to be added.
 - Adding new routers. See [Routers](https://github.com/cristianoliveira/croutera/blob/master/croutera/models/base.py) to get the router interface you should implement.
 - Creating issues/requests/bug fixes
 - Adding Unit Tests
 - Using! And sending feedback.

## Code Contribute
 - Fork it!
 - Create your feature branch: `git checkout -b my-new-feature`
 - Commit your changes: `git commit -am 'Add some feature'`
 - Push to the branch: `git push origin my-new-feature`
 - Submit a pull request

**Pull Request should have unit tests**

## How to test my Implementation?
 See the online simulators available. [Simulators](https://github.com/cristianoliveira/croutera/issues/11)

### Routers available:
 - Cisco:
   - DPC3928S / EPC3928: http://www.cisco.com/web/consumer/support/modem_dpc3928.html
 - Dlink:
   - DR610: http://www.dlink.com.br/produto/dir-610-a1
 - TpLink:
   - WR340G: http://www.tp-link.com.br/products/details/?model=TL-WR340G
   - WR720N: http://www.tp-link.com.br/products/details/?model=TL-WR720N
   - And all TL-WR* based router using 'tplink-tl-wrbased'
**MIT License**
