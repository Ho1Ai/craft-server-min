create database craft_package_manager_minimal;

create table packages_list (
	id BIGSERIAL PRIMARY KEY,
	name varchar(255) unique not null,
	version varchar(255),
	dependencies bigint[],
	maintainer varchar(255),
	pkg_server_path TEXT,
	repo_url TEXT,
	downloads bigint default 0
);
