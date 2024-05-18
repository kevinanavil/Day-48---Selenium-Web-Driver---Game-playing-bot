from selenium import webdriver
from selenium.webdriver.common.by import By
from time import time

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)
edge_options.add_argument("--mute-audio")

driver = webdriver.Edge(options=edge_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie_button = driver.find_element(By.ID, "cookie")

start_time = time()
buy_interval = 5
next_purchase_time = start_time + buy_interval
five_min = time() + 60*1

while True:

    try:
        cookie_button.click()
        current_time = time()   

        if current_time >= next_purchase_time:
            upgrades = driver.find_elements(By.CSS_SELECTOR, "#store>div:not(.grayed)")
            print(f"Buying: {upgrades[-1].text}") 
            upgrades[-1].click()
            purchase_time = time()
            next_purchase_time = current_time + buy_interval
            elapsed_time_since_start = purchase_time - start_time
            print(f"Time since start : {elapsed_time_since_start:.2f} s\n")

        if time() > five_min:
            cookies_per_second = driver.find_element(By.ID, "cps")
            print(cookies_per_second.text)
            end_time = time()
            elapsed_time = end_time - start_time
            print(f"Total time : {elapsed_time:.2f} s\n")
            driver.quit()
            break

    except Exception as e:
        print(f"An unexpected error occurred : {e}\n")
        driver.quit()
        break


