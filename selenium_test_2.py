import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def browser():
    driver = None
    try:
        driver = webdriver.Chrome()
        yield driver
    finally:
        if driver is not None:
            driver.quit()


def test_find_element_by_css_selector(browser):
    browser.get("http://91.221.70.79:8042/21")
    password_field = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "pass"))
    )
    password_field.clear()
    password_field.send_keys("test")
    button_element = browser.find_element(By.CSS_SELECTOR,
                                          "button[style='margin-top: 32px; height: 34px;']")
    button_element.click()
    button_test_2 = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID,
                                        "69789"))
    )
    button_test_2.click()
    word = "Сообщение"
    xpath_expression = f"//table//th[contains(., 'Сообщение')]"
    message = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        xpath_expression))
    )
    message_text = message.text
    assert message_text == word
