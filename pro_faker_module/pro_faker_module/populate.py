import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','pro_faker_module.settings')
import django
django.setup()
import random
from app1.models import Employee
from faker import Faker

fake = Faker()

def populate(value):
    for i in range(value):
        eid = random.randint(1,200)
        name = fake.name()
        salary  = random.randint(20000,80000) 
        mail = fake.email()
        city = fake.city()
        
        obj = Employee.objects.get_or_create(
            
            eid=eid,name=name,salary=salary,mail=mail,city=city)
        
    
def main():
    no = int(input("How many records you want to add : "))
    populate(no)
    
if __name__ == '__main__':
    main()        
