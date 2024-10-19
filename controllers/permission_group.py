
def index():
    
    return locals()
def create():

    return locals()

def submit():
    errors=[]
    project = request.vars.project
    group_name = request.vars.group_name
    status = "ACTIVE" if str(request.vars.status) == "ACTIVE" else "INACTIVE"
    
    if not project:
        errors.append('Project Name is Required.')
    if not group_name:
        errors.append('Group Name is Required.')
        
    if errors:
        msg = ''
        for item in errors:
            msg = msg + item + ' <br>'
        session.flash = {"msg_type":"error","msg":msg}
        redirect (URL('permission_group','create'))
    
    db.permission_groups.insert(
        project=project,
        group_name=group_name,
        status=status
    )
    session.flash = {"msg_type":"success","msg":"Group successfully Added!"}
    redirect(URL("permission_group","index"))
    return locals()

def edit():

    return locals()


def get_data():
    status = request.vars.status
    print("aaaaaa")
    print(status)
    #Search Start##
    conditions = ""
    if  request.vars.group_name != None and request.vars.group_name !='':
        group_name = str(request.vars.group_name)
        conditions += " and group_name = '"+group_name+"'"
    # if  request.vars.designation_name != None and request.vars.designation_name !='':
    #     conditions += " and id = '"+str(request.vars.designation_name)+"'"
    if  request.vars.status != None and request.vars.status != '':
        status = request.vars.status
        print(status)
        conditions += " and status = '"+status+"'" 
    #Search End## 

    ##Paginate Start##     
    total_rows = len(db.executesql( "SELECT * FROM `permission_groups` where 1" + conditions, as_dict=True)) 
    page = int(request.vars.page or 1)
    rows_per_page = int(request.vars.rows_per_page or 10)
    if rows_per_page == -1:
        rows_per_page = total_rows
    start = (page - 1) * rows_per_page         
    end = rows_per_page
    ##Paginate End##

    ##Ordering Start##
    sort_column_index = int(request.vars['order[0][column]'] or 0)
    if sort_column_index == 0:
        sort_column_index = 1 #defult sorting column define
    sort_column_name = request.vars['columns[' + str(sort_column_index) + '][data]']
    sort_direction = request.vars['order[0][dir]']
    ##Ordering End##

    ##Querry Start##
    sql = """
    SELECT * FROM `permission_groups` where 1"""+conditions+""" ORDER BY """+sort_column_name+""" """+sort_direction+""" LIMIT """+str(start)+""","""+str(end)+""";
    """
    data = db.executesql(sql, as_dict=True)
    ##Qurry End##

    return dict(data=data, total_rows=total_rows,recordsFiltered=total_rows,recordsTotal=total_rows,sort_column_name=sort_column_name)

