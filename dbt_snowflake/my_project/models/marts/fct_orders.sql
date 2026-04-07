{{ config(materialized='table') }}

SELECT
    o.order_id,
    o.order_date,
    o.amount_usd,
    c.country,

    -- business metrics
    COUNT(*) OVER (PARTITION BY o.order_date) AS daily_orders

FROM {{ ref('stg_orders') }} o
LEFT JOIN {{ ref('stg_customers') }} c
    ON o.customer_id = c.customer_id