import sqlite3

#type is a string
def getInstructionsByType (type):
    connection = sqlite3.connect("BarcodeDataBase.db")
    cursor = connection.cursor()
    cursor.execute("SELECT Instructions FROM Barcodes WHERE Type='%s';" %type)
    results = cursor.fetchall()

    cursor.close()
    connection.close()

    return results[0][0]

#test
#myType = 'fork'
#print(getInstructionsByType(myType))