from PySide6.QtCore import Qt, QSize
import json, random, sys
from PySide6.QtWidgets import QApplication, QMainWindow,QLabel,QLineEdit,QPushButton,QVBoxLayout,QWidget, QLayout, QListWidget
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Random Item Picker")
        self.setFixedSize(250, 400)

        add_item = QPushButton("Add item")
        pick_item = QPushButton("Pick item")
        widgets = [QListWidget, QLineEdit, add_item, QLabel, pick_item]
        layout = QVBoxLayout()
        for widget in widgets:
            if isinstance(widget, QPushButton):
                layout.addWidget(widget, alignment=Qt.AlignmentFlag.AlignHCenter)
                widget.setFixedSize(200, 40)
                
            else:
                layout.addWidget(widget(), alignment=Qt.AlignmentFlag.AlignHCenter)

        central_widget = QWidget()
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)

app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()


    	