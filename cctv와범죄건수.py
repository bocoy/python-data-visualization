#_*_coding:utf-8 _*_
import numpy as np
import pandas as pd
import glob, re
import matplotlib
import matplotlib.pyplot as plt 
import seaborn as sns 
import platform

from matplotlib import font_manager, rc

font_location="C:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)
matplotlib.rcParams['axes.unicode_minus'] = False

cctv = pd.read_excel("c:\\Temp\\서울시 자치구 년도별 CCTV 설치 현황.xlsx") #cctv 데이터를 불러옴

typelist = [u'강남구',u'강동구',u'강북구',u'강서구',u'관악구',u'광진구',u'구로구',u'금천구',u'노원구',u'도봉구',u'동작구',u'마포구',u'서대문구',u'서초구',u'성동구',u'성북구',u'송파구',u'양천구',u'영등포구',u'용산구',u'은평구',u'종로구',u'중구']
typelist2 = [u'2011년',u'2012년',u'2013년',u'2014년',u'2015년',u'2016년',u'2017년',u'2018년']
typelist3 = [u'발생건수(2011년)',u'발생건수(2012년)',u'발생건수(2013년)',u'발생건수(2014년)',u'발생건수(2015년)',u'발생건수(2016년)',u'발생건수(2017년)',u'발생건수(2018년)']



df1 = pd.DataFrame(cctv.T) #index를 년도로 하기위해 전치

cctvdata = pd.DataFrame(columns=typelist,index=typelist2) #column이 자치구이고 index가 년도인 빈 데이터 프레임 생성  
index = 0

for type in typelist:
    cctvdata[type] = df1[index]  #df1 컬럼 데이터를 cctvdata에 넣음 
    index += 1
cctvdata = cctvdata.apply(pd.to_numeric) #데이터를 int로 형변환 



crime_files = glob.glob('c:\\Temp\\crime_*.xlsx') #glob으로 년도별로 생성되어 있는 xlsx파일을 불러옴
index2 = 0
df6 = pd.DataFrame()    #빈 데이터 프레임 생성
for f in crime_files:
    df4 = pd.read_excel(f)  #xlsx파일을 순차적으로 부름
    df5 = pd.DataFrame({typelist3[index2]:df4[typelist3[index2]]})  #발생건수 컬럼을 추출
    df6 = pd.concat([df6,df5],axis = 1)     #df6에 적용
    
    index2 += 1

df7 = df6.T #년도를 index로 주기위해 전치 
crimedata = pd.DataFrame(index = typelist3) #년도를 index주는 데이터 프레임 생성


for i in range(0,23): 
    crimedata[typelist[i]] = df7[i] #자치구 컬럼 지정


index3 = 1
index4 = 1
index5 = 1

# 관계대수 비교를 위한 scatter 생성
plt.figure(figsize=(18,18)) 
for i in range(0,9):
    plt.subplot(3,3,index3)
    plt.scatter(cctvdata[typelist[i]],crimedata[typelist[i]], s = 50, c = 'r')
    sns.regplot(x=cctvdata[typelist[i]],  y=crimedata[typelist[i]], fit_reg=True) # default
    plt.title(typelist[i])
    plt.xlabel('CCTV')
    plt.ylabel('사건수')
    index3 += 1
plt.figure(figsize=(18,18)) 
for i in range(9,18):
    plt.subplot(3,3,index4)
    plt.scatter(cctvdata[typelist[i]],crimedata[typelist[i]], s = 50, c = 'r',)
    sns.regplot(x=cctvdata[typelist[i]],  y=crimedata[typelist[i]], fit_reg=True) # default
    plt.title(typelist[i])
    plt.xlabel('CCTV')
    plt.ylabel('사건수')
    index4 += 1 
plt.figure(figsize=(20,20))
for i in range(18,23):
    plt.subplot(3,3,index5)
    plt.scatter(cctvdata[typelist[i]],crimedata[typelist[i]], s = 50, c = 'r')
    sns.regplot(x=cctvdata[typelist[i]],  y=crimedata[typelist[i]], fit_reg=True) # default
    plt.title(typelist[i])
    plt.xlabel('CCTV')
    plt.ylabel('사건수')
    index5 += 1
plt.savefig('fig1.png')

index6 = 1
index7 = 1
index8 = 1
index9 = np.arange(len(typelist2))
bar_width = 0.35

alpha = 0.5

#막대그래프 생성
plt.figure(figsize=(18,18))
for i in range(0,9):
    plt.subplot(3,3,index6)
    plt.bar(index9, cctvdata[typelist[i]],bar_width,color='b', alpha=alpha,label='CCTV')
    plt.plot(index9, cctvdata[typelist[i]],bar_width,color='b', alpha=alpha)
    plt.bar(index9 + bar_width, crimedata[typelist[i]], bar_width,  color='r', alpha=alpha,label='사건사고수')
    plt.plot(index9 + bar_width, crimedata[typelist[i]], bar_width,  color='r', alpha=alpha)
    plt.title(typelist[i], fontsize=10)
    plt.ylabel('cctv&사건사고수', fontsize=10)
    plt.xticks(index9, typelist2, fontsize=8)  
    index6 +=1
    plt.legend()
    
plt.figure(figsize=(18,18))    
for i in range(9,18):
    plt.subplot(3,3,index7)
    plt.bar(index9, cctvdata[typelist[i]],bar_width,color='b', alpha=alpha,label='CCTV')
    plt.plot(index9, cctvdata[typelist[i]],bar_width,color='b', alpha=alpha)
    plt.bar(index9 + bar_width, crimedata[typelist[i]], bar_width,  color='r', alpha=alpha,label='사건사고수')
    plt.plot(index9 + bar_width, crimedata[typelist[i]], bar_width,  color='r', alpha=alpha)
    plt.title(typelist[i], fontsize=10)
    plt.ylabel('cctv&사건사고수', fontsize=10)
    plt.xticks(index9, typelist2, fontsize=8)  
    index7 +=1
    plt.legend()
    
plt.figure(figsize=(18,18))    
for i in range(18,23):
    plt.subplot(3,3,index8)
    plt.bar(index9, cctvdata[typelist[i]],bar_width,color='b', alpha=alpha,label='CCTV')
    plt.plot(index9, cctvdata[typelist[i]],bar_width,color='b', alpha=alpha)
    plt.bar(index9 + bar_width, crimedata[typelist[i]], bar_width,  color='r', alpha=alpha,label='사건사고수')
    plt.plot(index9 + bar_width, crimedata[typelist[i]], bar_width,  color='r', alpha=alpha)
    plt.title(typelist[i], fontsize=10)
    plt.ylabel('CCTV&사건사고수', fontsize=10)
    plt.xticks(index9, typelist2, fontsize=8)  
    index8 +=1
    plt.legend()
plt.show()

