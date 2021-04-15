# -*- coding: utf-8 -*-

from peewee import *

db = SqliteDatabase("mattos_proxie.db")
db.connect()

class ProxieList(Model):
    id = IntegerField(primary_key=True)
    hostname = CharField(max_length=100, null=False)
    port = CharField(max_length=10, null=False)
    id_country = CharField(max_length=10, null=False)
    country = CharField(max_length=50, null=False)
    anonymity = CharField(max_length=100, null=False)
    google = CharField(max_length=10, null=False)
    https = CharField(max_length=10, null=False)
    last_checked = CharField(max_length=10, null=False)

    class Meta:
        database = db

db.create_tables([ProxieList])
