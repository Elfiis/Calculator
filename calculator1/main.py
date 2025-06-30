import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton,
    QGridLayout, QLineEdit, QVBoxLayout
)
from PyQt6.QtCore import Qt


class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hesap Makinesi")
        self.setFixedSize(300, 400)

        main_layout = QVBoxLayout()

        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setFixedHeight(50)
        self.display.setStyleSheet("font-size: 24px;")
        main_layout.addWidget(self.display)

        layout = QGridLayout()

        self.buttons = [
            "+", "-", ".",
            "/", "*", "=",
            "1", "2", "3",
            "4", "5", "6",
            "7", "8", "9",
            "C", "0", "<"
        ]

        positions = [(i // 3, i % 3) for i in range(len(self.buttons))]
        for pos, text in zip(positions, self.buttons):
            button = QPushButton(text)
            button.setFixedSize(80, 50)
            layout.addWidget(button, pos[0], pos[1])
            button.clicked.connect(lambda _, t=text: self.on_button_click(t))

        main_layout.addLayout(layout)
        self.setLayout(main_layout)

    def on_button_click(self, text):
        if text == "C":
            self.display.clear()
        elif text == "<":
            current = self.display.text()
            self.display.setText(current[:-1])
        elif text == "=":
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except Exception:
                self.display.setText("Hata")
        else:
            self.display.setText(self.display.text() + text)

    def keyPressEvent(self, event):
        key = event.key()


        if key == Qt.Key.Key_Backspace:
            self.on_button_click("<")
            event.accept()

        elif key == Qt.Key.Key_Return or key == Qt.Key.Key_Enter:
            self.on_button_click("=")
            event.accept()

        elif key in [Qt.Key.Key_0, Qt.Key.Key_1, Qt.Key.Key_2, Qt.Key.Key_3,
                      Qt.Key.Key_4, Qt.Key.Key_5, Qt.Key.Key_6, Qt.Key.Key_7,
                      Qt.Key.Key_8, Qt.Key.Key_9, Qt.Key.Key_Plus,
                      Qt.Key.Key_Minus, Qt.Key.Key_Period,
                      Qt.Key.Key_Slash, Qt.Key.Key_Asterisk]:
            self.on_button_click(event.text())
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec())
