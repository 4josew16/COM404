def climb_ladder(steps_remaining, steps_crossed):
    if steps_remaining < steps_crossed:
        print("Still some way to go!")
    else:
        print("We made it!")
climb_ladder(2,5)
climb_ladder(5,5)