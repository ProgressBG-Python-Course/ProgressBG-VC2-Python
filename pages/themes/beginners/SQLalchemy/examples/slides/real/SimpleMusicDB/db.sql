create database SimpleMusicDB default character set utf8 default collate utf8_bin;


CREATE USER pythontest@localhost IDENTIFIED BY '123';

GRANT ALL PRIVILEGES ON SimpleCompanyDB.* to pythontest@'%' IDENTIFIED BY '123';

-- GRANT ALL PRIVILEGES ON pac.* to pacuser@'localhost' IDENTIFIED BY 'pacuser';
  GRANT ALL PRIVILEGES ON SimpleMusicDB.* to pythontest@'%';