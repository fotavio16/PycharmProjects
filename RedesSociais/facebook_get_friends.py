import json
import facebook

if __name__ == '__main__':
    token = "EAACEdEose0cBALLqHaIO4x1lD679BDZBGt1z2xtgp6UGHaW9WfJJ7osn6G8PQWHz1pJKxUqZBXZAsQSC8O1fCaGHs0yY8IIbvP7m6H7MMN8PZCZCdZCheOU9MJhBvREi42LCo2YRHcfoQQlZCNkBDc8Rc2dHRBRqw4F0MxjbmbYNh9qn2SsC44bg0x8wbTCnGgZD"

    graph = facebook.GraphAPI(token)
    user = graph.get_object('me')
    friends = graph.get_connections(user["id"], "friends")

    print(json.dumps(friends, indent=4))
