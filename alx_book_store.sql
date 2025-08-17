-- alx_book_store_postgres.sql
-- Minimal, COPY-PASTE friendly PostgreSQL DDL for the alx_book_store schema

CREATE SCHEMA IF NOT EXISTS alx_book_store;
SET search_path TO alx_book_store, public;

CREATE TABLE IF NOT EXISTS authors (
  author_id SERIAL PRIMARY KEY,
  author_name VARCHAR(215) NOT NULL
);

CREATE TABLE IF NOT EXISTS books (
  book_id SERIAL PRIMARY KEY,
  title VARCHAR(130) NOT NULL,
  author_id INT NOT NULL REFERENCES authors(author_id),
  price DOUBLE PRECISION NOT NULL,
  publication_date DATE
);

CREATE TABLE IF NOT EXISTS customers (
  customer_id SERIAL PRIMARY KEY,
  customer_name VARCHAR(215) NOT NULL,
  email VARCHAR(215) NOT NULL UNIQUE,
  address TEXT
);

CREATE TABLE IF NOT EXISTS orders (
  order_id SERIAL PRIMARY KEY,
  customer_id INT NOT NULL REFERENCES customers(customer_id),
  order_date DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS order_details (
  orderdetailid SERIAL PRIMARY KEY,
  order_id INT NOT NULL REFERENCES orders(order_id) ON DELETE CASCADE,
  book_id INT NOT NULL REFERENCES books(book_id),
  quantity DOUBLE PRECISION NOT NULL
);

-- END

