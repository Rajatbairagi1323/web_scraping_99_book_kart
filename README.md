# Fiction Book Scraping from 99bookscart

This Python script allows you to scrape data about historical fiction books from the website www.99bookscart.com using the curl command. The extracted information is then parsed and saved into a CSV file for further analysis or use.

## Prerequisites

Make sure you have the following installed on your system:

- Python 3
- curl (for extracting data from web)

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/Rajatbairagi1323/web_scraping_99bookscart.git
    ```

2. Navigate to the project directory:

    ```bash
    web_scrapping_99bookscart
    ```

3. Run the script:

    ```bash
    python3 today_books.py
    ```

   The script will iterate over multiple pages and save the extracted data to a CSV file (`historical_fiction.csv`).

## Features

- **Data Extraction:** Scrapes data about historical fiction books from www.99bookscart.com.

- **Pagination Support:** Iterates over multiple pages to gather a comprehensive dataset.

- **Error Handling:** Catches errors during the scraping process, such as unexpected response formats or JSON decoding errors.

- **CSV Output:** Saves the extracted data into a CSV file (`historical_fiction.csv`) with relevant fields like book name, language, author, publisher, price, pages, rating, and ISBN.

## CSV Fields

- **name:** The name of the historical fiction book.
- **language:** The language in which the book is written.
- **author:** The author of the book.
- **publisher:** The publisher of the book.
- **price:** The price of the book.
- **pages:** The number of pages in the book.
- **rating:** The rating of the book.
- **isbn:** The ISBN (International Standard Book Number) of the book.


## Acknowledgments

- Thanks to www.99bookscart.com for providing the data.

Feel free to contribute or use this script for your own data collection purposes!
