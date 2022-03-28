import mysql.connector
import pandas as pd
import numpy as np
mydb=mysql.connector.connect(host='localhost',user='root',passwd='RDPCGSt65.@',database='for_management')
mycursor=mydb.cursor()
parent_id=['U1','U2','U3','U4','U5','U6','U7']
users=['A','B','C','D','E','F','G','H','I','J']
dic={}
for i in parent_id:
	sql='''SELECT a.parent_id,b.* FROM layers.second_evaluation_indicators a INNER JOIN layers.evaluation_entry b ON a.id=b.id WHERE parent_id LIKE %(ia)s'''
	mycursor.execute(sql,{'ia':i})
	table_rows=mycursor.fetchall()
	#print(table_rows)
	df=pd.DataFrame(table_rows,columns=['parent_id','id','second_evaluation_indicators','A','B','C','D','E','F','G','H','I','J'])
	dic.update({i:df})
dic2={}
for i in range(len(dic)):
	c=pd.DataFrame()
	k=list(dic.values())[i]
	#print(k)
	c['id']=k['id']
	c['A']=k['A']
	c['B']=k["B"]
	c['C']=k['C']
	c['D']=k['D']
	c['E']=k['E']
	c['F']=k['F']
	c['G']=k['G']
	c['H']=k['H']
	c['I']=k['I']
	c['J']=k['J']
	dic2.update({k['parent_id'][0]:c})

dic3={}
print(parent_id[0])

##3##### major changes from here ####
first_evaluation_indicators=['U1','U2','U3','U4','U5','U6','U7']
final_dict={}
for m in range(7):
	df=pd.DataFrame()
	df['id']=list(dic2.values())[m]['id']
	df_transposed=df.T
	#print(df_transposed)
	gf=pd.DataFrame()
	gf=list(dic2.values())[m]
	gf=gf.to_numpy()
	#print(gf)
	count_records={}
	for i in gf:
		count_1=0
		count_2=0
		count_3=0
		count_4=0
		count_5=0
		key=i[0]
		#print(key)
		for j in range(len(i)):
			j=j+1
			if j==len(i):
				break;
			if i[j]==1:
				count_1=count_1+1
			elif i[j]==2:
				count_2=count_2+1
			elif i[j]==3:
				count_3=count_3+1
			elif i[j]==4:
				count_4=count_4+1
			elif i[j]==5:
				count_5=count_5+1
			result={key:[count_1,count_2,count_3,count_4,count_5]}
		count_records.update(result)
	#print(count_records)
	evaluation_count=pd.DataFrame.from_dict(count_records)
	#print(evaluation_count)
	sum=evaluation_count.sum(axis=0)
	#print(sum)
	#print(sum['U11'])
	columns=(evaluation_count.columns)
	normalization={}
	df=evaluation_count.squeeze()
	for i in columns:
		for j in sum.index:
			#print(j)
			if i==j:
				check=df[i]/sum[j]
				key=i
				#print('printing check')
				#print('check')
				#print(check)
				to_update={key:check}
				normalization.update(to_update)
	#print(normalization)
	norm_data=pd.DataFrame.from_dict(normalization)
	update_this={first_evaluation_indicators[m]:norm_data}
	final_dict.update(update_this)
#print(final_dict)
RU={}
c=1
for i in final_dict.values():
	print(type(i))
	print(i)
	print('original matrix is:')
	i=i.to_numpy()
	print(i)
	print('transposed_matrix is:')
	i=np.transpose(i)
	#print(i)
	key='U'+str(c)
	to_update={key:i}
	RU.update(to_update)
	c=c+1
print(RU)

#test
for i in RU.keys():
	print(i)
mydb2=mysql.connector.connect(host='localhost',user='root',passwd='RDPCGSt65.@',database='layers')
mycursor=mydb2.cursor()
parent_id=['U1','U2','U3','U4','U5','U6','U7']
users=['A','B','C','D','E','F','G','H','I','J']
dic2={}
for i in RU.keys():
	sql='''SELECT a.weightage_value FROM layers.for_weightage a WHERE parent_id LIKE %(ia)s'''
	mycursor.execute(sql,{'ia':i})
	table_rows=mycursor.fetchall()
	#print(table_rows)
	df=pd.DataFrame(table_rows,columns=['weightage_value'])
	i=dic2.update({i:df})
