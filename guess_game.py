import random

print("🎯 بازی حدس عدد 🎯")
print("من یه عدد بین 1 تا 100 انتخاب کردم. حدس بزن!")

number = random.randint(1, 100)
guess = None
tries = 0

while guess != number:
    guess = int(input("حدس شما: "))
    tries += 1

    if guess < number:
        print("عدد من بزرگ‌تره! ⬆️")
    elif guess > number:
        print("عدد من کوچیک‌تره! ⬇️")
    else:
        print(f"آفرین! عدد {number} رو بعد از {tries} تلاش پیدا کردی 🎉")