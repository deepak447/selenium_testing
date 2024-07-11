from selenium.webdriver import ChromeService
from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
import os
from loguru import logger
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

 # log the file here
logger.add("testingfile.log",enqueue=True)
#  Create WebDriver Object

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) # Create a WebDriver object. The service argument specifies the path to the ChromeDriver binary.


# Load URL and Wait for Element

url = "https://atg.party/"
t1 = time.time()
driver.get(url) # get the url of particular site 
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "atg-secondarybtn-tiny")))
logger.info(f"Response time of page load is : {round(time.time() - t1,2)} sec") # Here log the respose time of page load 

# Extract HTTP Response Status Code 

for i in driver.requests: # use the seleniumwire to log the HTTP response of the  url 
    if i.url == "https://atg.party/": # apply condition to extract the particular url status response 
        logger.info(f"Response Status Code for {i.url} :- {i.response.status_code}"
                    )
        break

# Extract the element by class name for login 

driver.implicitly_wait(20)
elem = driver.find_element(By.CLASS_NAME, "atg-secondarybtn-tiny") 
# time.sleep(3) # here i have provide 3 sec wait before click enter
elem.click() # It Work like enter button of keyboard

# Write email and password in login field that findout by ID

email_field = driver.find_element(By.ID, "email_landing") 
email_field.clear() # Its clear the input that existing already  
email_field.send_keys(USERNAME) # NOw send input keyword 

password_field = driver.find_element(By.ID, "password_landing")
password_field.clear()
password_field.send_keys(PASSWORD)

sign_in_button = driver.find_element(By.CLASS_NAME, "landing-signin-btn")
sign_in_button.click()

# Now find element for Dropdown and Click on it  

create_dropdown = driver.find_element(By.ID, "create-btn-dropdown")
create_dropdown.click()

select_artical = driver.find_element(By.CLASS_NAME,"atg-p-8")
select_artical.click()

# Upload the Image Here Use  OS for Define The Path of Image

file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']") # Use CSS Selector to find out the path for image upload   
root_dir = os.path.dirname(os.path.abspath(__file__))  # Get absolute path of script's directory
image_path = os.path.join(root_dir, "static", "testing.jpeg")# Use os to find path in system
file_input.send_keys(image_path)
driver.find_element(By.CLASS_NAME, "overlay-image-option").click()

select_artical = driver.find_element(By.ID,"hpost_btn")
select_artical.click()

post = driver.find_element(By.CLASS_NAME,"cdx-block")
post.send_keys("Best of luck")
post.click()

post = driver.find_element(By.ID,"title")
post.send_keys("this is for testing purpose")

artical = driver.find_element(By.ID,"hpost_btn")
artical.click()

# Log  Current URL of the Webpage

time.sleep(10)
logger.info(f" To see Current Post Visit This URL {driver.current_url}") # Here return the currect url of the webpage 


## Close the Driver 


driver.quit()