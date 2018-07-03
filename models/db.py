from gluon.contrib.appconfig import AppConfig
configuration  = AppConfig(reload=True)


db = DAL("sqlite://storage.sqlite")
db.define_table("users",
                 Field('db_fullname'),
                 Field('db_email'),
                 Field('db_password'),
                 Field('db_phone')) 


db.define_table("register",
                Field('db_fullname'),
                Field('db_email'),
                Field('db_password'),
                Field('db_phone'),
                Field('db_gender'))
	