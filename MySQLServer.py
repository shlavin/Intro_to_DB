

import mysql.connector


def create_database():
    try:
        # Connecting to MySQL server 
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Kahumu2002_'   
        )

        if connection.is_connected():
            cursor = connection.cursor()

            
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error while connecting to MySQL: {err}")

    finally:
        
        try:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection closed.")
        except:
            pass
if __name__ == "__main__":
    create_database()
