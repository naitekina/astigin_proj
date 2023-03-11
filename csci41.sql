DROP DATABASE IF EXISTS astigin;
CREATE DATABASE astigin;
USE astigin;
DROP TABLE IF EXISTS customer;
DROP TABLE IF EXISTS train_date;
DROP TABLE IF EXISTS train;
DROP TABLE IF EXISTS maintenance_work;
DROP TABLE IF EXISTS maintenance_crew;
DROP TABLE IF EXISTS ticket;
DROP TABLE IF EXISTS route;
DROP TABLE IF EXISTS inter_route;
DROP TABLE IF EXISTS nodes;
DROP TABLE IF EXISTS station;
DROP TABLE IF EXISTS station_routes;
DROP TABLE IF EXISTS train_system;
DROP TABLE IF EXISTS trip;
DROP TABLE IF EXISTS ticket_trip;

CREATE TABLE customer (
  customer_id INT NOT NULL PRIMARY KEY,
  last_name VARCHAR(255) NOT NULL,
  first_name VARCHAR(255) NOT NULL,
  middle_initial VARCHAR(5) NOT NULL,
  birth_date DATE NOT NULL,
  gender VARCHAR(100) DEFAULT 'Prefer Not to Say',
  CHECK
  (gender IN ('Male', 'Female', 'Prefer Not to Say'))
);

CREATE TABLE train_date (
  date_id INT NOT NULL PRIMARY KEY,
  trip_sched DATE NOT NULL
);

CREATE TABLE train (
  train_id INT NOT NULL PRIMARY KEY,
  train_model VARCHAR(255),
  train_maxspeed INT NOT NULL DEFAULT 0,
  no_of_seats INT NOT NULL DEFAULT 1,
  no_of_toilets INT DEFAULT 0,
  reclining_seats BOOL DEFAULT FALSE,
  luggage_storage BOOL DEFAULT FALSE,
  folding_tables BOOL DEFAULT FALSE,
  vending_machines BOOL DEFAULT FALSE,
  disability_access BOOL DEFAULT FALSE,
  food_service BOOL DEFAULT FALSE,
  date_id INT,
  FOREIGN KEY (date_id) REFERENCES train_date(date_id)
);
CREATE TABLE maintenance_work (
  maintenance_id INT NOT NULL PRIMARY KEY,
  date_maintained DATE,
  maintenance_condition VARCHAR(255) DEFAULT 'Poor',
  train_id INT,
  FOREIGN KEY (train_id) REFERENCES train(train_id),
  CHECK
  (maintenance_condition IN ('Poor', 'Good', 'Very Good', 'Excellent'))

);

CREATE TABLE maintenance_crew (
  crew_id INT NOT NULL PRIMARY KEY,
  crew_rep VARCHAR(255) DEFAULT 'None',
  task VARCHAR(255) DEFAULT 'None',
  maintenance_id INT,
  FOREIGN KEY (maintenance_id) REFERENCES maintenance_work(maintenance_id)
);
CREATE TABLE ticket (
  ticket_no INT NOT NULL PRIMARY KEY,
  date_purchased DATE NOT NULL,
  ticket_cost INT NOT NULL,
  customer_id INT,
  FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
);
CREATE TABLE route (
  route_id INT NOT NULL PRIMARY KEY,
  route_start VARCHAR (30),
  route_end VARCHAR (30),
  route_cost INT NOT NULL CHECK(route_cost >= 0),
  route_duration VARCHAR (30) NOT NULL,
  route_type VARCHAR (10) NOT NULL, 
  one_way BOOL DEFAULT FALSE,
  CHECK
  (route_type IN ('inter', 'local'))
);


CREATE TABLE nodes (
   node_ID INT NOT NULL PRIMARY KEY,
   connected_station_ID_1 INT,
   connected_station_1_duration INT CHECK (connected_station_1_duration >= 0),
   connected_station_ID_2 INT,
   connected_station_2_duration INT CHECK (connected_station_2_duration >= 0)
 );

CREATE TABLE station (
    station_ID INT NOT NULL PRIMARY KEY,
    station_name VARCHAR(100),
    train_system VARCHAR(30),
    one_way BOOL DEFAULT FALSE,
    node_ID INT,
    FOREIGN KEY (node_ID) REFERENCES nodes(node_ID)
);

CREATE TABLE station_routes (
  station_routes_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
   station_ID INT,
   route_id INT,
   FOREIGN KEY (station_ID) REFERENCES station(station_ID),
   FOREIGN KEY (route_ID) REFERENCES route(route_ID)
);

CREATE TABLE train_system (
  train_system_ID INT NOT NULL PRIMARY KEY,
  system_name VARCHAR(100),
  system_type VARCHAR(30), 
  train_system_cost INT CHECK (train_system_cost >= 0),
  CHECK (system_type IN ('Inter', 'Local'))
);


CREATE TABLE trip(
  trip_ID INT NOT NULL PRIMARY KEY,
  trip_origin VARCHAR(100),
  trip_destination VARCHAR(100),
  trip_departure DATETIME NOT NULL,
  trip_arrival DATETIME NOT NULL,
  trip_duration VARCHAR(30) NOT NULL,
  trip_cost INT NOT NULL CHECK(trip_cost >= 2),
  trip_date_id INT,
  FOREIGN KEY (trip_date_id) REFERENCES train_date(date_id)
);

