import sqlfluff

#  -------- DIALECTS ----------

dialects = sqlfluff.list_dialects()
# dialects = [DialectTuple(label='ansi', name='ansi', inherits_from='nothing'), ...]
dialect_names = [dialect.label for dialect in dialects]
print(dialect_names)
# dialect_names = ["ansi", "snowflake", ...]


#  -------- RULES ----------

rules = sqlfluff.list_rules()
# rules = [
#     RuleTuple(
#         code='Example_LT01',
#         description='ORDER BY on these columns is forbidden!'
#     ),
#     ...
# ]
rule_codes = [rule.code for rule in rules]
print(rule_codes)
# rule_codes = ["LT01", "LT02", ...]

my_bad_query = "ALTER TABLE t_c4c_opportunity MODIFY COLUMN rfp_date DATE;"

# Lint the given string and return an array of violations in JSON representation.
lint_result = sqlfluff.lint(my_bad_query, dialect="mysql")
print(lint_result)