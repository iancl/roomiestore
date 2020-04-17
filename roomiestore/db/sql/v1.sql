-- *************** SqlDBM: PostgreSQL ****************;
-- ***************************************************;


-- ************************************** "role"

CREATE TABLE "role"
(
 "role_id"     smallserial NOT NULL,
 "name"        varchar(50) NOT NULL,
 "description" text NOT NULL,
 CONSTRAINT "PK_roles" PRIMARY KEY ( "role_id" )
);


-- ************************************** "user"

CREATE TABLE "user"
(
 "user_id"      bigserial NOT NULL,
 "fname"        varchar(50) NOT NULL,
 "lname"        varchar(50) NOT NULL,
 "dob"          date NOT NULL,
 "email"        text NOT NULL UNIQUE,
 "phone"        varchar(15) NULL,
 "username"     varchar(50) NOT NULL UNIQUE,
 "password"     varchar(128) NOT NULL,
 "date_created" date NOT NULL,
 "last_updated" date NOT NULL,
 "role_id"      smallint NOT NULL,
 CONSTRAINT "PK_user" PRIMARY KEY ( "user_id" ),
 CONSTRAINT "FK_262" FOREIGN KEY ( "role_id" ) REFERENCES "role" ( "role_id" )
);

CREATE INDEX "fkIdx_262" ON "user"
(
 "role_id"
);

CREATE INDEX "user_email_idx" ON "user"
(
 "email"
);

CREATE INDEX "user_username_idx" ON "user"
(
 "username"
);

-- ************************************** "order"

CREATE TABLE "order"
(
 "order_id"     serial NOT NULL,
 "date_created" date NOT NULL,
 "last_updated" date NOT NULL,
 "due_date"     date NOT NULL,
 "notes"        text NULL,
 "date_payed"   date NOT NULL,
 "user_id"      bigint NOT NULL,
 CONSTRAINT "PK_Order" PRIMARY KEY ( "order_id" ),
 CONSTRAINT "FK_268" FOREIGN KEY ( "user_id" ) REFERENCES "user" ( "user_id" )
);

CREATE INDEX "fkIdx_268" ON "order"
(
 "user_id"
);

-- ************************************** "country"

CREATE TABLE "country"
(
 "country_id" serial NOT NULL,
 "name"       text NOT NULL,
 CONSTRAINT "PK_country" PRIMARY KEY ( "country_id" )
);

-- ************************************** "type"

CREATE TABLE "type"
(
 "type_id"      bigserial NOT NULL,
 "name"         varchar(50) NOT NULL,
 "last_updated" date NOT NULL,
 CONSTRAINT "PK_item_type" PRIMARY KEY ( "type_id" )
);

-- ************************************** "item"

CREATE TABLE "item"
(
 "item_id"            bigserial NOT NULL,
 "name"               varchar(50) NOT NULL,
 "alcohol_percentage" decimal(2,1) NOT NULL,
 "count"              bigint NOT NULL,
 "date_purchased"     date NOT NULL,
 "last_updated"       date NOT NULL,
 "price"              decimal(2,1) NOT NULL,
 "likes"              bigint NOT NULL,
 "description"        text NOT NULL,
 "country_id"         integer NOT NULL,
 "type_id"            bigint NOT NULL,
 CONSTRAINT "PK_item" PRIMARY KEY ( "item_id" ),
 CONSTRAINT "FK_217" FOREIGN KEY ( "country_id" ) REFERENCES "country" ( "country_id" ),
 CONSTRAINT "FK_280" FOREIGN KEY ( "type_id" ) REFERENCES "type" ( "type_id" )
);

CREATE INDEX "fkIdx_217" ON "item"
(
 "country_id"
);

CREATE INDEX "fkIdx_280" ON "item"
(
 "type_id"
);

CREATE INDEX "item_name_idx" ON "item"
(
 "name"
);

CREATE INDEX "item_likes_idx" ON "item"
(
 "likes"
);

