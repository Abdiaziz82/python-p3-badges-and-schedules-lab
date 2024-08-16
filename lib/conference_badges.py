def badge_maker(name):
    return f"Hello, my name is {name}."


def batch_badge_creator(names):
    return [f"Hello, my name is {name}." for name in names]

def assign_rooms(names):
    messages = []
    for i, name in enumerate(names, start=1):
        messages.append(f"Hello, {name}! You'll be assigned to room {i}!")
    return messages

def printer(messages):
    badge_messages = batch_badge_creator(messages)
    room_assignments = assign_rooms(messages)

    for message in badge_messages:
        print(message)
    
    for assignment in room_assignments:
        print(assignment)
