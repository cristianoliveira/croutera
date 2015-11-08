# Croutera
Simple terminal Cli Router Admin (*C**R*outer*A*)
to handle common Routers actions like login, restart , list clientes, log, etc.

## Using
Clone this repo and inside this folder do:
```bash
   python croutera.py -help
```

## Commands
The current commands

### Restart
Restart modem
```bash
python croutera.py [model] [username] [password] -restart
```

## How to help?
 - Adding new routers. See [Routers](https://github.com/CristianOliveiraDaRosa/croutera/blob/master/croutera/models/routers.py) to get the router interface you should implement.
 - Creating issues/requests/bug fixes
 - Adding Unit Tests
 - Coding

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
 

