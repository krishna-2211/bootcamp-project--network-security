import hashlib

print("*" * 10 + "Python and Network Security" + "*" * 10)
print()

entered_string = input("Please enter a string: ")
hash_str = hashlib.md5(entered_string.encode())
print(hash_str.hexdigest())