CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    studentnumber CHAR(6) NOT NULL
);

CREATE TABLE IF NOT EXISTS groupsschedule (
    id INT AUTO_INCREMENT PRIMARY KEY,
    schedulename VARCHAR(255) NOT NULL,
    groupnumber INT NOT NULL,
    date DATETIME NOT NULL,
    usersid INT NOT NULL
);

CREATE TABLE IF NOT EXISTS groupssetting (
    id INT AUTO_INCREMENT PRIMARY KEY,
    groupname VARCHAR(255) NOT NULL
);

INSERT INTO users (name,studentnumber) VALUES ('John Doe', '022000'), ('Jane Smith', '122001');

INSERT INTO groupsschedule (schedulename,groupnumber,date,usersid) VALUES ('meeting', '1','2024-06-20 15:30:00','2'), ('announcement','2','2024-07-03 19:20:00','1');

INSERT INTO groupssetting (groupname) VALUES ('Ateam'), ('Bteam');