Brazilian E-Commerce Analytics: End-to-End SQL & Power BI Pipeline
Project Overview:
-----This project transforms raw, siloed e-commerce data from Olist (the largest department store in Brazilian marketplaces) into an interactive business intelligence dashboard. I built a data pipeline that moves from 9 relational CSV files into a centralized SQL        database, performs multi-way joins for language translation and data enrichment, and delivers actionable insights on regional sales and consumer credit behavior.

 1) The Business Problem:
----The raw data was provided in Portuguese across multiple tables, making it difficult for English-speaking stakeholders to:

----Identify high-growth product categories.

----Understand regional sales concentration.

----Analyze the impact of installment-based payments on cash flow.

2) Technical Stack:
----Database: SQLite (SQL) for relational data modeling and transformation.

----Data Processing: Python (Pandas) for ETL (Extract, Transform, Load) and timestamp formatting.

---Visualization: Power BI (DAX) for interactive reporting.

3) Data Architecture & SQL Pipeline
----I engineered a "Master View" by joining 5 core tables. This eliminated data silos and translated product categories from Portuguese to English at the source.

---The "Master Join" Query:

SQL
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
    
4) Key Business Insights
----Credit Dependency:  A significant portion of high-ticket sales are driven by 10+ installment payment plans, highlighting the importance of consumer credit in the Brazilian market.

----Regional Monopoly: Over X% of total revenue is concentrated in the São Paulo (SP) region, suggesting a need for logistical optimization in outer states.

----Seasonal Surges:  The "Trend" analysis identified massive revenue spikes in November, correlating with Black Friday seasonal promotions.

5) Dashboard Features
----Revenue Trend: An Area Chart showing continuous growth from 2016 to 2018.

----Top Sellers: A Clustered Bar Chart identifying English-translated "Hero" categories.

----Geo-Analysis: A Bubble Map visualizing state-wise sales density.

----Payment Split: A Donut Chart revealing the dominance of Credit Cards over Boleto/Vouchers.

----Installment Histogram: A deep dive into how many "slices" customers use to pay for goods.
