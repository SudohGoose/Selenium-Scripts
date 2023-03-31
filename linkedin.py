

from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
import random
import time
driver = webdriver.Firefox()

# open file containing motivational quotes and add a random quote to the variable quotes
    
def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)
quotes = (random_line('motivational_quotes.txt'))
    
# Launch the web browser and navigate to the LinkedIn login page
driver.get("https://www.linkedin.com/login")

# Enter your LinkedIn account username and password and click the login button
driver.find_element(By.ID, "username").send_keys("your_username")  
driver.find_element(By.ID, "password").send_keys("your_password",Keys.RETURN)

# Navigate to the LinkedIn homepage and create a new post with your motivation quote
time.sleep(10)
driver.find_element(By.XPATH, "//*[@id='ember25']").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "div[aria-label='Text editor for creating content']").click()
post_field=driver.find_element(By.CSS_SELECTOR, "div[aria-label='Text editor for creating content']")
post_field.send_keys(quotes)
time.sleep(2)
driver.find_element(By.XPATH, "//button[@id='ember349']").click() 
time.sleep(2)

# Logout from your LinkedIn account and close the web browser
driver.get("https://www.linkedin.com/m/logout/")
driver.quit()
