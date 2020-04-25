import json
import facebook
import requests

if __name__ == '__main__':
    token = "EAACEdEose0cBALLqHaIO4x1lD679BDZBGt1z2xtgp6UGHaW9WfJJ7osn6G8PQWHz1pJKxUqZBXZAsQSC8O1fCaGHs0yY8IIbvP7m6H7MMN8PZCZCdZCheOU9MJhBvREi42LCo2YRHcfoQQlZCNkBDc8Rc2dHRBRqw4F0MxjbmbYNh9qn2SsC44bg0x8wbTCnGgZD"

    graph = facebook.GraphAPI(token)
    posts = graph.get_connections('me', 'posts')

    while True: # keep paginating
        try:
            with open('my_posts.jsonl', 'a') as f:
                for post in posts['data']:
                    f.write(json.dumps(post)+"\n")
                # get next page
                posts = requests.get(posts['paging']['next']).json()
        except KeyError:
            # no more pages, break the loop
            break
