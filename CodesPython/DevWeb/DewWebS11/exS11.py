import requests
url = "https://fakestoreapi.com/products"
response = requests.get(url)
data = response.json()
#Affichage de nom du produit specifique 
#print("Title of product 1:", data[0]["title"])

#recherche d'un produit par nom:
Title_to_find = input("Enter the product title to search: ")
for product in data:
    if Title_to_find in product["title"]:
        print("Found Product - Title:", product["title"])

# Affichage des titres et prix de chaque produit
for product in data:
    print(" Title:", product["title"], "/ price:", product["price"] )

#comparer les prix des produits:
min_price= min(product["price"] for product in data) #comparer les prix 
print ("Le Prix le plus bas est:", min_price) #afficher le moins cher

max_price= max(product["price"] for product in data) #comparer les prix
print ("Le Prix le plus élevé est:", max_price) #afficher le plus cher
