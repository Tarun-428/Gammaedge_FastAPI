{{ config(materialized='ephemeral') }}

SELECT
    o.order_id,
    o.customer_id,
    o.amount_usd,
    o.status,
    o.created_at,
    o.order_date,

    c.country,
    c.signup_date,

    DATEDIFF('day', c.signup_date, o.order_date) AS days_since_signup

FROM {{ ref('stg_orders') }} o
LEFT JOIN {{ ref('stg_customers') }} c
    ON o.customer_id = c.customer_id