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
def string_len(a):
    b=0
    for i in a:
        b+=1
    return b
def non_repeat_char(a):
    for i in range(len(a)):
        is_repeated = False
        for j in range(len(a)):
            if i != j and a[i] == a[j]:
                is_repeated = True
                break
        
        if not is_repeated:
            print(f"First non-repeating character is: {a[i]}")
            return a[i]
            
    print("None found")
def freq_count(a):
    b={}
    for i in a:
        if i not in b:
            b[i]=1
        else:
            b[i]+=1
    return b
def rem_dupli_char(a):
    b=set()
    result=""
    for char in a:
        if char not in b:
            result+=char
            b.add(char)
    return result
def longest_word(a):
    b=0
    c=""
    for i in a.split():
        if len(i)>b:
            b=len(i)
            c=i
        elif len(i)==b:
            print(f"Longest words are: {c} and {i}")
    return c
def max_min_array(a):
    b=a[0]
    c=a[0]
    for i in a:
        if i > b:
            b=i
        if i < c:
            c=i
    print(f"Maximum element: {b} \n Minimum element: {c}")
def sum_array(a):
    sum=0
    for i in a:
        sum+=i
    print(f"Sum of elements= {sum}")
def rev_array(a):
    b = []
    for i in range(len(a) - 1, -1, -1):
        b.append(a[i])
    return b

def second_largest(a):
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            if a[i] > a[j]:
                temp=a[i]
                a[i]=a[j]
                a[j]=temp
    return a[len(a)-2]
def odd_even(a):
    odd,even=0,0
    for num in a:
        if num %2==0:
            even+=1
        else:
            odd+=1
    print(f"odd number count={odd} and even number count = {even}")
def two_sum_values(a, target):
    seen = set()
    
    for num in a:
        b = target - num
        if b in seen:
            return [b, num]
        seen.add(num)
    return None
def freq_count(a):
    b={}
    for i in a:
        if i not in b:
            b[i]=1
        else:
            b[i]+=1
    return b
def missing_num(a):
    b=[]
    for i in range(a[0],a[-1]+1):
        if i not in a:
            b.append(i)
    print(b)
missing_num([1,2,4,5,6,8,9])
def merge_sort(a,b):
    result=[]
    c=0
    d=0
    while c<len(a) and d<len(b):
        if a[c]<b[d]:
            result.append(a[c])
            c+=1
        else:
            result.append(b[d])
            d+=1
    result.extend(a[c:])
    result.extend(b[d:])

    return result
