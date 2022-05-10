# http-impact-pkkmqg-git.codesubmit.io-impact--qa-automation-lslcrp

# PLEASE NOTE: Project was tested using the latest versions Selenium and Python on PyCharm and the Chrome web driver.

# UI and Functionality Testing was applied in this Test plan


Testing scenario Information : This description for each type of user best describes the test results of each automated test.

TEST RESULTS for Problem User Login ->(Mostly manually Tested)

#Fails
Product images are incorrect , as they do not show the actual products and when the image link is clicked different product names are displayed.

Users cannot add to cart products that like "Sauce Labs Bolt T-Shirt" ,"Sauce Labs Fleece Jacket" and "Test.allTheThings() T-Shirt (Red)" and for

When the product "Sauce Labs Fleece Jacket" is clicked on it displays that the heading "item is not found" but the user is able to add it to the cart

Sorting filter is not functional as it stays on the "Name(A to Z)" option

When the About page is clicked from the burger menu it doesn't show the actual Saucelab about page but instead gives a 404 error message to show that the page doesnt exist.

Reset App State removes items from the cart but it doesn't return the products on the inventory page back to add to cart , the user will have to reload to be able to reset "remove to add to cart"

On the checkout information , the user is only able to enter the zipcode but cannot enter the last name. when they first enter the first name and then enter the last name , the first name is replaced by the last name entered by the user which defers the user from continuing to the checkout as the last name is required.



#TEST RESULTS for Performance User
Semi Successful Test , User is able to perform all website processes but the performance of the website is slow because of the slow loading time.





#TEST RESULTS for Locked out User
 The user is unable to login because they are locked out and an error message is displayed "Epic Sadface : Sorry, this user has been locked out."




#TEST RESULTS for Standard User
Successful Test , User is able to perform all website processes






