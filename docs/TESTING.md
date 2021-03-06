## Code Validation - HTML, CSS, JavaScript, Python

***HTML Validity***

All pages put through [W3C Markup Validator](https://validator.w3.org/nu/) using 'View Page Source' on webpage due to Jinja language.

Errors throughout checking included:

- Error: Stray start tag th.
- - Resolved: Added table tags to django forms

- Warning: Empty heading.
- - Ignored: Jinja block content throughout site but not on index page

- Warning: Section lacks heading. Consider using h2-h6 elements to add identifying headings to all sections.
- - Ignored: No heading necessary.

- Warning: The type attribute is unnecessary for JavaScript resources.
- - Resolved: removed type attribute.

- Warning: Consider using the h1 element as a top-level heading only (all h1 elements are treated as top-level headings by many screen readers and other tools).
- - Resolved: changed to h2.

- Error: An img element must have an alt attribute, except under certain conditions. 
- - Resolved: added in necessary alt tags.

- Error: Duplicate ID id_email.
- - Ignored: Due to looping in jinja language.

- Error: End tag p seen, but there were open elements.
- - Resolved: Error with a tag inside p tag, simple fix.

- Error: Start tag div seen in table. *followed by* Fatal Error: Cannot recover after last error. Any further errors will be ignored.
- - Resolved: Removed div tags from table and replaced with correct table elements.

- Error: Bad value #3-Maple and Oak thumb-stick - blue/black for attribute href on element a: Illegal character in fragment: space is not allowed.
- - Resolved: Delete modals values changed. EG. used product SKU not product name.

- Warning: A table row was 5 columns wide and exceeded the column count established by the first row (3).
- - Resolved: Added in extra columns and displayed as 'none' if unrequired.

The same errors came up through multiple pages and all errors/warnings were fixed if necessary.

***CSS Validity***

CSS validated using [W3C CSS Validation](https://jigsaw.w3.org/css-validator/)

Errors included.

`Value Error : font-style 1.7em is not a font-style value : 1.7em` - resolved: removed.

`1829		Property animate doesn't exist : 0.2s` - resolved: removed.

`1853		Property animate doesn't exist : 0.2s` - resolved: removed.

`1872		Property animate doesn't exist : 0.2s` - resolved: removed.

`2795		Value Error : color Parse Error var()` - resolved: removed.

After fixing errors. No errors found.

![](/docs/img/css-validation.png)

***JavaScript Validity***

JS Validity

All JavaScript code validated using [JSHint](https://jshint.com/)

Any errors were fixed.

Errors included:

- Unused variables.
- - Resolved: Removed.

- Semi colons.
- - Resolved: added in semi colons just for consistency.

- Undefined variables
- - Ignored: Used for gsap, materialize, gliderjs, stripe from other scripts.

- 'arrow function syntax (=>)' is only available in ES6 (use 'esversion: 6').
- - Ignored

- 'template literal syntax' is only available in ES6 (use 'esversion: 6').
- - Ignored

- Do not use 'new' for side effects.
- - Ignored: required for gliderjs

***Python Validity***

- Installed flake8 to check errors in Python code.
- - Warnings in auto generated files ignored.
- - Edited line lengths, unused variables and other errors/warnings.
- Checked all Python files with through [pep8online](http://pep8online.com/) to check PEP8 compliance.
- All files passed.

## User Stories

As an anonymous user, I want to be able to:

- Expected: **navigate site**, so that I can - *find what I'm looking for easily*
- - Logo links directly back to home page.
- - Home link throughout site in header section links back to home page.
- - Blog page links direct to specific blog post page.
- - Products page links direct to specific product detail page.
- - About section link on home page as you scroll down links to about page.
- - Category cards on home page links to products page with selected categories filtered, as expected.
- - - Result: Achieved.

---

- Expected: **search for products**, so that I can - *consider buying something*
- - Searched known post in blog page, page refreshes with correct blogs from search.
- - Searched various incorrect words, page refreshes with '0 blogs found' heading.
- - Searched known product in products page, page refreshes with correct products from search.
- - Searched various incorrect products, page refreshes with '0 products found' heading.
- - - Result: Achieved.

---

- Expected: **filter products**, so that I can - *find exactly what I am looking for easily*
- - Wood filtering button displays sidenav and on click, page refreshes an am shown correct products filtered with wood type.
- - Checked all sort features, page refreshes and correctly orders the products with the chosen sort method.
- - Category links all refresh and display correct products once clicked, including checkmark next to category name.
- - - Result: Achieved.

---

- Expected: **read about products**, so that I can - *understand the product more*
- - Viewed shop now link and clicked individual products, clear description of the product is shown on each page.
- - - Result: Achieved.

---

- Expected: **read about site**, so that I can - *understand about woodturning and how the products are made*
- - Viewed about link in nav to see clear details about the site.
- - Also scrolling down, I can read information about the making of walking sticks.
- - - Result: Achieved.

---

- Expected: **contact site**, so that I can - *enquire about any questions/issues I have*
- - Tried sending contact form with empty fields, was asked to fill in fields.
- - Sent form with correct fields. Received success message and redirected to home page.
- - Received email from DragonEggWoodturning email as an auto reply.
- - - Result: Achieved.

---

- Expected: **register**, so that I can - *save my buying history and details for any other purchases*
- - Tried registering with incorrect fields, non-matching passwords and emails. Displayed error messages detailing errors.
- - Registered with correct details. Received message detailing success sign up and redirected to verify email page detailing that a verification link has been sent to my email.
- - Received email with verification link. Clicked link and confirmed email. Success message displayed and am redirected to login page.
- - - Result: Achieved.

---


- Expected: **buy products**, so that I can - *receive what I like from the store*
- - Added 10 items to bag. Shown success message. Icon displayed next to shopping bag nav icon.
- - Tried adding another item of same type. Shown warning message that only 10 items max allowed.
- - Tried editing bag items in shopping bag. Shown success message and redirected to shopping bag with updated items.
- - Tried removing all items. Shown success message and redirected to shopping bag page with empty bag.
- - Added item, am shown free delivery message.
- - Tried checking out with empty fields, am shown message to fill in fields.
- - - Result: Achieved.

---

- Expected: **make secure payments**, so that I can - *make sure my payments are handled safely*
- - Filled in forms apart from card, am shown card incomplete message.
- - Filled in correct card details and am taken to checkout success page with order number.
- - - Result: Achieved.

---

- Expected: **receive confirmation**, so that I can - *know that I have made the purchase*
- - Recieved email confirmation with order number, order date, order total, shipping details and a contact link.
- - - Result: Achieved.

---

- Expected: **review products**, so that I can - *give my feedback*
- - Product detail page displays warning above review section that I can't edit or delete my review if I post a review.
- - Tried posting a review. Shown success message and redirected to product detail page. My review is displayed with anonymous review as the user.
- - - Result: Achieved.

---

- Expected: **subscribe to newsletter**, so that I can - *stay updated with site's new products and additional information*
- - Tried subscribing with empty field. Was shown fill in field message.
- - Subscribed with correct email. Was shown success message and directed back to home page.
- - Received email from Dragon Egg Woodturning, with unsubscribe link.
- - - Result: Achieved.

---

- Expected: **unsubscribe to newsletter**, so that I can - *stop receiving updates*
- - Clicked on unsubscribe link. Was shown success message that my email has been unsubscribed.
- - - Result: Achieved.

---


As a registered user, I want to be able to:

- Expected: **log in**, so that I can - *view previous buying history and save my details*
- - Tried signing in with incorrect password. Am not able to log in.
- - Tried signing in with correct password. Given success message and am directed to home page with account icon in nav bar.
- - Tried logging out and am given success message and directed back to home page. Account icon no longer in nav bar.
- - Attempting to go to profile url when logged out takes me to log in page.
- - - Result: Achieved.

---

- Expected: **store my details/view profile**, so that I can - *prevent having to enter my details everytime*
- - Profile for logged in user displays my username with details on when I became a member and my last log in date.
- - Profile navigation displays orders table, review table and account info.
- - - Result: Achieved.

---

- Expected: **update details**, so that I can - *save new details if any need to be changed*
- - Tried updating profile and am shown success message. Profile account info is now filled with my data.
- - Checkout form is now filled with account data.
- - - Result: Achieved.

---

- Expected: **view purchase history**, so that I can - *check previous buys to see if I want to buy another*
- - All orders are listed in profile under order history with link to view in full.
- - - Result: Achieved.

---

- Expected: **review products**, so that I can - *give feedback to the store*
- - Tried posting review as logged in user. No warning about editing displayed. Review posted with my review displayed with my user name. Review also now in profile.
- - Tried liking blog post. Given info message saying only logged in users can like a post. Redirected to blog post page.
- - - Result: Achieved.

---

- Expected: **comment on blog posts**, so that I can - *give feedback to the store*
- - Tried commenting on a post. Was given info message saying only logged in users can post. Was redirected to blog post page.
- - Tried commenting on blog post as logged in user. Am shown success message, redirected to post and my comment is now displayed with edit and delete links. Other comments dont have these links.
- - Liked post in blog post page, am shown success message and the thumb icon has filled and like count has increased.
- - Unliked post in blog post page, am shown success message and thumb icon not filled and like count has decreased.
- - - Result: Achieved.

---

- Expected: **edit/delete any comments, reviews I have made**, so that I can - *have full control over my involvement in the site*
- - Tried editing review. Given success message and redirected. Edited review now displayed on product page and in profile.
- - Tried deleting review. Given success message and redirected. Review no longer displayed on product page and in profile.
- - Edit comment link takes me to edit comment page. Editing comment redirects me back to post with success message with new edited comment.
- - Delete link displays pop up delete notification. Confirming delete redirects to post with success message and comment no longer displayed.
- - Tried going back to edit link and am displayed with info message saying it doesn't exist and redirected to home page.
- - - Result: Achieved.

---

As an admin user, I want to be able to:

- Expected: **add new products**, so that I can - *update current stock*
- - Tried add product with empty fields. Was shown fill in field message.
- - Tried add product with correct fields. Was shown success message and redirected to back to profile.
- - New product is now on products page, has its own product detail page and is listed in my admin profile product section.
- - Tested adding product where a category was on sale. Price was updated accordingly.
- - - Result: Achieved.

- Expected: **edit products**, so that I can - *make changes if necessary*
- - Can edit product from profile section. Clicked edit link and am shown edit product page with prefilled data.
- - Edited product, shown success message, redirected to product detail page and updated product is now listed on the site and in my profile section.
- - Can edit product images from profile section. Clicked edit images link and am shown edit images product page with prefilled images.
- - Can select multiple images to upload.
- - Added multiple images, redirected back to edit images page where new images are shown. New images are now shown in product detail page.
- - - Result: Achieved.

- Expected: **delete products**, so that I can - *remove old products if certain products are no longer available in the store *
- - Can delete product images from profile section. Clicked edit images link and am shown edit images product page with prefilled images.
- - Deleted image, shown success message, redirected to edit images page where the deleted image is now no longer there or on the product detail page.
- - Can delete product from profile section. Clicked delete link and am shown delete modal pop up.
- - Deleted product, shown success message and deleted product is now no longer listed on the site or in my profile section.
- - - Result: Achieved.

- Expected: **create blog posts**, so that I can - *give readers an update on what is currently going on with the store and the woodturning work*
- - Tried add blog post with empty fields. Was shown fill in field message.
- - Tried add blog post with correct fields. Was shown success message and redirected to blog page.
- - New blog is now on blog page, has its own blog post page and is listed in my admin profile blog section.
- - - Result: Achieved.

- Expected: **edit blog posts**, so that I can - *make changes if necessary*
- - Can edit blog from blog post page or from profile section. Clicked edit link and am shown edit blog page with prefilled data.
- - Edited blog, shown success message and updated blog is now listed on the site and in my profile section.
- - - Result: Achieved.

- Expected: **delete blog posts**, so that I can - *remove any unwanted posts if necessary*
- - Can delete blog from blog post page or from profile section. Clicked delete link and am shown delete modal pop up.
- - Deleted blog, shown success message and deleted blog is now no longer listed on the site or in my profile section.
- - - Result: Achieved.

- Expected: **add discounts**, so that I can - *provide updates on pricing to users*
- - Set discount for walking sticks. All walking sticks prices now have a line through original price and display updated price. Walking sticks category on home page now has sale icon attached to it. Category name in profile has discount notification displayed. Individual products show discount in product page.
- - Removed discount, all products now back to original price.
- - Set discount for individual product on product detail page. Individual product now shows updated price in product detail page.
- - - Result: Achieved.

- Expected: **send newsletters**, so that I can - *update subscribers on anything relating to new products, new blogs, discounts etc*
- - Tried sending newsletter with incorrect fields. Shown fill in fields notification.
- - Sent newsletter and shown success message and redirected back to profile.
- - Checked a subscriber test email and it had received newsletter email from Dragon Egg Woodturning with unsubscribe link attached also.
- - - Result: Achieved.

## Manual Site Testing

**Responsiveness - mobile, tablet, laptop**

Site tested on multiple screen sizes.

Used [responsitor](https://www.responsinator.com/) to check multiple phones/tablets.

Site on different screen sizes can be seen [here](https://www.responsinator.com/?url=https%3A%2F%2Fdragon-egg-woodturning.herokuapp.com%2F)

**Crud**

- Error: Tried liking blog post. Redirected to log in page
- - Fixed: removed login_required decorator.

- Error: Tried to comment on post. Received ValueError
- - Fixed: edited blog_post view to ensure only authenticated users can post.

- Error: Tried to edit comment. Received Error.
- - Fixed: removed bug in edit comment view.

- Continuously tested adding, editing, deleting of posts, comments, reviews, likes, products etc. throughout build, both in development and production.

**Subscribe and Unsubscribe**

- Tried subscribing with same email. Was shown error message saying email already subscribed.
- Tested unsubscribe links to make sure they work.
- Tested visiting old unsubscribe link to make sure correct message was shown saying 'already unsubscribed'.

**Login/Register/Logout**

- Tested login functionality with incorrect passwords, emails etc.

**Newsletter Forms**

- Tested newsletter is sent to all subscribers.
- Tested confirmation email after subscribing.

**404 and 500**

- Error header styled incorrectly
- - was fixed.

- Incorrect URL directs to 404 page as expected.
- Go home and shop now links all direct to correct page.
- 500 page assumed to be correct.

**Admin**

- Logged in as superuser. Profile has additional sections including newsletter, discounts, products and blogs.

**Footer**

- Tested all footer links to ensure they all work.
- Social Media links all open in new tab.

**Searching/filtering/sorting - Products, Blogs**

- Tested search functionality in both products and blog pages. Results show correct queries.
- Tested sorting products. Results show correct sorting.
- Tested filtering by wood. Filter results show correct filtered products.

**Contact Forms**

- Contact form styled incorrectly
- - was fixed.

- Contact header styled incorrectly
- - was fixed.

- Default email address received email with message sent from contact form.
- Tested auto reply email was sent to email in the contact form.

**Profile**

- Error: going back to edit link displays server error after deleting comment
- - Fixed: added conditional if statements to views where this may be applicable.

- Profile link only visible to logged in users.
- Logout link only visible to logged in users. Logout button in profile directs to logout page.

--------------------
**Navigation - links**

- Tested all navigation links to ensure they all work, including mobile navigation.
- Login/Register links only visible to users not logged in.
- Sign in link directs to log in page on register page. Sign up link directs to register page on login page.

**Payment**

- Error: order number in email different to order number in checkout, also 2 orders in admin
- - Fixed: checkout view post_code to postcode form data. (Indicates webhook working correctly as order was generated as it wasn't found to match in the database)

- Tried checking out again, received email confirmation with order number matching checkout success. Also only 1 order in admin.
- Webhooks checked throughout site build by disabling form submit action.

**Database updates**

- Continously checked, throughout site build and at the end that:
- - ratings for products were updated on adding a new review.
- - like count for blog post was updated on liking/unliking posts
- - comment count for blog posts was updated on adding/deleting comments
- - review count in product detail page updated on adding/deleting reviews
- - price of products updated after both individual discount and discount category functions
- - category on home page displays sale notification on category card if category is on sale
- - subscribers are removed from database on visiting unsubscribe URL
- - profile account info is updated on save info checkbox and profile update

**Other**

- Tested that only certain links are visible to certain users.
- Tested that links to products/reviews/comments etc that don't exist are redirected back home with an info message.
- Tested on various browsers.

----------
Testing using deployed version