CREATE TABLE ticket_trip (
  ticket_trip_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  ticket_no INT,
  FOREIGN KEY (ticket_no) REFERENCES ticket(ticket_no),
  trip_id INT,
  FOREIGN KEY (trip_id) REFERENCES trip(trip_ID)
);

CREATE TABLE trip_train_system(
  train_trip_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  trip_ID INT,
  train_system_ID INT,
  FOREIGN KEY(train_system_ID) REFERENCES train_system(train_system_ID),
  FOREIGN KEY (trip_ID) REFERENCES trip(trip_ID)
);


--
-- customers
INSERT INTO customer(customer_id, last_name, first_name,  middle_initial, birth_date, gender)
VALUES
(1001, 'Tohsaka', 'Rin', 'G', '2000-02-03', 'Female'),
(1002, 'Bright', 'Estelle', 'A', '2000-08-07', 'Female'),
(1003, 'Emiya', 'Shirou', 'B', '2000-02-03', 'Male'),
(1004, 'Soryu', 'Asuka', 'C', '2001-12-04', 'Female'),
(1005, 'Shinomiya', 'Kaguya', 'D', '2000-01-01', 'Female'),
(1006, 'Shirogane', 'Miyuki', 'Q', '2000-09-09', 'Male'),
(1007, 'Fujiwara', 'Chika', 'S', '2000-03-03', 'Female'),
(1008, 'Ishigami', 'Yu', 'G', '2001-03-03', 'Male'),
(1009, 'Iino', 'Miko', 'I', '2000-05-05', 'Female'),
(1010, 'Hayasaka', 'Ai', 'G', '1999-04-02', 'Female'),
(1011, 'Shijo', 'Maki', 'L', '2000-01-01', 'Female'),
(1012, 'Monkey', 'Luffy', 'D', '1998-05-05', 'Male'),
(1013, 'Roronoa', 'Zoro', 'D', '1996-11-11', 'Male'),
(1014, 'Tony Tony', 'Chopper', 'D', '2000-12-24', 'Male'),
(1015, 'Nico', 'Robin', 'D', '1987-02-06', 'Female'),
(1016, 'Nefertari', 'Vivi', 'D', '1999-02-02', 'Female'),
(1017, 'Ronaldo', 'Cristiano', 'D', '1985-02-05', 'Male'),
(1018, 'Messi', 'Lionel', 'P', '1987-06-24', 'Male'),
(1019, 'Santos', 'Neymar', 'D', '1992-02-05', 'Male'),
(1020, 'Modric', 'Luka', 'A', '1985-09-09', 'Male');

INSERT INTO train_date(date_id, trip_sched)
VALUES
(0207, '2022-02-07'),
(0208, '2022-02-08'),
(0209, '2022-05-05'),
(0210, '2022-06-06'),
(0211, '2022-06-10');

-- trains
INSERT INTO train(train_id, train_model, train_maxspeed, no_of_seats, no_of_toilets, reclining_seats, luggage_storage, folding_tables, vending_machines, disability_access, food_service, date_id)
VALUES
(201, 'A-102', 100, 150, 5, TRUE, FALSE, TRUE, FALSE, TRUE, FALSE, 0207),
(202, 'B-540', 120, 130, 5, TRUE, TRUE , TRUE, FALSE, FALSE, TRUE, 0207),
(203, 'C-321', 130, 110, 4, TRUE, TRUE, TRUE, TRUE, FALSE, TRUE, 0207),
(204, 'D-231', 90, 100, 6, TRUE, TRUE, FALSE, FALSE, TRUE, TRUE, 0207),
(205, 'E-120', 95, 100, 5, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, 0207),
(206, 'F-213', 90, 100, 5, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, 0208),
(207, 'G-292', 95, 100 , 8, TRUE, TRUE, TRUE, FALSE, FALSE, TRUE, 0208),
(208, 'H-112', 115, 100, 10, FALSE, FALSE, FALSE, TRUE, FALSE, TRUE, 0208),
(209, 'I-112', 125, 95, 15, FALSE, TRUE, FALSE, TRUE, FALSE, TRUE, 0208),
(210, 'J-912', 120, 100, 20, FALSE, FALSE, FALSE, TRUE, TRUE, FALSE, 0208);

 -- maintenance
INSERT INTO maintenance_work(maintenance_id, date_maintained, maintenance_condition, train_id)
VALUES (901, '2022-04-04', 'Good', 201),
(902, '2022-10-02', 'Poor', 202),
(903, '2022-09-02', 'Very Good', 203),
(904, '2022-03-02', 'Excellent', 204),
(905, '2022-04-05', 'Poor', 205),
(906, '2021-12-12', 'Poor', 206),
(907, '2022-02-01', 'Good', 207),
(908, '2022-01-02', 'Excellent', 208),
(909, '2022-02-02', 'Excellent', 209);

