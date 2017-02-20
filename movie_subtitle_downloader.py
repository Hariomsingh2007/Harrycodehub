import time
import requests
import sys
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


file_details=sys.argv[1]

file_name_with_ext=file_details[file_details.rfind('\\',0,len(file_details))+1:]

file_path=file_details[0:file_details.rfind('\\',0,len(file_details))]

file_path_abs=file_path.replace('\\','/')


print(file_path)
print(file_name_with_ext)

file_name=file_name_with_ext[0:file_name_with_ext.rfind('.',0,len(file_name_with_ext)):]

print(file_name)



chrome_options = Options()
chrome_options.add_experimental_option('prefs', {'download.default_directory':file_path_abs})
driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver',chrome_options=chrome_options)



movie_name=file_name
#movie_name='the cove [2009] 720p brrip h.264 aac - extratorrentrg'
#driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver')  # Optional argument, if not specified will search path.
driver.get('http://www.opensubtitles.org/en/search');
#time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('MovieName')
search_box.send_keys(movie_name)
search_box.submit()
#time.sleep(5)
print(driver.current_url)

r=requests.get(driver.current_url)
soup=BeautifulSoup(r.content)
url=[]
#for i in soup.find_all("table",{"id":"search_results"}):
    #print(i.find('href'))
for j in soup.find_all("a","bnone"):
    url.append(j.get('href'))

print(url)
print(len(url))
if(len(url)!=0):
    print('inside if')
    new_url='http://www.opensubtitles.org'+url[0]
    print(new_url)
    driver.get(new_url);
    
#time.sleep(5)
driver.find_element_by_xpath(
    ".//*[contains(text(), 'Use OpenSubtitles Download Manager')]").click()
#time.sleep(5)
driver.find_element_by_id("bt-dwl-bt").click()
time.sleep(10)
driver.quit()

