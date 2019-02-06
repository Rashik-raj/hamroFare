import sqlite3
from sqlite3 import Error

def fare(distance):
    if(distance<=5):
        return 10
    elif(distance>5 and distance<=8):
        return 13
    elif(distance>8 and distance<=15):
        return 17
    else:
        return 25

def entryCheck(cardKey):
    database = "db.sqlite3"
    conn = create_connection(database)
    cur = conn.cursor()
    query = """ SELECT * FROM user_User where card_key = ?"""
    cur.execute(query, (cardKey,))
    rows = cur.fetchall()
    for row in rows:
        data=row[0]
    cardId = data
    query = """ SELECT * FROM user_Card where card_key_id = ?"""
    cur.execute(query, (cardId,))
    rows = cur.fetchall()
    for row in rows:
        data = row[5]
    balance = data
    print("\nbalance of the user is",balance)
    if(balance < 25):
        print("\nNOT ENOUGH BALANCE (BEEP! BEEP!)\n")
        return False
    else:
        print("\nWELCOME! ENJOY THE JOURNEY!\n")
        return True



def updateBalance(cardKey,cost,deviceId1,deviceId2):
    #deduce balance of the user

    database = "db.sqlite3"
    conn = create_connection(database)
    cur = conn.cursor()
    query = """ SELECT * FROM user_User WHERE card_key = ?"""
    cur.execute(query, (cardKey,))
    rows = cur.fetchall()
    for row in rows:
        data = row[0]
    cardId = data
    query = """ SELECT * FROM user_Card WHERE card_key_id = ?"""
    cur.execute(query, (cardId,))
    rows = cur.fetchall()
    for row in rows:
        data = row[5]
    balance = data
    balance-=cost
    print("updated balance of the user is",balance)
    query = """ UPDATE user_Card SET balance = ? WHERE card_key_id = ?"""
    cur.execute(query, (balance,cardId,))
    conn.commit()
    conn.close()

    #append balance to the owner

    conn = create_connection(database)
    cur = conn.cursor()
    query = """ SELECT * FROM company_device WHERE enter_device_id = ?"""
    cur.execute(query, (deviceId1,))
    rows = cur.fetchall()
    for row in rows:
        data=row[4]
    balance = data
    print("\nbalance of the vehicle owner is", balance)
    balance+=cost
    print("\nupdated balance of the vehicle owner is",balance)
    query = """ UPDATE company_device SET balance = ? WHERE enter_device_id = ?"""
    cur.execute(query, (balance,deviceId1,))
    conn.commit()
    conn.close()


def transaction (origin,destination,distance,deviceId1,deviceId2,cardKey):
    cost = fare(distance)
    updateBalance(cardKey,cost,deviceId1,deviceId2)


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None

def main():

    #these variables values comes from the device API

    cardKey="9fc1-661b-9760-3e9b"
    deviceId1=123456
    deviceId2=456789
    origin="kalanki"
    destination="kapan"
    distance=8

    if entryCheck(cardKey):
        transaction(origin,destination,distance,deviceId1,deviceId2,cardKey)


if __name__ == '__main__':
    main()

