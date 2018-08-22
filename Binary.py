# Binary Search Implementation In Python 
arr=list(map(int,input('Enter array :  ').split()))
s_ele=int(input('Enter the Number To Search : '))
left_p,right_p,mid,f=0,len(arr)-1,0,0
while(left_p<=right_p):
	mid=left_p+(right_p-left_p)//2
	print("mid : %d"%(mid))
	if arr[mid]==s_ele:
		print("found")
		f=1
		break
	if(arr[mid]<s_ele):
		left_p=mid+1
		print("mid : %d"%(mid))
	else:
		right_p=mid-1
		print("mid : %d"%(mid))
if f==0:
	print("Not found")


