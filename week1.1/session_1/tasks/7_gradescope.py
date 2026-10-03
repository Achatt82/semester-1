
def InputValue():
    try:
        val = float(input("Enter Value: "))
    except ValueError:
        print("That is not a number")

    return val

val1 = InputValue()
val2 = InputValue()
res = val1 * val2

print(f"Result {res}")