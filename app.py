from PySide6.QtWidgets import QApplication
from model.standard import Standard


if __name__ == "__main__":
    app = QApplication()  
    w = Standard()
    w.show()

    app.exec()  