from db_connect.dbconnectpgm import *
db=get_connection()
cursor=db.cursor()
sql="insert into faculty values('101','anay','os')"
try:
    cursor.execute(sql)
    db.commit()#save changes to db
    print("success")
except Exception as e:
    print(e.args)
finally:
    db.close()
