import pytest
import time
from selenium import webdriver

def test_item_language(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    btn = browser.find_element_by_class_name("btn-add-to-basket")
    assert btn.is_enabled(), "NO BUTTON!"



    

    

