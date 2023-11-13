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
#### 5D: US - As a logged-in user, I want to be able to add products to the shopping bag from the Wishlist page
* **Acceptance Criteria:** A logged-in user should be able to select the quantity value and add any product to the shopping bag from the Wishlist page.
* **Summary:**<br>
   - There is a container with input for quantity and an <em>Add to bag</em> button on every element listed on Wishlist page;<br>
   - There is a container with input for quantity and an <em>Add to bag</em> button on every product detail page;<br>
   - The quantity input has validation that doesn't allow the user to insert and submit a value greater than the stock value or smaller than 1; <br>
   - When a product is added to the shopping bag an alert is triggered with the success message "Added ... to your bag"<br>
   - When the same product is added to the shopping bag, only the quantity value is updated and an alert is triggered with the success message "Updated ... quantity to ...".<br><br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass

#### 5E: US - As a user, I want to see how many times a product has been added to the Wishlist by all the users
* **Acceptance Criteria:** A user should see the number of times a product has been added to the Wishlist by all the users for creating a better idea of its popularity
* **Summary:**<br>
    - On the wishlist page, every product element has a section that includes a heart icon and a value representing the number of times the product has been added to the Wishlist by all the users; <br><br>

    *By testing this feature, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass
### EPIC - BAG
#### 6A: US - As a user, I want to see all the products I added to the shopping bag
* **Acceptance Criteria:** A user should be able to access a page with all the products added to the shopping bag.
* **Summary:**<br>
    - There is a <em>Shopping bag</em> page with a table that contains every product added to the bag in the selected quantity;<br>
    - The table list reflects the actual state of the added products.<br><br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass
#### 6B: US - As a user, I want to be able to add/remove from the wishlist any product from the shopping bag
* **Acceptance Criteria:** A user should be able to add/remove a product from the wishlist through an implemented feature.
* **Summary:**<br>
   - On the <em>Shopping bag</em> page, for every product in the table there is a wishlist feature visible only to users that are authenticated and not staff members, considering that this feature wouldn't make sense for admins;<br>
    - To add a product object to the wishlist, a form is displayed with an empty heart icon that acts like a button, and a suggestive message, "Add to wishlist", that indicates to the user what is its purpose;<br>
    - When the user clicks on the button, the change is visible immediately, as the heart icon changes its shape into a filled heart, and the message is now "Remove from Wishlist";<br>
    - The change is also reflected in the Wishlist page where the list of products includes only the ones that are currently in the wishlist database;<br>
    - By clicking on the filled heart, the form comes back to its initial state, and the wine is removed from the list.<br><br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass
#### 6C: US - As a user, I want to see all the details about the price for the order
* **Acceptance Criteria:** A user should be able to see a section with price details for the items added to the shopping bag.
* **Summary:**<br>
   - On the <em>Shopping bag</em> page, for every product in the table, the price per item and the total price is displayed;<br>
   - There is also an <em>Order Summary</em> section with full specifications about the total and grand total price, and also the part of it calculated for delivery;<br> 
   - The value from <em>Order Summary</em> section updates according to the shopping bag list of products and quantity update.<br><br> 

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** 
#### 6D: US - As a user, I want to be able to remove a product from the shopping bag
* **Acceptance Criteria:** A user should be able to delete any product from the shopping bag through an implemented feature.
* **Summary:**<br>
   - On the <em>Shopping bag</em> page, for every product in the table there is a feature for deleting the product that is represented by a bin icon;<br>
   - When the users click on the bin icon, a modal is triggered asking for confirmation of deletion, this being implemented as part of defensive programming;<br>
   - After the deletion, the product is removed from the bag.<br><br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:**
#### 6E: US - As a user, I want to be able to edit the quantity of the products
* **Acceptance Criteria:** A user should be able to update the quantity for any product from the shopping bag through an implemented feature.
* **Summary:**<br>
    - On the <em>Shopping bag</em> page, for every product in the table there is a feature for updating the quantity;<br>
    - The feature includes an input with addition and subtraction buttons that can be used to set the value for the quantity;<br>
    - The <em>Update quantity</em> button submit action sets the input value as the quantity value and also updates the price details.<br><br>
   
    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:**
#### 6F: US - As a user, I want that all the discounts announced on the website to be applied properly
* **Acceptance Criteria:** A user should get a 20% discount voucher on registration, as it is announced on the website.
* **Summary:**<br>
    - When a user confirms his account he gets an email with a unique 20% discount code;<br><br>  
   
    *By testing this feature, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:**
