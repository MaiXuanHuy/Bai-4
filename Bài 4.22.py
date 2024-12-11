print("Mai Xuân Huy")
print("MSSV:235752021610062")
print("#################")
result = []
for num in range(1000, 3001):
    num_str = str(num)
    if all(int(digit) % 2 == 0 for digit in num_str):
        result.append(num_str)
print(','.join(result))
