import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_checkout_flow(driver):
    wait = WebDriverWait(driver, 15)

    driver.get("https://www.saucedemo.com/")

    wait.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    ).send_keys("standard_user")

    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    add_buttons = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "button.btn_inventory")
        )
    )

    for button in add_buttons:
        button.click()

    wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
    ).click()

    wait.until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    ).click()

    wait.until(
        EC.visibility_of_element_located((By.ID, "first-name"))
    ).send_keys("Test")

    driver.find_element(By.ID, "last-name").send_keys("User")
    driver.find_element(By.ID, "postal-code").send_keys("12345")

    wait.until(
        EC.element_to_be_clickable((By.ID, "continue"))
    ).click()

    wait.until(
        EC.element_to_be_clickable((By.ID, "finish"))
    ).click()

    success_message = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
    ).text

    assert success_message == "Thank you for your order!"
