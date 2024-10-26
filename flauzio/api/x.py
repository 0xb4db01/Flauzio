##
# x.py
# Author: 0xb4db01
#
# Description: this is the xorred file download api for Flauzio.
# From this endpoint it is possible to download any file defined in
# static_file_dir in the Flauzio config, which will be XOR'd with the key
# defined in "key" entry in Flauzio config file.
#

from sys import exit
from flauzio import config, app
from fastapi.responses import FileResponse

HELPMSG='''
apis section of Flauzio config needs an "x" entry.
Example:

"apis":{
    "x": {
        "enpoint_name": "x",
        "key": 136
    }
}

Where endpoint_name is the api endpoint name you want to use and key is the
xor key.
'''

def x_help():
    print(HELPMSG)

    exit(-1)

if 'x' not in config['apis']:
    x_help()

if 'endpoint_name' not in config['apis']['x']:
    x_help()

if 'key' not in config['apis']['x']:
    x_help()

ENDPOINT = '/%s/{filename}' % (config['apis']['x']['endpoint_name'])

def xorfile(filename: str) -> str:
    sfcontent = open(filename, 'rb').read()

    dfcontent = bytearray(len(sfcontent))

    for i in range(len(sfcontent)):
        dfcontent[i] = sfcontent[i] ^ config['apis']['x']['key']

    f = open(filename+'.x', 'wb')
    f.write(dfcontent)
    f.close()

    return filename+'.x'

@app.get(ENDPOINT)
async def x(filename: str):
    static = config['flauzio']['static_file_dir']
    path = xorfile(f'/{static}/{filename}')

    return FileResponse(
        path=path,
        filename=filename,
        media_type='application/octet-stream'
    )
