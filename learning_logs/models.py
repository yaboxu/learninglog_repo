from django.db import models #导入模块models
from django.contrib.auth.models import User #修改模型Topic

# Create your models here. #创建自己的模型
class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User) #修改模型Topic
    
    def __str__(self):
        """返回模型的字符串表示"""
        return self.text

class Entry(models.Model):
    """学到的有关每个主题的具体知识"""
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.TextField() #别忘了()
    date_added = models.DateTimeField(auto_now_add=True)
    
    
    class Meta: #Entry类嵌套Meta类，没有()
        verbose_name_plural = 'entries'
        
    def __str__(self):
        """返回模型的字符串表示"""
        if len(self.text) > 50:
            return self.text[:50] + "..."
        else:
            return self.text 
