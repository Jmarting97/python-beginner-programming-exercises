total = int(input('How much money do you have in your pocket\n'))

# ✅ ↓ YOUR CODE HERE ↓ ✅
if total > 100:
    print("Give me your money!")
elif total > 50:
    print("¡Cómprame un cafe!")
elif total <= 50:
    print("¡Eres probre!")
