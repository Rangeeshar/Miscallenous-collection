def printdistinct(arr):
	dis_arr=set(arr)
	for i in dis_arr:
		print(i,end=' ')

arr=[1,1,2,2,2,3,3,3]
printdistinct(arr)