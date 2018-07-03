
def signup():
    return dict()

def store():
    submitted_fullname = request.vars.fullname
    submitted_email = request.vars.email
    submitted_password = request.vars.password
    submitted_phone = request.vars.phone

    results = db.users.insert(
        db_fullname = submitted_fullname,
        db_email = submitted_email,
        db_password = submitted_password,
        db_phone= submitted_phone,
    )

    if results:
        return "User Saved Successfully"
    else:
        return "An error Occured"




def login():
    return dict()

def homepage():
    return dict()

def aboutus():
    return dict()

def register():
    return dict()     


def authenticate():
    submitted_email = request.vars.email
    submitted_password = request.vars.password

    if db(db.users.db_email==submitted_email
            and db.users.db_password==submitted_password).count()>0:
        return  redirect(URL('homepage'))

    else:
        return "User Not found. Please Sign up" 





def register():
    return dict()

def store():
    submitted_fullname = request.vars.fullname
    submitted_email = request.vars.email
    submitted_password = request.vars.password
    submitted_phone = request.vars.phone
    submitted_gender = request.vars.gender


    results = db.register.insert(
        db_fullname = submitted_fullname,
        db_email = submitted_email,
        db_password = submitted_password,
        db_phone = submitted_phone,
        db_gender= submitted_gender,

    )

    if results:
        return "User Saved Successfully"
    else:
        return "An error Occured"




