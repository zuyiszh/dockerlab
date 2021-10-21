#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

from django.shortcuts import render
from qytdb.models import Courses
from qytdb.forms import AddCourseForm


# 查看课程
def courses(request):
    courses_list = [{'department': c.department,
                     'course_name': c.course_name,
                     'description': c.description} for c in Courses.objects.all()]

    return render(request, 'courses.html', {'courses_list': courses_list})


# 添加课程
def addcourse(request):
    if request.method == 'POST':
        form = AddCourseForm(request.POST)
        # 如果请求为POST,并且Form校验通过,把新添加的学员信息写入数据库
        if form.is_valid():
            student = Courses(department=request.POST.get('department'),
                              course_name=request.POST.get('course_name'),
                              description=request.POST.get('description'))
            student.save()
            # 写入成功后,显示'学员添加成功'信息!,并且显示空表单
            form = AddCourseForm()
            return render(request, 'add_course.html', {'form': form,
                                                       'successmessage': '添加课程成功!'})

        else:  # 如果Form校验失败,返回客户在Form中输入的内容和报错信息
            # 如果检查到错误,会添加错误内容到form内,例如:<ul class="errorlist"><li>QQ号码已经存在</li></ul>
            return render(request, 'add_course.html', {'form': form})
    else:  # 如果不是POST,就是GET,表示为初始访问, 显示表单内容给客户
        form = AddCourseForm()
        return render(request, 'add_course.html', {'form': form})
