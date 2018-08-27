#!/usr/bin/env python
# -*- coding:utf-8 -*-

from app1.models import *
from Zadmin.service import zadmin

zadmin.site.register(Book)
