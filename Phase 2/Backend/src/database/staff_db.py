from src.establish_db_connection import database

admins = database.Staffs
incidents = database.Incidents

def get_staffs_by_station(station_name):
    try:
        documents = admins.find({"station_name": station_name})
        if documents == None:
            return {"ERROR":"NO SUCH STAFF EXISTS"}
        else:
            staffs = []
            for document in documents:
                del document['_id']
                del document['password']
                staffs.append(document)
            return {"SUCCESS": staffs}
    except Exception as e:
        print(e)
        return {"ERROR":"SOME ERROR OCCURRED"}

def update_staff_token(id, token):
    try:
        document = admins.update_one({"id": id}, {"$set": {"notification_token":token}})
        if(document.matched_count>0):
            return "SUCCESS"
        else:
            return "INVALID"
    except Exception as e:
        print(e)
        return "Some Error Occurred"

def update_staff_status(id, status):
    try:
        admins.update_many({"id":{"$in":id}}, {"$set":{"status":status}})
        return {"SUCCESS":"STATUS UPDATED"}
    except Exception as e:
        print(e)
        return {"ERROR":"SOME ERROR OCCURRED"}

def get_staffs_by_id(id):
    try:
        document = admins.find_one({"id":id})
        if document == None:
            return {"ERROR":"NO SUCH STAFF EXISTS"}
        else:
            del document['_id']
            del document['password']
            return {"SUCCESS":document}
    except Exception as e:
        print(e)
        return {"ERROR":"SOME ERROR OCCURRED"}
    
def update_staff_availability():
    try:
        assigned_staff_ids = list(incidents.find({"status":"Pending", "assigned_to": {"$ne": "None"}}, {"assigned_to":1}))
        assigned_staff_ids = [staff_id["assigned_to"] for staff_id in assigned_staff_ids]
        admins.update_many({"id": {"$in": assigned_staff_ids}}, {"$set": {"status": "Busy"}})
        admins.update_many({"id": {"$nin": assigned_staff_ids}}, {"$set": {"status": "Available"}})
    except Exception as e:
        print(e)
        return {"ERROR":"SOME ERROR OCCURRED"}
    
        