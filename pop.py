l = eval(input("Enter a list: "))
n = len(l)
if n % 2 == 0:
    result = l[n//2:] + l[n//2:][::-1]
else:
    result = l[n//2+1:] + [l[n//2]] + l[n//2+1:][::-1]
print(result)