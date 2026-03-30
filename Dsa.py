def check_prime(a):
    if a<=1:
        print("Value Error")
    for i in range(2,int(a**0.5)+1):
        if a % i==0:
             return False
        
    return True

def factorial(a):
    if a==0 or a==1:
        return 1
    else:
        return a*factorial(a-1)
def num_palindrome(a):
      r=0
      temp=abs(a)
      while temp!=0:
          r=(r*10)+(temp%10)
          temp=temp//10
      if r==abs(a):
          print("Number is a palindrome")
      else:
           print("Number is not a palindrome")
def sum_digits(a):
    s=0
    temp=abs(a)
    while temp!=0:
        s=s+temp%10
        temp=temp//10
    print(s)
def print_divisor(a):
             
    b=[]
    for i in range(1,a+1):
        if a%i==0:
            
            b.append(i)
    return b
def check_ArmstrongNumber(a):
    r=0
    num=str(a)
    digit=len(num)
    for i in num:
        r+=int(i)**digit
    
    if r==a:
        print(f"{a} is an armstrong number")
    else:
         print(f"{a} is not an armstrong number")
def primeNumbers(a):
    for i in range(2,a):
        if check_prime(i):
            print(i,end=" ")
def find_gcd_lcm(a,b):
    a1=print_divisor(a)
    b1=print_divisor(b)
    c1=[]
    for i in a1:
        if i in b1:
            c1.append(i)
    c=c1[len(c1)-1]
    lcm=(a*b)//c
    print(f"LCM = {lcm} GCD ={c}")
def dec_bin(a):
    r=""
    tem=a
    while tem!=0:
        r=str(tem%2)+r
        tem=tem//2
    return r
def check_perfectNumber(a):
    r=0
    temp=print_divisor(a)
    for i in temp:
        if i ==temp[len(temp)-1]:
            break
        r+=i
        
    if r==a:
        print(f"{a} is a perfect number")
    else:
        print(f"{a} is not a perfect number")
def rev_string(a):
    b=""
    for i in range(len(a)-1,-1,-1):
        b+=a[i]
    return b
def check_str_palindrome(a):
    b=rev_string(a)
    if b==a:
        print(f"{a} is a palindrome")
    else:
        print(f"{a} is not a palindrome")
def count_vow_cons(a):
    v="aeiouAEIOU"
    b=0
    for char in a:
        if char in v:
            b+=1
    c=len(a)-b
    print(f"Number of vowels = {b}")
    print(f"Number of consonents = {c}")

