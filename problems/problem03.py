"""
Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

Found algorithm here: https://math.stackexchange.com/questions/389675/largest-prime-factor-of-600851475143
"""


def main():
    num = 600851475143

    # initial conditions:
    divisor = 2
    largest_prime_factor = 0

    while num > 1:
        if num % divisor == 0:
            num /= divisor
            largest_prime_factor = max(largest_prime_factor, divisor)

            divisor = 2
            print(num, largest_prime_factor)
        else:
            divisor += 1
    print(largest_prime_factor)


if __name__ == "__main__":
    main()
