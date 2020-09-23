# Scrapy_Ikang
## Project Description:
Use scrapy in python to crawl: https://mall.ikang.com/ <br />
This is an advanced web-crawling example, because the website has anti-crawler mechanism <br />
Thus, we use selenium package together with scrapy. <br />
Selenium can simulate web-browser actions like opening the browser, scrolling, clicking a button, switching back and forth among tabs, etc. <br />
The key feature to use in selenium is driver. Driver "directs" those actions mentioned above <br />

## Set up
1) Install Google Chrome browser. It's most commonly-used in selenium and probably has the best performance <br />
2) Install chromedriver from: https://chromedriver.chromium.org/downloads <br />
NOTICE: You need to check the particular version of your Chrome and download the corresponding driver.. Find it in setting->About Google Chrome. <br />
3) Unzip the file and put it into your project folder. <br />
4) Install scrapy, selenium package and make sure they can functions in your project environment <br />

## Special Notice
Make sure you put the unzipped chromedriver executable in the correct place, otherwise you get error when initializing the driver. <br />
The STARTER.py file is just for convinience. You don't need to type in the terminal, just run this file in your IDE. <br />
