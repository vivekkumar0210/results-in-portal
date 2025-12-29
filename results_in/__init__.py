import pymysql

pymysql.version_info = (2, 2, 7, "final", 0) # <--- Ye line version check bypass karegi
pymysql.install_as_MySQLdb()