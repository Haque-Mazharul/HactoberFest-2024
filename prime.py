def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test with an example
num = 29
if is_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
