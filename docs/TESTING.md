**User Stories**

**Responsiveness - mobile, tablet, laptop**

**Navigation - links**

**Footer**

**Searching - Products, Blogs**

**Crud - posts, comments, reviews, products**

**Login/Register/Logout**

**Contact Forms**

**Newsletter Forms**

**404 and 500**

**Code Validation - HTML, CSS, JavaScript, Python**

HTML Validity

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

**Payment - adding, editing, removing**

**Profile - orders, reviews, account info**

**Admin - discount, newsletter, products, blogs**

**Subscribe and Unsubscribe**

**Manual Site Testing - Anon user, registered user, admin**

Testing deployed version