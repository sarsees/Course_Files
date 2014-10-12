import sqlite3 as dbapi

con = dbapi.connect("portal_mammals")
cur = con.cursor()
#cur.execute("DROP TABLE FieldNotes")
cur.execute("CREATE TABLE FieldNotes (Day REAL, Month REAL, Year REAL, Notes VARCHAR)")
# Adding field values to FieldNotes
cur.execute("""INSERT INTO FieldNotes (Day, Month, Year, Notes) 
                      VALUES (01, 04, 1963, 'Just completed the April 1963 census of the site. 
                      The region is teeming with Dipodomys spectabilis. 
                      Using the time machine to conduct trapping prior to the start of the study 
                      is working out great!')""")
con.commit()
# Adding another set of new field values-- sqlite3.OperationalError: near "t": syntax error
cur.execute("""INSERT INTO FieldNotes (Day, Month, Year, Notes) 
                      VALUES (01, 10, 2013, 'Vegetation seems to have returned to normal for this time of year. 
                      The landscape isn``t exactly green, but there is a decent amount of plant activity and there 
                      should be enough food for the rodents to the winter')""")
con.commit()

#Update a mistaken value
cur.execute("UPDATE FieldNotes SET Year = '2012' WHERE Day = 1 AND Month = 10 AND Year = 2013")
con.commit()

