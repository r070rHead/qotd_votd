from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import json
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless") # Run Chrome in headless mode
chrome_options.add_argument("--no-sandbox") # Disable sandbox
chrome_options.add_argument("--disable-dev-shm-usage") # Overcome limited resources in Docker

# Set up Selenium WebDriver with WebDriver Manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Open the target webpage
    url = "https://www.churchofjesuschrist.org/my-home?lang=eng"
    driver.get(url)

    # Wait for the page to load JavaScript content
    time.sleep(5)  # Adjust this wait time as needed

    # Locate the "of-the-day" div by its ID
    content_div = driver.find_element(By.ID, "of-the-day")

    # Extract the text content
    all_text_content = content_div.text
  
    # Extract the HTML content
    all_html_content = content_div.get_attribute("outerHTML")

    # Format the data into a dictionary
    output = {
        "all_text_content": all_text_content,
        "all_html_content": all_html_content
    }

    # Save the data to a JSON file
    with open("output.json", "w") as file:
        json.dump(output, file, indent=2)

    # Print the output for verification
    print(json.dumps(output, indent=2))

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Quit the WebDriver
    driver.quit()
