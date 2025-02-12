# Little Lemon Restaurant Application

> This code shows the whole Little Lemon restaurant application, built with Django, as part of the Backend Development specialization from Meta on Coursera.

## Project Requirements

- Users should be able to register, login and logout
- It should be possible to add a booking and see the list of bookings
- It should be possible to add elements from the django admin panel

## Installation

1. Clone the repository
2. Create a virtual environment and activate it

```python
python3 -m venv env
source env/bin/activate
```

3. Install the dependencies with `pip install -r requirements.txt`
4. Run the server with `python manage.py runserver`

When working on MacOS, you might need to install the following dependencies:

```bash
brew install mysql-client pkg-config
```

then export the following environment variables:

```bash
export PKG_CONFIG_PATH="$(brew --prefix)/opt/mysql-client/lib/pkgconfig"
```

then install the requirements from the `requirements.txt` file.

## Application

The application contains not only the backend but also the frontend, built through templates present under the restaurant/templates directory.
