create database cforge_package_manager;

create table packages_list (
	id BIGSERIAL PRIMARY KEY,
	name varchar(255) unique,
	version varchar(255),
	dependencies bigint[],
	maintainer varchar(255),
	description text,
	server_name varchar(255),
	downloads bigint
)
