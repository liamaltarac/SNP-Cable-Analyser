from PyQt5 import QtGui, QtCore
from app.node import Node

class TreeModel(QtGui.QStandardItemModel):
    def __init__(self, parent = None):
        super(TreeModel, self).__init__()
        self.setHorizontalHeaderLabels(["name"])

    # def index(self, row, column, parent):
    #     if not self.hasIndex(row, column, parent):
    #         return QtCore.QModelIndex()

    #     if not parent.isValid():
    #         parentItem = self.rootItem
    #     else:
    #         parentItem = parent.internalPointer()

    #     childItem = parentItem.child(row)
    #     if childItem:
    #         return self.createIndex(row, column, childItem)
    #     else:
    #         return QtCore.QModelIndex()

    # def parent(self, index):
    #     if not index.isValid():
    #         return QtCore.QModelIndex()

    #     childItem = index.internalPointer()
    #     parentItem = childItem.parent

    #     if parentItem == self.rootItem:
    #         return QtCore.QModelIndex()

    #     return self.createIndex(parentItem.row(), 0, parentItem)

    # def rowCount(self, parent):
    #     if parent.column() > 0:
    #         return 0
    #     if not parent.isValid():
    #         parentItem = self.rootItem
    #     else:
    #         parentItem = parent.internalPointer()

    #     return parentItem.childCount()

    # def columnCount(self, parent):
    #     if parent.isValid():
    #         return parent.internalPointer().columnCount()
    #     else:
    #         return self.rootItem.columnCount()

    # def data(self, index, role):
    #     if not index.isValid():
    #         return None

    #     if role != QtCore.Qt.DisplayRole:
    #         return None

    #     item = index.internalPointer()
    #     return item.data(index.column())

    # def headerData(self, section, orientation, role):
    #     if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
    #         return self._header[section]

    #     return None

    def getRootFromIndex(self, index):
        item = index
        while self.parent(item) != QtCore.QModelIndex():
            item = self.parent(item)
        return item

    # def deleteItems(self, indexes):
    #     for index in indexes:
    #         item = index.internalPointer()
    #         item.parent.removeChild(item)