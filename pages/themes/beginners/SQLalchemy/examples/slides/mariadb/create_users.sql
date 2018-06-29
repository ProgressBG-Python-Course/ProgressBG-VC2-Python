CREATE USER 'demo' IDENTIFIED BY '123';
-- GRANT USAGE ON *.* TO 'demo'@localhost IDENTIFIED BY '123';
GRANT USAGE ON `*`.* TO 'demo'@'%' IDENTIFIED BY '123';
GRANT ALL privileges ON SimpleCompanyDB.* TO 'demo'@'%';
FLUSH PRIVILEGES;

SHOW GRANTS FOR 'demo';