Questions to be asked in interview:

Python:

1) Explain the use of Ternary operator in Python?

In Python, Ternary operator added in the version 2.5. It is used as a conditional statement; it consists of the true or false values. Ternary operator evaluates the statement and stores true or false values.

What is the use of dir() function?

After assigning values to a few variables, we could use the dir() function to show their existence. In the following example, variables p, av, and d are shown among other names.

What is string replication operator in Python?

A) * is the string replication operator, repeating a single string however many times you would like through the integer you provide.

Example: Let’s print out “Python” 5 times without typing out “Python” 5 times with the * operator:

print(“Python” * 5)

Output: PythonPythonPythonPythonPython

1. What is lambda function?

2. How do you copy an object in python? How many ways are there?

3. Can we achieve the method overloading in python? If yes? how?

4. What is diff between .py and .pyc?

5. What is context manager in python?

6. What is GIL in python?

7. What diff bet access specifier and namespace?

django

1. How you can ensure the security of Django application proper user authentication and authorization mechanisms.

2. How to optimize api performance?

3. Api integration challenges?

Fastapi:

1. How do you validate the request body in fastapi?

2. What architecture fatsapi follow? 3. Can you explain how you would implement authentication and authorization in FastAPI? 4. How would you handle exception handling and custom error responses in FastAPI?

AWS:

1. what is api gateway in aws?

2. What is lambda function in aws?

3. What Is dynamo db?

4. What procedure you follow to deploy your application on serverless service of aws?

Coding:

s1 = "skyies are blue"

s2 = "134"

result = “s1kyi3es a4re blue”

flatten list using recursion

l = [1,2,3,[4,5,[6,[7,8]]]]


Sort the dictionary by values.

{‘a’:10,’b’:5,’c’:3,’d’:20}




s1 = "skyies are blue"

s2 = "134"

def skipchar(s1,s2):

lst=[]

for i in s2:

if i.isdigit():

lst.append(i)

result = ""

for i in lst:

s3 = s1[:int(i)]+f"{i}"

#print(s3)

s1= s1[int(i):]

print(s1)

result = result + s3

#print(result)

result = result + s1


print(result)

skipchar(s1,s2)

Barclays interview questions

Internal Round :

1. How to iterate a list in python
2.How to find the count in a list 
3.How to get a unique list
4.Repartition and coalesce
5.About project explain
6. Spark optimization techniques used
7. Syntax for performing joins
8. given a sentence and asked to find the count for each word(word count)

Round - 1 Interview (Client) : 

1.Union and Union all (diff)
2.Managed and external tables in hive (diff)
3.Trancate and delete (diff)
4. How union behaves in pyspark and sql 
5. Diff b/w Row_number(),rank(),dense_rank()
6.Repartition and Coalesce (diff)
7. What to be used when we have write the target files as single file 
8. I have 10 dates (1-10 Jan) , I want to write 10 part files where data corresponding to the dates should be saved. 
9. Regarding version control 
10. GitHub question : commit, commit revert, how to get the old commit code, how to take it to local.  

Round - 2 Interview (Client) :

1. What is indexing. 
2. What is primary indexing and secondary indexing 
3. Given a table 
   a  b
   1  1
   2  2
   3  3
      4
    asked to display only 4. 
4. Given a table and asked to give rank according to row_number() and rank()
5. Given a table asked to take the employee who gets highest salary
6. Same as above asked to display minimum salaried employee. 


spark architecture
how read zip files in pyspark
what is the difference between parquet and csv
lazy evaluation
explain some optimization techniques in pyspark
how to handle skewed data
To swap the values in the gender column of the student table where the gender is 'female' and 'male'
difference between repartision and coaleesce
write spark program to retrieve the last 7 days records
diffrence between cache and persist

QBE account






















































































Questons bank of vanguard
1.explain what is spark architecture
2.what are the optimization techniques use in spark and ur project
3.diffrence between broadcast variable and sort merge and hash join 
4. how can u sortout if u r spark job getting slow what causes u consider or what tactics u used to get over.
5.have u work on aws tell me redshift aws glue and emr
6. solving scenario on sql just orally giving hints and execution
7.task stage job explain in detail.



What services you used in aws ?
Optimizing techniquics in spark ?



To swap the values in the gender column of the student table where the gender is 'female' and 'male'
input table
 Eno Ename Mgrno
10 Anil NULL
20 Pavan 10
30 Sunil 20
40 Kumar 10
50 Vijay 20
Result ======
Eno Ename Mgr Name
10 Anil No Manager
20 Pavan Anil
30 Sunil Pavan
40 Kumar Anil
50 Vijay Pavan

Finding Duplicate Email IDs in SQL

rank(),dens_rank,lead andlag related questions

joins() related questions
diffrence between delete and truncate

QBE account  questions:


Python	What is the relevant exp. in Python
	Do you have idea about Rest Apis ?
	Which module is used for calling REST APIS?
	Have you used various data types like List, Tuple, dictionary, Set in your Python Scripts?
	Have you worked on file handling through python?
	Do you have knowledge on OOPS concepts?
	Do you have experience using commandline arguments in Python scripts?
	Can you name some primary modules used in Python?
	Have you used paramiko module in python? If yes, what is the purpose
	
Django	What is the relevant exp. in Django
	How many projects have you worked on Django ?
	Do you know how to create a REST API in Django?
	Do you have work exp. in HTML, CSS?
	Have you worked on Bootstrap?
	Do you have working  knowledge of Javascript/Jquery?
	Do you have idea on deploying web application on web server?
	Do you have working exp. on Javascript framework like React, Node, Angular, Vue
	Do you have working exp. On Jinja template engine
	Do you have working exp. in Database 


































Return dictionary with number and its square using dict comprehension
Joins in sql
Explain rank 
find second max salary 
create dataframe of given data in pandas then rename column name 
"Questions on :Decorators
List and dictionary comprehension
Inheritance
Polymorphism
Abstraction
Memory management"
Agile methodology
"input_list=[1,2,3,4,5,6,7] target=9

output=[(2,7),(3,6)(4,5)]

write a python program"