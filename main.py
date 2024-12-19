import json
import time
from matplotlib import pyplot
import math
import numpy as np

# Игнорирование ошибок tensorflow
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

from tensorflow import keras
from tensorflow.keras.layers import Dense, Flatten, Dropout, concatenate, Input, Reshape, Conv2D, MaxPool2D, UpSampling2D, BatchNormalization

from keras.models import Sequential
from keras.utils import plot_model

# Получаем массивы из картинок
import cv2
from PIL import Image

class DataSet(object):
    def __init__ (self, filename, visibleExamples=0):
        self.filename = filename
        self.data = []
        with open(self.filename, "r") as read_file:
            self.data = np.asarray(json.load(read_file)) # 2270
        ''' Выводим 3 строки датасета, для наглядности '''
        if (visibleExamples>0):
            print("Examples from dataset" + filename)
        for i in range(visibleExamples):
            print(str(i) + ": " + str(self.data[i]))

        ''' Определяем количество данных '''
        self.packetCount = len(self.data)
        print("All count: " + str(self.packetCount))


# Функция генерации тренировочного набора данных
def getTrainDataSet(count = 500, RxTxLabel='ff'):
  XMass=[]
  YMass=[]
  AMass=[]
  for i in range(count):
    if RxTxLabel=='ff':

          XMass.append(amplffDS1.data[i])
          XMass.append(amplffDS2.data[i])
          XMass.append(amplffDS3.data[i])
          XMass.append(amplffDS4.data[i])
          XMass.append(amplffDS5.data[i])
          XMass.append(amplffDS6.data[i])
          XMass.append(amplffDS7.data[i])
          XMass.append(amplffDS8.data[i])
          XMass.append(amplffDS9.data[i])
          XMass.append(amplffDS10.data[i])



          AMass.append(phffDS1.data[i])
          AMass.append(phffDS2.data[i])
          AMass.append(phffDS3.data[i])
          AMass.append(phffDS4.data[i])
          AMass.append(phffDS5.data[i])
          AMass.append(phffDS6.data[i])
          AMass.append(phffDS7.data[i])
          AMass.append(phffDS8.data[i])
          AMass.append(phffDS9.data[i])
          AMass.append(phffDS10.data[i])



          YMass.append(image2arr1)
          YMass.append(image2arr2)
          YMass.append(image2arr3)
          YMass.append(image2arr4)
          YMass.append(image2arr5)
          YMass.append(image2arr6)
          YMass.append(image2arr7)
          YMass.append(image2arr8)
          YMass.append(image2arr9)
          YMass.append(image2arr10)



    if RxTxLabel=='fs':


          XMass.append(amplfsDS1.data[i])
          XMass.append(amplfsDS2.data[i])
          XMass.append(amplfsDS3.data[i])
          XMass.append(amplfsDS4.data[i])
          XMass.append(amplfsDS5.data[i])
          XMass.append(amplfsDS6.data[i])
          XMass.append(amplfsDS7.data[i])
          XMass.append(amplfsDS8.data[i])
          XMass.append(amplfsDS9.data[i])
          XMass.append(amplfsDS10.data[i])



          AMass.append(phfsDS1.data[i])
          AMass.append(phfsDS2.data[i])
          AMass.append(phfsDS3.data[i])
          AMass.append(phfsDS4.data[i])
          AMass.append(phfsDS5.data[i])
          AMass.append(phfsDS6.data[i])
          AMass.append(phfsDS7.data[i])
          AMass.append(phfsDS8.data[i])
          AMass.append(phfsDS9.data[i])
          AMass.append(phfsDS10.data[i])



          YMass.append(image2arr1)
          YMass.append(image2arr2)
          YMass.append(image2arr3)
          YMass.append(image2arr4)
          YMass.append(image2arr5)
          YMass.append(image2arr6)
          YMass.append(image2arr7)
          YMass.append(image2arr8)
          YMass.append(image2arr9)
          YMass.append(image2arr10)

    if RxTxLabel=='ft':


          XMass.append(amplftDS1.data[i])
          XMass.append(amplftDS2.data[i])
          XMass.append(amplftDS3.data[i])
          XMass.append(amplftDS4.data[i])
          XMass.append(amplftDS5.data[i])
          XMass.append(amplftDS6.data[i])
          XMass.append(amplftDS7.data[i])
          XMass.append(amplftDS8.data[i])
          XMass.append(amplftDS9.data[i])
          XMass.append(amplftDS10.data[i])



          AMass.append(phftDS1.data[i])
          AMass.append(phftDS2.data[i])
          AMass.append(phftDS3.data[i])
          AMass.append(phftDS4.data[i])
          AMass.append(phftDS5.data[i])
          AMass.append(phftDS6.data[i])
          AMass.append(phftDS7.data[i])
          AMass.append(phftDS8.data[i])
          AMass.append(phftDS9.data[i])
          AMass.append(phftDS10.data[i])



          YMass.append(image2arr1)
          YMass.append(image2arr2)
          YMass.append(image2arr3)
          YMass.append(image2arr4)
          YMass.append(image2arr5)
          YMass.append(image2arr6)
          YMass.append(image2arr7)
          YMass.append(image2arr8)
          YMass.append(image2arr9)
          YMass.append(image2arr10)



    if RxTxLabel=='st':



          XMass.append(amplstDS1.data[i])
          XMass.append(amplstDS2.data[i])
          XMass.append(amplstDS3.data[i])
          XMass.append(amplstDS4.data[i])
          XMass.append(amplstDS5.data[i])
          XMass.append(amplstDS6.data[i])
          XMass.append(amplstDS7.data[i])
          XMass.append(amplstDS8.data[i])
          XMass.append(amplstDS9.data[i])
          XMass.append(amplstDS10.data[i])



          AMass.append(phstDS1.data[i])
          AMass.append(phstDS2.data[i])
          AMass.append(phstDS3.data[i])
          AMass.append(phstDS4.data[i])
          AMass.append(phstDS5.data[i])
          AMass.append(phstDS6.data[i])
          AMass.append(phstDS7.data[i])
          AMass.append(phstDS8.data[i])
          AMass.append(phstDS9.data[i])
          AMass.append(phstDS10.data[i])



          YMass.append(image2arr1)
          YMass.append(image2arr2)
          YMass.append(image2arr3)
          YMass.append(image2arr4)
          YMass.append(image2arr5)
          YMass.append(image2arr6)
          YMass.append(image2arr7)
          YMass.append(image2arr8)
          YMass.append(image2arr9)
          YMass.append(image2arr10)




    if RxTxLabel=='ss':



          XMass.append(amplssDS1.data[i])
          XMass.append(amplssDS2.data[i])
          XMass.append(amplssDS3.data[i])
          XMass.append(amplssDS4.data[i])
          XMass.append(amplssDS5.data[i])
          XMass.append(amplssDS6.data[i])
          XMass.append(amplssDS7.data[i])
          XMass.append(amplssDS8.data[i])
          XMass.append(amplssDS9.data[i])
          XMass.append(amplssDS10.data[i])



          AMass.append(phssDS1.data[i])
          AMass.append(phssDS2.data[i])
          AMass.append(phssDS3.data[i])
          AMass.append(phssDS4.data[i])
          AMass.append(phssDS5.data[i])
          AMass.append(phssDS6.data[i])
          AMass.append(phssDS7.data[i])
          AMass.append(phssDS8.data[i])
          AMass.append(phssDS9.data[i])
          AMass.append(phssDS10.data[i])



          YMass.append(image2arr1)
          YMass.append(image2arr2)
          YMass.append(image2arr3)
          YMass.append(image2arr4)
          YMass.append(image2arr5)
          YMass.append(image2arr6)
          YMass.append(image2arr7)
          YMass.append(image2arr8)
          YMass.append(image2arr9)
          YMass.append(image2arr10)
    if RxTxLabel=='sf':



          XMass.append(amplsfDS1.data[i])
          XMass.append(amplsfDS2.data[i])
          XMass.append(amplsfDS3.data[i])
          XMass.append(amplsfDS4.data[i])
          XMass.append(amplsfDS5.data[i])
          XMass.append(amplsfDS6.data[i])
          XMass.append(amplsfDS7.data[i])
          XMass.append(amplsfDS8.data[i])
          XMass.append(amplsfDS9.data[i])
          XMass.append(amplsfDS10.data[i])



          AMass.append(phsfDS1.data[i])
          AMass.append(phsfDS2.data[i])
          AMass.append(phsfDS3.data[i])
          AMass.append(phsfDS4.data[i])
          AMass.append(phsfDS5.data[i])
          AMass.append(phsfDS6.data[i])
          AMass.append(phsfDS7.data[i])
          AMass.append(phsfDS8.data[i])
          AMass.append(phsfDS9.data[i])
          AMass.append(phsfDS10.data[i])



          YMass.append(image2arr1)
          YMass.append(image2arr2)
          YMass.append(image2arr3)
          YMass.append(image2arr4)
          YMass.append(image2arr5)
          YMass.append(image2arr6)
          YMass.append(image2arr7)
          YMass.append(image2arr8)
          YMass.append(image2arr9)
          YMass.append(image2arr10)




    if RxTxLabel=='tf':



          XMass.append(ampltfDS1.data[i])
          XMass.append(ampltfDS2.data[i])
          XMass.append(ampltfDS3.data[i])
          XMass.append(ampltfDS4.data[i])
          XMass.append(ampltfDS5.data[i])
          XMass.append(ampltfDS6.data[i])
          XMass.append(ampltfDS7.data[i])
          XMass.append(ampltfDS8.data[i])
          XMass.append(ampltfDS9.data[i])
          XMass.append(ampltfDS10.data[i])



          AMass.append(phtfDS1.data[i])
          AMass.append(phtfDS2.data[i])
          AMass.append(phtfDS3.data[i])
          AMass.append(phtfDS4.data[i])
          AMass.append(phtfDS5.data[i])
          AMass.append(phtfDS6.data[i])
          AMass.append(phtfDS7.data[i])
          AMass.append(phtfDS8.data[i])
          AMass.append(phtfDS9.data[i])
          AMass.append(phtfDS10.data[i])



          YMass.append(image2arr1)
          YMass.append(image2arr2)
          YMass.append(image2arr3)
          YMass.append(image2arr4)
          YMass.append(image2arr5)
          YMass.append(image2arr6)
          YMass.append(image2arr7)
          YMass.append(image2arr8)
          YMass.append(image2arr9)
          YMass.append(image2arr10)

    if RxTxLabel=='ts':



          XMass.append(ampltsDS1.data[i])
          XMass.append(ampltsDS2.data[i])
          XMass.append(ampltsDS3.data[i])
          XMass.append(ampltsDS4.data[i])
          XMass.append(ampltsDS5.data[i])
          XMass.append(ampltsDS6.data[i])
          XMass.append(ampltsDS7.data[i])
          XMass.append(ampltsDS8.data[i])
          XMass.append(ampltsDS9.data[i])
          XMass.append(ampltsDS10.data[i])



          AMass.append(phtsDS1.data[i])
          AMass.append(phtsDS2.data[i])
          AMass.append(phtsDS3.data[i])
          AMass.append(phtsDS4.data[i])
          AMass.append(phtsDS5.data[i])
          AMass.append(phtsDS6.data[i])
          AMass.append(phtsDS7.data[i])
          AMass.append(phtsDS8.data[i])
          AMass.append(phtsDS9.data[i])
          AMass.append(phtsDS10.data[i])



          YMass.append(image2arr1)
          YMass.append(image2arr2)
          YMass.append(image2arr3)
          YMass.append(image2arr4)
          YMass.append(image2arr5)
          YMass.append(image2arr6)
          YMass.append(image2arr7)
          YMass.append(image2arr8)
          YMass.append(image2arr9)
          YMass.append(image2arr10)




    if RxTxLabel=='tt':



          XMass.append(amplttDS1.data[i])
          XMass.append(amplttDS2.data[i])
          XMass.append(amplttDS3.data[i])
          XMass.append(amplttDS4.data[i])
          XMass.append(amplttDS5.data[i])
          XMass.append(amplttDS6.data[i])
          XMass.append(amplttDS7.data[i])
          XMass.append(amplttDS8.data[i])
          XMass.append(amplttDS9.data[i])
          XMass.append(amplttDS10.data[i])



          AMass.append(phttDS1.data[i])
          AMass.append(phttDS2.data[i])
          AMass.append(phttDS3.data[i])
          AMass.append(phttDS4.data[i])
          AMass.append(phttDS5.data[i])
          AMass.append(phttDS6.data[i])
          AMass.append(phttDS7.data[i])
          AMass.append(phttDS8.data[i])
          AMass.append(phttDS9.data[i])
          AMass.append(phttDS10.data[i])



          YMass.append(image2arr1)
          YMass.append(image2arr2)
          YMass.append(image2arr3)
          YMass.append(image2arr4)
          YMass.append(image2arr5)
          YMass.append(image2arr6)
          YMass.append(image2arr7)
          YMass.append(image2arr8)
          YMass.append(image2arr9)
          YMass.append(image2arr10)
      # Преобразуем в массив numPy

  print(np.asarray(XMass).shape)
  print(np.asarray(AMass).shape)
  print(np.asarray(YMass).shape)
  #trainDataSet_X = np.array([xi+[None]*(56-len(xi)) for xi in XMass])
  #trainDataSet_A = np.array([xi+[None]*(56-len(xi)) for xi in AMass])
  #trainDataSet_Y = np.array([yi for yi in YMass])
  # Перемешаем для верности
  # trainDataSet = utils.shuffle(trainDataSet)
  return(np.asarray(XMass).T, np.asarray(YMass), np.asarray(AMass).T)
  #return(trainDataSet_X, trainDataSet_Y, trainDataSet_A)

