"""Task
Given an integer, n, perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird
Input Format

A single line containing a positive integer, .

Constraints

Output Format

Print Weird if the number is weird. Otherwise, print Not Weird."""

if __name__ == '__main__':
    n = int(input("Enter a number : "))
    if 1 <= n <= 100:
        if n % 2 != 0 or (n % 2 == 0 and n in range(6, 21)):
            print("Weird")
        elif n % 2 == 0 and (n in range(2, 6) or n > 20):
            print("not Weird")
