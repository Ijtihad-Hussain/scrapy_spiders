These scripts are written in Scrapy. If Scrapy is not installed in your system, install it by running this command:
pip install Scrapy

To run the scripts Open terminal inside the project folder (i.e scripySpiders) and run these commands.
python -m venv scrapy-env
scrapy-env\Scripts\activate.bat
scrapy crawl applion -o filename.csv (for applion.com)
scrapy crawl bestbuylaptop -o filename.csv (for bestbuy.com)
scrapy crawl dell -o filename.csv (for dell.com)
scrapy crawl newegg -o filename.csv (for newegg.com)
scrapy crawl walmart -o filename.csv (for walmart.com)