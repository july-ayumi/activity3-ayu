from django.db import models
from django.utils import timezone

class Department(models.Model):
    name = models.CharField('部署名' ,max_length=20)

    def __str__(self):
        return self.name


#class ToDo(models.Model):
    #name = models.CharField('TODO', max_length=50)
    #create_at = models.DateTimeField('日付', default=timezone.now)

    #def __str__(self):
        #return self.name

class DateModel(models.Model):
    date_field = models.DateField()

class Employee(models.Model):
    name = models.CharField('名前', max_length=50)
    #他のモデルと紐づくようになるForeignkey
    department = models.ForeignKey(
        Department, verbose_name = '部署', on_delete=models.PROTECT,
    )
    todo = models.CharField('TODO', max_length=50)
    #todo = models.ManyToManyField(
        #ToDo, verbose_name = 'TODO',
    #)
    due = models.DateField('期日', default=timezone.now)
    tododetail = models.CharField('詳細', max_length=100, default='---')
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField('日付', default=timezone.now)

    def __str__(self):
        return '{0}{1}{2}{3}'.format(self.name, self.department, self.todo, self.due)

class Login(models.Model):
    login_id = models.CharField('ログインID', max_length=20)
