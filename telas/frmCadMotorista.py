# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmCadMotorista.ui'
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

class Ui_frmCadastroMotorista(object):
    def setupUi(self, frmCadastroMotorista):
        frmCadastroMotorista.setObjectName(_fromUtf8("frmCadastroMotorista"))
        frmCadastroMotorista.resize(890, 522)
        font = QtGui.QFont()
        font.setPointSize(11)
        frmCadastroMotorista.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/motorista.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmCadastroMotorista.setWindowIcon(icon)
        frmCadastroMotorista.setSizeGripEnabled(False)
        frmCadastroMotorista.setModal(True)

        self.grbDadosPessoaJuridica = QtGui.QGroupBox(frmCadastroMotorista)
        self.grbDadosPessoaJuridica.setEnabled(False)
        self.grbDadosPessoaJuridica.setGeometry(QtCore.QRect(10, 3, 871, 161))
        self.grbDadosPessoaJuridica.setObjectName(_fromUtf8("grbDadosPessoaJuridica"))

        self.txtCnpj = QtGui.QLineEdit(self.grbDadosPessoaJuridica)
        self.txtCnpj.setEnabled(False)
        self.txtCnpj.setGeometry(QtCore.QRect(142, 38, 182, 25))
        self.txtCnpj.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly|QtCore.Qt.ImhPreferNumbers|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.txtCnpj.setText(_fromUtf8("..-"))
        self.txtCnpj.setCursorPosition(0)
        self.txtCnpj.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.txtCnpj.setObjectName(_fromUtf8("txtCnpj"))

        self.lblNome = QtGui.QLabel(self.grbDadosPessoaJuridica)
        self.lblNome.setGeometry(QtCore.QRect(10, 64, 81, 19))
        self.lblNome.setObjectName(_fromUtf8("lblNome"))

        self.lblCpf = QtGui.QLabel(self.grbDadosPessoaJuridica)
        self.lblCpf.setGeometry(QtCore.QRect(142, 18, 41, 19))
        self.lblCpf.setObjectName(_fromUtf8("lblCpf"))

        self.txtNome = QtGui.QLineEdit(self.grbDadosPessoaJuridica)
        self.txtNome.setEnabled(False)
        self.txtNome.setGeometry(QtCore.QRect(10, 84, 841, 25))
        self.txtNome.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.txtNome.setMaxLength(70)
        self.txtNome.setObjectName(_fromUtf8("txtNome"))

        self.lblSobrenome = QtGui.QLabel(self.grbDadosPessoaJuridica)
        self.lblSobrenome.setGeometry(QtCore.QRect(8, 108, 101, 19))
        self.lblSobrenome.setObjectName(_fromUtf8("lblSobrenome"))

        self.txtInscricaoEstadua = QtGui.QLineEdit(self.grbDadosPessoaJuridica)
        self.txtInscricaoEstadua.setEnabled(False)
        self.txtInscricaoEstadua.setGeometry(QtCore.QRect(330, 38, 178, 25))
        self.txtInscricaoEstadua.setInputMethodHints(QtCore.Qt.ImhPreferNumbers|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.txtInscricaoEstadua.setMaxLength(8)
        self.txtInscricaoEstadua.setObjectName(_fromUtf8("txtInscricaoEstadua"))

        self.txtSobrenome = QtGui.QLineEdit(self.grbDadosPessoaJuridica)
        self.txtSobrenome.setEnabled(False)
        self.txtSobrenome.setGeometry(QtCore.QRect(8, 128, 844, 25))
        self.txtSobrenome.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.txtSobrenome.setMaxLength(70)
        self.txtSobrenome.setObjectName(_fromUtf8("txtSobrenome"))

        self.lblRg = QtGui.QLabel(self.grbDadosPessoaJuridica)
        self.lblRg.setGeometry(QtCore.QRect(330, 18, 121, 19))
        self.lblRg.setObjectName(_fromUtf8("lblRg"))

        self.lblCodigo = QtGui.QLabel(self.grbDadosPessoaJuridica)
        self.lblCodigo.setGeometry(QtCore.QRect(10, 18, 71, 19))
        self.lblCodigo.setObjectName(_fromUtf8("lblCodigo"))

        self.txtCodigo = QtGui.QLineEdit(self.grbDadosPessoaJuridica)
        self.txtCodigo.setGeometry(QtCore.QRect(10, 38, 121, 25))
        self.txtCodigo.setInputMethodHints(QtCore.Qt.ImhPreferNumbers|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.txtCodigo.setMaxLength(8)
        self.txtCodigo.setObjectName(_fromUtf8("txtCodigo"))

        self.btnPesquisarEmpresa = QtGui.QPushButton(self.grbDadosPessoaJuridica)
        self.btnPesquisarEmpresa.setGeometry(QtCore.QRect(123, 50, 16, 16))
        self.btnPesquisarEmpresa.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnPesquisarEmpresa.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/search_mini.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPesquisarEmpresa.setIcon(icon)
        self.btnPesquisarEmpresa.setFlat(True)
        self.btnPesquisarEmpresa.setObjectName(_fromUtf8("btnPesquisarEmpresa"))

        self.tabWiAdicionais = QtGui.QTabWidget(frmCadastroMotorista)
        self.tabWiAdicionais.setEnabled(False)
        self.tabWiAdicionais.setGeometry(QtCore.QRect(10, 180, 871, 281))
        self.tabWiAdicionais.setTabShape(QtGui.QTabWidget.Triangular)
        self.tabWiAdicionais.setDocumentMode(True)
        self.tabWiAdicionais.setObjectName(_fromUtf8("tabWiAdicionais"))

        self.geral = QtGui.QWidget()
        self.geral.setObjectName(_fromUtf8("geral"))

        self.txtObservacao = QtGui.QTextEdit(self.geral)
        self.txtObservacao.setGeometry(QtCore.QRect(10, 110, 851, 71))
        self.txtObservacao.setObjectName(_fromUtf8("txtObservacao"))

        self.lblObservacao = QtGui.QLabel(self.geral)
        self.lblObservacao.setGeometry(QtCore.QRect(10, 90, 81, 16))
        self.lblObservacao.setObjectName(_fromUtf8("lblObservacao"))

        self.grbAtivo = QtGui.QGroupBox(self.geral)
        self.grbAtivo.setEnabled(False)
        self.grbAtivo.setGeometry(QtCore.QRect(620, 10, 120, 61))
        self.grbAtivo.setObjectName(_fromUtf8("grbAtivo"))

        self.radBtnAtivo = QtGui.QRadioButton(self.grbAtivo)
        self.radBtnAtivo.setGeometry(QtCore.QRect(20, 20, 61, 17))
        self.radBtnAtivo.setObjectName(_fromUtf8("radBtnAtivo"))

        self.radBtnDesativo = QtGui.QRadioButton(self.grbAtivo)
        self.radBtnDesativo.setGeometry(QtCore.QRect(20, 40, 81, 17))
        self.radBtnDesativo.setObjectName(_fromUtf8("radBtnDesativo"))

        self.txtPis = QtGui.QLineEdit(self.geral)
        self.txtPis.setGeometry(QtCore.QRect(350, 42, 251, 25))
        self.txtPis.setMaxLength(25)
        self.txtPis.setObjectName(_fromUtf8("txtPis"))

        self.lblCnhMotorista = QtGui.QLabel(self.geral)
        self.lblCnhMotorista.setGeometry(QtCore.QRect(120, 22, 41, 19))
        self.lblCnhMotorista.setObjectName(_fromUtf8("lblCnhMotorista"))

        self.txtCategoriaCnh = QtGui.QComboBox(self.geral)
        self.txtCategoriaCnh.setGeometry(QtCore.QRect(10, 42, 101, 25))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.txtCategoriaCnh.setPalette(palette)
        self.txtCategoriaCnh.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.txtCategoriaCnh.setObjectName(_fromUtf8("txtCategoriaCnh"))

        self.txtCnh = QtGui.QLineEdit(self.geral)
        self.txtCnh.setGeometry(QtCore.QRect(120, 42, 221, 25))
        self.txtCnh.setMaxLength(9)
        self.txtCnh.setObjectName(_fromUtf8("txtCnh"))

        self.lblPis = QtGui.QLabel(self.geral)
        self.lblPis.setGeometry(QtCore.QRect(350, 28, 75, 13))
        self.lblPis.setObjectName(_fromUtf8("lblPis"))

        self.lblCategoriaCnh = QtGui.QLabel(self.geral)
        self.lblCategoriaCnh.setGeometry(QtCore.QRect(10, 20, 101, 19))
        self.lblCategoriaCnh.setObjectName(_fromUtf8("lblCategoriaCnh"))

        self.tabWiAdicionais.addTab(self.geral, _fromUtf8(""))
        self.contatos = QtGui.QWidget()
        self.contatos.setObjectName(_fromUtf8("contatos"))

        self.tabContatoTelefone = QtGui.QTableWidget(self.contatos)
        self.tabContatoTelefone.setGeometry(QtCore.QRect(13, 84, 361, 141))
        self.tabContatoTelefone.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tabContatoTelefone.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tabContatoTelefone.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.tabContatoTelefone.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tabContatoTelefone.setObjectName(_fromUtf8("tabContatoTelefone"))
        self.tabContatoTelefone.setColumnCount(2)
        self.tabContatoTelefone.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tabContatoTelefone.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tabContatoTelefone.setHorizontalHeaderItem(1, item)
        self.tabContatoTelefone.horizontalHeader().setStretchLastSection(True)
        self.tabContatoTelefone.verticalHeader().setVisible(False)
        self.btnRemoverTelefone = QtGui.QPushButton(self.contatos)
        self.btnRemoverTelefone.setGeometry(QtCore.QRect(343, 230, 31, 27))
        self.btnRemoverTelefone.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnRemoverTelefone.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRemoverTelefone.setIcon(icon1)
        self.btnRemoverTelefone.setObjectName(_fromUtf8("btnRemoverTelefone"))

        self.btnAddEmail = QtGui.QPushButton(self.contatos)
        self.btnAddEmail.setGeometry(QtCore.QRect(823, 39, 31, 27))
        self.btnAddEmail.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnAddEmail.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAddEmail.setIcon(icon2)
        self.btnAddEmail.setObjectName(_fromUtf8("btnAddEmail"))

        self.lblContatoTelefone = QtGui.QLabel(self.contatos)
        self.lblContatoTelefone.setGeometry(QtCore.QRect(13, 27, 53, 13))
        self.lblContatoTelefone.setObjectName(_fromUtf8("lblContatoTelefone"))

        self.lblContatoEmail = QtGui.QLabel(self.contatos)
        self.lblContatoEmail.setGeometry(QtCore.QRect(493, 16, 53, 13))
        self.lblContatoEmail.setObjectName(_fromUtf8("lblContatoEmail"))

        self.btnAddTelefone = QtGui.QPushButton(self.contatos)
        self.btnAddTelefone.setGeometry(QtCore.QRect(343, 50, 31, 27))
        self.btnAddTelefone.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnAddTelefone.setText(_fromUtf8(""))
        self.btnAddTelefone.setIcon(icon2)
        self.btnAddTelefone.setObjectName(_fromUtf8("btnAddTelefone"))

        self.txtNumeroTelefone = QtGui.QLineEdit(self.contatos)
        self.txtNumeroTelefone.setGeometry(QtCore.QRect(73, 51, 261, 25))
        self.txtNumeroTelefone.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.txtNumeroTelefone.setMaxLength(15)
        self.txtNumeroTelefone.setObjectName(_fromUtf8("txtNumeroTelefone"))

        self.txtEnderecoEmail = QtGui.QLineEdit(self.contatos)
        self.txtEnderecoEmail.setGeometry(QtCore.QRect(553, 40, 261, 25))
        self.txtEnderecoEmail.setMaxLength(50)
        self.txtEnderecoEmail.setObjectName(_fromUtf8("txtEnderecoEmail"))

        self.txtContatoEmail = QtGui.QLineEdit(self.contatos)
        self.txtContatoEmail.setGeometry(QtCore.QRect(553, 10, 261, 25))
        self.txtContatoEmail.setMaxLength(25)
        self.txtContatoEmail.setObjectName(_fromUtf8("txtContatoEmail"))

        self.tabContatoEmail = QtGui.QTableWidget(self.contatos)
        self.tabContatoEmail.setGeometry(QtCore.QRect(493, 73, 361, 151))
        self.tabContatoEmail.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tabContatoEmail.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tabContatoEmail.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.tabContatoEmail.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tabContatoEmail.setObjectName(_fromUtf8("tabContatoEmail"))
        self.tabContatoEmail.setColumnCount(2)
        self.tabContatoEmail.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tabContatoEmail.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tabContatoEmail.setHorizontalHeaderItem(1, item)
        self.tabContatoEmail.horizontalHeader().setStretchLastSection(True)
        self.tabContatoEmail.verticalHeader().setVisible(False)
        self.txtContatoTelefone = QtGui.QLineEdit(self.contatos)
        self.txtContatoTelefone.setGeometry(QtCore.QRect(73, 21, 261, 25))
        self.txtContatoTelefone.setMaxLength(25)
        self.txtContatoTelefone.setObjectName(_fromUtf8("txtContatoTelefone"))

        self.lblEmail = QtGui.QLabel(self.contatos)
        self.lblEmail.setGeometry(QtCore.QRect(493, 44, 61, 16))
        self.lblEmail.setObjectName(_fromUtf8("lblEmail"))

        self.btnRemoverEmail = QtGui.QPushButton(self.contatos)
        self.btnRemoverEmail.setGeometry(QtCore.QRect(823, 230, 31, 27))
        self.btnRemoverEmail.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnRemoverEmail.setText(_fromUtf8(""))
        self.btnRemoverEmail.setIcon(icon1)
        self.btnRemoverEmail.setObjectName(_fromUtf8("btnRemoverEmail"))

        self.lblTelefone = QtGui.QLabel(self.contatos)
        self.lblTelefone.setGeometry(QtCore.QRect(13, 55, 61, 16))
        self.lblTelefone.setObjectName(_fromUtf8("lblTelefone"))

        self.tabWiAdicionais.addTab(self.contatos, _fromUtf8(""))
        self.cadastroVeiculo = QtGui.QWidget()
        self.cadastroVeiculo.setObjectName(_fromUtf8("cadastroVeiculo"))

        self.btnAddNovoVeiculo = QtGui.QPushButton(self.cadastroVeiculo)
        self.btnAddNovoVeiculo.setEnabled(False)
        self.btnAddNovoVeiculo.setGeometry(QtCore.QRect(20, 14, 181, 27))
        self.btnAddNovoVeiculo.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnAddNovoVeiculo.setIcon(icon2)
        self.btnAddNovoVeiculo.setObjectName(_fromUtf8("btnAddNovoVeiculo"))

        self.txtPlaca = QtGui.QLineEdit(self.cadastroVeiculo)
        self.txtPlaca.setGeometry(QtCore.QRect(600, 70, 191, 25))
        self.txtPlaca.setObjectName(_fromUtf8("txtPlaca"))

        self.txtModelo = QtGui.QLineEdit(self.cadastroVeiculo)
        self.txtModelo.setGeometry(QtCore.QRect(310, 70, 281, 25))
        self.txtModelo.setMaxLength(50)
        self.txtModelo.setObjectName(_fromUtf8("txtModelo"))

        self.lblPlaca = QtGui.QLabel(self.cadastroVeiculo)
        self.lblPlaca.setGeometry(QtCore.QRect(600, 50, 51, 19))
        self.lblPlaca.setObjectName(_fromUtf8("lblPlaca"))

        self.lblModelo = QtGui.QLabel(self.cadastroVeiculo)
        self.lblModelo.setGeometry(QtCore.QRect(310, 50, 61, 19))
        self.lblModelo.setObjectName(_fromUtf8("lblModelo"))

        self.lblMarca = QtGui.QLabel(self.cadastroVeiculo)
        self.lblMarca.setGeometry(QtCore.QRect(20, 50, 51, 19))
        self.lblMarca.setObjectName(_fromUtf8("lblMarca"))

        self.txtMarca = QtGui.QLineEdit(self.cadastroVeiculo)
        self.txtMarca.setGeometry(QtCore.QRect(20, 70, 281, 25))
        self.txtMarca.setMaxLength(50)
        self.txtMarca.setObjectName(_fromUtf8("txtMarca"))

        self.tabWiAdicionais.addTab(self.cadastroVeiculo, _fromUtf8(""))
        self.grbBotoes = QtGui.QGroupBox(frmCadastroMotorista)
        self.grbBotoes.setGeometry(QtCore.QRect(10, 470, 871, 51))
        self.grbBotoes.setTitle(_fromUtf8(""))
        self.grbBotoes.setObjectName(_fromUtf8("grbBotoes"))

        self.btnNovo = QtGui.QPushButton(self.grbBotoes)
        self.btnNovo.setGeometry(QtCore.QRect(360, 12, 88, 27))
        self.btnNovo.setFocusPolicy(QtCore.Qt.ClickFocus)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/filenew.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnNovo.setIcon(icon3)
        self.btnNovo.setObjectName(_fromUtf8("btnNovo"))

        self.btnSalvar = QtGui.QPushButton(self.grbBotoes)
        self.btnSalvar.setEnabled(False)
        self.btnSalvar.setGeometry(QtCore.QRect(460, 12, 88, 27))
        self.btnSalvar.setFocusPolicy(QtCore.Qt.ClickFocus)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/filesave.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSalvar.setIcon(icon4)
        self.btnSalvar.setObjectName(_fromUtf8("btnSalvar"))

        self.btnCancelar = QtGui.QPushButton(self.grbBotoes)
        self.btnCancelar.setEnabled(False)
        self.btnCancelar.setGeometry(QtCore.QRect(660, 12, 88, 27))
        self.btnCancelar.setFocusPolicy(QtCore.Qt.ClickFocus)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/cancel.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCancelar.setIcon(icon5)
        self.btnCancelar.setObjectName(_fromUtf8("btnCancelar"))

        self.btnDeletar = QtGui.QPushButton(self.grbBotoes)
        self.btnDeletar.setEnabled(False)
        self.btnDeletar.setGeometry(QtCore.QRect(760, 10, 88, 27))
        self.btnDeletar.setFocusPolicy(QtCore.Qt.ClickFocus)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/critical.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnDeletar.setIcon(icon6)
        self.btnDeletar.setObjectName(_fromUtf8("btnDeletar"))

        self.btnEditar = QtGui.QPushButton(self.grbBotoes)
        self.btnEditar.setEnabled(False)
        self.btnEditar.setGeometry(QtCore.QRect(560, 12, 88, 27))
        self.btnEditar.setFocusPolicy(QtCore.Qt.ClickFocus)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/Save-as_37111.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEditar.setIcon(icon7)
        self.btnEditar.setObjectName(_fromUtf8("btnEditar"))

        self.lblPesquisar = QtGui.QLabel(self.grbBotoes)
        self.lblPesquisar.setGeometry(QtCore.QRect(10, 20, 111, 19))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(118, 116, 108))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.lblPesquisar.setPalette(palette)
        self.lblPesquisar.setObjectName(_fromUtf8("lblPesquisar"))

        self.lblNome.setBuddy(self.txtNome)
        self.lblCpf.setBuddy(self.txtCnpj)
        self.lblSobrenome.setBuddy(self.txtSobrenome)
        self.lblRg.setBuddy(self.txtInscricaoEstadua)
        self.lblCodigo.setBuddy(self.txtCodigo)
        self.lblObservacao.setBuddy(self.txtObservacao)
        self.lblCnhMotorista.setBuddy(self.txtCnh)
        self.lblPis.setBuddy(self.txtPis)
        self.lblCategoriaCnh.setBuddy(self.txtCategoriaCnh)
        self.lblContatoTelefone.setBuddy(self.txtContatoTelefone)
        self.lblContatoEmail.setBuddy(self.txtContatoEmail)
        self.lblEmail.setBuddy(self.txtEnderecoEmail)
        self.lblTelefone.setBuddy(self.txtNumeroTelefone)
        self.lblPlaca.setBuddy(self.txtPlaca)
        self.lblModelo.setBuddy(self.txtModelo)
        self.lblMarca.setBuddy(self.txtMarca)

        self.retranslateUi(frmCadastroMotorista)
        self.tabWiAdicionais.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(frmCadastroMotorista)
        frmCadastroMotorista.setTabOrder(self.txtCodigo, self.txtCnpj)
        frmCadastroMotorista.setTabOrder(self.txtCnpj, self.txtInscricaoEstadua)
        frmCadastroMotorista.setTabOrder(self.txtInscricaoEstadua, self.txtNome)
        frmCadastroMotorista.setTabOrder(self.txtNome, self.txtSobrenome)
        frmCadastroMotorista.setTabOrder(self.txtSobrenome, self.tabWiAdicionais)
        frmCadastroMotorista.setTabOrder(self.tabWiAdicionais, self.txtCnh)
        frmCadastroMotorista.setTabOrder(self.txtCnh, self.txtPis)
        frmCadastroMotorista.setTabOrder(self.txtPis, self.radBtnAtivo)
        frmCadastroMotorista.setTabOrder(self.radBtnAtivo, self.radBtnDesativo)
        frmCadastroMotorista.setTabOrder(self.radBtnDesativo, self.txtObservacao)
        frmCadastroMotorista.setTabOrder(self.txtObservacao, self.txtContatoTelefone)
        frmCadastroMotorista.setTabOrder(self.txtContatoTelefone, self.txtNumeroTelefone)
        frmCadastroMotorista.setTabOrder(self.txtNumeroTelefone, self.txtContatoEmail)
        frmCadastroMotorista.setTabOrder(self.txtContatoEmail, self.txtEnderecoEmail)
        frmCadastroMotorista.setTabOrder(self.txtEnderecoEmail, self.txtMarca)
        frmCadastroMotorista.setTabOrder(self.txtMarca, self.txtModelo)
        frmCadastroMotorista.setTabOrder(self.txtModelo, self.txtPlaca)

    def retranslateUi(self, frmCadastroMotorista):
        frmCadastroMotorista.setWindowTitle(_translate("frmCadastroMotorista", "Cadastro Funcionario", None))
        self.grbDadosPessoaJuridica.setWhatsThis(_translate("frmCadastroMotorista", "Grupo de Dados para cadastro e edição de empresas", None))
        self.grbDadosPessoaJuridica.setTitle(_translate("frmCadastroMotorista", "Dados Pessoa Fisíca", None))
        self.txtCnpj.setToolTip(_translate("frmCadastroMotorista", "CNPJ", None))
        self.txtCnpj.setWhatsThis(_translate("frmCadastroMotorista", "<html><head/><body><p>Campo do numero do CNPJ da pessoa fisica</p></body></html>", None))
        self.txtCnpj.setInputMask(_translate("frmCadastroMotorista", "000.000.000-00; ", None))
        self.lblNome.setText(_translate("frmCadastroMotorista", "Nome", None))
        self.lblCpf.setText(_translate("frmCadastroMotorista", "CPF", None))
        self.txtNome.setToolTip(_translate("frmCadastroMotorista", "Razão Social", None))
        self.txtNome.setWhatsThis(_translate("frmCadastroMotorista", "<html><head/><body><p>Campo do nome da razão social da pessoa fisica</p></body></html>", None))
        self.lblSobrenome.setText(_translate("frmCadastroMotorista", "Sobrenome", None))
        self.txtInscricaoEstadua.setToolTip(_translate("frmCadastroMotorista", "Inscrição Estadual", None))
        self.txtInscricaoEstadua.setWhatsThis(_translate("frmCadastroMotorista", "<html><head/><body><p>Campo do numero do inscrição estadual da pessoa fisica</p></body></html>", None))
        self.txtSobrenome.setToolTip(_translate("frmCadastroMotorista", "Nome Fantasia", None))
        self.txtSobrenome.setWhatsThis(_translate("frmCadastroMotorista", "<html><head/><body><p>Campo do nome fantasia da pessoa fisica</p></body></html>", None))
        self.lblRg.setText(_translate("frmCadastroMotorista", "RG", None))
        self.lblCodigo.setText(_translate("frmCadastroMotorista", "Codigo", None))
        self.txtCodigo.setToolTip(_translate("frmCadastroMotorista", "Inscrição Estadual", None))
        self.txtCodigo.setWhatsThis(_translate("frmCadastroMotorista", "<html><head/><body><p>Campo do numero de identificação da pessoa fisica</p></body></html>", None))
        self.btnPesquisarEmpresa.setWhatsThis(_translate("frmCadastroMotorista", "Botão para pesquisar dados de empresa", None))
        self.tabWiAdicionais.setWhatsThis(_translate("frmCadastroMotorista", "<html><head/><body><p>Botão adicionar um novo veiculo</p></body></html>", None))
        self.txtObservacao.setToolTip(_translate("frmCadastroMotorista", "Observação", None))
        self.txtObservacao.setWhatsThis(_translate("frmCadastroMotorista", "<html><head/><body><p>Campo de texto de observação sobre o motorista</p></body></html>", None))
        self.lblObservacao.setText(_translate("frmCadastroMotorista", "Observação", None))
        self.grbAtivo.setTitle(_translate("frmCadastroMotorista", "Situação", None))
        self.radBtnAtivo.setWhatsThis(_translate("frmCadastroMotorista", "<html><head/><body><p>Item de seleção para motorista ativa e operante</p></body></html>", None))
        self.radBtnAtivo.setText(_translate("frmCadastroMotorista", "Ativo", None))
        self.radBtnDesativo.setWhatsThis(_translate("frmCadastroMotorista", "<html><head/><body><p>Item de seleção para motorista desativado e inoperante</p></body></html>", None))
        self.radBtnDesativo.setText(_translate("frmCadastroMotorista", "Desativo", None))
        self.txtPis.setToolTip(_translate("frmCadastroMotorista", "PIS/PASEP", None))
        self.txtPis.setWhatsThis(_translate("frmCadastroMotorista", "<html><head/><body><p>Campo do número do PIS/PASEP do motorista</p></body></html>", None))
        self.lblCnhMotorista.setText(_translate("frmCadastroMotorista", "CNH", None))
        self.txtCategoriaCnh.setWhatsThis(_translate("frmCadastroMotorista", "<html><head/><body><p>Campo de seleção da categoria da CNH</p></body></html>", None))
        self.txtCnh.setToolTip(_translate("frmCadastroMotorista", "CNH", None))
        self.txtCnh.setWhatsThis(_translate("frmCadastroMotorista", "Campo do numero de identificação CNH", None))
        self.lblPis.setText(_translate("frmCadastroMotorista", "PIS/PASEP", None))
        self.lblCategoriaCnh.setText(_translate("frmCadastroMotorista", "Categoria CNH", None))
        self.tabWiAdicionais.setTabText(self.tabWiAdicionais.indexOf(self.geral), _translate("frmCadastroMotorista", "Geral", None))
        self.tabContatoTelefone.setWhatsThis(_translate("frmCadastroMotorista", "<html><head/><body><p>Tabela de informações de contato de telefone</p></body></html>", None))
        item = self.tabContatoTelefone.horizontalHeaderItem(0)
        item.setText(_translate("frmCadastroMotorista", "Contato", None))
        item = self.tabContatoTelefone.horizontalHeaderItem(1)
        item.setText(_translate("frmCadastroMotorista", "Telefone", None))
        self.btnRemoverTelefone.setToolTip(_translate("frmCadastroMotorista", "Remover", None))
        self.btnRemoverTelefone.setWhatsThis(_translate("frmCadastroMotorista", "<html><head/><body><p>Botão remover um contato  de telefone a lista</p></body></html>", None))
        self.btnAddEmail.setToolTip(_translate("frmCadastroMotorista", "Adicionar", None))
        self.btnAddEmail.setWhatsThis(_translate("frmCadastroMotorista", "<html><head/><body><p>Botão adicionar um contato de e-mail a lista</p></body></html>", None))
        self.lblContatoTelefone.setText(_translate("frmCadastroMotorista", "Contato", None))
        self.lblContatoEmail.setText(_translate("frmCadastroMotorista", "Contato", None))
        self.btnAddTelefone.setToolTip(_translate("frmCadastroMotorista", "Adicionar", None))
        self.btnAddTelefone.setWhatsThis(_translate("frmCadastroMotorista", "<html><head/><body><p>Botão adicionar um contato de telefone a lista</p></body></html>", None))
        self.txtNumeroTelefone.setToolTip(_translate("frmCadastroMotorista", "Telefone", None))
        self.txtNumeroTelefone.setWhatsThis(_translate("frmCadastroMotorista", "<html><head/><body><p>Campo do numero de telefone do contato</p></body></html>", None))
        self.txtEnderecoEmail.setToolTip(_translate("frmCadastroMotorista", "E-mail", None))
        self.txtEnderecoEmail.setWhatsThis(_translate("frmCadastroMotorista", "<html><head/><body><p>Campo do endereço de e-mail do contato</p></body></html>", None))
        self.txtContatoEmail.setToolTip(_translate("frmCadastroMotorista", "Contato", None))
        self.txtContatoEmail.setWhatsThis(_translate("frmCadastroMotorista", "<html><head/><body><p>Campo do nome do contato</p></body></html>", None))
        self.tabContatoEmail.setWhatsThis(_translate("frmCadastroMotorista", "<html><head/><body><p>Tabela de informações de endereço de e-mail</p></body></html>", None))
        item = self.tabContatoEmail.horizontalHeaderItem(0)
        item.setText(_translate("frmCadastroMotorista", "Contato", None))
        item = self.tabContatoEmail.horizontalHeaderItem(1)
        item.setText(_translate("frmCadastroMotorista", "E-mail", None))
        self.txtContatoTelefone.setToolTip(_translate("frmCadastroMotorista", "Contato", None))
        self.txtContatoTelefone.setWhatsThis(_translate("frmCadastroMotorista", "<html><head/><body><p>Campo do nome do contato</p></body></html>", None))
        self.lblEmail.setText(_translate("frmCadastroMotorista", "E-mail", None))
        self.btnRemoverEmail.setToolTip(_translate("frmCadastroMotorista", "Remover", None))
        self.btnRemoverEmail.setWhatsThis(_translate("frmCadastroMotorista", "<html><head/><body><p>Botão remover um contato de e-mail da lista</p></body></html>", None))
        self.lblTelefone.setText(_translate("frmCadastroMotorista", "Telefone", None))
        self.tabWiAdicionais.setTabText(self.tabWiAdicionais.indexOf(self.contatos), _translate("frmCadastroMotorista", "Contato", None))
        self.btnAddNovoVeiculo.setToolTip(_translate("frmCadastroMotorista", "Adicionar Novo Veiculo", None))
        self.btnAddNovoVeiculo.setWhatsThis(_translate("frmCadastroMotorista", "<html><head/><body><p>Botão adicionar um novo Veiculo</p></body></html>", None))
        self.btnAddNovoVeiculo.setText(_translate("frmCadastroMotorista", "Adicionar Novo Veiculo", None))
        self.txtPlaca.setToolTip(_translate("frmCadastroMotorista", "Placa", None))
        self.txtPlaca.setWhatsThis(_translate("frmCadastroMotorista", "Campo de identificação da placa do veiculo", None))
        self.txtPlaca.setInputMask(_translate("frmCadastroMotorista", "nnn-0000; ", None))
        self.txtPlaca.setText(_translate("frmCadastroMotorista", "-", None))
        self.txtModelo.setToolTip(_translate("frmCadastroMotorista", "Modelo", None))
        self.txtModelo.setWhatsThis(_translate("frmCadastroMotorista", "Campo com o nome do modelo do veiculo", None))
        self.lblPlaca.setText(_translate("frmCadastroMotorista", "Placa", None))
        self.lblModelo.setText(_translate("frmCadastroMotorista", "Modelo", None))
        self.lblMarca.setText(_translate("frmCadastroMotorista", "Marca", None))
        self.txtMarca.setToolTip(_translate("frmCadastroMotorista", "Marca", None))
        self.txtMarca.setWhatsThis(_translate("frmCadastroMotorista", "Campo do nome da marca do veiculo", None))
        self.tabWiAdicionais.setTabText(self.tabWiAdicionais.indexOf(self.cadastroVeiculo), _translate("frmCadastroMotorista", "Veiculo", None))
        self.btnNovo.setToolTip(_translate("frmCadastroMotorista", "Novo", None))
        self.btnNovo.setWhatsThis(_translate("frmCadastroMotorista", "<html><head/><body><p>Botão para cadastrar uma novo registro da pessoa jurídica</p></body></html>", None))
        self.btnNovo.setText(_translate("frmCadastroMotorista", "Novo", None))
        self.btnSalvar.setToolTip(_translate("frmCadastroMotorista", "Salvar", None))
        self.btnSalvar.setWhatsThis(_translate("frmCadastroMotorista", "<html><head/><body><p>Botão para salvar um novo registro da pessoa jurídica</p></body></html>", None))
        self.btnSalvar.setText(_translate("frmCadastroMotorista", "Salvar", None))
        self.btnCancelar.setToolTip(_translate("frmCadastroMotorista", "Cancelar", None))
        self.btnCancelar.setWhatsThis(_translate("frmCadastroMotorista", "Botão para cancelar a operação ", None))
        self.btnCancelar.setText(_translate("frmCadastroMotorista", "Cancelar", None))
        self.btnDeletar.setToolTip(_translate("frmCadastroMotorista", "Deletar", None))
        self.btnDeletar.setWhatsThis(_translate("frmCadastroMotorista", "<html><head/><body><p>Botão de deletar o registro da pessoa jurídica</p></body></html>", None))
        self.btnDeletar.setText(_translate("frmCadastroMotorista", "Deletar", None))
        self.btnEditar.setToolTip(_translate("frmCadastroMotorista", "Editar", None))
        self.btnEditar.setWhatsThis(_translate("frmCadastroMotorista", "<html><head/><body><p>Botão para salvar o registo editado da pessoa jurídica</p></body></html>", None))
        self.btnEditar.setText(_translate("frmCadastroMotorista", "Editar", None))
        self.lblPesquisar.setText(_translate("frmCadastroMotorista", "[F12] Pesquisar", None))

