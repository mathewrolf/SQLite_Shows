from SQLite3 import SQLite_databases
db = SQLite_databases 

USER_CHOICE = """
Enter:
- 'a' to add a new show
- 'l' to list all shows
- 'r' to mark a show's progress
- 'd' to delete a show
- 'q' to quit
Your choice: """


def menu():
    db.create_show_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_show()
        elif user_input == 'l':
            list_shows()
        elif user_input == 'r':
            watch_progress()
        elif user_input == 'd':
            prompt_delete_show()

        user_input = input(USER_CHOICE) 


def prompt_add_show():
    name = input('Enter the show: ')
    season = input('Enter Current Season: ')
    ep = input('Enter Current Episode: ')
    db.add_show(name, season, ep) 
   


def list_shows():
    print(db.get_all_shows()) 


def watch_progress():
    name = input('Enter show name you wish to update your progress on: ')
    season = input('Enter Current Season: ')
    ep = input('Enter Current Episode: ')
    db.mark_progress(name, season, ep)  


def prompt_delete_show():
    name = input('Enter show name to delete: ') 
    db.delete_show(name)  


menu()   