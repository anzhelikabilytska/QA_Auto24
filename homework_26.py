from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    print("Запускаємо браузер...")
    driver.get("http://localhost:8000/dz.html")

    wait = WebDriverWait(driver, 10, poll_frequency=0.2)

    frames = driver.find_elements(By.TAG_NAME, "iframe")
    print(f"Знайдено {len(frames)} фрейм(ів) на сторінці.")
    for index, frame in enumerate(frames):
        print(f"Фрейм {index}: {frame.get_attribute('id')}")

    print("Очікуємо доступності фрейму 'frame1'...")
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "frame1")))
    print("Фрейм 'frame1' доступний.")

    input1 = driver.find_element(By.ID, "input1")
    input1.send_keys("Frame1_Secret")
    driver.find_element(By.TAG_NAME, "button").click()
    driver.switch_to.default_content()

except Exception as e:
    print(f"Виникла помилка: {e}")
finally:
    if driver:
        print("Закриваємо браузер...")
        driver.quit()