#### 6G: US - As a user, I want to be able to add my vouchers to the order
* **Acceptance Criteria:** A user should be able to apply his voucher through an implemented feature. 
* **Summary:**<br>
   - On the <em>Shopping bag</em> page, there is a section with a feature for adding a voucher code;<br>
   - The feature includes a form with only an input for the voucher code;<br>
   - When the voucher code is submitted an element appears as an active voucher and also the discount is reflected in the order summary section;<br>
   - The voucher can be removed by deleting the active voucher element and the price details will come back to the initial state;<br>
   - When the order is completed with the voucher code active, the code will be removed from the database so it can't be used twice.<br><br>
   
    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:**
### EPIC - CHECKOUT
#### 7A: US - As a logged-in user, I want to be able to see and edit my default delivery details for the order
* **Acceptance Criteria:** A logged-in user should be able to see and update his delivery details if they were registered before.
* **Summary:**<br>
    - On the <em>Checkout</em> page there is a form section with fields for delivery information;<br>
    - The form section for delivery details is prefilled with data corresponding to the authenticated user if it exists;<br>
    - If the checkbox with the text <em>Save delivery details to my profile</em> is checked, the profile will be updated with the delivery data from the form on submit;<br><br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass
#### 7B: US- As a user, I want to see the order summary with all the price details
* **Acceptance Criteria:** A logged-in user should be able to see a section with price details for the items added to the checkout.
* **Summary:**<br>
    - On the <em>Checkout</em> page, there is a table with every product added to checkout;<br>
    - On the <em>Checkout</em> page, for every product in the table, the price per item is displayed;<br>
    - There is also an <em>Order Summary</em> section with full specifications about the total price, grand total price, discount and also delivery cost;<br> <br>
    
    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass
#### 7C: US - As a user, I want to be able to add my delivery details for the order
* **Acceptance Criteria:** A guest user should be able to add his delivery details for the order.
* **Summary:**<br>
    - On the <em>Checkout</em> page there is a form section with fields for delivery information;<br>
    - The form can be filled by the user, considering that the fields for <em>Country</em>, <em>County</em> and <em>City</em> are set by default to <q>Ireland</q><q>Cork</q><q>Cork</q> as the shop only delivers to Cork city;<br>
    - If the checkbox with the text <em>Save delivery details to my profile</em> is checked, the profile will be updated with the delivery data from the form on submit;<br><br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass
#### 7D: US - As a user, I want to be able to introduce my card details for payment
* **Acceptance Criteria:** A user should be able to add his payment details in order to complete the order
* **Summary:**<br>
    - On the <em>Checkout</em> page there is a form section with fields for payment information;<br>
    - The form can be filled by the user with the card details;<br>
    - The card input has validation that doesn't accept invalid card details.<br><br>
    
    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass
### EPIC - USER PROFILE
#### 8A: US - As a logged-in user, I want to be able to see and edit my delivery details
* **Acceptance Criteria:** A logged-in user should be able to add his delivery details to the profile page.
* **Summary:**<br>  
    - On the <em>Profile</em> page, there is a form with fields for delivery details;<br>
    - The fields for <em>Country</em>, <em>County</em> and <em>City</em> are set by default to <q>Ireland</q><q>Cork</q><q>Cork</q> as the shop only delivers to Cork city;<br>
    - The form has validation that forces the user to insert only phone numbers with the format available in Ireland;<br>
    - When the user adds or updates the delivery values in the <em>Profile</em> page, the form from the<em>Checkout</em> page is prefilled with the updated data.<br><br> 
    
    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass
#### 8B: US - As a logged-in user, I want to be able to see my orders history
* **Acceptance Criteria:** A logged-in user should be able to see a list of the orders he has made.
    - On the <em>Profile</em> page, there is a table that includes a list of all the orders made by the authenticated user;<br>
    - Every order element displayed in the table contains information about the order number, date, quantity and total price.<br><br>
    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass
#### 8C: US - As a logged-in user, I want to see the full details for every order I placed on the website
* **Acceptance Criteria:** A logged-in user should be able to see a page with full specifications for every order he has made.
* **Summary:**<br> 
   - Every order_number value corresponding to the order elements in the table is a link that redirects the user to a details page for the order;<br>
   - The page contains all the details of the order.<br><br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass
### EPIC - ADMIN MANAGE ORDERS
#### 9A: US - As an admin, I want to be able to see all the orders placed on the website grouped by date
* **Acceptance Criteria:** An admin user should be able to see a list with all the existing orders. 
* **Summary:**<br>  
    - On the <em>Orders</em> page, there is a table that includes a list of all the orders made by all the users;<br>
    - Every order element displayed in the table contains information about order number, date, quantity and total price;<br>
    - The orders are initially displayed for the current day for a better user experience.<br><br>

     *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass
