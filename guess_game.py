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
        import random

number = random.randint(1, 100)
attempts = 0

motivations = [
    "نزدیک بود! یه کم بیشتر فکر کن 😅",
    "نه هنوز درست نیست، ولی داری خوب پیش می‌ری 💪",
    "اشتباهه، ولی ناامید نشو! تو می‌تونی 😎",
    "یه تلاش دیگه! شاید این بار درست باشه 🎯",
    "فکر کن... عددت خیلی دور نیست 🤔"
]

print("بازی حدس عدد شروع شد! عددی بین ۱ تا ۱۰۰ رو حدس بزن:")

while True:
    guess = int(input("حدس شما: "))
    attempts += 1

    if guess == number:
        print(f"آفرین! عدد درست بود 🎉 شما در {attempts} تلاش حدس زدی.")
        break
    elif guess < number:
        print("عدد بزرگ‌تره!")
    else:
        print("عدد کوچک‌تره!")

    # پیام انگیزشی تصادفی
    print(random.choice(motivations))
