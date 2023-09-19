def play_mini_golf():
    # Prompt for the user's name
    name = input("Enter your name: ")

    # Prompt for the number of holes to play (3 or 6)
    holes_to_play = int(input("Enter the number of holes you'd like to play (3 or 6): "))

    # Initialize variables to keep track of score and par
    total_putts = 0
    total_par = holes_to_play * 3

    # Iterate through each hole and prompt for the number of putts
    for hole_num in range(1, holes_to_play + 1):
        hole_par = 3  # Par for each hole is 3
        putts = int(input(f"How many putts for hole {hole_num}? (par: {hole_par}): "))
        total_putts += putts

    # Calculate the golfer's total par for the round
    par_difference = total_putts - total_par

    # Determine the message based on the par difference
    if par_difference < 0:
        message = f"Great job, {name}! Your total par was: {par_difference}."
    elif par_difference > 0:
        message = f"Nice try, {name}... Your total par was: +{par_difference}."
    else:
        message = f"Good game, {name}. Your total par was: 0."

    print(message)


if __name__ == "__main__":
    print("Welcome to the Mini Golf Game!")
    play_mini_golf()
