import numpy as np
import pandas as pd
import sklearn
import sklearn.tree
from sklearn.base import BaseEstimator,TransformerMixin
import copy
from abc import ABCMeta,abstractmethod
import warnings

class BaseDiscretizer(BaseEstimator,TransformerMixin):
	"""
	抽象类，用户自定义扩展变量离散化方法。
	必有的属性：
	feature_names:需要离散化的变量列表，非负整数或者字符串
	fill_na : 对于缺失值指定特殊类别
	return_numeric ： True返回数值类别，False返回字符串类别
	dicimal：字符串类别中保存的小数保留位
	cuts：若fit的X为一维数组或者Series，cut的分割点为一维数组（表示只有单一变量）
			若fit的X为二维数组或者Dataframe，cuts为字典。（键为变量名，值为分割点的一维数组）
	"""
	__metaclass__ = ABCMeta

	def __init__(self,feature_names = None, fill_na = -1,return_numeric = True,return_array = False,decimal  = 2):
		self.feature_names = feature_names
		self.fill_na = fill_na
		self.return_numeric = return_numeric
		self.return_array = return_array
		self.decimal = decimal

	@abstractmethod
	def fit(self, X,y= None) :
		"""
		对于feature_names中的变量获取各自离散化分割点。
		X: 一维或二维数组，或者Dataframe或Series
		y: 一维数组，或Series。
		"""
		pass

	def Transform(self,X):
		"""
		离散化数据，数值为0到n-1，对于缺失值会增加类别-1.
		X：一维或二维数组，或DataFrame 或者Series
		返回离散化后的数据，一维或二维数组，或Dataframe，或Series
		"""
		data = X.copy()
		if isinstance(data,np.array):
			if isinstance(self.fill_na,str):
				raise Exception('numpy数组缺失值只能设置成数值！')
			if not self.return_numeric:
				warnings.warn('numpy数组只能返回数值编码，若想返回字符串编码，请输入dataframe或series！')
		if not self.return_numeric:
			newlabel = self.get_label()
		if len(data.shape) == 1:
			tmp = np.searchsorted(self.cuts,data).astype(int)
			result = np.where(np.isnan(data,-1,tmp))