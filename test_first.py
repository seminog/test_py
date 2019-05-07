import allure

import logging

from selenium import webdriver


@allure.feature('Сми сегодня')
@allure.story('Яндекс')
def test_open_ya():
    with allure.step('Шаг 1'):
        wd = webdriver.Chrome()
    with allure.step('Шаг 2'):
        wd.get('http://yandex.ru')
    with allure.step('Шаг 3'):
        wd.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[1]/div/div[1]/div/div[1]/div/div[1]/'
                                 'div/div[1]/div[1]/h1/a').click()

    with allure.step('Шаг 4'):
        logging.info(f'!!!!!!! - {wd.current_url}')
        assert wd.current_url != 'https://news.yandex.ru/?msid=1557147681.82138.140563.247752&mlid=1557147086.glob_225'
