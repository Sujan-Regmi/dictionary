d1 = {
    1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
    6: "six", 7: "seven", 8: "eight", 9: "nine"
}

d2 = {
    10: "ten", 20: "twenty", 30: "thirty", 40: "forty",
    50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty",
    90: "ninety", 100: "one hundred"
}

n = int(input("Enter a number (1-101): "))

if n in d1:
    print(f"Spelling of {n} is {d1[n]}")

elif n in d2:
    print(f"Spelling of {n} is {d1[n]}")

elif 11 <= n <= 19:
    d2 = {
        11: "eleven", 12: "twelve", 13: "thirteen",
        14: "fourteen", 15: "fifteen", 16: "sixteen",
        17: "seventeen", 18: "eighteen", 19: "nineteen"
    }
    print(f"Spelling of {n} is {d2[n]}")

elif 21 <= n <= 99:
    t = (n // 10) * 10
    u = n % 10
    print(f"Spelling of {n} is {d2[t]} {d1[u]}")

elif n == 101:
    print("Spelling of 101 is one hundred one")

else:
    print("Invalid input")