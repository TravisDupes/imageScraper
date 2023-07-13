from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#gets subreddit to scrape from user
subreddit = input("Enter subreddit to scrape: ")

#opens subreddit
driver = webdriver.Firefox()
driver.get("https://old.reddit.com/r/" + subreddit)

#check for and bypass "over 18" page

if(driver.title == "reddit.com: over 18?"):
    driver.find_element(By.XPATH,'//button[text()="continue"]').click()

#create a list of comment links
commentLinks = []

commentLinks.extend(driver.find_elements(By.PARTIAL_LINK_TEXT, "comment"))

for link in commentLinks:
    print(link.get_attribute("href"))
    print("\n")


#elem = driver.find_element(By.NAME, "q")
#elem.clear()
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
