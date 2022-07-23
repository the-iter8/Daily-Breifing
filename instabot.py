from selenium import webdriver
from time import sleep


#name = input("your username")
#password = input("Your account password")
name = 'themodops'
password = 'vikas12b'


d3 = webdriver.Chrome()
d3.implicitly_wait(2)
d3.get('https://www.instagram.com/')
d3.minimize_window()

d3.find_element_by_css_selector('input[name = "username"]').send_keys(name)
d3.find_element_by_css_selector('input[name = "password"]').send_keys(password)
d3.find_element_by_css_selector('button[type = "submit"]').click()
sleep(3)

try:
    d3.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
except:
    d3.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
    
    d3.minimize_window()
    d3.find_element_by_css_selector('svg[aria-label="Activity Feed"]').click()


#change
#here we have to iterate for the range of 5 notifications.
for i in range(5):
        dnotif = '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[4]/div/div/div[2]/div[2]/div/div/div/div/div['+str(i+1)+']/div[2]'
        try:
            ele = d3.find_element_by_xpath(dnotif)
            print(str(i+1)+'\t'+ ele.text)
        except:
            print("No new notification for your lmao.")
            break
            
d3.close()
