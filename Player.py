from PyQt6.QtWidgets import QGraphicsPixmapItem
from PyQt6.QtCore import Qt, QUrl
from Bullet import Bullet
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput


class Player(QGraphicsPixmapItem):
    def __init__(self):
        super().__init__()


        self.bullet_sound = QMediaPlayer()
        self.audio = QAudioOutput()
        self.bullet_sound.setAudioOutput(self.audio)


        bullet_sound_url = QUrl.fromLocalFile("bg2.mp3")
        self.bullet_sound.setSource(bullet_sound_url)

    def keyPressEvent(self, event):

        if not self.scene():
            return

        scene_width = self.scene().sceneRect().width()

        if event.key() == Qt.Key.Key_Space:

            bullet = Bullet()


            if self.pixmap():
                bullet.setPos(self.x() + self.pixmap().width() / 2 - bullet.pixmap().width() / 2, self.y())
            else:
                bullet.setPos(self.x(), self.y())

            self.scene().addItem(bullet)


            if self.bullet_sound.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
                self.bullet_sound.stop()

            self.bullet_sound.play()

        elif event.key() == Qt.Key.Key_Left:
            if self.x() > 0:
                self.setPos(self.x() - 10, self.y())

        elif event.key() == Qt.Key.Key_Right:
            if self.x() + (self.pixmap().width() if self.pixmap() else 0) < scene_width:
                self.setPos(self.x() + 10, self.y())

        elif event.key() == Qt.Key.Key_Up:
            self.setPos(self.x(), self.y()-10)

        elif event.key() == Qt.Key.Key_Down:
            self.setPos(self.x(), self.y()+10)

