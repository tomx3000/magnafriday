import numpy as np

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
	# 
	# a = np.array([[3,1], [1,2]])
	# b = np.array([9,8])

	# eq1=[(0.02*250000),(0.01*200000),(0.005*150000),(0.002*100000),(0.001*50000),(0.0005*25000),(0.0002*10000),(0.00025*5000)]

	# true equation
	# eq1=[(0.02*5000),(0.02*10000),(0.01*25000),(0.007*50000),(0.004*100000),(0.002*150000),(0.0014*200000),(0.0012*250000)]

	eq1=[(0.02*5000),(0.02*10000),(0.01*25000),(0.007*50000),(0.004*100000),(0.002*150000),(0.0014*200000),(0.0012*250000)]
	eq2=[1,1,1,1,1,1,1,1]
	eq3=[-1,1,0,0,0,0,0,0]
	eq4=[0,-1,1,0,0,0,0,0]
	eq5=[0,0,-1,1,0,0,0,0]
	eq6=[0,0,0,-1,1,0,0,0]
	eq7=[0,0,0,0,-1,1,0,0]
	eq8=[0,0,0,0,0,-1,1,0]
	eq9=[0,0,0,0,0,0,-1,1]

	a = np.array([eq1, eq2,eq3,eq4,eq5,eq6,eq7,eq8])
	b = np.array([200000*2290,400000,5000,10000,30000,50000,100000,100000])
	x = np.linalg.solve(a, b)
	print(x)


sove_higher_orde_eq()
