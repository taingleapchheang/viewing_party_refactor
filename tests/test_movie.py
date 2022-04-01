import pytest
from viewing_party.movie import Movie

    # def __init__(self, title, genre, rating, host):
    #     self.title = title
    #     self.genre = genre
    #     self.rating = rating
    #     self.host = host
    
    # def update_rating(self, new_rating):
    #     self.rating = new_rating



def test_1():
    # Arrange
    movie = Movie("The JavaScript and the React","Action", 2.2, "Netflix")

    # Act
    movie.update_rating(5)

    # Assert
    assert movie.rating == 5

