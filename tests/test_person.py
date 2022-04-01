import pytest
from viewing_party.person import Person
from viewing_party.movie import Movie

    # def __init__(self, name, watched,friends,subscriptions):
    #     self.name = name
    #     self.watched = watched
    #     self.friends = friends
    #     self.subscriptions = subscriptions
    # def add_watched(self,movie):
    #     self.watched.append(movie)
    # def get_num_watched(self):
    #     return len(self.watched)


def test_1():
    # Arrange
    movie1 = Movie("The JavaScript and the React","Action", 2.2, "Netflix")
    movie2 = Movie("Zero Dark Python","Intrigue", 3, "Disney")
    person = Person("Tom",[movie1],[],"Hulu")

    # Act
    person.add_watched(movie2)

    # Assert
    assert movie2 in person.watched
    assert len(person.watched) == 2

def test_2():
    # Arrange
    movie1 = Movie("The JavaScript and the React","Action", 2.2, "Netflix")
    person = Person("Tom",[movie1],[],"Hulu")

    # Act
    count = person.get_num_watched()

    # Assert
    assert count == 1
