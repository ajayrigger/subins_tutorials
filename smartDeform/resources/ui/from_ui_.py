# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/venture/subins_tutorials/smartDeform/resources/ui/from_ui.ui'
#
# Created: Sun Dec  9 20:26:50 2018
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(604, 758)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.toolBox = QtGui.QToolBox(self.centralwidget)
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.page = QtGui.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 586, 626))
        self.page.setObjectName(_fromUtf8("page"))
        self.verticalLayout = QtGui.QVBoxLayout(self.page)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox_from = QtGui.QGroupBox(self.page)
        self.groupBox_from.setObjectName(_fromUtf8("groupBox_from"))
        self.gridLayout_from = QtGui.QGridLayout(self.groupBox_from)
        self.gridLayout_from.setSpacing(10)
        self.gridLayout_from.setContentsMargins(30, 10, 20, 10)
        self.gridLayout_from.setObjectName(_fromUtf8("gridLayout_from"))
        self.radioButton_softSelection = QtGui.QRadioButton(self.groupBox_from)
        self.radioButton_softSelection.setObjectName(_fromUtf8("radioButton_softSelection"))
        self.gridLayout_from.addWidget(self.radioButton_softSelection, 0, 0, 1, 1)
        self.radioButton_blendshape = QtGui.QRadioButton(self.groupBox_from)
        self.radioButton_blendshape.setObjectName(_fromUtf8("radioButton_blendshape"))
        self.gridLayout_from.addWidget(self.radioButton_blendshape, 0, 1, 1, 1)
        self.radioButton_wire = QtGui.QRadioButton(self.groupBox_from)
        self.radioButton_wire.setObjectName(_fromUtf8("radioButton_wire"))
        self.gridLayout_from.addWidget(self.radioButton_wire, 0, 2, 1, 1)
        self.radioButton_lattice = QtGui.QRadioButton(self.groupBox_from)
        self.radioButton_lattice.setObjectName(_fromUtf8("radioButton_lattice"))
        self.gridLayout_from.addWidget(self.radioButton_lattice, 1, 0, 1, 1)
        self.radioButton_cluster = QtGui.QRadioButton(self.groupBox_from)
        self.radioButton_cluster.setObjectName(_fromUtf8("radioButton_cluster"))
        self.gridLayout_from.addWidget(self.radioButton_cluster, 1, 1, 1, 1)
        self.radioButton_skincluster = QtGui.QRadioButton(self.groupBox_from)
        self.radioButton_skincluster.setObjectName(_fromUtf8("radioButton_skincluster"))
        self.gridLayout_from.addWidget(self.radioButton_skincluster, 1, 2, 1, 1)
        self.radioButton_from = QtGui.QRadioButton(self.groupBox_from)
        self.radioButton_from.setObjectName(_fromUtf8("radioButton_from"))
        self.gridLayout_from.addWidget(self.radioButton_from, 0, 3, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_from)
        self.groupBox_to = QtGui.QGroupBox(self.page)
        self.groupBox_to.setObjectName(_fromUtf8("groupBox_to"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_to)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setContentsMargins(30, 10, 10, 10)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.radioButton_clusterTo = QtGui.QRadioButton(self.groupBox_to)
        self.radioButton_clusterTo.setObjectName(_fromUtf8("radioButton_clusterTo"))
        self.horizontalLayout_2.addWidget(self.radioButton_clusterTo)
        self.radioButton_skinclusterTo = QtGui.QRadioButton(self.groupBox_to)
        self.radioButton_skinclusterTo.setObjectName(_fromUtf8("radioButton_skinclusterTo"))
        self.horizontalLayout_2.addWidget(self.radioButton_skinclusterTo)
        self.radioButton_deformTo = QtGui.QRadioButton(self.groupBox_to)
        self.radioButton_deformTo.setObjectName(_fromUtf8("radioButton_deformTo"))
        self.horizontalLayout_2.addWidget(self.radioButton_deformTo)
        self.radioButton_to = QtGui.QRadioButton(self.groupBox_to)
        self.radioButton_to.setObjectName(_fromUtf8("radioButton_to"))
        self.horizontalLayout_2.addWidget(self.radioButton_to)
        self.verticalLayout.addWidget(self.groupBox_to)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setMargin(2)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.groupBox_source = QtGui.QGroupBox(self.page)
        self.groupBox_source.setObjectName(_fromUtf8("groupBox_source"))
        self.verticalLayout_source = QtGui.QVBoxLayout(self.groupBox_source)
        self.verticalLayout_source.setSpacing(5)
        self.verticalLayout_source.setMargin(5)
        self.verticalLayout_source.setObjectName(_fromUtf8("verticalLayout_source"))
        self.horizontalLayout_source = QtGui.QHBoxLayout()
        self.horizontalLayout_source.setSpacing(1)
        self.horizontalLayout_source.setObjectName(_fromUtf8("horizontalLayout_source"))
        self.lineEdit_source = QtGui.QLineEdit(self.groupBox_source)
        self.lineEdit_source.setEnabled(True)
        self.lineEdit_source.setObjectName(_fromUtf8("lineEdit_source"))
        self.horizontalLayout_source.addWidget(self.lineEdit_source)
        self.button_source = QtGui.QPushButton(self.groupBox_source)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_source.sizePolicy().hasHeightForWidth())
        self.button_source.setSizePolicy(sizePolicy)
        self.button_source.setMinimumSize(QtCore.QSize(20, 20))
        self.button_source.setMaximumSize(QtCore.QSize(16777215, 20))
        self.button_source.setText(_fromUtf8(""))
        self.button_source.setObjectName(_fromUtf8("button_source"))
        self.horizontalLayout_source.addWidget(self.button_source)
        self.verticalLayout_source.addLayout(self.horizontalLayout_source)
        self.comboBox = QtGui.QComboBox(self.groupBox_source)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/wire.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon, _fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.verticalLayout_source.addWidget(self.comboBox)
        self.listWidget_source = QtGui.QListWidget(self.groupBox_source)
        self.listWidget_source.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget_source.setObjectName(_fromUtf8("listWidget_source"))
        self.verticalLayout_source.addWidget(self.listWidget_source)
        self.horizontalLayout_4.addWidget(self.groupBox_source)
        self.groupBox_target = QtGui.QGroupBox(self.page)
        self.groupBox_target.setObjectName(_fromUtf8("groupBox_target"))
        self.verticalLayout_target = QtGui.QVBoxLayout(self.groupBox_target)
        self.verticalLayout_target.setSpacing(5)
        self.verticalLayout_target.setMargin(5)
        self.verticalLayout_target.setObjectName(_fromUtf8("verticalLayout_target"))
        self.horizontalLayout_target = QtGui.QHBoxLayout()
        self.horizontalLayout_target.setSpacing(1)
        self.horizontalLayout_target.setObjectName(_fromUtf8("horizontalLayout_target"))
        self.lineEdit_target = QtGui.QLineEdit(self.groupBox_target)
        self.lineEdit_target.setEnabled(True)
        self.lineEdit_target.setObjectName(_fromUtf8("lineEdit_target"))
        self.horizontalLayout_target.addWidget(self.lineEdit_target)
        self.button_target = QtGui.QPushButton(self.groupBox_target)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_target.sizePolicy().hasHeightForWidth())
        self.button_target.setSizePolicy(sizePolicy)
        self.button_target.setMinimumSize(QtCore.QSize(20, 20))
        self.button_target.setMaximumSize(QtCore.QSize(16777215, 20))
        self.button_target.setText(_fromUtf8(""))
        self.button_target.setObjectName(_fromUtf8("button_target"))
        self.horizontalLayout_target.addWidget(self.button_target)
        self.verticalLayout_target.addLayout(self.horizontalLayout_target)
        self.listWidget_target = QtGui.QListWidget(self.groupBox_target)
        self.listWidget_target.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget_target.setObjectName(_fromUtf8("listWidget_target"))
        self.verticalLayout_target.addWidget(self.listWidget_target)
        self.horizontalLayout_4.addWidget(self.groupBox_target)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.toolBox.addItem(self.page, _fromUtf8(""))
        self.page_2 = QtGui.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 586, 626))
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.page_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox_mirror = QtGui.QGroupBox(self.page_2)
        self.groupBox_mirror.setObjectName(_fromUtf8("groupBox_mirror"))
        self.horizontalLayout_mirror = QtGui.QHBoxLayout(self.groupBox_mirror)
        self.horizontalLayout_mirror.setSpacing(0)
        self.horizontalLayout_mirror.setContentsMargins(-1, 0, 0, 0)
        self.horizontalLayout_mirror.setObjectName(_fromUtf8("horizontalLayout_mirror"))
        self.radioButton_clusterX = QtGui.QRadioButton(self.groupBox_mirror)
        self.radioButton_clusterX.setMinimumSize(QtCore.QSize(0, 10))
        self.radioButton_clusterX.setObjectName(_fromUtf8("radioButton_clusterX"))
        self.horizontalLayout_mirror.addWidget(self.radioButton_clusterX)
        self.radioButton_clusterY = QtGui.QRadioButton(self.groupBox_mirror)
        self.radioButton_clusterY.setObjectName(_fromUtf8("radioButton_clusterY"))
        self.horizontalLayout_mirror.addWidget(self.radioButton_clusterY)
        self.radioButton_clusterZ = QtGui.QRadioButton(self.groupBox_mirror)
        self.radioButton_clusterZ.setObjectName(_fromUtf8("radioButton_clusterZ"))
        self.horizontalLayout_mirror.addWidget(self.radioButton_clusterZ)
        self.button_clusterMirror = QtGui.QPushButton(self.groupBox_mirror)
        self.button_clusterMirror.setObjectName(_fromUtf8("button_clusterMirror"))
        self.horizontalLayout_mirror.addWidget(self.button_clusterMirror)
        self.verticalLayout_2.addWidget(self.groupBox_mirror)
        self.horizontalLayout_cluster = QtGui.QHBoxLayout()
        self.horizontalLayout_cluster.setSpacing(0)
        self.horizontalLayout_cluster.setObjectName(_fromUtf8("horizontalLayout_cluster"))
        self.button_combineCluster = QtGui.QPushButton(self.page_2)
        self.button_combineCluster.setObjectName(_fromUtf8("button_combineCluster"))
        self.horizontalLayout_cluster.addWidget(self.button_combineCluster)
        self.button_copyWeight = QtGui.QPushButton(self.page_2)
        self.button_copyWeight.setObjectName(_fromUtf8("button_copyWeight"))
        self.horizontalLayout_cluster.addWidget(self.button_copyWeight)
        self.verticalLayout_2.addLayout(self.horizontalLayout_cluster)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.toolBox.addItem(self.page_2, _fromUtf8(""))
        self.page_3 = QtGui.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 586, 626))
        self.page_3.setObjectName(_fromUtf8("page_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.page_3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.groupBox_clusterOption = QtGui.QGroupBox(self.page_3)
        self.groupBox_clusterOption.setObjectName(_fromUtf8("groupBox_clusterOption"))
        self.verticalLayout_clusterOption = QtGui.QVBoxLayout(self.groupBox_clusterOption)
        self.verticalLayout_clusterOption.setObjectName(_fromUtf8("verticalLayout_clusterOption"))
        self.horizontalLayout_clusterOption = QtGui.QHBoxLayout()
        self.horizontalLayout_clusterOption.setSpacing(0)
        self.horizontalLayout_clusterOption.setObjectName(_fromUtf8("horizontalLayout_clusterOption"))
        self.button_exportCluster = QtGui.QPushButton(self.groupBox_clusterOption)
        self.button_exportCluster.setObjectName(_fromUtf8("button_exportCluster"))
        self.horizontalLayout_clusterOption.addWidget(self.button_exportCluster)
        self.button_importCluster = QtGui.QPushButton(self.groupBox_clusterOption)
        self.button_importCluster.setObjectName(_fromUtf8("button_importCluster"))
        self.horizontalLayout_clusterOption.addWidget(self.button_importCluster)
        self.verticalLayout_clusterOption.addLayout(self.horizontalLayout_clusterOption)
        self.listWidget_clusterWeight = QtGui.QListWidget(self.groupBox_clusterOption)
        self.listWidget_clusterWeight.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget_clusterWeight.setObjectName(_fromUtf8("listWidget_clusterWeight"))
        self.verticalLayout_clusterOption.addWidget(self.listWidget_clusterWeight)
        self.verticalLayout_3.addWidget(self.groupBox_clusterOption)
        self.toolBox.addItem(self.page_3, _fromUtf8(""))
        self.verticalLayout_4.addWidget(self.toolBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 604, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox_from.setTitle(_translate("MainWindow", "From", None))
        self.radioButton_softSelection.setText(_translate("MainWindow", "Soft Selection", None))
        self.radioButton_blendshape.setText(_translate("MainWindow", "Blendshape", None))
        self.radioButton_wire.setText(_translate("MainWindow", "Wire", None))
        self.radioButton_lattice.setText(_translate("MainWindow", "Lattice", None))
        self.radioButton_cluster.setText(_translate("MainWindow", "Cluster", None))
        self.radioButton_skincluster.setText(_translate("MainWindow", "Skincluster", None))
        self.radioButton_from.setText(_translate("MainWindow", "From", None))
        self.groupBox_to.setTitle(_translate("MainWindow", "To", None))
        self.radioButton_clusterTo.setText(_translate("MainWindow", "Cluster", None))
        self.radioButton_skinclusterTo.setText(_translate("MainWindow", "Skincluster", None))
        self.radioButton_deformTo.setText(_translate("MainWindow", "Deform", None))
        self.radioButton_to.setText(_translate("MainWindow", "To", None))
        self.groupBox_source.setTitle(_translate("MainWindow", "Source Mesh", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "Subin", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "Gopi", None))
        self.groupBox_target.setTitle(_translate("MainWindow", "Target Mesh", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "Subin", None))
        self.radioButton_clusterX.setText(_translate("MainWindow", "X", None))
        self.radioButton_clusterY.setText(_translate("MainWindow", "Y", None))
        self.radioButton_clusterZ.setText(_translate("MainWindow", "Z", None))
        self.button_clusterMirror.setText(_translate("MainWindow", "Mirror", None))
        self.button_combineCluster.setText(_translate("MainWindow", "Combine Cluster", None))
        self.button_copyWeight.setText(_translate("MainWindow", "Copy Weight", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "Page 2", None))
        self.groupBox_clusterOption.setTitle(_translate("MainWindow", "Cluster Options", None))
        self.button_exportCluster.setText(_translate("MainWindow", "Export Cluster", None))
        self.button_importCluster.setText(_translate("MainWindow", "Import Cluster", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("MainWindow", "Page", None))

import test_rc