#### 9B: US -As an admin, I want to be able to filter the orders by date
* **Acceptance Criteria:** An admin user should be able to filter the orders by date.
    - Considering that the page displays by default only the orders for the current day, there is a form that is used for filtering the data by date;<br>
    - On submitting the form the orders for the selected date appear with the informative text displaying the date and number of orders;<br><br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass
#### 9C: US -As an admin, I want to see full details of every order placed on the website 
* **Acceptance Criteria:** An admin user should be able to see a page with full specifications for any order.
* **Summary:**<br>  An admin user should be able to see a page with full specifications for every order existent.
   - Every order_number value corresponding to the order elements in the table is a link that redirects the admin to a details page for the order;<br>
   - The page contains all the details of the order.<br><br>

    *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
### EPIC - NEWSLETTER
#### 10A: US - As a user, I want to be able to subscribe to a newsletter, so I can always be up to date with the latest promotions
* **Acceptance Criteria:** A user should be able to register his email to newsletter for getting informed about the latest promotions
* **Summary:**<br>  
    - There is a form available in the footer of every page where the user can register his email;<br>
    - The form has validation that doesn't let the user register the same email twice.<br><br>

     *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass

### EPIC - ABOUT
#### 10B: US - As a user, I want to be able to see information about the website, including their story, philosophy and commitment
* **Acceptance Criteria:** A user should be able to see all the relevant information about the website.
* **Summary:**<br>  
    - The about page of the website include information about the bakeshop such as how they came to be, their philosophy and commitment;<br><br>

     *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass

### EPIC - FAQs
#### 10C: US - As a user, I want to be able to see information about frequently asked questions about the website and their products
* **Acceptance Criteria:** A user should be able to see frequently asked questions about the website
* **Summary:**<br>  
    - The FAQs page of the website contains information about frequently asked questions about the website and their products;<br><br>

     *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass

### EPIC - CONTACT
#### 10D: US - As a user, I want to be able to see all the relevant information of the bakeshop's contact.
* **Acceptance Criteria:** A user should be able to see the bakeshops address, telephone number, email and opening hours
    - The CONTACT page of the website contains information about the bakeshop's address, including a google map, telephone number, email and opening hours;<br><br>

     *By testing all these features, it can be affirmed that the user story is accomplished.*<br> 
* **Outcome:** Pass



### Aditional Manual Testing
#### Error Handling

* Ensure that **403 HTTP** errors display custom 403.html.
    - **Stress Test:** Input a route in the URL for accessing another user content
* Ensure that **404 HTTP** errors display the custom 404.html.
    - **Stress Test:** Input a random route in the URL that can't be found in the declared paths of the project
* Ensure that **500 HTTP** errors display the custom 500.html.
    - **Stress Test:** Set debug to false and try to access a path that has been breaked intentionally.


#### Interface Interaction

* Ensure all interactive elements respond appropriately:
    - **Desktop:**
        - All navbar elements correctly respond to hovering.
        - All buttons correctly respond to hovering.
        - All authentication links correctly respond to hovering
    - **Mobile:**
        - All navbar elements correctly respond to touch.
        - All buttons correctly respond to touch.
        - All authentication links correctly respond to touch


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
The contact page result is showing one error about the map image missing alternative text. I tried to fix it but was unsuccessful.
<img src="media/wave_contact.png" width="30%"><br><br>
</details>
<details>
<summary>FAQs Page</summary>
<img src="media/wave_faqs.png" width="30%"><br><br>
</details>
<details>
<summary>Bag Page</summary>
<img src="media/wave_bag.png" width="30%"><br><br>
</details>
<details>
<summary>Admin Page</summary>
<img src="media/wave_admin_orders.png" width="30%"><br><br>
</details><br>



### Performance
The performance of the website was tested with [Google Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/)

**Lighthouse reports:**<br>
The lighthouse report scores are lower than I expected. I made every effort to increase these scores, but I am still not satisfied with the final outcome. But due to time constraints I was not able to rectify all the errors that are causing poor performance.

