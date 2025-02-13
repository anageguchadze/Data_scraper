# Data_scraper

This Django-based web scraping application is designed to extract business manager information. The data includes business manager names, emails, phone numbers, business names, and regions, which are scraped and exported to a **CSV file**.

## Features:
- Scrape business manager data (name, email, phone, business, region).
- Save scraped data to a **CSV file**.
- View the extracted data in **JSON format** via a simple endpoint.
- Built using **Python**, **Django**, and **BeautifulSoup** for web scraping.

## Setup Instructions:
1. Clone the repository:
   git clone https://github.com/anageguchadze/Data_scraper.git
   cd Data_scraper

Install required dependencies:
pip install -r requirements.txt

Apply migrations (if applicable):
python manage.py migrate

Run the Django development server:
python manage.py runserver

Visit http://127.0.0.1:8000/scrape/ to trigger the scraping process.

How It Works:
The scraping process is simulated on a sample HTML structure.
The data is scraped and saved to scraped_managers.csv.
You can extend this scraper to interact with the real Planity website by modifying the scrape_planity view.

Technologies Used:
Python
Django
BeautifulSoup (for web scraping)
CSV

License:
This project is licensed under the MIT License - see the LICENSE file for details.

Contact:
If you have any questions or need further assistance, feel free to reach out!