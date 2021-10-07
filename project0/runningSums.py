def runningSum(nums):
    runningSums = [nums[0]]
    i = 1
    while i < len(nums):
        runningSums.append(runningSums[i-1] + nums[i])
        i = i + 1
    return(runningSums)

numbersList = [1,2,3,4]
numbers = runningSum(numbersList)
print(numbers)