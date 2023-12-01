import subprocess
import csv
import json

for i in range(52):  # Assuming you want to iterate over pages 0 and 52
    # Define the base curl command
    curl_command = [
        'curl',
        f'https://www.99bookscart.com/api/products/byGenre?genre=historical-fiction&pageNumber/{i}/' 
    ]

    try:
        # Run the curl command using subprocess
        response = subprocess.run(curl_command, capture_output=True, text=True, check=True)
        data = json.loads(response.stdout)  # Parse JSON data

        # Check if the response format is as expected
        if 'products' in data:
            products = data['products']

            results = []  # Define the 'results' list

            # Iterate through the list of products
            for product in products:
                name = product.get('name', '')
                language = product.get('langauge', '')  # Correct typo in 'language'
                author = product.get('author', '')
                publisher = product.get('publisher', '')
                price = product.get('price', '')
                #image = product.get('image', '')
                pages = product.get('pages', '')
                rating = product.get('rating', '')
                isbn = product.get('isbn', '')

                # Create a dictionary for each product and add it to the results list
                result = {
                    "name": name,
                    "language": language,
                    "author": author,
                    "publisher": publisher,
                    "price": price,
                    #"image": image,
                    "pages": pages,
                    "rating": rating,
                    "isbn": isbn

                }
                results.append(result)

            # Save the extracted data to a CSV file
            with open("/home/rajat/Desktop/web_scrap/historical_fiction.csv", "a", newline='', encoding="utf-8") as csvfile:
                fieldnames = ["name",  "language",  "author",  "publisher",  "price", "pages", "rating", "isbn" ]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                # Write header only if the file is empty
                if csvfile.tell() == 0:
                    writer.writeheader()

                # Write each product's data to the CSV file
                for product in results:
                    writer.writerow(product)

            print(f"Data for page {i} has been saved")
        else:
            print(f"Unexpected response format for page {i}:\n{json.dumps(data, indent=2)}")

    except subprocess.CalledProcessError as e:
        print(f"Error running curl command for page {i}: {e}")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON response for page {i}: {e}")








