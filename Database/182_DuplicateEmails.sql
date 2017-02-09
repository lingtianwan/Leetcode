-- Write a SQL query to find all duplicate emails in a table named Person.
--
-- +----+---------+
-- | Id | Email   |
-- +----+---------+
-- | 1  | a@b.com |
-- | 2  | c@d.com |
-- | 3  | a@b.com |
-- +----+---------+
-- For example, your query should return the following for the above table:
--
-- +---------+
-- | Email   |
-- +---------+
-- | a@b.com |
-- +---------+
-- Note: All emails are in lowercase.


# Write your MySQL query statement below
select distinct a.Email from Person a
  inner join
  (select Email, count(Id) as Email_count
   from Person
   group by Email) b
  on a.Email=b.Email
  where b.Email_count > 1;
