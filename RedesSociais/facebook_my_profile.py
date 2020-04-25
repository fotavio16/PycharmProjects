import os
import json
import facebook

if __name__ == '__main__':
    #token = os.environ.get('FACEBOOK_TEMP_TOKEN')
    token = "EAACEdEose0cBAPeICi0HBhtFcCUhk0iAzvggBjXyO4ZBmRZA4uoS6iiLnb3Fiwg6H4rJ4e9iuhtaWx33m6IVMmBNPGKVweLNohie8jAXHISmgFTSTqTILJWsM1URC4ZChzE27vdOqLss7Us6xtPwZBLVMTC3ZBkYNR8GyctybVgNkZBSuteAoV1Q0Gp9TBZBTUZD"


    graph = facebook.GraphAPI(token)
    profile = graph.get_object('me', fields='name,location{location}')

    print(json.dumps(profile, indent=4))
