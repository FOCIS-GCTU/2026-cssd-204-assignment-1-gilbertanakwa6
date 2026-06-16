# File: GNA.py
# Description: Simulates a simplified version of the dice game craps and prints statistics.
# Assignment Number: 6
#
# Name: <Gilbert Nana Anakwa>
# SID: <2425405055>
# Email: <2425405055@live.gctu.edu.gh>
# Grader: <Mr Augustus Buckman>
#
# On my honor, <Gilbert Nana Anakwa>, this programming assignment is my own work
# and I have not provided this code to any other student.

def main():
    print("This program simulates the dice game of craps.")

    # Prompt user whether they want to set the random seed
    seed_choice = input("Do you want to set the seed? Enter y for yes, anything else for no: ")

    if seed_choice == 'y':
        seed_value = int(input("Enter an int for the initial seed: "))
        random.seed(seed_value)

    # Get the total number of rounds to simulate
    num_rounds = int(input("Enter the number of rounds to run: "))

    # If the number of rounds is invalid, print zeros and exit
    if num_rounds <= 0:
        print("Player won 0 times in 0 rounds.")
        print("Maximum number of rolls in a round = 0")
        return

    # Set up counters for wins and longest round
    wins = 0
    max_rolls = 0

    # Run the simulation for each round
    for round_num in range(num_rounds):
        # First roll of the round
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        initial_sum = die1 + die2
        rolls_in_round = 1

    # Determine the outcome of the initial roll
      if initial_sum == 7 or initial_sum == 11
    # Immediate win for the player
      wins += 1
      elif initial_sum == 2 or initial_sum == 3 or initial_sum == 12:
    # Immediate loss, do nothing
      pass
      else:
    # The point is established
      point = initial_sum

    # Keep rolling until the player wins or loses
      while True
      die1 = random.randint(1, 6)
                die2 = random.randint(1, 6)
                roll_sum = die1 + die2
                rolls_in_round += 1

                if roll_sum == point:
                    # Player wins by hitting the point again
                    wins += 1
                    break
                elif roll_sum == 7:
                    # Player loses by rolling a seven before the point
                    break

    # Track the highest number of rolls in any single round
        if rolls_in_round > max_rolls:
            max_rolls = rolls_in_round

    # Choose correct singular or plural words for output
        if num_rounds == 1:
        round_word = "round"
        else:
        round_word = "rounds"

       if wins == 1:
        time_word = "time"
        else:
        time_word = "times"

    # Display the final results
    print(f"Player won {wins} {time_word} in {num_rounds} {round_word}.")
    print(f"Maximum number of rolls in a round = {max_rolls}")


main()


# 1. Does the simulation show that casinos win long-term? Why?*  
Yes. In the simulation, the player won 4,935 out of 10,000 rounds with seed 1212 - that’s 49.35%. With 10,000,000 rounds and seed -251, they won 4,927,042 times, about 49.27%.  
Since the player wins under 50% of the time, the house wins over 50%. That edge means the casino makes a profit over many rounds.

*2. You have $2,000. Option: keep it, or play craps betting $10 per round until you’re broke or hit 500 games. Which would you pick and why?*  
I’d keep the $2,000. The simulation shows the player only wins ∼49.3% of the time, so the expected value of each $10 bet is negative. Over 500 games you’d expect to lose money on average.  
Keeping the cash guarantees you still have $2,000. Playing gives you a high chance of walking away with less.