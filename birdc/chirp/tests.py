from django.test import TestCase

# Create your tests here.


from .views import find_user_by_name

class ResultsTest(TestCase):

    def test_if_first_name_has_searched_string(self):
        res = find_user_by_name('R')
        for r in res:
            self.assertIs(r.first_name == 'R',  True)


