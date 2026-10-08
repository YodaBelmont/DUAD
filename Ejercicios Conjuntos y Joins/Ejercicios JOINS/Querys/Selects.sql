--Query1

-- SELECT Books.Name AS book_name, Authors.Name AS author_name
-- FROM Books
-- LEFT JOIN Authors
-- ON Books.Author = Authors.ID;

--Query2

-- SELECT Books.Name AS book_name, Authors.Name AS author_name
-- FROM Books
-- LEFT JOIN Authors
-- ON Books.Author = Authors.ID
-- WHERE Books.Author IS NULL;

--Query3

-- SELECT Books.Name AS book_name, Authors.Name AS author_name
-- FROM Authors
-- LEFT JOIN Books
-- ON Authors.ID = Books.Author
-- WHERE Books.Author IS NULL;

--Query4

-- SELECT Books.Name AS book_name,Rents.State AS rent_state
-- FROM Rents
-- LEFT JOIN Books
-- ON Rents.BookID = Books.ID;

--Query5

-- SELECT Books.Name AS book_name,Rents.State AS rent_state
-- FROM Books
-- LEFT JOIN Rents
-- ON Books.ID = Rents.BookID
-- WHERE rent_state IS NULL;

--Query6

-- SELECT Customers.Name AS customer_name,Rents.BookID AS book_id
-- FROM Customers
-- LEFT JOIN Rents
-- ON Customers.ID = Rents.CustomerID
-- WHERE book_id IS NULL;

--Query7

-- SELECT Books.Name AS book_name,Rents.State AS rent_state
-- FROM Books
-- LEFT JOIN Rents
-- ON Books.ID = Rents.BookID
-- WHERE rent_state = 'Overdue';