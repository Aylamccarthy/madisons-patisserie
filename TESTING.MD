# Testing

Back to [README.MD](README.md)<br>

## Table of contents
* [User Story and Feature Testing](#user-story-and-feature-testing)
* [Automated View Testing](#automated-view-testing)
* [Browser Testing](#browser-testing)
* [Code Validation](#code-validation)
* [Bugs](#bugs)

## User Story and Feature Testing
All the user stories were tested manually comprehensively, including all the representative features, and were documented below with a summary of the steps made for demonstrating the validation of the tests: <br>

### EPIC - VIEWING AND NAVIGATION
#### 1A: US - As a user, I want to understand the purpose of the website from the first interaction with it
* **Acceptance Criteria:** A site user should see information about the promoted bakeshop and its products.
* **Summary:**<br>
    - When a user first navigate the site, he is redirected to the home page where the purpose of the site is described;<br>
    - The home page contains a cover with an image that suggests what products are being sold;<br>
    - The title that exists on the cover clarifies that the website is made for selling baked products;<br>
    - A 'shop now' button is created to attract the user to click on it and redirected to the products page;<br>
    - There is also a suggestive slogan to further inform the user what the website is about.
    - There is also a short description with details about the bakeshop, and an image of the Bakeshop Cafe.<br><br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br>
* **Outcome:** Pass

#### 1B: US - As a user, I want to be able to easily use the site functionalities on all viewports, so I can shop the products from any device
* **Acceptance Criteria:** A user should be able to see a nice design responsive to all devices.
* **Summary:**   
    - The website's features are functional on all types of devices;<br>
    - The headers have been adapted to fit the smaller devices' screens;<br>
    - The forms' inputs have been adapted to fit the smaller devices' screens.<br><br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br>
* **Outcome:** Pass

#### 1C: US - As a user, I want to see a footer with all relevant information present.
* **Acceptance Criteria:** A user should see relevant information and important documents that clarify privacy aspects. 
* **Summary:**<br>
   - The footer contains link to <em>All products page;</em><br>
   - The footer contains link to <em>Privacy And Policy</em> document for the website;<br>
   - The footer contains link to <em>Terms & Conditions</em> document for the website;<br>
   - The footer contains links to different social media pages.<br><br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br>
* **Outcome:** Pass   

#### 1D: US - As a user, I want to be able to access a navigation menu at any time, so I can easily navigate through the website content
* **Acceptance Criteria:** A site user should always have access to the navigation menu so he can easily switch between pages at any time.
* **Summary:**<br>
    - When a user visits the website he can easily see the navigation menu at the top of the page;<br>
    - Even if switching the pages, the navigation menu is always present and indicates what page is active;<br>
    - The navigation menu is set to sticky so it is always fixed on the top of the page;<br>
    - For logged-in users, the menu contains an additional page, <em>My Profile</em>, and <em>Logout</em> link replaces <em>Register</em> and <em>Login</em> pages;<br>
    - For logged-in staff members, the navigation includes <em>Orders</em>Orders, instead of <em>Profile</em>, as well as <em>Add a new product</em> link.<br><br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br>
* **Outcome:** Pass 

#### 1E: US - US - As a user, I want to be able to search through site products by entering a keyword
* **Acceptance Criteria:** A site user should be able to use the search feature for filtering through site products.
* **Summary:**<br>
    - A search bar is present at any time on the top navigation header;<br>
    - The user can enter and submit any keyword; <br>
    - The websites display only the products that contain in their description the keyword entered by the user, or an informative text if no product matches the search query; <br><br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br>
* **Outcome:** Pass 

### EPIC - USER REGISTRATION/AUTHENTICATION
#### 2A: US - As a user, I want to be able to register on the website
* **Acceptance Criteria:** A site user should be able to create an account by filling in a form on the website.
* **Summary:**<br>
    - There is a Register page that provides a form with email, username and password for the user to fill in;<br>
    - When the user submits the form he is redirected to a page that informs him that he needs to verify his email to finalize the signup process;<br>
    - An info alert is displayed with the message "Confirmation e-mail sent to..." that suggests the user needs to verify his email.<br><br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass 

#### 2B: US - As a user, I want to be able to confirm my account with an email
* **Acceptance Criteria:** A site user should be able to confirm his account using his email.
* **Summary:**<br>
    - An email is sent to the user when he tries to register on the page;<br>
    - The email includes a link that will redirect him to a page from the shop website where he can confirm the email by clicking on a button.<br><br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass

#### 2C: US - As a user/admin, I want to be able to authenticate using only email and password
* **Acceptance Criteria:** A site user should be able to authenticate at any time with email and password.
* **Summary:**  
    - There is a Login page that provides a form with email and password to be filled;<br> 
    - The authentication form has a "Remember me" checkbox that will keep the user logged in;<br> 
    - A success alert is displayed with the message "Logged in as..." that confirms to the user that he has been logged in successfully.<br> <br> 
    
    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass

#### 2D: US - As a user, I want to be able to reset my password in case I forgot it
* **Acceptance Criteria:** A site user should be able to reset his password with his email.
* **Summary:**    
    - On the <em>Login</em> page there is a clickable link with the text <em>Forgot password?</em>;<br>
    - The link redirects the user to a page where he can enter the email address where he wants to receive the email for resetting the password;<br>
    - An email is sent to the specified address with a link;<br>
    - The link redirects the user to a page on the shop website where he can enter and submit the new password;<br>
    - The user can now authenticate with the updated password.<br><br> 
    
    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass

#### 2E: US - As a user/admin, I want to be able to log out at any time
* **Acceptance Criteria:** A site user should be able to exit the current account at any time.
* **Summary:**    
    - There is a Logout modal that can be triggered when clicking on the hyperlink in the navbar. The modal is implemented as part of a defensive programming;<br> 
    - The logout modal asks the user again if he wishes to log out of the current account;<br> 
    - A success alert is displayed with the message "Logged out" that confirms to the user that he has been successfully logged out.<br><br> 
    
    *By testing all these features, it can be affirmed that the user story is accomplished.*<br>
* **Outcome:** Pass

### EPIC - PRODUCTS
#### 3A: US - As a user, I want to see a catalogue with all the products and also grouped by categories
* **Acceptance Criteria:** A user should be able to access a page with all the products, and other pages for every category.
* **Summary:**<br> 
   - In the navigation menu there are separate links that redirect the user to the products' catalogue. These links are classified as: <em>All products</em>, <em>Cakes</em>, <em>Everday Essentials</em>, <em>Sweet Treats</em> and <em>Desserts</em>;<br><br>

    *By testing this feature, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass

#### 3B: US - As a user, I want to be able to apply filters and sort the listed products, so I can easily find the ones I am interested to buy
* **Acceptance Criteria:** A user should be able to apply filters for different types of wine selections.
* **Summary:**<br>
   - On the pages that contain a list of products, there is a filtering section on the top of the page;<em>
   - Every filter is a dropdown with the values corresponding to the list of wines displayed;<br>
   - When a user chooses a value for filtering, the active filter is removed from the filters' list and added to a list of active filters;<br>
   - Any applied filter can be cancelled and the list of products will be displayed only considering the active filters;<br>
   - There is a button for removing all the filters at once;<br>
   - There is also a select input for sorting the products;<br>
   - All sorting options work properly;<br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass

#### 3C: US - As a user, I want to be able to see the stock availability for low-stock products
* **Acceptance Criteria:** A user should see a banner with text that informs him about the product's availability.
* **Summary:**<br>
    - Every product that is in low stock contains a banner element with information about its value;<br>
    - The banner is also visible on the product's details page;<br><br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass

#### 3D: US - As a user, I want to see a page with full specifications for every product, so I can easily decide which one I would want to buy
* **Acceptance Criteria:** A user should have access to every product's full description
* **Summary:**<br>
    - Every item listed on products' pages is clickable and it redirects to the selected product's details page;<br>
    - The details page includes the product's name, price, and a short description of the product;<br><br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass

#### 3E: US - As a user, I want to be able to add any product to the shopping bag in a selected quantity
* **Acceptance Criteria:** A user should be able to select the quantity value and add any product to the shopping bag.
* **Summary:**<br>
   - There is a container with input for quantity and an <em>Add to bag</em> button on every element listed in products pages;<br>
   - There is a container with input for quantity and an <em>Add to bag</em> button on every product detail page;<br>
   - The quantity input has validation that doesn't allow the user to insert and submit a value greater than the stock value or smaller than 1; <br>
   - When a product is added to the shopping bag an alert is triggered with the success message "Added ... to your bag"<br>
   - When the same product is added to the shopping bag, only the quantity value is updated and an alert is triggered with the success message "Updated ... quantity to ...".<br><br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass

#### 3F: US - As an admin, I want to be able to edit product details 
* **Acceptance Criteria:** An admin user should have access to a form to update specifications for any product.
* **Summary:**<br>
    - When a user is logged in as admin, the page for product details replaces the section for updating shopping bag
    with another section that includes a button for <em>Edit product</em>;<br>
    - When the button is clicked, a modal is triggered and contains a form for editing every detail of the product;<br>
    - The form is prefilled with existing data;<br>
    - The form has validation that prevents the user to update a product with invalid information;<br>
    - Any update is reflected in the product's details page;<br><br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br><br> 
* **Outcome:** Pass

#### 3G: US - As an admin, I want to be able to delete products from the catalogue, so it reflects the existing stock
* **Acceptance Criteria:** An admin user should be able to delete any product.
* **Summary:**<br>
   - When a user is logged in as admin, the page for product details replaces the section for updating shopping bag
    with another section that includes a button for <em>Delete product</em>;<br>
    - The button triggers a modal that asks the admin to confirm the deletion of the item/product, as part of the defensive programming;<br>
    - After deletion, the item is removed from the products' list.<br><br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass

#### 3H: US - As an admin, I want to be able to add new products to the catalog, so it reflects the existing stock
* **Acceptance Criteria:** An admin user should have access to a form for adding a new product.
* **Summary:**<br>
    - When a user is logged in as admin, the navigation panel includes a link for <em>Add a new product</em>;<br>
    - When the link is clicked, a modal is triggered and contains a form with fields for every detail of the product;<br>
    - The form has validation that prevents the user to add a product with invalid information.
    - After the form is submitted, the element is added to the products' list.<br><br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass
### EPIC - REVIEWS
#### 4A: US - As a user, I want to be able to see all the reviews added for any product, so I can easily make an opinion about its quality
* **Acceptance Criteria:** A user should have access to all the reviews for any product.
* **Summary:**<br>
    - All the reviews registered for a product are listed on the <em>Product details</em> page;
    - Every review element has an attractive design and contains relevant details such as User name, Review text, Star rating and Date and Time of posting;
    - The reviews are ordered by time in a reverse way so that the last added review is the first on the list.<br> <br> 
    
    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass

#### 4B: US - As a logged-in user, I want to be able to add a review for any product I want
* **Acceptance Criteria:** A logged-in user should be provided with a way of adding a review for any product.
* **Summary:**<br> 
    - On the <em>Product details</em> page there is a section for "Add a review" only visible for authenticated users that are not staff members, as this action wouldn't make sense for admins to make;<br>
    - For a user that hasn't already added a review to the list, there is a form to fill in for creating one;
    - The form only contains an input for the review message to be posted, and a star rating functionality was implemented with a default value of 1 star;<br>
    - There is no implementation for approval of the reviews for the purpose of full transparency;<br>
    - When the review is posted, an alert is triggered confirming that the review was successfully added to the list;<br>
    - The response is immediate and the review appears as the first on the list; <br><br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass 

#### 4C: US - As a logged-in user, I want to be able to see and edit my reviews added to products
* **Acceptance Criteria:** A logged-in user should be able to see and edit his review added to a product.
* **Summary:**<br> 
    - If the current user already added his review, it is displayed in the section "Your review";<br>
    - For editing the review, a form is displayed when the user clicks on the Update button;<br>
    - The form already contains the text of the review to be edited, and the Star rating feature has by default the initial value;<br>
    - When the user submits the edited review, an alert is triggered to confirm that the update was successful;<br>
    - The date and time are updated with the current ones and the review becomes first on the list;<br>
    - "Your review" section updates its values as well;<br>
    - It has been tested the updating of the current review entry using the URL and no action is performed. Also when it was tested for another user's review, the custom 403(forbidden) page appears;<br><br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass

#### 4D: US - As a user, I want to be able to see a general review of every product
* **Acceptance Criteria:** A user should be able to see the general rating of any product if available.
* **Summary:**<br> 
    - Every product has a general rating value which is calculated as an average of all the corresponding reviews values.
    - The rating is displayed on the product's details page and for every element listed on the products' pages.<br>
    - When a user posts a review, it also influences the value of the product's rating.<br>
    - When a user updates a review, it also influences the value of the product's rating.<br><br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass

### EPIC - WISHLIST
#### 5A: US - As a logged-in user, I want to be able to add/remove any product from the Wishlist
* **Acceptance Criteria:** A logged-in user should be able to add a product to the wishlist through an implemented feature.
* **Summary:**<br>
    - On every product's details page there is a wishlist feature visible only to users that are authenticated and not staff members, considering that this feature wouldn't make sense for admins;<br>
    - To add a product object to the wishlist, a form is displayed with an empty heart icon that acts like a button, and a suggestive message, "Add to wishlist", that indicates to the user what is its purpose;<br>
    - When the user clicks on the button, the change is visible immediately, as the heart icon changes its shape into a filled heart, and the message is now "Remove from Wishlist";<br>
    - The change is also reflected in the Wishlist page where the list of products includes only the ones that are currently in the wishlist database;<br>
    - By clicking on the filled heart, the form comes back to its initial state, and the relevant product is removed from the list.<br><br>
    
    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass

#### 5B: US - As a logged-in user, I want to see all the products added to the wishlist
* **Acceptance Criteria:** A logged-in user should be able to access a page with all the favourite products.
* **Summary:**<br>
    - For an authenticated user the content of the Wishlist page is available with all the products added to the wishlist;<br>
    - The page content is not accessible to admins or guest users;<br>
    - Every product element is clickable and redirects to the details page.<br><br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass

#### 5C: US - As a logged-in user, I want to be able to apply filters and sort the products in the wishlist
* **Acceptance Criteria:** A logged-in user should be able to apply filters for different types of wine selections on the Wishlist page.
* **Summary:**<br>
    - On the wishlist page, there is a filtering section on the top of the page;<em>
    - Every filter is a dropdown with the values corresponding to the list of wines displayed;<br>
    - When a user chooses a value for filtering, the active filter is removed from the filters' list and added to a list of active filters;<br>
    - Any applied filter can be cancelled and the list of products will be displayed only considering the active filters;<br>
    - There is a button for removing all the filters at once;<br>
    - There is also a select input for sorting the products;<br>
    - All sorting options work properly;<br><br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass


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

<img src="media/pp5_html_validation.png" width="60%"><br><br>

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
* About
* Login/Register
* 403/404/500 custom pages

### CSS

The CSS code was validated using [W3 Jigsaw Validator](https://jigsaw.w3.org/css-validator/)<br>
At the time of deployment the validation for *base.css* has the following outcome:<br><br>

<img src="media/pp5_css_valid.png" width="60%"><br><br>

### Javascript

The Javascript code was validated using using [JsHint](https://jshint.com/)<br>
At the time of deployment the validation for *script.js* and *stripe_elements.js* have the following outcome:<br>
<details>
<summary>script.js</summary>
<img src="media/js_validation.png" width="40%"><br><br>
</details>
<details>
<summary>stripe_elements.js</summary>
<img src="media/js_validation_stripe.png" width="40%"><br><br>
</details>

* The warnings listed are caused by the EventListeners added to elements in a loop.<br>
I tried to solve the issue but no successful method has been found, so I chose to ignore the warning as it is not affecting the way my code works in any way.

### Python
The python code was tested using [Code Institute python linter](https://pep8ci.herokuapp.com/) online validator.<br>
At the time of deployment the python code validation have the following outcomes:<br><br>

<details>
<summary>Main App</summary>
<img src="media/context_processor.png" width="70%"><br><br>
<img src="media/main_url.png" width="70%"><br><br>
<img src="media/settings.py.png" width="70%"><br><br>
</details>
<details>
<summary>Bag App</summary>
<img src="media/bag_context.png" width="70%"><br><br>
<img src="media/bag_test.png" width="70%"><br><br>
<img src="media/bag_url.png" width="70%"><br><br>
<img src="media/bag_views.png" width="70%"><br><br>
</details>
<details>
<summary>Checkout App</summary>
<img src="media/checkout_app1.png" width="70%"><br><br>
<img src="media/checkout_app2.png" width="70%"><br><br>
<img src="media/checkout_app3.png" width="70%"><br><br>
<img src="media/checkout_app4.png" width="70%"><br><br>
<img src="media/checkout_app5.png" width="70%"><br><br>
<img src="media/checkout_app6.png" width="70%"><br><br>
<img src="media/checkout_app7.png" width="70%"><br><br>
<img src="media/checkout_app8.png" width="70%"><br><br>
<img src="media/checkout_app9.png" width="70%"><br><br>
</details>
<details>
<summary>Contact App</summary>
<img src="media/contact_app1.png" width="70%"><br><br>
<img src="media/contact__app2.png" width="70%"><br><br>
</details>
<details>
<summary>Newsletter App</summary>
<img src="media/newsletter_app1.png" width="70%"><br><br>
<img src="media/newsletter_app2.png" width="70%"><br><br>
<img src="media/newsletter_app3.png" width="70%"><br><br>
<img src="media/newsletter_app4.png" width="70%"><br><br>
</details>
<details>
<summary>Product Reviews App</summary>
<img src="media/review_app1.png" width="70%"><br><br>
<img src="media/review_app2.png" width="70%"><br><br>
<img src="media/reviews_app3.png" width="70%"><br><br>
<img src="media/reviews_app4.png" width="70%"><br><br>
<img src="media/reviews_app5.png" width="70%"><br><br>
</details>
<details>
<summary>Products App</summary>
<img src="media/products_app1.png" width="70%"><br><br>
<img src="media/products_app2.png" width="70%"><br><br>
<img src="media/products_app3.png" width="70%"><br><br>
<img src="media/products_app4.png" width="70%"><br><br>
<img src="media/products_app5.png" width="70%"><br><br>
<img src="media/products_app6.png" width="70%"><br><br>
<img src="media/products_app7.png" width="70%"><br><br>
</details>
<details>
<summary>Profiles App</summary>
<img src="media/profiles_app1.png" width="70%"><br><br>
<img src="media/profiles_app2.png" width="70%"><br><br>
<img src="media/profiles_app3.png" width="70%"><br><br>
<img src="media/profiles_app4.png" width="70%"><br><br>
<img src="media/profiles_app6.png" width="70%"><br><br>


</details>
<details>
<summary>Voucher App</summary>
<img src="media/vouchers_app1.png" width="70%"><br><br>
<img src="media/vouchers_app2.png" width="70%"><br><br>
<img src="media/vouchers_app3.png" width="70%"><br><br>
<img src="media/vouchers_app4.png" width="70%"><br><br>
<img src="media/vouchers_app5.png" width="70%"><br><br>
</details>
<details>
<summary>Wishlist App</summary>
<img src="media/wishlist_app1.png" width="70%"><br><br>
<img src="media/wishlist_app2.png" width="70%"><br><br>
<img src="media/wishlist_app3.png" width="70%"><br><br>
<img src="media/wishlist_app4.png" width="70%"><br><br>
<img src="media/wishlist_app5.png" width="70%"><br><br>
<img src="media/wishlist_app6.png" width="70%"><br><br>
</details>

### Accesibility 
The accesibility of the website was tested with [Wave](https://wave.webaim.org/)

**Wave results:**<br>
<details>
<summary>Home page</summary>
<img src="media/wave_home.png" width="30%"><br><br>
</details>
<details>
<summary>Products page</summary>
<img src="media/wave_products.png" width="30%"><br><br>
</details>
<details>
<summary>Login page</summary>
<img src="media/wave_signin.png" width="30%"><br><br>
</details>
<details>
<summary>Register page</summary>
<img src="media/wave_register.png" width="30%"><br><br>
</details>
<details>
<summary>About page</summary>
<img src="media/wave_about.png" width="30%"><br><br>
</details>
<details>
<summary>Contact page</summary>
<img src="media/wave_contact.png" width="30%"><br><br>
</details><br>







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