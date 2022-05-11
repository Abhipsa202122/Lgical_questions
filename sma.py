largest = 0
smallest = 0
while True:
    num = input("Enter a number: ")
    if num =="done": break
    try:
           fnum = float(num)
    except:
        print("Invalid input")
        continue

    if largest == 0 or num >= largest: largest = num
    else: largest= largest
    if smallest == 0 or num <= smallest: smallest = num
    else: smallest= smallest

print("Maximum is", largest)
print("Minimum is", smallest)
