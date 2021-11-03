
### Prerequisites
 - Python 3
 - `pip`

### Installation
```bash
$ pip install -r requirements.txt
```


### Description

I performed web scraping to get the necessary data for creating the csv file. Initially my dataset had only five columns namely name, dob, email, and address. I used the random package of python to create the ethnicity and education columns. <br />
I decided to go with sqlalchemy library to complete this project. First, I created a sqlite db to store my tables. Then, I initiated a session to communicate with my db. Next, I  created models for my tables: raw and clean. My next task was to populate the raw table using the csv file. I used the data_transformer.py script to eliminate people from my raw table and use to resulting dataset to populate my clean table. Then, I used run_example() to further filter the clean table by either ethnicity or education. By using format.py, I provided a way to display the all of the infomation about a person.

