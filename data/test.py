from requests import get, post, delete


# print(post('http://localhost:5000/api/v2/news',
#            json={'title': 'Заголовок',
#                  'content': 'Текст новости',
#                  'user_id': 4,
#                  'is_private': False}).json())
print(get('http://localhost:5000/api/v2/news').json())
# print(delete('http://localhost:5000/api/news/999').json())
# новости с id = 999 нет в базе
#
# print(delete('http://localhost:5000/api/news/2').json())