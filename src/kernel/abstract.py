#-*- coding: utf-8 -*-

from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4 import uic

##################################

### abstract classes ###

class QWindow(QtGui.QMainWindow):

	def __init__(self, interface, *args):
		super(QWindow, self).__init__(*args)
		uic.loadUi(interface, self)

		self.inifile = 'pyclient.ini'
		self.settings = None

		self.dbname = 'data/pyclient.db'




class QWorker(QtCore.QThread):

	def __init__(self, parent, callable, *args, **kwargs):
		QtCore.QThread.__init__(self, parent)
		self.callable = callable
		self.args = args
		self.kwargs = kwargs
		self.result = None

	def run(self):
#		try:
			self.result = self.callable(self, *self.args, **self.kwargs)

#		except Exception, e:
#			print e
#			self.emit(QtCore.SIGNAL("exception(PyQt_PyObject)"), e)

#		else:
			self.emit(QtCore.SIGNAL("exit(PyQt_PyObject)"), self.result)

	def iter(self, num=None):
		pass

	def __on_start(self, callable):
		print 'Qworker started'

	def __on_stop(self, callable):
		print 'Qworker stopped'

	def __del__(self):
		self.emit(QtCore.SIGNAL("exit(PyQt_PyObject)"), self.result)

################################
