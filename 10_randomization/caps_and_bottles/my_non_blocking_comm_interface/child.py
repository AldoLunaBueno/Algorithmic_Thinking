import time

print("What's your name?")
while True:
    name = input()
    if name == "exit":
        break
    print(f"Hello, {name}")
    time.sleep(1)
    print("What's your name?")