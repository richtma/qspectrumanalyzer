# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qspectrumanalyzer/qspectrumanalyzer.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_QSpectrumAnalyzerMainWindow(object):
    def setupUi(self, QSpectrumAnalyzerMainWindow):
        QSpectrumAnalyzerMainWindow.setObjectName(_fromUtf8("QSpectrumAnalyzerMainWindow"))
        QSpectrumAnalyzerMainWindow.resize(1200, 810)
        self.centralwidget = QtGui.QWidget(QSpectrumAnalyzerMainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.plotSplitter = QtGui.QSplitter(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotSplitter.sizePolicy().hasHeightForWidth())
        self.plotSplitter.setSizePolicy(sizePolicy)
        self.plotSplitter.setOrientation(QtCore.Qt.Vertical)
        self.plotSplitter.setObjectName(_fromUtf8("plotSplitter"))
        self.mainPlotLayout = GraphicsLayoutWidget(self.plotSplitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPlotLayout.sizePolicy().hasHeightForWidth())
        self.mainPlotLayout.setSizePolicy(sizePolicy)
        self.mainPlotLayout.setObjectName(_fromUtf8("mainPlotLayout"))
        self.waterfallPlotLayout = GraphicsLayoutWidget(self.plotSplitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.waterfallPlotLayout.sizePolicy().hasHeightForWidth())
        self.waterfallPlotLayout.setSizePolicy(sizePolicy)
        self.waterfallPlotLayout.setObjectName(_fromUtf8("waterfallPlotLayout"))
        self.horizontalLayout.addWidget(self.plotSplitter)
        QSpectrumAnalyzerMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(QSpectrumAnalyzerMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 30))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName(_fromUtf8("menu_File"))
        self.menu_Help = QtGui.QMenu(self.menubar)
        self.menu_Help.setObjectName(_fromUtf8("menu_Help"))
        QSpectrumAnalyzerMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(QSpectrumAnalyzerMainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        QSpectrumAnalyzerMainWindow.setStatusBar(self.statusbar)
        self.controlsDockWidget = QtGui.QDockWidget(QSpectrumAnalyzerMainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.controlsDockWidget.sizePolicy().hasHeightForWidth())
        self.controlsDockWidget.setSizePolicy(sizePolicy)
        self.controlsDockWidget.setMinimumSize(QtCore.QSize(10, 10))
        self.controlsDockWidget.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        self.controlsDockWidget.setObjectName(_fromUtf8("controlsDockWidget"))
        self.controlsDockWidgetContents = QtGui.QWidget()
        self.controlsDockWidgetContents.setObjectName(_fromUtf8("controlsDockWidgetContents"))
        self.gridLayout_2 = QtGui.QGridLayout(self.controlsDockWidgetContents)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.startButton = QtGui.QPushButton(self.controlsDockWidgetContents)
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.gridLayout_2.addWidget(self.startButton, 0, 0, 1, 1)
        self.stopButton = QtGui.QPushButton(self.controlsDockWidgetContents)
        self.stopButton.setObjectName(_fromUtf8("stopButton"))
        self.gridLayout_2.addWidget(self.stopButton, 0, 1, 1, 1)
        self.singleShotButton = QtGui.QPushButton(self.controlsDockWidgetContents)
        self.singleShotButton.setObjectName(_fromUtf8("singleShotButton"))
        self.gridLayout_2.addWidget(self.singleShotButton, 1, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(20, 561, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 2, 0, 1, 1)
        self.controlsDockWidget.setWidget(self.controlsDockWidgetContents)
        QSpectrumAnalyzerMainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.controlsDockWidget)
        self.frequencyDockWidget = QtGui.QDockWidget(QSpectrumAnalyzerMainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frequencyDockWidget.sizePolicy().hasHeightForWidth())
        self.frequencyDockWidget.setSizePolicy(sizePolicy)
        self.frequencyDockWidget.setMinimumSize(QtCore.QSize(10, 10))
        self.frequencyDockWidget.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        self.frequencyDockWidget.setObjectName(_fromUtf8("frequencyDockWidget"))
        self.frequencyDockWidgetContents = QtGui.QWidget()
        self.frequencyDockWidgetContents.setObjectName(_fromUtf8("frequencyDockWidgetContents"))
        self.formLayout = QtGui.QFormLayout(self.frequencyDockWidgetContents)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_2 = QtGui.QLabel(self.frequencyDockWidgetContents)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.startFreqSpinBox = QtGui.QDoubleSpinBox(self.frequencyDockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startFreqSpinBox.sizePolicy().hasHeightForWidth())
        self.startFreqSpinBox.setSizePolicy(sizePolicy)
        self.startFreqSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.startFreqSpinBox.setDecimals(3)
        self.startFreqSpinBox.setMinimum(24.0)
        self.startFreqSpinBox.setMaximum(1766.0)
        self.startFreqSpinBox.setProperty("value", 87.0)
        self.startFreqSpinBox.setObjectName(_fromUtf8("startFreqSpinBox"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.startFreqSpinBox)
        self.label_3 = QtGui.QLabel(self.frequencyDockWidgetContents)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.stopFreqSpinBox = QtGui.QDoubleSpinBox(self.frequencyDockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopFreqSpinBox.sizePolicy().hasHeightForWidth())
        self.stopFreqSpinBox.setSizePolicy(sizePolicy)
        self.stopFreqSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.stopFreqSpinBox.setDecimals(3)
        self.stopFreqSpinBox.setMinimum(24.0)
        self.stopFreqSpinBox.setMaximum(1766.0)
        self.stopFreqSpinBox.setProperty("value", 108.0)
        self.stopFreqSpinBox.setObjectName(_fromUtf8("stopFreqSpinBox"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.stopFreqSpinBox)
        self.label = QtGui.QLabel(self.frequencyDockWidgetContents)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label)
        self.binSizeSpinBox = QtGui.QDoubleSpinBox(self.frequencyDockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.binSizeSpinBox.sizePolicy().hasHeightForWidth())
        self.binSizeSpinBox.setSizePolicy(sizePolicy)
        self.binSizeSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.binSizeSpinBox.setDecimals(3)
        self.binSizeSpinBox.setMaximum(2800.0)
        self.binSizeSpinBox.setProperty("value", 10.0)
        self.binSizeSpinBox.setObjectName(_fromUtf8("binSizeSpinBox"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.binSizeSpinBox)
        spacerItem1 = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(3, QtGui.QFormLayout.SpanningRole, spacerItem1)
        self.frequencyDockWidget.setWidget(self.frequencyDockWidgetContents)
        QSpectrumAnalyzerMainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.frequencyDockWidget)
        self.settingsDockWidget = QtGui.QDockWidget(QSpectrumAnalyzerMainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settingsDockWidget.sizePolicy().hasHeightForWidth())
        self.settingsDockWidget.setSizePolicy(sizePolicy)
        self.settingsDockWidget.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        self.settingsDockWidget.setObjectName(_fromUtf8("settingsDockWidget"))
        self.settingsDockWidgetContents = QtGui.QWidget()
        self.settingsDockWidgetContents.setObjectName(_fromUtf8("settingsDockWidgetContents"))
        self.gridLayout = QtGui.QGridLayout(self.settingsDockWidgetContents)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_4 = QtGui.QLabel(self.settingsDockWidgetContents)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.settingsDockWidgetContents)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 0, 1, 1, 1)
        self.intervalSpinBox = QtGui.QDoubleSpinBox(self.settingsDockWidgetContents)
        self.intervalSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.intervalSpinBox.setMaximum(999.0)
        self.intervalSpinBox.setProperty("value", 1.0)
        self.intervalSpinBox.setObjectName(_fromUtf8("intervalSpinBox"))
        self.gridLayout.addWidget(self.intervalSpinBox, 1, 0, 1, 1)
        self.gainSpinBox = QtGui.QSpinBox(self.settingsDockWidgetContents)
        self.gainSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.gainSpinBox.setMinimum(-1)
        self.gainSpinBox.setMaximum(49)
        self.gainSpinBox.setProperty("value", -1)
        self.gainSpinBox.setObjectName(_fromUtf8("gainSpinBox"))
        self.gridLayout.addWidget(self.gainSpinBox, 1, 1, 1, 2)
        self.label_5 = QtGui.QLabel(self.settingsDockWidgetContents)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.settingsDockWidgetContents)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 2, 1, 1, 1)
        self.ppmSpinBox = QtGui.QSpinBox(self.settingsDockWidgetContents)
        self.ppmSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ppmSpinBox.setMinimum(-999)
        self.ppmSpinBox.setMaximum(999)
        self.ppmSpinBox.setObjectName(_fromUtf8("ppmSpinBox"))
        self.gridLayout.addWidget(self.ppmSpinBox, 3, 0, 1, 1)
        self.mainCurveCheckBox = QtGui.QCheckBox(self.settingsDockWidgetContents)
        self.mainCurveCheckBox.setChecked(True)
        self.mainCurveCheckBox.setObjectName(_fromUtf8("mainCurveCheckBox"))
        self.gridLayout.addWidget(self.mainCurveCheckBox, 4, 0, 1, 1)
        self.colorsButton = QtGui.QPushButton(self.settingsDockWidgetContents)
        self.colorsButton.setObjectName(_fromUtf8("colorsButton"))
        self.gridLayout.addWidget(self.colorsButton, 4, 1, 1, 2)
        self.peakHoldMaxCheckBox = QtGui.QCheckBox(self.settingsDockWidgetContents)
        self.peakHoldMaxCheckBox.setObjectName(_fromUtf8("peakHoldMaxCheckBox"))
        self.gridLayout.addWidget(self.peakHoldMaxCheckBox, 5, 0, 1, 1)
        self.peakHoldMinCheckBox = QtGui.QCheckBox(self.settingsDockWidgetContents)
        self.peakHoldMinCheckBox.setObjectName(_fromUtf8("peakHoldMinCheckBox"))
        self.gridLayout.addWidget(self.peakHoldMinCheckBox, 5, 1, 1, 2)
        self.averageCheckBox = QtGui.QCheckBox(self.settingsDockWidgetContents)
        self.averageCheckBox.setObjectName(_fromUtf8("averageCheckBox"))
        self.gridLayout.addWidget(self.averageCheckBox, 6, 0, 1, 1)
        self.smoothCheckBox = QtGui.QCheckBox(self.settingsDockWidgetContents)
        self.smoothCheckBox.setObjectName(_fromUtf8("smoothCheckBox"))
        self.gridLayout.addWidget(self.smoothCheckBox, 7, 0, 1, 1)
        self.smoothButton = QtGui.QToolButton(self.settingsDockWidgetContents)
        self.smoothButton.setAutoRaise(False)
        self.smoothButton.setObjectName(_fromUtf8("smoothButton"))
        self.gridLayout.addWidget(self.smoothButton, 7, 2, 1, 1)
        self.persistenceCheckBox = QtGui.QCheckBox(self.settingsDockWidgetContents)
        self.persistenceCheckBox.setObjectName(_fromUtf8("persistenceCheckBox"))
        self.gridLayout.addWidget(self.persistenceCheckBox, 8, 0, 1, 1)
        self.persistenceButton = QtGui.QToolButton(self.settingsDockWidgetContents)
        self.persistenceButton.setAutoRaise(False)
        self.persistenceButton.setObjectName(_fromUtf8("persistenceButton"))
        self.gridLayout.addWidget(self.persistenceButton, 8, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 1, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 9, 0, 1, 1)
        self.cropSpinBox = QtGui.QSpinBox(self.settingsDockWidgetContents)
        self.cropSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.cropSpinBox.setObjectName(_fromUtf8("cropSpinBox"))
        self.gridLayout.addWidget(self.cropSpinBox, 3, 1, 1, 2)
        self.settingsDockWidget.setWidget(self.settingsDockWidgetContents)
        QSpectrumAnalyzerMainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.settingsDockWidget)
        self.levelsDockWidget = QtGui.QDockWidget(QSpectrumAnalyzerMainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.levelsDockWidget.sizePolicy().hasHeightForWidth())
        self.levelsDockWidget.setSizePolicy(sizePolicy)
        self.levelsDockWidget.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        self.levelsDockWidget.setObjectName(_fromUtf8("levelsDockWidget"))
        self.levelsDockWidgetContents = QtGui.QWidget()
        self.levelsDockWidgetContents.setObjectName(_fromUtf8("levelsDockWidgetContents"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.levelsDockWidgetContents)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.histogramPlotLayout = GraphicsLayoutWidget(self.levelsDockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.histogramPlotLayout.sizePolicy().hasHeightForWidth())
        self.histogramPlotLayout.setSizePolicy(sizePolicy)
        self.histogramPlotLayout.setObjectName(_fromUtf8("histogramPlotLayout"))
        self.verticalLayout_6.addWidget(self.histogramPlotLayout)
        self.levelsDockWidget.setWidget(self.levelsDockWidgetContents)
        QSpectrumAnalyzerMainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.levelsDockWidget)
        self.action_Settings = QtGui.QAction(QSpectrumAnalyzerMainWindow)
        self.action_Settings.setObjectName(_fromUtf8("action_Settings"))
        self.action_Quit = QtGui.QAction(QSpectrumAnalyzerMainWindow)
        self.action_Quit.setObjectName(_fromUtf8("action_Quit"))
        self.action_About = QtGui.QAction(QSpectrumAnalyzerMainWindow)
        self.action_About.setObjectName(_fromUtf8("action_About"))
        self.menu_File.addAction(self.action_Settings)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Quit)
        self.menu_Help.addAction(self.action_About)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.label_2.setBuddy(self.startFreqSpinBox)
        self.label_3.setBuddy(self.stopFreqSpinBox)
        self.label.setBuddy(self.binSizeSpinBox)
        self.label_4.setBuddy(self.intervalSpinBox)
        self.label_6.setBuddy(self.gainSpinBox)
        self.label_5.setBuddy(self.ppmSpinBox)
        self.label_7.setBuddy(self.cropSpinBox)

        self.retranslateUi(QSpectrumAnalyzerMainWindow)
        QtCore.QMetaObject.connectSlotsByName(QSpectrumAnalyzerMainWindow)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.startButton, self.stopButton)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.stopButton, self.singleShotButton)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.singleShotButton, self.startFreqSpinBox)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.startFreqSpinBox, self.stopFreqSpinBox)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.stopFreqSpinBox, self.binSizeSpinBox)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.binSizeSpinBox, self.intervalSpinBox)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.intervalSpinBox, self.gainSpinBox)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.gainSpinBox, self.ppmSpinBox)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.ppmSpinBox, self.cropSpinBox)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.cropSpinBox, self.mainCurveCheckBox)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.mainCurveCheckBox, self.colorsButton)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.colorsButton, self.peakHoldMaxCheckBox)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.peakHoldMaxCheckBox, self.peakHoldMinCheckBox)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.peakHoldMinCheckBox, self.averageCheckBox)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.averageCheckBox, self.smoothCheckBox)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.smoothCheckBox, self.smoothButton)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.smoothButton, self.persistenceCheckBox)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.persistenceCheckBox, self.persistenceButton)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.persistenceButton, self.histogramPlotLayout)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.histogramPlotLayout, self.mainPlotLayout)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.mainPlotLayout, self.waterfallPlotLayout)

    def retranslateUi(self, QSpectrumAnalyzerMainWindow):
        QSpectrumAnalyzerMainWindow.setWindowTitle(_translate("QSpectrumAnalyzerMainWindow", "QSpectrumAnalyzer", None))
        self.menu_File.setTitle(_translate("QSpectrumAnalyzerMainWindow", "&File", None))
        self.menu_Help.setTitle(_translate("QSpectrumAnalyzerMainWindow", "&Help", None))
        self.controlsDockWidget.setWindowTitle(_translate("QSpectrumAnalyzerMainWindow", "Controls", None))
        self.startButton.setText(_translate("QSpectrumAnalyzerMainWindow", "&Start", None))
        self.stopButton.setText(_translate("QSpectrumAnalyzerMainWindow", "S&top", None))
        self.singleShotButton.setText(_translate("QSpectrumAnalyzerMainWindow", "Si&ngle shot", None))
        self.frequencyDockWidget.setWindowTitle(_translate("QSpectrumAnalyzerMainWindow", "Frequency", None))
        self.label_2.setText(_translate("QSpectrumAnalyzerMainWindow", "Start:", None))
        self.startFreqSpinBox.setSuffix(_translate("QSpectrumAnalyzerMainWindow", " MHz", None))
        self.label_3.setText(_translate("QSpectrumAnalyzerMainWindow", "Stop:", None))
        self.stopFreqSpinBox.setSuffix(_translate("QSpectrumAnalyzerMainWindow", " MHz", None))
        self.label.setText(_translate("QSpectrumAnalyzerMainWindow", "Bin size:", None))
        self.binSizeSpinBox.setSuffix(_translate("QSpectrumAnalyzerMainWindow", " kHz", None))
        self.settingsDockWidget.setWindowTitle(_translate("QSpectrumAnalyzerMainWindow", "Settings", None))
        self.label_4.setText(_translate("QSpectrumAnalyzerMainWindow", "Interval [s]:", None))
        self.label_6.setText(_translate("QSpectrumAnalyzerMainWindow", "Gain [dB]:", None))
        self.gainSpinBox.setSpecialValueText(_translate("QSpectrumAnalyzerMainWindow", "auto", None))
        self.label_5.setText(_translate("QSpectrumAnalyzerMainWindow", "Corr. [ppm]:", None))
        self.label_7.setText(_translate("QSpectrumAnalyzerMainWindow", "Crop [%]:", None))
        self.mainCurveCheckBox.setText(_translate("QSpectrumAnalyzerMainWindow", "Main curve", None))
        self.colorsButton.setText(_translate("QSpectrumAnalyzerMainWindow", "Colors...", None))
        self.peakHoldMaxCheckBox.setText(_translate("QSpectrumAnalyzerMainWindow", "Max. hold", None))
        self.peakHoldMinCheckBox.setText(_translate("QSpectrumAnalyzerMainWindow", "Min. hold", None))
        self.averageCheckBox.setText(_translate("QSpectrumAnalyzerMainWindow", "Average", None))
        self.smoothCheckBox.setText(_translate("QSpectrumAnalyzerMainWindow", "Smoothing", None))
        self.smoothButton.setText(_translate("QSpectrumAnalyzerMainWindow", "...", None))
        self.persistenceCheckBox.setText(_translate("QSpectrumAnalyzerMainWindow", "Persistence", None))
        self.persistenceButton.setText(_translate("QSpectrumAnalyzerMainWindow", "...", None))
        self.levelsDockWidget.setWindowTitle(_translate("QSpectrumAnalyzerMainWindow", "Levels", None))
        self.action_Settings.setText(_translate("QSpectrumAnalyzerMainWindow", "&Settings...", None))
        self.action_Quit.setText(_translate("QSpectrumAnalyzerMainWindow", "&Quit", None))
        self.action_Quit.setShortcut(_translate("QSpectrumAnalyzerMainWindow", "Ctrl+Q", None))
        self.action_About.setText(_translate("QSpectrumAnalyzerMainWindow", "&About", None))

from pyqtgraph import GraphicsLayoutWidget