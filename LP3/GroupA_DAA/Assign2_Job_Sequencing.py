data=[]
n=int(input("Enter number of jobs: "))
maxDeadline=0

				
			
for i in range(0,n):
	job=[]
	a=i+1
	print("For Job",i+1)
	b=int(input("Enter deadline of job : "))
	#simulatenously finding max deadline 
	if(maxDeadline<b):
		maxDeadline=b
	c=int(input("Enter profit : "))
	job.append(a)
	job.append(b)
	job.append(c)
	data.append(job)
	
def sort(data):
	for i in range(0,n):
		for j in range(0,n):
			if(data[i][2]>data[j][2]):
				#job number
				temp=data[i][0]
				data[i][0]=data[j][0]
				data[j][0]=temp
				#deadline
				temp=data[i][1]
				data[i][1]=data[j][1]
				data[j][1]=temp
				#profit
				temp=data[i][2]
				data[i][2]=data[j][2]
				data[j][2]=temp

def printArray(data):
	for i in range(0,n):
		for j in range(0,3):
			print(data[i][j])
		print("\n")	
			
sort(data)
printArray(data)


def Arrange(data,n):
	ans=[]
	for j in range(0,maxDeadline):
		ans.append(-1)
	for i in range(0,n):
		deadline=data[i][1]
		for m in reversed(range(maxDeadline)):
			if(deadline<=m+1 and ans[m]==-1):
				ans[m]=data[i][0]
	#print the answer
	print("\n"+ "Answer is")
	for k in range(0,maxDeadline):
		print(ans[k])
		
Arrange(data,n)

