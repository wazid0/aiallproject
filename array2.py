import numpy as p
a =p.array([[1,2,4],[5,8,7]],dtype='float')
print("\narray created using passed list:\n",a)
b =p.array((1,3,2))
print("\narray created using tuple:\n",b)
c =p.zeros((3,4))
print("\narray initiate with all zero:\n",c)
d =p.full((3,3),6,dtype='complex')
print("\narray initiate with 6s.","array type is complex:\n",d)
e =p.random.random((2,2))
print("\nA random array:\n",e)

#from 0 to 30 with steps of 5

f =p.arange(0,30,5)
print("\nA sequential array with steps 5:\n",f)
g =p.linspace(0,5,10)
print("\nA sequential array with 10 values between""0 and 5:\n",g)
arr =p.array([[1,2,3,5],[4,5,6,7],[5,0,4,2]])
newarr=arr.reshape(2,2,3)
print("\norignal array:\n",arr)
print("\nreshape array:\n",newarr)
#flatten array
arr =p.array([[1,2,3],[4,5,6]])
flarr=arr.flatten()
print("\norignal array:\n",arr)
print("\nflatten array:\n",flarr)

