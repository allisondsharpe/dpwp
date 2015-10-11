class FavoriteMovies(object):
    def __init__(self):
        self.__movie_list = []
        #have an array to hold movie information
        #some way to add to array of movies
        #generate a list of the movies at the end
        #calculate time span between movies

    def add_movie(self, m):
        self.__movie_list.append(m)
        print m.title
        #<Movie Data Object >

    def compile_list(self):
        output = ''
        for movie in self.__movie_list: #for each movie in movie array
            output += 'Title: ' + movie.title + ' (' + str(movie.year) + ') Directed by: ' + movie.director + '<br />'
        return output

    def calc_time_span(self):
        '''
        calculate the time in between movies
        '''
        #years
        years = []
        for movie in self.__movie_list:
            years.append(movie.year)

        print years
        #sort years from low to high
        years.sort()
        print years
        #subtract the low year from the high year
        num = len(years) - 1 #length of array
        span = years[num] - years[0] #last number - first number
        #return the span of time
        return "The span between films entered is " + str(span)

    @property
    def movie_list(self):
        return self.__movie_list

class MovieData(object): #data object
    def __init__(self):
        self.title = ''
        self.__year = 0 #check for valid year
        self.director = ''

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, y): #setter receives information, doesn't return info
        if y > 2014: #if the date is not valid
            print "Error, invalid date!"
            self.__year = 2014
        else:
            self.__year = y