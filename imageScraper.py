from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import datetime
import requests


#takes webdriver
#assumes subreddit is already loaded
#returns a list of links for comment pages after recursively opening all subreddit pages
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



#takes webdriver and comment page commentURL
#returns a list with image URLs, if there are any
#otherwise returns an empty list
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
            imageLinks.append(previewElement.get_attribute("src").split("?")[0].replace("preview","i"))
        return(imageLinks)

    return(imageLinks)





#gets subreddit to scrape from user
subreddit = input("Enter subreddit to scrape: ")

#the save directory is just the subreddit and date
saveDirectory = subreddit + datetime.datetime.now().strftime("%Y%m%d")

if not os.path.exists(saveDirectory):
    os.makedirs(saveDirectory)

os.chdir(saveDirectory)

#opens subreddit
driver = webdriver.Firefox()
driver.get("https://old.reddit.com/r/" + subreddit)

#check for and bypass "over 18" page

if(driver.title == "reddit.com: over 18?"):
    driver.find_element(By.XPATH,'//button[text()="continue"]').click()


commentLinks = []

#collects all comment pages
commentLinks.extend(recursiveCommentLinkScrape(driver))


imageLinks = []

#opens all comment pages and returns the links for images
for commentLink in commentLinks:
    imageLinks = imageLinks + imageLinkScrape(driver, commentLink)


filename = ""


for imageLink in imageLinks:
    filename = imageLink.split("/")[3]
    localFile = open(filename,'wb')
    localFile.write(requests.get(imageLink).content)
    localFile.close()
