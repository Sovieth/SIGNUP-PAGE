from bson import ObjectId
from .. import mongo

class get_service:
    def Add_Service(service):
        return mongo.db.services.insert_one(service)
    
    def getall_services():
        return mongo.db.services.find()
    
    def delete_service(service_id):
        return mongo.db.services.delete_one({"_id": ObjectId(service_id)})
    
    def edit_service1(id, service):
        return mongo.db.services.update_one({"_id": ObjectId(id)}, {"$set": service})

    def find():
        return mongo.db.services.find()
    
    
    
    
    

 
    