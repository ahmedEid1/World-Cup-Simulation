import tkinter as tk

from world_cup_logic import WorldCup
from screens.GroupStageScreen import GroupStageScreen
from screens.InitialScreen import InitialScreen
from screens.intermediateStageScreen import intermediateStageScreen
from screens.FinalScreen import FinalScreen
from screens.WinnerScreen import WinnerScreen


class MainWindow(tk.Tk):
    def __init__(self, wc):
        super().__init__()
        self.setWorldCup(wc)
        self.initUI()

    def setWorldCup(self, wc):
        self.worldCup = wc
        self.pots = wc.pots
        self.groups = wc.groups
        self.knockout_stage_winners = wc.knockout_teams
        self.round_of_16_matchs = wc.round_of_16_matches
        self.round_of_16_winner = wc.round_of_16
        self.quarter_finals_matchs = wc.quarter_final_matches
        self.quarter_finals_winner = wc.quarter_finals
        self.semi_finals_matchs = wc.semi_finals_matches
        self.semi_finals_winner = wc.semi_finals
        self.thrid_place_teams = [team for team in self.quarter_finals_winner if team not in self.semi_finals_winner]
        self.first_place = wc.first_place
        self.second_place = wc.second_place
        self.third_place = wc.third_place

    def initUI(self):
        self.initalScreen = InitialScreen(self)
        self.screen0 = GroupStageScreen(self, self.pots, self.groups)
        self.screen1 = intermediateStageScreen(self, self.knockout_stage_winners, self.round_of_16_matchs,
                                               "Round of 16 Teams.",
                                               "Round of 16 Matches.",
                                               "Round of 16.")
        self.screen2 = intermediateStageScreen(self, self.round_of_16_winner, self.quarter_finals_matchs,
                                               "Quarter Finals Teams.",
                                               "Quarter Finals Matches.",
                                               "Quarter Finals.")
        self.screen3 = intermediateStageScreen(self, self.quarter_finals_winner, self.semi_finals_matchs,
                                               "Semi Finals Teams.",
                                               "Semi Finals Matches.",
                                               "Semi Finals.")
        self.screen4 = FinalScreen(self, self.semi_finals_winner, self.thrid_place_teams)
        self.screen5 = WinnerScreen(self, self.first_place, self.second_place, self.third_place)

        self.screens = [self.screen0, self.screen1, self.screen2, self.screen3, self.screen4, self.screen5]
        self.currentScreen = -1
        self.initalScreen.pack()

        self.title('World Cup App')
        self.geometry('900x500')
        self.mainloop()

    def showNextScreen(self):
        self.currentScreen += 1

        self.showScreen()

    def showPrevScreen(self):
        self.currentScreen -= 1
        self.showScreen()

    def resetScreen(self):
        self.currentScreen = 0
        self.showScreen()

    def showScreen(self):
        if (self.currentScreen == 0):
            self.initalScreen.pack_forget()
        for screen in self.screens:
            screen.pack_forget()
        self.screens[self.currentScreen].pack()


if __name__ == '__main__':
    rankings = {
        "Brazil": 1,
        "Germany": 2,
        "Spain": 3,
        "Argentina": 4,
        "France": 5,
        "Belgium": 6,
        "Portugal": 7,
        "Switzerland": 8,
        "England": 9,
        "Colombia": 10,
        "Mexico": 11,
        "Uruguay": 12,
        "Croatia": 13,
        "Russia": 14,
        "Denmark": 15,
        "Sweden": 16,
        "Poland": 17,
        "Senegal": 18,
        "Nigeria": 19,
        "Japan": 20,
        "Iran": 21,
        "South Korea": 22,
        "Egypt": 23,
        "Australia": 24,
        "Peru": 25,
        "Costa Rica": 26,
        "Serbia": 27,
        "Iceland": 28,
        "Tunisia": 29,
        "Panama": 30,
        "Morocco": 31,
        "Saudi Arabia": 32
    }

    window = MainWindow(WorldCup(rankings))
