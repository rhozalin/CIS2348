# Name-Rhozalin Nath
# PS ID: 2050395

class Team:
    def __init__(self, name="none", wins=0, losses=0):
        self.name = name
        self.wins = wins
        self.losses = losses

    def get_win_percentage(self):
        if (self.wins+self.losses==0):
            return 0.0
        else:
            win_percentage=float(self.wins/(self.wins+self.losses))
        return win_percentage
    def print_standing(self):
        win_percentage=self.get_win_percentage()
        if (win_percentage >= 0.5):
            print(f"Congratulations, Team {self.name} has a winning average!")
        else:
            print(f"Team {self.name} has a losing average.")

if __name__ == "__main__":
    team_name = input()
    team_wins = int(input())
    team_losses = int(input())
    team = Team(team_name,team_wins,team_losses)
    team.print_standing()

