L=[3,2,4]
Target=6
def two_sum(nums,target):
    output=[]
    for x in range(len(nums)):
        for y in range(len(nums)):
            if x==y:
                continue
            else:
                if nums[x]+nums[y]==target:
                    print(x,y)
                    exit()
                    # output.append(x)
                    # output.append(y)

two_sum(L,Target)
