import numpy as np

arr=np.random.randn(6,6)

print(arr)

print("Shape:",arr.shape)
print("Size:",arr.size)
print("Datatype:",arr.dtype)

print("Maximum Index:",arr.argmax())
print("Minimum Index:",arr.argmin())

print("Top Left 3x3")
print(arr[:3,:3])

arr[arr<0]=np.abs(arr[arr<0])

print("Modified Matrix")
print(arr)