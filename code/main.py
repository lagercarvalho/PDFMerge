import sys, os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem, QPushButton, QFileDialog
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QIcon
import comtypes


class ListboxWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setGeometry(20, 70, 400, 400)
        self.supportedTypes = (".pdf", ".pptx", ".odp",".doc",".docx",".odt")

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

            self.addItems(links)
        else:
            event.ignore()



class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(1200, 300, 700, 500)
        self.setWindowTitle("Pdf Merger")
        self.setWindowIcon(QIcon("img/pdf_icon.png"))

        self.label = QtWidgets.QLabel(self)
        self.label.setText("Add the files to convert and merge:")
        self.label.setGeometry(20, 20, 200, 20)

        self.lstView = ListboxWidget(self)

        self.mergeBtn = QPushButton("Merge", self)
        self.mergeBtn.setGeometry(485, 375, 150, 50)
        self.mergeBtn.clicked.connect(self.merge)

        self.browseBtn = QPushButton("Browse", self)
        self.browseBtn.setGeometry(485, 275, 150, 50)
        self.browseBtn.clicked.connect(self.searchFile)

    def merge(self):
        for item in self.lstView.items():
            #todo continue working on the merge function


    def searchFile(self):
        permissions = "PDF files (*.pdf);;Powerpoint files (*.pptx, *.odp);;Word documents(*.doc,*.docx,*odt)"
        fileName = QFileDialog.getOpenFileName(self, 'Open File', os.environ['HOMEPATH'], permissions)
        if not fileName:
            self.lstView.addItems(fileName[0])


def window():
    app = QApplication(sys.argv)

    win = AppWindow()
    win.show()

    sys.exit(app.exec_())

window()