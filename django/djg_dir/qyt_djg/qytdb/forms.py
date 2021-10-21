from django import forms


class AddCourseForm(forms.Form):
    # 为了添加必选项前面的星号
    # 下面是模板内的内容
    """
    < style type = "text/css" >
    label.required::before
    {
        content: "*";
    color: red;
    }
    < / style >
    """
    required_css_class = 'required'  # 这是Form.required_css_class属性, use to add class attributes to required rows
    # 添加效果如下
    # <label class="required" for="id_name">学员姓名:</label>
    # 不添加效果如下
    # <label for="id_name">学员姓名:</label>

    # 学员姓名,最小长度2,最大长度10,
    # label后面填写的内容,在表单中显示为名字,
    # 必选(required=True其实是默认值)
    # attrs={"class": "form-control"} 主要作用是style it in Bootstrap
    department = forms.CharField(max_length=10,
                                 label='部门',
                                 widget=forms.TextInput(attrs={'class': "form-control"}))
    course_name = forms.CharField(max_length=10,
                                  label='课程',
                                  widget=forms.TextInput(attrs={'class': "form-control"}))
    description = forms.CharField(max_length=100,
                                  label='描述',
                                  widget=forms.TextInput(attrs={'class': "form-control"}))