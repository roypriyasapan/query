from django.shortcuts import render
from .models import Student
from django.http import HttpResponse


# Create your views here.
def home (request):
    # #get method
    # cnt=Student.objects.get(id=2)
    # print(cnt)
    # return HttpResponse("BY PRIYA")

#last
    #  cnt=Student.objects.last()
    #  cnt = Student.objects.order_by('stu_name').last()
    #  cnt = Student.objects.order_by('-stu_name').last()
    #  print(cnt)
    #  return HttpResponse("BY PRIYA")
#first
    #  cnt=Student.objects.first()
    #  cnt = Student.objects.order_by('stu_name').first()
    #  cnt = Student.objects.order_by('stu_name').last()
    #  cnt = Student.objects.order_by('-stu_name').first()
    #  print(cnt)
    #  return HttpResponse("BY PRIYA")

## update(**kwargs)
    # cnt= Student.objects.filter(id=3).update(stu_name='shubham',stu_city='bihar')
    # print(cnt)
    # return HttpResponse("By PRIYA")

 ## Update Multiple objects values at a time
    # cnt = Student.objects.filter(stu_city="nepal").update(stu_name='mehak')
    # print(cnt)
    # return HttpResponse("PRIYA")    
    

# reverse()
    #  cnt=Student.objects.reverse()
    #  print(cnt)
    #  return HttpResponse("PRIYA")

 ## Delete the given object
    # cnt = Student.objects.get(id=1).delete() 
    # cnt = Student.objects.get(id=1)
    # cnt.delete()
    # cnt = Student.objects.filter(stu_name = "suriya").delete()
    # print(cnt)
    # return HttpResponse("PRIYA")    

## count all no of object prasent in table
    # cnt = Student.objects.all()
    # print(cnt.count()) # In terminal provide total no of objects present
    
    # cnt = Student.objects.explain()
    # print(cnt)

    # # update_or_create(**kwargs,default=None)
    # cnt,created = Student.objects.update_or_create(id=2, stu_city="pipriya", defaults={'stu_name':"nikhil"})
    # print(cnt)
    # print(created)
    # return HttpResponse(cnt)
    # cnt = Student.objects.all()
    # print(cnt)
    

    ## bulk_create()      
    # cnt = Student.objects.bulk_create([Student(stu_name="shubham",stu_email="shubham@gmail.com",stu_city='bihar'),Student(stu_name="pardsi" ,stu_email="pardsi@gmail.com",stu_city='narmadapuram'),Student(stu_name="nikhil" ,stu_email="nikhil@gmail.com",stu_city='pipriya')
    # ])
    # print(cnt)
    
    ## filter().update()
    # cnt = Student .objects.filter(id=1).update(stu_name="mehak",stu_email="mehak@gmail.com",stu_city='nepal')
    # print(cnt)

    ## get().delete()
    # cnt = Student.objects.get(id=11).delete()
    # print(cnt)

    # filter().delete()
    cnt = Student.objects.filter(stu_name="pardasi").delete()
    print(cnt)    