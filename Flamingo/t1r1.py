import keyboard  # Install this package with pip or conda
import time

start_time = time.time()  # start timer
while True:  # infinite loop to run continuously
    print("Start typing...")
    keys = []  # variable that stores all the pressed keys
    for i in range(5):  # capture typing for 5 seconds
        keys.append(keyboard.read_key())
        time.sleep(0.2)
    end_time = time.time()  # stop timer

    total_time = end_time - start_time  # total time taken

    total_words = 0  # number of words for simplicity
    for key in keys:
        if not any(key in s for s in ["(", ")", " ", "\t", "'", ","]):  # all the other characters are counted as a word
            total_words += 1

    print("You typed {} words in {} seconds, your typing speed is {} words per minute.".format(total_words, total_time, int(total_words / total_time * 60)))
