
def index():
    
    return locals()
def create():
    
    return locals()
def submit():
    project = request.vars.project
    group_name = request.vars.group_name
    status = "ACTIVE" if str(request.vars.status) == "ACTIVE" else "INACTIVE"
    
    db.permission_groups.insert(
        project=project,
        group_name=group_name,
        status=status
    )
    
    redirect(URL("permission_group","index"))
    return locals()