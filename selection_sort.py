def selection_sort(nums):
    for i in range(len(nums)):
        min = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min]:
                min = j
        nums[i], nums[min] = nums[min], nums[i]


nums = [15, 7, 2, 30, 12]
selection_sort(nums)
print(nums)
