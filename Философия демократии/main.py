def is_true(i, promise):
    result = promise[:-(i + 1):i + 1]
    return len(set(result)) >= 7


count = 0
i = 1
while string != "И будет нам счастье!" and count < 5:
    string = input()
    if is_true(i, string):
        print(string)
        count += 1
    i += 1
