import sys
import json
import os
from urllib.parse import urlparse
from urllib.request import urlopen, Request

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} <token>")
    sys.exit()

if sys.argv[1] :
    if not os.path.exists('abi'):
        os.mkdir('./abi')

    filename = f'abi/{sys.argv[1]}.json'
    if os.path.exists(filename):
        with open(filename, 'r') as abi_file:
            abi = abi_file.read()
    else:
        # TODO: Error handling
        url = 'https://bkcscan.com/api?module=contract&action=getabi&address=' + sys.argv[1]
        abi_response = urlopen(Request(url, headers={'User-Agent': 'Mozilla'})).read().decode('utf8')
        abi = json.loads(abi_response)['result']

        with open(filename, 'w') as abi_file:
            abi_file.write(abi)
else:
    raise Exception(f"argument {sys.argv[1]} does not exist in configuration!")



