from pymongo import MongoClient
cl=MongoClient()
db=cl["mvt"]
coll=db["user"]
data=[{"username":"neha","password":"abcd123","mailid":"neha123@gmail.com","phno":123456789},{"username":"Abby","password":"123abc","mailid":"abby123@gmail.com","phno":987654321},{"username":"Anna","password":"a1b2c3","mailid":"anna123@gmail.com","phno":678912345}]
coll.insert_many(data)
out=coll.find()
for i in out:
    print(i)
