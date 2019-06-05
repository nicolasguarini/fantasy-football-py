import time
import random


class Match:
    def __init__(self, team_1, team_2):
        self.team_1 = team_1
        self.team_2 = team_2
        self.score = [0, 0]

    def play(self):
        team_1_strength = self.team_1.formation.strength()
        team_2_strength = self.team_2.formation.strength()

        totale_strength = team_1_strength + team_2_strength
        team_1_win_percentage = team_1_strength * 100 / totale_strength

        play_time = 0

        while play_time < 30:
            extracted_number = extract_casual_number()

            if extracted_number <= 100:
                if extracted_number <= team_1_win_percentage:
                    self.score[0] += 1
                    goal_notification(self.team_1, self.score)
                else:
                    self.score[1] += 1
                    goal_notification(self.team_2, self.score)

            time.sleep(1)
            play_time += 1

        self.result_notification()

    def result_notification(self):
        if self.score[0] > self.score[1]:
            victory_notification(winner=self.team_1, score=self.score)
                              
        elif self.score[0] == self.score[1]:
            draw_notification(self.score)

        else:
            victory_notification(winner=self.team_2, score=self.score)
                              

def extract_casual_number():
    return random.randint(1, 300)


def victory_notification(winner, score):
    print("---\nThe team %s wins the match!!\n--\nScore: %d - %d\n" % (winner.name, score[0], score[1]))


def draw_notification(score):
    print("---\nDraw!!\n----\nScore: %d - %d\n" % (score[0], score[1]))


def goal_notification(team_that_scored, score):
    print("---\nThe team %s made goal!!!\nScore: %d - %d\n" % (team_that_scored.name, score[0], score[1]))
