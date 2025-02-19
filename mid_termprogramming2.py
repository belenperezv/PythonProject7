# question 1
a = 16
a = a // 2
print(a**2)
a = a + 11
print(a+1)
a = a - 3
print(a)

# question 2
#What will the following code print?
print((2+3)*6/2 and 18.0)

#question 3
import datetime
a = 7
b = 2
today = datetime.datetime.today()
day_of_week = today.weekday() #0 (monday) and 6 (sunday)
month_of_year = today.month # 1 (jan) and 12 (dec)
a = a + day_of_week
b += month_of_year
print(a)
print(b)
c = a + b
print(c)
d = "xyz" * (c // 3)
print(d)

#question 4
def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False
numbers = [
    "2704702208931031198668911301398022074072",  # A
    "4257304920394478392772938744930294037524",  # B
    "0974101607733149676776769413377061014790",  # C
    "7798338247658278460338648728567428338977"   # D
]
# revise each number
for i, num in enumerate(numbers, start=1):
    print(palindrome(num))

# question 5
def count_pattern_occurrences(text):
    count = 0
    start = 0  # Start searching from the beginning
    while True:
        # Step 1: Find the next occurrence of 'un'
        start = text.find("un", start)
        if start == -1:  # If no 'un' found, break the loop
            break
        # Step 2: Find the next occurrence of 'an' after 'un'
        end = text.find("an", start)
        if end != -1:  # If 'an' is found after 'un'
            count += 1  # Increase match count
            start = end + 3  # Move the search forward
        else:
            break  # No more valid patterns found
    return count  # Return total number of matches
text = "Uncertain,Unbroken,Unclean,Underman,Underplan,Unshaken"
print(count_pattern_occurrences(text))

#question 7
import random
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))
for i in range(len(random_numbers)):
    if random_numbers[i] > 50:
        random_numbers[i] = random.randint(20, 30)  # Replacing with 20 and 30
    else:
        random_numbers[i] = "XX"
print(random_numbers)
# question 8
import validators
def is_valid_url(url):
    """Check if the given URL is valid."""
    return validators.url(url) # Returns true if valid, false if not
urls = [
    "https://gutenberg.org/cache/epub/77/p977.txt",
    "https://www.instagram.com/bakewithzoha/",
    "invalid-url",
    "https://www.economist.com/"
]
for url in urls:
    if is_valid_url(url):
        print(f"is a Valid URL: {url}")
    else:
        print(f"is an Invalid URL:{url}")

#question 9
import datetime
def days_since_last_birthday(birthday):
    # Step 1: Extract day and month from the birthday string
    day, month, year = map(int, birthday.split("-"))
    # Step 2: Get today's date
    today = datetime.date(2025,2,19)
    # Step 3: Determine last birthday
    this_year_birthday = datetime.date(2025, 7, 24)  # This year's birthday
    if today >= this_year_birthday:
        # If birthday already happened this year, use this year's date
        last_birthday = this_year_birthday
    else:
        # If birthday hasn't happened yet, use last year's birthday
        last_birthday = datetime.date(today.year - 1, month, day)
    # Step 4: Calculate the difference in days
    days_passed = (today - last_birthday).days
    return days_passed
# Example usage
print(days_since_last_birthday("24-07-2004")) # the year, is not even 1 , so we count days




