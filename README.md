# django-vue-nuxt
基于django rest framework 后台开发 ，/vue/nuxt 前端分离快速入手demo

此分支，是初始的django项目，还没进行rest-framework配置
## 创建django项目

首先要清楚Django-Rest-Framework只是一个django工具包，用于构建Web API

### 为什么要使用Rest Framework

Django REST Framework可以在Django的基础上迅速实现API，并且自身还带有WEB的测试页面，可以方便的测试自己的API

### 和Django的区别

Rest Framework只是在django的基础上继承django的视图类(view),进行的API接口开发，实现了APIView类
，同时也封装了一部分路由功能所以对于熟练使用django的小伙伴来说，使用django-rest-framework还是很轻松的

