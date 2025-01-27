import allure

from ht11.elements.cart import Cart
from ht11.elements.header import NavigationPanel
from ht11.pages.home_page import HomePage


@allure.suite("Tests for 'Cart' sidebar")
class TestCart:

    @allure.title("Verify CART sidebar can be opened via 'HOME' page")
    def test_open_empty_cart(self, driver):
        homepage = HomePage(driver)
        homepage.open()
        header = NavigationPanel(driver)
        header.click_on(header.CART)
        cart = Cart(driver)
        cart.assert_empty_cart_is_displayed()
        cart.click_on(cart.CLOSE_ICON)
        cart.assert_cart_is_not_displayed()
