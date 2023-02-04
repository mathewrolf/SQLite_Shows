from typing import List, Dict, Union
from .database_connection import DatabaseConnection
from sqlite3.dbapi2 import IntegrityError

show = Dict[str , Union[str, list]]  

def create_show_table() -> None:
    
    with DatabaseConnection('data.db') as connection:
        c = connection.cursor() 

        c.execute('CREATE TABLE IF NOT EXISTS shows(name TEXT PRIMARY KEY, season TEXT, ep TEXT)')  
    

def add_show(name:str, season:str, ep:str) -> None: 
    with DatabaseConnection('data.db') as connection:
        c = connection.cursor() 

        try:
            c.execute('INSERT INTO shows VALUES(?, ?, ?)', (name, season, ep)) #never use f-strings in connections because of attacks

        except IntegrityError:
            print('Show already in library.')



def get_all_shows() -> str:
    with DatabaseConnection('data.db') as connection:
        c = connection.cursor()

        c.execute('SELECT * from shows') 
        show_list = [{'name': row[0], 'season': row[1], 'ep': row[2]} for row in c.fetchall()]
    

    for show in show_list:
        print("...")
        print(f"{show['name']} : Season {show['season']}, Episode {show['ep']}")
    return "..."


def mark_progress(name:str, season:str, ep:str) -> None:
   with DatabaseConnection('data.db') as connection:
    c = connection.cursor()

    c.execute(f'UPDATE shows SET season=? WHERE name=?', (season, name))    
    c.execute(f'UPDATE shows SET ep=? WHERE name=?', (ep, name))    


def delete_show(name:str):
    with DatabaseConnection('data.db') as connection:
        c = connection.cursor() 

        c.execute('DELETE FROM shows WHERE name=?', (name))  
