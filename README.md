# Higher Diploma in Science in Data Analytics
*****

## Web Services and Applications Module

![Programming](Images/img_programming.jpeg)
************

## My Assessment Repository

This repository was created as part of the Web Services and Applications assessment module for the course in the [Higher Diploma in Science in Data Analytics](https://www.atu.ie/courses/higher-diploma-in-science-data-analytics?_gl=1%2A1bcdos0%2A_ga%2AMTE3OTU2MzQ5LjE2OTY2MDYwMzE.%2A_ga_5R02GBYV8V%2AMTcxNDMzOTE2Ni4xMS4xLjE3MTQzMzkyMDAuMC4wLjA.) at [ATU](https://www.atu.ie/). This README has been written with [Github's Documentation On READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) in mind. You can find more about [writing in Mark Down in GitHub's documentation](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).
*****

## Getting Started

This repository contains my [Big Project](https://github.com/RodrigoDMU/WSAA_big_project) submission for the module, showcasing the skills I have developed throughout the course in Web Services and Applications.
******

### Big Project - Event Music List

A RESTful API built with Flask for managing a music library. It allows you to **create**, **read**, **update**, and **delete** music entries from a MySQL database.

![EventMusicListTable](Images/Event_Music_List_Table.png)
******

### 🌍 Live App

View the public viewer page:  
👉 [https://rodrigodmu.pythonanywhere.com/musicviewer.html](https://rodrigodmu.pythonanywhere.com/musicviewer.html)
*****

#### 🌐 Project Structure

- [`musicviewer.html`](https://github.com/RodrigoDMU/WSAA_big_project/blob/main/musicviewer.html): Event playlist public preview page.

- [`server.py`](https://github.com/RodrigoDMU/WSAA_big_project/blob/main/server.py): Main Flask app.

- [`musicDAO.py`](https://github.com/RodrigoDMU/WSAA_big_project/blob/main/musicDAO.py): Data access logic (CRUD operations).

- [`dbconfig.py`](https://github.com/RodrigoDMU/WSAA_big_project/blob/main/dbconfig_template.py): MySQL connection configuration.

- [`requirements.txt`](https://github.com/RodrigoDMU/WSAA_big_project/blob/main/requirements.txt): Python package dependencies.
*****

#### ⚙️ Setup Instructions

##### 1. Clone the repository in Pythonanywhere
```bash
git clone https://github.com/RodrigoDMU/WSAA_big_project
cd WSAA_big_project
```

##### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
```

##### 3. Install dependencies
```bash
pip install -r requirements.txt
```

##### 4. Set up the MySQL database
Create a MySQL database and run the following SQL:
```bash
CREATE TABLE music (
    id INT AUTO_INCREMENT PRIMARY KEY,
    artist VARCHAR(255) NOT NULL,
    title VARCHAR(255) NOT NULL,
    minutes INT CHECK (minutes >= 0),
    year INT CHECK (year >= 0),
    category ENUM(
        'Blues',
        'Classical',
        'Contemporary R&B',
        'Country',
        'Disco',
        'Electronic',
        'Gospel',
        'Hip Pop',
        'Jazz',
        'Pop',
        'Reggae',
        'Rock',
        'Soul Music',
        'Others'
    ) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

##### 5. Configure database connection
The `dbconfig.py` file is included in .gitignore to protect personal informations.

```bash
mysql = {
    'host': "host",
    'user': "username",
    'password': "password",
    'database': "database"
}
```

##### 6. Run the application
The public viewer page can be accessed at: https://rodrigodmu.pythonanywhere.com/musicviewer.html
*****

## Author

**Rodrigo De Martino Ucedo:**
 I am currently studying Higher Diploma in Science in Data Analysis at Atlantic Technological University. For more information or questions, please contact me on GitHub or add me on [LinkedIn](https://www.linkedin.com/in/rdmdemartino/).

*******
## End
last commit on 24/05/2025.