#from django.test import TestCase (Django TDD)
import guestbook.models as guestbookmodel


def test_guestbookmodel_insert():
    guestbookmodel.insert('조중현', '1234', '안녕하세요~')


def test_guestbookmodel_fetchlist():
    results = guestbookmodel.fetchlist()
    print(results)

def test_guestbookmodel_delete():
    guestbookmodel.delete(5, '1234')


#test_guestbookmodel_insert()
test_guestbookmodel_fetchlist()
test_guestbookmodel_delete()