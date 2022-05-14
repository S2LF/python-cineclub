import os
import json 
import logging

LOGGER = logging.getLogger()

CUR_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(CUR_DIR, 'data', 'movies.json')

def get_movies():
    """
    Return a list of movies.
    """
    with open(DATA_FILE) as f:
        movies_title = json.load(f)
    return [Movie(movie_title) for movie_title in movies_title]
    

class Movie():
    """
    Class that represents a movie
    """

    def __init__(self, title):
        """
        Constructor
        """
        self.title = title.title()

    def __str__(self):
        """
        String representation of the movie
        """
        return self.title

    def _get_movies(self):
        """
        Get the movies from the file
        """
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
           return json.load(f)
    
    def _write_movies(self, movies):
        """
        Write the movies to the file
        """
        with open(DATA_FILE, "w", encoding='utf-8') as f:
            json.dump(movies, f, indent=4)

    def add_to_movies(self):
        """
        Add the movie to the file
        """
        movies = self._get_movies()
        # Check if the movie is already in the file
        if self.title in movies:
            LOGGER.warning(f"Le film '{self.title}' est déjà dans la liste.")
            return False
        else :
            movies.append(self.title)
            self._write_movies(movies)
        return True

    def remove_from_movies(self):
        """
        Remove the movie from the file
        """
        movies = self._get_movies()
        # Check if the movie is in the file
        if self.title not in movies:
            LOGGER.warning(f"Le film '{self.title}' n\'est pas dans la liste.")
            return False
        else :
            movies.remove(self.title)
            self._write_movies(movies)
        return True


if __name__ == '__main__':
    m = Movie("The Godfather")
    # m.add_to_movies()
    m.remove_from_movies()
    # m._write_movies(['le seigneur des anneaux'])
    print(m._get_movies())
    print(get_movies())