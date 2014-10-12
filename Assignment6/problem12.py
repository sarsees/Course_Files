import sqlite3 as dbapi

con = dbapi.connect("portal_mammals")
cur = con.cursor()
cur.execute("CREATE TABLE OldNewCodeKey(NewCode STR, OldCode STR)")

cur.execute("SELECT new_code, oldcode FROM PortalMammals_species")
myqueryrecord = cur.fetchall()
for newcode, oldcode in myqueryrecord:
    oldcodes = oldcode.split(",")
    for code in oldcodes:
        cur.execute("INSERT INTO OldNewCodeKey VALUES (?,?)", (newcode,code))
con.commit()