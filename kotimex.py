
# coding: utf-8

# In[2]:


import json
import sys
sys.path.append('../')

import re


# In[19]:


text = '2019년 4월 24일에'


# In[33]:


def basic_time_normalizer(text):
    # find year
    regex = re.compile("(?P<YEAR>\d+)년")
    year = regex.search(text).group('YEAR')
    if not year:
        year = '0000'
    
    # find month
    regex = re.compile("(?P<MONTH>\d+)월")
    month = regex.search(text).group('MONTH')
    if not month:
        month = '0'
    
    # find day
    regex = re.compile("(?P<DAY>\d+)일")
    day = regex.search(text).group('DAY')
    if not day:
        day = '0'
    
    ymd = year+month+day
    
    if ymd.isdigit():
        time_rep = year+'-'+month+'-'+day
    else:
        time_rep = text    
    return time_rep    


# In[35]:


def time2xsd(text):
    time_rep = basic_time_normalizer(text)
    xsd = '\"'+time_rep+'\"'+'^^<http://www.w3.org/2001/XMLSchema#date>'
    return xsd

