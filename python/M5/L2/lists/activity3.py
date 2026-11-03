class pair_elements:
    def twoSum(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            needed = target - num
            if needed in lookup:
                return (lookup[needed], i)
            lookup[num] = i
        return None


numbers = (10, 20, 30, 40, 50, 60, 70)
target = int(input("Enter the target sum: "))
result = pair_elements().twoSum(numbers, target)

if result is None:
    print("No pair found.")
else:
    print(f"Pair found at positions {result[0]} and {result[1]}.")
