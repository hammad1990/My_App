# from flask import Flask
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import requests
from bs4 import BeautifulSoup

# URL = "http://10.20.23.11:5000/"
# URL="https://www.google.com/"
# page = requests.get(URL,verify=False)
# soup = BeautifulSoup(page.content, "html.parser")
# soup.find("input",{"name":"Lemail"})["value"]="m-hamad@petra-eng.com.jo"
# soup.find("input",{"name":"Lpassword"})["value"]="111"




# print(tag.string)
# results = soup.find(id="Model")
# job_elements = results.find_all("div", class_="card-content")
# print(page.content)

browser=webdriver.Chrome(ChromeDriverManager().install())
# browser.get("http://10.20.23.11:5000/",verify=False)
browser.get("https://www.google.com/",verify=False)
# app1=Flask(__name__)

# @app1.route('/')#post means to post to server, get means to get from server.


# def hello():
#   return '<h1>Hello, World!</h1>'


# if __name__=="__main__":
#   app1.run(debug=True)