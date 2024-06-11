CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    studentnumber INT NOT NULL,
    classtype INT NOT NULL
);

CREATE TABLE IF NOT EXISTS groupsschedule (
    id INT AUTO_INCREMENT PRIMARY KEY,
    schedulename VARCHAR(255) NOT NULL,
    groupnumber INT NOT NULL,
    date DATETIME NOT NULL,
    usersid INT NOT NULL
);

INSERT INTO users (name,studentnumber,classtype) VALUES ('John Doe', '22000','1'), ('Jane Smith', '22001','2');

INSERT INTO groupsschedule (schedulename,groupnumber,date,usersid) VALUES ('meeting', '1','2024-06-20 15:30:00','2'), ('announcement','3','2024-07-03 19:20:00','1');
