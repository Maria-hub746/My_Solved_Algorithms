def bubble_sort(nums):
    status = True
    while status:
        status = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                status = True

nums = [2, 1, 5, 4, 7, 3, 6]
bubble_sort(nums)
print(nums)