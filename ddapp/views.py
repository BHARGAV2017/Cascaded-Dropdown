# NOTE : No need to do migrate database--name. 
# NOTE : For sqllite use executescript for multiple line command.
#************************************************** Mysql *******************************************
# for showing all fk relations for all db
"""
select *
from INFORMATION_SCHEMA.TABLE_CONSTRAINTS
where CONSTRAINT_TYPE = 'FOREIGN KEY'
"""
# for showing all fk relations for specific db
"""
SELECT 
  TABLE_NAME,COLUMN_NAME,CONSTRAINT_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME
FROM
  INFORMATION_SCHEMA.KEY_COLUMN_USAGE
WHERE
  REFERENCED_TABLE_SCHEMA = 'world'
"""


#**************************************************** sqllite ******************************************
"""
DROP TABLE IF EXISTS fklist;
        DROP TABLE IF EXISTS master_copy;
        DROP TRIGGER IF EXISTS load_fklist;
        CREATE TABLE IF NOT EXISTS fklist AS SELECT '' AS child,* 
            FROM pragma_foreign_key_list((SELECT name FROM sqlite_master WHERE type = 'not a type' LIMIT 1));
            CREATE TABLE IF NOT EXISTS master_copy AS SELECT * FROM sqlite_master WHERE type = 'not a type';
            CREATE TRIGGER IF NOT EXISTS load_fklist 
            AFTER INSERT ON master_copy
            BEGIN
                INSERT INTO fklist SELECT new.name,* FROM pragma_foreign_key_list(new.name);
            END
        ;
        INSERT INTO master_copy SELECT * 
            FROM sqlite_master 
            WHERE type = 'table' 
                AND instr(sql,' REFERENCES ') > 0
        ;

        SELECT * FROM fklist
        SELECT * FROM fklist;
        DROP TABLE IF EXISTS fklist;
        DROP TABLE IF EXISTS master_copy;
        DROP TRIGGER IF EXISTS load_fklist;
"""


unneccessarytab   = [ None, 'auth_group', 'auth_permission', 'django_content_type', 'auth_user']

from django.shortcuts import render
from django.db import connections

# Create your views here.
from ddapp.models import Country, State, District

from collections import defaultdict
  

# 1st input the dbname >> return all the table of related to dbname  >> input/select tablename return all table name related to foreign key >> execute multiple query return all the 
# column name related to each table >> return result of all column data ie executing the select query using sql.

def selectMysqlDb(db): # return all table name
    with connections["nath"].cursor() as cursor:
        # cursor.execute(f"""SELECT TABLE_NAME,COLUMN_NAME,CONSTRAINT_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME 
        # FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE WHERE REFERENCED_TABLE_SCHEMA = '{db}'
        # """)
        operation = [f"use {db};","show tables;"]
        for result in (operation):
            cursor.execute(result)
            obj = cursor.fetchall()
            if obj:
                print(obj)

selectMysqlDb('world')

def listFKTable(db):

    with connections["nath"].cursor() as cursor:
        cursor.execute(f""" SELECT CONSTRAINT_NAME, COLUMN_NAME, TABLE_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME  FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE WHERE CONSTRAINT_SCHEMA = '{db}'; """)
        obj = cursor.fetchall()
        join = []
        # lst = []
        reftab_tab =  defaultdict(list)
        for col in obj:
            if col[3] not in unneccessarytab:
                join.append([col[2],col[3], col[1]])
                if  col[0] == 'PRIMARY':
                    print(col[0], col)
                else:
                    reftab_tab[col[2]].append(col[3])
                    # print(reftab_tab[col[3]].append(col[2]))
                    # reftab_tab[col[3]] = reftab_tab[col[3]].append(col[2])

        print(reftab_tab)
        # print("************************")
        # print(reftab_tab.keys())
        # print("************************")
        # print(reftab_tab.values())
        # print("join tablename, reference  tablename ", join)
        return join



def generateJoinTableColumn(dbname, tablename):
    for i in listFKTable(dbname):
        print(i)


generateJoinTableColumn('sakila','address')

# with connections['moid3'].cursor() as cursor:
    # cursor.execute("SELECT * FROM sakila.actor LIMIT 10")
    # cursor.execute("SELECT * FROM bnath.first_level_products;")
    # obj = cursor.fetchone()
    # print(obj)
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
# def get_no_inputfields():
#     return schema_map.keys()
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


#{'address': ['city'], 'city': ['country'], 'customer': ['address', 'store'], 'ddapp_district': ['ddapp_state'], 'ddapp_state': ['ddapp_country'], 'film': ['language', 'language'], 'film_actor': ['actor', 'film'], 'film_category': ['category', 'film'], 'inventory': ['film', 'store'], 'payment': ['customer', 'rental', 'staff'], 'rental': ['customer', 'inventory', 'staff'], 'staff': ['address', 'store'], 'store': ['address', 'staff']}

#
# (('city',), ('country',), ('countrylanguage',))
# defaultdict(<class 'list'>, {'address': ['city'], 'city': ['country'], 'customer': ['address', 'store'], 'ddapp_district': ['ddapp_state'], 'ddapp_state': ['ddapp_country'], 'film': ['language', 'language'], 'film_actor': ['actor', 'film'], 'film_category': ['category', 'film'], 'inventory': ['film', 'store'], 'payment': ['customer', 'rental', 'staff'], 'rental': ['customer', 'inventory', 'staff'], 'staff': ['address', 'store'], 'store': ['address', 'staff']})
# ['address', 'city', 'city_id']
# ['city', 'country', 'country_id']
# ['customer', 'address', 'address_id']
# ['customer', 'store', 'store_id']
# ['ddapp_district', 'ddapp_state', 'state_id']
# ['ddapp_state', 'ddapp_country', 'country_id']
# ['film', 'language', 'language_id']
# ['film', 'language', 'original_language_id']
# ['film_actor', 'actor', 'actor_id']
# ['film_actor', 'film', 'film_id']
# ['film_category', 'category', 'category_id']
# ['film_category', 'film', 'film_id']
# ['inventory', 'film', 'film_id']
# ['inventory', 'store', 'store_id']
# ['payment', 'rental', 'rental_id']
# ['payment', 'staff', 'staff_id']
# ['rental', 'customer', 'customer_id']
# ['rental', 'inventory', 'inventory_id']
# ['rental', 'staff', 'staff_id']
# ['staff', 'address', 'address_id']
# ['staff', 'store', 'store_id']
# ['store', 'address', 'address_id']
# ['store', 'staff', 'manager_staff_id']
