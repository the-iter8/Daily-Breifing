from time import sleep
from selenium import webdriver

def start():
    global url
    url = []
    global news
    news = []
    
    for i in range (0,4):
        head = '/html/body/div[1]/section/div/div/div[1]/div[3]/div['+str(i+1)+']/div/div[2]/a'
        n1 =  d2.find_element_by_xpath(head)
        
        url.append(n1)
        news.append(n1.text)
    for j in range (len(news)):
        print("\n "+str(j+1)+".)"+str(news[j])+"\n")
    ask1()



def sorry():
    print("Oh, It seems like you have selected a wrong answer, please retry. ")
def ask1():
    ask = input("would you like to see any one of these in detail ? ")
    if ask.lower() == "yes":
        ask2()
    elif ask.lower() == "no":
        print("Alright, Have a great day ahead !")
    else:
        sorry()
        ask1()
def ask2():
    which = int(input("Which headline you would like to see in detail ? "))
    if which<=4 :
        url[which-1].click()
        item = d2.find_elements_by_xpath('//div[@class = "storyDetail"]/p')
        for i in item:
            print("\n",i.text)
        d2.back()
        d2.refresh()
        start()
    else:
        sorry()
        ask2()

#__main__
d2= webdriver.Chrome()
d2.maximize_window()
d2.implicitly_wait(3)
d2.get('https://www.hindustantimes.com/top-news/')
sleep(5)
d2.find_element_by_xpath('//*[@id="deny"]').click()

#url and news list are now globally available. You could use it anywhere inside this file.
start()


    

    

    


    
    
    
    

