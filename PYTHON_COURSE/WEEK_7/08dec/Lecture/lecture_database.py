import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()

sql = """CREATE TABLE CUSTOMERS(
    ID  INT                 NOT NULL,
    NAME VARCHAR (20)       NOT NULL,
    AGE INT                 NOT NULL,
    ADDRESS CHAR (25) ,
    SALARY  DECIMAL (18,2),
    PRIMARY KEY (ID)
"""

c.execute(sql)

c.commit()

c.fetchall("DESC CUSTOMERS")

dir example.db

sqlite3 example.db

sqlite> .schema CUSTOMERS
#cela affiche le tableau

sqlite> SELECT * FROM CUSTOMERS;

sqlite3 example.db

sqlite> INSERT INTO CUSTOMERS(ID, NAME, AGE, ADDRESS, SALARY) VALUES(1, "John Rice", 20, "Ashdod", 8000)

sqlite> SELECT * FROM CUSTOMERS;
#1|John Rice|20|Ashdod|8000
sqlite> INSERT INTO CUSTOMERS(ID, NAME, AGE, ADDRESS, SALARY) VALUES(2, "Syamily", 28, "India", 5000)
#1|John Rice|20|Ashdod|8000
#2|Syamily|28|India|5000

sqlite> SELECT * FROM CUSTOMERS WHERE AGE >= 28
#2|Syamily|28|India|5000
sqlite> SELECT * FROM CUSTOMERS WHERE SALARY < 8000
#2|Syamily|28|India|5000
sqlite> SELECT * FROM CUSTOMERS WHERE SALARY < 10000 OR AGE >= 20
#1|John Rice|20|Ashdod|8000
#2|Syamily|28|India|5000
sqlite> SELECT * FROM CUSTOMERS WHERE SALARY > 4000 AND AGE > 30
# nothing
sqlite> SELECT Name FROM CUSTOMERS WHERE Age >= 20
#John Rice
sqlite> SELECT Name FROM CUSTOMERS WHERE Salary - Age >= 25;
#JohnRice
#Syamily
sqlite> CREATE TABLE USER_LOGINS(
    ID  INT                 NOT NULL,
    NAME varchar(50)        NOT NULL,
    LAST_LOGIN_DATE datetime NOT NULL,
    LAST_INTERACTION_DATE datetime NOT NULL,
    PRIMARY KEY (ID));

sqlite> SELECT * FROM USER_LOGINS;


sqlite> SELECT date();
#2019-12-08
sqlite> SELECT date() as some_date;
#2019-12-08
INSERT INTO USER_LOGINS(ID, NAME, LAST_LOGIN_DATE, LAST_INTERACTION_DATE) VALUES(1, 'John Rice', datetime(), datetime())
sqlite> SELECT * FROM USER_LOGINS;
#1|John Rice|2019-12-08 08:10:04|2019-12-08 08:10:04
sqlite> SELECT * FROM USER_LOGINS WHERE LAST_LOGIN_DATE - LAST_INTERACTION_DATE <= 1;
#1|John Rice|2019-12-08 08:10:04|2019-12-08 08:10:04
sqlite> SELECT *, julianday(LAST_LOGIN_DATE), julianday(LAST_INTERACTION_DATE) FROM USER_LOGINS WHERE julianday(LAST_LOGIN_DATE) - julian(LAST_INTERACTION_DAY) <= 1;



# --------------------------
$ pip install fake2db