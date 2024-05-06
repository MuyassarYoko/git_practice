'''
CREATE TABLE IF NOT EXISTS employees(
	id SERIAL PRIMARY KEY,
	name VARCHAR(50),
	age INT,
	position VARCHAR(50)
);

-- INSERT INTO employees(name, age, position)
-- VALUES
-- ('Kiko', 19, 'admin'),
-- ('Micle', 22, 'director'),
-- ('Filip', 28, 'teacher'),
-- ('Delart', 16, 'shop assistant');

SELECT * FROM employees;

-- 5 --
CREATE TABLE IF NOT EXISTS departments(
	id SERIAL PRIMARY KEY,
 	name VARCHAR(50),
	location VARCHAR(30)
);

-- INSERT INTO departments(name, location)
-- VALUES
-- ('Kiko', 'Moscow'),
-- ('Micle', 'USA'),
-- ('Filip', 'Germany'),
-- ('Delart', 'Berlin');

-- ALTER TABLE employees
-- ADD COLUMN department_id SMALLINT,
-- ADD CONSTRAINT fk_department FOREIGN KEY (department_id) REFERENCES departments(id);

-- INSERT INTO employees(name, age, position, department_id)
-- VALUES
-- ('Kiko', 19, 'admin', 1),
-- ('Micle', 22, 'director', 4),
-- ('Filip', 28, 'teacher', 3),
-- ('Delart', 16, 'shop assistant', 3);

SELECT e.name, d.name FROM employees e
JOIN departments d ON e.department_id = d.id;

-- 9 --
CREATE TABLE IF NOT EXISTS projects(
	id SERIAL PRIMARY KEY,
	name VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS employee_project(
	id SERIAL PRIMARY KEY,
	employee_id INT, project_id INT,
	FOREIGN KEY (employee_id) REFERENCES employees(id),
	FOREIGN KEY (project_id) REFERENCES projects(id)
);
-- INSERT INTO projects(name)
-- VALUES
-- ('Html'),
-- ('Python'),
-- ('Css'),
-- ('Django'),
-- ('Java Script');

-- INSERT INTO employee_project(employee_id, project_id)
-- VALUES
-- (1, 3),
-- (3, 4),
-- (2, 2),
-- (4, 1);

SELECT e.name, p.name FROM  employee_project e_p
JOIN employees e ON e_p.employee_id = e.idJOIN projects p ON e_p.project_id = p.id;

-- 13 --

SELECT AVG(age) from employees;

-- 14 --

-- ALTER TABLE departments
-- ADD COLUMN employee_id SMALLINT,
-- ADD CONSTRAINT fk_employee FOREIGN KEY (employee_id)
-- REFERENCES employees(id);

-- INSERT INTO departments(name, location, employee_id)
-- VALUES
-- ('Kiko', 'Moscow', 1),
-- ('Micle', 'USA', 4),
-- ('Filip', 'Germany', 1),
-- ('Delart', 'Berlin', 4),
-- ('Honor', 'Frence', 4);

SELECT d.name, COUNT(e) FROM departments dJOIN employees e ON d.employee_id = e.id
GROUP BY(d.name);

-- 15 --
SELECT d.name, COUNT(employee_id) FROM departments d
GROUP BY d.name
ORDER BY(COUNT(employee_id));

-- 16 --
SELECT e.name, p.name FROM  employee_project e_projectJOIN employees e ON e_project.employee_id = e.id
JOIN projects p ON e_project.project_id = p.id;

-- 17 --
SELECT e.name, p.name FROM  employee_project e_project
JOIN employees e ON e_project.employee_id = e.idRIGHT JOIN projects p ON e_project.project_id = p.id;

-- 18 --
CREATE INDEX name_ind ON employees(name);

-- 19 --
CREATE OR REPLACE FUNCTION add_data() RETURNS TRIGGER AS
$$
BEGIN
	UPDATE employees
	SET employees.data = DATE()
	FROM employees ;
	RETURN NEW;
END;
$$
LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER data_tr
AFTER INSERT ON employees
FOR EACH ROW
EXECUTE PROCEDURE add_data();

-- INSERT INTO employees(name, age, position)
-- VALUES
-- ('Jimmy', 16, 'teacher');

SELECT * FROM employees;

-- 20 --

CREATE OR REPLACE FUNCTION updated() RETURNS TRIGGER AS
$$
BEGIN
	UPDATE employees
	SET last_updated = NOW()
	WHERE id = NEW.id;
	RETURN NEW;
END;
$$
LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER updated_tr
AFTER UPDATE ON employees
FOR EACH ROW
EXECUTE PROCEDURE updated();
'''