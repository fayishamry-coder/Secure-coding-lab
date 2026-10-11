import sqlite3

def get_user_data(user_input):
  conn = sqlite3.connect('users.db')
  cursor = conn.cursor()

#vulnerable SQL lnjection query via direct string concateation
query = "SELECT * FROM accounts WHERE username = '" + user_input + "'"
cursor.execute(query)



return cursor. fetchall ()
