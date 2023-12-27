import sqlfluff

# def lint_sql_syntax(queries):
#     error_count = 0

#     for idx, query in enumerate(queries, start=1):
#         try:
#             # Parse and lint individual SQL query using sqlfluff without fixing
#             parsed = sqlfluff.parse(query, dialect='ansi', fix=False)

#             # If no parsing error occurred, syntax is valid
#             print(f"SQL query {idx}: Valid syntax.")
        
#         except sqlfluff.exceptions.SQLBaseError as e:
#             print(f"SQL query {idx}: Syntax error - {e}")
#             error_count += 1  # Increment error count for each syntax error
    
#     return error_count  # Return the total count of syntax errors found
import sqlfluff

# Sample queries
sample_query_list = [
    "SELECT * FROM table1 WHERE condition1;",
    "SELECT column1, column2 FROM table2 WHERE condition2;",
    "SELECT * FROM table3 WHERE condition3 AND",  # This query has a syntax error
    "SELECT column1 FROM table4 WHERE condition4;"
]

# Join queries into a single string
queries_string = "\n".join(sample_query_list)

# Lint the queries
result = sqlfluff.lint(queries_string)

# Access exceptions if there are linting errors
if result:
    for violation in result:
        print(violation)
    total_errors = len(result)
    print(total_errors)
else:
      print("No error")

# Sample list of SQL queries


# # Run the function to lint SQL query syntax
# total_errors = lint_sql_syntax(sample_query_list)

# # Exit with status code based on the number of syntax errors found
# exit(total_errors)
