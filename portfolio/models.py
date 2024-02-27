from django.db import models

# Create your models here.

class Project:
    def __init__(self, title, filenames):
        self.title = title
        self.filenames = filenames
        self.filepath = f"portfolio/content/{title}/"