# Функция генерации тестового набора данных
def getTestDataSet(frm = 500, count = 100, RxTxLabel='ff'):
  XMass=[]
  YMass=[]
  AMass=[]
  for i in range(frm, frm+count):
        if RxTxLabel=='ff':

          XMass.append(amplffDS1.data[i])
          XMass.append(amplffDS2.data[i])
          XMass.append(amplffDS3.data[i])
          XMass.append(amplffDS4.data[i])
          XMass.append(amplffDS5.data[i])
          XMass.append(amplffDS6.data[i])
          XMass.append(amplffDS7.data[i])
          XMass.append(amplffDS8.data[i])
          XMass.append(amplffDS9.data[i])
          XMass.append(amplffDS10.data[i])



          AMass.append(phffDS1.data[i])
          AMass.append(phffDS2.data[i])
          AMass.append(phffDS3.data[i])
          AMass.append(phffDS4.data[i])
          AMass.append(phffDS5.data[i])
          AMass.append(phffDS6.data[i])
          AMass.append(phffDS7.data[i])
          AMass.append(phffDS8.data[i])
          AMass.append(phffDS9.data[i])
          AMass.append(phffDS10.data[i])



          YMass.append(image2arr1)
          YMass.append(image2arr2)
          YMass.append(image2arr3)
          YMass.append(image2arr4)
          YMass.append(image2arr5)
          YMass.append(image2arr6)
          YMass.append(image2arr7)
          YMass.append(image2arr8)
          YMass.append(image2arr9)
          YMass.append(image2arr10)



        if RxTxLabel=='fs':


          XMass.append(amplfsDS1.data[i])
          XMass.append(amplfsDS2.data[i])
          XMass.append(amplfsDS3.data[i])
          XMass.append(amplfsDS4.data[i])
          XMass.append(amplfsDS5.data[i])
          XMass.append(amplfsDS6.data[i])
          XMass.append(amplfsDS7.data[i])
          XMass.append(amplfsDS8.data[i])
          XMass.append(amplfsDS9.data[i])
          XMass.append(amplfsDS10.data[i])



          AMass.append(phfsDS1.data[i])
          AMass.append(phfsDS2.data[i])
          AMass.append(phfsDS3.data[i])
          AMass.append(phfsDS4.data[i])
          AMass.append(phfsDS5.data[i])
          AMass.append(phfsDS6.data[i])
          AMass.append(phfsDS7.data[i])
          AMass.append(phfsDS8.data[i])
          AMass.append(phfsDS9.data[i])
          AMass.append(phfsDS10.data[i])



          YMass.append(image2arr1)
          YMass.append(image2arr2)
          YMass.append(image2arr3)
          YMass.append(image2arr4)
          YMass.append(image2arr5)
          YMass.append(image2arr6)
          YMass.append(image2arr7)
          YMass.append(image2arr8)
          YMass.append(image2arr9)
          YMass.append(image2arr10)

        if RxTxLabel=='ft':


          XMass.append(amplftDS1.data[i])
          XMass.append(amplftDS2.data[i])
          XMass.append(amplftDS3.data[i])
          XMass.append(amplftDS4.data[i])
          XMass.append(amplftDS5.data[i])
          XMass.append(amplftDS6.data[i])
          XMass.append(amplftDS7.data[i])
          XMass.append(amplftDS8.data[i])
          XMass.append(amplftDS9.data[i])
          XMass.append(amplftDS10.data[i])



          AMass.append(phftDS1.data[i])
          AMass.append(phftDS2.data[i])
          AMass.append(phftDS3.data[i])
          AMass.append(phftDS4.data[i])
          AMass.append(phftDS5.data[i])
          AMass.append(phftDS6.data[i])
          AMass.append(phftDS7.data[i])
          AMass.append(phftDS8.data[i])
          AMass.append(phftDS9.data[i])
          AMass.append(phftDS10.data[i])



          YMass.append(image2arr1)
          YMass.append(image2arr2)
          YMass.append(image2arr3)
          YMass.append(image2arr4)
          YMass.append(image2arr5)
          YMass.append(image2arr6)
          YMass.append(image2arr7)
          YMass.append(image2arr8)
          YMass.append(image2arr9)
          YMass.append(image2arr10)



        if RxTxLabel=='st':



          XMass.append(amplstDS1.data[i])
          XMass.append(amplstDS2.data[i])
          XMass.append(amplstDS3.data[i])
          XMass.append(amplstDS4.data[i])
          XMass.append(amplstDS5.data[i])
          XMass.append(amplstDS6.data[i])
          XMass.append(amplstDS7.data[i])
          XMass.append(amplstDS8.data[i])
          XMass.append(amplstDS9.data[i])
          XMass.append(amplstDS10.data[i])



          AMass.append(phstDS1.data[i])
          AMass.append(phstDS2.data[i])
          AMass.append(phstDS3.data[i])
          AMass.append(phstDS4.data[i])
          AMass.append(phstDS5.data[i])
          AMass.append(phstDS6.data[i])
          AMass.append(phstDS7.data[i])
          AMass.append(phstDS8.data[i])
          AMass.append(phstDS9.data[i])
          AMass.append(phstDS10.data[i])



          YMass.append(image2arr1)
          YMass.append(image2arr2)
          YMass.append(image2arr3)
          YMass.append(image2arr4)
          YMass.append(image2arr5)
          YMass.append(image2arr6)
          YMass.append(image2arr7)
          YMass.append(image2arr8)
          YMass.append(image2arr9)
          YMass.append(image2arr10)




        if RxTxLabel=='ss':



          XMass.append(amplssDS1.data[i])
          XMass.append(amplssDS2.data[i])
          XMass.append(amplssDS3.data[i])
          XMass.append(amplssDS4.data[i])
          XMass.append(amplssDS5.data[i])
          XMass.append(amplssDS6.data[i])
          XMass.append(amplssDS7.data[i])
          XMass.append(amplssDS8.data[i])
          XMass.append(amplssDS9.data[i])
          XMass.append(amplssDS10.data[i])



          AMass.append(phssDS1.data[i])
          AMass.append(phssDS2.data[i])
          AMass.append(phssDS3.data[i])
          AMass.append(phssDS4.data[i])
          AMass.append(phssDS5.data[i])
          AMass.append(phssDS6.data[i])
          AMass.append(phssDS7.data[i])
          AMass.append(phssDS8.data[i])
          AMass.append(phssDS9.data[i])
          AMass.append(phssDS10.data[i])



          YMass.append(image2arr1)
          YMass.append(image2arr2)
          YMass.append(image2arr3)
          YMass.append(image2arr4)
          YMass.append(image2arr5)
          YMass.append(image2arr6)
          YMass.append(image2arr7)
          YMass.append(image2arr8)
          YMass.append(image2arr9)
          YMass.append(image2arr10)
        if RxTxLabel=='sf':



          XMass.append(amplsfDS1.data[i])
          XMass.append(amplsfDS2.data[i])
          XMass.append(amplsfDS3.data[i])
          XMass.append(amplsfDS4.data[i])
          XMass.append(amplsfDS5.data[i])
          XMass.append(amplsfDS6.data[i])
          XMass.append(amplsfDS7.data[i])
          XMass.append(amplsfDS8.data[i])
          XMass.append(amplsfDS9.data[i])
          XMass.append(amplsfDS10.data[i])



          AMass.append(phsfDS1.data[i])
          AMass.append(phsfDS2.data[i])
          AMass.append(phsfDS3.data[i])
          AMass.append(phsfDS4.data[i])
          AMass.append(phsfDS5.data[i])
          AMass.append(phsfDS6.data[i])
          AMass.append(phsfDS7.data[i])
          AMass.append(phsfDS8.data[i])
          AMass.append(phsfDS9.data[i])
          AMass.append(phsfDS10.data[i])



          YMass.append(image2arr1)
          YMass.append(image2arr2)
          YMass.append(image2arr3)
          YMass.append(image2arr4)
          YMass.append(image2arr5)
          YMass.append(image2arr6)
          YMass.append(image2arr7)
          YMass.append(image2arr8)
          YMass.append(image2arr9)
          YMass.append(image2arr10)




        if RxTxLabel=='tf':



          XMass.append(ampltfDS1.data[i])
          XMass.append(ampltfDS2.data[i])
          XMass.append(ampltfDS3.data[i])
          XMass.append(ampltfDS4.data[i])
          XMass.append(ampltfDS5.data[i])
          XMass.append(ampltfDS6.data[i])
          XMass.append(ampltfDS7.data[i])
          XMass.append(ampltfDS8.data[i])
          XMass.append(ampltfDS9.data[i])
          XMass.append(ampltfDS10.data[i])



          AMass.append(phtfDS1.data[i])
          AMass.append(phtfDS2.data[i])
          AMass.append(phtfDS3.data[i])
          AMass.append(phtfDS4.data[i])
          AMass.append(phtfDS5.data[i])
          AMass.append(phtfDS6.data[i])
          AMass.append(phtfDS7.data[i])
          AMass.append(phtfDS8.data[i])
          AMass.append(phtfDS9.data[i])
          AMass.append(phtfDS10.data[i])



          YMass.append(image2arr1)
          YMass.append(image2arr2)
          YMass.append(image2arr3)
          YMass.append(image2arr4)
          YMass.append(image2arr5)
          YMass.append(image2arr6)
          YMass.append(image2arr7)
          YMass.append(image2arr8)
          YMass.append(image2arr9)
          YMass.append(image2arr10)

        if RxTxLabel=='ts':



          XMass.append(ampltsDS1.data[i])
          XMass.append(ampltsDS2.data[i])
          XMass.append(ampltsDS3.data[i])
          XMass.append(ampltsDS4.data[i])
          XMass.append(ampltsDS5.data[i])
          XMass.append(ampltsDS6.data[i])
          XMass.append(ampltsDS7.data[i])
          XMass.append(ampltsDS8.data[i])
          XMass.append(ampltsDS9.data[i])
          XMass.append(ampltsDS10.data[i])



          AMass.append(phtsDS1.data[i])
          AMass.append(phtsDS2.data[i])
          AMass.append(phtsDS3.data[i])
          AMass.append(phtsDS4.data[i])
          AMass.append(phtsDS5.data[i])
          AMass.append(phtsDS6.data[i])
          AMass.append(phtsDS7.data[i])
          AMass.append(phtsDS8.data[i])
          AMass.append(phtsDS9.data[i])
          AMass.append(phtsDS10.data[i])



          YMass.append(image2arr1)
          YMass.append(image2arr2)
          YMass.append(image2arr3)
          YMass.append(image2arr4)
          YMass.append(image2arr5)
          YMass.append(image2arr6)
          YMass.append(image2arr7)
          YMass.append(image2arr8)
          YMass.append(image2arr9)
          YMass.append(image2arr10)




        if RxTxLabel=='tt':



          XMass.append(amplttDS1.data[i])
          XMass.append(amplttDS2.data[i])
          XMass.append(amplttDS3.data[i])
          XMass.append(amplttDS4.data[i])
          XMass.append(amplttDS5.data[i])
          XMass.append(amplttDS6.data[i])
          XMass.append(amplttDS7.data[i])
          XMass.append(amplttDS8.data[i])
          XMass.append(amplttDS9.data[i])
          XMass.append(amplttDS10.data[i])



          AMass.append(phttDS1.data[i])
          AMass.append(phttDS2.data[i])
          AMass.append(phttDS3.data[i])
          AMass.append(phttDS4.data[i])
          AMass.append(phttDS5.data[i])
          AMass.append(phttDS6.data[i])
          AMass.append(phttDS7.data[i])
          AMass.append(phttDS8.data[i])
          AMass.append(phttDS9.data[i])
          AMass.append(phttDS10.data[i])



          YMass.append(image2arr1)
          YMass.append(image2arr2)
          YMass.append(image2arr3)
          YMass.append(image2arr4)
          YMass.append(image2arr5)
          YMass.append(image2arr6)
          YMass.append(image2arr7)
          YMass.append(image2arr8)
          YMass.append(image2arr9)
          YMass.append(image2arr10)
      # Преобразуем в массив numPy
  print(np.asarray(XMass).shape)
  print(np.asarray(AMass).shape)
  print(np.asarray(YMass).shape)

  #testDataSet_X = np.array([xi+[None]*(56-len(xi)) for xi in XMass])
  #testDataSet_A = np.array([xi+[None]*(56-len(xi)) for xi in AMass])
  #testDataSet_Y = np.array([yi for yi in YMass])
  # Перемешаем для верности
  # trainDataSet = utils.shuffle(trainDataSet)
  #return(testDataSet_X, testDataSet_Y, testDataSet_A)
  return(np.asarray(XMass).T, np.asarray(YMass), np.asarray(AMass).T)





