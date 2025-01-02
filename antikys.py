import keyboard
import random

# Current input buffer
arr = []

# target sequence
target_sequences = []

# very bad words
targeted_words = [
    'kys', 
    'nigg', 
    'fuck', 
    'idiot', 
    'shit', 
    'faggot', 
    'bitch', 
    'stfu', 
    'asshole', 
    'dumbass', 
    'bastard', 
    'retard', 
    'whore',
    'kurwa',
    'talon e out of bridge'

]


# simpler adding of words
for item in targeted_words:
    target_sequences.append(list(item))  # convert targeted_words strings into characters

# positive words!
positive_words = [
    'have a nice day!',
    'enjoy the rest of your game!', 
    'keep yourself safe!', 
    'share love', 
    'love you!', 
    'stay awesome!', 
    'spread positivity', 
    'be kind', 
    'you are amazing!'
]


def checkArr(arr):
    global positive_count
    print('Current buffer:', arr)

    for sequence in target_sequences:
        # check if swear word exists in current buffer
        # example: converts ['f', 'u', 'c', 'k'] to 'fuck' in converts ['h', 'e', 'l', 'l', 'o', ' ', 'f', 'u', 'c', 'k', ' ', 'y', 'o', 'u'] to 'hello fuck you'
        # so if fuck is in arr it will do the cool thingy
        if ''.join(sequence) in ''.join(arr):

            # remove swear word and replace it with positive one instead! 💘
            for _ in range(len(sequence)):
                keyboard.send('backspace')

            # choose random message each time
            positive_count = random.randrange(0, len(positive_words), 1)

            # write positive message
            keyboard.write(positive_words[positive_count], delay=0.01)

            return True
    return False

while True:
    # wait for keyboard event
    event = keyboard.read_event()

    if event.event_type == "down":
        key = event.name  # get symbol
        
        # if user misstypes like kyes then backspaces 2x and presses s it wouldn't register it as swear word
        # so this should fix it
        if key == "backspace":
            if arr:
                arr.pop()
        
        # avoid adding invalid keys (e.g., shift, ctrl, etc.)
        if len(key) == 1:
            arr.append(key)

        # Trim the buffer to a reasonable length to prevent overflow
        max_length = max(len(seq) for seq in target_sequences)
        arr = arr[-(max_length + 5):]  # Allow some extra context for sentences

        print(f"Current buffer: {arr}")

        # if swear word is true clear arr
        if checkArr(arr):
            arr = []
