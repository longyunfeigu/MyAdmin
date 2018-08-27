#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.conf.urls import url
from django.shortcuts import render

class ZModelAdmin(object):
    def __init__(self, model, site):
        self.model = model
        self.site = site

    def addView(self, request):
        return render(request, 'add_view.html')

    def listView(self, request):
        data_list = self.model.objects.all()
        return render(request, 'list_view.html', {'data_list': data_list})

    def changeView(self, request,nid):
        return render(request, 'change_view.html')

    def deleteView(self, request,nid):
        return render(request, 'delete_view.html')

    def get_urls(self):
        temp = []
        temp.append(url("^$", self.listView))
        temp.append(url("^add/", self.addView))
        temp.append(url("^(\d+)/delete", self.deleteView))
        temp.append(url("^(\d+)/change", self.changeView))
        return temp

class ZAdminSite(object):
    def __init__(self):
        self._registry = {}

    def register(self, model, admin_class=None, **options):
        if not admin_class:
            admin_class = ZModelAdmin
        if model not in self._registry:
            self._registry[model] = admin_class(model, self)
    def get_urls(self):
        temp = []
        for model, admin_class_obj in self._registry.items():
            temp.append(url('^%s/%s/'%(model._meta.app_label, model._meta.model_name), (admin_class_obj.get_urls(), None, None)))
        return temp
    @property
    def urls(self):
        return self.get_urls(), None, None

site = ZAdminSite()