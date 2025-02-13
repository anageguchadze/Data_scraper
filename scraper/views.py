import requests
from bs4 import BeautifulSoup
import csv
from django.http import JsonResponse
from django.shortcuts import render

# Function to simulate scraping Planity data
def scrape_planity(request):
    # Sample HTML (pretend it's from Planity)
    sample_html = """
    <div class="manager">
        <h2 class="name">Jean Dupont</h2>
        <p class="email">jean@salonparis.fr</p>
        <p class="phone">0601020304</p>
        <p class="business">Salon Beauté Paris</p>
        <p class="region">75</p>
    </div>
    <div class="manager">
        <h2 class="name">Claire Morel</h2>
        <p class="email">claire@coiffure92.com</p>
        <p class="phone">0612345678</p>
        <p class="business">Coiffure Élite</p>
        <p class="region">92</p>
    </div>
    """
    
    soup = BeautifulSoup(sample_html, "html.parser")
    managers = soup.find_all("div", class_="manager")

    data = []
    for manager in managers:
        name = manager.find("h2", class_="name").text
        email = manager.find("p", class_="email").text
        phone = manager.find("p", class_="phone").text
        business = manager.find("p", class_="business").text
        region = manager.find("p", class_="region").text

        data.append({"name": name, "email": email, "phone": phone, "business": business, "region": region})

    # Save to CSV
    with open("scraped_managers.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "email", "phone", "business", "region"])
        writer.writeheader()
        writer.writerows(data)

    return JsonResponse(data, safe=False)
