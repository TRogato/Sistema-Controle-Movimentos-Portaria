# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmPesquisarNotasFiscais.ui'
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

class Ui_frmConsultarNotasFiscais(object):
    def setupUi(self, frmConsultarNotasFiscais):
        frmConsultarNotasFiscais.setObjectName(_fromUtf8("frmConsultarNotasFiscais"))
        frmConsultarNotasFiscais.resize(793, 606)
        frmConsultarNotasFiscais.setMinimumSize(QtCore.QSize(793, 606))
        frmConsultarNotasFiscais.setMaximumSize(QtCore.QSize(793, 606))
        font = QtGui.QFont()
        font.setPointSize(11)
        frmConsultarNotasFiscais.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/folder_saved_search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmConsultarNotasFiscais.setWindowIcon(icon)
        frmConsultarNotasFiscais.setSizeGripEnabled(False)
        frmConsultarNotasFiscais.setModal(True)

        self.grbTipoPesquisa = QtGui.QGroupBox(frmConsultarNotasFiscais)
        self.grbTipoPesquisa.setGeometry(QtCore.QRect(10, 10, 341, 141))
        self.grbTipoPesquisa.setObjectName(_fromUtf8("grbTipoPesquisa"))

        self.radBtnFantasiaEmitente = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnFantasiaEmitente.setGeometry(QtCore.QRect(10, 55, 131, 23))
        self.radBtnFantasiaEmitente.setObjectName(_fromUtf8("radBtnFantasiaEmitente"))

        self.radBtnRazaoSocialEmitente = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnRazaoSocialEmitente.setGeometry(QtCore.QRect(10, 75, 161, 23))
        self.radBtnRazaoSocialEmitente.setObjectName(_fromUtf8("radBtnRazaoSocialEmitente"))

        self.radBtnCnpjEmitente = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnCnpjEmitente.setGeometry(QtCore.QRect(10, 95, 111, 23))
        self.radBtnCnpjEmitente.setObjectName(_fromUtf8("radBtnCnpjEmitente"))

        self.radBtnIncrisaoEstadualEmitente = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnIncrisaoEstadualEmitente.setGeometry(QtCore.QRect(10, 115, 161, 23))
        self.radBtnIncrisaoEstadualEmitente.setObjectName(_fromUtf8("radBtnIncrisaoEstadualEmitente"))

        self.radBtnNumNotaFiscal = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnNumNotaFiscal.setGeometry(QtCore.QRect(10, 15, 111, 23))
        self.radBtnNumNotaFiscal.setObjectName(_fromUtf8("radBtnNumNotaFiscal"))

        self.radBtnRomaneio = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnRomaneio.setGeometry(QtCore.QRect(10, 35, 111, 23))
        self.radBtnRomaneio.setObjectName(_fromUtf8("radBtnRomaneio"))

        self.radBtnRazaoSocialDestinatario = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnRazaoSocialDestinatario.setGeometry(QtCore.QRect(180, 34, 151, 23))
        self.radBtnRazaoSocialDestinatario.setObjectName(_fromUtf8("radBtnRazaoSocialDestinatario"))

        self.radBtnCnpjDestinatario = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnCnpjDestinatario.setGeometry(QtCore.QRect(180, 54, 101, 23))
        self.radBtnCnpjDestinatario.setObjectName(_fromUtf8("radBtnCnpjDestinatario"))

        self.radBtnFantasiaDestinatario = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnFantasiaDestinatario.setGeometry(QtCore.QRect(180, 14, 121, 23))
        self.radBtnFantasiaDestinatario.setObjectName(_fromUtf8("radBtnFantasiaDestinatario"))

        self.radBtnIncrisaoEstadualDestinatario = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnIncrisaoEstadualDestinatario.setGeometry(QtCore.QRect(180, 74, 151, 23))
        self.radBtnIncrisaoEstadualDestinatario.setObjectName(_fromUtf8("radBtnIncrisaoEstadualDestinatario"))

        self.radBtnDataLanamento = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnDataLanamento.setGeometry(QtCore.QRect(180, 95, 141, 23))
        self.radBtnDataLanamento.setObjectName(_fromUtf8("radBtnDataLanamento"))

        self.radBtnDataPeriodos = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnDataPeriodos.setGeometry(QtCore.QRect(180, 115, 111, 23))
        self.radBtnDataPeriodos.setObjectName(_fromUtf8("radBtnDataPeriodos"))

        self.txtPesquisar = QtGui.QLineEdit(frmConsultarNotasFiscais)
        self.txtPesquisar.setEnabled(False)
        self.txtPesquisar.setGeometry(QtCore.QRect(360, 120, 381, 25))
        self.txtPesquisar.setObjectName(_fromUtf8("txtPesquisar"))

        self.lblPesquisar = QtGui.QLabel(frmConsultarNotasFiscais)
        self.lblPesquisar.setGeometry(QtCore.QRect(360, 100, 71, 19))
        self.lblPesquisar.setObjectName(_fromUtf8("lblPesquisar"))

        self.btnPesquisar = QtGui.QPushButton(frmConsultarNotasFiscais)
        self.btnPesquisar.setEnabled(False)
        self.btnPesquisar.setGeometry(QtCore.QRect(750, 120, 31, 27))
        self.btnPesquisar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnPesquisar.setText(_fromUtf8(""))
        self.btnPesquisar.setObjectName(_fromUtf8("btnPesquisar"))

        self.tabPesquisar = QtGui.QTableWidget(frmConsultarNotasFiscais)
        self.tabPesquisar.setGeometry(QtCore.QRect(10, 160, 771, 381))
        self.tabPesquisar.horizontalHeader().setStretchLastSection(True)
        self.tabPesquisar.verticalHeader().setVisible(False)
        self.tabPesquisar.setColumnCount(22)
        self.tabPesquisar.setHorizontalHeaderLabels(['COD.', 'Num Nota Fiscal', 'Data', 'Valor Total', 'COD.', 'Desti. Fantasia', 'Desti. Razao Socil', 'Desti. CNPJ', 'Desti. Ins. Estadual', 'COD.', 'Empr. Fantasia', 'Empr. Razao Socil', 'Empr. CNPJ', 'Empr. Ins. Estadual', 'COD.', 'Nome Motorista', 'RG', 'CPF', 'COD.', 'Num. Romaneio', 'Certificada', 'Metragem'])
        self.tabPesquisar.setEditTriggers(self.tabPesquisar.NoEditTriggers)
        self.tabPesquisar.setSelectionBehavior(self.tabPesquisar.SelectRows)
        self.tabPesquisar.setSelectionMode(self.tabPesquisar.SingleSelection)
        self.tabPesquisar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tabPesquisar.setObjectName(_fromUtf8("tabPesquisar"))


        self.btnImprimir = QtGui.QPushButton(frmConsultarNotasFiscais)
        self.btnImprimir.setGeometry(QtCore.QRect(730, 550, 51, 51))
        self.btnImprimir.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnImprimir.setText(_fromUtf8(""))
        self.btnImprimir.setObjectName(_fromUtf8("btnImprimir"))

        self.btnLimpar = QtGui.QPushButton(frmConsultarNotasFiscais)
        self.btnLimpar.setGeometry(QtCore.QRect(670, 550, 51, 51))
        self.btnLimpar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnLimpar.setText(_fromUtf8(""))
        self.btnLimpar.setObjectName(_fromUtf8("btnLimpar"))

        self.txtDataInicial = QtGui.QDateEdit(frmConsultarNotasFiscais)
        self.txtDataInicial.setEnabled(False)
        self.txtDataInicial.setGeometry(QtCore.QRect(430, 10, 110, 25))
        self.txtDataInicial.setCalendarPopup(True)
        self.txtDataInicial.setObjectName(_fromUtf8("txtDataInicial"))

        self.txtDataFinal = QtGui.QDateEdit(frmConsultarNotasFiscais)
        self.txtDataFinal.setEnabled(False)
        self.txtDataFinal.setGeometry(QtCore.QRect(430, 60, 110, 25))
        self.txtDataFinal.setCalendarPopup(True)
        self.txtDataFinal.setObjectName(_fromUtf8("txtDataFinal"))

        self.lblDataInicio = QtGui.QLabel(frmConsultarNotasFiscais)
        self.lblDataInicio.setGeometry(QtCore.QRect(360, 13, 66, 19))
        self.lblDataInicio.setObjectName(_fromUtf8("lblDataInicio"))

        self.lblDataFinal = QtGui.QLabel(frmConsultarNotasFiscais)
        self.lblDataFinal.setGeometry(QtCore.QRect(360, 63, 66, 19))
        self.lblDataFinal.setObjectName(_fromUtf8("lblDataFinal"))

        self.lblPesquisar.setBuddy(self.txtPesquisar)
        self.lblDataInicio.setBuddy(self.txtDataInicial)
        self.lblDataFinal.setBuddy(self.txtDataFinal)

        self.retranslateUi(frmConsultarNotasFiscais)
        QtCore.QMetaObject.connectSlotsByName(frmConsultarNotasFiscais)
        frmConsultarNotasFiscais.setTabOrder(self.radBtnNumNotaFiscal, self.radBtnRomaneio)
        frmConsultarNotasFiscais.setTabOrder(self.radBtnRomaneio, self.radBtnFantasiaEmitente)
        frmConsultarNotasFiscais.setTabOrder(self.radBtnFantasiaEmitente, self.radBtnRazaoSocialEmitente)
        frmConsultarNotasFiscais.setTabOrder(self.radBtnRazaoSocialEmitente, self.radBtnCnpjEmitente)
        frmConsultarNotasFiscais.setTabOrder(self.radBtnCnpjEmitente, self.radBtnIncrisaoEstadualEmitente)
        frmConsultarNotasFiscais.setTabOrder(self.radBtnIncrisaoEstadualEmitente, self.radBtnFantasiaDestinatario)
        frmConsultarNotasFiscais.setTabOrder(self.radBtnFantasiaDestinatario, self.radBtnRazaoSocialDestinatario)
        frmConsultarNotasFiscais.setTabOrder(self.radBtnRazaoSocialDestinatario, self.radBtnCnpjDestinatario)
        frmConsultarNotasFiscais.setTabOrder(self.radBtnCnpjDestinatario, self.radBtnIncrisaoEstadualDestinatario)
        frmConsultarNotasFiscais.setTabOrder(self.radBtnIncrisaoEstadualDestinatario, self.radBtnDataLanamento)
        frmConsultarNotasFiscais.setTabOrder(self.radBtnDataLanamento, self.radBtnDataPeriodos)
        frmConsultarNotasFiscais.setTabOrder(self.radBtnDataPeriodos, self.txtPesquisar)
        frmConsultarNotasFiscais.setTabOrder(self.txtPesquisar, self.txtDataInicial)
        frmConsultarNotasFiscais.setTabOrder(self.txtDataInicial, self.txtDataFinal)

    def retranslateUi(self, frmConsultarNotasFiscais):
        frmConsultarNotasFiscais.setWindowTitle(_translate("frmConsultarNotasFiscais", "Consultar Notas Fiscal / Romaneios", None))
        self.grbTipoPesquisa.setTitle(_translate("frmConsultarNotasFiscais", "Tipo Pesquisa", None))
        self.radBtnFantasiaEmitente.setToolTip(_translate("frmConsultarNotasFiscais", "Fantasia", None))
        self.radBtnFantasiaEmitente.setText(_translate("frmConsultarNotasFiscais", "Fantasia Emiten.", None))
        self.radBtnRazaoSocialEmitente.setToolTip(_translate("frmConsultarNotasFiscais", "Razão Social", None))
        self.radBtnRazaoSocialEmitente.setText(_translate("frmConsultarNotasFiscais", "Razão Social Emiten.", None))
        self.radBtnCnpjEmitente.setToolTip(_translate("frmConsultarNotasFiscais", "CNPJ", None))
        self.radBtnCnpjEmitente.setText(_translate("frmConsultarNotasFiscais", "CNPJ Emiten.", None))
        self.radBtnIncrisaoEstadualEmitente.setToolTip(_translate("frmConsultarNotasFiscais", "Inscrição Estadual", None))
        self.radBtnIncrisaoEstadualEmitente.setText(_translate("frmConsultarNotasFiscais", "Inscr. Estad. Emiten.", None))
        self.radBtnNumNotaFiscal.setToolTip(_translate("frmConsultarNotasFiscais", "Fantasia", None))
        self.radBtnNumNotaFiscal.setText(_translate("frmConsultarNotasFiscais", "Nº Nota Fiscal", None))
        self.radBtnRomaneio.setToolTip(_translate("frmConsultarNotasFiscais", "Fantasia", None))
        self.radBtnRomaneio.setText(_translate("frmConsultarNotasFiscais", "Nº Romaneio", None))
        self.radBtnRazaoSocialDestinatario.setToolTip(_translate("frmConsultarNotasFiscais", "Razão Social", None))
        self.radBtnRazaoSocialDestinatario.setText(_translate("frmConsultarNotasFiscais", "Razão Social Destin.", None))
        self.radBtnCnpjDestinatario.setToolTip(_translate("frmConsultarNotasFiscais", "CNPJ", None))
        self.radBtnCnpjDestinatario.setText(_translate("frmConsultarNotasFiscais", "CNPJ Destin.", None))
        self.radBtnFantasiaDestinatario.setToolTip(_translate("frmConsultarNotasFiscais", "Fantasia", None))
        self.radBtnFantasiaDestinatario.setText(_translate("frmConsultarNotasFiscais", "Fantasia Destin.", None))
        self.radBtnIncrisaoEstadualDestinatario.setToolTip(_translate("frmConsultarNotasFiscais", "Inscrição Estadual", None))
        self.radBtnIncrisaoEstadualDestinatario.setText(_translate("frmConsultarNotasFiscais", "Inscr. Estad. Destin.", None))
        self.radBtnDataLanamento.setToolTip(_translate("frmConsultarNotasFiscais", "Inscrição Estadual", None))
        self.radBtnDataLanamento.setText(_translate("frmConsultarNotasFiscais", "Data Lançamento", None))
        self.radBtnDataPeriodos.setToolTip(_translate("frmConsultarNotasFiscais", "Inscrição Estadual", None))
        self.radBtnDataPeriodos.setText(_translate("frmConsultarNotasFiscais", "Data Periodos", None))
        self.txtPesquisar.setToolTip(_translate("frmConsultarNotasFiscais", "Pesquisar", None))
        self.txtPesquisar.setWhatsThis(_translate("frmConsultarNotasFiscais", "Campo de inserir os dados para pesquisar", None))
        self.lblPesquisar.setText(_translate("frmConsultarNotasFiscais", "Pesquisar", None))
        self.txtDataInicial.setToolTip(_translate("frmConsultarNotasFiscais", "Data Inicio", None))
        self.txtDataInicial.setWhatsThis(_translate("frmConsultarNotasFiscais", "Campo de data inicial", None))
        self.txtDataFinal.setToolTip(_translate("frmConsultarNotasFiscais", "Data Final", None))
        self.txtDataFinal.setWhatsThis(_translate("frmConsultarNotasFiscais", "Campo de data final", None))
        self.lblDataInicio.setText(_translate("frmConsultarNotasFiscais", "Data Incio", None))
        self.lblDataFinal.setText(_translate("frmConsultarNotasFiscais", "Data Final", None))

