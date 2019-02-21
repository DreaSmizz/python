movies = ["THe Holy Grail", "The Life of Brian", "The Meaning of Life"]
print(movies[1])
cast = ["Cleese", 'Palin', 'Jones', "Idle"]
print(len(cast))
print(cast[1])
cast.append("Gilliam")
print(cast)
cast.pop()
print(cast)
cast.extend(["Gilliam", "Chapman"])
print(cast)
movies.insert(1, 1975)
movies.insert(3, 1979)
movies.append(1983)
print(movies)
fav_movies = ["The Holy Grail", "The Life of Brian"]
for each_flick in fav_movies:
    print(each_flick)

movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91, 
            ["Graham Chapman", ["Micheal Palin", "John Cleese", 
                "Terry Gilliam", "Eric Idle", "Terry Jones"]]]
print(movies)
for each_item in movies:
    print(each_item)

names = ['Micheal', 'Terry']
isinstance(names, list)
num_names = len(names)
isinstance(num_names, list)

for each_item in movies:
    if isinstance(each_item, list):
        for nested_item in each_item:
            if isinstance(nested_item, list):
                for deeper_item in nested_item:
                    print(deeper_item)                
            else:
                print(nested_item)
    else:
        print(each_item)
