def main():
lower = int(input(" "))
 upper = int(input(" "))
 for n in range(lower, upper + 1):
order = len(str(n))
sum = 0
temp = n
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10
       if n == sum:
       print(n)
       if __name__ == '__main__':
    main()
