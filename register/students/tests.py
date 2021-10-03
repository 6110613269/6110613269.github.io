from django.test import TestCase,Client
from .models import Student,Quota
from django.db.models import Max
# Create your tests here.

class QuotaTestCase(TestCase):
    def setUp(self):
        user1 = Student.objects.create(first="a",last="aa",username="aaa")
        user2 = Student.objects.create(first="b",last="bb",username="bbb")


        Quota.objects.create(code="x", name="xx", semester=1, limit=2, year=2021, status="open")
        Quota.objects.create(code="y", name="yy", semester=1, limit=2, year=2021, status="open")
        r = Quota.objects.get(name="xx")
        r.quotas.add(user1)
        r.quotas.add(user2)


    def test_sit(self):
        y = Quota.objects.get(name="xx")
        self.assertEqual(y.quotas.all().count(),2)

    def test_invalid_limit(self):
        y = Quota.objects.get(name="xx")
        self.assertTrue(y.is_valid_limit())


    def test_invalid_status(self):
        y = Quota.objects.get(name="xx")
        self.assertTrue(y.is_valid_open())

#test views
#test index and student views
    def test_student(self):
        c = Client()
        user1 = Student.objects.create(first="a",last="aa",username="aaa")
        response = c.get(f"/students/{user1.id}")
        self.assertEqual(response.status_code,200)
#test back
    def test_back(self):
        c = Client()
        user1 = Student.objects.create(first="a",last="aa",username="aaa")
        response = c.get(f"/students/{user1.id}/back")
        self.assertEqual(response.status_code,200)

    def test_invalid_students_page(self):
        c = Client()
        max_id = Student.objects.all().aggregate(Max("id"))["id__max"]
        max_id = max_id+1
        response = c.get(f"/students/{max_id}")
        self.assertEqual(response.status_code,404)

#test book
    def test_enroll_student(self):
        q = Quota.objects.get(name="yy")
        useradd = Student.objects.create(first="q",last="qq",username="qqq")
        q.quotas.add(useradd)
        c = Client()
        response = c.get(f"/students/{useradd.id}")
        """ student has quotas """
        self.assertEqual(response.context["enrolls"].count(),1)
        """ quotas has student """
        self.assertEqual(response.context["non_enrolls"].count(),1)

    def test_non_enroll_student(self):
        q = Quota.objects.get(name="yy")
        useradd = Student.objects.create(first="q",last="qq",username="qqq")
        c = Client()
        response = c.get(f"/students/{useradd.id}")
        """ quotas hasn't student """
        self.assertEqual(response.context["non_enrolls"].count(),2)
        
        self.assertEqual(response.context["enrolls"].count(),0)
        
        
        
        
    
#test drop

    def test_drop_student(self):
        q = Quota.objects.get(name="yy")
        useradd = Student.objects.create(first="q",last="qq",username="qqq")
        q.quotas.add(useradd)
        q.quotas.remove(useradd)
        c = Client()
        response = c.get(f"/students/{useradd.id}")
        
        self.assertEqual(response.context["enrolls"].count(),0)
        
        self.assertEqual(response.context["non_enrolls"].count(),2)
    
    
    
    

