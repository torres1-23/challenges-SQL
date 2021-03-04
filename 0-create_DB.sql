-- Creates a database and tables.
CREATE DATABASE
    IF NOT EXISTS boli_assurance;
USE boli_assurance;
CREATE TABLE
    IF NOT EXISTS boli_assurance.employee(
        id_employee INT PRIMARY KEY,
        first_name VARCHAR(256) NOT NULL,
        last_name VARCHAR(256) NOT NULL,
        department VARCHAR(50) NOT NULL
    );
CREATE TABLE
    IF NOT EXISTS boli_assurance.client(
        id_client INT NOT NULL PRIMARY KEY,
        first_name VARCHAR(256) NOT NULL,
        last_name VARCHAR(256) NOT NULL,
        phone INT,
        email VARCHAR(256)
    );
CREATE TABLE
    IF NOT EXISTS boli_assurance.vehicle(
        id_plate INT PRIMARY KEY,
        value INT NOT NULL,
        date_assurance TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        time_asssurance INT NOT NULL,
        is_assured BIT(1),
        id_employee INT NOT NULL,
        id_client INT NOT NULL,
        FOREIGN KEY(id_employee)
            REFERENCES boli_assurance.employee(id_employee),
        FOREIGN KEY(id_client)
            REFERENCES boli_assurance.client(id_client)
    );
