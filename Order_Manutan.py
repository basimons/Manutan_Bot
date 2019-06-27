#!/usr/bin/env python3
from input_file import *
import numpy as np
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

#Link
Link = "https://www.manutan.nl/nl/mnl/catalogus-aanvraag"

# go to site
try:
	Number_of_manutans = int(Number_of_manutans)
except:
	print('Number of manutans has to be an integer')
	exit()

if Number_of_manutans == 0:
	exit()

def Orderman(driver,num,Link):
	if num == 0:
		exit()

	frame = driver.find_element_by_id('newsletterFrame')
	driver.switch_to.frame(frame)

	#Number of manutans
	numman = Select(driver.find_element_by_class_name('form-control'))
	numman.select_by_visible_text(str(num))

	#Dhr. or Mevr.
	Sex_element = Select(driver.find_element_by_name('TITLE'))
	Sex_element.select_by_visible_text(str(Sex))

	#Comany name
	Compname = driver.find_element_by_id('COMPANYNAME')
	Compname.click()	
	Compname.send_keys(Company_name)

	#Zip-code
	Zipcode = driver.find_element_by_name('POSTCODE')
	Zipcode.click()
	Zipcode.send_keys(Street_adjective)
	
	#House number
	Housenum = driver.find_element_by_id('HUISNR')
	Housenum.click()
	Housenum.send_keys(Street_number)

	#House addon
	Houseaddon = driver.find_element_by_name('TOEVOEGING')
	Houseaddon.click()
	Houseaddon.send_keys(Zip_code)
	
	#Initials
	Initials_element = driver.find_element_by_id('INITIALS')
	Initials_element.click()	
	Initials_element.send_keys(Initials)

	#Street name
	Street = driver.find_element_by_id('Straatnaam')
	Street.click()	
	Street.send_keys(Street_adres)

	#City
	City_element = driver.find_element_by_id('PLAATS')
	City_element.click()	
	City_element.send_keys(City)

	#Surname
	Surname_element = driver.find_element_by_id('NAME')
	Surname_element.click()	
	Surname_element.send_keys(Surname)

	#Submit
	Submit = driver.find_element_by_id('submit_link')	
	Submit.click()	

	return

def main(num,Link):
	
	#initialize driver
	driver = webdriver.Firefox(executable_path=r'./geckodriver')
	driver.get(Link)

	#go to manutan catologus site and order n amount.

	while Number_of_manutans > 5:
		if 0 <= Number_of_manutans <= 5
			Orderman(driver, Number_of_manutans,Link)
			break		
		Orderman(driver,5,Link)		
		Number_of_manutans -= 5
		driver.refresh()
	
	#done
	driver.close()
	return 




main(Number_of_manutans,Link)
