# Run with args: --page GoldenSongs (ou nome da page)

import json
from argparse import ArgumentParser
import facebook
import requests

def get_parser():
    parser = ArgumentParser()
    parser.add_argument('--page', default='GoldenSongs')
    parser.add_argument('--n', default=100, type=int)
    return parser

if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()

    token = "EAACEdEose0cBAIZA9Um2TcLX8ZCeJZBKArI2YAZAFfgRMKZAXjBGybsjlaHZBZCMvknzqGfZBQQdPFTbwB4WFxVf5vDWjZBeXz7TcbUf8SyZALyPd5gzP6SIj9rhFCT1zyZAxKZBxIfLBD9eErWtt02D8S20duThfWCkNP2iu3ZBvdWshNPiwfmaY94ZCnPZCfuYZAUIDcjg55BZBJrnnCABSaujaNTS4wLvZB2MPxmo7gibOdcMhZAKwZDZD"

    graph = facebook.GraphAPI(token, version=2.7)
    all_fields = [
        'id',
        'message',
        'created_time',
        'shares',
        'likes.summary(true)',
        'comments.summary(true)',
        'reactions'
        ]
    all_fields = ','.join(all_fields)
    posts = graph.get_connections('GoldenSongs', 'posts', fields=all_fields)

    downloaded = 0
    while True: # keep paginating
        if downloaded >= args.n:
            break
        try:
            fname = "posts_{}.jsonl".format(args.page)
            with open(fname, 'a') as f:
                for post in posts['data']:
                    downloaded += 1
                    f.write(json.dumps(post)+"\n")
                # get next page
                posts = requests.get(posts['paging']['next']).json()
        except KeyError:
            # no more pages, break the loop
            break

