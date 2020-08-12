import json
from peewee import *

"""
Host
ec2-46-137-113-157.eu-west-1.compute.amazonaws.com
Database
d43638j1mqjsms
User
lmujffhuwvdwlq
Port
5432
Password
b5831431d3051c1d92186990331a34506481c652cf5fd52f0c56aad5a12b87b6
URI
postgres://lmujffhuwvdwlq:b5831431d3051c1d92186990331a34506481c652cf5fd52f0c56aad5a12b87b6@ec2-46-137-113-157.eu-west-1.compute.amazonaws.com:5432/d43638j1mqjsms
Heroku CLI
heroku pg:psql postgresql-asymmetrical-92635 --app fmaatombot1
"""


def get_db():
    password = "b5831431d3051c1d92186990331a34506481c652cf5fd52f0c56aad5a12b87b6"
    db_name = "d43638j1mqjsms"
    user = 'lmujffhuwvdwlq'
    host = "ec2-46-137-113-157.eu-west-1.compute.amazonaws.com"
    return PostgresqlDatabase(db_name, user=user, password=password,
                              host=host, port=5432)


class BaseModel(Model):
    class Meta:
        database = get_db()


class AbitsFMA1(BaseModel):
    id = AutoField(null=False)
    number = CharField(max_length=7, null=True, default=None)

    class Meta:
        table_name = "abitsFMA1"


class AbitsFMA1consent(BaseModel):
    id = AutoField(null=False)
    number = CharField(max_length=7, null=True, default=None)

    class Meta:
        table_name = "abitsFMA1consent"


class AbitsFMA3consent(BaseModel):
    id = AutoField(null=False)
    number = CharField(max_length=7, null=True, default=None)

    class Meta:
        table_name = "abitsFMA3consent"


class AbitsFMA3(BaseModel):
    id = AutoField(null=False)
    number = CharField(max_length=7, null=True, default=None)

    class Meta:
        table_name = "abitsFMA3"


class AbitsFEN1(BaseModel):
    id = AutoField(null=False)
    number = CharField(max_length=7, null=True, default=None)

    class Meta:
        table_name = "abitsFEN1"


def fma1Select():
    query = AbitsFMA1.select(AbitsFMA1.number)
    fma1 = []
    for i in query:
        fma1.append(i.number)
    return fma1

def newFma1(abitList):
    AbitsFMA1.delete().execute()
    for i in abitList:
        AbitsFMA1(number='{}'.format(i)).save()


def fma1consentSelect():
    query = AbitsFMA1consent.select(AbitsFMA1consent.number)
    fma1 = []
    for i in query:
        fma1.append(i.number)
    return fma1

def fma3consentSelect():
    query = AbitsFMA3consent.select(AbitsFMA3consent.number)
    fma3 = []
    for i in query:
        fma3.append(i.number)
    return fma3

def newFma1consent(abitList):
    AbitsFMA1consent.delete().execute()
    for i in abitList:
        AbitsFMA1consent(number='{}'.format(i)).save()

def newFma3consent(abitList):
    AbitsFMA3consent.delete().execute()
    for i in abitList:
        AbitsFMA3consent(number='{}'.format(i)).save()


def fma3Select():
    query = AbitsFMA3.select(AbitsFMA3.number)
    fma3 = []
    for i in query:
        fma3.append(i.number)
    return fma3

def newFma3(abitList):
    AbitsFMA3.delete().execute()
    for i in abitList:
        AbitsFMA3(number='{}'.format(i)).save()

def fen1Select():
    query = AbitsFEN1.select(AbitsFEN1.number)
    fen1 = []
    for i in query:
        fen1.append(i.number)
    return fen1

def newFen1(abitList):
    AbitsFEN1.delete().execute()
    for i in abitList:
        AbitsFEN1(number='{}'.format(i)).save()
        
a=get_db().create_tables([AbitsFMA3consent])
newFma3consent()
