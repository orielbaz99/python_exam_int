import json
import requests


class Post:
    def __init__(self, d):
        self.__dict__ = d

    def __str__(self, k, v):
        r = ''
        for k, v in self.__dict__.items():
            r += k
            r += '->'
            r += str(v)
            return r


id = input('Which post would you like to watch ? ')
response = requests.get('http://jsonplaceholder.typicode.com/posts/' + id)

postdict = json.loads(response.content)

if response.status_code // 100 == 2:
    postX = Post(postdict)
    print(f'user Id -> {postX.userId}\nid -> {postX.id}\ntitle -> {postX.title}\nbody -> {postX.body}')
else:
    print('invalid URL')
