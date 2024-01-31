import sys
import os
from QtPy import QtWidgets as Qt
from QtPy import QtWidgets
from QtPy.QtWidgets import (
    QApplication, QHBoxLayout, QLineEdit, QLabel, QTextEdit, QPushButton, QFileSystemModel, QListView
)
from QtPy import QtCore
from PyQt5.QtGui import QDrag
from PyQt5.QtCore import QMimeData

class Window(Qt.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.label = Qt.QLabel('Drop files', self)
        self.label.setGeometry(QtCore.QRect(0, 50, 500, 100))
        self.label.setTextFormat(Qt.RichText)
        self.label.setDragEnterMode(Qt.DragOnly)

        self.model = QFileSystemModel()
        self.tableView = QListView()
        self.tableView.setModel(self.model)

        # Qt: For 'drag and drop'
        self.tableView.viewport().
        self.tableView.setAcceptDrops(True)
        self.tableView.setDragEnabled(True)
        self.tableView.setDragDropMode(Qt.DragOnly)

        # setting up valid data
        mimetypes = ['text/uri-list']
        self.tableView.setMimeTypes(mimetypes)

        print('initUI done')

        # adding the Event Handlers

        # def dragEnterEvent(self, ev):
        #    ev.accept()

        self.tableView.dragEnterEvent = self.dragEnterEvent
        self.tableView.setAcceptDrops(True)

        self.tableView.dragMoveEvent = self.dragMoveEvent

        self.tableView.dropEvent =self.dropEvent

        self.tableView.show()

        self.show()

    def dragEnterEvent(self, ev):
        print("[EVENT] dragEnterEvent")

    def dragMoveEvent(self, ev):
        print("[EVENT] dragMoveEvent")

    def dropEvent(self, ev):
        print("[EVENT] dropEvent")

        # Here, find the file path.
        mimeData = ev.mimeData()
        urls_str = mimeData.text()

        urls = [urlstr.toLocalFile() for urlstr in urls_str.split()]
        for _url in urls:
            print("PATH: " + _url)

def main():
    app =Qt.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
