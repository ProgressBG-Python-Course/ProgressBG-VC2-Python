
CREATE DATABASE IF NOT EXISTS SimpleMusicDB DEFAULT CHARACTER set utf8 default collate utf8_bin;
USE SimpleMusicDB;

DROP TABLE IF EXISTS album;
CREATE TABLE album(
  id int(11) NOT NULL AUTO_INCREMENT,
  album_name varchar(255) DEFAULT NULL,
  artist_id smallint(5),
  album_id smallint(4),

  PRIMARY KEY (`id`)
  FOREIGN KEY(artist_id) REFERENCES artists(id)
  FOREIGN KEY(artist_id) REFERENCES artists(id)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;
SET character_set_client = @saved_cs_client;

CREATE TABLE artists (
  id    INTEGER PRIMARY KEY,
  name  TEXT
);

CREATE TABLE tracks (
  traid     INTEGER,
  title   TEXT,
  artist INTEGER,
  FOREIGN KEY(artist) REFERENCES artists(id)
);