from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Edge options to keep the browser window open after execution
edge_options = EdgeOptions()
edge_options.add_experimental_option("detach", True)

# Initialize the Microsoft Edge driver
driver = webdriver.Edge(options=edge_options)

try:
    # Navigate directly to the Neopets login page
    driver.get("https://www.neopets.com/login/")

    # Wait for the username input field to be present (up to 10 seconds)
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "loginUsername"))
    )

    # Locate the password field
    password_field = driver.find_element(By.ID, "loginPassword")

    # Enter credentials
    username_field.clear()
    username_field.send_keys("123")

    password_field.clear()
    password_field.send_keys("123")

    # Press Enter on the password field to submit the form
    password_field.send_keys(Keys.RETURN)

    error_message_p = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#validateUsername p"))
    )

    new_text = "Credenciales erróneas"
    driver.execute_script("arguments[0].textContent = arguments[1];", error_message_p, new_text)

    checkbox = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='checkbox']")))
    
    checkbox.click()

    print("Look the results")

except Exception as e:
    print(f"An error occurred: {e}")

# Note: We intentionally do NOT call driver.quit() here.