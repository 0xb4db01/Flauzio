from sys import argv, exit
from getopt import getopt
from json import loads

def flauzio_help():
    print('-c <config file>')

    exit(-1)

if len(argv) <= 1:
    flauzio_help()

opts, args = getopt(argv[1:], 'c:')

cfgfile = False

for opt in opts:
    if opt[0] == '-c':
        cfgfile = opt[1]

if cfgfile is False:
    flauzio_help()

config = loads(open(cfgfile).read())

if 'host' not in config['flauzio']:
    print('Flauzio config needs a flauzio.host definition!')

    exit(-1)

if 'port' not in config['flauzio']:
    print('Flauzio config needs a flauzio.port definition!')

    exit(-1)

if 'static_file_dir' not in config['flauzio']:
    print('Flauzio config needs a flauzio.static_file_dir definition!')

    exit(-1)

if 'ssl' not in config['flauzio']:
    print('Flauzio config needs a flazio.ssl with',
            '"enable": true|false, "ssl_keyfile" and "ssl_certfile"',
            'definitions!')

    exit(-1)

if 'enable' not in config['flauzio']['ssl']:
    print('Flauzio config needs a flazio.ssl with',
            '"enable": true|false, "ssl_keyfile" and "ssl_certfile"',
            'definitions!')

    exit(-1)

if 'ssl_keyfile' not in config['flauzio']['ssl']:
    print('Flauzio config needs a flazio.ssl with',
            '"enable": true|false, "ssl_keyfile" and "ssl_certfile"',
            'definitions!')

    exit(-1)

if 'ssl_certfile' not in config['flauzio']['ssl']:
    print('Flauzio config needs a flazio.ssl with',
            '"enable": true|false, "ssl_keyfile" and "ssl_certfile"',
            'definitions!')

    exit(-1)

from fastapi import FastAPI

app = FastAPI()
