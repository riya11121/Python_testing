def largest(arr,n):
    max=arr[0]

    for i in range(1,n):
        if arr[i]>max:
            max=arr[i]
    return max

arr=[5,6,7,8,9,34]
n=len(arr)
ans=largest(arr,n)
print("Largest in array:",ans)