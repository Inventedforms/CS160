CREATE DATABASE cs160;
\c cs160
CREATE TABLE user_profile (
    Username            varchar(100) NOT NULL,		   
    Password         	bytea NOT NULL, 
    F_name        		varchar(100) NOT NULL,           
    L_name            	varchar(100) NOT NULL,    
	PRIMARY KEY (Username)
);
CREATE TABLE valid_extensions (
	Extension	varchar(100) NOT NULL,
	PRIMARY KEY (Extension)
);
CREATE TABLE user_login (
	Session_id				bigserial,
   	Username        	varchar(100) references user_profile(Username), 
   	Login_date			timestamp,
	Login_ip 			varchar(100),
	MAC_Address			varchar(100),
	PRIMARY KEY (Session_id, Username)
);
CREATE TABLE video_metadata (
	Video_id			bigserial,
    	Framerate           real CHECK(Framerate > 0),
	frame_num_total		int CHECK(frame_num_total > 0),
	resolution			point,
	video_name			varchar[100] NOT NULL,
	encoding			varchar[100] NOT NULL,
	PRIMARY KEY (Video_id) 
);