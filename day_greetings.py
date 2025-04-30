import time

def greet_user():
    current_hour = time.localtime().tm_hour

    if 5 <= current_hour < 12:
        print("Good Morning!")
    elif 12 <= current_hour < 18:
        print("Good Afternoon!")
    elif 18 <= current_hour < 22:
        print("Good Evening!")
    else:
        print("Hello! It's quite late Good night, take care!")

if __name__ == "__main__":
    greet_user()