from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

year = input('Which year?\n')
find = input('Enter organization/technology/topic keyword?\n')
url = f"https://summerofcode.withgoogle.com/archive/{year}/organizations"
xpath_searchbox = "/html/body/app-root/app-layout/mat-sidenav-container/mat-sidenav-content[1]/div/div/main/app-organizations/app-orgs-grid/section[2]/div/div[1]/div[1]/app-search/div/input"

#Open WebBrowser
driver = webdriver.Firefox()
driver.get(url)
# driver.implicitly_wait(15)
time.sleep(5)

#Search the keyword
search = driver.find_element(By.XPATH,xpath_searchbox)
search.send_keys(find)

#Creates a text file for the output
file = open(f"{find}_stations_{year}.txt","w+")
time.sleep(5)
# driver.implicitly_wait(10)

#Prints first 50 resulting station names in the file
for i in range(1,51):
    # time.sleep(1)
    driver.implicitly_wait(1)
    xpath_stations = f"/html/body/app-root/app-layout/mat-sidenav-container/mat-sidenav-content[1]/div/div/main/app-organizations/app-orgs-grid/section[2]/div/div[3]/div/div[{i}]/div/app-orgs-card/app-card/div/a/div[2]/div[1]"
    name = driver.find_element(By.XPATH,xpath_stations)
    file.write(name.text+"\n")

file.close()
driver.quit()