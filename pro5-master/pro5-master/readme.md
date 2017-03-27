installation instructions:
    * install python 2.7 (This will install pip and python)
    * navigate to myapp folder and run the following command :
        pip install -r requirements.txt
        (This will install dependencies)
    * Now run the following command :
        pip install git+https://github.com/django-nonrel/django@nonrel-1.5
        (This will install the compatible django version and django nonrel)
    * to get site id : that needs to be placed in settings.py use the following commands
        python manage.py shell
        from django.contrib.sites.models import Site
        s = Site()
        exit()
        python ./manage.py tellsiteid
    * Note: django non rel doesnt support django 1.7
    * Now create a super user using the following command:
        // admin usage
        python manage.py createsuperuser

    * If you get error in the launch of django from django.apps import apps apps not found
       simply comment out the line like this in __init__.py in django_extensions:
       # from django.apps import apps
    * For starting mongo.cmd make a .cmd file with the following content:
        mongod.exe --dbpath=<path to db>
        Ex : mongod.exe --dbpath=E:\programfiles\mongodb