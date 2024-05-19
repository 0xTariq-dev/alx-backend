# 0x00-pagination Project

## Description :bulb:
This project was created with learning purposes at Holberton School.
It's a simple API that works as a pagination system for large datasets of popular baby names.
The dataset is a CSV file that contains the following columns:
- `Year of Birth`
- `Gender`
- `Ethnicity`
- `Child's First Name`
- `Count`
- `Rank`

## Technologies & Tools :wrench:
- Python 3.7 or higher
- CSV module
- Typing module


## Files :card_file_box:
- `0-simple_helper_function.py`: Contains a function named `index_range` that takes two integer arguments `page` and `page_size` and returns a tuple of size two containing a start index and an end index corresponding to the range of indexes to return in a list for those particular pagination parameters.
- `1-simple_pagination.py`: Contains a function named `get_page` that takes two integer arguments `page` (default=1) and `page_size` (default=10) and returns a list of the correct page of the dataset.
- `2-hypermedia_pagination.py`: Contains a function named `get_hyper` that takes two integer arguments `page` (default=1) and `page_size` (default=10) and returns a dictionary containing the following key-value pairs:
  - `page_size`: the length of the returned dataset page
  - `page`: the current page number
  - `data`: the dataset page (equivalent to return from previous task)
  - `next_page`: number of the next page, `None` if no next page
  - `prev_page`: number of the previous page, `None` if no previous page
  - `total_pages`: the total number of pages in the dataset as an integer
