# -*- coding: cp936 -*-
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import time
import re
import urllib

browser = webdriver.Firefox()
#��½
def login(login, pw):
      url = 'https://www.pinterest.com/login/'
      #����ʱ��
      browser.set_page_load_timeout(30)
      #������ҳ
      try:
            browser.get(url)
      except TimeoutException:
            print 'time out after 30s when loading page'
            #ֹͣ������ҳ
            browser.execute_script('window.stop()')
      time.sleep(10)
      #�����˺�����
      try:
            browser.find_element_by_name('id').send_keys(login)
            print 'input email success!'
      except:
            print 'input email error!'
      time.sleep(3)
      #��������
      try:
            browser.find_element_by_name('password').send_keys(pw)
            print 'input password success!'
      except:
            print 'input password error!'
      time.sleep(3)
      #���continue����½
      try:
            browser.find_element_by_css_selector('button[type="submit"]').click()
            print 'click continue success!'
      except:
            print 'click continue error!'

#����ҳ��
def scroll():
      for x in range(11):
            #print "NO." + str(x) + " sroll" 
            js = "var q=document.documentElement.scrollTop=5000*20"
            browser.execute_script(js)
            time.sleep(5)

#��ͼƬ
def getImage():
      content=browser.page_source
      reg = r'https://s-media-cache-ak0.pinimg.com/originals/.+?\.jpg 4x'
      imglist = re.findall(reg,content)
      num = 1
      for img in imglist:
            img = img.replace(" 4x",'')
            try:
                  urllib.urlretrieve(img, "D:\\pinterest\\jpg\\" + str(num) +".jpg",timeout=10)
                  print str(num) + '.jpg is successfully downloaded.'
                  num +=1
            except  socket.timeout as e:
                  print 'timeout'
            
            
      if num == 1:
            print 'error in crawl!'



if __name__ == '__main__':
      email = raw_input('please input your email:')
      pw = raw_input('please input your password:')
      login(login=email,pw=pw)
      print 'sleep 30s'
      time.sleep(30)
      print 'start scroll!'
      scroll()
      print 'start crawl!'
      getImage()
      print 'Program terminated normally'

                                                
