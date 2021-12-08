# [**Dragon Egg Woodturning**](https://dragon-egg-woodturning.herokuapp.com)

_Use CTRL+click or CMD+click to open links throughout the README in a new tab_

***Disclaimer: This website is for educational purposes only***

![DragonEggWoodturning](/docs/img/amiresponsive-dragonegg.png)

## Overview

Prior to starting the Code Institute Software Development course, I had a little experience with basic understanding of web development. I used this basic knowledge to make a website with Shopify for my father to sell his woodturning products. Fast forward to now and my learning has come full circle as I now can create the store entirely on my own thanks to Code Institute. This is why I chose to do this for my final MS4 project.

[Link to live website here](https://dragon-egg-woodturning.herokuapp.com/)

<p style="font-size: 10px; font-style: italic;">*** If you would like to view the original shopify website, you can do so at https://dragoneggwoodturning.co.uk/ but be aware, depending on when you try to view this site, it may have been taken down as my father no longer wants it live ***</p>
---

## Description

Dragon Egg Woodturning is an e-commerce store selling hand made woodturning gifts ranging from walking sticks to unusual items built with a variety of different wood types.
- Anonymous users are able to navigate the site, buy products, review products and subscribe to the newsletter.
- Logged in users can also like blog posts, comment on blog posts and have a personal profile with their information, orders and reviews available.
- Admin/Site Owner can add/edit/delete new products, add/edit/delete new blogs, add discounts to products/categories and send out newsletters to subscribers.

---

## UX

### User Stories

As an anonymous user, I want to be able to:

- **navigate site**, so that I can
- - *find what I'm looking for easily*
- **search for products**, so that I can
- - *consider buying something*
- **filter products**, so that I can
- - *find exactly what I am looking for easily*
- **read about products**, so that I can
- - *understand the product more*
- **read about site**, so that I can
- - *understand about woodturning and how the products are made*
- **contact site**, so that I can
- - *enquire about any questions/issues I have*
- **register**, so that I can
- - *save my buying history and details for any other purchases*
- **buy products**, so that I can
- - *receive what I like from the store*
- **make secure payments**, so that I can
- - *make sure my payments are handled safely*
- **receive confirmation**, so that I can
- - *know that I have made the purchase*
- **review products**, so that I can
- - *give my feedback*
- **subscribe to newsletter**, so that I can
- - *stay updated with site's new products and additional information*
- **unsubscribe to newsletter**, so that I can
- - *stop receiving updates*

As a registered user, I want to be able to:

- **log in**, so that I can
- - *view previous buying history and save my details*
- **store my details/view profile**, so that I can
- - *prevent having to enter my details everytime*
- **update details**, so that I can
- - *save new details if any need to be changed*
- **view purchase history**, so that I can
- - *check previous buys to see if I want to buy another*
- **review products**, so that I can
- - *give feedback to the store*
- **comment on blog posts**, so that I can
- - *give feedback to the store*
- **edit/delete any comments, reviews I have made**, so that I can
- - *have full control over my involvement in the site*

As an admin user, I want to be able to:

- **add new products**, so that I can
- - *update current stock*
- **edit products**, so that I can
- - *make changes if necessary*
- **delete products**, so that I can
- - *remove old products if certain products are no longer available in the store *
- **create blog posts**, so that I can
- - *give readers an update on what is currently going on with the store and the woodturning work*
- **edit blog posts**, so that I can
- - *make changes if necessary*
- **delete blog posts**, so that I can
- - *remove any unwanted posts if necessary*
- **add discounts**, so that I can
- - *provide updates on pricing to users*
- **send newsletters**, so that I can
- - *update subscribers on anything relating to new products, new blogs, discounts etc*

### **Strategy**

#### External User's Goals

- To view various woodturning products that they can purchase.
- To comment on blog posts and like/unlike them.
- To review products.
- To subscribe to site's newsletter.
- To create an account and view/edit user information such as profile details, order history and reviews.

#### Site Owner's Goals

- To promote and sell hand made woodturning products.
- To create, edit and delete blog posts.
- To upload new products.
- To edit and delete current products.
- To discount certain products.
- To put categories on sale
- To send out newsletters.

### **Scope**

- Fits in with current programming ability which includes HTML, CSS, Javascript, Python and Django.
- Focus of the site is to provide an e-commerce platform that users can buy products from, read blog posts, review products, create an account and subscribe to site's newsletter.

### **Structure**

- Easy to navigate structure, with fixed header including shop link, profile link, shopping cart link.
- Consistent base structure throughout site of gallery, site information detailing making of walking sticks and about section with call to action.
- Consistent footer throughout site.
- Built mainly with CSS grid but use of flexbox too.

# Datebase Schema

![Database Schema](/docs/img/database_image.png)

# Apps/Models

- Bag app:
- - Contains `contexts.py` file to provide bag use throughout site.
---
- Blog app:
- - Post model
- - - stores information about the blog post, including likes, which is a manytomany field of registered users who have liked the post.
- - - like count updated in like post view.
- - Comment model
- - - stores information about each comment with foreign keys to Post and User
---
- Checkout app:
- - Order model
- - - Stores information about each order
- - - Generates unique order number
- - - Updates total based on OrderLineItems
- - OrderLineItem model
- - - Stores information for the order.
- - - Calculates price of each line item.
---
- Home app:
- - Returns index, about and contact pages.
- - Sends emails in contact view.
---
- Newsletter app:
- - Available across site with use of `contexts.py` file.
- - Subscribers model
- - - Stores information about each subscriber
- - - Generates unique unsubscribe link for each subscriber
- - - Sends welcome email via signal.
- - Newsletter model
- - - Stores information about each newsletter
- - - Sends newsletter to each subscriber with their own individual unsubscribe link via signal.
---
- Products app:
- - Category model
- - - Contains information about each category
- - - Has on sale and on sale amount features that are calculated in discounts view
- - WoodType model
- - - Contains information about each wood type. 
- - Product model
- - - Contains information about each product.
- - - Has discounted and discounted amount features that are updated with discounts view 
- - - Has a final price feature that is updated with product save. Price is altered if discounted.
- - - Has a rating feature that is updated with signals when review is added/saved/deleted.
- - - Checks if category is on sale so new added product has correct discount added, done via signal.
- - Image model
- - - Contains information about images.
- - - Has a foreign key to the Product.
- - Review model
- - - Contains information about the review
- - - Has a foreign key to the Product
- - - Rating choices are from 1-5
---
- Profiles app:
- - UserProfile model
- - - Contains information about the user
- - - Has a foreign key to User model


### **Skeleton**

# Wireframes

[Home Page inc. mobile](/docs/wireframes/homepage.png)

[About Page inc. mobile](/docs/wireframes/aboutpage.png)

[Contact Page inc. mobile](/docs/wireframes/contactpage.png)

[Blog Page inc. mobile](/docs/wireframes/blogpage.png)

[Products Page inc. mobile](/docs/wireframes/productspage.png)

[Products Category Page inc. mobile](/docs/wireframes/productcategorypage.png)

[Individual Product Page inc. mobile](/docs/wireframes/productindividualpage.png)

[Checkout Page inc. mobile](/docs/wireframes/checkoutpage.png)

[Shopping Cart Page inc. mobile](/docs/wireframes/shoppingcartpage.png)

[Profile Page inc. mobile](/docs/wireframes/profilepage.png)

[Admin Page inc. mobile](/docs/wireframes/adminpage.png)


### **Surface**

Colour scheme:

![Color Palette](/docs/img/colourpalete.png)

Images:

- Images are my own as all products are built by my father.

Typography:

- Poppins and Roboto font used.

Animations:

- Mousemove particle system on loading page.

- [GSAP](https://greensock.com/) animations throughout site for enjoyable UX experience. Primarily on landing page and as you scroll.

- Mouse move event listener on gallery section that moves the images across the screen and rotates them.

Design: 

 - Dark theme with CSS 3D imagery in some parts.
 - Bright orange contrasts really well with dark brown background.
 - Use of box shadows add visual pop to the site in places.
 - Color scheme was generated from [ColorSpace](https://mycolor.space/)

---

## Features

- Loading animation includes html canvas element with mouse move drawing of particles for nice UX experience as page loads. Techniques used I learned from a really good youtuber [here](https://www.youtube.com/c/Frankslaboratory)

**Landing page**
- Distinct image and highlighted section letting the user know exactly what the site is about
- Call to action buttons
- Scrolling down, category selection grid, detailing categories of products. If category is on sale, an icon is displayed with sale amount shown.
- Scrolling down, review section, which takes 10 reviews, and randomises the order in which they are displayed. Glider JS used to create the scrollable carousel.
- Scrolling down, 4 image display of wood with mouse move event listener to move images. Images move side to side smoothly, with rotation also.
- Scrolling down, information about the making of walking sticks
- Scrolling down, call to action to read more, which links to the about page.
- Scrolling down, newsletter section where people can sign up to the newsletter. If they subscribe, they are sent a welcome email with an unsubscribe link attached. Unsubscribe link is generated vua uuid for each subscriber.
- Base structure is used throughout site.

**About page**
- Grid layout detailing the use of wood in making of the products

**Contact page**
- Simple contact page with form.
- On completion an email is sent to the user to let them know we have received their message.
- The message is sent to the sites default email.

**Blog and blog post page**
- Grid layout of current blogs, detailing title, amount of comments, amount of likes, date posted and a snippet of the blog.
- On hover, each post links to individual blog post where the full post is displayed.
- Has a search feature to search blogs based on title and body of the blogs.
- Full blog page displays comments and a liked thumb along with the blog post itself.
- Logged in users can like and unlike a post. Which is displayed by filling out the thumb icon if they have liked it.
- Like count for blog post is updated with each like/unlike.
- Logged in users can comment on a post. They can edit and delete their comment also.

**Products page**
- Displays all products and a nav to select products from one of the categories.
- An icon is displayed as a checkmark next to the category name detailing which category you are currently looking at.
- Has a search feature to search products based on product name and description.
- Has a filter wood feature that lets users filter products by various wood types.
- Has a sort feature to sort products by price, rating, name, category.
- Each product has a rating, which is calculated in the backend when someone adds/deletes a review via signals.

**Product detail page**
- If the product has more than 1 image, a scroll feature is displayed, with a scroll progress feature.
- Images can be viewed full screen on click.
- Users have a quantity selector for up or down, from 1 to 10 items. If a user adds more than 10 items, a message is displayed to say no more than 10 items of each allowed.
- Adding an item displays a notification in the navbar shopping cart icon.
- Admin users have a feature to add a discount to an individual product, ranging from 5% to 50% off.
- If discounted, the original product price has a line through with the updated price shown next to it.
- Each product page has a review section, with users able to post reviews and their rating. Anonymous users are warned that they can not edit or delete reviews.
- Each review shows filled star icons equal to their rating.
- The rating in each review is used to calculate product rating in the backend.
- Page watermarks are generated with javascript based on category/woodtype filtering.

**Shopping cart page**
- Displays empty bag message if no items in shopping bag.
- If items in shopping bag, a notification on the shopping bag icon is displayed, detailing total items in shopping bag.
- Users can edit their bag in the shopping cart page. They can also remove items.
- Has a free delivery threshold that lets users know about free delivery if they spend a certain amount.

**Checkout page**
- Shows checkout form with option to save account information if buyer is a logged in user.
- Display order summary of whats in the shopping bag.

**Profile page**
- Has a profile navigation allowing users to view their information such as:
- Profile home - detailing the date the user signed up, their last login date and a log out button.
- Account info - which they can edit.
- Orders - which they can view seperately.
- Reviews - a list of reviews they have posted that they can edit and delete.

**Admin profile page**
- Has all the features of a regular user but also has access to:
- Newsletter section - where admin can send out a newsletter which is sent as an email through a loop to all subscribers. Subscribers are given individual unsubscribe link in each email.
- Discount section - where admin can add discounts to categories which puts all items from that category on sale. Product price is updated in products page and category section on home page displays a sale feature if category has a discount. Categories on discount are displayed with text notification in profile discount section.
- Products section - where admin can add, edit and delete products. Can edit product photos seperately to product information. Can add multiple photos at once. If a product is added to a category that is currently on sale, the price will be discounted via a signal.
- Blog section - where admin can add, edit and delete blogs.

**Custom 404 and 500 pages**
- Include links back to home and shop

## Technologies Used

### Languages

[HTML5](https://en.wikipedia.org/wiki/HTML5)

[CSS3](https://en.wikipedia.org/wiki/CSS) - code written with SCSS, then compiled into CSS using Sass compiler extension in Gitpod.

[JavaScript](https://en.wikipedia.org/wiki/JavaScript)

[Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries and Programs Used

[GitPod](https://www.gitpod.io/) - Online IDE

[Git](https://git-scm.com/) - Version Control

[Github](https://github.com/) - Where Git repositories are stored

[Balsamiq](https://balsamiq.com/) - for wireframes

[FontAwesome](https://fontawesome.com/) - for icons

[Materialize](https://materializecss.com/) - CSS framework for design and layout.

[Glider JS](https://nickpiscitelli.github.io/Glider.js/) - for review section carousel.

[GSAP](https://greensock.com/) - for animations.

[jQuery](https://jquery.com/) - JavaScript library.

[Google Fonts](https://fonts.google.com/) - for fonts

[Favicon Generator](https://favicon.io/favicon-generator/) - for favicon

[DB Docs](https://dbdocs.io/) - for database structure image

[Jinja](https://jinja.palletsprojects.com/en/3.0.x/) - template engine for Python

[Django](https://www.djangoproject.com/) - high-level Python web framework.

### Resources

[ColorSpace](https://mycolor.space/) - for color palette

[CSS Tricks](https://css-tricks.com/) - for general help

[Stack Overflow](https://stackoverflow.com/) - for support

[W3Schools](https://www.w3schools.com/) - for general help

[YouTube](https://youtube.com) - for general help 

[Responsinator](http://www.responsinator.com/) - helping to test responsiveness

[TinyPNG](https://tinypng.com/) - for image compression

[CompressJPEG](https://compressjpeg.com/) - for image compression

[Am I Responsive](http://ami.responsivedesign.is/) - for responsive help and README image

[Autoprefixer](https://autoprefixer.github.io/) - adds vendor prefixes to CSS

[Heroku](https://www.heroku.com/) - cloud platform service for deployment

[Heroku Postgres](https://www.heroku.com/postgres) - database used in production

[SQLite3](https://www.sqlite.org/index.html) - database used in development

[AWS](https://aws.amazon.com/s3/) - cloud storage for media and static files

Code Institute Course

Code Institute Slack Community

Chrome Dev Tools

---

## Testing

- Can be found [here](/docs/TESTING.md)

### Project Barriers and Solutions

- Auto focus on checkout form broke the sites loading animation. After trying to debug why this was happening for a good hour I tested removing the auto focus feature and the animations worked. Whilst having auto focus on the checkout form would be useful, I felt it was more important to keep the fluid loading animations throughout the site, instead of trying to have it disabled for just one page and keep the auto focus. There is probably a better fix to include both but due to time constraints I chose to simply remove the auto focus.

- The sidenav popout for the wood filter broke when adding in GSAP animations. I fixed this by taking it out of the 'main' dom element and putting it above.

- Had issues with reviews user input. Easy fix by adding null=true and blank=true to review model. Of course this means anonymous users can not edit or delete their reviews but I decided to let this be a feature as anonymous users can buy products, so they should be able to review also. A warning is shown above the review form on each product detail page to inform users of this.

- The add to bag feature allows inputs from 1 - 10. But you could add multiple 'add to bag' inputs and go above 10. I fixed this by calculating item total and informing users via messages if they tried to add more items that only 10 items per product could be purchased.

- Initially styled the site with a light theme, but as I built the site further and further I switched to a darker theme as I felt this looks cleaner and gave a better UX experience.

- Adding a new product set the original price. But with the category on sale feature, it meant that if a new product was added to a category, it wouldnt match the category discount. I fixed this by adding in a signal to check if product category was on sale and then calculating the correct price from that.

### Features To Improve

**I intended on implementing most of the features below but due to time constraints I wasn't able to**

- Add more blog photos to a blog post
- Add/edit/remove category, woodtype functionality
- Add favourites functionality
- Add 3-5 current discounted products, and top 3 blogs to landing page as you scroll down, similar to review section.
- Add feature to display most liked, most commented on blogs.
- Profile notifications when theres a comment/like on a post or review on a product
- Deleting profile
- Share on social media
- Log in with social media
- Adding a points system where repeat buyers can accumulate points and use those points for discounts.
- Add pagination to products page.
- Add a view comments and view reviews feature for when comments and reviews sections get too long.
- Have a product total amount so a product can be listed as 'currently sold out'.
- Have the site able to have users sell their own products on the store.
- - This wasn't in the original plan but I think would be something interesting to do in the future.


---

### Known issues

- Site is a bit slow, but loading animation helps ease the UX experience.
- Didn't have time to implement a scroll to the top button on the products page. So there is a bit of scrolling in the all products view.
- Same goes for the comment and review section.

---

## Deployment

### Local Install

- Repository initially set up on Github with Code Institute template.

- Use of Gitpod for code editor.

- Deployed using the master branch.

**Clone**

- Locate the GitHub Repository.

- Click the "Code" button.

- Highlight the "HTTPS" button to clone with HTTPS and copy the link.

- Open Git Bash

- Identify location in IDE where you want the cloned directory to be made.

- Type git clone, and then paste the URL, which is the link that's been copied.

- Your local clone will be made.

**Create Environment Variables**

- Create `env.py` file, add `import os` to the top of file and add these environment variables.

| Env variables |
| ------------- |
| `os.environ['DEVELOPMENT']` = `True` |
| `os.environ['SECRET_KEY']` = `'<your value>'` |
| `os.environ['STRIPE_PUBLIC_KEY']` = `'<your value>'` |
| `os.environ['STRIPE_SECRET_KEY']` = `'<your value>'  ` |
| `os.environ['STRIPE_WH_SECRET']` = `'<your value>'` |
| `os.environ['AWS_ACCESS_KEY_ID']` = `'<your value>'` |
| `os.environ['AWS_S3_REGION_NAME']` = `'<your value>'` |
| `os.environ['AWS_SECRET_ACCESS_KEY']` = `'<your value>'` |
| `os.environ['AWS_STORAGE_BUCKET_NAME']` = `'<your value>'` |
| `os.environ['EMAIL_HOST_PASS']` = `'<your value>'` |
| `os.environ['EMAIL_HOST_USER']` = `'<your value>'` |
| `os.environ['DEFAULT_FROM_EMAIL']` = `'<your value>'` |
| `os.environ['UNSUBSCRIBE_URL']` = `'<your value>'` |
| `os.environ['HEROKU_HOSTNAME']` = `'<your value>'` |

- Create `.gitignore` file.

| Include in `.gitignore` |
| ------------- |
| `env.py` |
| `__pycache__/` |
| `*.sqlite3` |
| `core.Microsoft*` |
| `core.mongo*` |
| `core.python*` |
| `*.py[cod]` |
| `node_modules/` |
| `.github/` |
| `*.pyc` |

**Install project dependencies**

- Install project requirements by typing `pip install -r requirements.txt`

**Create Superuser**

- Type `python manage.py createsuperuser` and following instructions in the terminal.

**Migrate**

- Apply model migrations with `python3 manage.py makemigrations` followed by `python3 manage.py migrate`.

**Load product data**

- Type `python3 manage.py loaddata db.json`

**Deploy Locally**

- Run `python3 manage.py runserver` and open localhost URL.

### Heroku

- Register Heroku account, or log in if you already have one.

- Create new app.

- Finish setup, including name and region.

- Under resources, choose heroku postgres database with free hobby dev account

- Postgres requires dj_database_url and psycopg2, which is installed with `requirements.txt` file.

- Under settings, reveal config vars. Configure config variables from `env.py` file excluding development variable.
- - Add in `USE AWS = True`
- - Add in `DATABASE_URL = <your value>`

- Deploy tab and select github option

- Connect to your github

- Manually deploy

- Once complete, enable automatic deploys

- Open app to see deployed version.

## AWS

- Instructions for hosting media and static files with AWS S3 Bucket can be found [here](https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html)

---

## Credits

### Code Snippets

- Used Code Institute walkthrough project Boutique Ado for general help.
- Used help to get for attribute after Django removed it after adding fieldsets in [here](https://www.skillsugar.com/how-to-get-form-input-id-label-name-in-django-template)
- Canvas particle system on loading page --- Learned Canvas drawing from [youtuber here](https://www.youtube.com/c/Frankslaboratory)


### Images and videos

- All images used are my own as the site was based on a site I built with shopify for my father several years back.

### Written Content

- All written content is used from original site, with slight adjustments.

### Acknowledgments

- Code Institute Software Development Course - for the education.
- Code Institute Slack Community group - for the support.
- My mentor [Antonio Rodriguez](https://github.com/AkaAnto) - for the guidance and support throughout.