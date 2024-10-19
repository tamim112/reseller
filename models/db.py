# -*- coding: utf-8 -*-

#########################################################################

from gluon.tools import *

mail = Mail()  # mailer
auth = Auth(globals(), db)  # authentication/authorization
crud = Crud(globals(), db)  # for CRUD helpers using auth
service = Service(globals())  # for json, xml, jsonrpc, xmlrpc, amfrpc
plugins = PluginManager()

mail.settings.server = "logging" or "smtp.gmail.com:587"  # your SMTP server
mail.settings.sender = "you@gmail.com"  # your email
mail.settings.login = "username:password"  # your credentials or None

auth.settings.hmac_key = (
    "sha512:d6160708-08e3-4217-bd9e-e9a550109a8d"  # before define_tables()
)
# auth.define_tables()                           # creates all needed tables
auth.settings.mailer = mail  # for user email verification
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.messages.verify_email = (
    "Click on the link http://"
    + request.env.http_host
    + URL("default", "user", args=["verify_email"])
    + "/%(key)s to verify your email"
)
auth.settings.reset_password_requires_verification = True
auth.messages.reset_password = (
    "Click on the link http://"
    + request.env.http_host
    + URL("default", "user", args=["reset_password"])
    + "/%(key)s to reset your password"
)

#########################################################################

crud.settings.auth = None  # =auth to enforce authorization on crud

#########################################################################
# Common Variable
# mreporting_http_pass='abC321'
# ' " / \ < > ( ) [ ] { } ,

# ======================date========================
import datetime
import os

datetime_fixed = str(date_fixed)[0:19]  # default datetime 2012-07-01 11:48:10
current_date = str(date_fixed)[0:10]  # default date 2012-07-01

first_currentDate = datetime.datetime.strptime(
    str(current_date)[0:7] + "-01", "%Y-%m-%d"
)
# ================Master_Database===================
# --------------------------- signature
signature = db.Table(db,
    "signature",
    Field("field1", "string", default=""),
    Field("field2", "integer", default=0),
    Field("note", "string", default=""),
    Field("created_on", "datetime", default=date_fixed),
    Field("created_by", default=session.user_id),
    Field("updated_on", "datetime", update=date_fixed),
    Field("updated_by", update=session.user_id),
)
cid="RMS"
#============Main Table Start==================

# *********************************User Management***********************************************
# ---------------------------permission_groups Table-------------------------------------
db.define_table("permission_groups",
    Field("cid", "string",length=10,default=cid),
    Field("project","string",length=100),
    Field("group_name","string",length=100),
    Field("status", "string",length=10, requires=IS_IN_SET(("ACTIVE", "INACTIVE")), default="ACTIVE"),
    migrate=True
)
# ---------------------------permission_groups Table-------------------------------------

# ---------------------------permissions Table-------------------------------------
db.define_table("permissions",
    Field("cid", "string",length=10,default=cid),
    Field("group_id","integer"),
    Field("permission","string",length=200),
    Field("status", "string",length=10, requires=IS_IN_SET(("ACTIVE", "INACTIVE")), default="ACTIVE"),
    migrate=True
)
# ---------------------------permissions Table-------------------------------------

# ---------------------------role_has_permissions Table-------------------------------------
db.define_table("role_has_permissions",
    Field("cid", "string",length=10,default=cid),
    Field("group_id","integer"),
    Field("permission_id","string",length=200),
    Field("role","string",length=200),
    Field("status", "string",length=10, requires=IS_IN_SET(("ACTIVE", "INACTIVE")), default="ACTIVE"),
    migrate=True
)
# ---------------------------role_has_permissions Table-------------------------------------

# ---------------------------users Table-------------------------------------
db.define_table("users",
    Field("cid", "string",length=10,default=cid),
    Field("username","string",length=100),
    Field("email","string",length=100),
    Field("mobile","string",length=15),
    Field("password","string",length=15),
    Field("password_expire_date","date"),
    Field("pin_status","string",length=10,requires=IS_IN_SET(("YES", "NO")), default="NO"),
    Field("pin","string",length=10),
    
    Field("first_name","string",length=100),
    Field("last_name","string",length=100),
    Field("full_name","string",length=100),
    
    Field("address","string",length=100),
    Field("image","string",length=100),
    
    Field("role_id","integer"),
    Field("role","string",length=200),
    Field("status", "string",length=10, requires=IS_IN_SET(("ACTIVE", "INACTIVE")), default="ACTIVE"),
    migrate=True
)
# ---------------------------users Table-------------------------------------

# *********************************User Management***********************************************
