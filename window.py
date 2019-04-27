# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(904, 720)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 481, 241))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.mouseCaptureRegion = QtWidgets.QGroupBox(self.gridLayoutWidget)
        self.mouseCaptureRegion.setEnabled(True)
        self.mouseCaptureRegion.setTitle("")
        self.mouseCaptureRegion.setObjectName("mouseCaptureRegion")
        self.progressBar = QtWidgets.QProgressBar(self.mouseCaptureRegion)
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QtCore.QRect(10, 131, 461, 20))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.hashCombo = QtWidgets.QComboBox(self.mouseCaptureRegion)
        self.hashCombo.setGeometry(QtCore.QRect(10, 210, 101, 21))
        self.hashCombo.setAutoFillBackground(False)
        self.hashCombo.setMaxVisibleItems(5)
        self.hashCombo.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.hashCombo.setObjectName("hashCombo")
        self.hashCombo.addItem("")
        self.hashCombo.addItem("")
        self.hashInput = QtWidgets.QLineEdit(self.mouseCaptureRegion)
        self.hashInput.setGeometry(QtCore.QRect(10, 160, 461, 41))
        self.hashInput.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.hashInput.setInputMask("")
        self.hashInput.setText("")
        self.hashInput.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.hashInput.setDragEnabled(True)
        self.hashInput.setClearButtonEnabled(False)
        self.hashInput.setObjectName("hashInput")
        self.loadFileButton = QtWidgets.QPushButton(self.mouseCaptureRegion)
        self.loadFileButton.setGeometry(QtCore.QRect(120, 210, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.loadFileButton.setFont(font)
        self.loadFileButton.setObjectName("loadFileButton")
        self.randomKeyButton = QtWidgets.QPushButton(self.mouseCaptureRegion)
        self.randomKeyButton.setGeometry(QtCore.QRect(230, 210, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.randomKeyButton.setFont(font)
        self.randomKeyButton.setObjectName("randomKeyButton")
        self.hashButton = QtWidgets.QPushButton(self.mouseCaptureRegion)
        self.hashButton.setGeometry(QtCore.QRect(370, 210, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.hashButton.setFont(font)
        self.hashButton.setObjectName("hashButton")
        self.gridLayout.addWidget(self.mouseCaptureRegion, 0, 1, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(500, 0, 391, 251))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.sineTable = QtWidgets.QTableWidget(self.groupBox)
        self.sineTable.setGeometry(QtCore.QRect(200, 50, 181, 191))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sineTable.sizePolicy().hasHeightForWidth())
        self.sineTable.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.sineTable.setFont(font)
        self.sineTable.setToolTip("")
        self.sineTable.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sineTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.sineTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.sineTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.sineTable.setTabKeyNavigation(False)
        self.sineTable.setObjectName("sineTable")
        self.sineTable.setColumnCount(0)
        self.sineTable.setRowCount(0)
        self.sineTable.horizontalHeader().setVisible(False)
        self.sineTable.horizontalHeader().setStretchLastSection(True)
        self.sineTable.verticalHeader().setVisible(False)
        self.label_16 = QtWidgets.QLabel(self.groupBox)
        self.label_16.setGeometry(QtCore.QRect(10, 50, 61, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.groupBox)
        self.label_17.setGeometry(QtCore.QRect(10, 70, 61, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.groupBox)
        self.label_18.setGeometry(QtCore.QRect(10, 110, 61, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.groupBox)
        self.label_19.setGeometry(QtCore.QRect(10, 90, 61, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.regAText = QtWidgets.QLineEdit(self.groupBox)
        self.regAText.setGeometry(QtCore.QRect(70, 50, 121, 20))
        self.regAText.setReadOnly(True)
        self.regAText.setObjectName("regAText")
        self.regBText = QtWidgets.QLineEdit(self.groupBox)
        self.regBText.setGeometry(QtCore.QRect(70, 70, 121, 20))
        self.regBText.setReadOnly(True)
        self.regBText.setObjectName("regBText")
        self.regCText = QtWidgets.QLineEdit(self.groupBox)
        self.regCText.setGeometry(QtCore.QRect(70, 90, 121, 20))
        self.regCText.setReadOnly(True)
        self.regCText.setObjectName("regCText")
        self.regDText = QtWidgets.QLineEdit(self.groupBox)
        self.regDText.setGeometry(QtCore.QRect(70, 110, 121, 20))
        self.regDText.setReadOnly(True)
        self.regDText.setObjectName("regDText")
        self.regEText = QtWidgets.QLineEdit(self.groupBox)
        self.regEText.setGeometry(QtCore.QRect(70, 130, 121, 20))
        self.regEText.setReadOnly(True)
        self.regEText.setObjectName("regEText")
        self.label_21 = QtWidgets.QLabel(self.groupBox)
        self.label_21.setGeometry(QtCore.QRect(10, 130, 61, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.tableLabel = QtWidgets.QLabel(self.groupBox)
        self.tableLabel.setGeometry(QtCore.QRect(230, 30, 131, 17))
        self.tableLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.tableLabel.setObjectName("tableLabel")
        self.digestSizeLabel = QtWidgets.QLabel(self.groupBox)
        self.digestSizeLabel.setGeometry(QtCore.QRect(10, 160, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.digestSizeLabel.setFont(font)
        self.digestSizeLabel.setObjectName("digestSizeLabel")
        self.blockSizeLabel = QtWidgets.QLabel(self.groupBox)
        self.blockSizeLabel.setGeometry(QtCore.QRect(10, 180, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.blockSizeLabel.setFont(font)
        self.blockSizeLabel.setObjectName("blockSizeLabel")
        self.blockSizeLabel_2 = QtWidgets.QLabel(self.groupBox)
        self.blockSizeLabel_2.setGeometry(QtCore.QRect(10, 200, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.blockSizeLabel_2.setFont(font)
        self.blockSizeLabel_2.setObjectName("blockSizeLabel_2")
        self.digestSizeLabel_2 = QtWidgets.QLabel(self.groupBox)
        self.digestSizeLabel_2.setGeometry(QtCore.QRect(120, 160, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.digestSizeLabel_2.setFont(font)
        self.digestSizeLabel_2.setObjectName("digestSizeLabel_2")
        self.digestSizeLabel_3 = QtWidgets.QLabel(self.groupBox)
        self.digestSizeLabel_3.setGeometry(QtCore.QRect(120, 180, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.digestSizeLabel_3.setFont(font)
        self.digestSizeLabel_3.setObjectName("digestSizeLabel_3")
        self.digestSizeLabel_4 = QtWidgets.QLabel(self.groupBox)
        self.digestSizeLabel_4.setGeometry(QtCore.QRect(120, 200, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.digestSizeLabel_4.setFont(font)
        self.digestSizeLabel_4.setObjectName("digestSizeLabel_4")
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 250, 881, 431))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.verticalLayoutWidget)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_20 = QtWidgets.QLabel(self.tab_2)
        self.label_20.setGeometry(QtCore.QRect(140, 60, 581, 71))
        self.label_20.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_20.setWordWrap(True)
        self.label_20.setObjectName("label_20")
        self.padding_BlockText = QtWidgets.QTextEdit(self.tab_2)
        self.padding_BlockText.setGeometry(QtCore.QRect(100, 140, 641, 141))
        self.padding_BlockText.setReadOnly(True)
        self.padding_BlockText.setObjectName("padding_BlockText")
        self.padding_LeftArrow = QtWidgets.QToolButton(self.tab_2)
        self.padding_LeftArrow.setGeometry(QtCore.QRect(280, 300, 22, 17))
        self.padding_LeftArrow.setArrowType(QtCore.Qt.LeftArrow)
        self.padding_LeftArrow.setObjectName("padding_LeftArrow")
        self.padding_RightArrow = QtWidgets.QToolButton(self.tab_2)
        self.padding_RightArrow.setGeometry(QtCore.QRect(570, 300, 22, 17))
        self.padding_RightArrow.setArrowType(QtCore.Qt.RightArrow)
        self.padding_RightArrow.setObjectName("padding_RightArrow")
        self.paddingStatusLabel = QtWidgets.QLabel(self.tab_2)
        self.paddingStatusLabel.setGeometry(QtCore.QRect(310, 300, 251, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.paddingStatusLabel.sizePolicy().hasHeightForWidth())
        self.paddingStatusLabel.setSizePolicy(sizePolicy)
        self.paddingStatusLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.paddingStatusLabel.setWordWrap(True)
        self.paddingStatusLabel.setObjectName("paddingStatusLabel")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setGeometry(QtCore.QRect(0, 0, 831, 271))
        self.widget.setObjectName("widget")
        self.exportButton = QtWidgets.QPushButton(self.tab)
        self.exportButton.setGeometry(QtCore.QRect(380, 340, 71, 20))
        self.exportButton.setObjectName("exportButton")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(490, 100, 221, 91))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_13 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.fBufferVal = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.fBufferVal.setFont(font)
        self.fBufferVal.setReadOnly(True)
        self.fBufferVal.setObjectName("fBufferVal")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.fBufferVal)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.gBufferVal = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.gBufferVal.setFont(font)
        self.gBufferVal.setReadOnly(True)
        self.gBufferVal.setObjectName("gBufferVal")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.gBufferVal)
        self.loopCountLabel = QtWidgets.QLabel(self.layoutWidget)
        self.loopCountLabel.setObjectName("loopCountLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.loopCountLabel)
        self.progressSlider = QtWidgets.QSlider(self.tab)
        self.progressSlider.setEnabled(False)
        self.progressSlider.setGeometry(QtCore.QRect(218, 270, 471, 16))
        self.progressSlider.setMinimum(1)
        self.progressSlider.setMaximum(5)
        self.progressSlider.setProperty("value", 1)
        self.progressSlider.setOrientation(QtCore.Qt.Horizontal)
        self.progressSlider.setObjectName("progressSlider")
        self.workingWordText = QtWidgets.QLineEdit(self.tab)
        self.workingWordText.setGeometry(QtCore.QRect(30, 40, 771, 51))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.workingWordText.setFont(font)
        self.workingWordText.setAlignment(QtCore.Qt.AlignCenter)
        self.workingWordText.setReadOnly(True)
        self.workingWordText.setClearButtonEnabled(False)
        self.workingWordText.setObjectName("workingWordText")
        self.loopCountLabel_2 = QtWidgets.QLabel(self.tab)
        self.loopCountLabel_2.setGeometry(QtCore.QRect(30, 20, 201, 16))
        self.loopCountLabel_2.setObjectName("loopCountLabel_2")
        self.layoutWidget1 = QtWidgets.QWidget(self.tab)
        self.layoutWidget1.setGeometry(QtCore.QRect(160, 100, 311, 146))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget1)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.aBufferVal = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.aBufferVal.setFont(font)
        self.aBufferVal.setReadOnly(True)
        self.aBufferVal.setObjectName("aBufferVal")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.aBufferVal)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.bBufferVal = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.bBufferVal.setFont(font)
        self.bBufferVal.setReadOnly(True)
        self.bBufferVal.setObjectName("bBufferVal")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.bBufferVal)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.cBufferVal = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.cBufferVal.setFont(font)
        self.cBufferVal.setReadOnly(True)
        self.cBufferVal.setObjectName("cBufferVal")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.cBufferVal)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.dBufferVal = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.dBufferVal.setFont(font)
        self.dBufferVal.setReadOnly(True)
        self.dBufferVal.setObjectName("dBufferVal")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.dBufferVal)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_15.setObjectName("label_15")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.eBufferVal = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.eBufferVal.setFont(font)
        self.eBufferVal.setReadOnly(True)
        self.eBufferVal.setObjectName("eBufferVal")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.eBufferVal)
        self.outputText = QtWidgets.QLineEdit(self.tab)
        self.outputText.setGeometry(QtCore.QRect(228, 290, 451, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.outputText.setFont(font)
        self.outputText.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.outputText.setAutoFillBackground(False)
        self.outputText.setAlignment(QtCore.Qt.AlignCenter)
        self.outputText.setReadOnly(True)
        self.outputText.setObjectName("outputText")
        self.launchVisualiserError = QtWidgets.QLabel(self.tab)
        self.launchVisualiserError.setGeometry(QtCore.QRect(240, 370, 401, 21))
        self.launchVisualiserError.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.launchVisualiserError.setAlignment(QtCore.Qt.AlignCenter)
        self.launchVisualiserError.setObjectName("launchVisualiserError")
        self.launchVisualiserButton = QtWidgets.QPushButton(self.tab)
        self.launchVisualiserButton.setGeometry(QtCore.QRect(470, 340, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.launchVisualiserButton.setFont(font)
        self.launchVisualiserButton.setObjectName("launchVisualiserButton")
        self.tabWidget.addTab(self.tab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 904, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionConverter_Tool = QtWidgets.QAction(MainWindow)
        self.actionConverter_Tool.setObjectName("actionConverter_Tool")
        self.actionKill_Children = QtWidgets.QAction(MainWindow)
        self.actionKill_Children.setObjectName("actionKill_Children")
        self.menuFile.addAction(self.actionConverter_Tool)
        self.menuFile.addAction(self.actionKill_Children)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.hashCombo.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.hashCombo.setItemText(0, _translate("MainWindow", "MD5"))
        self.hashCombo.setItemText(1, _translate("MainWindow", "SHA-1"))
        self.hashInput.setPlaceholderText(_translate("MainWindow", "Enter Input to be Hashed"))
        self.loadFileButton.setText(_translate("MainWindow", "Load File"))
        self.randomKeyButton.setText(_translate("MainWindow", "Generate Random Key"))
        self.hashButton.setText(_translate("MainWindow", "Hash Message"))
        self.groupBox.setTitle(_translate("MainWindow", "Hash Preview"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#83ac60;\">Buffer A</span></p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#58b4e2;\">Buffer B</span></p></body></html>"))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#dbaa2f;\">Buffer D</span></p></body></html>"))
        self.label_19.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff1111;\">Buffer C</span></p></body></html>"))
        self.label_21.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#834187;\">Buffer E</span></p></body></html>"))
        self.tableLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; text-decoration: underline;\">Constants</span></p></body></html>"))
        self.digestSizeLabel.setText(_translate("MainWindow", "Digest Size:"))
        self.blockSizeLabel.setText(_translate("MainWindow", "Block Size:"))
        self.blockSizeLabel_2.setText(_translate("MainWindow", "Rounds:"))
        self.digestSizeLabel_2.setText(_translate("MainWindow", "0"))
        self.digestSizeLabel_3.setText(_translate("MainWindow", "0"))
        self.digestSizeLabel_4.setText(_translate("MainWindow", "0"))
        self.label_20.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Merkle Damgard construction is a method for building collision resistant functions and involves various steps to preparing raw data for the main loop. Use the arrow keys to navigate between steps.</span></p></body></html>"))
        self.padding_LeftArrow.setText(_translate("MainWindow", "..."))
        self.padding_RightArrow.setText(_translate("MainWindow", "..."))
        self.paddingStatusLabel.setText(_translate("MainWindow", "Binary of Input"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Padding"))
        self.exportButton.setText(_translate("MainWindow", "Export"))
        self.label_13.setText(_translate("MainWindow", "F"))
        self.label_14.setText(_translate("MainWindow", "g"))
        self.loopCountLabel.setText(_translate("MainWindow", "Loop Count : "))
        self.loopCountLabel_2.setText(_translate("MainWindow", "Current Operational Block"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#83ac60;\">Buffer A</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#58b4e2;\">Buffer B</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff1111;\">Buffer C</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#dbaa2f;\">Buffer D</span></p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#834187;\">Buffer E</span></p></body></html>"))
        self.launchVisualiserError.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#aa0000;\">Visualiser is not currently supported on your system</span></p></body></html>"))
        self.launchVisualiserButton.setText(_translate("MainWindow", "Visualise this section"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Main Loop"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionConverter_Tool.setText(_translate("MainWindow", "Converter Tool"))
        self.actionKill_Children.setText(_translate("MainWindow", "Close Other Windows"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

