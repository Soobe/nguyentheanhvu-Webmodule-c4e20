from models.service import Service
import mlab

mlab.connect()

id_to_find = "5b781eeb06f3e62b684a8b77"

# hera = Service.objects(id=id_to_find)
# hera = Service.objects.get(id =id_to_find)
service = Service.objects.with_id(id_to_find)

if service is not None:
    # service.delete()
    # print("Deleted")
    print(service.to_mongo())
    service.update(set__yob = 2000,set__name = "Linh ku")
    service.reload()
    print("After: ")
    print(service.to_mongo())
else:
    print("Not Found")