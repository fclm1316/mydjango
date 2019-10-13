from django.db import models

# Create your models here.

#表名为类名
class Grades(models.Model):
    #不指定主键，自动创建自增长的主键
    #属性为字段
    gname = models.CharField(max_length=20)
    gdate = models.DateField()
    ggirlsum = models.IntegerField()
    gboysum = models.IntegerField()
    isDelete = models.BooleanField()
    # def __str__(self):
    #     return "{}-{}-{}-{}-{}".format(self.gname,self.gdate,self.ggirlsum,self.gboysum,self.isDelete)
    def __str__(self):
        return "{}:{}".format(self.gname,self.gdate)

class StudentsManager(models.Manager):
    def get_queryset(self):
        # 改写父类中的get_queryset() 带过滤object.all()
        return super(StudentsManager,self).get_queryset().filter(isDelete=False)
# 类方法创建对象。cls为student 楼下。两种方法
#     在管理器中添加
    def createstudent(self,name,gender,age,contend,isD,grade):
        stu = self.model()
        stu.sname = name
        stu.sgender = gender
        stu.sage = age
        stu.sconend = contend
        stu.isDelete = isD
        stu.sgrade = grade
        return stu


class Students(models.Model):
    #自定义模型管理器
    stuObj = models.Manager()
    stuObj2 = StudentsManager()
    sname = models.CharField(max_length=20)
    sgender = models.BooleanField(default=True)
    sage = models.IntegerField()
    sconend = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    #关联外键,需要指定。为了避免两个表里的数据不一致问题
    sgrade = models.ForeignKey("Grades",on_delete=models.CASCADE)
    def __str__(self):
        return self.sname ,self.sage
    # class Meta:
    # 定义表名 ，默认为:应用_表名
    #     db_table = 'students'
    #表排序正序['id'],倒序[-'id']
    #     ordering=['id']
# 最后一次修改时间
# modles.DataTimeField(auto_now=Ture)
# 创建时间
# modles.DataTimeField(auto_now_add=Ture)
    #类方法创建对象。cls为student
    #     在管理器中添加, 楼上 .两种方法
    @classmethod
    def createStudent(cls,name,gender,age,contend,isD,grade):
        stu = cls(sname = name,sgender=gender,sage=age,sconend=contend,isDelete=isD,sgrade=grade)
        return stu


        



