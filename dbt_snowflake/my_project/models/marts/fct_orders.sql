with orders as (

    select * from {{ ref('stg_orders') }}

),

customers as (

    select * from {{ ref('stg_customers') }}

),

joined as (

    select
        o.order_id,
        o.customer_id,
        o.order_date,
        o.amount_usd,
        o.status,
        c.signup_date,
        current_date - c.signup_date as days_since_signup

    from orders o
    left join customers c
        on o.customer_id = c.customer_id

),

final as (

    select
        *,
        case 
            when days_since_signup > 30 then 'old'
            else 'new'
        end as customer_segment

    from joined

)

select *
from final

{% if is_incremental() %}
where order_date > (select max(order_date) from {{ this }})
{% endif %}