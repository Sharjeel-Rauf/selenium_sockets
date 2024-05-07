# Import required modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys

# Create Chrome options
chrome_options = Options()
# Path to your Chrome profile
profile_path = r"C:/Users/ehsan/AppData/Local/Google/Chrome/User Data/Default"
chrome_options.add_argument(f"--user-data-dir={profile_path}")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)
# Keep the browser open after the script finishes
chrome_options.add_experimental_option("detach", True)
# Specify the path to ChromeDriver
service = Service(executable_path="C:\\Program Files (x86)\\chromedriver.exe")

# Initialize the Chrome WebDriver with the specified service and options
try:
    driver = webdriver.Chrome(service=service, options=chrome_options)
except Exception as e:
    print(f"Error initializing Chrome WebDriver: {e}")
    exit()

# Navigate to the YouTube video URL
video_url = "https://www.youtube.com/watch?v=b5jt2bhSeXs&ab_channel=TechWithTim"
driver.get(video_url)

# Introduce a delay to allow the page to load
time.sleep(5)

# Define the CSS selector to locate the "Sign in" button based on its class attribute
css_selector_signin = (
    ".yt-spec-button-shape-next.yt-spec-button-shape-next--outline"
    ".yt-spec-button-shape-next--call-to-action"
    ".yt-spec-button-shape-next--size-m"
    ".yt-spec-button-shape-next--icon-leading"
)

# Locate the "Sign in" button using the CSS selector and wait until it is clickable
try:
    signin_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector_signin))
    )
    # Click the "Sign in" button
    signin_button.click()
    print("Successfully clicked the Sign In button.")
except Exception as e:
    print(f"Error clicking Sign In button: {e}")


try:
    email_input = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "identifierId"))
    )

    # Enter the email address into the input element
    email_address = "sharjeel03317840080@gmail.com"
    email_input.send_keys(email_address)

    # Send an ENTER key to submit the email
    email_input.send_keys(Keys.ENTER)

    # Introduce a delay to allow the page to process the action
    time.sleep(5)

except Exception as e:
    # Handle any exceptions that may occur
    print(f"An error occurred: {e}")

# Wait for the password input element to be present
try:
    password_input = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.NAME, "Passwd"))
    )

    # Enter the password into the input element
    password = "SHETAAN1234"  # Replace with your actual password
    password_input.send_keys(password)

    # Send an ENTER key to submit the password
    password_input.send_keys(Keys.ENTER)

    # Introduce a delay to allow the page to process the action
    time.sleep(5)

except Exception as e:
    # Handle any exceptions that may occur
    print(f"An error occurred: {e}")





# Define the CSS selector to locate the "Like" button based on its class attribute
css_selector = (
    ".yt-spec-button-shape-next.yt-spec-button-shape-next--tonal"
    ".yt-spec-button-shape-next--mono.yt-spec-button-shape-next--size-m"
    ".yt-spec-button-shape-next--icon-leading"
    ".yt-spec-button-shape-next--segmented-start"
)

# Locate the "Like" button using the CSS selector and wait until it is clickable
like_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector))
)

# Click the "Like" button
like_button.click()

# Print a message indicating successful clicking of the Like button
print("Successfully clicked the Like button.")


# # Navigate to the YouTube video URL
# video_url = "https://www.techwithtim.net/tutorials"
# driver.get(video_url)

# # Print the page title
# print(driver.title)

# # Wait for the like button to be clickable on the page
# try:
#     print("Waiting for the element to be present...")
#     # Locate the element using XPath
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "tutorial__TutorialCardContainer-sc-1rebzxr-0 kiZnIX"))
#     )
#     print("Element found:", element.text)
#     # Click the element
#     element.click()
# except Exception as e:
#     print("An error occurred:", e)
#     print("Like button not found within the timeout period.")
#     driver.quit()
