import requests

HOST: str = '<HOST>'
PORT: str = '<PORT>'
SSL: bool = False
KEY: int = 0x88
ENDPOINT: str = 'xoxo'
FILENAME: str = '<FILENAME>'

def xorro(content: bytes) -> bytes:
    retval = bytearray(len(content))

    for i in range(len(content)):
        retval[i] = content[i] ^ KEY
        
    return retval

def main():
    url = ''

    if SSL is True:
        url += 'https://'
    else:
        url += 'http://'

    url += HOST + ':' + PORT + '/' + ENDPOINT + '/' + FILENAME

    xcontent = requests.get(url, verify=False, allow_redirects=True)

    content = xorro(xcontent.content)

    f = open(FILENAME, 'wb')
    f.write(content)
    f.close()

if __name__ == '__main__':
    main()
