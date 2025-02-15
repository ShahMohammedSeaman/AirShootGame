from PyQt6.QtWidgets import QGraphicsPixmapItem
from PyQt6.QtCore import QTimer
from Enemy import Enemy
from Score import Score
from PyQt6.QtGui import QPixmap





class Bullet(QGraphicsPixmapItem):
    def __init__(self):
        super().__init__()


        self.setPixmap(QPixmap("bullet1.png"))

        self.timer = QTimer()

        self.timer.timeout.connect(self.move)

        self.timer.start(50)


    def move(self):
        self.setPos(self.x(), self.y()-10)


        colliding_items = self.collidingItems()

        for item in colliding_items:
            if isinstance(item, Enemy):
                for scene_items in self.scene().items():
                    if isinstance(scene_items, Score):
                        scene_items.increase()
                        print("Score increased")
                self.scene().removeItem(item)
                self.scene().removeItem(self)

                print("Bullet hit an Enemy")

                self.timer.stop()


                del item
                del self

                return














