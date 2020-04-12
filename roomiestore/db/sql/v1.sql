--- Setting up tables and relationships

-- *************** SqlDBM: PostgreSQL ****************;
-- ***************************************************;

SET search_path TO public;

CREATE DATABASE IF NOT EXISTS roomiestore;

-- ************************************** "user"

CREATE TABLE IF NOT EXISTS "user"
(
 "user_id"      bigserial NOT NULL,
 "fname"        varchar(50) NOT NULL,
 "lname"        varchar(50) NOT NULL,
 "dob"          date NOT NULL,
 "username"     varchar(50) NOT NULL,
 "password"     text NOT NULL,
 "role_id"      smallint NOT NULL,
 "last_updated" date NOT NULL,
 CONSTRAINT "PK_user" PRIMARY KEY ( "user_id" ),
 CONSTRAINT "FK_50" FOREIGN KEY ( "role_id" ) REFERENCES "roles" ( "role_id" )
);

CREATE INDEX "fkIdx_50" ON "user"
(
 "role_id"
);

CREATE INDEX "idx_fname" ON "user"
(
 "fname"
);

CREATE INDEX "idx_lname" ON "user"
(
 "lname"
);

CREATE INDEX "idx_username" ON "user"
(
 "lname"
);

-- ************************************** "user_bills"

CREATE TABLE "user_bills"
(
 "bill_id" bigint NOT NULL,
 "user_id" bigint NOT NULL,
 CONSTRAINT "FK_63" FOREIGN KEY ( "bill_id" ) REFERENCES "bill" ( "bill_id" ),
 CONSTRAINT "FK_66" FOREIGN KEY ( "user_id" ) REFERENCES "user" ( "user_id" )
);

CREATE INDEX "fkIdx_63" ON "user_bills"
(
 "bill_id"
);

CREATE INDEX "fkIdx_66" ON "user_bills"
(
 "user_id"
);


-- ************************************** "user_items"

CREATE TABLE "user_items"
(
 "user_id" bigint NOT NULL,
 "item_id" bigint NOT NULL,
 CONSTRAINT "FK_37" FOREIGN KEY ( "user_id" ) REFERENCES "user" ( "user_id" ),
 CONSTRAINT "FK_43" FOREIGN KEY ( "item_id" ) REFERENCES "item" ( "item_id" )
);

CREATE INDEX "fkIdx_37" ON "user_items"
(
 "user_id"
);

CREATE INDEX "fkIdx_43" ON "user_items"
(
 "item_id"
);



-- ************************************** "bill"

CREATE TABLE "bill"
(
 "bill_id"      bigserial NOT NULL,
 "due_date"     date NOT NULL,
 "last_updated" date NOT NULL,
 CONSTRAINT "PK_bill" PRIMARY KEY ( "bill_id" )
);

-- ************************************** "item"

CREATE TABLE "item"
(
 "item_id"            bigserial NOT NULL,
 "item_type_id"       bigint NOT NULL,
 "name"               varchar(50) NOT NULL,
 "alcohol_percentage" decimal(2,1) NOT NULL,
 "count"              bigint NOT NULL,
 "pic"                bytea NULL,
 "date_purchased"     date NOT NULL,
 "last_updated"       date NOT NULL,
 "price"              decimal(2,1) NOT NULL,
 CONSTRAINT "PK_item" PRIMARY KEY ( "item_id" ),
 CONSTRAINT "FK_17" FOREIGN KEY ( "item_type_id" ) REFERENCES "item_type" ( "item_type_id" )
);

CREATE INDEX "fkIdx_17" ON "item"
(
 "item_type_id"
);

CREATE INDEX "name_idx" ON "item"
(
 "name"
);

CREATE INDEX "alcohol_percentage_idx" ON "item"
(
 "alcohol_percentage"
);

-- ************************************** "item_type"

CREATE TABLE "item_type"
(
 "item_type_id" bigserial NOT NULL,
 "name"         varchar(50) NOT NULL,
 "last_updated" date NOT NULL,
 CONSTRAINT "PK_item_type" PRIMARY KEY ( "item_type_id" )
);

CREATE INDEX "name_idx" ON "item_type"
(
 "name"
);

-- ************************************** "prices"

CREATE TABLE "prices"
(
 "price_id" bigserial NOT NULL,
 "price"    decimal(2,1) NOT NULL,
 "created"  date NOT NULL,
 "item_id"  bigint NOT NULL,
 CONSTRAINT "PK_prices" PRIMARY KEY ( "price_id" ),
 CONSTRAINT "FK_78" FOREIGN KEY ( "item_id" ) REFERENCES "item" ( "item_id" )
);

CREATE INDEX "fkIdx_78" ON "prices"
(
 "item_id"
);

-- ************************************** "roles"

CREATE TABLE "roles"
(
 "role_id" smallserial NOT NULL,
 "name"    varchar(50) NOT NULL,
 CONSTRAINT "PK_roles" PRIMARY KEY ( "role_id" )
);

CREATE INDEX "name_id" ON "roles"
(
 "name"
);


































