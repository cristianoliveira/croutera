# Croutera
Simple Cli Router Admin (*CR*outer*A*).

The missing CLI for common Routers actions like login, restart , list clientes, log, etc.

## Motivation
Almost all of tools I am used to use have a CLI to handle their functionality
but my WiFi router haven't. Croutera comes to supply this missing CLI for this
kind of WiFi routers/modems.

## Installing
Clone this repo and inside this folder do:
```bash
make install
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

## How to help?
 - Adding new routers. See [Routers](https://github.com/CristianOliveiraDaRosa/croutera/blob/master/croutera/models/routers.py) to get the router interface you should implement.
 - Creating issues/requests/bug fixes
 - Adding Unit Tests
 - Using! And sending feedback.

## Contributing
 - Fork it!
 - Create your feature branch: `git checkout -b my-new-feature`
 - Commit your changes: `git commit -am 'Add some feature'`
 - Push to the branch: `git push origin my-new-feature`
 - Submit a pull request

**Pull Request should have unit tests**

### Routers available:
 - Dlink:
  - DR610: http://www.dlink.com.br/produto/dir-610-a1
 - TpLink:
  - WR340G: http://www.tp-link.com.br/products/details/?model=TL-WR340G

**MIT License**
