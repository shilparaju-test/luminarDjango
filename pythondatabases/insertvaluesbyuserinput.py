from db_connect.dbconnectpgm import *
db=get_connection()
cursor=db.cursor()
id=input('ID:')
f_name=input('Name:')
sub=input('Subject:')
# sql="""INSERT INTO faculty(id,name,subject) VALUES (%s,%s,%s)""", (id,f_name,sub)
# print(sql)
try:
    # cursor.execute(sql)
    cursor.execute("""
    INSERT INTO faculty(id,name,subject) VALUES (%s,%s,%s)""", (id,f_name,sub))
    db.commit()#save changes to db
    print("success")
except Exception as e:
    print(e.args)
finally:
    db.close()