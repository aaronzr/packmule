import time

def typing_speed():
    start_time = time.time()
    # Prompt the user to input a certain number of characters
    print("Enter 100 characters:")
    user_input = input()

    # Check if the user entered the correct number of characters
    if len(user_input) != 100:
        print("Please enter exactly 100 characters.")
        return

    # Calculate how long it took the user to type the 100 characters
    end_time = time.time()
    total_time = end_time - start_time
    
    # Calculate the user's typing speed in words per minute (wpm)
    wpm = round((len(user_input)/5) / (total_time / 60), 2)
    print(f"Done! You typed {user_input} in {wpm} words per minute.")

typing_speed()
