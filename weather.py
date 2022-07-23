from selenium.webdriver.common.keys import Keys
from selenium import webdriver


d1 = webdriver.Chrome()
d1.minimize_window()

d1.get('https://google.com')
d1.implicitly_wait(2)


##place = input("Please Enter your location. ")
##search = 'weather in '+ place

search = "Weather in Laxmi Nagar Today."
d1.find_element_by_css_selector('input[title = "Search"]').send_keys(search + Keys.ENTER)
lst = []

p = int(d1.find_element_by_css_selector('span[id = "wob_pp"]').text.strip('%'))
t = int(d1.find_element_by_xpath('//*[@id="wob_tm"]').text)

lst.append(d1.find_element_by_css_selector('div[id="wob_loc"]').text)
lst.append(d1.find_element_by_css_selector('div[id="wob_dts"]').text)
lst.append("Precipitation:- "+ str(p))
lst.append("Average Tempreature:- " +str(t)+"C")



print("\n"*2)

if (p < 30):
    print("Chances of getting a random natural shower are quite low. ")
elif (p < 50) and (p > 30) :
    print("Consider carrying a pocket umbrella with you. ")
else:
    print("Very high chances of your reaching workplace, drenched from a random drizzle. ")
    
if t< 20:
    print("Also, There’s a nip in the air, would suggest you to wear something warm.")
elif t< 30 and t>20:
    print("Also, Today is another pleasant day to be alive, wear your favorite attire to rock this day!")
else:
    print("Also, It's steaming hot outside. Try to calm yourself, wear some bright colored cloths. ")

print("\n")
for i in lst:
    print(i,end='\n')

d1.close()
