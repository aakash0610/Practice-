# movies = []
MOVIE_ATTRIBUTES = []
menu = """
\tL - List Movies
A - Add a new movie
W - Watch a new movie
Q - Quit"""
print(menu)
user_choice = input("Choice: ")

in_file = open("movies.csv","W")
movies = []
in_file.close()

while user_choice != "Q":
    if user_choice == "A":
        movie_name = input("Enter a movie name: ")
        MOVIE_ATTRIBUTES.append(movie_name)
        year_released = input("Year of release: ")
        MOVIE_ATTRIBUTES.append(year_released)
        movie_category = input("Category: ")
        MOVIE_ATTRIBUTES.append(movie_category)
        MOVIE_ATTRIBUTES.append("u")

    # elif user_choice == "L":
    #     # in_file = open("trial.csv", "r")
    #     # movie_list = in_file.readlines()
    #     for line in movie_list:
    #         counter = 1
    #         movie_attributes = line.strip()
    #         if movie_attributes[4] == "u":
    #             print("{}.* {:70} - {} ({})").format(counter, movie_attributes[0], movie_attributes[1],
    #                                                  movie_attributes[2])
    #         elif movie_attributes[4] == "w":
    #             print("{}. {:70} - {} ({})").format(counter, movie_attributes[0], movie_attributes[1],
    #                                                 movie_attributes[2])
    #     in_file.close()
