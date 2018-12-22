import time
from selenium import webdriver

delay = 0 # in seconds... Less delay = faster typing speed
driver_path = 'browser\\geckodriver-win.exe'

print('Setting up browser...')
driver = webdriver.Firefox(executable_path = driver_path) # Firefox driver (gechodriver)

print('Loading page...')
driver.get('https://typing-speed-test.aoeu.eu/')
wordEl = driver.find_element_by_id('currentword')
wordsEl = [wordEl] + driver.find_elements_by_class_name('nextword')
inp = driver.find_element_by_id('input')
words = []
print("Starting typing...")
for i in wordsEl:
	#for letter in i.get_attribute('innerHTML'):
	#	inp.send_keys(letter)
	#	#time.sleep(delay)
	#inp.send_keys(i.get_attribute('innerHTML') + ' ')
	words.append(i.get_attribute('innerHTML') + ' ')
	#inp.send_keys(' ')

words2 = ''
for i in words:
	words2 += i

inp.send_keys(words2)
