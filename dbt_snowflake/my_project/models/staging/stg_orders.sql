{{ config(materialized='view') }}

WITH source AS (
    SELECT * FROM {{ source('raw', 'orders') }}
),

cleaned AS (
    SELECT
        VARIANT_COL:order_id::VARCHAR        AS order_id,
        VARIANT_COL:customer_id::VARCHAR     AS customer_id,
        VARIANT_COL:status::VARCHAR          AS status,
        VARIANT_COL:amount_cents::NUMBER     AS amount_cents,
        VARIANT_COL:amount_usd::FLOAT        AS amount_usd,
        VARIANT_COL:created_at::DATE         AS created_at,
        TO_DATE(VARIANT_COL:created_at::STRING) AS order_date
    FROM source
)

SELECT * FROM cleaned