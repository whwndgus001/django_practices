from django.test import TestCase
from emaillist import models

#conn() Test
# db = models.conn()
# print(db)

# insert() Test
models.insert('또', '치', 'ddochi@naver.com')


#fetchlist() Test
# results = models.fetchlist()
# print(results)