-- crew
INSERT INTO maintenance_crew(crew_id, crew_rep, task, maintenance_id)
VALUES 
(601, 'Winry Rockbell', 'Oil Change', 909),
(602, 'Simone Celestial', 'Cleaning',902),
(603, 'Zero Two', 'Cooking', 903),
(604, 'Santai Cruz', 'Replacement of brake discs', 904),
(605, 'Poppa Uppa', 'Complete oil change', 905);

-- tickets
INSERT INTO ticket(ticket_no, date_purchased, ticket_cost, customer_id)
VALUES 
(001, '2022-02-07', 10, 1001),
(002, '2022-02-06', 6, 1003),
(003, '2022-01-04', 6, 1004),
(004, '2022-04-06', 6, 1005),
(005,'2022-05-04', 10, 1010);

INSERT INTO nodes (node_ID, connected_station_ID_1, connected_station_1_duration, connected_station_ID_2, connected_station_2_duration)
VALUES
    (001, 502, 5, null, null),
    (002, 503, 5, null, null),
    (003, 504, 5, null, null),
    (004,  401, 5, null, null),
    (005, 504, 10, 402, 10),
    (006, 401, 20, 403, 20),
    (007, 402, 20, 404, 20),
    (008, 403, 20, 405, 20),
    (009, 404, 30, 406, 30),
    (010, 405, 30, 407, 30),
    (011, 406, 40, 408, 40),
    (012, 407, 20, 409, 30),
    (013, 408, 20, 410, 20),
    (014, 409, 20, 504, 40);
    

INSERT INTO train_system (train_system_ID, system_name, system_type, train_system_cost)
  VALUES
  (2001, 'Taguig', 'Local', 2),
  (3001, 'Luzon', 'Inter', null);

INSERT INTO station (station_ID, station_name, train_system, one_way, node_ID)
   VALUES
   (501, 'Katipunan', 'Taguig', TRUE, 001),
   (502, 'Allies Enclave', 'Taguig', TRUE, 002),
   (503, 'The Wardorbe', 'Taguig', TRUE, 003),
   (504, 'The Lamp Post','Taguig', TRUE, 004),
   (401, 'Mr Tumms', 'Luzon', FALSE, 005),
   (402, 'The Stone Table', 'Luzon', FALSE, 006),
   (403, 'Dancing Lawn', 'Luzon', FALSE, 007),
   (404, 'Anvard', 'Luzon', FALSE, 008),
   (405, 'Cherry Tree', 'Luzon', FALSE, 009),
   (406, 'Father Christmas', 'Luzon', FALSE, 010),
   (407, 'Cauldron Pool', 'Luzon', FALSE, 011),
   (408, 'Asian Camp', 'Luzon', FALSE, 012),
   (409, 'Witch Camp', 'Luzon', FALSE, 013),
   (410, 'Antipolo', 'Luzon', FALSE, 014);

   INSERT INTO route (route_id, route_start, route_end, route_cost, route_duration, route_type, one_way)
   VALUES
   (2001, 501, 502, 6, '2 hr 04 mins','Local', FALSE),
   (2002, 503, 504, 6, '2 hr 20 mins','Local', FALSE),
   (3001, 401, 402, 10, '3 hr 05 mins','Inter', FALSE),
   (3002, 402, 403, 15, '4 hr 05 mins','Inter', FALSE),
   (3003, 406, 410, 25, '4 hr 44 mins','Inter', TRUE),
   (3004, 405, 408, 15, '3 hr 21 mins','Inter', FALSE),
   (3005, 406, 408, 10, '3 hr 54 mins','Inter', TRUE);

INSERT INTO station_routes(station_id, route_id)
VALUES
  (501, 2001),
  (502, 2001),
  (503, 2002),
  (401, 3001),
  (402, 3001);

INSERT INTO trip(trip_ID, trip_origin, trip_destination, trip_departure, trip_arrival, trip_duration, trip_cost, trip_date_id)
	VALUES
    (5001, 'Katipunan', 'Allies Enclave', '2022-02-07 12:00:00','2022-02-07 15:05:00', '3:05:00', 10, 0207 ),
    (5002, 'The Wardorbe', 'The Lamp Post', '2022-02-08 14:00:00', '2022-02-08 16:20:00','2:20:00',6,0208),
    (5003, 'Mr Tumms', 'The Stone Table', '2022-05-05 04:00:00','2022-05-05 08:25:00','4:25:00',25,0209),
    (5004, 'The Stone Table', 'Dancing Lawn', '2022-06-06 15:00:00','2022-06-06 18:21:00','3:21:00',15,0210),
    (5005, 'Father Christmas', 'Antipolo', '2022-06-10 5:00:00','2022-06-10 10:25:00','5:25:00',20,0211);

INSERT INTO ticket_trip(ticket_no, trip_id)
VALUES
  (001, 5001),
  (002, 5002),
  (003, 5002),
  (004, 5002),
  (005, 5001);

INSERT INTO trip_train_system(trip_ID, train_system_ID)
VALUES
  (5001, 2001),
  (5002, 2001),
  (5003, 3001),
  (5004, 3001),
  (5005, 3001);
