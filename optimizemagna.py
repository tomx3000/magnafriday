
def solve():	
	print("magna")
	# converting the number into tsh
	profit_margin=200000*2290

	# percentage cut for profit
	p_cut1=0.005
	p_cut2=0.0025
	
	number_transaction1=812000
	number_transaction2=50000

	# 
	sales_1=number_transaction1*p_cut1
	sales_2=number_transaction2*p_cut2

	# 
	tcap=3000000

	v2 =(profit_margin -((sales_1)*(tcap)))/(sales_2-sales_1)
	v1=tcap-v2

	print("v1: {} :Transactions: {} : Percentage: {} AmountCut {}".format(round(v1),number_transaction1, p_cut1,round(p_cut1*v1)))
	print(" v2 :{} :Transactions: {} : Percentage: {} AmountCut {}".format(round(v2),number_transaction2,p_cut2,round(p_cut2*v2)))
	
	
	if is_correct(v1,v2,tcap,sales_1,sales_2,profit_margin):
		print('okay')
	else:
		print('cha kike')

def is_correct(v1,v2,tcap,sales_1,sales_2,profit_margin):
	
	if ((tcap == v1+v2) and (profit_margin == round((sales_1*v1 + sales_2*v2)))):
		return True
	else:
		return False


def sove_higher_orde_eq():
	import numpy as np

	# 
	# a = np.array([[3,1], [1,2]])
	# b = np.array([9,8])

	# eq1=[(0.02*250000),(0.01*200000),(0.005*150000),(0.002*100000),(0.001*50000),(0.0005*25000),(0.0002*10000),(0.00025*5000)]

	# true equation
	# eq1=[(0.02*5000),(0.02*10000),(0.01*25000),(0.007*50000),(0.004*100000),(0.002*150000),(0.0014*200000),(0.0012*250000)]


	# 11 variables, new day 
	# eq1=[(0.02*250000),(0.01*200000),(0.005*150000),(0.002*100000),(0.001*50000),(0.0005*25000),(0.0002*10000),(0.0001*5000),(0.00005*2500),(0.000025*1250),(0.0000125*625)]

	# percentage_cut={"fivek":0.02,"tenk":0.01,"twentyk":0.005,"fourtyk":0.002,"fiftyk":0.001,"onehundredk":0.0005,"twohundredk":0.0002,"threehundredk":0.0001,"fourhundredk":0.00005,"fivehundredk":0.000025,"onethousandk":0.0000125}


	percentage_cut={"fivek":0.02,"tenk":0.01,"twentyk":0.005,"fourtyk":0.004,"fiftyk":0.005,"onehundredk":0.005,"twohundredk":0.005,"threehundredk":0.005,"fourhundredk":0.004,"fivehundredk":0.002,"onethousandk":0.001}

	# number_of_transactions=[{"twentyk"}250000,{"twentyk"}200000,{"twentyk"}200000,{"twentyk"}150000,{"twentyk"}100000,{"twentyk"}50000,{"twentyk"}25000,{"twentyk"}10000,{"twentyk"}5000,{"twentyk"}2500,{"twentyk"}1250,{"twentyk"}625]
	number_of_transactions={"fivek":180000,"tenk":100000,"twentyk":100000,"fourtyk":100000,"fiftyk":100000,"onehundredk":150000,"twohundredk":50000,"threehundredk":40000,"fourhundredk":20000,"fivehundredk":2500,"onethousandk":1250}
	
	 # eq1=[(0.02*250000),(0.01*200000),(0.005*150000),(0.002*100000),(0.001*50000),(0.0005*25000),(0.0002*10000),(0.0001*5000),(0.00005*2500),(0.000025*1250),(0.0000125*625)]
	eq1=[]
	for index in percentage_cut:
		for index2 in number_of_transactions:
			if(index2==index):
				eq1.append(percentage_cut[index]*number_of_transactions[index2])

	# eq2=[1,1,1,1,1,1,1,1,1,1,1]
	eq3=[-1,1,0,0,0,0,0,0,0,0,0]
	eq4=[0,-1,1,0,0,0,0,0,0,0,0]
	eq5=[0,0,-1,1,0,0,0,0,0,0,0]
	eq6=[0,0,0,-1,1,0,0,0,0,0,0]
	eq7=[0,0,0,0,-1,1,0,0,0,0,0]
	eq8=[0,0,0,0,0,-1,1,0,0,0,0]
	eq9=[0,0,0,0,0,0,-1,1,0,0,0]
	eq10=[0,0,0,0,0,0,0,-1,1,0,0]
	eq11=[0,0,0,0,0,0,0,0,-1,1,0]
	eq_v1=[1,0,0,0,0,0,0,0,0,0,0]

	a = np.array([eq1, eq11,eq3,eq4,eq5,eq6,eq7,eq8,eq9,eq10,eq_v1])
	b = np.array([200000*2290,500000,5000,10000,30000,50000,100000,100000,100000,100000,5000])
	x = np.linalg.solve(a, b)

	total_number_of_transactions=0
	temp=0
	for index,value in enumerate(percentage_cut):
		for index2,value2 in enumerate(number_of_transactions):
			for index3,value3 in enumerate(x):
				if(index==index2==index3):
					temp+=percentage_cut[value]*value3*number_of_transactions[value2]/2290
					print("Amount:Tsh {} :P_Co:$ {}: Transactions {} : % {} : Cut {} ".format(round(value3),round(temp),number_of_transactions[value2],percentage_cut[value],round(percentage_cut[value]*value3)))

					total_number_of_transactions+=number_of_transactions[value2]


	# print(x)
	print("Total Number of Transactions {}".format(total_number_of_transactions))

sove_higher_orde_eq()
# print('old ')
# solve()
