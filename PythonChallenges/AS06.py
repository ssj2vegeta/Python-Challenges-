vowelchecker = input("check for number of vowels")
count = 0
vowelchecker = vowelchecker.strip().lower()
for i in vowelchecker:
    if i in ["a","e","i","o","u"]:
        count += 1
    else:
        continue

print(f"the number of times vowels appeared in {vowelchecker} is {count}")
