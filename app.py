from PySide6.QtWidgets import QApplication
# from model.standard import Standard
from model.scientific import Scientific


if __name__ == "__main__":
    app = QApplication()  
    w = Scientific()
    w.show()

    app.exec()   