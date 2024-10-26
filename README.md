# Flauzio

Flauzio is a tiny webserver I wrote during pentesting tasks, for transfering suspicious files that can be intercepted by traffic monitoring technologies. In order to do so, Flauzio will encrypt such files before sending them to the client.

To make things a little bit simpler, Flauzio comes with stagers that can be donwloaded initially. These stagers will provide the means to download from Flauzio encrypted files and decrypt them once download is finished.

To do so, Flauzio hosts an endpoint that does not encrypt files; which is basically like having a classic python -m http.server at the end of the day.

The encryption endpoints are defined in "apis". For now, there is only a "x" endpoint that will XOR the file. I will maybe one day add an AES endpoint.

# Install

To install Flauzio

```
virtualenv /whatever/path/flauzio
source /whatever/path/flauzio/bin/activate
pip install -r requirements.txt
python3 setup install
```

# Usage

To use Flauzio you will need to create a cfg file, which is just a json file. An example flauzio.cfg file is provided.

The example cfg file is pretty much self explanatory. Note that if you do not want to enable SSL you still need to define the `ssl_keyfile` and `ssl_certfile` keys, with "" as value.

```
{
    "flauzio": {
        "host": "<BIND HOST>,
        "port": <BIND PORT>,
        "static_file_dir": "<STATIC FILE DIR>",
        "ssl": {
            "enable": true,
            "ssl_keyfile": "<KEY FILE OR EMPTY IF ENABLE IS FALSE>",
            "ssl_certfile": "<PEM FILE OR EMPTY IF ENABLE IS FALSE>"
        }
    },
    "apis": {
        "d": {
            "endpoint_name": "dld"
        },
        "x": {
            "endpoint_name": "xoxo",
            "key": 136
        }
    }
}
```

The "apis" object is where the fun happens. The "d" key defines the non encrypting file transfer endpoint. This is what you want to contact to download the stager.

The "x" entry is the XOR encryption endpoint, you can define a key (one byte only for now) that Flauzio will use to XOR any file you will download from here. If you use a stager you should end up with the original file, deXOR'd.

Note that you can rename the endpoints as you wish with the `endpoint_name` key.

Remember to define a `static_file_dir` where you will put the stagers and whatever other file you want to transfer.

Once you installed and configured your cfg file, just run `flauzio -c file.cfg`.

# Stagers

At the moment, only XOR is supported and there are only 2 stagers. A python3 stager and a PS stager. Feel free to write your own in whatever language you want.

# Future

The code is pretty spaghetty so I think I will make it better whenever I have time and, also, will probably add at least AES encryption enpoint and stagers.

Stay tuned.

Also, this is - as usual - stuff I do for *authorized operations only* and I do *not* support any illegal activities. Don't be a skid or, if you can't avoid being one, don't use my crappy tools!
