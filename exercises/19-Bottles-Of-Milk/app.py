# ✅↓ Write your code here ↓✅
def number_of_bottles():
    for i in range (99, 0, -1):
        if i == 1:
            print("1 bottle of milk on the wall, 1 bottle of milk.")
            print("Take one down and pass it around, no more bottles of milk on the wall.")
        elif i >= 1:
            print(f"{i} bottles of milk on the wall {i} bottles of milk.")
    print("No more bottles of milk on the wall, no more bottles of milk.")
    print("Go to the store and buy some more, 99 bottles of milk on the wall.")

number_of_bottles()      