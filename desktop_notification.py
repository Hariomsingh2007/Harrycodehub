from PyQt5 import Qt
import sys

app = Qt.QApplication(sys.argv)
tray = Qt.QSystemTrayIcon()
tray.show()
tray.showMessage("Notify", "Hai Harry how are you")
