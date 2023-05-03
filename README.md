#  Library

Library CRUD Project
<br>
Live version: -- WIP --
<br>

## 🚀 Run Locally

Clone the project

```bash
  git clone https://github.com/Rantoryu/Library.git
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Run connection with MySQL Server on 3306 port and Apache on 80, 443 using Xampp for example

<a href="https://www.apachefriends.org/pl/index.html" target="_blank"><img align="left" alt="Xampp APP" style="padding-right:10px;" src="https://i.imgur.com/JGZXkY0.png"/></a>

<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

Log in to MySQL as the root user:

```bash
mysql -u root -p

```

Create a new user account:

```bash
CREATE USER 'user'@'localhost' IDENTIFIED BY '';

```

Grant privileges to the new user account:

```bash
GRANT ALL PRIVILEGES ON *.* TO 'user'@'localhost';

```

Start python script

```bash
  python .\library.py

```

## 📝 Tech Stack

Python, MySQL


## 👨‍🚀 Show your support

Give a ⭐️ if this project helped you!
