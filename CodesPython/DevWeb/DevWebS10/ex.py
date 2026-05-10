from bs4 import BeautifulSoup
import requests

url = "https://books.toscrape.com/"
response = requests.get(url)

print("status_code:", response.status_code)
if response.status_code != 200:
    print("Failed to access the website")
    exit()

soup = BeautifulSoup(response.text, 'html.parser')
books = soup.find_all('article', class_='product_pod')

# -------- PRIX --------
Max_book_price = 0
Most_expensive_book = ""
Min_book_price = 0
Least_expensive_book = ""

# -------- ÉTOILES --------
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

best_rating = 0
best_book = ""

for book in books:
    book_title = book.h3.a['title']

    # PRIX
    book_price_text = book.find('p', class_='price_color').text
    book_price = float(book_price_text.replace('£', '').replace('Â', ''))

    # ÉTOILES
    rating_class = book.find('p', class_='star-rating')['class']
    rating_word = rating_class[1]
    rating = rating_map[rating_word]

    print(f"Title: {book_title}, Price: £{book_price}, Rating: {rating}⭐")

    # livre le plus cher
    if book_price > Max_book_price:
        Max_book_price = book_price
        Most_expensive_book = book_title

    # livre le moins cher
    if book_price < Min_book_price or Min_book_price == 0:
        Min_book_price = book_price
        Least_expensive_book = book_title

    # meilleur livre par étoiles
    if rating > best_rating:
        best_rating = rating
        best_book = book_title

# -------- AFFICHAGE FINAL --------
print("\n📘 LIVRE LE PLUS CHER")
print(f"{Most_expensive_book} — £{Max_book_price}")

print("\n📗 LIVRE LE MOINS CHER")
print(f"{Least_expensive_book} — £{Min_book_price}")

print("\n🌟 MEILLEUR LIVRE SELON LES ÉTOILES")
print(f"{best_book} — {best_rating} ⭐")