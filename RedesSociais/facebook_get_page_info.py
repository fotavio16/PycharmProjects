# Run with args: --page GoldenSongs (ou nome da page)

import json
import facebook
from argparse import ArgumentParser

def get_parser():
    parser = ArgumentParser()
    parser.add_argument('--page')
    return parser

if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()

    token = "EAABwL0cVZAOcBAE02WAk1geGcdLelN10VlCsZCjelv8bcLPYcZCf8E4zs3QFLRZAujh7Dm89DYWch87VChghOsN8jKZBKUyZCjebANLzfNSxa69gLZBxIW6kIq5cisJDtoZA2QIe9QlQ0dDH1UenK5nUhG9nxZBqlAjMfHuBO2BDtnDhEDTNvAYQrn419Dwb2HLUZD"

    fields = ['id',
        'name',
        'about',
        'likes',
        'website',
        'link',
        ]
    fields = ','.join(fields)
    #print(fields)

    #print(args.page)

    graph = facebook.GraphAPI(token)
    page = graph.get_object(args.page, fields=fields)

    print(json.dumps(page, indent=4))
