
def index():
    response.flash = T("Hello World")
    return dict(message=T('Welcome to web2py!'))

def create():
    response.flash = T("Hello World")
    return locals()
def submit():
    redirect(URL("users","index"))
    return locals()