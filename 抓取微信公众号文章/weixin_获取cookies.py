#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from selenium import webdriver
import time
import json
driver = webdriver.Chrome()    #需要一个谷歌驱动chromedriver.exe,要支持你当前谷歌浏览器的版本
driver.get('https://mp.weixin.qq.com/')     #发起get请求打开微信公众号平台登录页面，然后输入账号密码登录微信公众号

driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/form/div[1]/div[1]/div/span/input').clear()    #定位到账号输入框，清除里面的内容
driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/form/div[1]/div[1]/div/span/input').send_keys('这里输入你的账号')   #定位到账号输入框，输入账号
time.sleep(3)     #等待3秒后执行下一步操作，避免因为网络延迟，浏览器来不及加载出输入框，从而导致以下的操作失败
driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/form/div[1]/div[2]/div/span/input').clear()   #定位到密码输入框，清除里面的内容
driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/form/div[1]/div[2]/div/span/input').send_keys('这里输入你的密码')   #定位到密码输入框，输入密码
time.sleep(3)     #原因和以上相同
driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/form/div[3]/label').click()   #点击记住密码
time.sleep(3)     #原因和以上相同
driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/form/div[4]/a').click()   #点击登录

time.sleep(15)    #15秒内扫码登录
cookies = driver.get_cookies()  #获取扫码登录成功之后的cookies
print(cookies)       #如果超时了还不扫码，获取到的cookies是不完整的，不能用来登录公众号，所以第一次必须扫码登录以获取完整的cookies
cookie = {}      #定义一个空字典，以便把获取的cookies以字典的形式写入

for items in cookies:             #把登录成功后获取的cookies提取name和value参数写入空字典cookie
    cookie[items.get('name')] = items.get('value')

with open('cookies.txt','w') as file:          #新建并打开一个cookies.txt文件
    file.write(json.dumps(cookie))  #写入转成字符串的字典

driver.close()      #关闭浏览器