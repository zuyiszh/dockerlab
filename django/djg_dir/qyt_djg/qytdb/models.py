from django.db import models


# 课程
class Courses(models.Model):
    # 部门
    department = models.CharField(max_length=100, verbose_name='部门名称')
    # 课程名称
    course_name = models.CharField(max_length=100, unique=True, verbose_name='课程名称')
    # 课程描述
    description = models.CharField(max_length=100, blank=True, null=True, verbose_name='课程描述')
    # 修改时间
    change_datetime = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    # 创建时间
    create_datetime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return f"{self.__class__.__name__}(课程名称: {self.course_name} | 部门: {self.department})"

