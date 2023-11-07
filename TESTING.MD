
#### Links

* Ensure the external links to social media present in the footer open up in new tabs.

## Automated View Testing
### Test Overview

* **Home App**<br>
Tests applied for user stories: **#1, #2 #7**<br>
<img src="media/test_home.png"><br><br>

* **Products App**<br>
Tests applied for user stories: **#10, #11, #12**<br>
<img src="media/test_products.png"><br><br>

* **Bag App**<br>
Tests applied for user stories: **#15, #16**<br>
<img src="media/test_bag.png"><br><br>

* **Checkout App**<br>
Tests applied for user stories: **#17, #18, #22**<br>
<img src="media/test_checkout.png"><br><br>

* **Product Reviews App**<br>
Tests applied for user stories: **#13, #11**<br>
<img src="media/test_product_reviews.png"><br><br>

* **Wishlist App**<br>
Tests applied for user stories: **#19, #14**<br>
<img src="media/test_wishlist.png"><br><br>

* **Profiles App**<br>
Tests applied for user stories: **#19, #20, #21**<br>
<img src="media/test_profiles.png"><br><br>

* **Vouchers App**<br>
Tests applied for user stories: **#22**<br>
<img src="media/test_vouchers.png"><br><br>

* **Newsletter App**<br>
Tests applied for user stories: **#8**<br>
<img src="media/test_newsletter.png"><br><br>

### Test Coverage
For generating a report with the coverage of the automated tests, [coverage](https://coverage.readthedocs.io/en/coverage-5.5/) module was used.<br>
Full coverage results:<br><br>
<img width="80%" src="media/coverage_report.png"><br><br>
<img src="media/coverage_report2.png"><br><br>

## Browser Testing
The website was tested on different browser to ensure all features work accordingly.
* Chrome
* Edge
* Safary
* Opera
* Firefox

## Code Validation
### HTML

The html code of the website was validated using [W3 Markup Validator](https://validator.w3.org/).<br>
At the time of deployment the validation have the following outcome:<br><br>

<img src="media" width="40%"><br><br>

The following pages have been tested:
* Home
* Products
* Product details
* Bag
* Checkout
* Checkout Success
* User Profile
* Admin Orders
* Wishlist
* FAQs
* Contact
* Login/Register
* 403/404/500 custom pages

### CSS

The CSS code was validated using [W3 Jigsaw Validator](https://jigsaw.w3.org/css-validator/)<br>
At the time of deployment the validation for *base.css* has the following outcome:<br><br>

<img src="media/pp5_css_validation.png" width="60%"><br><br>








## BUGS
### Solved
* ** Duplicate key error. 
     When I added the unique attribute on sku and code fields (to ensure that all the products skus and codes are unique and therefore will prevent error of duplication for future data entries), I got the duplicate key error. I found this bug significantly challenging as I have never encountered it from previous problem. And also because this is my first experience implementing fixtures file on a project, this bug had been so challenging but at the same time a great learning experience.
     Solution:
     After research and tutor and mentor consultation, I reset my database. Make migrations again. Create a new superuser. And reload data again.

* ** Stripe Element not working as expected.
     When I implemented stripe payments and try to check that everything works, I could only go as far as 'Complete Order' but it wouldn't bring me to success checkout page as expected.
     Solution:
     It turns out that I am using the slim version of JQuery which doesn't support fadeToggle. By switching to normal minified version, the issue was fixed.


### Unsolved