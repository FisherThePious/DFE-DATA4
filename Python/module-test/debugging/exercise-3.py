# import pdb
# pdb.set_trace()

def is_prime(x):
    if x < 2:                    # Prime number's are greater than 1
        return False
    else:
        for n in range(2, x):
            if x % n == 0:
                return False
        return True

x = int(input("If you insert a prime number the following print statement should return true\n"))
if is_prime(x):
    print(f"{x} is a prime number.")
else:
    print(f"{x} is not a prime number.")

#=============================================================================
#       Original sample                                                        
#=============================================================================
# def is_prime(x):
#     if x < 2:
#         return False
#     else:
#         for n in range(2, x-1):
#             if x % n = 0:
#                 return False
#             return True