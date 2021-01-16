"""Task
The provided code stub reads and integer, n, from STDIN. For all non-negative integers i < n, print i*i
where 1 <= n <=20.
"""

if __name__ == '__main__':
    a = int(input())
    if 1<= a <= 20:
        for i in range(0, a):
            print(i*i)
