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

#    if len(nextButton) > 0:
#        nextButton[0].click()
#        return(commentLinks + recursiveCommentLinkScrape(driver))

    return(commentLinks)

def imageLinkScrape(driver, commentURL):

    imageLinks = []

    driver.get(commentURL)

    postLinkElements = driver.find_elements(By.XPATH,'//a[@class="may-blank post-link"]')
    if len(postLinkElements) > 0:
        for postLinkElement in postLinkElements:
            imageLinks.append(postLinkElement.get_attribute("href"))
        return(imageLinks)


    previewElements = driver.find_elements(By.XPATH,'//img[@class="preview"]')
    if len(previewElements) > 0:
        for previewElement in previewElements:
            imageLinks.append(previewElement.get_attribute("src"))
        return(imageLinks)

    return(imageLinks)





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


imageLinks = []

for commentLink in commentLinks:
    imageLinks = imageLinks + imageLinkScrape(driver, commentLink)




for imageLink in imageLinks:
    print(imageLink)
    print("\n")

#elem = driver.find_element(By.NAME, "q")
#elem.clear()
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
