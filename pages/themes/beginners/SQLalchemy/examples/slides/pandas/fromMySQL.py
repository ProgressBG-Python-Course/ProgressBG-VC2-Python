import MySQLdb
mysql_cn= MySQLdb.connect(host='myhost',
          port=3306,user='myusername', passwd='mypassword',
          db='information_schema')
df_mysql = pd.read_sql('select * from VIEWS;', con=mysql_cn)
print 'loaded dataframe from MySQL. records:', len(df_mysql)
mysql_cn.close()