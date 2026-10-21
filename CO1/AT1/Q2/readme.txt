
import re

products = [
    "Apple iPhone",
    "Apple Watch",
    "Samsung Galaxy",
    "Samsung TV",
    "HP Laptop",
    "Dell Laptop",
    "Wireless Mouse",
    "Wireless Keyboard"
]

def search_products(keyword, search_type):
    if search_type == "exact":
        pattern = r"\b" + re.escape(keyword) + r"\b"
    elif search_type == "prefix":
        pattern = r"\b" + re.escape(keyword)
    elif search_type == "suffix":
        pattern = re.escape(keyword) + r"\b"
    elif search_type == "partial":
        pattern = re.escape(keyword)
    else:
        print("Invalid search type")
        return

    matches = [
        product for product in products
        if re.search(pattern, product, re.I)
    ]

    print("\nMatching Products:")
    if matches:
        for product in matches:
            print(product)
    else:
        print("No products found")

    print("Total Matching Products:", len(matches))


# User input
keyword = input("Enter search keyword: ")
search_type = input(
    "Enter search type (exact/prefix/suffix/partial): "
).lower()

search_products(keyword, search_type)

