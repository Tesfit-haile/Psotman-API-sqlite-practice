
import requests
import json

###### this how you can access the stack overflow api

# q = requests.get('http://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')
#
# for question in q.json()['items']:
#     if [question['answer_count']] == 0:
#         print(question['title'])
#         print(question['link'])
#     else:
#         print('skipped')
#     print('###################################################')
#