print(dic2)
c=1
weightage_matrix={}
for i in dic2.values():
	#print('original matrix is:')
	i=i.to_numpy(dtype='float32')
	#print(i)
	#print('transposed_matrix is:')
	i=np.transpose(i)
	print(type(i))
	key='mt_WU'+str(c)
	to_update={key:i}
	weightage_matrix.update(to_update)
	c=c+1
print(weightage_matrix)

BU={}
c=0
for i in RU.values():
	d=0
	for j in weightage_matrix.values():
		if c==d:
			#print('the weightge matrix is')
			#print(j)
			#print('the originl mtriz is')
			#print(i)
			value=np.dot(j,i)
			key='BU'+str(d+1)
			to_update={key:value}
			BU.update(to_update)
			#print('the value is')
			#print(value)
			#np.concatenate(mat,value,1)
			d=d+1
		else: 
			d=d+1
			continue
	c=c+1
#print(mat)

#calculation B=WR
calc_B_WR={}
V=[1,2,3,4,5]
d=1
for k in BU.values():
	value=np.dot(k,V)
	key='FU'+str(d)
	d=d+1
	to_update={key:value}
	calc_B_WR.update(to_update)
print(calc_B_WR)
calc_B_WR=pd.DataFrame.from_dict(calc_B_WR)
print(calc_B_WR)

#calc final
calc_final={}
V=[1,2,3,4,5]
d=1
print(BU)
mydb3=mysql.connector.connect(host='localhost',user='root',passwd='RDPCGSt65.@',database='layers')
mycursor=mydb3.cursor()
parent_id=['U1','U2','U3','U4','U5','U6','U7']
dic3={}
for i in parent_id:
	print(i)
	sql='''SELECT a.weightage_value FROM layers.weightage a WHERE a.factor LIKE %(ia)s'''
	mycursor.execute(sql,{'ia':i})
	table_rows=mycursor.fetchall()
	print('printing table rows')
	print(table_rows)
	df=pd.DataFrame(table_rows,columns=['weightage_value'])
	to_update={i:df}
	dic3.update(to_update)
#print(dic3)

c=1
final_weightage_matrix=[]
for i in dic3.values():
	#print('original matrix is:')
	i=i.to_numpy()
	#print(i)
	#print('transposed_matrix is:')
	i=np.transpose(i)
	i=float(i)
	print(type(i))
	key='final_mat_WU'+str(c)
	to_update={key:i}
	final_weightage_matrix.append(i)
	c=c+1
print(final_weightage_matrix)


final_BU=BU
print(final_BU)
print('the final weightage_matrix is')
print(final_weightage_matrix)
print(type(BU))
print(weightage_matrix)
calc_B_WR={}
V=[1,2,3,4,5]
d=1

the_final_BU={}
for i in final_BU:
	key=i
	value=final_BU.get(key).flatten()
	to_update={key:value}
	the_final_BU.update(to_update)
print(the_final_BU)

final_BU_matrix=[]
for i in the_final_BU.values():
	print(i)
	final_BU_matrix.append(i)
print(final_BU_matrix)
BU_matrix=np.array(final_BU_matrix)
print(BU_matrix)
print(BU_matrix.shape)
transpose_BU_matrix=np.transpose(BU_matrix)
print(transpose_BU_matrix)
print(transpose_BU_matrix.shape)

final_weightage_matrix=np.array(final_weightage_matrix)
print(final_weightage_matrix)
print(final_weightage_matrix.shape)

final_B=np.dot(transpose_BU_matrix,final_weightage_matrix)
print(type(final_B))
print(final_B)
v=np.array([1,2,3,4,5])
print(V)
F=np.dot(final_B,V)
print(F)
print('the overall safety is:', F)




