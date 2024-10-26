##
# d.py
# Author: 0xb4db01
#
# Description: this is the simple file download api for Flauzio.
# From this endpoint it is possible to download any file defined in
# static_file_dir in the Flauzio config.
#

from sys import exit
from flauzio import config, app
from fastapi.responses import FileResponse

HELPMSG='''
apis section of Flauzio config needs an "d" entry.
Example:

"apis":{
    "d": {
        "enpoint_name": "x",
    }
}

Where endpoint_name is the api endpoint name you want to use.
'''

def d_help():
    print(HELPMSG)

    exit(-1)

if 'd' not in config['apis']:
    d_help()

if 'endpoint_name' not in config['apis']['d']:
    d_help()

ENDPOINT = '/%s/{filename}' % (config['apis']['d']['endpoint_name'])

@app.get(ENDPOINT)
async def d(filename: str):
    static = config['flauzio']['static_file_dir']
    path = f'/{static}/{filename}'

    return FileResponse(
        path=path,
        filename=filename,
        media_type='application/octet-stream'
    )
