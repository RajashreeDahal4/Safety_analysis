import pymysql
import pandas as pd
import sqlalchemy
import warnings
import numpy as np
from sqlalchemy.types import Integer
from sqlalchemy.types import String
#=========user details====

# password='RDPCGSt65.@'
engine=sqlalchemy.create_engine('mysql+pymysql://root:RDPCGSt65.%40@localhost/layers')
print('engine_created')
#for second_evaluation_indicators
df_sec=pd.read_sql_table('second_evaluation_indicators',engine)
checklist_mapping=pd.DataFrame()
checklist_mapping['id']=df_sec['id']
checklist_mapping['first_evaluation_indicators']=df_sec['first_evaluation_indicators']


#=======for username and password:
engine2=sqlalchemy.create_engine('mysql+pymysql://root:RDPCGSt65.%40@localhost/for_management')
user_pass=pd.read_sql_table('user_details',engine2)
print(user_pass)
user=pd.DataFrame()
print('hello')
for i in user_pass['username']:
	user[i]=0
# print(user.head())
# checklist_mapping=checklist_mapping.join(user)
# print(checklist_mapping)
dict={}
# for i in checklist_mapping['first_evaluation_indicators']:
# 	print(i)


#===== get key based on value===
def get_key(user_dict,val):
	for key,value in user_dict.items():
		if val==value:
			return key

def welcome(user_pass,checklist_mapping):
	username=input('Welcome to rating survey. Please input your username:')
	print('username noted')
	user_pass1=user_pass[user_pass['username']==username]
	print(user_pass1)
	if len(user_pass1.index)>0:
		password=input('Please input your password:')
		print('okay')
		pass1=user_pass1[user_pass1['password']==password]
		if len(pass1.index)>0:
			print('thank you for logging in. Lets continue the survey')
			# rating=pd.DataFrame()
			# rating[username]=
			user_dict={1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',8:'I',10:'J'}
			value=get_key(user_dict,username)
			names=[username]
			user_df=pd.DataFrame(columns=names)
			checklist_mapping=checklist_mapping.join(user_df)
			checklist_mapping=checklist_mapping.fillna(0)
			print(checklist_mapping)
			print('Lets start rating of the factors')
			mapping_final=pd.DataFrame(columns=['id','first_evaluation_indicators',username])
			for m in checklist_mapping['first_evaluation_indicators']:
				a=input("enter the rating for %s in the range 1 to 5:" %m)
				a=int(a)
				if a<0 or a>5:
					print('please enter value within range')
					break;
				#print(checklist_mapping)
				checklist_mapping[username]=checklist_mapping[checklist_mapping['first_evaluation_indicators']==m][username]+a
				checklist_mapping=checklist_mapping.fillna(0)
				checklist_mapping['id']=checklist_mapping['id']
				checklist_mapping['first_evaluation_indicators']=checklist_mapping['first_evaluation_indicators']
				checklist_mapping[username]=checklist_mapping[username]
				# print(checklist_mapping)
				mapping_final=mapping_final.append(checklist_mapping)
			print(mapping_final)
			mapping_final=mapping_final.groupby(['id','first_evaluation_indicators'])[username].sum()
			print(mapping_final)
		else:
			print('the password is incorrect')
	else:
		print('the username is not registered')

	return mapping_final,username



user_dict={1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',8:'I',10:'J'}
for i in user_dict.values():
	dataframe=pd.DataFrame()  
	dataframe,table_name=welcome(user_pass,checklist_mapping)
	table_name=table_name.lower()
	engine3=sqlalchemy.create_engine('mysql+pymysql://root:RDPCGSt65.%40@localhost/layers')
	dbconnection=engine3.connect()
	frame=dataframe.to_sql('user_'+table_name,dbconnection,if_exists='replace',dtype={'id':String(5),'first_evaluation_indicators':String(50)})
	print('Table %s created successfully.'%table_name)
	dbconnection.close()
	result=input('Do you want to continue another user input?? If Yes type Y, if No, type N')
	if result=='Y':
		print("Lets begin another entry")
	else:
		break