-- ************************************** "order_items"

CREATE TABLE "order_items"
(
 "order_id" integer NOT NULL,
 "item_id"  bigint NOT NULL,
 CONSTRAINT "FK_240" FOREIGN KEY ( "order_id" ) REFERENCES "order" ( "order_id" ),
 CONSTRAINT "FK_243" FOREIGN KEY ( "item_id" ) REFERENCES "item" ( "item_id" )
);

CREATE INDEX "fkIdx_240" ON "order_items"
(
 "order_id"
);

CREATE INDEX "fkIdx_243" ON "order_items"
(
 "item_id"
);

-- ************************************** "tag"

CREATE TABLE "tag"
(
 "tag_id" serial NOT NULL,
 "name"   text NOT NULL,
 "notes"  text NOT NULL,
 CONSTRAINT "PK_tag" PRIMARY KEY ( "tag_id" )
);

CREATE INDEX "tag_name_idx" ON "tag"
(
 "name"
);

-- ************************************** "item_tags"

CREATE TABLE "item_tags"
(
 "date_created" date NOT NULL,
 "tag_id"       integer NOT NULL,
 "item_id"      bigint NOT NULL,
 CONSTRAINT "FK_224" FOREIGN KEY ( "tag_id" ) REFERENCES "tag" ( "tag_id" ),
 CONSTRAINT "FK_227" FOREIGN KEY ( "item_id" ) REFERENCES "item" ( "item_id" )
);

CREATE INDEX "fkIdx_224" ON "item_tags"
(
 "tag_id"
);

CREATE INDEX "fkIdx_227" ON "item_tags"
(
 "item_id"
);

-- ************************************** "picture"
-- can either be bytea or the url to a cdn

CREATE TABLE "picture"
(
 "picture_id"   serial NOT NULL,
 "url"          text NULL,
 "last_updated" date NOT NULL,
 "data"         bytea NULL,
 "item_id"      bigint NOT NULL,
 CONSTRAINT "PK_picture" PRIMARY KEY ( "picture_id" ),
 CONSTRAINT "FK_274" FOREIGN KEY ( "item_id" ) REFERENCES "item" ( "item_id" )
);

CREATE INDEX "fkIdx_274" ON "picture"
(
 "item_id"
);

-- ************************************** "container"

CREATE TABLE "container"
(
 "container_id" serial NOT NULL,
 "name"         text NOT NULL,
 "notes"        text NOT NULL,
 "milliliters"  int NOT NULL,
 CONSTRAINT "PK_container" PRIMARY KEY ( "container_id" )
);

-- ************************************** "item_containers"

CREATE TABLE "item_containers"
(
 "item_id"      bigint NOT NULL,
 "container_id" integer NOT NULL,
 CONSTRAINT "FK_127" FOREIGN KEY ( "item_id" ) REFERENCES "item" ( "item_id" ),
 CONSTRAINT "FK_285" FOREIGN KEY ( "container_id" ) REFERENCES "container" ( "container_id" )
);

CREATE INDEX "fkIdx_127" ON "item_containers"
(
 "item_id"
);

CREATE INDEX "fkIdx_285" ON "item_containers"
(
 "container_id"
);

-- ************************************** "price"
-- price should be on it's own db or it can be a single table with no relationship
-- a price will be created for an item
-- each time an item is purchased, we will look for the price that was created last and use
-- it for that item. So that every time an item is purchased, the latest price is used

CREATE TABLE "price"
(
 "price"   decimal(2,1) NOT NULL,
 "created" date NOT NULL,
 "item_id" bigint NOT NULL,
 CONSTRAINT "FK_288" FOREIGN KEY ( "item_id" ) REFERENCES "item" ( "item_id" ),
 CONSTRAINT "PK_item_id" PRIMARY KEY ( "item_id" )
);

CREATE INDEX "fkIdx_288" ON "price"
(
 "item_id"
);
