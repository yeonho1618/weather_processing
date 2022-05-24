'''
{
    "2021" : {
        "12" : {
            "7" : {
                "아침" : {
                    season = scrapy.Field()
                    #family = scrapy.Field()
                    temperature = scrapy.Field() # 기온
                    skystate = scrapy.Field() 
                    snow = scrapy.Field()     
                },
                "저녁"
            }
        }
    }
}
'''

from ast import Import
import csv
import sys
import re
import pandas as pd
import numpy as np
import os 

FILE_PATH = 'C:/Users/seoyh/Desktop/김천_자동화/20220331_DataBase/전처리 파일/김천 작년(21년) 날씨 데이터/초단기예보/'
STORED_FILE_PATH = ''

FILE_START_DATE = '202101'
FILE_END_DATE = '202112'
FILE_VALUE = ['기온','하늘상태','강수','1시간적설']
FILE_FORNAT = 'csv'



FILE_NAME = f'날씨_PROCESSING_FILE_{FILE_START_DATE}-{FILE_END_DATE}.{FILE_FORNAT}' # 날씨_PROCESSING_FILE_202101-202112.CSV

LOCATION_LIST = ['감문면', '감천면', '개령면', '구성면', '남면', '남산동', '농소면', '대곡동', '대덕면', '대신동', '대항면',
             '봉산면', '부항면', '아포읍', '양금동', '어모면', '율곡동', '자산동', '조마면', '증산면', '지례면', '지좌동']


    