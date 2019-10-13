from django.contrib import admin

# Register your models here.
from . models import Grades,Students
#关联对象继承类
class StudentsInfo(admin.TabularInline):
    #数据库表
    model = Students
    #俩列
    extra = 2
#注册
class GradesAdmin(admin.ModelAdmin):
    #添加页面中直接增加
    inlines = [StudentsInfo]
    #列表页属性
    list_display = ['pk','gname','gdate','ggirlsum','gboysum','isDelete']  #显示字段
    list_filter = ['gname']  #过滤器
    list_per_page = 20  #分页
    search_fields = ['gname','gdate'] #搜索器
   #添加、修改页属性。不能同时使用
    # fields = ['gdate','gname','ggirlsum','gboysum','isDelete']   #添加时的顺序
    fieldsets = [
        ("num",{"fields":['ggirlsum','gboysum']}),
        ("base",{"fields":['gname','gdate','isDelete']}),
    ] #给属性分组
class StudentsAdmin(admin.ModelAdmin):
    #布尔值显示问题
    def gender(self):
        if self.sgender:
            return "男"
        else:
            return "女"
    #页面列的名称
    gender.short_description = '性别'
    # list_display = ['pk','sname','sgender','sage','sconend','isDelete',]
    list_display = ['pk','sname',gender,'sage','sconend','isDelete',]
    list_per_page = 20  #分页
    search_fields = ['sname','sage'] #搜索器
    # actions_on_bottom = False # 执行动作


admin.site.register(Grades,GradesAdmin)
admin.site.register(Students,StudentsAdmin)
