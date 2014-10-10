import sqlite3 as dbapi

khan = dbapi.connect("portal_mammals")
kur = khan.cursor()
kur.execute("SELECT mo, dy, yr, plot FROM PortalMammals_main where yr=2002")#runs query in database
#samples_2002 = kur.fetchall()
#print samples_2002

record = kur.fetchone()
while record:
    print(record)
    record = kur.fetchone()
    
