import os
import psycopg2
from dotenv import find_dotenv, load_dotenv
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
db_password = os.getenv('db_password')

# Setup connection to database
conn = psycopg2.connect(
    dbname='bachelor_degree',
    user='postgres',
    password=db_password,
    host='localhost',
    port='5432'
)
cur = conn.cursor()

folder_path = r'data\polish_trade_gus'

# Iterating through files in a folder
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        try:
            with open(file_path, 'r') as f:
                # Reading data and replacing commas with dots
                content = f.read().replace(',', '.')
                
                # Creating a temporary file to store modified data
                temp_file_path = file_path.replace('.csv', '_temp.csv')
                with open(temp_file_path, 'w') as temp_file:
                    temp_file.write(content)

                # Importing data into the trade_raw table from the temporary file
                with open(temp_file_path, 'r') as temp_file:
                    cur.copy_expert("COPY trade_raw FROM STDIN WITH CSV HEADER DELIMITER ';'", temp_file)

                # Informing about successful import
                print(f"Imported file: {filename}")

                # Deleting the temporary file
                os.remove(temp_file_path)
        except Exception as e:
            # Informing about an error during import
            print(f"Error importing file {filename}: {e}")

# Committing changes and closing the connection
conn.commit()
cur.close()
conn.close()