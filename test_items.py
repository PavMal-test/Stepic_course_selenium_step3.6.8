# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 17:59:15 2021

@author: user
"""

import time




def test_guest_should_see_add_to_basket_button(browser):
    
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    assert browser.find_element_by_css_selector(".btn-add-to-basket")
    time.sleep(3)