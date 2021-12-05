# [**DragonEggWoodturning**](https://dragon-egg-woodturning.herokuapp.com)

_Use CTRL+click or CMD+click to open links throughout the README in a new tab_

***Disclaimer: This website is for educational purposes only***

![]()

## Overview

Prior to starting the Code Institute Software Development course, I had a little experience with basic understanding of web development. I used this basic knowledge to make a website with Shopify for my father to sell his woodturning products. Fast forward to now and my learning has come full circle as I now can create the store entirely on my own thanks to Code Institute.

Link to website: [Here](https://dragon-egg-woodturning.herokuapp.com/)

---

## Description

Dragon Egg Woodturning is an e-commerce store selling hand made woodturning gifts ranging from walking sticks to unusual items built with a variety of different wood types.

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
- **store my details**, so that I can
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

![Database Schema]()


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

---

## Features

- Loading animation includes html canvas element with mouse move drawing of particles for nice UX experience as page loads. Techniques used I learned from a really good youtuber [here](https://www.youtube.com/c/Frankslaboratory)

**Landing page**
- Distinct image and highlighted section letting the user now exactly what the site is about
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
- Logged in users can comment on a post. They can edit and delete their comment also.

**Products page**
- Displays all products and a nav to select products from one of the categories.
- An icon is displayed as a checkmark next to the category name detailing which category you are currently looking at.
- Has a search feature to search products based on product name and description.
- Has a filter wood feature that lets users filter products by various wood types.
- Has a sort feature to sort products by price, rating, name, category.
- Each product has a rating, which is calculated in the backend when someone adds/deletes a review via signals.

**Product detail page**
- If the product has more than 1 image, a scroll feature is displayed.
- Users have a quantity selector for up or down, from 1 to 10 items. If a user adds more than 10 items, a message is displayed to say no more than 10 items of each allowed.
- Adding an item displays a notification in the navbar shopping cart icon.
- Admin users have a feature to add a discount to an individual product, ranging from 5% to 50% off.
- If discounted, the original product price has a line through with the updated price shown next to it.
- Each product page has a review section, with users able to post reviews and their rating. Anonymous users are warned that they can not edit or delete reviews.
- The rating in each review is used to calculate product rating in the backend.

**Shopping cart page**
- Displays empty bag message if no items in shopping bag.
- If items in shopping bag, a notification on the shopping bag icon is displayed, detailing total items in shopping bag.
- Users can edit their bag in the shopping cart page. They can also remove items.

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

[Google Fonts](https://fonts.google.com/) - for fonts

[Favicon Generator](https://favicon.io/favicon-generator/) - for favicon

[DB Docs](https://dbdocs.io/) - for database structure image

[Jinja](https://jinja.palletsprojects.com/en/3.0.x/) - template engine for Python

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

Code Institute Course

Code Institute Slack Community

Chrome Dev Tools

---

## Testing

### Project Barriers and Solutions

- Auto focus on checkout form broke the sites loading animation. After trying to debug why this was happening for a good hour I tested removing the auto focus feature and the animations worked. Whilst having auto focus on the checkout form would be useful, I felt it was more important to keep the fluid loading animations throughout the site, instead of trying to have it disabled for just one page and keep the auto focus. There is probably a better fix to include both but due to time constraints I chose to simply remove the auto focus.

- The sidenav popout for the wood filter broke when adding in GSAP animations. I fixed this by taking it out of the 'main' dom element and putting it above.

- Had issues with reviews user input. Easy fix by adding null=true and blank=true to review model. Of course this means anonymous users can not edit or delete their reviews but I decided to let this be a feature as anonymous users can buy products, so they should be able to review also. A warning is shown above the review form on each product detail page to inform users of this.

- The add to bag feature allows inputs from 1 - 10. But you could add multiple 'add to bag' inputs and go above 10. I fixed this by calculating item total and informing users via messages if they tried to add more items that only 10 items per product could be purchased.

- Initially styled the site with a light theme, but as I built the site further and further I switched to a darker theme as I felt this looks cleaner and gave a better UX experience.

- Adding a new product set the original price. But with the category on sale feature, it meant that if a new product was added to a category, it wouldnt match the category discount. I fixed this by adding in a signal to check if product category was on sale and then calculating the correct price from that.

### Feature To Improve

---

### Known issues
---

## Deployment

---

## Credits

### Code Snippets

### Images and videos

- All images used are my own as the site was based on a site I built with shopify for my father several years back.

### Written Content

- All written content is used from original site, with slight adjustments.

### Acknowledgments

- Code Institute Software Development Course - for the education.
- Code Institute Slack Community group - for the support.
- My mentor [Antonio Rodriguez](https://github.com/AkaAnto) - for the guidance and support throughout.