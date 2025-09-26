import json
from Task.helpers import validate_coma_list,validate_coma_list_st

def product_data_transformer():
    while True:
        product_names = validate_coma_list_st(prompt="Enter product names (comma-separated): ")
        product_prices = validate_coma_list(prompt="Enter product prices (comma-separated): ")
        if len(product_names) != len(product_prices):
            print("number of product names and prices must be equal.")
        else:
            break

    paired = zip(product_names, product_prices)

    filtered = filter(lambda x: x[1] > 0, paired)

    dict = list(map(lambda x: {
        "product": x[0],
        "price": x[1],
        "discounted": round(x[1] * 0.9, 2)
    }, filtered))

    filename = "products.json"
    with open(filename, "w") as f:
        json.dump(dict, f, indent=4)

    print(f"Data saved to '{filename}'")
    print("(Preview  5):")
    for item in dict[:5]:
        print(item)
