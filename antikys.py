import keyboard

# Current input buffer
arr = []

# target sequance
target_sequences = []

# very bad words
targeted_words = [
    'kys',
    'nigg',
    'fucking',
    'idiot',
    'shit',
    'fuck',
    'asshole',
    'bitch',
    'bastard',
    'prick',
    'wanker',
    'cunt',
    'douche',
    'dick',
    'pussy',
    'cock',
    'blowjob',
    'tits',
    'slut',
    'retard',
    'whore',
    'fag',
    'faggot',
    'motherfucker',
    'scumbag',
    'dumbass',
    'crap',
    'arse',
    'arsehole',
    'twat',
    'bugger',
    'bollocks',
    'tosser',
    'wank',
    'jackass',
    'moron',
    'screw',
    'loser',
    'bimbo',
    'skank',
    'knob',
    'nutjob',
    'weirdo',
    'psycho',
    'bastards',
    'piss',
    'pissing',
    'arsewipe',
    'shitface',
    'fuckwit',
    'shithead',
    'dipshit',
    'asshat',
    'tool',
    'douchebag',
    'numbnuts',
    'jerk',
    'creep',
    'snitch',
    'simp',
    'virgin',
    'incel',
    'cum',
    'sperm',
    'horny',
    'horndog',
    'pedophile',
    'pedo',
    'necrophile',
    'cocksucker',
    'balls',
    'suckit',
    'lickme',
    'anus',
    'bootlicker',
    'freak',
    'scum',
    'trash',
    'garbage',
    'dirtbag',
    'hellhole',
    'burninhell',
    'die',
    'goaway',
    'kill',
    'murderer',
    'hateyou',
    'disgusting'
]

# simplier adding of words
for item in targeted_words:
    target_sequences.append(list(item))  # convert targeted_words strings into characters


def checkArr(arr):
    for sequence in target_sequences:
        # check if stored symbols matches target ones
        if arr == sequence:
            # remove swear word (no swear words!!)
            for _ in range(len(arr)):
                keyboard.send('backspace')
            return True
    return False

while True:
    # wait for keyboard event
    event = keyboard.read_event()

    if event.event_type == "down":
        key = event.name  # get symbol

        # avoid adding invalid keys (e.g., shift, ctrl, etc.)
        if len(key) == 1:
            arr.append(key)

        # get maximal length of target
        max_length = max(len(seq) for seq in target_sequences)
        arr = arr[-max_length:] 

        print(f"Current buffer: {arr}")

        # if swear word is true clear arr
        if checkArr(arr):
            arr = []
        else:
            # 0 idea how this works but it works ty gpt
            if not any(arr[:len(seq)] == seq[:len(arr)] for seq in target_sequences):
                arr = []
