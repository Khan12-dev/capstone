from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login(driver):
    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
    )


def add_all_to_cart(driver):
    buttons = driver.find_elements(By.CSS_SELECTOR, 'button[id^="add-to-cart-"]')
    print(f"Found {len(buttons)} Add to Cart buttons")
    for button in buttons:
        button.click()


def test_add_all_products_to_cart():
    driver = webdriver.Chrome()
    try:
        login(driver)
        add_all_to_cart(driver)

        badge = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        )

        assert badge.text == "6", f"Expected 6 items in cart, but got {badge.text}"
    finally:
        driver.quit()
