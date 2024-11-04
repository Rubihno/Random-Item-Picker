from PySide6.QtCore import Qt, QSize
import json, random, sys
from PySide6.QtWidgets import QApplication, QMainWindow,QLabel,QLineEdit,QPushButton,QVBoxLayout,QWidget, QLayout, QListWidget, QKeySequenceEdit
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Random Item Picker")
        self.setFixedSize(250, 400)

        self.list = QListWidget()
        self.item_tekst = QLineEdit(self)
        self.add_item = QPushButton("Add item")
        self.label = QLabel()
        self.pick_item = QPushButton("Pick item")

        self.pick_item.setShortcut("space")
        self.add_item.setShortcut("return")

        widgets = [self.list, self.item_tekst, self.add_item, self.label, self.pick_item]
        layout = QVBoxLayout()

        for widget in widgets:
            if isinstance(widget, QPushButton):
                layout.addWidget(widget, alignment=Qt.AlignmentFlag.AlignHCenter)
                widget.setFixedSize(200, 40)  
                widget.setStyleSheet("""
                font-size: 12px;
                background-color: RoyalBlue;
                color: white;
                """)
            elif isinstance(widget, QLineEdit):
                layout.addWidget(widget, alignment=Qt.AlignmentFlag.AlignHCenter) 
            elif isinstance(widget, QListWidget):
                layout.addWidget(widget, alignment=Qt.AlignmentFlag.AlignHCenter) 
            else:
                layout.addWidget(widget, alignment=Qt.AlignmentFlag.AlignHCenter)

        central_widget = QWidget()
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)

        self.add_item.clicked.connect(self.text_toevoegen)
        self.list.currentTextChanged.connect(self.text_changed)

        self.pick_item.clicked.connect(self.random_item)

    def opslaan_items(self, data):
        try:
            with open("gui-opslag.json", "r") as f:
                bestaande_data = json.load(f)
            if not isinstance(bestaande_data, list):
                bestaande_data = []
        except(FileNotFoundError, json.JSONDecodeError):
            bestaande_data = []

        bestaande_data.append(data)

        with open("gui-opslag.json", "w") as f:
            json.dump(bestaande_data, f, indent=4)
        return bestaande_data

    def ophalen_items(self):
        with open("gui-opslag.json", "r") as f:
            huidige_data = json.load(f)
        return huidige_data

    # Voegt tekst toe aan de lijst en json file indien er tekst aanwezig is
    def text_toevoegen(self):
        item_text = self.item_tekst.text()
        if item_text:
            self.list.addItem(self.item_tekst.text())
            self.opslaan_items(item_text)
            self.item_tekst.clear()

    # Wordt aangeroepen als de lijst wordt aangepast
    def text_changed(self, text):
        print(text)

    # Laat een random item uit de lijst zien en verwijdert de lijst
    def random_item(self):
        try: 
            random_item = random.choice(self.ophalen_items())
            self.label.setText(random_item)

            open("gui-opslag.json", "w").close()
        except(json.decoder.JSONDecodeError):
            self.label.setText("Geen items gevonden!")

app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()


    	