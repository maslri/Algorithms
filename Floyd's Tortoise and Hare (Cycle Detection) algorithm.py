def findCycleStartAndLength(nums):
    # Step 1: Detect the presence of a cycle
    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # Step 2: Find the starting point of the cycle
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    # return slow
    cycle_start = slow  # This is the starting point of the cycle

    # Step 3: Find the length of the cycle
    length = 1
    fast = nums[cycle_start]
    while fast != cycle_start:
        fast = nums[fast]
        length += 1

    return cycle_start, length

# Example usage:
nums = [1, 3, 4, 2, 2]
cycle_start, cycle_length = findCycleStartAndLength(nums)
print("Starting point of the cycle:", cycle_start)
print("Length of the cycle:", cycle_length)
