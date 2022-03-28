print('check')
import mysql.connector
def table_insertion_first_time(users_detail):
	mydb=mysql.connector.connect(host='localhost',user='root',passwd='RDPCGSt65.@',database='for_management')
	mycursor=mydb.cursor()
	for i in users_detail.items():
		term=i[0]
		valueses=i[1]
		add_user=("INSERT INTO for_management.user_details"
			"(username,password)"
			"VALUES(%s,%s)")
		details=(term,valueses)
		mycursor.execute(add_user,details)
	mydb.commit()
	mycursor.close()

	print('table successfully updated')
print('check')
users_detail={'A':'A','B':'B','C':'C','D':'D','E':'E','F':'F','G':'G','H':'H','I':'I','J':'J'}
table_insertion_first_time(users_detail)
print('check')