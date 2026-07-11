import pymysql


def get_connection():

    conn = pymysql.connect(

        host="mysql-b0aee9a-kimmai291205-8020.c.aivencloud.com",

        port=26069,

        user="avnadmin",

        password="AVNS_BS8nFXF-tG8IEc29iBv",

        database="company",

        ssl={
            "ca": "ca.pem"
        }

    )

    return conn
