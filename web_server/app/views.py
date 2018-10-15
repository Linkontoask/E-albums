# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from app.models import Picture, Media, PhotoAlbum
import json
import datetime


# Create your views here.
def create_album(request):
    if request.method == "GET":
        temp_get_data = request.GET
        photo_album = PhotoAlbum(
            name=temp_get_data.get("name"),
            point=temp_get_data.get("point"),
            createTime=datetime.datetime.now().strftime('%Y-%m-%d'),
        )
        photo_album.save()
    return HttpResponse({"data": {"success": "e"}})


def upload(request):
    if request.method == "POST":
        print (request.FILES.get("file"), type(request.FILES.get("file")))
        temp_file = request.FILES.get("file")
        if request.POST.get("type") == "picture":
            img = Picture(
                file=temp_file,
                name=temp_file.name,
                size=temp_file.size,
                point=request.POST.get("point", None),
                title=request.POST.get("title", None),
                album=PhotoAlbum.objects.filter(id=request.POST.get("album_id")).first(),
                date=datetime.datetime.now().strftime('%Y-%m-%d')
            )
            img.save()
            obj = PhotoAlbum.objects.filter(id=request.POST.get("album_id"))
            length = Picture.objects.filter(album_id=obj)
            print (len(length), type(length))
            obj.update(count=len(length))
            return HttpResponse(json.dumps({"data": {"e": 0, "code": "success"}}), content_type="application/json")
        else:
            media = Media(
                file=temp_file,
                name=temp_file.name,
                size=temp_file.size,
                point=request.POST.get("point", None),
                title=request.POST.get("title", None),
                date=datetime.datetime.now().strftime('%Y-%m-%d')
            )
            media.save()
            return HttpResponse(json.dumps({"data": {"e": 0, "code": "success"}}), content_type="application/json")
    return HttpResponse(json.dumps({"data": {"e": -1, "code": "{} method don't allow".format(request.method)}}),
                        content_type="application/json")


def get_picture(request):
    img = Picture.objects.all()
    data = json.dumps(
        {"data": [{"id": i.id, "url": i.file.url, "name": i.name, "point": i.point, "date": i.date, "title": i.title}
                  for i in img]})
    return HttpResponse(data)


def get_album(request):
    if request.method == "POST":
        album_type = json.loads(request.body.decode()).get("type")
        if album_type == "all":
            album_all = PhotoAlbum.objects.all()
            data = json.dumps(
                {"data": [{"title": i.name, "point": i.point, "createTime": i.createTime, "id": i.id,
                           "url": Picture.objects.filter(album_id=i.id).first().file.url}
                          for i in album_all]})
            return HttpResponse(data)
        else:
            obj = PhotoAlbum.objects.filter(id=json.loads(request.body.decode()).get("album_id")).first()
            data_obj = Picture.objects.filter(album_id=obj)
            data = json.dumps({"data": [{"url": i.file.url,
                                         "size": i.size, "name": i.name,
                                         "point": i.point, "createTime": i.date,
                                         "title": i.title}
                                        for i in data_obj]})
            return HttpResponse(data)
    return HttpResponse(json.dumps({"data": {"e": -1, "code": "{} method don't allow".format(request.method)}}),
                        content_type="application/json")


def get_album_info(request):
    if request.method == "POST":
        album_key_value = PhotoAlbum.objects.all()
        data = json.dumps({"data": [{"label": i.name, "value": i.id} for i in album_key_value]})
        return HttpResponse(data)
    return HttpResponse(json.dumps({"data": {"e": -1, "code": "{} method don't allow".format(request.method)}}),
                        content_type="application/json")


def get_media(request):
    media = Media.objects.all()
    data = json.dumps(
        {"data": [{"id": i.id, "url": i.file.url, "name": i.name, "point": i.point, "date": i.date} for i in media]})
    return HttpResponse(data)
