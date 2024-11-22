#Program 2 – Message Redaction
#Description:   Design and write a program that counts and removes all desired letters from 
#               any user-entered sentence or phrase.

#Student #: Brayden Creese
#Student Name: W0491583

def messageRedaction():
    while True:
        phrase = input("Type a phrase (or 'quit' to exit): ")
        if phrase.lower() == "quit":
            break

        lettersRedacted = input("Enter letters to redact (comma-separated): ").lower()
        redactedpPhrase = ""
        redactedCount = 0

        for char in phrase:
            if char.lower() in lettersRedacted:
                redactedpPhrase += "_"
                redactedCount += 1
            else:
                redactedpPhrase += char

        print("Number of letters redacted:", redactedCount)
        print("Redacted phrase:", redactedpPhrase)
        print()

messageRedaction()

