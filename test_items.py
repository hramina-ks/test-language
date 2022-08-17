import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_should_see_button_add_to_cart(browser):
	browser.get(link)
	basket_button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
	assert basket_button.is_enabled() == True, "Button is not enabled!"
	
