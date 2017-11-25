# -*- coding:utf-8 -*-
import sys,socket,requests,urllib,urllib2
import re,json
#import qrcode,PIL
from urlparse import urlparse
# Import Qt GUI component
from PySide.QtGui import *
import xlrd,xlwt
import unittest,ddt
# Import GUI File
from demo import Ui_FKAPI
from MakeMd5 import Md5
from d_excel import D_excel

reload(sys)
sys.setdefaultencoding('gb2312')
class  MainWindow(QMainWindow,Ui_FKAPI):
	
	def  __init__(self,parent=None):
		super(MainWindow,self).__init__(parent)
		self.setupUi(self)
		self.pushButton_4.clicked.connect(self.run_once)
		self.pushButton_2.clicked.connect(self.checknetwork)
		self.pushButton_3.clicked.connect(self.run_file)
		self.pushButton.clicked.connect(self.findfile)
	def cc(self):
		pass
	def checkmd5(self):#check checkbox
			pass
	def check_md5(self):#check sign by self
		Y=self.checkBox.isChecked()
		if Y:
			MD5=Md5().Mkmd5
		else:
			MD5=Md5().md5
		return MD5
	def run_once(self):#API just once
		MD5=self.check_md5()  #get md5
		'''Y = self.checkBox.isChecked()
		if Y:
			MD5 = Md5().Mkmd5
		else:
			MD5 = Md5().md5
		'''
		url=self.lineEdit_1.text()
		method_txt=self.comboBox.currentText()
		ssl=self.checkBox_11.isChecked()
		if ssl:
			varify=True
		else:
			varify=False
		#varify_txt=self.comboBox_1.currentText()
		if method_txt=="GET":
			method=requests.get
		elif method_txt=="POST":
			method=requests.post
		elif method_txt == "UPDATE":
			method = requests.update
		elif method_txt=="HEAD":
			method=requests.head
		elif method_txt=="DELETE":
			method=requests.delete
		argv1=self.lineEdit_3.text()
		argv1_1 = self.lineEdit_6.text()
		argv2=self.lineEdit_4.text()
		argv2_2=self.lineEdit_5.text()
		argv3=self.lineEdit_7.text()
		argv3_3=self.lineEdit_8.text()
		argv4=self.lineEdit_9.text()
		argv4_4=self.lineEdit_10.text()
		argv5=self.lineEdit_11.text()
		argv5_5=self.lineEdit_12.text()
		argv6=self.lineEdit_13.text()
		argv6_6=self.lineEdit_14.text()
		argv7=self.lineEdit_15.text()
		argv7_7=self.lineEdit_16.text()
		argv8=self.lineEdit_17.text()
		argv8_8=self.lineEdit_18.text()
		argv9=self.lineEdit_19.text()
		argv9_9=self.lineEdit_20.text()
		payload={
			argv1:argv1_1,
			argv2: argv2_2,
			argv3: argv3_3,
			argv4: argv4_4,
			argv5: argv5_5,
			argv6: argv6_6,
			argv7: argv7_7,
			argv8: argv8_8,
			argv9: argv9_9,

		}

		request_txt=self.textEdit.toPlainText()
		print request_txt
		if request_txt:
			#request_tt=json.dumps(request_txt)
			request_tt=eval(request_txt)
			print request_tt
			#print request_tt.get('userName')

		try:
			global req
			if request_txt:
				req=method(url,data=request_tt,verify=varify)
			else:
				req=method(url,data=payload,verify=varify)
		except:
			tt="ERROR 1"
			print "ERROR 1" #net error or parm error
			self.textBrowser_2.setText(tt)
		txt=req.text
		self.textBrowser_2.setText(txt)
		print url,method_txt,payload,txt
	def txt2dic(self):
		txt = self.textEdit.toPlainText()
		txt_dic=eval(txt)
		return txt_dic
	def request_text(self):# check text is or not used
		pass
	def findfile(self):#use file
		#dir_path = QFileDialog.getExistingDirectory(self, "choose directory", "C:\Users\Administrator\Desktop")
		#QFileOpenEvent(dir_path)
		file_name = QFileDialog.getOpenFileName(self, "选择文件", "C:\Users\Administrator\Desktop"
											)
		print file_name
		self.lineEdit.setText(file_name[0])
		return file_name[0]
	def run_file(self):
		file_name=self.lineEdit.text()#url method md5 等可以借助其他模块元素 参考run_once
		#print file_name#  deal filetype xls or json
		MD5 = self.check_md5()  # get md5
		url = self.lineEdit_1.text()
		method_txt = self.comboBox.currentText()
		ssl = self.checkBox_11.isChecked()
		if ssl:
			varify = True
		else:
			varify = False
		# varify_txt=self.comboBox_1.currentText()
		if method_txt == "GET":
			method = requests.get
		elif method_txt == "POST":
			method = requests.post
		elif method_txt == "UPDATE":
			method = requests.update
		elif method_txt == "HEAD":
			method = requests.head
		elif method_txt == "DELETE":
			method = requests.delete
		excel=D_excel(file_name)
		#print excel.next()[0] #可以使用eval执行Excel中的MD5函数
		len=excel.nrow-1
		a=excel.next()
		result=[]
		for i in range (0,len):
			print a[i]			#循环读取
			req=method(url,data=a[i],verify=varify)
			a[i]['result']=req.text
			result.append(a[i])
			print result
			return 	 result		#返回响应内容    后续处理签名

	def checknetwork(self):#check network
		a = self.lineEdit_1.text()
		topHostPostfix = (
			'.com', '.la', '.io', '.co', '.info', '.net', '.org', '.me', '.mobi',
			'.us', '.biz', '.xxx', '.ca', '.co.jp', '.com.cn', '.net.cn',
			'.org.cn', '.mx', '.tv', '.ws', '.ag', '.com.ag', '.net.ag',
			'.org.ag', '.am', '.asia', '.at', '.be', '.com.br', '.net.br',
			'.bz', '.com.bz', '.net.bz', '.cc', '.com.co', '.net.co',
			'.nom.co', '.de', '.es', '.com.es', '.nom.es', '.org.es',
			'.eu', '.fm', '.fr', '.gs', '.in', '.co.in', '.firm.in', '.gen.in',
			'.ind.in', '.net.in', '.org.in', '.it', '.jobs', '.jp', '.ms',
			'.com.mx', '.nl', '.nu', '.co.nz', '.net.nz', '.org.nz',
			'.se', '.tc', '.tk', '.tw', '.com.tw', '.idv.tw', '.org.tw',
			'.hk', '.co.uk', '.me.uk', '.org.uk', '.vg', ".com.hk")

		regx = r'[^\.]+(' + '|'.join([h.replace('.', r'\.') for h in topHostPostfix]) + ')$'
		pattern = re.compile(regx, re.IGNORECASE)

		print "--" * 40
		parts = urlparse(a)
		host = parts.netloc
		m = pattern.search(host)
		res = m.group() if m else host
		print "unkown" if not res else res
		ip=socket.gethostbyname(host)
		self.textBrowser_2.setText(ip)
		print ip
	def clear(self):
		self.lineEdit_13.clear()
	def clearargv(self):
		self.lineEdit_3.clear()
		self.lineEdit_4.clear()
		self.lineEdit_5.clear()
		self.lineEdit_6.clear()
		self.lineEdit_7.clear()
		self.lineEdit_8.clear()
		self.lineEdit_9.clear()
		self.lineEdit_10.clear()
		self.lineEdit_11.clear()
		self.lineEdit_12.clear()



if __name__=='__main__':
	Program = QApplication(sys.argv)
	Window=MainWindow()
	Window.show()
	Program.exec_()