# -*- coding: utf-8 -*-
"""
@Time ： 2021/1/30 22:30
@Auth ： Zoey
@File ：training_5.py
@Description：
"""

import pytest
from selenium import webdriver
import time
import allure


@allure.testcase("https://zoeyteam.coding.net/p/hgwart/")   # 添加测试用例的链接地址
@allure.feature("百度搜索")
@pytest.mark.parametrize('test_data1', ['allure', 'pytest', 'unitest'])
def test_steps_demo(test_data1):

    with allure.step("打开chrom浏览器"):     # 测试用例步骤
        driver = webdriver.Chrome()
    with allure.step("访问百度"):
        driver.get("http://www.baidu.com")
    with allure.step("浏览器最大化"):
        driver.maximize_window()

    with allure.step(f'输入搜索词{test_data1}'):
        driver.find_element_by_id('kw').send_keys(test_data1)
        time.sleep(2)

    with allure.step("保存图片"):
        driver.save_screenshot("./result/b.png")
        allure.attach.file("./result/b.png", attachment_type=allure.attachment_type.PNG)
        allure.attach("<head></head><body>首页</body>", "Attach with HTML type", allure.attachment_type.HTML)
    with allure.step("关闭浏览器"):
        driver.quit()
