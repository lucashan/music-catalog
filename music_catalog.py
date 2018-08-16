import sys
from array_list import *
from linked_list import *


# a Song represents tracks and its information
class Song:
    def __init__(self, title, artist, album, index):
        self.title = title
        self.artist = artist
        self.album = album
        self.index = index

    def __repr__(self):
        return "Song({!r}, {!r}, {!r}, {!r})"\
            .format(self.title, self.artist, self.album, self.index)


# Song Menu
def menu():
    print("Song Catalog")
    print("   1) Print Catalog\n   2) Song Information\n   3) Sort\n   4) Add Songs\n   0) Quit")
    user_input = input("Enter selection: ")
    return user_input


# Sort Menu
def sort_menu():
    print("\nSort Songs")
    print("   0) By Number\n   1) By Title\n   2) By Artist\n   3) By Album")
    user_input = input("Sort by: ")
    print()
    return user_input


# Returns song information from text file input to list of Song objects
def file_read(filename):
    infile = open(filename, 'r')
    main_list = empty_list()
    global invalid_lines
    invalid_lines = []
    line_count = 1
    list_index = 0
    number = 0
    for line in infile:
        count = 0
        line = line.strip()
        if line == '':
            pass
        else:
            list1 = line.split('--')
            if len(list1) == 3:
                new_song = Song(list1[0], list1[1], list1[2], number)
                main_list = add(main_list, list_index, new_song)
                list_index += 1
                number += 1
            else:
                invalid_lines.append(line_count)
        line_count += 1
    return main_list
    infile.close()


def main():
    filename = sys.argv[1]
    main_list = file_read(filename)
    if len(invalid_lines) > 0:
        print("Catalog input errors:")
        for line in invalid_lines:
            print("line", line, ": malformed song information ")
        print()
    user_input = menu()
    while user_input != "0" and user_input != "end-of-file":

        if user_input == "1":                                       # Print Catalog
            for i in range(0, length(main_list)):
                song = get(main_list, i)
                print("{!r}--{}--{}--{}".format(song.index, song.title, song.artist, song.album))
            print()

        elif user_input == "2":                                     # Song information
            song_num = input("Enter song number: ")
            if int(song_num) >= length(main_list) or int(song_num) < 0:
                print("\n... Invalid song number")
                print()
            else:
                valid_song = search(main_list, song_num)
                print("\nSong information ...")
                print("   Number:", valid_song.index)
                print("   Title:", valid_song.title)
                print("   Artist:", valid_song.artist)
                print("   Album:", valid_song.album)
                print()

        elif user_input == "3":                                      # Sort songs
            menu_choice = sort_menu()
            main_list = sort_catalog(main_list, menu_choice)

        elif user_input == "4":                                      # Add new songs
            load_file = input("Enter name of file to load: ")
            try:
                add_file = open(load_file, 'r')
                global song_no
                line_count = 1
                index = length(main_list)
                error_lines = []
                for line in add_file:
                    line = line.strip()
                    if line == '':
                        pass
                    else:
                        line_list = line.split('--')
                        if len(line_list) == 3:
                            new_song = Song(line_list[0], line_list[1], line_list[2], song_no)
                            main_list = add(main_list, index, new_song)
                            song_no += 1
                            index += 1
                        else:
                            error_lines.append(line_count)
                        line_count += 1
                if sort_choice is not None:
                    main_list = sort_catalog(main_list, sort_choice)
                if len(error_lines) > 0:
                    print("\nCatalog input errors:")
                    for line in error_lines:
                        print("lines", line, ": malformed song information\n")
            except IndexError:
                print("\nUsage: python3 music_catalog.py <file>\n")
            except FileNotFoundError:
                print("\n'{}': No such file or directory\n".format(load_file))
        else:
            print("Invalid option")
    if user_input == "0":
        exit()


# list string -> list
# helper function that sorts list based on input
def sort_catalog(lst, option):
    if option != '0' and option != '1' and option != '2' and option != '3':
        print("... Invalid sort option\n")
    else:
        if option == '0':
            lst = sort(lst, less_than_index)
        elif option == '1':
            lst = sort(lst, less_than_title)
        elif option == '2':
            lst = sort(lst, less_than_artist)
        elif option == '3':
            lst = sort(lst, less_than_album)
        global sort_choice
        sort_choice = option
    return lst


# song song -> bool
# return True if first song's index is less-than second index
def less_than_index(song1, song2):
    if song1.index < song2.index:
        return True
    else:
        return False


# song song -> bool
# return True if first song's title is less-than second index
def less_than_title(song1, song2):
    if song1.title < song2.title:
        return True
    elif song1.title == song2.title:
        if song1.artist < song2.artist:
            return True
        elif song1.artist == song2.artist:
            if song1.title < song2.title:
                return True
            elif song1.title == song2.title:
                return less_than_index(song1, song2)
    return False


# song song -> bool
# return True if first song's title is less-than second index
def less_than_artist(song1, song2):
    if song1.artist < song2.artist:
        return True
    elif song1.artist == song2.artist:
        if song1.album < song2.album:
            return True
        elif song1.album == song2.album:
            if song1.title < song2.title:
                return True
            elif song1.title == song2.title:
                return less_than_index(song1, song2)
    return False


# song song -> bool
# return True if first song's title is less-than second index
def less_than_album(song1, song2):
    if song1.album < song2.album:
        return True
    elif song1.album == song2.album:
        if song1.artist < song2.artist:
            return True
        elif song1.artist == song2.artist:
            if song1.title < song2.title:
                return True
            elif song1.title == song2.title:
                return less_than_index(song1, song2)
    return False

sys.setrecursionlimit(10100)
