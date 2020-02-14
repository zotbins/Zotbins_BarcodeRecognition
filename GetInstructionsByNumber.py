import sqlite3

def getInstructionByNumber (number):
    connection = sqlite3.connect("BarcodeDataBase.db")
    cursor = connection.cursor()
    cursor.execute("SELECT Instructions FROM Barcodes WHERE Number='%s';" %number)
    results = cursor.fetchall()

    cursor.close()
    connection.close()

    return results[0][0]

#test
#myNumber = '49000052350'
#print(getInstructionByNumber(myNumber))