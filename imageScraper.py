from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import datetime


def recursiveCommentLinkScrape(driver):
    #create a list of comment comment Links
    commentLinks = []

    commentElements = driver.find_elements(By.PARTIAL_LINK_TEXT, "comment")

    if len(commentElements) > 0:
        for commentElement in commentElements:
            commentLinks.append(commentElement.get_attribute("href"))

    nextButton = driver.find_elements(By.LINK_TEXT, "next ›")

    if len(nextButton) > 0:
        nextButton[0].click()
        return(commentLinks + recursiveCommentLinkScrape(driver))

    return(commentLinks)

#gets subreddit to scrape from user
subreddit = input("Enter subreddit to scrape: ")

saveDirectory = "ImageScraper/" + subreddit + datetime.datetime.now().strftime("%Y%m%d")

if not os.path.exists(saveDirectory):
    os.makedirs(saveDirectory)


#opens subreddit
driver = webdriver.Firefox()
driver.get("https://old.reddit.com/r/" + subreddit)

#check for and bypass "over 18" page

if(driver.title == "reddit.com: over 18?"):
    driver.find_element(By.XPATH,'//button[text()="continue"]').click()


commentLinks = []

commentLinks.extend(recursiveCommentLinkScrape(driver))





for link in commentLinks:
    print(link)
    print("\n")


#elem = driver.find_element(By.NAME, "q")
#elem.clear()
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
