# %%
import pandas as pd

# %%
import sqlite3 
import os

# %%
conn = sqlite3.connect('olist_database.db')

# %%
folder_path = 'C:/Users/venka/Downloads/ecommerce_olist'

# %%
for file in os.listdir(folder_path):
    if file.endswith('.csv'):
        table_name = file.replace('.csv', '')
        
        df = pd.read_csv(os.path.join(folder_path, file))
        
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        print(f"Table '{table_name}' created successfully.")

conn.close()

# %%
import sqlite3
import pandas as pd

conn = sqlite3.connect('olist_database.db')
cursor = conn.cursor()


cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("Tables in Database:")
for table in tables:
    print(f"- {table[0]}")

# %%

conn = sqlite3.connect('olist_database.db')


sql_query = """
SELECT 
    o.order_id,
    o.order_purchase_timestamp,
    STRFTIME('%m', o.order_purchase_timestamp) AS month, 
    STRFTIME('%Y', o.order_purchase_timestamp) AS year, 
    t.product_category_name_english AS category,
    oi.price,
    c.customer_state,
    pay.payment_type,       
    pay.payment_installments 
FROM olist_orders_dataset o
JOIN olist_order_items_dataset oi 
    ON o.order_id = oi.order_id
JOIN olist_products_dataset p 
    ON oi.product_id = p.product_id
JOIN olist_customers_dataset c 
    ON o.customer_id = c.customer_id
JOIN product_category_name_translation t 
    ON p.product_category_name = t.product_category_name
JOIN olist_order_payments_dataset pay 
    ON o.order_id = pay.order_id;
"""

df_master = pd.read_sql_query(sql_query, conn)

conn.close()


# %%
df_master

# %%
df_master['order_purchase_timestamp'] = pd.to_datetime(df_master['order_purchase_timestamp'])

# %%
df_master

# %%
df_master.dtypes

# %%
df_master.notnull().count()

# %%
df_master.to_csv('C:/Users/venka/Downloads/ecommerce.csv', index = False)

# %%



