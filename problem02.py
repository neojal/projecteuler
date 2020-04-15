"""
https://projecteuler.net/problem=2

Even Fibonacci numbers

Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
"""

import queue


def main():
    limit = 4_000_000
    q = queue.Queue(2)

    # starting conditions:
    q.put(1)
    q.put(2)
    result = 2

    current = 0
    while current <= limit:
        num1 = q.get()
        num2 = q.get()
        current = num1 + num2
        if current % 2 == 0:
            result += current
        q.put(num2)
        q.put(current)
    print(result)


if __name__ == "__main__":
    main()
