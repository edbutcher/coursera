largest = None
smallest = None
while True:
    num = input("Enter a number: ")

    if num == "done": break
    if len(num) < 1: break

    try:
        num = int(num)
    except:
        print("Invalid input")
        continue

    largest =
    smallest =
    print(num, largest, smallest)

print("Maximum", largest)