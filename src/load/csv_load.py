from dotenv import load_dotenv
import os
import mysql.connector


def load_csv(datas):

    load_dotenv(override=True) #override=true override the windows env variable

    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    database = os.getenv("DB_NAME")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")

    print(os.getenv("DB_HOST"))
    print(os.getenv("DB_USER"))
    print(os.getenv("DB_NAME"))

    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")

    )

    if connection.is_connected():
        print("connection is established")

        cursor = connection.cursor()

        query = """
            INSERT INTO EMPLOYEE (employee_id,name,department,salary,email,joining_date,processing_date)
            VALUES (%s,%s,%s,%s,%s,%s,%s)
            """
        #values =("101","John Doe","IT",75000,"john.doe@company.com","2021-03-15","2026-11-05")
        
        unique_id = {}

        cursor.execute("select employee_id from employee")
        unique_id = {str(row[0]) for row in cursor.fetchall()}

        values = []

        for rec in datas:
            if rec["employee_id"] not in unique_id:
                values.append(
                    (
                        rec["employee_id"],
                        rec["name"],
                        rec["department"],
                        rec["salary"],
                        rec["email"],
                        rec["joining_date"],
                        rec["process_date"]
                    )
                )
     

        cursor.executemany(query,values)

        connection.commit()

        connection.close()
    else:
        print("connection is failed")
        



    