# Python Flask Project - Dark Souls Bosses API

## `Database Info`

- Database name: dark_souls_bosses
- Table name: Boss
- Created with Python, Flask, PostgreSQL, and Peewee Models
- Runs on localhost port 9000

---

## `Navigating Database`

- Clone repo to your machine
- Start virtual environment in terminal
- Run `app.py` using `python3`
- Connect to `dark_souls_bosses` database via `psql` (probably need to create the database first)
- Add localhost server address to your browser, see below for CRUD implementation

---

## `CRUD Endpoints for Postman`

- `GET`:  
  /bosses/ -- returns data for all bosses  
  /bosses/id -- returns individual boss data

- `PUT`:  
  /bosses/id -- updates data provided for individual boss

- `POST`:  
  /bosses -- creates a new boss with data provided

- `DELETE`:  
  /bosses/id -- removes individual boss from database

---

Created by Mitch Raznick, GA-NYC SEI August 2022
