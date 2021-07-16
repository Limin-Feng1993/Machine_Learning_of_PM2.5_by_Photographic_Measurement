from PIL import Image
import os, sys
import numpy as np

import time
import datetime
from datetime import date
from datetime import timedelta
from datetime import datetime

import xlrd 
import xlwt 
import xlsxwriter
import pathlib
from pathlib import Path

def get_filename(filename):
  (filepath,tempfilename) = os.path.split(filename);
  (shotname,extension) = os.path.splitext(tempfilename);
  #return filepath, shotname, extension
  return shotname

# 字符串时间转换为计算机存储时间(datetime)
def Normaltime(str_time_input):
	Normaltime_output = datetime.strptime(str_time_input,'%Y%m%d%H%M%S%f')
	return Normaltime_output

# datetime转为字符串
def Changestr(datetime_input):
	str_output = datetime_input.strftime('%Y-%m-%d %H:%M')
	return str_output

#Excel时间序列处理方法第一步(当时间列为数值时)
def TS(x):
	return (x - np.datetime64('1970-01-01T00:00:00Z'))/np.timedelta64(1, 's')
	#return datetime.utcfromtimestamp(x.astype('O')/1e9)
	#return datetime.fromtimestamp(x.tolist()/1e9)

##Excel时间序列处理方法第二步DT(TS(x))
def DT(x):
	return datetime.utcfromtimestamp(x)

path_photo=pathlib.Path('D:\\Test_data\\2020\\Photo_Beijing\\')
filelist=list(path_photo.glob('**/*.jpg'))
print(len(filelist))

filename='RGB_R_L.xlsx'
workbook = xlsxwriter.Workbook(filename,options={'nan_inf_to_errors': True})
worksheet = workbook.add_worksheet(u'RGB_R_L')
headings = [ 'Time', 'R_R_M', 'G_R_M','B_R_M', 'R_L_M','G_L_M','B_L_M']
bold = workbook.add_format({'bold': 1})
worksheet.write_row('A1', headings, bold)

Time=[]
R_R_Mdata=[]
G_R_Mdata=[]
B_R_Mdata=[]
R_L_Mdata=[]
G_L_Mdata=[]
B_L_Mdata=[]

for file in filelist:
    photoname=get_filename(file)
    timei=Normaltime(photoname)
    print(timei)
    Time.append(timei)
    
    img = Image.open(file)
    width, height = img.size
    box_R = (0.5*width, 0, 0.9*width, height)
    box_L = (0.1*width, 0, 0.5*width, height)
    region_R = img.crop(box_R)
    region_L = img.crop(box_L)
    
    R_R, G_R, B_R = region_R.split()
    R_L, G_L, B_L = region_L.split()

    R_R_M = np.mean(R_R)
    G_R_M = np.mean(G_R)
    B_R_M = np.mean(B_R)

    R_L_M = np.mean(R_L)
    G_L_M = np.mean(G_L)
    B_L_M = np.mean(B_L)

    #print(R_R_M,G_R_M,B_R_M,R_L_M,G_L_M,B_L_M)
    
    R_R_Mdata.append(R_R_M)
    G_R_Mdata.append(G_R_M)
    B_R_Mdata.append(B_R_M)
    R_L_Mdata.append(R_L_M)
    G_L_Mdata.append(G_L_M)
    B_L_Mdata.append(B_L_M)
      
worksheet.write_column('A2', Time)
worksheet.write_column('B2', R_R_Mdata)
worksheet.write_column('C2', G_R_Mdata)
worksheet.write_column('D2', B_R_Mdata)
worksheet.write_column('E2', R_L_Mdata)
worksheet.write_column('F2', G_L_Mdata)
worksheet.write_column('G2', B_L_Mdata)
workbook.close() 
