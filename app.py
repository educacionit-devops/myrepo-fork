MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see all your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []

def add_movie():
    title = input("Enter the movie title: ")
    director = input("enter the movie director: ")
    year = input("Enter the movie release year: ")

    movies.append({"name": title,
                "director": director,
                "year": year
    })

def list_movies():
    print(movies)

def print_movie():
    title = input("Enter movie title: ")
    for movie in movies:
        if(movie["name"] == title):
            print(movie)
            return
    
    print("no movie was found with that title")


user_options = {
    "a": add_movie,
    "l": list_movies,
    "f": print_movie
}

selection = input(MENU_PROMPT)

while selection != 'q':
   if selection in user_options.keys():
        user_options[selection]()
   else:
        print("invalid input") 
   selection = input(MENU_PROMPT)
   