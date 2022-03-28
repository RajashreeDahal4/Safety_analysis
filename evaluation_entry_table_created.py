import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='RDPCGSt65.@',database='layers')
mycursor=mydb.cursor()
query=''' CREATE TABLE layers.evaluation_entry AS (
SELECT a.*,b.B,c.C,d.D,e.E,f.F,g.G,h.H,i.I,j.J FROM layers.user_a a
INNER JOIN layers.user_b b ON  a.id=b.id
INNER JOIN layers.user_c c ON a.id=c.id
INNER JOIN layers.user_d d ON a.id=d.id
INNER JOIN layers.user_e e ON a.id=e.id
INNER JOIN layers.user_f f ON a.id=f.id
INNER JOIN layers.user_g g ON a.id=g.id
INNER JOIN layers.user_h h ON a.id=h.id
INNER JOIN layers.user_i i ON a.id=i.id
INNER JOIN layers.user_j j ON a.id=j.id)'''
mycursor.execute(query)



mydb2=mysql.connector.connect(host='localhost',user='root',passwd='RDPCGSt65.@',database='layers')
mycursor=mydb2.cursor()
dic={}
query=''' CREATE TABLE layers.for_weightage AS (
SELECT a.*,b.parent_id FROM layers.weightage a
INNER JOIN layers.second_evaluation_indicators b on b.id=a.factor)'''
mycursor.execute(query)