import sqlite3

conn =sqlite3.connect("movies.db")
conn.execute(
'''
CREATE TABLE IF NOT EXISTS MOVIES(
NAME VARCHAR2(20) NOT NULL,
ACTOR VARCHAR2(20) NOT NULL,
ACTRESS VARCHAR2(20) NOT NULL,
DIRECTOR VARCHAR2(20) NOT NULL,
YEAR_OF_RELEASE INTEGER NOT NULL,
PRIMARY KEY(NAME,DIRECTOR,YEAR_OF_RELEASE)
);
''')
conn.close()
while(True):
    choice=int(input('''
--------------------------MOVIE DATABASE----------------------
                    1.Add a movie
                    2.Display the Database
                    3.Search for a movie
                    4.Exit
--------------------------------------------------------------
Enter your choice: 
'''))
    if choice==1:
        conn=sqlite3.connect("movies.db")
        conn.execute("INSERT INTO MOVIES VALUES(?,?,?,?,?)",(input("Enter the name of the movie: "),input("Enter the name of the actor: "),input("Enter the name of the actress: "),input("Enter the name of the director: "),int(input("Enter the year of release: "))))
        conn.commit()
        conn.close()
    if choice==2:
        conn=sqlite3.connect("movies.db")
        cur=conn.cursor()
        cur.execute("SELECT * FROM MOVIES")
        print(cur.fetchall())
        conn.close()
    elif choice==3:
            choice2=int(input('''
--------------------------MOVIE DATABASE----------------------
                        1.Search by name                            
                        2.Search by actor
                        3.Search by actress 
                        4.Search by director
                        5.Search by year of release
--------------------------------------------------------------
Enter your choice:
    '''))
            if choice2==1:
                conn=sqlite3.connect("movies.db")
                cur=conn.cursor()
                cur.execute("SELECT * FROM MOVIES WHERE NAME=?",(input("Enter the name of the movie: "),))
                data=cur.fetchall()
                if(data):
                    print(data)
                else:
                    print("not found")  
                conn.close()
            elif choice2==2:
                conn=sqlite3.connect("movies.db")
                cur=conn.cursor()
                cur.execute("SELECT * FROM MOVIES WHERE ACTOR=?",(input("Enter the name of the actor: "),))
                data=cur.fetchall()
                if(data):
                    print(data)
                else:
                    print("not found")           
                conn.close()
            elif choice2==3:
                conn=sqlite3.connect("movies.db")
                cur=conn.cursor()
                cur.execute("SELECT * FROM MOVIES WHERE ACTRESS=?",(input("Enter the name of the actress: "),))
                data=cur.fetchall()
                if(data):
                    print(data)
                else:
                    print("not found")  
                conn.close()
            elif choice2==4:
                conn=sqlite3.connect("movies.db")
                cur=conn.cursor()
                cur.execute("SELECT * FROM MOVIES WHERE DIRECTOR=?",(input("Enter the name of the director: "),))
                data=cur.fetchall()
                if(data):
                    print(data)
                else:
                    print("not found")  
                conn.close()
            elif choice2==5:
                conn=sqlite3.connect("movies.db")
                cur=conn.cursor()
                cur.execute("SELECT * FROM MOVIES WHERE YEAR_OF_RELEASE=?",(int(input("Enter the year of release: ")),))
                data=cur.fetchall()
                if(data):
                    print(data)
                else:
                    print("not found")  
                conn.close()
            else:
                print("Invalid choice")
    elif choice == 4:
     break
    else:
        print("Invalid choice")
