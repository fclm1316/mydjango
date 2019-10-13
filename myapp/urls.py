#encoding:utf-8
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #整型参数
    #匹配数字
    # path('<int:detail_id>', views.detail_id, name='detail'),
    #匹配字符串
    # path('<int:detail_id>/<str:detail_id_name>', views.detail_id_name, name='detail_id_name'),
    #匹配由ASCII字母或数字组成的任何slug字符串，以及连字符和下划线字符
    # path('<slug:detail>', views.detail, name='detail'),
# uuid：匹配一个uuid格式的对象。为了防止冲突，规定必须使用破折号，所有字母必须小写，
    # 例如’075194d3-6885-417e-a8a8-6c931e272f00‘ 。返回一个UUID对象；
    path('grades/',views.grades),
    path('gradesF/',views.gradesF),
    path('students/',views.students),
    path('students/<int:page>',views.setupage),
    path('search/',views.studentsearch),
    path('search2/',views.studentsearch2),
    path('grades/<int:id>', views.gradesStudenst),
    path('add/', views.addStudent),
    path('add2/', views.addStudent2),
    path('showregist/', views.showregist),
    path('showregist/regist/', views.regist),
    path('attrible/', views.attrible),
    path('get1/', views.get1),
    path('get2/', views.get2),
    path('cookietest/', views.cookietest),
]