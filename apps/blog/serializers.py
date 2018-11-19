# -*- coding:utf-8 -*-
from rest_framework import serializers
from .models import Tag, Blog


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'tag_name')


class BlogSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = ('id', 'caption', 'content', 'tags')

