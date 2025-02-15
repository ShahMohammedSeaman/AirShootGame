from PyQt6.QtWidgets import QGraphicsTextItem
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont



class Health(QGraphicsTextItem):
    def __init__(self):
        super().__init__()


        self.health = 3

        self.setPlainText("Health :" +str(self.health))
        self.setDefaultTextColor(Qt.GlobalColor.red)
        self.setFont(QFont("SansSerif", 18))




    def decrease(self, amount=1):
        self.health -= amount


        if self.health <0:
            self.health = 0

        self.setPlainText(f"Health : {self.health}")


    def is_alive(self):
        return self.health > 0
