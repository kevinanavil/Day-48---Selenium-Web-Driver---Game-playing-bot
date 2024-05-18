from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup WebDriver with options
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=edge_options)
driver.get("https://www.python.org/")  # Just load the URL, no need to assign to data

events_section = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "content")))
event_elements = driver.find_elements(By.CSS_SELECTOR, '.event-widget li')

events = {}
index = 0 

for li in event_elements:  # Enumerate event_elements to get index
            
    # Extract the datetime attribute from the 'time' tag
    time_element = li.find_element(By.TAG_NAME, 'time')
    datetime = time_element.get_attribute('datetime')
    
    # Extract the event title from the 'a' tag
    title_element = li.find_element(By.TAG_NAME, 'a')
    title = title_element.text
    
    # Create dictionary for the current event
    event_info = {
        'datetime': datetime,
        'title': title
    }
    
    # Add the event info to the events dictionary
    events[index] = event_info
    index += 1
    
    # Print the events dictionary
print(events)

driver.quit()
