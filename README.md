# Blog App

This is a blogging web app developed in Python, Flask, SQLite, and MongoDB.

Main features of the app:
- Secure authentication through password hashing. 
- CSRF protected.
- Role based access controlled.

Main entities of the app:
- Admins can create, edit, view, and delete blog posts and can manage users' roles.
- Authors can view, create, and edit their own blog posts.
- Readers can interact with created blog posts through viewing them and liking or disliking them.

## Installation

```shell
$ git clone https://github.com/TheRealQi/Flask-BlogApp.git
$ cd Flask-BlogApp
$ pip install -r requirements.txt
```

## Switching Databases

To switch databases from SQLite to MongoDB or vice-versa, open the .env file and simply change DATABASE variable.
```
DATABASE = 'SQL' // For SQLite
DATABASE = 'MONGODB' // For MongoDB
```
