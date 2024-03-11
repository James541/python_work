messages = ['wtf brother', 'hello good sir', 'omw', 'a number 6 with extra dip']
printed_messages = []

def show_messages(messages, printed_messages):
    while messages:
        current_message = messages.pop()
        print(current_message)
        printed_messages.append(current_message)


show_messages(messages, printed_messages)

print(messages)
print(printed_messages)