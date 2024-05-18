from selenium import webdriver
from selenium.webdriver.common.by import By

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=edge_options)
driver.get("https://www.amazon.com/VAMJAM-Running-Shoes-Fashion-Sneakers/dp/B097R39VPH/ref=s9_acsd_al_ot_c2_x_2_t?_encoding=UTF8&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-8&pf_rd_r=241TFFMDP7XKKR66GTTK&pf_rd_p=9e716e32-547d-416f-8d63-1c901327ceea&pf_rd_t=&pf_rd_i=19781749011")

captcha = driver.find_element(By.LINK_TEXT, "Try different image")
captcha.click()

price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")

print(f"The price is ${price_dollar.text}.{price_cents.text}")

driver.quit()
