DROP TABLE if EXISTS user;
CREATE TABLE user (
  user_id integer PRIMARY KEY autoincrement,
  username string NOT NULL,
  email string NOT NULL,
  pw_hash string NOT NULL
);

DROP TABLE if EXISTS group;
CREATE TABLE group (
  group_id integer PRIMARY KEY autoincrement,
  image_Id integer,
);

DROP TABLE if EXISTS image;
CREATE TABLE image (
  image_id integer PRIMARY KEY autoincrement,
  name string NOT NULL,
)
