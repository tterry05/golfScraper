from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from pushbullet import Pushbullet
import configparser
import requests
from selenium.webdriver.common.by import By

config = configparser.ConfigParser()
config.read('config.ini')
api_key = config['API']['key']
google_key = config['GOOGLEAPI']['googleapi']

emailName = config['EMAIL']['email']
passwordName = config['PASS']['pass']

pb = Pushbullet(api_key)
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.groupgolfer.com/account/login.php")

email = driver.find_element(By.ID, "email")
email.send_keys(emailName)
password = driver.find_element(By.ID, "password")
password.send_keys(passwordName)
button = driver.find_element(By.NAME, "signin")
button.click()

yourAddress = "yourAddress"
# temp code to use ohio page for testing
# modal = driver.find_element(By.CLASS_NAME, "js-modal-show")
# modal.click()
# link_element = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/ul/li[17]/a")
# link_element.click()

try:
    address = driver.find_element(By.CLASS_NAME, "vendor-address")

    # Define origin and destination addresses
    origin_address = yourAddress
    destination_address = address.text

    # Build the request URL
    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={origin_address}&destinations={destination_address}&mode=driving&key={google_key}"

    # Send request and get response
    response = requests.get(url)

    # Check for successful response

    if response.status_code == 200:
        data = response.json()

        # Extract travel time in minutes
        print(data)
        travel_time = data["rows"][0]["elements"][0]["duration"]["value"] / 60
        time = {travel_time}.pop()
        formatted_time = "{:.2f}".format(time)

        pb.push_note("Group Golfer", "The travel time is " + str(
            formatted_time) + " minutes." + "\n" + "The vendor address is " + address.text)


except NoSuchElementException:
    pb.push_note("Group Golfer", "No golf deal available today")

driver.quit()
