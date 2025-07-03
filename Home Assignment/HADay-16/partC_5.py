# Part C: Static Methods for General Operations
# 5.Math Helper Class
# oCreate a class MathHelper with static methods:
# is_prime(num) – Returns True if the number is a prime.
# gcd(a, b) – Returns the greatest common divisor.
# lcm(a, b) – Returns the least common multiple.
# oTest with different inputs.
class MathHelper:
    @staticmethod
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    @staticmethod
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    @staticmethod
    def lcm(a, b):
        return abs(a * b) // MathHelper.gcd(a, b)

# Test with different inputs
print("Prime Number Check:")
print(MathHelper.is_prime(11))  # True
print(MathHelper.is_prime(15))  # False

print("\nGreatest Common Divisor:")
print(MathHelper.gcd(48, 18))  # 6
print(MathHelper.gcd(54, 24))  # 6

print("\nLeast Common Multiple:")
print(MathHelper.lcm(4, 6))  # 12
print(MathHelper.lcm(15, 20))  # 60

