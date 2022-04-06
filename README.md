# New York City Guide by Borough
Project 2 Build NYC Guide in Django/Python

![NYC](https://s-media-cache-ak0.pinimg.com/originals/eb/8f/82/eb8f82555f88f8364929e5e829702caf.jpg)

This Django app is a pair-progrmming project that serves as a guide for users looking for activities and events in New York City, categorized by the city's boroughs.

---

## Contributors ##

- [Asha Maurya](https://github.com/jtc21am)  
- [Ulysses Ware](https://github.com/ThomasWare)

---

## Setting up the Virtual Environment ##

After cloning this repo into a directory, you need to create a new virtual environment. Run the following command:

```bash
  python -m venv venv  # you may have to use python3 instead of python
```

Now you need to activate the virtual environment. Do this with one of the following commands depending on the type of operating system you are using:

> MacOS, Linux, ChromeOS:  
> `source venv/bin/activate`  
> Windows:  
> `venv\Scripts\activate.bat`

---

## Install Project Dependencies ##

To install the project dependencies, run the following commands in the project's root directory:

```bash
  pip install django
  pip freeze install > requirements.txt
```

---

## Running the Application ##

Now you can run the application! First navigate to the `nyc-guide` directory and run the following commmand:

```bash
  python manage.py runserver # you may have to replace python with python3
```

Now you should be able to point your browser to [http://localhost:8000](http://localhost:8000) and use the app.

---

## Stopping the Application ##

After you are done navigating the app. You can shut the server down by typing `Ctrl+C` in the terminal. You can then exit the virtual environment by using the following command:

```bash
  deactivate
```

---

## Structure ##

The structure of the web pages corresponds to the following (along with their URL paths):

- **Home** `/`

  - **Brooklyn** `/brooklyn`
    - **Beaches** `/brooklyn/beaches`
      - **Brighton Beach** `/brooklyn/beaches/brighton%20beach`
      - **Coney Island** `/brooklyn/beaches/coney%20island`
      - **Manhattan Beach** `/brooklyn/beaches/manhattan%20beach`
  - **Bronx** `/bronx`
    - **Beaches** `/bronx/beaches`
      - **Orchard Beach** `/bronx/beaches/orchard%20beach`
    - **Zoos** `/bronx/zoos`
      - **Bronx Zoo** `/bronx/zoos/bronx%20zoo`
  - **Manhattan** `/manhattan`

    - **Food** `/manhattan/food`

      - **Cheeky Sandwiches** `/manhattan/food/cheeky%20sandwiches`
      - **Katz's Delicatessen** `/manhattan/food/katz's%20delicatessen`
      - **Veselka** `/manhattan/food/veselka`

    - **Parks** `/manhattan/parks`
      - **Central Park** `/manhattan/parks/central%20park`
      - **Riverside Park** `/manhattan/parks/riverside%20park`
      - **The High Line** `/manhattan/parks/the%20highline`
      - **Washington Square Park** `/manhattan/parks/washington%20square%20park`

  - **Queens** `/queens`
    - **Airports** `/queens/airports`
      - **John F Kennedy International Airport** `/queens/airports/john%20f%20kennedy%20international%20airport`
      - **LaGuardia Airport** `/queens/airports/laguardia%20airport`
    - **Beaches** `/queens/beaches`
      - **Rockaway Beaches** `/queens/beaches/rockaway%20beaches`
  - **Staten Island** `/staten%20island`
    - **Beaches** `/staten%20island/beaches`
      - **Cedar Grove Beach** `/staten%20island/beaches/cedar%20grove%20beach`
      - **Midland Beach** `/staten%20island/beaches/midland%20beach`
      - **South Beach** `/staten%20island/beaches/south%20beach`
      - **Wolfe's Pond Beach** `/staten%20island/beaches/wolfe's%20pond%20beach`
    - **Food** `/staten%20island/food`
      - **Lee's Tavern** `/staten%20island/food/lee's%20tavern`
      - **Ralph's Famous Italian Ices** `/staten%20island/food/ralph's%20famous%20italian%20ices`
      - **Royal Crown Bakery** `/staten%20island/food/royal%20crown%20bakery`
  
---

## Technical ##
Project required the implementation of:
1. Activity page (view and template) rendered at URL `<str:borough>/<str:activity>`(i.e. list of beaches, parks)
2. The Venue page (view and template) rendered at URL `<str:borough>/<str:activity>/<str:venue>` (i.e. details of a venue like Brighton Beach)

The following  in this project:
- Python data structures such as Lists, Dictionaries and their associated methods
- Python Classes and Inheritance
- Django [URLs](https://docs.djangoproject.com/en/3.2/topics/http/urls/) to understand how to capture parameters in views
- Django [Templates](https://docs.djangoproject.com/en/3.2/ref/templates/language/)