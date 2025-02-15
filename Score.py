from PyQt6.QtWidgets import QGraphicsTextItem
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont




class Score(QGraphicsTextItem):
    def __init__(self):
        super().__init__()


        self.score = 0


        self.setPlainText(("Score :" + str(self.score)))
        self.setDefaultTextColor(Qt.GlobalColor.black)
        self.setFont(QFont("SansSerif", 18))


    def increase (self, points=1) :
        self.score += points
        self.setPlainText(f"Score : {self.score}")
