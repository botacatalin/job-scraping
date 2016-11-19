# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'details.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Details(object):
    def setupUi(self, Details):
        Details.setObjectName("Details")
        Details.resize(480, 530)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Details.sizePolicy().hasHeightForWidth())
        Details.setSizePolicy(sizePolicy)
        Details.setMaximumSize(QtCore.QSize(480, 530))
        Details.setModal(True)
        self.label0 = QtWidgets.QLabel(Details)
        self.label0.setGeometry(QtCore.QRect(10, 10, 59, 16))
        self.label0.setObjectName("label0")
        self.find_similar_jobs = QtWidgets.QToolButton(Details)
        self.find_similar_jobs.setGeometry(QtCore.QRect(20, 100, 221, 22))
        self.find_similar_jobs.setObjectName("find_similar_jobs")
        self.details_result_list = QtWidgets.QListWidget(Details)
        self.details_result_list.setGeometry(QtCore.QRect(20, 271, 441, 221))
        self.details_result_list.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.details_result_list.setObjectName("details_result_list")
        self.layoutWidget = QtWidgets.QWidget(Details)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 40, 441, 46))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.company_selected_lbl = QtWidgets.QLabel(self.layoutWidget)
        self.company_selected_lbl.setFrameShape(QtWidgets.QFrame.Panel)
        self.company_selected_lbl.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.company_selected_lbl.setObjectName("company_selected_lbl")
        self.verticalLayout.addWidget(self.company_selected_lbl)
        self.job_selected_lbl = QtWidgets.QLabel(self.layoutWidget)
        self.job_selected_lbl.setFrameShape(QtWidgets.QFrame.Panel)
        self.job_selected_lbl.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.job_selected_lbl.setObjectName("job_selected_lbl")
        self.verticalLayout.addWidget(self.job_selected_lbl)
        self.open_in_browser2 = QtWidgets.QPushButton(Details)
        self.open_in_browser2.setGeometry(QtCore.QRect(322, 490, 141, 32))
        self.open_in_browser2.setObjectName("open_in_browser2")

        self.retranslateUi(Details)
        QtCore.QMetaObject.connectSlotsByName(Details)

    def retranslateUi(self, Details):
        _translate = QtCore.QCoreApplication.translate
        Details.setWindowTitle(_translate("Details", "Details"))
        self.label0.setText(_translate("Details", "Statistics:"))
        self.find_similar_jobs.setText(_translate("Details", "Find companies with similar jobs"))
        self.company_selected_lbl.setText(_translate("Details", "..."))
        self.job_selected_lbl.setText(_translate("Details", "..."))
        self.open_in_browser2.setText(_translate("Details", "Open in browser"))

