from selenium import webdriver
import  time
tckno=input("Tc Kimlik No: ")
babad=input("Baba Ad: ")
driver_path = "chromedriver.exe"
browser = webdriver.Chrome(executable_path=driver_path)
browser.get("https://esecmen.chp.org.tr/default.aspx")
time.sleep(3)
txtTCKNO=browser.find_element_by_name("txtTCKNO")
txtBabaAdi=browser.find_element_by_name("txtBabaAdi")
txtTCKNO.send_keys(tckno)
txtBabaAdi.send_keys(babad)
xgiris="//*[@id='btnSorgula']"
giris=browser.find_element_by_xpath(xgiris)
giris.click()
time.sleep(1)
secmen=browser.find_element_by_id("secmen").text
il=browser.find_element_by_id("il").text
ilce=browser.find_element_by_id("ilce").text
mahalle=browser.find_element_by_id("mahalle").text
sandikAlani=browser.find_element_by_id("sandikAlani").text
sandikNo=browser.find_element_by_id("sandikNo").text
browser.close()
print(secmen)
print(il)
print(ilce)
print(mahalle)
print(sandikAlani)
print(sandikNo)







