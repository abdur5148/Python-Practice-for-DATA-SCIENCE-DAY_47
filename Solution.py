def compute():
    return 5/0


try:
    print(compute())

except Exception as e:
    print("You are doing WRONG!!!")
