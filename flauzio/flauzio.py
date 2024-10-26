from . import config, app
import uvicorn
from .api import *

def main():
    if config['flauzio']['ssl']['enable'] is True:
        uvicorn.run(
                app, 
                host=config['flauzio']['host'], 
                port=config['flauzio']['port'], 
                ssl_keyfile=config['flauzio']['ssl']['ssl_keyfile'], 
                ssl_certfile=config['flauzio']['ssl']['ssl_certfile'])
    else:
        uvicorn.run(
            app,
            host=config['flauzio']['host'],
            port=config['flauzio']['port']
        )

if __name__ == '__main__':
    main()
