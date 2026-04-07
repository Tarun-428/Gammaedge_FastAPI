{{ config(materialized='view') }}

SELECT
    VARIANT_COL:order_id::int as order_id,
    VARIANT_COL:customer_id::string as customer_id,
    VARIANT_COL:status::string as status,
    VARIANT_COL:amount_usd::float as amount_usd,
    VARIANT_COL:created_at::date as order_date
FROM {{ source('raw', 'orders') }}

WHERE order_id IS NOT NULL