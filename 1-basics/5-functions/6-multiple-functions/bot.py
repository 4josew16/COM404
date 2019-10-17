
def display_ladder(steps):
    steps=int(input())
    print("| " * steps)
    print("* " * steps)
    print("| " * steps)
    print("* " * steps)
    print("| " * steps)
    print("* " * steps)
    print("| " * steps)
    print("* " * steps)


def create_ladder():
    print("Please enter a number of steps")

create_ladder()
display_ladder(1)
