											#This program is used to add two matrix given by the user as per specified dimensions.
row1=int(input('Enter number of rows in first matrix: '))
col1=int(input('Enter number of coloumns in first matrix: '))
row2=int(input('Enter number of rows in second matrix: '))
col2=int(input('Enter number of coloumns in second matrix: '))
Matrix1 =[]
Matrix2=[]
											#input first matrix
for i in range(row1):
	row=[]
	for j in range(col1):
		print('Enter element in',i+1,'row and',j+1,'coloum: ')
		inpt=int(input())
		row.append(inpt)
	Matrix1.append(row)
#input second matrix
for i in range(row2):
	row=[]
	for j in range(col2):
		print('Enter element in',i+1,'row and',j+1,'coloum: ')
		inpt=int(input())
		row.append(inpt)
	Matrix2.append(row)
											#printing original matrices
print('Matrix A:')
for i in Matrix1:
	print(i)
print('Matrix B:')
for i in Matrix2:
	print(i)
											#check if addition is possible
if row1==row2 and col1==col2:
	resultant_matrix=[]
	for i in range(len(Matrix1)):
		row=[]
		for j in range(len(Matrix1[0])):
			sum=Matrix1[i][j]+Matrix2[i][j]
			row.append(sum)
		resultant_matrix.append(row)
	print('Resultant Matrix:')
	for i in resultant_matrix:
		print(i)
else:
	print('Addition not possible due to incompatible dimensions of the two matrix.')