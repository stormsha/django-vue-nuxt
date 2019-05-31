from django.shortcuts import HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
from link import models
from link.utils.CustomSerializer import MeSerializers as Ser
import json


class LinksView(APIView):

    def get(self, request, *args, **kwargs):

        # 获取数据库全部数据
        links = models.Links.objects.all()
        ser = Ser.LinksSerializer(instance=links, many=True)
        data = json.dumps(ser.data, ensure_ascii=False)
        return HttpResponse(data)





