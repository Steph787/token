import requests
# https://docs.python-requests.org/en/latest/
# Why you have to use requests - https://realpython.com/beautiful-soup-web-scraper-python/
# Why I choose BeautifulSoup & have to scrap
# https://gologin.com/blog/web-scraping-with-python#:~:text=First%2C%20choose%20a%20Python%20web,as%20%E2%80%9Cpip%20install%20beautifulsoup4%E2%80%9D.

from bs4 import BeautifulSoup
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

import datetime
# https://docs.python.org/3/library/datetime.html

import time
# https://docs.python.org/3/library/time.html

# identify your URL
url = "https://sis.galvanize.com/cohorts/139/attendance/mine/"


try:
    while True:
    # Send a GET request to the webpage
        print("Sending GET request to", url)
        response = requests.get(url)
        # by using the request import from Python it will make a HTTP request
        # the request.get(URL VARIABLE above)
        # using the .get method
        print("Received response with status code:", response.status_code)


        soup = BeautifulSoup(response.content, 'html.parser')
        # BeautifulSoup is a python library
        # we use the newly named variable called "response" from above
        # https://www.geeksforgeeks.org/response-content-python-requests/ << examples of this .content attribute
        # 'html.parser' is from BeautifuSoup - it will parse html content
        # all of this gets stored in the variable named Soup

        token_element = soup.find("span", {"class": "tag is-danger is-size-6"})
        # called the soup variable to get us parsed info from HTML
        # use the .find method in BeautifulSoup to specify what you are looking for in the HTML
        # https://scrapeops.io/python-web-scraping-playbook/python-beautifulsoup-find/
        # inspected the HTML for the SIS page to find the token element name

        if token_element:
        # this if statement will look for if the token is not empty or NONE
            token = token_element.get_text()
            # we use the variable from above
            # get.text doc https://tedboy.github.io/bs4_doc/8_output.html#get-text
            # create a variable for token post strip
            print("Found token:", token)


            if token:
                submit_url = "https://sis.galvanize.com/cohorts/139/attendance/mine/"
                token_data = {'token': token}
                # inspected the HTML for the input field & token name is token
                # create a dict for
                print("Sending POST request to", submit_url)  # Debug statement

                response = requests.post(submit_url, data=token_data)
                # just like above - requests. will make a request to the HTML
                # instead of .get we are using .post
                # we use the URL above in the different variable than what we used in the get above
                #  we just data=token to tell it what we want to submit from the dict
                print("Received response with status code:", response.status_code)  # Debug statement

        # Check the response for success or error messages
                if response.ok:
                    print("Token submitted successfully.")
                else:
                    print("Token submission failed.")
            else:
                print("Token element not found on the page.")

        time.sleep(10)  # Add a 10-second delay before the next request

except KeyboardInterrupt:
    print("Script terminated by user.")
