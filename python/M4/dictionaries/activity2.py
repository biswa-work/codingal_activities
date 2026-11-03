# Activity 2: Check the Frequency

test_dict = {
    "apple": 5,
    "banana": 3,
    "mango": 5,
    "orange": 2,
    "grapes": 5
}

target = 5
count = 0

for key in test_dict:
    if test_dict[key] == target:
        count += 1

print("Dictionary:", test_dict)
print("Target value:", target)
print("Frequency:", count)
