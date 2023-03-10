from django.shortcuts import render
from django.db import connection

# Create your views here.
from ddapp.models import Country, State, District

# cursor1 = connection.cursor()
# obj = cursor1.execute('SELECT * FROM sqlite_master WHERE type = "table"')

# for i in obj:
#     cursor2 = connection.cursor()
#     obj2 = cursor2.execute(f"PRAGMA table_info({i[1]})")
#     for j in obj2:
#         print(j)
#     print("******************************")
    # print(i[1])


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

