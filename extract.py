#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pdfplumber
import re
import csv
import pandas as pd
from collections import namedtuple
import requests
import os

arr = os.listdir('./pdf-files')
print(arr)
line_items = []
for file in arr: 
    
    pdf = pdfplumber.open('./pdf-files/' + file)

    page = pdf.pages[0]
    left = page.crop((0, 0.1 * float(page.height), 0.3 * float(page.width), 0.23 * float(page.height)))
    mid = page.crop((0.3 * float(page.width), 0.1 * float(page.height), .6*(page.width), .23 * float(page.height)))

    text = page.extract_text()
    left_text = left.extract_text();
    left_text_split  = left_text.split('\n')
    #right_text = right.extract_text();
    mid_text = mid.extract_text();
    mid_text_split = mid_text.split('\n')

    print(left_text)

    player_tin = left_text_split[4][10:]
    account =  mid_text_split[0][7:];
    name = mid_text_split[1];
    address =  mid_text_split[2] +  mid_text_split[3]
    recipient_tin = mid_text_split[4][16:]


    Line = namedtuple('Line', 'account, name, address, recipient_tin, player_tin, src')
    
                
    src = 'C:\\Users\\anser\\Downloads\\ExtractKeywordsFromPDF-main\\pdf-files\\' + file        
    line_items.append(Line(account, name, address, recipient_tin, player_tin, src))
    
    
df = pd.DataFrame(line_items)
#print(df)

df.to_excel('f.xlsx',  index = None, header=True)




print("**********************Executing************************")
print("Done File Created")