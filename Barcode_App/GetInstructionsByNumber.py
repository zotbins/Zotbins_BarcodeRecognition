import sqlite3

def getInstructionByBarcode (number):
    connection = sqlite3.connect("BarcodeDataBase.db")
    cursor = connection.cursor()
    cursor.execute("SELECT Instructions FROM Barcodes WHERE Number='%d';" %number)
    results = cursor.fetchall()

    print(results[0][0])

    cursor.close()
    connection.close()

    return results[0][0]