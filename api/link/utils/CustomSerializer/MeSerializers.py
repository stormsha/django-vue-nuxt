from rest_framework import serializers
from link import models


class LinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Links
        fields = "__all__"
        # 连表查询
        depth = 0

