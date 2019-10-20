from django.db import models

# Create your models here.


class CompanyData(models.Model):
    company_name = models.CharField('首页：公司名字', max_length=128, null=True)
    company_add = models.CharField('首页：公司地址', max_length=128, null=True)
    company_phone_nub = models.CharField('首页：公司电话', max_length=16, null=True)
    company_email = models.CharField('首页：公司邮件', max_length=20, null=True)
    company_key_word = models.CharField('首页：公司属性（SEO）', max_length=60, null=True)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = '首页：公司信息'
        verbose_name_plural = '首页：公司信息'


class FourInfo(models.Model):
    four_title = models.CharField('四个字中的一个', max_length=5, null=False)
    four_one_words = models.CharField('四个标题中的一个', max_length=10, null=False)
    four_detail_words = models.TextField('详细介绍', max_length=500, null=False)
    # four_word_small_img = models.ImageField()
    # four_word_big_img = models.ImageField()

    def __str__(self):
        return self.four_title

    class Meta:
        verbose_name = '首页：四个案例信息'
        verbose_name_plural = '首页：四个案例信息'
