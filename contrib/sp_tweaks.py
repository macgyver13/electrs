#!/usr/bin/env python3
import argparse
import client
import json

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='127.0.0.1')
    parser.add_argument('--port', default=50001)
    parser.add_argument('--height', default=258257)    
    args = parser.parse_args()

    conn = client.Client((args.host, args.port))
    
    result = conn.call([client.request("blockchain.block.tweaks", int(args.height))])
    print(json.dumps(result[0]))


if __name__ == '__main__':
    
    main()
