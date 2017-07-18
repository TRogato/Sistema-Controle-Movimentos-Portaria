import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from telas.frmMainHouse import Ui_frmMainHouse
from .classEmpresa import Empresa
app = QtGui.QApplication(sys.argv)

class Principal(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_frmMainHouse()
        self.ui.setupUi(self)



        self.ui.subMenuCadastroEmpresa.triggered.connect(self.cadastroEmpresa)


    def cadastroEmpresa(self):
        app = Empresa()
        app.show()
        sys.exit(app.exec_())