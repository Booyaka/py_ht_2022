def removeDulicates(nums: list[int]) -> int:
    last = nums[0]
    j = 1
    my_nums = []
    my_nums.append(last)

    for i in range(1, len(nums)):
        if nums[i] != last:
            nums[j] = nums[i]
            last = nums[i]
            my_nums.append(nums[i])
            j += 1

    return f'{j}, {my_nums}'


nums = [1, 1, 2, 3, 3, 5]
print(removeDulicates(nums))