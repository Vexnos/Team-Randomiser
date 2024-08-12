'''
-------------------------
   File: teamrandomser.py
Project: Team Randomiser
 Author: Vexnos
   Date: 2024-08-13
Version: 1.0.0
-------------------------
'''
#-------Libraries-------
from random import choice

#-------Functions-------
# Draw Function
def draw(players):

    # Define empty teams
    team1 = []
    team2 = []

    # Calculate the team size based on user input of players
    team_size = round(len(players) / 2)

    # Draw until you run out of players to choose from
    while len(players) != 0:
        # Once team 1 reaches its maximum size, start drawing for team 2
        if len(team1) < team_size:
            # Randomly choose a player, append to team list and remove from the players list
            random_pick = choice(players)
            team1.append(random_pick)
            players.remove(random_pick)
        else:
            random_pick = choice(players)
            team2.append(random_pick)
            players.remove(random_pick)

    # Return teams when finished
    return team1, team2

#-------Main-Routine-------
if __name__ == "__main__":
    # Loop the program until the user quits
    drawing = True
    while drawing:
        # Get players from user and store as a list
        players_input = input("\nEnter your players here (each one sperated by a comma): ")
        players = players_input.split(", ")

        # Display a balancing warning if the user has entered an odd amount of players
        if len(players) % 2 != 0:
            odd_warning = input("\nWARNING: You have an odd amount of players, team distribution will NOT be balanced! Are you sure you want to continue? (y/n): ")
            if not odd_warning.lower().startswith("y"):
                # If the user does not want to continue with an odd amount of players, allow them to select players again
                continue

            # ---Old Code---
            # print("\nOdd numbered teams are not allowed")
            # continue

        # ---Debugging---
        # print(", ".join(players))
        # players = ["Vexnos", "Matthew", "Joshua", "Atomhix"]

        # Retrieve teams from the Draw function
        team1, team2 = draw(players)

        # Print the teams
        print("\nTeam 1: " + ", ".join(team1))
        print("\nTeam 2: " + ", ".join(team2))

        # Check if the user wants to quit or redraw
        drawing = input("\nDo you want to redraw? (y/n): ").lower().startswith("y")