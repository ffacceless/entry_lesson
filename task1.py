nums=[1,2,3,4,5,6,4]
target=7
res=[]
for i in range(len(nums)):
    for x in range(i+1,len(nums)):
        if nums[i]+nums[x]==target:
            if [nums[i], nums[x]] not in res and [nums[x], nums[i]] not in res:
                res.append([nums[i], nums[x]])
for s in res:
    print(s)
