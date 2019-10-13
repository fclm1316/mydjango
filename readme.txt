使用虚拟环境
pip install virtualenvwrapper-win
mkvirtualenv envname
workon envname
deactivate
rmvirtualenv
创建项目
django-admin.py startproject testdj
cd testdj
创建应用
python manager.py appname
生成数据库文件
python manage.py makemigrations
生成数据库表(settings.py)
python manage.py migrate


python manage.py shell
创建对象
对象.属性=值
对象.save()
类名.boject.all()
类名.boject.get(pk=2)
对象.delete()
python manage.py createsuper

1 定义html模板
2 myapp 下 url 匹配
3 分发views视图
4 views.py 获取数据
5 将数据渲染返回给 html模板  setting.py 模板目录配置


1 定义视图
2 配置url
3 定义模板



最后一次修改时间
modles.DataTimeField(auto_now=Ture)
创建时间
modles.DataTimeField(auto_now_add=Ture)

#所有
all()
#包含  =
filter(key=value)
#不包含 !=
exclude()
#排序
order_by()
#一条数据就是一个对象，返回一个列表
values()

返回单个数据
get() 返回一个满足条件的对象 如果没有找到符合的对象，会引发模型doesnotexist异常
        如果找到多个对象，会引发模型类 异常

count() 返回对象集的个数

first() 返回查询集的一个对象
last() 返回查询集的最后对象

exists() 判断是否有数据 有Ture



