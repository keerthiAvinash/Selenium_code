import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Initialize the Chrome driver
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in headless mode
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=options)

try:
    # Step 1: Navigate to google.com
    driver.get('https://www.google.com')
    time.sleep(2)

    # Step 2: Locate the search box
    search_box = driver.find_element(By.NAME, 'q')

    # Step 3: Enter search query
    query = 'Selenium testing'
    search_box.send_keys(query)

    # Step 4: Submit the search
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)

    # Step 5: Validate that results are displayed
    results = driver.find_elements(By.CSS_SELECTOR, 'div.g')
    links = [r.find_elements(By.TAG_NAME, 'a') for r in results]
    links_flat = [item for sublist in links for item in sublist]
    relevant = any('selenium' in l.get_attribute('href').lower() or 'selenium' in l.text.lower() for l in links_flat if l.get_attribute('href'))

    # Output results
    print('Actual Results:')
    print(f'Number of result blocks found: {len(results)}')
    print(f'Number of links found: {len(links_flat)}')
    print('Relevant Selenium link found:', relevant)

    if len(results) > 0 and relevant:
        print('Test Status: PASS')
    else:
        print('Test Status: FAIL')

except Exception as e:
    print('Test Status: FAIL')
    print('Error:', str(e))
finally:
    driver.quit()
