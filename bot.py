import eel
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options








chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)





@eel.expose
def run_bot(url_prof, url_my_prof, password, comment):
	print(url_prof)
	print(url_my_prof)
	print(comment)


	file1 = open(url_my_prof)
	file2 = open(comment)
	while True:
		driver = webdriver.Chrome('chromedriver_win32/chromedriver.exe', chrome_options=chrome_options)
		line = file1.readline()
		line_coment = file2.readline()
		if not line:
			print("NOT LINE")
			# driver.quit()
			break
		print(line.strip())
		sleep(2.5)
		driver.get("https://www.facebook.com/")

		sleep(2.3)
		element = driver.find_element_by_id("email")
	
	
	

		sleep(1.1)
		element.send_keys(line.strip())
		sleep(1)
		element = driver.find_element_by_id("pass")
		sleep(0.9)
		element.send_keys(password)
		sleep(0.8)
		element.send_keys(Keys.RETURN)
		sleep(1.5)
		driver.get(str(url_prof))
		sleep(1.6)
		element = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div[2]/span/span').click()
		sleep(2.8)
		element = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[1]/div[5]/div/div[2]/div[1]/div/div/div/form/div/div/div[2]/div/div/div/div/span')
		sleep(1)
		element.send_keys(line_coment.strip())
		sleep(3)
		element.send_keys(Keys.RETURN)
		driver.quit()


	print("Программа успешно завершила свою работу!")

# https://www.facebook.com/photo?fbid=263751838873759&set=a.188130859769191

eel.init('web')
eel.start('main.html', size = (828 , 1792))

