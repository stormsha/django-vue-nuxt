from django.db import models

# Create your models here.


class Keyword(models.Model):
    """
    关键词，用来作为 SEO 中 keywords
    """
    name = models.CharField('关键词', max_length=64)
    source = models.IntegerField(default=0, verbose_name="关键词来源")


class Sort(models.Model):
    """
    网址分类表
    """
    name = models.CharField('分类', max_length=20)
    order = models.IntegerField('分类顺序', help_text="从上一个分类往后排")
    description = models.TextField('描述', max_length=240, default="用于SEO",
                                   help_text='用来作为SEO中description,长度参考SEO标准')


class Tags(models.Model):
    """
    网址标签表
    """
    name = models.CharField('分类', max_length=64)
    description = models.TextField('描述', max_length=240, default="用于SEO",
                                   help_text='用来作为SEO中description,长度参考SEO标准')


class Links(models.Model):
    """
    网址表
    """
    name = models.CharField(max_length=32, verbose_name="网址名称")
    url = models.CharField(max_length=128, verbose_name='网址')

    icon = models.CharField(max_length=128, default='/static/logo@1x.png', verbose_name='logo')
    sort = models.ForeignKey(Sort, verbose_name='网址分类', blank=True, null=True, on_delete=models.CASCADE)

    tags = models.ManyToManyField(Tags, verbose_name="网址标签")
    keywords = models.ManyToManyField(Keyword, verbose_name='文章关键词',
                                      help_text='文章关键词，用来作为SEO中keywords，最好使用长尾词，3-4个足够')

    def __str__(self):
        return self.name

