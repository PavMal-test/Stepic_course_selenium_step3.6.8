# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 21:38:01 2021

@author: user
"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


    
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")    
    parser.addoption('--language', action='store', default="ru",
                 help="Choose language ru/en-gb/fr...")



@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    lang = request.config.getoption('language')
    lang_list=['ar','ca','cs','da','de','en-gb','el','es','fi','fr','it','ko',
               'nl','pl','ru','sk','uk','zh-hans', "en"]
    if lang not in lang_list:
        raise pytest.UsageError("--language is unacceptable")
      
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': lang})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", lang)
        browser = webdriver.Firefox(firefox_profile=fp)
        
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()






    
    