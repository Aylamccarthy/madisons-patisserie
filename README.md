# Madison's Patisserie - Online Bakeshop
<img src="" ><br>
<hr>

TABLE OF CONTENTS

  - [Overview](#overview)
  - [UX](#ux)
  - [Business Model](#business-model)
  - [Marketing](#marketing)
  - [Agile Methodology](#agile-methodology)
  - [Features](#features)
  - [Responsive Layout and Design](#responsive-layout-and-design)
  - [Tools Used](#tools-used)
  - [Testing](#testing)
  - [Deployment](#deployment)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)

## Overview
Madison's Patisserie is an e-commerce website created for a fictive bakeshop located in Cork, Ireland. The main purpose of the project was to implement a fully functional online store that will make the process of selecting and purchasing baked products much easier for customers.<br>
The users are given the possibility to see every product's details, create a wishlist, add items to the shopping bag, purchase with an online payment and access orders' history. Also, the staff members have permission for controlling the data using specially designed features.<br>
The website was developed using Python(Django), HTML, CSS and JavaScript. The data was stored in a PostgreSQL database using ElephantSql for manipulation.
<br><br>
The fully deployed project can be accessed at [this link]().<br><br>

## UX
This site was created respecting the Five Planes Of Website Design:<br>
### Strategy<hr>
**User Stories:** <br>

|   EPIC                                ||                                User Story                                                   |
| :-------------------------------------|--|:------------------------------------------------------------------------------------------- |
|**VIEWING AND NAVIGATION**             |  ||
|                                       || As a user, I want to understand the purpose of the website from the first interaction with its content |             
|                                       || As a user, I want to be able to easily use the site functionalities on all viewports, so I can shop the products from any device|
|                                       || As a user, I want to see a footer with relevant information and documents|
|                                       || As a user, I want to be able to access a navigation menu at any time, so I can easily navigate through the website content|
|                                       || As a user, I want to be able search through site products by entering a key word|
|**USER REGISTRATION/AUTENTHICATION**   |  || 
|                                       || As a user, I want to be able to register on the website|
|                                       || As a user, I want to be able to confirm my account with an email|
|                                       || As a user/admin, I want to be able to authenticate using only email and password|
|                                       || As a user, I want to be able to reset my password in case I forgot it|
|                                       || As a user/admin, I want to be able to log out at any time|
|**PRODUCTS**                           |  ||
|                                       || US - As a user, I want to see a catalog with all the products and also grouped by categories|
|                                       || US - As a user, I want to be able to apply filters and to sort the listed products, so I can easily find the ones I am interested to buy|
|                                       || US - As a user, I want to be able to see the stock availability for low stock products|
|                                       || US - As a user, I want to see a page with full specifications for every product, so I can easily decide which one I would want to buy|
|                                       || US - As a user, I want to be able to add any product to the shopping bag in a selected quantity|
|                                       || US - As an admin, I want to be able to edit product details|
|                                       ||  US - As an admin, I want to be able to delete products from the catalog, so it reflect the existent stock|
|                                       || US - As an admin, I want to be able to add new products to catalog, so it reflects the existent stock|
|**REVIEWS**                            |  ||
|                                       || US - As a user, I want to be able to see all the reviews added for any product, so I can easily make an opinion about its quality|
|                                       || US - As a logged in user, I want to be able to add a review for any product I want|
|                                       || US - As a logged in user, I want to be able to see and edit my reviews added to products|
|                                       || US - As a user, I want to be able to see a general review of every product|
|**WISHLIST**                           |  ||
|                                       || US - As a logged-in user, I want to be able to add/remove any product from the Wishlist|
|                                       || US - As a logged-in user, I want to see all the products added to Wishlist|
|                                       || US - As a logged-in user, I want to be able to apply filters and to sort the products in the Wishlist|
|                                       || US - As a logged-in user, I want to be able to add products to the shopping bag from the Wishlist page|
|                                       || US - As a user, I want to see how many times a product has been added to Wishlist by all the users|        
|**BAG**                                |  ||
|                                       || US - As a user, I want to see all the products I added to the shopping bag|
|                                       || US - As a user, I want to be able to add/remove from the wishlist any product from the shopping bag|
|                                       || US - As a user, I want to see all the details about the price for the order|
|                                       || US - As a user, I want to be able to remove a product from the shopping bag|
|                                       || US - As a user, I want to be able to edit the quantity of the products|
|                                       || US - As a user, I want that all the discounts announced on the website to be applied properly|
|                                       || US - As a user, I want to be able to add my vouchers to the order|
|**CHECKOUT**                           |  ||
|                                       || US - As a logged-in user, I want to be able to see and edit my default delivery details for the order|
|                                       || US- As a user, I want to see the order summary with all the price details|
|                                       || US - As a user, I want to be able to add my delivery details for the order|
|                                       || US - As a user I want to be able to introduce my card details for payment|
|**USER PROFILE**                       |  ||
|                                       || US - As a logged in user, I want to be able to see and edit my delivery details|
|                                       || US - As a logged-in user, I want to be able to see my orders history|
|                                       || US - As a logged-in user, I want to see the full details for every order I placed on the website|
|**ADMIN MANAGE ORDERS**                |  ||
|                                       || US - As an admin, I want to be able to see all the orders placed on the website grouped by date|
|                                       || US -As an admin, I want to be able to filter the orders by date|
|                                       || US -As an admin, I want to see full details of every order placed on the website|
|**NEWSLETTER**                         |  ||
|                                       || US - As a user, I want to be able to subscribe to a newsletter, so I can always be up to date with the latest promotions|