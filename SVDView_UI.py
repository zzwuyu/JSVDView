# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\微处理器\JSVDView\SVDView.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SVDView(object):
    def setupUi(self, SVDView):
        SVDView.setObjectName("SVDView")
        SVDView.resize(720, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SVDView.sizePolicy().hasHeightForWidth())
        SVDView.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Image/serial.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SVDView.setWindowIcon(icon)
        self.vLayout0 = QtWidgets.QVBoxLayout(SVDView)
        self.vLayout0.setObjectName("vLayout0")
        self.hLayout1 = QtWidgets.QHBoxLayout()
        self.hLayout1.setObjectName("hLayout1")
        self.lblDLL = QtWidgets.QLabel(SVDView)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblDLL.sizePolicy().hasHeightForWidth())
        self.lblDLL.setSizePolicy(sizePolicy)
        self.lblDLL.setObjectName("lblDLL")
        self.hLayout1.addWidget(self.lblDLL)
        self.linDLL = QtWidgets.QLineEdit(SVDView)
        self.linDLL.setObjectName("linDLL")
        self.hLayout1.addWidget(self.linDLL)
        self.btnDLL = QtWidgets.QPushButton(SVDView)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDLL.sizePolicy().hasHeightForWidth())
        self.btnDLL.setSizePolicy(sizePolicy)
        self.btnDLL.setObjectName("btnDLL")
        self.hLayout1.addWidget(self.btnDLL)
        self.vLayout0.addLayout(self.hLayout1)
        self.hLayout2 = QtWidgets.QHBoxLayout()
        self.hLayout2.setObjectName("hLayout2")
        self.lblSVD = QtWidgets.QLabel(SVDView)
        self.lblSVD.setObjectName("lblSVD")
        self.hLayout2.addWidget(self.lblSVD)
        self.cmbSVD = QtWidgets.QComboBox(SVDView)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbSVD.sizePolicy().hasHeightForWidth())
        self.cmbSVD.setSizePolicy(sizePolicy)
        self.cmbSVD.setObjectName("cmbSVD")
        self.hLayout2.addWidget(self.cmbSVD)
        self.btnSVD = QtWidgets.QPushButton(SVDView)
        self.btnSVD.setObjectName("btnSVD")
        self.hLayout2.addWidget(self.btnSVD)
        self.vLayout0.addLayout(self.hLayout2)
        self.hLayout3 = QtWidgets.QHBoxLayout()
        self.hLayout3.setObjectName("hLayout3")
        self.lblPeriph = QtWidgets.QLabel(SVDView)
        self.lblPeriph.setObjectName("lblPeriph")
        self.hLayout3.addWidget(self.lblPeriph)
        self.cmbPeriph = QtWidgets.QComboBox(SVDView)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbPeriph.sizePolicy().hasHeightForWidth())
        self.cmbPeriph.setSizePolicy(sizePolicy)
        self.cmbPeriph.setMinimumSize(QtCore.QSize(180, 0))
        self.cmbPeriph.setObjectName("cmbPeriph")
        self.hLayout3.addWidget(self.cmbPeriph)
        self.linPeriph = QtWidgets.QLabel(SVDView)
        self.linPeriph.setText("")
        self.linPeriph.setObjectName("linPeriph")
        self.hLayout3.addWidget(self.linPeriph)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hLayout3.addItem(spacerItem)
        self.btnRefresh = QtWidgets.QPushButton(SVDView)
        self.btnRefresh.setObjectName("btnRefresh")
        self.hLayout3.addWidget(self.btnRefresh)
        self.vLayout0.addLayout(self.hLayout3)
        self.tree = QtWidgets.QTreeWidget(SVDView)
        self.tree.setColumnCount(4)
        self.tree.setObjectName("tree")
        self.tree.headerItem().setText(0, "名称")
        self.tree.headerItem().setText(1, "偏移")
        self.tree.headerItem().setText(2, "值")
        self.tree.headerItem().setText(3, "描述")
        self.tree.header().setVisible(True)
        self.vLayout0.addWidget(self.tree)

        self.retranslateUi(SVDView)
        QtCore.QMetaObject.connectSlotsByName(SVDView)

    def retranslateUi(self, SVDView):
        _translate = QtCore.QCoreApplication.translate
        SVDView.setWindowTitle(_translate("SVDView", "XIVN1987 SVD Viewer"))
        self.lblDLL.setText(_translate("SVDView", "JLinkARM.dll："))
        self.btnDLL.setText(_translate("SVDView", "..."))
        self.lblSVD.setText(_translate("SVDView", "SVD 文件路径："))
        self.btnSVD.setText(_translate("SVDView", "..."))
        self.lblPeriph.setText(_translate("SVDView", "MCU 外设列表："))
        self.btnRefresh.setText(_translate("SVDView", "刷新"))

