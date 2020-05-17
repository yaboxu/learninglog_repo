from django import forms #导入模块forms

from .models import Topic,Entry

class TopicForm(forms.ModelForm):
    """用于添加主题的表单"""
    class Meta: #没有()###
        model = Topic #根据模型Topic创建一个表单
        fields = ['text'] #该表单只包含字段text
        labels = {'text':''} #让Django不要为字段text生成标签
        

class EntryForm(forms.ModelForm):
    """用于添加新条目的表单"""
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text':''}
        widgets = {'text':forms.Textarea(attrs={'cols':80})}
