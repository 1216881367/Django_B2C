# Django中操作MySQL数据库需要驱动程序MySQLdb.
# MySQLdb只适用于Python2.x的版本，Python3.x的版本中使用PyMySQL替代MySQLdb
import pymysql
pymysql.install_as_MySQLdb()