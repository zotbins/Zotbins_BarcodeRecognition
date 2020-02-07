import sqlite3

#type is a string
def getInstructionByNumber (type):
    connection = sqlite3.connect("BarcodeDataBase.db")
    cursor = connection.cursor()
    cursor.execute("SELECT Instructions FROM Barcodes WHERE Type='%d';" %type)
    results = cursor.fetchall()

    print(results[0][0])

    cursor.close()
    connection.close()

    return results[0][0]