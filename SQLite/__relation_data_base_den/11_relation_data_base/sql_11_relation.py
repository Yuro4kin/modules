from sqlalchemy import create_engine
import pandas as pd

data = pd.read_csv('input.csv')

# Create the db engine
engine = create_engine('sqlite:///:memory:')

# Store the dataframe as a table
data.to_sql('data_table', engine)

# Query 1 on the relational table
res1 = pd.read_sql_query('SELECT * FROM data_table', engine)
print('Result 1')
print(res1)
print('')

# Query 2 on the relational table
res2 = pd.read_sql_query('SELECT dept,sum(salary) FROM data_table group by dept', engine)
print('Result 2')
print(res2)



