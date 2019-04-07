#initializing our blockchain list
blockchain=[]

def get_last_blockchain_value():
    return blockchain[-1]

# def add_value(transaction_amount, last_transaction=[1]):
#     blockchain.append([last_transaction,transaction_amount])

def get_user_input():
    user_input=float(input("please input the transcation amount"))
    return(user_input)


tx_amount=get_user_input()
# add_value(tx_amount)

j=0

# while(j<len(blockchain)-1):
#     if blockchain[j] != blockchain[j+1][0]:
#         print("not secure!!!")
#         break;
#     j=j+1

#inserting data in database
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="omegadb"
)

mycursor = mydb.cursor()

#fetching data
mycursor.execute("SELECT * FROM chain")

myresult = mycursor.fetchall()
rs = list(myresult[0])
print(rs)
rs.append(tx_amount)
print(rs)


sql = "UPDATE chain SET data = %s"
val = (str(rs),)
mycursor.execute(sql, val)


mydb.commit()
