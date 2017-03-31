CREATE TABLE user_profile (
    Username            varchar(100) NOT NULL,		   
    Password         	bytea NOT NULL, 
    Salt				char NOT NULL,  
    F_name        		varchar(100) NOT NULL,           
    L_name            	varchar(100) NOT NULL,    
	PRIMARY KEY (Username)
);
CREATE TABLE valid_extensions (
	Extension	varchar(100) NOT NULL,
	PRIMARY KEY (Extension)
);
CREATE TABLE user_login (
	User_id				bigserial,
   	 Username        	varchar(100) references user_profile(Username), 
   	 Login_date			timestamp,
	Login_ip 			cidr,
	PRIMARY KEY (User_id, Username)
);

CREATE TABLE video_metadata (
	Video_id			bigserial,
    	Framerate           real CHECK(Framerate > 0),
	frame_num_total		int CHECK(frame_num_total > 0),
	resolution			point,
	video_name			char NOT NULL,
	encoding			char NOT NULL,
	PRIMARY KEY (Video_id) 
);

CREATE TABLE openface (
	Video_id			bigserial references video_metadata(Video_id),
	Frame_num			int CHECK(frame_num > 0), 
	Leftpup				point,
	Rightpup			point,
	FT_Leftpup			point,
	FT_Rightpup			point,
	Yaw					real,
	Pitch				real, 
	Roll				real,
	Datapoint_1 		point,
	Datapoint_2         point,
	Datapoint_3         point,
	Datapoint_4         point,
	Datapoint_5         point,
	Datapoint_6         point,
	Datapoint_7         point,
	Datapoint_8         point,
	Datapoint_9         point,
	Datapoint_10        point,
	Datapoint_11        point,
	Datapoint_12        point,
	Datapoint_13        point,
	Datapoint_14        point,
	Datapoint_15        point,
	Datapoint_16        point,
	Datapoint_17        point,
	Datapoint_18        point,
	Datapoint_19        point,
	Datapoint_20        point,
	Datapoint_21        point,
	Datapoint_22        point,
	Datapoint_23        point,
	Datapoint_24        point,
	Datapoint_25        point,
	Datapoint_26        point,
	Datapoint_27        point,
	Datapoint_28        point,
	Datapoint_29        point,
	Datapoint_30        point,
	Datapoint_31        point,
	Datapoint_32        point,
	Datapoint_33        point,
	Datapoint_34        point,
	Datapoint_35        point,
	Datapoint_36        point,
	Datapoint_37        point,
	Datapoint_38        point,
	Datapoint_39        point,
	Datapoint_40       	point,
	Datapoint_41        point,
	Datapoint_42        point,
	Datapoint_43        point,
	Datapoint_44        point,
	Datapoint_45        point,
	Datapoint_46        point,
	Datapoint_47        point,
	Datapoint_48        point,
	Datapoint_49        point,
	Datapoint_50        point,
	Datapoint_51        point,
	Datapoint_52        point,
	Datapoint_53        point,
	Datapoint_54        point,
	Datapoint_55        point,
	Datapoint_56        point,
	Datapoint_57        point,
	Datapoint_58        point,
	Datapoint_59        point,
	Datapoint_60        point,
	Datapoint_61        point,
	Datapoint_62        point,
	Datapoint_63        point,
	Datapoint_64        point,
	Datapoint_65        point,
	Datapoint_66        point,
	Datapoint_67        point,
	Datapoint_68        point,
	PRIMARY KEY (Video_id, Frame_num)
);


