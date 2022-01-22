import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_site_contains_add_button(browser):
    browser.get(link)
    time.sleep(30)
    button_add = browser.find_element_by_class_name('btn-add-to-basket')
    assert button_add, f'Кнопка не найдена'
