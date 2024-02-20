import cx_Oracle
# src: https://www.geeksforgeeks.org/oracle-database-connection-in-python/

#set connection to database
user = 'oil'
password = 'oil1234'
host = 'localhost'
sid = 'orcl'

def getData(table:str, column = "*", condition = '1=1') -> str:
    """
    what you want just tell me!!
    
    Args:
        table (str): table name like "student"
        column (str, optional): column name like (col1, col2, col3). Defaults is "*"
        condition (str, optional): condition like WHERE stdid = '663380035-4' Defaults is always True
    Raises:
        ValueError: _description_
    Returns:
        _type_: data or error
    """
    if table:
        query_str = f"select {column} from {table} where {condition}"
        # print(query_str)
    else:
        print('invalid table')
        return
    try:
        con = cx_Oracle.connect(f'{user}/{password}@{host}:1521/{sid}')
    except cx_Oracle.DatabaseError as er:
        print('There is an error in the Oracle database:' + str(er))
        return
    else:
        try:
            cursor = con.cursor()
            cursor.execute(query_str)
            rows = cursor.fetchall()
            return rows
        except cx_Oracle.DatabaseError as er:
            print('There is an error in the Oracle database:' + str(er))
            return
        except Exception as er:
            print('Error:' + str(er))
            return
        finally:
            if cursor:
                cursor.close()
    finally:
        if con:
            con.close()

def insertData(table:str, primary_key:str, values:str) -> bool:
    """_summary_
    Args:
        table (str): table name like "student"
        values (str): insert values like (stdid = '663380035-4', stdfname='ธนรัตน์', stdlname='แซ่เฮีย')
    """
    try:
        con = cx_Oracle.connect(f'{user}/{password}@{host}:1521/{sid}')
        cursor = con.cursor()
        if not check_primary_key(table=table, primary_key=primary_key):
            print(f"Primary key '{primary_key}' already exists.")
            return False
        else:
            cursor.execute(f'insert into {table} values({primary_key}, {values})')
            con.commit()
            return True
    except cx_Oracle.DatabaseError as e:
        print("There is a problem with Oracle" + str(e))
        return False
    except Exception as er:
        print("Error " + str(er))
        return False
    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()

def check_primary_key(table:str, primary_key:str) -> bool:
    allData = getData(table=table)
    for i in allData:
        if primary_key == str(i[0]):
            return False
    return True

def updateData(table:str, set:str, condition:str) -> bool:
    """_summary_
    Args:
        table (str): table name like "student"
        set (str): set values like stdfname = 'oil'
        condition (str): condition like WHERE stdid = '663380035-4'
    """
    try:
        con = cx_Oracle.connect(f'{user}/{password}@{host}:1521/{sid}')
        cursor = con.cursor()
        cursor.execute(f'update {table} set {set} where {condition}')
        con.commit()
        return True
    except cx_Oracle.DatabaseError as e:
        print("There is a problem with Oracle" + str(e))
        return False
    except Exception as er:
        print("Error " + str(er))
        return False
    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()

# print(getData(table="tester"))
# insertData(table="tester", primary_key='10', values="'oil', 'haha', 01212155555")
# print(updateData(table="tester", set="fname = 'heheheheh'", condition="id = 6"))