I also honestly didn't know how to rectify the SEO error I am getting. Please see screenshots. I consulted with my mentor and he wasn't sure either what was causing this. 
<!-- The main issues for which I couldn't find a solution.<br><br -->
 <img src="media/lighthouse_error1.png" width="40%"><br><br>
  <img src="media/lighthouse_error2.png" width="40%"><br><br>

 The following updates have been made for improving the performance score:
 * Compressed images with [Tiny PNG](https://tinypng.com/)
 * Converted images to <em>webp</em> format
 * Resized images [picresize](https://picresize.com/)

 After these updates were made, the score improved but the lowest score remains <b>67</b> for desktop and <b>64</b> for mobile.
 

#### Desktop
<details>
<summary>Home Page</summary>
<img src="media/lighthouse_desktop_home.png" width="30%"><br><br>
</details>
<details>
<summary>About Page</summary>
<img src="media/lighthouse_desktop_about.png" width="30%"><br><br>
</details>
<details>
<summary>Products Page</summary>
<img src="media/lighthouse_desktop_products.png" width="30%"><br><br>
</details>
<details>
<summary>contact Page</summary>
<img src="media/lighthouse_desktop_contact.png" width="30%"><br><br>
</details>
<details>
<summary>Faqs Page</summary>
<img src="media/lighthouse_desktop_faqs.png" width="30%"><br><br>
</details>
<details>
<summary>Bag Page</summary>
<img src="media/lighthouse_desktop_bag.png" width="30%"><br><br>
</details>
<details>
<summary>Login/Register Page</summary>
<img src="media/lighthouse_desktop_login.png" width="30%"><br><br>
</details>
<details>
<summary>Admin Manage Order Page</summary>
<img src="media/lighthouse_desktop_orderadmin.png" width="30%"><br><br>
</details>

#### Mobile
<details>
<summary>Home Page</summary>
<img src="media/lighthouse_mobile_home.png" width="30%"><br><br>
</details>
<details>
<summary>About Page</summary>
<img src="media/lighthouse_mobile_about.png" width="30%"><br><br>
</details>
<details>
<summary>Products Page</summary>
<img src="media/lighthouse_mobile_products.png" width="30%"><br><br>
</details>
<details>
<summary>contact Page</summary>
<img src="media/lighthouse_mobile_contact.png" width="30%"><br><br>
</details>
<details>
<summary>Faqs Page</summary>
<img src="media/lighthouse_mobile_faqs.png" width="30%"><br><br>
</details>
<details>
<summary>Bag Page</summary>
<img src="media/lighthouse_mobile_bag.png" width="30%"><br><br>
</details>
<details>
<summary>Login/Register Page</summary>
<img src="media/lighthouse_mobile_login.png" width="30%"><br><br>
</details>
<details>
<summary>Admin Manage Order Page</summary>
<img src="media/lighthouse_mobile_orderadmin.png" width="30%"><br><br>
</details>


## BUGS
I encountered countless bugs during the whole building process of this project. So much so, that I often forget to list them down here and just get my head stuck in solving them. But the ones listed below were the ones that really challenged my tenacity and patience.
### Solved
* **Duplicate key error**
     When I added the unique attribute on sku and code fields (to ensure that all the products skus and codes are unique and therefore will prevent error of duplication for future data entries), I got the duplicate key error. I found this bug significantly challenging as I have never encountered it from previous problem. And also because this is my first experience implementing fixtures file on a project, this bug had been so challenging but at the same time a great learning experience.
     Solution:
     After research and tutor and mentor consultation, I reset my database. Make migrations again. Create a new superuser. And reload data again.

* **Stripe Element not working as expected**
     When I implemented stripe payments and try to check that everything works, I could only go as far as 'Complete Order' but it wouldn't bring me to success checkout page as expected.
     Solution:
     It turns out that I am using the slim version of JQuery which doesn't support fadeToggle. By switching to normal minified version, the issue was fixed.

* **Confirmation email not being sent to the user**
    This bug had been so challenging for me, I thought for the longest time debugging that the error must be coming from the webhook handlers. But after mentor consultation and a bit of guidance form Daisy McGirr, it turned out that format of the confirmation email was what was causing the problem. 
    Solution:
    By switching the format to txt.file instead of an html.file, the issue has been resolved.


### Unsolved
* **Update delivery details returns a 500error**
    The logged in user cannot updated his delivery details, and returns a  NameError: name 'template' is not defined on the terminal. Due to time constraint, I was unable to fix this bug on time.

* **Update delivery details returns a 500error**
    Filter by 'ratings'  return a 500error.

* **Pagination**
    I have tried to implement pagination for the Products page using the class-based view <code>ListView</code> by setting the <code>paginate_by</code> value. The implementation didn't succeed as it seems that the view's feature doesn't work properly with filtered querysets. An alternative way of doing the pagination would be by using javascript but I didn't consider it as being completely necessary and I left it for future implementations because of time constraints.

* **Google Map**
    The google map script is  showing an error on the console. But it is working as expected. 

* **Lighthouse Reports**
    The lighthouse reports are significantly lower than expected, and I honestly do not know how to fix the SEO error I am getting.

Back to [README.MD](README.MD)<br>