from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("work hard")

# def detail(request,detail):
#     return HttpResponse("detail {0:s}".format(detail))
#
# def detail_id(request,detail_id):
#     return HttpResponse("detail %s"%detail_id)
#
# def detail_id_name(request,detail_id,detail_id_name):
#     return HttpResponse("detail id :{0:d}  name : {1:s}".format(detail_id,detail_id_name))

from . models import Grades,Students
def grades(request):
#     获取数据.object.get()
    gradesList = Grades.objects.all()
#     将数据给模板,模板在渲染页面，将渲染好的页面返回给浏览器
# {“grades”:} 模板中定义的变量
    return render(request,'myapp/grades.html',{"grades":gradesList})

def gradesStudenst(request,id):
    #pk 主键
    grade = Grades.objects.get(pk=id)
    #关联键获得学生
    studentList = grade.students_set.all()
    return render(request,'myapp/students.html',{'students':studentList})

def students(request):
    studentList = Students.stuObj.all()
    # models中改写了object.all()
    # studentList = Students.stuObj2.all()
    return render(request,'myapp/students.html',{"students":studentList})


#以下两种为数据库添加数据
#模型中类方法添加
#管理器方式添加
def addStudent(request):
    #获得班级为 1 的班级
    grade = Grades.objects.get(pk=1)
    stu = Students.createStudent("闪电",True,23,"巴里",False,grade)
    #保存到数据库
    stu.save()
    return HttpResponse('add')

def addStudent2(request):
    #获得班级为 1 的班级
    grade = Grades.objects.get(pk=1)
    stu = Students.stuObj2.createstudent("绿箭",True,23,"奥利",False,grade)
    #保存到数据库
    stu.save()
    return HttpResponse('add')

# 分页问题
def setupage(request,page):
    page = int(page)
    #通过下标，切片的方式显示
    # [0:2]
    studentList = Students.stuObj2.all()[(page -1 )* 2 : page * 2 ]
    return render(request,'myapp/students.html',{"students":studentList})

def studentsearch(request,):
    #使用双下划线
    #区分大小写。iexact , icontains,istartwith，前面加i不区分
    #sql 中的 like.%占位。不需要转移
    # studentList = Students.stuObj.filter(sname__contains='超')
    # 开始
    # studentList = Students.stuObj.filter(sname__startswith="大")
    # 结束
    # studentList = Students.stuObj.filter(sname__endswith='超')
    # in
    # studentList = Students.stuObj.filter(id__in=[2,4,6,8])
    #gt gte lt lte 大于 大于等于  小于  小于等于
    studentList = Students.stuObj.filter(sage__gt=20)
    # studentList = Students.stuObj.filter(lastTime__year=2017)
    #关联查询。查询学生表中scoend 包含 '杭州' 描述，对应外键grades模型中返回的值
    grade = Grades.objects.filter(students__sconend__contains='杭州')
    print(grade)
    return render(request,'myapp/students.html',{"students":studentList})

from django.db.models import Max,Min,Sum,Count
#使用聚合函数
def studentsearch2(request,):
    MaxAge= Students.stuObj.aggregate(Max("sage"))
    for key,value in MaxAge.items():
        return HttpResponse('{} -- {}'.format(key,value))

from django.db.models import F,Q
#F对象 同一个对象的两个属性比较
def gradesF(request):
    #比较 女生数量大于男生数量。可以接受时间或者数量加减
    # studentList = Grades.objects.filter(ggirlsum__gt=F('gboysum')+10)
    # return render(request,'myapp/students.html',{"students":studentList})
# 查询中的 or 查询
    studentList = Students.stuObj.filter(Q(id__gt=3) | Q(sage__gt=35))
    # studentList = Students.stuObj.filter(Q(id__gt=3))
    # 取反
    # studentList = Students.stuObj.filter(~Q(id__gt=3))
    return render(request,'myapp/students.html',{"students":studentList})

def regist(request):
    name = request.POST.get("name")
    gender = request.POST.get("gender")
    age = request.POST.get("age")
    hobby = request.POST.getlist("hobby")
    return HttpResponse("POST 获取到的数据:"+  name +" , "+ gender+" , " + age+" , " + str(hobby))


def showregist(request):
    return render(request,'myapp/regist.html')

def attrible(request):
    print(request.path)
    print(request.encoding)
    print(request.method)
    print(request.GET)
    print(request.POST)
    print(request.FILES)
    print(request.COOKIES)
    print(request.session)
    return HttpResponse("attrible")

#获取get的传递数据
# http://127.0.0.1:8000/get1?a=1&b=2&c=3
#get 要求单一值
def get1(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    c = request.GET.get('c')
    return HttpResponse(a + " " + b + " " + c)

# http://127.0.0.1:8000/get1?a=1&a=2&c=3
def get2(request):
    a = request.GET.getlist('a')
    a1 = a[0]
    a2 = a[1]
    c = request.GET.get('c')
    return HttpResponse(a1 + " " + a2 + " " + c)


def cookietest(request):
    res = HttpResponse()
    # 写入cookie
    # cookie = request.COOKIES
    # res.write(cookie['man'])
    #设置cookie,(key,value)
    cookie = res.set_cookie("man","good")
    #
    # delete_cookie(key)
    return res
