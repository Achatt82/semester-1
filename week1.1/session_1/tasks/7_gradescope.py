
def InputValue():
    while True:
        try:
            val = float(input("Enter Value: "))
            break
        except ValueError:
            print("Invalid input")

    return val

val1 = InputValue()
val2 = InputValue()
res = val1 * val2

print(f"Result {res}")