if __name__ == '__main__':

    # ff phase
    phffDS1 = DataSet("DataSet18.04/Phase/FF/data_class_1_phase_ff.json")
    phffDS2 = DataSet("DataSet18.04/Phase/FF/data_class_2_phase_ff.json")
    phffDS3 = DataSet("DataSet18.04/Phase/FF/data_class_3_phase_ff.json")
    phffDS4 = DataSet("DataSet18.04/Phase/FF/data_class_4_phase_ff.json")
    phffDS5 = DataSet("DataSet18.04/Phase/FF/data_class_5_phase_ff.json")
    phffDS6 = DataSet("DataSet18.04/Phase/FF/data_class_6_phase_ff.json")
    phffDS7 = DataSet("DataSet18.04/Phase/FF/data_class_7_phase_ff.json")
    phffDS8 = DataSet("DataSet18.04/Phase/FF/data_class_8_phase_ff.json")
    phffDS9 = DataSet("DataSet18.04/Phase/FF/data_class_9_phase_ff.json")
    phffDS10 = DataSet("DataSet18.04/Phase/FF/data_class_10_phase_ff.json")
    
    # fs phase
    phfsDS1 = DataSet("DataSet18.04/Phase/FS/data_class_1_phase_fs.json")  # 2270
    phfsDS2 = DataSet("DataSet18.04/Phase/FS/data_class_2_phase_fs.json")  # 2420
    phfsDS3 = DataSet("DataSet18.04/Phase/FS/data_class_3_phase_fs.json")  # 2400
    phfsDS4 = DataSet("DataSet18.04/Phase/FS/data_class_4_phase_fs.json")  # 2509
    phfsDS5 = DataSet("DataSet18.04/Phase/FS/data_class_5_phase_fs.json")  # 2532
    phfsDS6 = DataSet("DataSet18.04/Phase/FS/data_class_6_phase_fs.json")  # 2631
    phfsDS7 = DataSet("DataSet18.04/Phase/FS/data_class_7_phase_fs.json")  # 2388
    phfsDS8 = DataSet("DataSet18.04/Phase/FS/data_class_8_phase_fs.json")  # 2611
    phfsDS9 = DataSet("DataSet18.04/Phase/FS/data_class_9_phase_fs.json")  # 2430
    phfsDS10 = DataSet("DataSet18.04/Phase/FS/data_class_10_phase_fs.json")  # 2562
    
    # ft phase
    phftDS1 = DataSet("DataSet18.04/Phase/FT/data_class_1_phase_ft.json")  # 2270
    phftDS2 = DataSet("DataSet18.04/Phase/FT/data_class_2_phase_ft.json")  # 2420
    phftDS3 = DataSet("DataSet18.04/Phase/FT/data_class_3_phase_ft.json")  # 2400
    phftDS4 = DataSet("DataSet18.04/Phase/FT/data_class_4_phase_ft.json")  # 2509
    phftDS5 = DataSet("DataSet18.04/Phase/FT/data_class_5_phase_ft.json")  # 2532
    phftDS6 = DataSet("DataSet18.04/Phase/FT/data_class_6_phase_ft.json")  # 2631
    phftDS7 = DataSet("DataSet18.04/Phase/FT/data_class_7_phase_ft.json")  # 2388
    phftDS8 = DataSet("DataSet18.04/Phase/FT/data_class_8_phase_ft.json")  # 2611
    phftDS9 = DataSet("DataSet18.04/Phase/FT/data_class_9_phase_ft.json")  # 2430
    phftDS10 = DataSet("DataSet18.04/Phase/FT/data_class_10_phase_ft.json")  # 2562
    
    # sf phase
    phsfDS1 = DataSet("DataSet18.04/Phase/SF/data_class_1_phase_sf.json")  # 2270
    phsfDS2 = DataSet("DataSet18.04/Phase/SF/data_class_2_phase_sf.json")  # 2420
    phsfDS3 = DataSet("DataSet18.04/Phase/SF/data_class_3_phase_sf.json")  # 2400
    phsfDS4 = DataSet("DataSet18.04/Phase/SF/data_class_4_phase_sf.json")  # 2509
    phsfDS5 = DataSet("DataSet18.04/Phase/SF/data_class_5_phase_sf.json")  # 2532
    phsfDS6 = DataSet("DataSet18.04/Phase/SF/data_class_6_phase_sf.json")  # 2631
    phsfDS7 = DataSet("DataSet18.04/Phase/SF/data_class_7_phase_sf.json")  # 2388
    phsfDS8 = DataSet("DataSet18.04/Phase/SF/data_class_8_phase_sf.json")  # 2611
    phsfDS9 = DataSet("DataSet18.04/Phase/SF/data_class_9_phase_sf.json")  # 2430
    phsfDS10 = DataSet("DataSet18.04/Phase/SF/data_class_10_phase_sf.json")  # 2562
    
    # ss phase
    phssDS1 = DataSet("DataSet18.04/Phase/SS/data_class_1_phase_ss.json")  # 2270
    phssDS2 = DataSet("DataSet18.04/Phase/SS/data_class_2_phase_ss.json")  # 2420
    phssDS3 = DataSet("DataSet18.04/Phase/SS/data_class_3_phase_ss.json")  # 2400
    phssDS4 = DataSet("DataSet18.04/Phase/SS/data_class_4_phase_ss.json")  # 2509
    phssDS5 = DataSet("DataSet18.04/Phase/SS/data_class_5_phase_ss.json")  # 2532
    phssDS6 = DataSet("DataSet18.04/Phase/SS/data_class_6_phase_ss.json")  # 2631
    phssDS7 = DataSet("DataSet18.04/Phase/SS/data_class_7_phase_ss.json")  # 2388
    phssDS8 = DataSet("DataSet18.04/Phase/SS/data_class_8_phase_ss.json")  # 2611
    phssDS9 = DataSet("DataSet18.04/Phase/SS/data_class_9_phase_ss.json")  # 2430
    phssDS10 = DataSet("DataSet18.04/Phase/SS/data_class_10_phase_ss.json")  # 2562
    
    # st phase
    phstDS1 = DataSet("DataSet18.04/Phase/ST/data_class_1_phase_st.json")  # 2270
    phstDS2 = DataSet("DataSet18.04/Phase/ST/data_class_2_phase_st.json")  # 2420
    phstDS3 = DataSet("DataSet18.04/Phase/ST/data_class_3_phase_st.json")  # 2400
    phstDS4 = DataSet("DataSet18.04/Phase/ST/data_class_4_phase_st.json")  # 2509
    phstDS5 = DataSet("DataSet18.04/Phase/ST/data_class_5_phase_st.json")  # 2532
    phstDS6 = DataSet("DataSet18.04/Phase/ST/data_class_6_phase_st.json")  # 2631
    phstDS7 = DataSet("DataSet18.04/Phase/ST/data_class_7_phase_st.json")  # 2388
    phstDS8 = DataSet("DataSet18.04/Phase/ST/data_class_8_phase_st.json")  # 2611
    phstDS9 = DataSet("DataSet18.04/Phase/ST/data_class_9_phase_st.json")  # 2430
    phstDS10 = DataSet("DataSet18.04/Phase/ST/data_class_10_phase_st.json")  # 2562

    # tf phase
    phtfDS1 = DataSet("DataSet18.04/Phase/TF/data_class_1_phase_tf.json")  # 2270
    phtfDS2 = DataSet("DataSet18.04/Phase/TF/data_class_2_phase_tf.json")  # 2420
    phtfDS3 = DataSet("DataSet18.04/Phase/TF/data_class_3_phase_tf.json")  # 2400
    phtfDS4 = DataSet("DataSet18.04/Phase/TF/data_class_4_phase_tf.json")  # 2509
    phtfDS5 = DataSet("DataSet18.04/Phase/TF/data_class_5_phase_tf.json")  # 2532
    phtfDS6 = DataSet("DataSet18.04/Phase/TF/data_class_6_phase_tf.json")  # 2631
    phtfDS7 = DataSet("DataSet18.04/Phase/TF/data_class_7_phase_tf.json")  # 2388
    phtfDS8 = DataSet("DataSet18.04/Phase/TF/data_class_8_phase_tf.json")  # 2611
    phtfDS9 = DataSet("DataSet18.04/Phase/TF/data_class_9_phase_tf.json")  # 2430
    phtfDS10 = DataSet("DataSet18.04/Phase/TF/data_class_10_phase_tf.json")  # 2562

    # ts phase
    phtsDS1 = DataSet("DataSet18.04/Phase/TS/data_class_1_phase_ts.json")  # 2270
    phtsDS2 = DataSet("DataSet18.04/Phase/TS/data_class_2_phase_ts.json")  # 2420
    phtsDS3 = DataSet("DataSet18.04/Phase/TS/data_class_3_phase_ts.json")  # 2400
    phtsDS4 = DataSet("DataSet18.04/Phase/TS/data_class_4_phase_ts.json")  # 2509
    phtsDS5 = DataSet("DataSet18.04/Phase/TS/data_class_5_phase_ts.json")  # 2532
    phtsDS6 = DataSet("DataSet18.04/Phase/TS/data_class_6_phase_ts.json")  # 2631
    phtsDS7 = DataSet("DataSet18.04/Phase/TS/data_class_7_phase_ts.json")  # 2388
    phtsDS8 = DataSet("DataSet18.04/Phase/TS/data_class_8_phase_ts.json")  # 2611
    phtsDS9 = DataSet("DataSet18.04/Phase/TS/data_class_9_phase_ts.json")  # 2430
    phtsDS10 = DataSet("DataSet18.04/Phase/TS/data_class_10_phase_ts.json")  # 2562

    # tt phase
    phttDS1 = DataSet("DataSet18.04/Phase/TT/data_class_1_phase_tt.json")  # 2270
    phttDS2 = DataSet("DataSet18.04/Phase/TT/data_class_2_phase_tt.json")  # 2420
    phttDS3 = DataSet("DataSet18.04/Phase/TT/data_class_3_phase_tt.json")  # 2400
    phttDS4 = DataSet("DataSet18.04/Phase/TT/data_class_4_phase_tt.json")  # 2509
    phttDS5 = DataSet("DataSet18.04/Phase/TT/data_class_5_phase_tt.json")  # 2532
    phttDS6 = DataSet("DataSet18.04/Phase/TT/data_class_6_phase_tt.json")  # 2631
    phttDS7 = DataSet("DataSet18.04/Phase/TT/data_class_7_phase_tt.json")  # 2388
    phttDS8 = DataSet("DataSet18.04/Phase/TT/data_class_8_phase_tt.json")  # 2611
    phttDS9 = DataSet("DataSet18.04/Phase/TT/data_class_9_phase_tt.json")  # 2430
    phttDS10 = DataSet("DataSet18.04/Phase/TT/data_class_10_phase_tt.json")  # 2562

    # ff ampl
    amplffDS1 = DataSet("DataSet18.04/Amplituda/FF/data_class_1_ampl_ff.json")  # 2270
    amplffDS2 = DataSet("DataSet18.04/Amplituda/FF/data_class_2_ampl_ff.json")  # 2420
    amplffDS3 = DataSet("DataSet18.04/Amplituda/FF/data_class_3_ampl_ff.json")  # 2400
    amplffDS4 = DataSet("DataSet18.04/Amplituda/FF/data_class_4_ampl_ff.json")  # 2509
    amplffDS5 = DataSet("DataSet18.04/Amplituda/FF/data_class_5_ampl_ff.json")  # 2532
    amplffDS6 = DataSet("DataSet18.04/Amplituda/FF/data_class_6_ampl_ff.json")  # 2631
    amplffDS7 = DataSet("DataSet18.04/Amplituda/FF/data_class_7_ampl_ff.json")  # 2388
    amplffDS8 = DataSet("DataSet18.04/Amplituda/FF/data_class_8_ampl_ff.json")  # 2611
    amplffDS9 = DataSet("DataSet18.04/Amplituda/FF/data_class_9_ampl_ff.json")  # 2430
    amplffDS10 = DataSet("DataSet18.04/Amplituda/FF/data_class_10_ampl_ff.json")  # 2562

    # fs ampl
    amplfsDS1 = DataSet("DataSet18.04/Amplituda/FS/data_class_1_ampl_fs.json")  # 2270
    amplfsDS2 = DataSet("DataSet18.04/Amplituda/FS/data_class_2_ampl_fs.json")  # 2420
    amplfsDS3 = DataSet("DataSet18.04/Amplituda/FS/data_class_3_ampl_fs.json")  # 2400
    amplfsDS4 = DataSet("DataSet18.04/Amplituda/FS/data_class_4_ampl_fs.json")  # 2509
    amplfsDS5 = DataSet("DataSet18.04/Amplituda/FS/data_class_5_ampl_fs.json")  # 2532
    amplfsDS6 = DataSet("DataSet18.04/Amplituda/FS/data_class_6_ampl_fs.json")  # 2631
    amplfsDS7 = DataSet("DataSet18.04/Amplituda/FS/data_class_7_ampl_fs.json")  # 2388
    amplfsDS8 = DataSet("DataSet18.04/Amplituda/FS/data_class_8_ampl_fs.json")  # 2611
    amplfsDS9 = DataSet("DataSet18.04/Amplituda/FS/data_class_9_ampl_fs.json")  # 2430
    amplfsDS10 = DataSet("DataSet18.04/Amplituda/FS/data_class_10_ampl_fs.json")  # 2562

    # ft ampl
    amplftDS1 = DataSet("DataSet18.04/Amplituda/FT/data_class_1_ampl_ft.json")  # 2270
    amplftDS2 = DataSet("DataSet18.04/Amplituda/FT/data_class_2_ampl_ft.json")  # 2420
    amplftDS3 = DataSet("DataSet18.04/Amplituda/FT/data_class_3_ampl_ft.json")  # 2400
    amplftDS4 = DataSet("DataSet18.04/Amplituda/FT/data_class_4_ampl_ft.json")  # 2509
    amplftDS5 = DataSet("DataSet18.04/Amplituda/FT/data_class_5_ampl_ft.json")  # 2532
    amplftDS6 = DataSet("DataSet18.04/Amplituda/FT/data_class_6_ampl_ft.json")  # 2631
    amplftDS7 = DataSet("DataSet18.04/Amplituda/FT/data_class_7_ampl_ft.json")  # 2388
    amplftDS8 = DataSet("DataSet18.04/Amplituda/FT/data_class_8_ampl_ft.json")  # 2611
    amplftDS9 = DataSet("DataSet18.04/Amplituda/FT/data_class_9_ampl_ft.json")  # 2430
    amplftDS10 = DataSet("DataSet18.04/Amplituda/FT/data_class_10_ampl_ft.json")  # 2562

    # sf ampl
    amplsfDS1 = DataSet("DataSet18.04/Amplituda/SF/data_class_1_ampl_sf.json")  # 2270
    amplsfDS2 = DataSet("DataSet18.04/Amplituda/SF/data_class_2_ampl_sf.json")  # 2420
    amplsfDS3 = DataSet("DataSet18.04/Amplituda/SF/data_class_3_ampl_sf.json")  # 2400
    amplsfDS4 = DataSet("DataSet18.04/Amplituda/SF/data_class_4_ampl_sf.json")  # 2509
    amplsfDS5 = DataSet("DataSet18.04/Amplituda/SF/data_class_5_ampl_sf.json")  # 2532
    amplsfDS6 = DataSet("DataSet18.04/Amplituda/SF/data_class_6_ampl_sf.json")  # 2631
    amplsfDS7 = DataSet("DataSet18.04/Amplituda/SF/data_class_7_ampl_sf.json")  # 2388
    amplsfDS8 = DataSet("DataSet18.04/Amplituda/SF/data_class_8_ampl_sf.json")  # 2611
    amplsfDS9 = DataSet("DataSet18.04/Amplituda/SF/data_class_9_ampl_sf.json")  # 2430
    amplsfDS10 = DataSet("DataSet18.04/Amplituda/SF/data_class_10_ampl_sf.json")  # 2562

    # ss ampl
    amplssDS1 = DataSet("DataSet18.04/Amplituda/SS/data_class_1_ampl_ss.json")  # 2270
    amplssDS2 = DataSet("DataSet18.04/Amplituda/SS/data_class_2_ampl_ss.json")  # 2420
    amplssDS3 = DataSet("DataSet18.04/Amplituda/SS/data_class_3_ampl_ss.json")  # 2400
    amplssDS4 = DataSet("DataSet18.04/Amplituda/SS/data_class_4_ampl_ss.json")  # 2509
    amplssDS5 = DataSet("DataSet18.04/Amplituda/SS/data_class_5_ampl_ss.json")  # 2532
    amplssDS6 = DataSet("DataSet18.04/Amplituda/SS/data_class_6_ampl_ss.json")  # 2631
    amplssDS7 = DataSet("DataSet18.04/Amplituda/SS/data_class_7_ampl_ss.json")  # 2388
    amplssDS8 = DataSet("DataSet18.04/Amplituda/SS/data_class_8_ampl_ss.json")  # 2611
    amplssDS9 = DataSet("DataSet18.04/Amplituda/SS/data_class_9_ampl_ss.json")  # 2430
    amplssDS10 = DataSet("DataSet18.04/Amplituda/SS/data_class_10_ampl_ss.json")  # 2562

    # st ampl
    amplstDS1 = DataSet("DataSet18.04/Amplituda/ST/data_class_1_ampl_st.json")  # 2270
    amplstDS2 = DataSet("DataSet18.04/Amplituda/ST/data_class_2_ampl_st.json")  # 2420
    amplstDS3 = DataSet("DataSet18.04/Amplituda/ST/data_class_3_ampl_st.json")  # 2400
    amplstDS4 = DataSet("DataSet18.04/Amplituda/ST/data_class_4_ampl_st.json")  # 2509
    amplstDS5 = DataSet("DataSet18.04/Amplituda/ST/data_class_5_ampl_st.json")  # 2532
    amplstDS6 = DataSet("DataSet18.04/Amplituda/ST/data_class_6_ampl_st.json")  # 2631
    amplstDS7 = DataSet("DataSet18.04/Amplituda/ST/data_class_7_ampl_st.json")  # 2388
    amplstDS8 = DataSet("DataSet18.04/Amplituda/ST/data_class_8_ampl_st.json")  # 2611
    amplstDS9 = DataSet("DataSet18.04/Amplituda/ST/data_class_9_ampl_st.json")  # 2430
    amplstDS10 = DataSet("DataSet18.04/Amplituda/ST/data_class_10_ampl_st.json")  # 2562

    # tf ampl
    ampltfDS1 = DataSet("DataSet18.04/Amplituda/TF/data_class_1_ampl_tf.json")  # 2270
    ampltfDS2 = DataSet("DataSet18.04/Amplituda/TF/data_class_2_ampl_tf.json")  # 2420
    ampltfDS3 = DataSet("DataSet18.04/Amplituda/TF/data_class_3_ampl_tf.json")  # 2400
    ampltfDS4 = DataSet("DataSet18.04/Amplituda/TF/data_class_4_ampl_tf.json")  # 2509
    ampltfDS5 = DataSet("DataSet18.04/Amplituda/TF/data_class_5_ampl_tf.json")  # 2532
    ampltfDS6 = DataSet("DataSet18.04/Amplituda/TF/data_class_6_ampl_tf.json")  # 2631
    ampltfDS7 = DataSet("DataSet18.04/Amplituda/TF/data_class_7_ampl_tf.json")  # 2388
    ampltfDS8 = DataSet("DataSet18.04/Amplituda/TF/data_class_8_ampl_tf.json")  # 2611
    ampltfDS9 = DataSet("DataSet18.04/Amplituda/TF/data_class_9_ampl_tf.json")  # 2430
    ampltfDS10 = DataSet("DataSet18.04/Amplituda/TF/data_class_10_ampl_tf.json")  # 2562

    # ts ampl
    ampltsDS1 = DataSet("DataSet18.04/Amplituda/TS/data_class_1_ampl_ts.json")  # 2270
    ampltsDS2 = DataSet("DataSet18.04/Amplituda/TS/data_class_2_ampl_ts.json")  # 2420
    ampltsDS3 = DataSet("DataSet18.04/Amplituda/TS/data_class_3_ampl_ts.json")  # 2400
    ampltsDS4 = DataSet("DataSet18.04/Amplituda/TS/data_class_4_ampl_ts.json")  # 2509
    ampltsDS5 = DataSet("DataSet18.04/Amplituda/TS/data_class_5_ampl_ts.json")  # 2532
    ampltsDS6 = DataSet("DataSet18.04/Amplituda/TS/data_class_6_ampl_ts.json")  # 2631
    ampltsDS7 = DataSet("DataSet18.04/Amplituda/TS/data_class_7_ampl_ts.json")  # 2388
    ampltsDS8 = DataSet("DataSet18.04/Amplituda/TS/data_class_8_ampl_ts.json")  # 2611
    ampltsDS9 = DataSet("DataSet18.04/Amplituda/TS/data_class_9_ampl_ts.json")  # 2430
    ampltsDS10 = DataSet("DataSet18.04/Amplituda/TS/data_class_10_ampl_ts.json")  # 2562

    # tt ampl
    amplttDS1 = DataSet("DataSet18.04/Amplituda/TT//data_class_1_ampl_tt.json")  # 2270
    amplttDS2 = DataSet("DataSet18.04/Amplituda/TT//data_class_2_ampl_tt.json")  # 2420
    amplttDS3 = DataSet("DataSet18.04/Amplituda/TT//data_class_3_ampl_tt.json")  # 2400
    amplttDS4 = DataSet("DataSet18.04/Amplituda/TT//data_class_4_ampl_tt.json")  # 2509
    amplttDS5 = DataSet("DataSet18.04/Amplituda/TT//data_class_5_ampl_tt.json")  # 2532
    amplttDS6 = DataSet("DataSet18.04/Amplituda/TT//data_class_6_ampl_tt.json")  # 2631
    amplttDS7 = DataSet("DataSet18.04/Amplituda/TT//data_class_7_ampl_tt.json")  # 2388
    amplttDS8 = DataSet("DataSet18.04/Amplituda/TT//data_class_8_ampl_tt.json")  # 2611
    amplttDS9 = DataSet("DataSet18.04/Amplituda/TT//data_class_9_ampl_tt.json")  # 2430
    amplttDS10 = DataSet("DataSet18.04/Amplituda/TT//data_class_10_ampl_tt.json")  # 2562

    image = cv2.imread("DataSet18.04/Images/img1_IUV.jpg", cv2.IMREAD_GRAYSCALE)
    image2arr1 = Image.fromarray(image)
    image2arr1 = np.array(image2arr1) / 255

    image = cv2.imread("DataSet18.04/Images/img11_IUV.jpg", cv2.IMREAD_GRAYSCALE)
    image2arr2 = Image.fromarray(image)
    image2arr2 = np.array(image2arr2) / 255

    image = cv2.imread("DataSet18.04/Images/img21_IUV.jpg", cv2.IMREAD_GRAYSCALE)
    image2arr3 = Image.fromarray(image)
    image2arr3 = np.array(image2arr3) / 255

    image = cv2.imread("DataSet18.04/Images/img31_IUV.jpg", cv2.IMREAD_GRAYSCALE)
    image2arr4 = Image.fromarray(image)
    image2arr4 = np.array(image2arr4) / 255

    image = cv2.imread("DataSet18.04/Images/img41_IUV.jpg", cv2.IMREAD_GRAYSCALE)
    image2arr5 = Image.fromarray(image)
    image2arr5 = np.array(image2arr5) / 255

    image = cv2.imread("DataSet18.04/Images/img51_IUV.jpg", cv2.IMREAD_GRAYSCALE)
    image2arr6 = Image.fromarray(image)
    image2arr6 = np.array(image2arr6) / 255

    image = cv2.imread("DataSet18.04/Images/img61_IUV.jpg", cv2.IMREAD_GRAYSCALE)
    image2arr7 = Image.fromarray(image)
    image2arr7 = np.array(image2arr7) / 255

    image = cv2.imread("DataSet18.04/Images/img71_IUV.jpg", cv2.IMREAD_GRAYSCALE)
    image2arr8 = Image.fromarray(image)
    image2arr8 = np.array(image2arr8) / 255

    image = cv2.imread("DataSet18.04/Images/img81_IUV.jpg", cv2.IMREAD_GRAYSCALE)
    image2arr9 = Image.fromarray(image)
    image2arr9 = np.array(image2arr9) / 255

    image = cv2.imread("DataSet18.04/Images/img91_IUV.jpg", cv2.IMREAD_GRAYSCALE)
    image2arr10 = Image.fromarray(image)
    image2arr10 = np.array(image2arr10) / 255

    pyplot.imshow(image)
    # Генерация обучающей выборки
    (xff, yff, aff) = getTrainDataSet(RxTxLabel='ff')
    (xfs, yfs, afs) = getTrainDataSet(RxTxLabel='fs')
    (xft, yft, aft) = getTrainDataSet(RxTxLabel='ft')
    (xsf, ysf, asf) = getTrainDataSet(RxTxLabel='sf')
    (xss, yss, ass) = getTrainDataSet(RxTxLabel='ss')
    (xst, yst, ast) = getTrainDataSet(RxTxLabel='st')
    (xtf, ytf, atf) = getTrainDataSet(RxTxLabel='tf')
    (xts, yts, ats) = getTrainDataSet(RxTxLabel='ts')
    (xtt, ytt, att) = getTrainDataSet(RxTxLabel='tt')

    # Генерация тестовой выборки
    (txff, tyff, taff) = getTestDataSet(RxTxLabel='ff')
    (txfs, tyfs, tafs) = getTestDataSet(RxTxLabel='fs')
    (txft, tyft, taft) = getTestDataSet(RxTxLabel='ft')
    (txsf, tysf, tasf) = getTestDataSet(RxTxLabel='sf')
    (txss, tyss, tass) = getTestDataSet(RxTxLabel='ss')
    (txst, tyst, tast) = getTestDataSet(RxTxLabel='st')
    (txtf, tytf, tatf) = getTestDataSet(RxTxLabel='tf')
    (txts, tyts, tats) = getTestDataSet(RxTxLabel='ts')
    (txtt, tytt, tatt) = getTestDataSet(RxTxLabel='tt')

    # Собираем фазы в 1 массив
    fullPhaseTrainMass = np.concatenate([aff, afs, aft, asf, ass, ast, atf, ats, att]).T
    print("Size: " + str(fullPhaseTrainMass.shape))
    # Собираем амплитуды в 1 массив
    fullAmplTrainMass = np.concatenate([xff, xfs, xft, xsf, xss, xst, xtf, xts, xtt]).T

    # Собираем амплитуды в 1 массив для теста
    fullAmplTestMass = np.concatenate([txff, txfs, txft, txsf, txss, txst, txtf, txts, txtt]).T

    # Собираем амплитуды в 1 массив для теста
    fullPhaseTestMass = np.concatenate([taff, tafs, taft, tasf, tass, tast, tatf, tats, tatt]).T

    # Собираем саммв и фаз и амплитуд
    #fullPhaseAndAmplTrainMass = np.concatenate([fullPhaseTrainMass, fullAmplTrainMass])
    #fullPhaseAndAmplTestMass = np.concatenate([fullPhaseTestMass, fullAmplTestMass])

    print(fullAmplTrainMass.shape)
    print(fullPhaseTrainMass.shape)

    ''' Модель автоэнкодера '''
    # Слой входных данных по амплитуде
    input_ampl = Input(shape=(504,))

    a = Dense(512, activation='relu', input_shape=(504))

    # Слой водных данных по фазе
    input_phase = Input(shape=(504,))

    p = Dense(512, activation='relu', input_shape=(504))

    # Соединение слоёв
    x = concatenate([input_ampl, input_phase])

    # Полносвязный слой
    xx = Dense(4096, activation='relu')(x)
    #xx = Dense(65536, activation='relu')(x)

    # Скрытый слой с hidden_dim нейронами
    encoded_start = Dense(4096, activation='tanh')(xx)

    reshape_layer = Reshape((8, 8, 64), input_shape=(4096,))(encoded_start)

    upsampl_layer1 = UpSampling2D(size=(2, 2))(reshape_layer)

    encoded_layer1 = Conv2D(512, (3, 3), activation='tanh', padding='same')(upsampl_layer1)

    batchnormal_layer1 = BatchNormalization(momentum=0.5)(encoded_layer1)

    upsampl_layer2 = UpSampling2D(size=(2, 2))(batchnormal_layer1)

    encoded_layer2 = Conv2D(256, (3, 3), activation='tanh', padding='same')(upsampl_layer2)

    batchnormal_layer2 = BatchNormalization(momentum=0.5)(encoded_layer2)

    upsampl_layer3 = UpSampling2D(size=(2, 2))(batchnormal_layer2)

    encoded_layer3 = Conv2D(128, (3, 3), activation='tanh', padding='same')(upsampl_layer3)

    batchnormal_layer3 = BatchNormalization(momentum=0.5)(encoded_layer3)

    encoded_layer4 = Conv2D(1, (3, 3), activation='tanh', padding='same')(batchnormal_layer3)

    # Собираем модель из слоёв
    encoder = keras.Model([input_ampl, input_phase], encoded_layer4, name="encoder")
    encoder.compile(optimizer='adam', loss='mean_squared_error')

    encoder.summary()

    history = encoder.fit([fullAmplTrainMass, fullPhaseTrainMass], yff, epochs=1,
                          validation_data=([fullAmplTestMass, fullPhaseTestMass], tyff))
    pyplot.plot(history.history['loss'])
    pyplot.plot(history.history['val_loss'])
    pyplot.title('Потери на этапах проверки и обучения')
    pyplot.ylabel('Потери')
    pyplot.xlabel('Эпохи')
    pyplot.legend(['Потери на этапе обучения', 'Потери на этапе проверки'], loc='upper left')
    pyplot.show()
    encoder.save_weights('model.weights.h5')
    model_json = encoder.to_json()
    # Записываем модель в файл
    json_file = open("mnist_model.json", "w")
    json_file.write(model_json)
    json_file.close()
    decodedImg = encoder.predict([fullAmplTestMass, fullPhaseTestMass])
    print(decodedImg[0])
    n = 10
    pyplot.figure(figsize=(20, 20))
    res = 1
    resdel = 0
    respr = 0
    sum = 4096

    for i in range(n):
        resdel = 0
        # оригинальные изображения
        ax = pyplot.subplot(10, n, i + 1)
        pyplot.imshow((tyff[i]))
        pyplot.gray()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        # восстановленные изображения автоэнкодером
        ax = pyplot.subplot(10, n, i + 1 + n)
        pyplot.imshow(np.array(decodedImg[i]))
        pyplot.gray()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        for j in range(64):
            for k in range(64):
                if ((tyff[i][j][k] > 0.8) == (decodedImg[i][j][k] > 0.8)):
                    respr = respr + 1
        resdel = respr / sum
        res = res * resdel
        respr = 0

    pyplot.show()
    print(res)


    input()
    print('PyCharm')

