class MyMatrix:

	def __init__(self, row, column):
		self.row=row
		self.column=column
		self.matrix=[[0 for x in xrange(row)] for y in xrange(column)]

	def setElement(self, row, column, value):
		self.matrix[row][column]=value

	def getElement(self,row,column):
		return self.matrix[row][column]

	def __getRow__(self, rowNum):
		return self.matrix[rowNum]
		# first row matrix[0]

	def __getColumn__(self, colNum):
		col= [0 for i in xrange(0,self.column)]
		for x in xrange(0,self.column):
			col[x]=self.matrix[x][colNum]
		return col

	def add(self, matrixB):
		if self.column != matrixB.column or self.row != matrixB.row:
			print " matrixes are not of compatible sixe"
			returnMatrix= MyMatrix(0,0)
		else :
			returnMatrix = MyMatrix(self.row, self.column)
			for i in xrange(0,self.row):
				returnMatrix.matrix[i] = [x+y for x,y in zip(self.__getRow__(i), matrixB.__getRow__(i))]
		return returnMatrix

	def multiply(self, matrixB):
		if self.column!=matrixB.row:
			print "matrixes are incompatible"
		else:
			returnMatrix = MyMatrix(matrixB.row, self.column)
			for i in xrange(0,self.row+1):
				for j in xrange(0,matrixB.column+1):
					returnMatrix.matrix[i][j]= sum([x*y for x,y in zip(self.__getRow__(i),matrixB.__getColumn__(j))])
		return returnMatrix 

def main():
	matrixA = MyMatrix(2,3)
	matrixA.setElement(2,1,1)
	matrixA.setElement(1,1,2)
	matrixB = MyMatrix(3,2)
	matrixB.setElement(1,2,1)
	matrixC = matrixA.multiply(matrixB)

	print ("c")
	for x in xrange(0,matrixC.column):
		print matrixC.__getRow__(x)
	print "a"
	for x in xrange(0,matrixA.column):
		print matrixA.__getRow__(x)
	print "b"
	for x in xrange(0,matrixB.column):
		print matrixB.__getRow__(x)

if __name__=="__main__":
	main()
