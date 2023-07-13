from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#gets subreddit to scrape from user
subreddit = input("Enter subreddit to scrape: ")

driver = webdriver.Firefox()
driver.get("https://old.reddit.com/r/" + subreddit)



#elem = driver.find_element(By.NAME, "q")
#elem.clear()
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
