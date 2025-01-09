# Commerce

Commerce is an eBay-like e-commerce auction platform built as part of **[CS50's Web Programming with Python and JavaScript](https://cs50.harvard.edu/web/2020/)** course. This web application allows users to post auction listings, place bids, comment on listings, and add them to a "watchlist." The project incorporates Django's powerful features for user authentication, database management, and handling dynamic content updates for auction interactions.

## About the Project

In this project, I built a simplified e-commerce auction platform with the following features:

- **User Authentication**: Users can sign up, log in, and log out.
- **Creating Listings**: Users can create auction listings with a title, description, starting bid, and optional image URL and category.
- **Bidding**: Users can place bids on listings, with the bid needing to exceed the current highest bid.
- **Watchlist**: Signed-in users can add listings to their watchlist and easily access them later.
- **Comments**: Users can comment on listings, and all comments are visible on the listing's page.
- **Auction Categories**: Listings can be categorized, and users can filter by category.
- **Admin Interface**: Administrators can manage listings, bids, and comments through the Django admin interface.

The project uses Django for backend functionality and Python for business logic, ensuring a smooth user experience while interacting with auction listings.

## Features

- **User Authentication**: Secure login, registration, and logout system.
- **Create Listings**: Users can post new auction listings with descriptions, images, and categories.
- **Bid on Listings**: Place bids on active auctions with a valid bid amount.
- **Watchlist**: Add or remove listings from your personal watchlist.
- **Commenting System**: Add comments on listings for discussions.
- **Category Pages**: Filter and view listings based on categories.
- **Admin Panel**: Site administrators can manage auctions, bids, and comments.

## Technologies Used

- **Python**
- **Django**
- **HTML/CSS**
- **SQLite** (for database storage)
- **JavaScript** (for dynamic content updates)

## Setup and Installation

To run this project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/lonyasha/cs50w-commerce.git
2. **Navigate into the project directory**:
   ```bash
   cd cs50w-commerce
3. **Create a virtual environment**:
      ```bash
      python3 -m venv venv
4. **Activate the virtual environment**:
   - For **Windows**:
     ```bash
     venv\Scripts\activate
   - For **MacOS/Linux**:
     ```bash
     source venv/bin/activate
5. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
6. **Run the migrations to set up the database**:
   ```bash
   python manage.py migrate
7. **Create a superuser to access the admin panel (optional)**:
   ```bash
   python manage.py createsuperuser
8. **Run the server**:
   ```bash
   python manage.py runserver

### Key Points:
- All installation and setup instructions are placed in properly formatted code blocks.
- This allows for easy copying and pasting directly into the terminal.

---

This project is a part of **[CS50's Web Programming with Python and JavaScript](https://cs50.harvard.edu/web/2020/)** course by Harvard University. The course provided a comprehensive introduction to web development, and this project was designed to showcase the skills learned throughout the course.

Thank you for visiting! 🎉
