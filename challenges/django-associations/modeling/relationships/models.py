from django.db import models


####
# Language, Framework is a one to many relationship
# One language can have many frameworks
# One framework can only have one language
####

class Language(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    # Language.objects.filter(framework__name='Flask')
    # returns <QuerySet [<Language: Python>]>


class Framework(models.Model):
    name = models.CharField(max_length=10)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    # Framework.objects.filter(language__name='Python')
    # returns <QuerySet [<Framework: Django>, <Framework: Flask>]>


####
# Movie, Charcater is a many to many relationship
# One movie can have many characters
# One character can have many movies
####

class Movie(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    # avengers.character_set.all()
    # return <QuerySet [<Character: America>, <Character: Thor>]>


class Character(models.Model):
    name = models.CharField(max_length=10)
    movies = models.ManyToManyField(Movie)

    def __str__(self):
        return self.name

    # captain_america.movies.all()
    # returns <QuerySet [<Movie: Avengers>, <Movie: Civil War>, <Movie: Thor Movie>, <Movie: Winter>]>
