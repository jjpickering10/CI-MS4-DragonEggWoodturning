# [**DragonEggWoodturning**]()

_Use CTRL+click or CMD+click to open links throughout the README in a new tab_

***Disclaimer: This website is for educational purposes only***

![]()

## Overview

Prior to starting the Code Institute Software Development course, I had a little experience with basic understanding of web development. I used this basic knowledge to make a website with Shopify for my father to sell his woodturning products. Fast forward to now and my learning has come full circle as I now can create the store entirely on my own thanks to Code Institute.


Link to website: []()

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

### **Strategy**

#### External User's Goals

- To view various woodturning products that they can purchase and review.

#### Site Owner's Goals

- To promote and sell hand made woodturning products.
- To create, edit and delete blog posts.
- To upload new products
- To edit and delete current products.

### **Scope**

- Fits in with current programming ability which includes HTML, CSS, Javascript, Python and Django.
- Focus of the site is to provide and e-commerce platform that users can buy products from.
- Users can review products and read blog posts.


### **Structure**

- Easy to navigate structure, with various categories of products and woodtypes.
- Consistent footer throughout site.


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

[GSAP](https://greensock.com/) animations throughout site for enjoyable UX experience. Primarily on landing page and as you scroll.

Design: 


---

## Features

- Landing page
- - Distinct image and highlighted section letting the user now exactly what the site is about
- - Call to action buttons
- - Scrolling down, category selection grid
- - Scrolling down, review section
- - Scrolling down, 4 image display of wood with mouse move event listener to move images
- - Scrolling down, information about the making of walking sticks
- - Scrolling down, call to action to read more.
- - Scrolling down, newsletter section where people can sign up to the newsletter. If they subscribe, they are sent a welcome email with an unsubscribe link attached.

- About page
- - Grid layout detailing the use of wood in making of the products
- - Continued use of base structure as you scroll down.

- Contact page
- - ****

- Blog page
- - Grid layout of current blogs, detailing title, amount of comments, amount of likes, date posted and a snippet of the blog.
- - Links to individual blog post where the full post is displayed.
- - Full blog page displays comments and a liked thumb.
- - Has a search feature to search blogs.
- - Logged in users can like and unlike a post. Which is displayed filling out the thumb icon if they have liked it.
- - Logged in users can comment on a post. They can edit and delete their post also.

- Products page
- - Displays all products and a nav to select products from one of the categories.
- - Has a search feature to search products.
- - Has a filter wood feature that lets users filter products by various wood types.
- - Has a sort feature to sort products by price, rating, name, category.
- - Each product has a rating, which is calculated in the backend when someone adds a review.

- Product detail page
- - If the product has more than 1 image, a scroll feature is displayed.
- - Users have a quantity selector to up or down, from 1 to 10 items. If a user adds more than 10 items, a message is displayed to say no more than 10 items of each allowed.
- - Admin users have a feature to add a discount to an individual product, ranging from 5% to 50% off.
- - Each product page has a review section, with users able to post reviews. Anonymous users are warned that they can not edit or delete reviews.
- - The rating in each review is used to calculate product rating in the backend.

- Shopping cart page
- - Displays empty bag message if no items in shopping bag.
- - If items in shopping bag, a notification in the nav is displayed.
- - Users can edit their bag in the shopping cart page. They can also remove items.

- Checkout page
- - Shows checkout form with option to save account information if buyer is a logged in user.
- - Display order summary of whats in the shopping bag.

- Profile page
- - Has a profile navigation allowing users to view their information such as:
- - Account info - which they can edit.
- - Orders - which they can view seperately.
- - Reviews - a list of reviews they have posted that they can edit and delete.

- Admin profile page
- - Has all the features of a regular user but also has access to:
- - Newsletter section - where admin can send out a newsletter which is sent as an email through a loop to all subscribers.
- - Discount section - where admin can add discounts to categories which puts all items from that category on sale. Product price is updated in products page and category section on home page displays a sale feature if category has a discount.
- - Products section - where admin can add, edit and delete products. Can edit product photos seperately to product information. Can add multiple photos at once.
- - Blog section - where admin can add a edit and delete blogs.

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

[GSAP](GSAP](https://greensock.com/)) - for animations.

[Google Fonts](https://fonts.google.com/) - for fonts

[Favicon Generator](https://favicon.io/favicon-generator/) - for favicon

[DB Docs](https://dbdocs.io/) - for database structure image

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

[EmailJS](https://www.emailjs.com/) - for email functionality

[Heroku](https://www.heroku.com/) - cloud platform service for deployment

Code Institute Course

Code Institute Slack Community

Chrome Dev Tools

---

## Testing

### Project Barriers and Solutions

### Feature To Improve

---

### Known issues
---

## Deployment

---

## Credits

### Code Snippets

### Images and videos

### Written Content

### Acknowledgments

- Code Institute Software Development Course - for the education.
- Code Institute Slack Community group - for the support.
- My mentor [Antonio Rodriguez](https://github.com/AkaAnto) - for the guidance and support throughout.