size = 10

# Separate Chaining
chain = [[] for _ in range(size)]

def separate_chaining(key):
    index = key % size
    chain[index].append(key)

# Linear Probing
linear = [None] * size

def linear_probing(key):
    index = key % size
    start = index

    while linear[index] is not None:
        index = (index + 1) % size

        if index == start:
            print("Hash table is full")
            return

    linear[index] = key

# Quadratic Probing
quadratic = [None] * size

def quadratic_probing(key):
    index = key % size
    i = 0

    while i < size:
        new_index = (index + i * i) % size

        if quadratic[new_index] is None:
            quadratic[new_index] = key
            return

        i += 1

    print("Cannot insert key:", key)

# Input keys
keys = list(map(int, input("Enter keys separated by spaces: ").split()))

for key in keys:
    separate_chaining(key)
    linear_probing(key)
    quadratic_probing(key)

print("\nSeparate Chaining:")
for i in range(size):
    print(i, ":", chain[i])

print("\nLinear Probing:")
for i in range(size):
    print(i, ":", linear[i])

print("\nQuadratic Probing:")
for i in range(size):
    print(i, ":", quadratic[i])
