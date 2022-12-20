DROP TABLE sessions;
DROP TABLE members;
DROP TABLE gym_classes;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255)
);

CREATE TABLE gym_classes (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    time VARCHAR (255),
    capacity INT,
    duration INT 
);

CREATE TABLE sessions (
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    gym_class_id INT NOT NULL REFERENCES gym_classes(id) ON DELETE CASCADE
);


