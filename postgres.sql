create table postgres.public.users(
user_id int primary key,
email text,
username text,
password_hash text,
firstname text,
lastname text,
bio text,
profile_pic text
);

select * from postgres.public.users;

create table postgres.public.posts (
post_id int primary key,
link text,
img text,
title text,
description text,
score real,
user_id int,
constraint fk_user foreign key(user_id) references postgres.public.users(user_id)
);

select * from postgres.public.posts;

create table comments(
comment_id int primary key,
user_id int,
post_id int,
comment_text text,
comment_time timestamp,
constraint fk_user foreign key(user_id) references postgres.public.users(user_id),
constraint fk_post foreign key(post_id) references postgres.public.posts(post_id)
);

select * from postgres.public.comments;

create table followers(
user_main int,
user_follower int,
constraint fk_user_main foreign key(user_main) references postgres.public.users(user_id),
constraint fk_user_follower foreign key(user_follower) references postgres.public.users(user_id)
);

select * from followers;

--drop table users;
--drop table followers;
--drop table posts;
--drop table comments;

select * from posts;
select * from users;
select * from comments;
select * from followers;
