def s_and_c():
    array = list(map(int, input("Enter numbers separated by space: ").split()))
    num = int(input("Enter the number to be searched: "))
    count = array.count(num)
    if count > 0:
        print(f"The number {num} appears {count} times.")
    else:
        print(f"The number {num} does not appear in the array.")


s_and_c()

