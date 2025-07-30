import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

#selectedFriend = friends[random.randint(0,4)]
selectedFriend = random.choice(friends)
print(selectedFriend)