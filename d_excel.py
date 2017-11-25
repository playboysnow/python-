# -*- coding:utf-8 -*-
import xlrd
import unittest
import ddt

class D_excel(object):
	
	def __init__(self,path):
		self.data=xlrd.open_workbook(path)
		self.sheet=self.data.sheet_by_index(sheetx=0)
		# title 
		#self.title=self.sheet.row_values(0)
		# row clo num
		self.nrow=self.sheet.nrows
		self.nclo=self.sheet.ncols
		self.curRow=1
		# 
		#for i in range(1,self.nrows):
			
		#	self.row=self.sheet.row_values(i)
			
			
	def next(self):
		data=[]
		dict_data=[]
		while self.hasNext():
			for i in range(0,self.nrow):
				data.append(self.sheet.row_values(i))#循环获取行元素
			
			for i in range(1,len(data)):
				temp=dict(zip(data[0],data[i]))#循环将行元素与title 合并成字典
				dict_data.append(temp)
				self.curRow+=1
		return dict_data

	def hasNext(self):#判断表是否结束
		if self.nrow !=0 and self.nrow > self.curRow:
			return True
		else:
			return False
		
		
