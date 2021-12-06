**User Stories**

**Responsiveness - mobile, tablet, laptop**

Site tested on multiple screen sizes.

Used [responsitor](https://www.responsinator.com/) to check multiple phones/tablets.

Site on different screen sizes can be seen [here](https://www.responsinator.com/?url=https%3A%2F%2Fdragon-egg-woodturning.herokuapp.com%2F)


**Navigation - links**

- Tested all navigation links to ensure they all work, including mobile navigation.
- Profile link only visible to logged in users.
- Logout link only visible to logged in users. Logout button in profile directs to logout page.
- Logo links directly back to home page.
- Home link throughout site in header section links back to home page.
- Blog page links direct to specific blog post page.
- Products page links direct to specific product detail page.
- About section link on home page as you scroll down links to about page.
- Category cards on home page links to products page with selected categories filtered, as expected.
- Login/Register links only visible to users not logged in.
- Sign in link directs to log in page on register page. Sign up link directs to register page on login page.

**Footer**

- Tested all footer links to ensure they all work.
- Social Media links all open in new tab.

**Searching/filtering/sorting - Products, Blogs**

- Searched known post in blog page, page refreshes with correct blogs from search.
- Searched various incorrect words, page refreshes with '0 blogs found' heading.
- Link back to all blogs directs to blog page.
- Searched known product in products page, page refreshes with correct products from search.
- Searched various incorrect products, page refreshes with '0 products found' heading.
- Category links all refresh and display correct products once clicked, including checkmark next to category name.
- Wood filtering button displays sidenav and on click, page refreshes an am shown correct products filtered with wood type.
- Checked all sort features, page refreshes and correctly orders the products with the chosen sort method.

**Crud - posts, comments, reviews, products**

-- Error: Tried liking blog post. Redirected to log in page - Fixed: removed login_required decorator.
-- Error: Tried to comment on post. Received ValueError - Fixed: edited blog_post view to ensure only authenticated users can post.

- Tried liking blog post. Given info message saying only logged in users can like a post. Redirected to blog post page.
- Tried commenting on a post. Was given info message saying only logged in users can post. Was redirected to blog post page.

- Product detail page displays warning above review section that I can't edit or delete my review if I post a review.
- Tried posting a review. Shown success message and redirected to product detail page. My review is displayed with anonymous review as the user.

**Login/Register/Logout**


**Contact Forms**

-- Contact form styled incorrectly: - was fixed.
-- Contact header styled incorrectly: - was fixed.

- Tried sending contact form with empty fields, was asked to fill in fields.
- Send form with correct fields. Received success message and redirected to home page.
- Received email from DragonEggWoodturning email as an auto reply.
- Default email address received email with message sent from contact form.

**Newsletter Forms**

**404 and 500**

-- Error header styled incorrectly: - was fixed.

- Incorrect URL directs to 404 page as expected.
- Go home and shop now links all direct to correct page.
- 500 page assumed to be correct.

**Code Validation - HTML, CSS, JavaScript, Python**

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


**Payment - adding, editing, removing**

- Added 10 items to bag. Shown success message. Icon displayed next to shopping bag nav icon.
- Tried adding another item of same type. Shown warning message that only 10 items max allowed.
- Tried editing bag items in shopping bag. Shown success message and redirected to shopping bag with updated items.
- Tried removing all items. Shown success message and redirected to shopping bag page with empty bag.
- Added item, am shown free delivery message.
- Tried checking out with empty fields, am shown message to fill in fields.
- Filled in forms apart from card, am shown card incomplete message.
- Filled in correct card details and am taken to checkout success page with order number.
- Recieved email confirmation with order number, order date, order total, shipping details and a contact link.
------ Error: order number in email different to order number in checkout, also 2 orders in admin - Fixed: checkout view post_code to postcode form data. (Indicates webhook working correctly as order was generated as it wasn't found to match in the database)
- Tried checking out again, received email confirmation with order number matching checkout success. Also only 1 order in admin.

**Profile - orders, reviews, account info**

**Admin - discount, newsletter, products, blogs**

**Subscribe and Unsubscribe**

- Tried subscribing with empty field. Was shown fill in field message.
- Subscribed with correct email. Was shown success message and directed back to home page.
- Received email from Dragon Egg Woodturning, with unsubscribe link.
- Tried subscribing with same email. Was shown error message saying email already subscribed.
- Clicked on unsubscribe link. Was shown success message that my email has been unsubscribed.

**Manual Site Testing - Anon user, registered user, admin**

Testing deployed version