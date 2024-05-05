from src.models.admin_model import Admin
from src.database.auth_db import create_admin
from src.database.incident_db import create_incident
from src.models.incidents_model import Incidents
from src.establish_db_connection import database
import sys

# #### Creating 2 Station admins
PASSWORD = "123456aA"

# admin1 = Admin(
#     password=PASSWORD,
#     station_name="Andheri",
#     role="STATION_ADMIN",
#     admin_name="Ravi"
# )

# admin2 = Admin(
#     password=PASSWORD,
#     station_name="CSMT",
#     role="STATION_ADMIN",
#     admin_name="kishore"
# )

# create_admin(admin1)
# create_admin(admin2)

#### Creating 10 incidents for each station

#crime, violence, stampede, cleanliness, safety threat
# type = ["Crime","Violence","Stampede","Cleanliness","Safety Threat"]

# for i in range(10):
#     incident1 = Incidents(
#         title="IncidentA"+str(i),
#         description="Incident"+str(i),
#         type=type[i%5],
#         station_name="Andheri",
#         location="Chakala street",
#         source="CCTV"
#     )
#     incident2 = Incidents(
#         title="IncidentB"+str(i),
#         description="Incident"+str(i),
#         type=type[i%5],
#         station_name="CSMT",
#         location="Regis Hotel",
#         source="CCTV"
#     )
#     create_incident(incident1)
#     create_incident(incident2)


# for i in range(10):
#     incident1 = Incidents(
#         title="IncidentA"+str(i),
#         description="Incident"+str(i),
#         type=type[i%5],
#         station_name="Andheri",
#         location="Chakala street",
#         source="User Report"
#     )
#     incident2 = Incidents(
#         title="IncidentB"+str(i),
#         description="Incident"+str(i),
#         type=type[i%5],
#         station_name="CSMT",
#         location="Regis Hotel",
#         source="User Report"
#     )
#     create_incident(incident1)
#     create_incident(incident2)

# ### Creating 5 staff for each station
# from src.models.staff_model import Staff
# from src.database.auth_db import create_staff

# for i in range(5):
#     staff1 = Staff(
#         password=PASSWORD,
#         station_name="Andheri",
#         staff_name="StaffA"+str(i),
#         phone="987654321"+str(i)
#     )
#     staff2 = Staff(
#         password=PASSWORD,
#         station_name="CSMT",
#         staff_name="StaffB"+str(i),
#         phone="987654322"+str(i)
#     )
#     create_staff(staff1)
#     create_staff(staff2)

# def create_seed_incidents():
#     #Create 10 Detected Incidents  who has src has CCTV
#     type = ["Crime","Violence","Stampede","Cleanliness","Safety Threat"]

#     for i in range(10):
#         incident1 = Incidents(
#             image="https://smartsurveillance.s3.ap-south-1.amazonaws.com/default.jpg",
#             title="IncidentA"+str(i),
#             description=type[i%5],
#             type=type[i%5],
#             station_name="Andheri",
#             location="Chakala street",
#             source="CCTV"
#         )
#         create_incident(incident1)

# if sys.argv[1]=="incident":
#     create_seed_incidents()


##update all incidents

database.Incidents.update_many({},{"$set":{"assigned_to":"None"}})