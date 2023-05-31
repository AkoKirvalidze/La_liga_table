import sqlite3


class TeamData:
    def __init__(self, data_name):
        self.conn = sqlite3.connect(data_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            create table if not exists La_Liga (
                id integer primary key,
                name text,
                points integer,
                matches integer,
                wins integer,
                loses integer,
                draws integer,
                GD text
            )
        """)
        self.conn.commit()

    def add_team(self, team):
        self.cursor.execute("""
            insert into La_liga(name, points, matches, wins, loses, draws, GD)
            values (?,?,?,?,?,?,?)
        """, (team.name, team.points, team.matches, team.wins, team.loses, team.draws, team.GD))
        self.conn.commit()

    def UCL_qualification(self):
        self.cursor.execute("""
            SELECT name FROM La_liga LIMIT 4
        """)
        raw = self.cursor.fetchall()
        for i in range(0, 4):
            print(raw[i][0])

    def EU_qualification(self):
        self.cursor.execute("""
            SELECT name FROM La_liga LIMIT 2 offset 4
        """)
        raw = self.cursor.fetchall()
        for i in range(0, 2):
            print(raw[i][0])

    def CF_qualification(self):
        self.cursor.execute("""
               SELECT name FROM La_liga where id=7
           """)
        raw = self.cursor.fetchall()
        print(raw[0][0])

    def relegated(self):
        self.cursor.execute("""
               SELECT name FROM La_liga LIMIT 3 offset 17
           """)
        raw = self.cursor.fetchall()
        for i in range(0, 3):
            print(raw[i][0])

    def get_amount(self, id):
        id = id + 1
        self.cursor.execute("""
            select id, name from La_liga where id<?
        """, (id,))
        raw = self.cursor.fetchall()
        for i in range(0, id - 1):
            print(f"{raw[i][0]} - {raw[i][1]}")

    def table(self):
        self.cursor.execute(""" 
            select * from La_liga
        """)
        raw = self.cursor.fetchall()
        for i in raw:
            print(i)

    def stats(self, name):
        self.cursor.execute("""
                    select id, name, points, matches, wins, loses, draws,GD from La_liga where name = ?
                """, (name,))
        raw = self.cursor.fetchone()
        if raw[0] == 1:
            print(f'{raw[1]} --- Winners!, Points - {raw[2]}, Matches - {raw[3]}, Wins - {raw[4]}, loses - {raw[5]}, '
                  f'draws - {raw[6]}, Goal Difference - {raw[7]}')
        else:
            print(
                f'{raw[1]} --- Place - {raw[0]}, Points - {raw[2]}, Matches - {raw[3]}, Wins - {raw[4]}, loses - {raw[5]}, draws - {raw[6]}, Goal Difference - {raw[7]} ')