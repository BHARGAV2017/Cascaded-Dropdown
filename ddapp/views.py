from django.shortcuts import render
from django.db import connections

# Create your views here.
from ddapp.models import Country, State, District

with connections['nath'].cursor() as cursor:
    cursor.execute("SELECT * FROM sakila.actor LIMIT 10")
    obj = cursor.fetchone()
    print(obj)
    # for i in obj:
        # print(i)
    # print(obj)


# print("nath nath nath")
# cursor1 = connection.cursor()
# obj = cursor1.execute('SELECT * FROM sqlite_master WHERE type = "table"')

# for i in obj:
#     cursor2 = connection.cursor()
#     obj2 = cursor2.execute(f"PRAGMA table_info({i[1]})")
#     for j in obj2:
#         print(j)
#     print("******************************")
    # print(i[1])
# print(re.findall('a(.*)b', 'axyzb'))

# cursor3 = connection.cursor()
# obj3 = cursor3.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")

# for i in obj3:
    # if "REFERENCES" in i[1] :
    #     print(i)
    #     x = i[1].split(',')
    #     x = [coltab for coltab in i if (coltab.startswith('"') and coltab.endswith('"'))]
    #     print(x)
    # print(i)
#*************************************************************SCHEMA BLOCK ************************************************************************

# cursor4 = connection.cursor()
# obj4 = cursor4.executescript( """DROP TABLE IF EXISTS fklist;
#         DROP TABLE IF EXISTS master_copy;
#         DROP TRIGGER IF EXISTS load_fklist;
#         CREATE TABLE IF NOT EXISTS fklist AS SELECT '' AS child,* 
#             FROM pragma_foreign_key_list((SELECT name FROM sqlite_master WHERE type = 'not a type' LIMIT 1));
#             CREATE TABLE IF NOT EXISTS master_copy AS SELECT * FROM sqlite_master WHERE type = 'not a type';
#             CREATE TRIGGER IF NOT EXISTS load_fklist 
#             AFTER INSERT ON master_copy
#             BEGIN
#                 INSERT INTO fklist SELECT new.name,* FROM pragma_foreign_key_list(new.name);
#             END
#         ;
#         INSERT INTO master_copy SELECT * 
#             FROM sqlite_master 
#             WHERE type = 'table' 
#                 AND instr(sql,' REFERENCES ') > 0
#         ;
#         """
#         )
# cursor5 = connection.cursor()
# obj5 = cursor5.execute("SELECT * FROM fklist")  

# schema_map= {}
# for i in obj5:
#     schema_map[i[0]]= i
    # print(i)

# cursor6 = connection.cursor()
# obj6 = cursor6.executescript("""
#         SELECT * FROM fklist;
#         DROP TABLE IF EXISTS fklist;
#         DROP TABLE IF EXISTS master_copy;
#         DROP TRIGGER IF EXISTS load_fklist;
#         """)
    
# print(schema_map)
#************************************************************* SCHEMA BLOCK ************************************************************************


#************************************************************* VALUES BLOCK ************************************************************************
# user give parent table that provides a dropdown list of relational table >> then user can select on each table what column they want to choose >> then pick the all column values give the final result of the  query.
def get_no_inputfields():
    return schema_map.keys()
# when user click the 1st keys then input field box opens up then for 2nd and so forth & frontend create input field accordingly . 
# for a in schema_map.keys():
    # if request.GET.get(a) != None:
        

# inp = request.GET.get('country', None) # input from the user 
# cursor7 = connection.cursor()
# obj7 = cursor7.execute(f"""SELECT """)
#************************************************************* VALUES BLOCK ************************************************************************
def dependantfield(request):
    countryid = request.GET.get('country', None)
    stateid = request.GET.get('state', None)
    state = None
    district = None
    # print("request_like",request)
    if countryid:
        getcountry = Country.objects.get(id= countryid)
        state = State.objects.filter(country= getcountry)

    if stateid:
        getstate = State.objects.get(id= stateid)
        district = District.objects.filter(state= getstate)
    
    country = Country.objects.all()
    
    return render(request,'dependantfield.html', locals())
    # return request
