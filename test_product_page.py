from pages.main_page import MainPage
from pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    add_page = ProductPage(browser, browser.current_url)
    add_page.add_product()          #нажали кнопку Добавить
    add_page.solve_quiz_and_get_code() #вычислилили математику
    add_page.check_name_product_in_busket() #проверяем в алерте что имя товара добавлено в корзину
    add_page.check_sum_product_in_busket() #проверяем совпадение цены товара с суммой в корзине