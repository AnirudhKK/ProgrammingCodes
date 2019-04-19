a=open('numbers.txt','r')
data=a.read()
name=[]
number=[]
d=data.split('\n')
for i in d:
	c=0
	for j in i:
		if (ord(j)!=32):
			c+=1
		elif ord(j)==32:
			na=i[0:c]
			nu=i[c+1:]
			name.append(na)
			number.append(nu)
print(number)