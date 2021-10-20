## weather scrapper

Project setup

1. Create virtual environment:

   ```bash
   python -m venv .venv
   ```

2. To initialize virtual environment execute

   ```bash
   source .venv/bin/activate
   ```

3. Create .env file in the root directory and paste the following code:

    ```bash
        # DJANGO SETTINGS
        SECRET_KEY=django-insecure-)a70$g)@@_9i2@5n7#iehvju!l=y&4l-tbr*)w2=wpp+nsc&f(

        # DATABASE
        DATABASE_NAME=guestbook
        DATABASE_USER=postgres
        DATABASE_HOST=127.0.0.1
        DATABASE_HOST=db
        DATABASE_PORT=5432
        DATABASE_PASSWORD=20eaa344Aef74f9B796baB092389a5234234defjfn645bjr54
   ```

4. To build and up db container execute

   ```bash
   docker-compose up -d --build
   ```

5. Run django server:
    ```bash
   python manage.py runserver
   ```
