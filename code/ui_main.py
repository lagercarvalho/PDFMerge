import sys, os
from pathlib import Path
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem, QPushButton, QFileDialog, QAbstractItemView, QSizePolicy
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QIcon
#import comtypes

class ListboxWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setGeometry(20, 70, 400, 400)
        self.supportedTypes = (".pdf", ".pptx", ".odp",".doc",".docx",".odt")
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()

            links = []

            for url in event.mimeData().urls():
                if url.isLocalFile():
                    urlName = str(url.toLocalFile())
                    if (urlName.endswith(self.supportedTypes)):
                        links.append(urlName)
                else:
                    urlName = str(url.toString())
                    if (urlName.endswith(self.supportedTypes)):
                        links.append(urlName)
            self.addItems(links)
        else:
            event.ignore()


class Button(QPushButton):
    def __init__(self, name = "None", parent=None):
        super().__init__(name, parent)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

class Label(QtWidgets.QLabel):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)


class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(1200, 300, 700, 500)
        self.setWindowTitle("Pdf Merger")
        self.setWindowIcon(QIcon("img/pdf_icon.png"))

        self.label = Label(self)
        self.label.setText("Add the files to convert and merge:")
        self.label.setGeometry(20, 20, 200, 20)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.lstView = ListboxWidget(self)

        self.upBtn = Button("Up", self)
        self.upBtn.setGeometry(430, 85, 50, 50)
        self.upBtn.clicked.connect(self.moveUp)

        self.downBtn = Button("Down", self)
        self.downBtn.setGeometry(430, 405, 50, 50)
        self.downBtn.clicked.connect(self.moveDown)

        self.mergeBtn = Button("Merge", self)
        self.mergeBtn.setGeometry(500, 305, 150, 50)
        self.mergeBtn.clicked.connect(self.merge)

        self.browseBtn = Button("Browse", self)
        self.browseBtn.setGeometry(500, 205, 150, 50)
        self.browseBtn.clicked.connect(self.searchFile)
        
        self.show()

    def merge(self):
        for item in self.lstView.items():
            #todo continue working on the merge function
            break

    def searchFile(self):
        permissions = "PDF files (*.pdf);;Powerpoint files (*.pptx, *.odp);;Word documents(*.doc,*.docx,*odt)"
        fileName = QFileDialog.getOpenFileName(self, 'Open File', os.environ['HOMEPATH'], permissions)
        print(fileName)
        if fileName:
            self.lstView.addItem(fileName[0])

    def move(self, dir):
        currentRow = self.currentRow()
        currentItem = self.takeItem(currentRow)
        self.insertItem(currentRow + dir, currentItem)

    def moveUp(self):
        self.move(self, -1)

    def moveDown(self):
        self.move(self, 1)


def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(Path('style.qss').read_text())

    win = AppWindow()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()