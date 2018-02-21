=============
Django Anchor
=============

Migration substitutes to anchor models when refactoring.

Installing
----------

Install Django Anchor::

    pip install django-anchor

Using it
--------

Make sure you have your table name explicitly named using `Meta.db_table` in your
model first!

Move a model between two Django apps. Make sure this is the only migration inducing
change you make.

Run `makemigrations` to create the migration files

In each file replace this::

    from django.db import migrations

With this::

    from anchor import anchor as migrations

All done.
