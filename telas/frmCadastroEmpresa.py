# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmCadastroEmpresa.ui'
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

class Ui_frmCadastroEmpresa(object):
    def setupUi(self, frmCadastroEmpresa):
        frmCadastroEmpresa.setObjectName(_fromUtf8("frmCadastroEmpresa"))
        frmCadastroEmpresa.resize(889, 695)
        font = QtGui.QFont()
        frmCadastroEmpresa.setSizeGripEnabled(False)
        frmCadastroEmpresa.setModal(True)
        font.setPointSize(11)
        frmCadastroEmpresa.setFont(font)
        self.grbBotoes = QtGui.QGroupBox(frmCadastroEmpresa)
        self.grbBotoes.setGeometry(QtCore.QRect(4, 614, 881, 80))
        self.grbBotoes.setTitle(_fromUtf8(""))
        self.grbBotoes.setObjectName(_fromUtf8("grbBotoes"))

        self.btnNovo = QtGui.QPushButton(self.grbBotoes)
        self.btnNovo.setGeometry(QtCore.QRect(370, 10, 81, 61))
        self.btnNovo.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnNovo.setObjectName(_fromUtf8("btnNovo"))

        self.btnCancelar = QtGui.QPushButton(self.grbBotoes)
        self.btnCancelar.setEnabled(False)
        self.btnCancelar.setGeometry(QtCore.QRect(670, 10, 81, 61))
        self.btnCancelar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnCancelar.setObjectName(_fromUtf8("btnCancelar"))

        self.btnDeletar = QtGui.QPushButton(self.grbBotoes)
        self.btnDeletar.setEnabled(False)
        self.btnDeletar.setGeometry(QtCore.QRect(770, 10, 81, 61))
        self.btnDeletar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnDeletar.setObjectName(_fromUtf8("btnDeletar"))

        self.btnSalvar = QtGui.QPushButton(self.grbBotoes)
        self.btnSalvar.setEnabled(False)
        self.btnSalvar.setGeometry(QtCore.QRect(470, 10, 81, 61))
        self.btnSalvar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnSalvar.setObjectName(_fromUtf8("btnSalvar"))

        self.btnEditar = QtGui.QPushButton(self.grbBotoes)
        self.btnEditar.setEnabled(False)
        self.btnEditar.setGeometry(QtCore.QRect(570, 10, 81, 61))
        self.btnEditar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnEditar.setObjectName(_fromUtf8("btnEditar"))

        self.grubTextos = QtGui.QGroupBox(frmCadastroEmpresa)
        self.grubTextos.setEnabled(False)
        self.grubTextos.setGeometry(QtCore.QRect(4, 3, 881, 361))
        self.grubTextos.setTitle(_fromUtf8(""))
        self.grubTextos.setObjectName(_fromUtf8("grubTextos"))

        self.lblCep = QtGui.QLabel(self.grubTextos)
        self.lblCep.setGeometry(QtCore.QRect(368, 212, 31, 19))
        self.lblCep.setObjectName(_fromUtf8("lblCep"))

        self.txtCidades = QtGui.QLineEdit(self.grubTextos)
        self.txtCidades.setEnabled(False)
        self.txtCidades.setGeometry(QtCore.QRect(532, 232, 341, 25))
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
        self.txtCidades.setPalette(palette)
        self.txtCidades.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.txtCidades.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.txtCidades.setMaxLength(70)
        self.txtCidades.setObjectName(_fromUtf8("txtCidades"))

        self.lblBairro = QtGui.QLabel(self.grubTextos)
        self.lblBairro.setGeometry(QtCore.QRect(8, 212, 41, 19))
        self.lblBairro.setObjectName(_fromUtf8("lblBairro"))

        self.lblComplemento = QtGui.QLabel(self.grubTextos)
        self.lblComplemento.setGeometry(QtCore.QRect(602, 142, 101, 16))
        self.lblComplemento.setObjectName(_fromUtf8("lblComplemento"))

        self.txtTelefone = QtGui.QLineEdit(self.grubTextos)
        self.txtTelefone.setGeometry(QtCore.QRect(650, 303, 191, 25))
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
        self.txtTelefone.setPalette(palette)
        self.txtTelefone.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly|QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.txtTelefone.setCursorPosition(1)
        self.txtTelefone.setObjectName(_fromUtf8("txtTelefone"))

        self.txtCnpj = QtGui.QLineEdit(self.grubTextos)
        self.txtCnpj.setGeometry(QtCore.QRect(331, 26, 182, 25))
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
        self.txtCnpj.setPalette(palette)
        self.txtCnpj.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly|QtCore.Qt.ImhPreferNumbers|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.txtCnpj.setText(_fromUtf8("../-"))
        self.txtCnpj.setCursorPosition(0)
        self.txtCnpj.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.txtCnpj.setObjectName(_fromUtf8("txtCnpj"))

        self.lblTipoEmpresa = QtGui.QLabel(self.grubTextos)
        self.lblTipoEmpresa.setGeometry(QtCore.QRect(153, 5, 121, 19))
        self.lblTipoEmpresa.setObjectName(_fromUtf8("lblTipoEmpresa"))

        self.lblRazaoSocial = QtGui.QLabel(self.grubTextos)
        self.lblRazaoSocial.setGeometry(QtCore.QRect(452, 72, 81, 19))
        self.lblRazaoSocial.setObjectName(_fromUtf8("lblRazaoSocial"))

        self.lblCnpj = QtGui.QLabel(self.grubTextos)
        self.lblCnpj.setGeometry(QtCore.QRect(331, 6, 41, 19))
        self.lblCnpj.setObjectName(_fromUtf8("lblCnpj"))

        self.txtRazaoSocial = QtGui.QLineEdit(self.grubTextos)
        self.txtRazaoSocial.setGeometry(QtCore.QRect(452, 92, 421, 25))
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
        self.txtRazaoSocial.setPalette(palette)
        self.txtRazaoSocial.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.txtRazaoSocial.setMaxLength(70)
        self.txtRazaoSocial.setObjectName(_fromUtf8("txtRazaoSocial"))

        self.txtCep = QtGui.QLineEdit(self.grubTextos)
        self.txtCep.setGeometry(QtCore.QRect(368, 232, 151, 25))
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
        self.txtCep.setPalette(palette)
        self.txtCep.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly|QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.txtCep.setInputMask(_fromUtf8("00000-000; "))

        self.txtCep.setCursorPosition(0)
        self.txtCep.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.txtCep.setObjectName(_fromUtf8("txtCep"))

        self.txtInscricaoMunicipal = QtGui.QLineEdit(self.grubTextos)
        self.txtInscricaoMunicipal.setGeometry(QtCore.QRect(703, 26, 171, 25))
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
        self.txtInscricaoMunicipal.setPalette(palette)
        self.txtInscricaoMunicipal.setInputMethodHints(QtCore.Qt.ImhPreferNumbers|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.txtInscricaoMunicipal.setMaxLength(8)
        self.txtInscricaoMunicipal.setObjectName(_fromUtf8("txtInscricaoMunicipal"))

        self.lblInscricaoMunicipal = QtGui.QLabel(self.grubTextos)
        self.lblInscricaoMunicipal.setGeometry(QtCore.QRect(703, 6, 141, 19))
        self.lblInscricaoMunicipal.setObjectName(_fromUtf8("lblInscricaoMunicipal"))

        self.txtTipoEmpresa = QtGui.QComboBox(self.grubTextos)
        self.txtTipoEmpresa.setGeometry(QtCore.QRect(153, 25, 171, 25))
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
        self.txtTipoEmpresa.setPalette(palette)
        self.txtTipoEmpresa.setObjectName(_fromUtf8("txtTipoEmpresa"))

        self.lblEndereco = QtGui.QLabel(self.grubTextos)
        self.lblEndereco.setGeometry(QtCore.QRect(8, 142, 66, 19))
        self.lblEndereco.setObjectName(_fromUtf8("lblEndereco"))

        self.txtComplemento = QtGui.QLineEdit(self.grubTextos)
        self.txtComplemento.setGeometry(QtCore.QRect(602, 162, 271, 25))
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
        self.txtComplemento.setPalette(palette)
        self.txtComplemento.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.txtComplemento.setMaxLength(50)
        self.txtComplemento.setObjectName(_fromUtf8("txtComplemento"))

        self.txtEstados = QtGui.QLineEdit(self.grubTextos)
        self.txtEstados.setEnabled(False)
        self.txtEstados.setGeometry(QtCore.QRect(8, 303, 201, 25))
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
        self.txtEstados.setPalette(palette)
        self.txtEstados.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.txtEstados.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhUppercaseOnly)
        self.txtEstados.setMaxLength(50)
        self.txtEstados.setObjectName(_fromUtf8("txtEstados"))

        self.txtNumero = QtGui.QLineEdit(self.grubTextos)
        self.txtNumero.setGeometry(QtCore.QRect(436, 162, 161, 25))
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
        self.txtNumero.setPalette(palette)
        self.txtNumero.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.txtNumero.setMaxLength(11)
        self.txtNumero.setObjectName(_fromUtf8("txtNumero"))

        self.lblNomeFantasia = QtGui.QLabel(self.grubTextos)
        self.lblNomeFantasia.setGeometry(QtCore.QRect(8, 72, 101, 19))
        self.lblNomeFantasia.setObjectName(_fromUtf8("lblNomeFantasia"))

        self.txtBairro = QtGui.QLineEdit(self.grubTextos)
        self.txtBairro.setGeometry(QtCore.QRect(8, 232, 351, 25))
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
        self.txtBairro.setPalette(palette)
        self.txtBairro.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.txtBairro.setMaxLength(50)
        self.txtBairro.setObjectName(_fromUtf8("txtBairro"))

        self.txtInscricaoEstadua = QtGui.QLineEdit(self.grubTextos)
        self.txtInscricaoEstadua.setGeometry(QtCore.QRect(519, 26, 178, 25))
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
        self.txtInscricaoEstadua.setPalette(palette)
        self.txtInscricaoEstadua.setInputMethodHints(QtCore.Qt.ImhPreferNumbers|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.txtInscricaoEstadua.setMaxLength(8)
        self.txtInscricaoEstadua.setObjectName(_fromUtf8("txtInscricaoEstadua"))

        self.lblTelefoene = QtGui.QLabel(self.grubTextos)
        self.lblTelefoene.setGeometry(QtCore.QRect(650, 283, 61, 19))
        self.lblTelefoene.setObjectName(_fromUtf8("lblTelefoene"))

        self.lblNumero = QtGui.QLabel(self.grubTextos)
        self.lblNumero.setGeometry(QtCore.QRect(436, 142, 51, 19))
        self.lblNumero.setObjectName(_fromUtf8("lblNumero"))

        self.txtEndereco = QtGui.QLineEdit(self.grubTextos)
        self.txtEndereco.setGeometry(QtCore.QRect(8, 162, 421, 25))
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
        self.txtEndereco.setPalette(palette)
        self.txtEndereco.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.txtEndereco.setMaxLength(50)
        self.txtEndereco.setObjectName(_fromUtf8("txtEndereco"))

        self.txtFantasia = QtGui.QLineEdit(self.grubTextos)
        self.txtFantasia.setGeometry(QtCore.QRect(8, 92, 431, 25))
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
        self.txtFantasia.setPalette(palette)
        self.txtFantasia.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.txtFantasia.setMaxLength(70)
        self.txtFantasia.setObjectName(_fromUtf8("txtFantasia"))

        self.lblCidades = QtGui.QLabel(self.grubTextos)
        self.lblCidades.setGeometry(QtCore.QRect(532, 212, 51, 19))
        self.lblCidades.setObjectName(_fromUtf8("lblCidades"))

        self.lblEstados = QtGui.QLabel(self.grubTextos)
        self.lblEstados.setGeometry(QtCore.QRect(10, 283, 51, 19))
        self.lblEstados.setObjectName(_fromUtf8("lblEstados"))

        self.lblInscricaoEstadual = QtGui.QLabel(self.grubTextos)
        self.lblInscricaoEstadual.setGeometry(QtCore.QRect(519, 6, 121, 19))
        self.lblInscricaoEstadual.setObjectName(_fromUtf8("lblInscricaoEstadual"))

        self.txtId = QtGui.QLineEdit(self.grubTextos)
        self.txtId.setEnabled(False)
        self.txtId.setGeometry(QtCore.QRect(6, 24, 141, 25))
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
        self.txtId.setPalette(palette)
        self.txtId.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.txtId.setInputMethodHints(QtCore.Qt.ImhPreferNumbers|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.txtId.setMaxLength(11)
        self.txtId.setObjectName(_fromUtf8("txtId"))

        self.lblCodigo = QtGui.QLabel(self.grubTextos)
        self.lblCodigo.setGeometry(QtCore.QRect(6, 4, 51, 19))
        self.lblCodigo.setObjectName(_fromUtf8("lblCodigo"))

        self.txtSite = QtGui.QLineEdit(self.grubTextos)
        self.txtSite.setGeometry(QtCore.QRect(220, 303, 421, 25))
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
        self.txtSite.setPalette(palette)
        self.txtSite.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.txtSite.setMaxLength(50)
        self.txtSite.setObjectName(_fromUtf8("txtSite"))

        self.lblSite = QtGui.QLabel(self.grubTextos)
        self.lblSite.setGeometry(QtCore.QRect(220, 283, 31, 19))
        self.lblSite.setObjectName(_fromUtf8("lblSite"))

        self.ckBoOperacional = QtGui.QCheckBox(self.grubTextos)
        self.ckBoOperacional.setEnabled(False)
        self.ckBoOperacional.setGeometry(QtCore.QRect(780, 340, 101, 17))
        self.ckBoOperacional.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.ckBoOperacional.setObjectName(_fromUtf8("ckBoOperacional"))

        self.grbPesquisa = QtGui.QGroupBox(frmCadastroEmpresa)
        self.grbPesquisa.setGeometry(QtCore.QRect(6, 368, 877, 241))
        self.grbPesquisa.setTitle(_fromUtf8(""))
        self.grbPesquisa.setObjectName(_fromUtf8("grbPesquisa"))

        self.txtPesquisa = QtGui.QLineEdit(self.grbPesquisa)
        self.txtPesquisa.setGeometry(QtCore.QRect(470, 14, 351, 25))
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
        self.txtPesquisa.setPalette(palette)
        self.txtPesquisa.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.txtPesquisa.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.txtPesquisa.setMaxLength(50)
        self.txtPesquisa.setObjectName(_fromUtf8("txtPesquisa"))

        self.btnPesquisar = QtGui.QPushButton(self.grbPesquisa)
        self.btnPesquisar.setGeometry(QtCore.QRect(830, 12, 41, 31))
        self.btnPesquisar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnPesquisar.setText(_fromUtf8(""))
        self.btnPesquisar.setObjectName(_fromUtf8("btnPesquisar"))

        self.tbPesquisa = QtGui.QTableWidget(self.grbPesquisa)
        self.tbPesquisa.setGeometry(QtCore.QRect(10, 51, 861, 151))
        self.tbPesquisa.setColumnCount(17)
        self.tbPesquisa.setHorizontalHeaderLabels(['COD.', 'Tipo Empresa', 'CNPJ', 'Ins. Estadual', 'Insc. Municipal', 'Fantasia', 'Razao Socil', 'Endereco', 'Numero', 'Complemento', 'Bairro', 'Telefone', 'Site', 'Cep', 'Cidade', 'Estado', 'Situação'])
        self.tbPesquisa.setEditTriggers(self.tbPesquisa.NoEditTriggers)
        self.tbPesquisa.setSelectionBehavior(self.tbPesquisa.SelectRows)
        self.tbPesquisa.setSelectionMode(self.tbPesquisa.SingleSelection)
        self.tbPesquisa.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tbPesquisa.setObjectName(_fromUtf8("tbPesquisa"))

        self.grbDadosPesquisa = QtGui.QGroupBox(self.grbPesquisa)
        self.grbDadosPesquisa.setGeometry(QtCore.QRect(0, 0, 451, 44))
        self.grbDadosPesquisa.setObjectName(_fromUtf8("grbDadosPesquisa"))

        self.radBtnCodigo = QtGui.QRadioButton(self.grbDadosPesquisa)
        self.radBtnCodigo.setGeometry(QtCore.QRect(10, 20, 61, 17))
        self.radBtnCodigo.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.radBtnCodigo.setObjectName(_fromUtf8("radBtnCodigo"))

        self.radBtnFantasia = QtGui.QRadioButton(self.grbDadosPesquisa)
        self.radBtnFantasia.setGeometry(QtCore.QRect(80, 20, 71, 17))
        self.radBtnFantasia.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.radBtnFantasia.setObjectName(_fromUtf8("radBtnFantasia"))

        self.radBtnRazaoSocial = QtGui.QRadioButton(self.grbDadosPesquisa)
        self.radBtnRazaoSocial.setGeometry(QtCore.QRect(160, 20, 101, 17))
        self.radBtnRazaoSocial.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.radBtnRazaoSocial.setObjectName(_fromUtf8("radBtnRazaoSocial"))

        self.radBtnCnpj = QtGui.QRadioButton(self.grbDadosPesquisa)
        self.radBtnCnpj.setGeometry(QtCore.QRect(270, 20, 51, 17))
        self.radBtnCnpj.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.radBtnCnpj.setObjectName(_fromUtf8("radBtnCnpj"))

        self.radBtnInsEstadual = QtGui.QRadioButton(self.grbDadosPesquisa)
        self.radBtnInsEstadual.setGeometry(QtCore.QRect(330, 20, 91, 17))
        self.radBtnInsEstadual.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.radBtnInsEstadual.setObjectName(_fromUtf8("radBtnInsEstadual"))

        self.btnLimparPesquisa = QtGui.QPushButton(self.grbPesquisa)
        self.btnLimparPesquisa.setGeometry(QtCore.QRect(750, 210, 121, 23))
        self.btnLimparPesquisa.setObjectName(_fromUtf8("btnLimparPesquisa"))

        self.lblCep.setBuddy(self.txtCep)
        self.lblBairro.setBuddy(self.txtBairro)
        self.lblComplemento.setBuddy(self.txtComplemento)
        self.lblTipoEmpresa.setBuddy(self.txtTipoEmpresa)
        self.lblRazaoSocial.setBuddy(self.txtRazaoSocial)
        self.lblCnpj.setBuddy(self.txtCnpj)
        self.lblInscricaoMunicipal.setBuddy(self.txtInscricaoMunicipal)
        self.lblEndereco.setBuddy(self.txtEndereco)
        self.lblNomeFantasia.setBuddy(self.txtFantasia)
        self.lblTelefoene.setBuddy(self.txtTelefone)
        self.lblNumero.setBuddy(self.txtNumero)
        self.lblCidades.setBuddy(self.txtCidades)
        self.lblEstados.setBuddy(self.txtEstados)
        self.lblInscricaoEstadual.setBuddy(self.txtInscricaoEstadua)
        self.lblCodigo.setBuddy(self.txtId)
        self.lblSite.setBuddy(self.txtSite)

        self.retranslateUi(frmCadastroEmpresa)
        QtCore.QMetaObject.connectSlotsByName(frmCadastroEmpresa)
        frmCadastroEmpresa.setTabOrder(self.txtId, self.txtTipoEmpresa)
        frmCadastroEmpresa.setTabOrder(self.txtTipoEmpresa, self.txtCnpj)
        frmCadastroEmpresa.setTabOrder(self.txtCnpj, self.txtInscricaoEstadua)
        frmCadastroEmpresa.setTabOrder(self.txtInscricaoEstadua, self.txtInscricaoMunicipal)
        frmCadastroEmpresa.setTabOrder(self.txtInscricaoMunicipal, self.txtFantasia)
        frmCadastroEmpresa.setTabOrder(self.txtFantasia, self.txtRazaoSocial)
        frmCadastroEmpresa.setTabOrder(self.txtRazaoSocial, self.txtEndereco)
        frmCadastroEmpresa.setTabOrder(self.txtEndereco, self.txtNumero)
        frmCadastroEmpresa.setTabOrder(self.txtNumero, self.txtComplemento)
        frmCadastroEmpresa.setTabOrder(self.txtComplemento, self.txtBairro)
        frmCadastroEmpresa.setTabOrder(self.txtBairro, self.txtCep)
        frmCadastroEmpresa.setTabOrder(self.txtCep, self.txtCidades)
        frmCadastroEmpresa.setTabOrder(self.txtCidades, self.txtEstados)
        frmCadastroEmpresa.setTabOrder(self.txtEstados, self.txtSite)
        frmCadastroEmpresa.setTabOrder(self.txtSite, self.txtTelefone)
        frmCadastroEmpresa.setTabOrder(self.txtTelefone, self.radBtnCodigo)
        frmCadastroEmpresa.setTabOrder(self.radBtnCodigo, self.radBtnFantasia)
        frmCadastroEmpresa.setTabOrder(self.radBtnFantasia, self.radBtnRazaoSocial)
        frmCadastroEmpresa.setTabOrder(self.radBtnRazaoSocial, self.radBtnCnpj)
        frmCadastroEmpresa.setTabOrder(self.radBtnCnpj, self.radBtnInsEstadual)
        frmCadastroEmpresa.setTabOrder(self.radBtnInsEstadual, self.txtPesquisa)
        frmCadastroEmpresa.setTabOrder(self.txtPesquisa, self.btnPesquisar)
        frmCadastroEmpresa.setTabOrder(self.btnPesquisar, self.tbPesquisa)
        frmCadastroEmpresa.setTabOrder(self.tbPesquisa, self.btnNovo)
        frmCadastroEmpresa.setTabOrder(self.btnNovo, self.btnSalvar)
        frmCadastroEmpresa.setTabOrder(self.btnSalvar, self.btnEditar)
        frmCadastroEmpresa.setTabOrder(self.btnEditar, self.btnCancelar)
        frmCadastroEmpresa.setTabOrder(self.btnCancelar, self.btnDeletar)

    def retranslateUi(self, frmCadastroEmpresa):
        frmCadastroEmpresa.setWindowTitle(_translate("frmCadastroEmpresa", "Cadastro Empresa", None))
        self.grbBotoes.setWhatsThis(_translate("frmCadastroEmpresa", "Grupo de botões referente as suas funções", None))
        self.btnNovo.setWhatsThis(_translate("frmCadastroEmpresa", "Botão de Criação de um novo registro", None))
        self.btnNovo.setText(_translate("frmCadastroEmpresa", "Novo", None))
        self.btnCancelar.setWhatsThis(_translate("frmCadastroEmpresa", "Botão de cancelar a operação iniciada", None))
        self.btnCancelar.setText(_translate("frmCadastroEmpresa", "Cancelar", None))
        self.btnDeletar.setWhatsThis(_translate("frmCadastroEmpresa", "Botão de deleção de um registro existente", None))
        self.btnDeletar.setText(_translate("frmCadastroEmpresa", "Deletar", None))
        self.btnSalvar.setWhatsThis(_translate("frmCadastroEmpresa", "Botão para salvar um novo registro", None))
        self.btnSalvar.setText(_translate("frmCadastroEmpresa", "Salvar", None))
        self.btnEditar.setWhatsThis(_translate("frmCadastroEmpresa", "Botão para salvar edição de um registro existente", None))
        self.btnEditar.setText(_translate("frmCadastroEmpresa", "Editar", None))
        self.grubTextos.setWhatsThis(_translate("frmCadastroEmpresa", "Grupo de Dados para cadastro e edição de empresas", None))
        self.lblCep.setText(_translate("frmCadastroEmpresa", "CEP", None))
        self.txtCidades.setToolTip(_translate("frmCadastroEmpresa", "Cidade", None))
        self.txtCidades.setWhatsThis(_translate("frmCadastroEmpresa", "Campo do nome da cidade referente a localização do endereço dentro do estado", None))
        self.lblBairro.setText(_translate("frmCadastroEmpresa", "Bairro", None))
        self.lblComplemento.setText(_translate("frmCadastroEmpresa", "Complemento", None))
        self.txtTelefone.setToolTip(_translate("frmCadastroEmpresa", "Telefone", None))
        self.txtTelefone.setWhatsThis(_translate("frmCadastroEmpresa", "Campo do numero de cantato de telefone da empresa", None))
        self.txtTelefone.setInputMask(_translate("frmCadastroEmpresa", "(00) 00000-0000; ", None))
        self.txtCnpj.setToolTip(_translate("frmCadastroEmpresa", "CNPJ", None))
        self.txtCnpj.setWhatsThis(_translate("frmCadastroEmpresa", "Campo do numero do CNPJ da empresa", None))
        self.txtCnpj.setInputMask(_translate("frmCadastroEmpresa", "00.000.000/0000-00; ", None))
        self.lblTipoEmpresa.setText(_translate("frmCadastroEmpresa", "Tipo de Empresa", None))
        self.lblRazaoSocial.setText(_translate("frmCadastroEmpresa", "Razão Social", None))
        self.lblCnpj.setText(_translate("frmCadastroEmpresa", "CNPJ", None))
        self.txtRazaoSocial.setToolTip(_translate("frmCadastroEmpresa", "Razão Social", None))
        self.txtRazaoSocial.setWhatsThis(_translate("frmCadastroEmpresa", "Campo do nome da razão social da empresa", None))
        self.txtCep.setToolTip(_translate("frmCadastroEmpresa", "CEP", None))
        self.txtCep.setWhatsThis(_translate("frmCadastroEmpresa", "Campo de CEP referente a identificação da cidade e qual estado pertence", None))
        self.txtInscricaoMunicipal.setToolTip(_translate("frmCadastroEmpresa", "Inscrição Municipal", None))
        self.txtInscricaoMunicipal.setWhatsThis(_translate("frmCadastroEmpresa", "Campo do numero do inscrição municipal da empresa", None))
        self.lblInscricaoMunicipal.setText(_translate("frmCadastroEmpresa", "Inscrição Municipal", None))
        self.txtTipoEmpresa.setToolTip(_translate("frmCadastroEmpresa", "Tipo de Empresa", None))
        self.txtTipoEmpresa.setWhatsThis(_translate("frmCadastroEmpresa", "Campo de escolha qual é  o tipo da empresa", None))
        self.lblEndereco.setText(_translate("frmCadastroEmpresa", "Endereço", None))
        self.txtComplemento.setToolTip(_translate("frmCadastroEmpresa", "Complemento", None))
        self.txtComplemento.setWhatsThis(_translate("frmCadastroEmpresa", "Campo complementar do endereço", None))
        self.txtEstados.setToolTip(_translate("frmCadastroEmpresa", "Estado", None))
        self.txtEstados.setWhatsThis(_translate("frmCadastroEmpresa", "Campo do nome do estado de localização do endereço", None))
        self.txtNumero.setToolTip(_translate("frmCadastroEmpresa", "Numero", None))
        self.txtNumero.setWhatsThis(_translate("frmCadastroEmpresa", "Campo de numero referente ao numero do endereço", None))
        self.lblNomeFantasia.setText(_translate("frmCadastroEmpresa", "Nome Fantasia", None))
        self.txtBairro.setToolTip(_translate("frmCadastroEmpresa", "Bairro", None))
        self.txtBairro.setWhatsThis(_translate("frmCadastroEmpresa", "Campo do nome do bairro referente ao endereço", None))
        self.txtInscricaoEstadua.setToolTip(_translate("frmCadastroEmpresa", "Inscrição Estadual", None))
        self.txtInscricaoEstadua.setWhatsThis(_translate("frmCadastroEmpresa", "Campo do numero do inscrição estadual da empresa", None))
        self.lblTelefoene.setText(_translate("frmCadastroEmpresa", "Telefone", None))
        self.lblNumero.setText(_translate("frmCadastroEmpresa", "Numero", None))
        self.txtEndereco.setToolTip(_translate("frmCadastroEmpresa", "Endereço", None))
        self.txtEndereco.setWhatsThis(_translate("frmCadastroEmpresa", "Campo de descrição do endereço", None))
        self.txtFantasia.setToolTip(_translate("frmCadastroEmpresa", "Nome Fantasia", None))
        self.txtFantasia.setWhatsThis(_translate("frmCadastroEmpresa", "Campo do nome fantasia da empresa", None))
        self.lblCidades.setText(_translate("frmCadastroEmpresa", "Cidade", None))
        self.lblEstados.setText(_translate("frmCadastroEmpresa", "Estado", None))
        self.lblInscricaoEstadual.setText(_translate("frmCadastroEmpresa", "Incrição Estadual", None))
        self.txtId.setToolTip(_translate("frmCadastroEmpresa", "Codigo", None))
        self.txtId.setWhatsThis(_translate("frmCadastroEmpresa", "Campo do codigo de identificação da empresa", None))
        self.lblCodigo.setText(_translate("frmCadastroEmpresa", "Codigo", None))
        self.txtSite.setToolTip(_translate("frmCadastroEmpresa", "Site", None))
        self.txtSite.setWhatsThis(_translate("frmCadastroEmpresa", "Campo endereço do site", None))
        self.lblSite.setText(_translate("frmCadastroEmpresa", "Site", None))
        self.ckBoOperacional.setText(_translate("frmCadastroEmpresa", "Operacional", None))
        self.txtPesquisa.setToolTip(_translate("frmCadastroEmpresa", "Pesquisa", None))
        self.txtPesquisa.setWhatsThis(_translate("frmCadastroEmpresa", "Campo pra inserir dados da pesquisa", None))
        self.tbPesquisa.setToolTip(_translate("frmCadastroEmpresa", "Tabela de Pesquisa", None))
        self.tbPesquisa.setWhatsThis(_translate("frmCadastroEmpresa", "Campo com as informações da pesquisa", None))
        self.grbDadosPesquisa.setTitle(_translate("frmCadastroEmpresa", "Dados Pesquisa", None))
        self.radBtnCodigo.setText(_translate("frmCadastroEmpresa", "Codigo", None))
        self.radBtnFantasia.setText(_translate("frmCadastroEmpresa", "Fantasia", None))
        self.radBtnRazaoSocial.setText(_translate("frmCadastroEmpresa", "Razão Social", None))
        self.radBtnCnpj.setText(_translate("frmCadastroEmpresa", "CNPJ", None))
        self.radBtnInsEstadual.setText(_translate("frmCadastroEmpresa", "Ins. Esta.", None))
        self.btnLimparPesquisa.setText(_translate("frmCadastroEmpresa", "Limpar Pesquisa", None))

