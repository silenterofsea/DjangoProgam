from django.db import models

# Create your models here.


class ProductsList(models.Model):
    pro_title = models.CharField('标题', max_length=30, null=False)
    pro_introduction = models.CharField('简单介绍', max_length=140, null=False)
    pro_img_face = models.ImageField('封面图片', upload_to='products_upload_images/')
    pro_information = models.TextField('详细介绍', max_length=1000, null=False)
    pro_time = models.DateTimeField('更新时间', null=True)

    def __str__(self):
        return self.pro_title

    class Meta:
        verbose_name = "案例列表"
        verbose_name_plural = '案例列表'


class ClientInfo(models.Model):
    client_name = models.CharField('客户名', max_length=10, null=False)
    client_email = models.EmailField('客户邮箱', null=True)
    client_phone = models.CharField('客户电话', max_length=20, null=False)
    client_message = models.CharField('客户留言', max_length=200, null=True)

    def __str__(self):
        return self.client_name

    class Meta:
        verbose_name = "客户留言"
        verbose_name_plural = "客户留言(时不时看一下，可能会有客户留言)"


class MyCompanyInfo(models.Model):
    my_name = models.CharField('公司名称', max_length=20, null=False, default="请在后台修改公司名称")
    my_add = models.CharField('公司地址', max_length=30, blank=True, null=False, default="City of the Hill")
    my_email = models.EmailField('公司邮箱', null=False, default="请在后台修改公司信息")
    my_phone = models.CharField('公司电话', null=False, default='15924239167', max_length=11)
    my_qq = models.CharField('公司QQ', null=False, default='303070738', max_length=12)

    def __str__(self):
        return self.my_name

    class Meta:
        verbose_name = "本公司信息"
        verbose_name_plural = "本公司信息"
