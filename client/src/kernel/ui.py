#-*- coding: utf-8 -*-

from PyQt4 import QtCore

from kernel import abstract
from kernel import wrapper

##################################

class PyMainWindow(abstract.QWindow):

	def refresh(self):
		wrapper.refresh_view(self)

	#
	@QtCore.pyqtSlot()
	def on_Error(self):
		self.parent._exit()


	# putButton

	@QtCore.pyqtSlot()
	def on_putButton_clicked(self):
		wrapper.put_start(self)

	@QtCore.pyqtSignature('PyQt_PyObject')
	def on_putButton_respond(self, data=None):
		wrapper.put_respond(self, data)

	# addButton

	@QtCore.pyqtSlot()
	def on_addButton_clicked(self):
		wrapper.add_parameter(self)

	# delButton

	@QtCore.pyqtSlot()
	def on_delButton_clicked(self):
		self.parametersTable.removeRow(self.parametersTable.currentRow())

	# actionDrop menu item

	@QtCore.pyqtSlot()
	def on_actionDrop_triggered(self):
		wrapper.truncate_tables(self)
		wrapper.prepare_main_form(self)

	# ComponentButton

	@QtCore.pyqtSlot()
	def on_component_button_clicked(self):
		print 'component wizard'

	# SymbolButton

	@QtCore.pyqtSlot()
	def on_symbol_button_clicked(self):
		dialog = PackageWizard('ui/symbol.ui', self)
		dialog.init()
		dialog.show()


	# PackageButton

	@QtCore.pyqtSlot()
	def on_package_button_clicked(self):
		dialog = PackageWizard('ui/package.ui', self)
		dialog.init()
		dialog.show()


	# ModelButton

	@QtCore.pyqtSlot()
	def on_model_button_clicked(self):
		dialog = PackageWizard('ui/model.ui', self)
		dialog.init()
		dialog.show()


	# exportButton

	@QtCore.pyqtSlot()
	def on_export_button_clicked(self):
		wrapper.sync(self)



	@QtCore.pyqtSignature('PyQt_PyObject')
	def on_exportButton_respond(self, data=None):
		wrapper.export_respond(self, data)

	# downloadButton

	@QtCore.pyqtSlot()
	def on_downloadButton_clicked(self):
		wrapper.download_start(self)

	@QtCore.pyqtSignature('PyQt_PyObject')
	def on_downloadButton_respond(self, data=None):
		wrapper.download_respond(self, data)

	# uploadButton

	@QtCore.pyqtSlot()
	def on_uploadButton_clicked(self):
		wrapper.upload_start(self)

	@QtCore.pyqtSignature('PyQt_PyObject')
	def on_uploadButton_respond(self, data=None):
		wrapper.upload_respond(self, data)




class PackageWizard(abstract.QDialog):

	def init(self):
		self.worker = wrapper.PackageWorker()
		self.worker.load()

	# okButton

	@QtCore.pyqtSlot()
	def accepted(self):
		print 'OK'

	@QtCore.pyqtSignature('PyQt_PyObject')
	def on_rejected(self, data=None):
		print 'Cancel'
