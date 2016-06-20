# Создание базы данных RecycleEasily в MySQL.

CREATE DATABASE recycle_easily;

USE recycle_easily;

CREATE TABLE `stations` (
	`ID` INT NOT NULL,
	`name` char(30) NOT NULL,
	`street_id` INT NOT NULL,
	`house` smallint NOT NULL,
	`building` smallint,
	`type_id` INT NOT NULL,
	`raiting` smallint,
	`position_x` FLOAT,
	`position_y` FLOAT,
	`add_date` DATE NOT NULL,
	`update_date` DATE NOT NULL,
	`description` TEXT(200),
	PRIMARY KEY (`ID`)
);

CREATE TABLE `cities` (
	`ID` INT NOT NULL,
	`name` char(30) NOT NULL UNIQUE,
	PRIMARY KEY (`ID`)
);

CREATE TABLE `streets` (
	`ID` INT NOT NULL,
	`city_id` INT(100) NOT NULL UNIQUE,
	`name` char(100) NOT NULL,
	PRIMARY KEY (`ID`)
);

CREATE TABLE `trash_types` (
	`ID` INT NOT NULL,
	`name` char(30) NOT NULL UNIQUE,
	`description` TEXT(200) NOT NULL,
	PRIMARY KEY (`ID`)
);

CREATE TABLE `station-examples` (
	`trash_id` INT NOT NULL,
	`station_id` INT NOT NULL,
	PRIMARY KEY (`trash_id`,`station_id`)
);

CREATE TABLE `station_types` (
	`ID` INT NOT NULL,
	`name` char(30) NOT NULL,
	`description` TEXT(200) NOT NULL,
	PRIMARY KEY (`ID`)
);

CREATE TABLE `trash_classes` (
	`ID` INT NOT NULL,
	`name` char(30) NOT NULL,
	`description` TEXT(200) NOT NULL,
	PRIMARY KEY (`ID`)
);

CREATE TABLE `trash_examples` (
	`ID` INT NOT NULL,
	`name` char(30) NOT NULL,
	`type_id` INT NOT NULL,
	`class_id` INT NOT NULL,
	PRIMARY KEY (`ID`)
);

CREATE TABLE `users` (
	`ID` INT NOT NULL,
	`login` char(30) NOT NULL UNIQUE,
	`password` bigint NOT NULL UNIQUE,
	`reg_date` DATE NOT NULL,
	`raiting` INT NOT NULL,
	PRIMARY KEY (`ID`)
);

CREATE TABLE `users-examples` (
	`trash_id` INT NOT NULL,
	`user_id` INT NOT NULL,
	PRIMARY KEY (`trash_id`,`user_id`)
);

CREATE TABLE `vk_users` (
	`ID` INT NOT NULL,
	`address` char(50) NOT NULL UNIQUE,
	PRIMARY KEY (`ID`)
);

CREATE TABLE `user-socialnet` (
	`user_id` INT NOT NULL,
	`vk_id` INT NOT NULL,
	`facebook_id` INT NOT NULL,
	PRIMARY KEY (`user_id`)
);

CREATE TABLE `facebook_users` (
	`ID` INT NOT NULL,
	`address` char(50) NOT NULL UNIQUE,
	PRIMARY KEY (`ID`)
);

ALTER TABLE `stations` ADD CONSTRAINT `stations_fk0` FOREIGN KEY (`street_id`) REFERENCES `streets`(`ID`);

ALTER TABLE `stations` ADD CONSTRAINT `stations_fk1` FOREIGN KEY (`type_id`) REFERENCES `station_types`(`ID`);

ALTER TABLE `streets` ADD CONSTRAINT `streets_fk0` FOREIGN KEY (`city_id`) REFERENCES `cities`(`ID`);

ALTER TABLE `station-examples` ADD CONSTRAINT `station-examples_fk0` FOREIGN KEY (`trash_id`) REFERENCES `stations`(`ID`);

ALTER TABLE `station-examples` ADD CONSTRAINT `station-examples_fk1` FOREIGN KEY (`station_id`) REFERENCES `trash_examples`(`ID`);

ALTER TABLE `trash_examples` ADD CONSTRAINT `trash_examples_fk0` FOREIGN KEY (`type_id`) REFERENCES `trash_types`(`ID`);

ALTER TABLE `trash_examples` ADD CONSTRAINT `trash_examples_fk1` FOREIGN KEY (`class_id`) REFERENCES `trash_classes`(`ID`);

ALTER TABLE `users-examples` ADD CONSTRAINT `users-examples_fk0` FOREIGN KEY (`trash_id`) REFERENCES `trash_examples`(`ID`);

ALTER TABLE `users-examples` ADD CONSTRAINT `users-examples_fk1` FOREIGN KEY (`user_id`) REFERENCES `users`(`ID`);

ALTER TABLE `user-socialnet` ADD CONSTRAINT `user-socialnet_fk0` FOREIGN KEY (`user_id`) REFERENCES `users`(`ID`);

ALTER TABLE `user-socialnet` ADD CONSTRAINT `user-socialnet_fk1` FOREIGN KEY (`vk_id`) REFERENCES `vk_users`(`ID`);

ALTER TABLE `user-socialnet` ADD CONSTRAINT `user-socialnet_fk2` FOREIGN KEY (`facebook_id`) REFERENCES `facebook_users`(`ID`);

