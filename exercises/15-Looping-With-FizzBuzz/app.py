def fizz_buzz():
    # ✅↓ Write your code here ↓✅
    for numero in range (1, 101):
        if numero % 3 == 0 and numero % 5 == 0:
            print (f"{numero}: FizzBuzz")
        elif numero % 3 == 0:
            print(f"{numero}: Fizz")
        elif numero % 5 == 0:
            print(f"{numero}:Buzz")
        else: 
            print (f"{numero}:numero")
# ❌↓ DON'T CHANGE THE CODE BELOW ↓❌
fizz_buzz()
