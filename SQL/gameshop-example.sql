CREATE DATABASE IF NOT EXISTS game_shop_example;
USE game_shop_example;

/*Creation of the Customer information table*/
CREATE TABLE customerinformation
(ID INT AUTO_INCREMENT,
firstname VARCHAR(20) NOT NULL,
secondname VARCHAR(20) NOT NULL,
address1 VARCHAR(120) NOT NULL,
address2 VARCHAR(120) NULL,
address3 VARCHAR(120) NULL,
city VARCHAR(100) NOT NULL,
postcode VARCHAR (10) NOT NULL,
PRIMARY KEY(ID)
);

/*Insertion of Sample Data*/
INSERT INTO customerinformation (firstname,	secondname,	address1, address2, city, postcode) 
VALUES ('Gabe', 'Newell', 'Volvo HQ', 'Money Heap Mountain', 'Steam Summer City', 'LE3 3E7');
INSERT INTO customerinformation (firstname,	secondname,	address1, city, postcode) 
VALUES ('Reece', 'Gardner', '123 Holbeck Avenue', 'Leeds', 'LS7 8QE'),
('Meme', 'Machine', 'Hoist House', 'Leeds', 'LS1 2QR'),
('Edward', 'Scissorhands', 'Waterlane House', 'York', 'YO1 2PR'),
('Nathan', 'Oconnor', '123 Dublin Avenue', 'Dublin', 'DB12 Q8U'),
('Ayyyyy', 'Lmayo', 'Area 51', 'Nevada', 'N02 1982'),
('Ya', 'Boi', 'Buckingham Palace', 'London', 'SW1A 1AA');

/*Creation of the Product Catalogue*/
CREATE TABLE productcatalogue(
productid INT AUTO_INCREMENT,
productname VARCHAR(30) NOT NULL,
pegi ENUM('3', '7', '12', '16', '18') NOT NULL,
genre VARCHAR(20) NOT NULL,
releasedate DATE,
stock INT NOT NULL,
PRIMARY KEY(productid)
);

/*Insertion of Sample Data*/
INSERT INTO productcatalogue (productname, pegi, genre, releasedate, stock)
VALUES ('SKYRIM REMASTERED', '12', 'TODDSWHITEWHALE', '2030-11-30', 14586),
('CHEF: THE VIDEO GAME', '18', 'GRITTY', '2018-04-01', 10546),
('TEAM FORTRESS 4', '18', 'HATSIMULATOR', '2020-11-30', 10545),
('OUTER WILDS', '12', 'EXPLORATION', '2019-08-22', 18493),
('FIFA23', '7', 'GAMBLING', '2022-10-10', '17283'),
('YET ANOTHER MOBA', '12', 'TIMESINK', '2021-11-30', 15555),
('FAR CREED 12', '12', 'UBISOFT SANDBOX', '2022-01-14', 17289);

/*Creation of the Order information table*/
CREATE TABLE orderhistory(
orderid INT AUTO_INCREMENT,
customer INT NOT NULL,
product INT NOT NULL,
transactiontime DATETIME DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY (orderid),
FOREIGN KEY (customer) REFERENCES customerinformation(ID), 
FOREIGN KEY (product) REFERENCES productcatalogue(productid) 
);

/*Insertion of Sample Data*/
INSERT INTO orderhistory (customer, product)
VALUES (1,4), (7,7), (3,2), (2,1), (6,4), (6,6), (2,7); /*Manually Input this into the CLI*/
