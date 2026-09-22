-- Write your query below
with second_layer as (
    select a.employee_id, a.employee_name, a.manager_id, 
        b.manager_id as second_layer
    from employees a
    left join employees b on a.manager_id = b.employee_id
),
third_layer as (
    select a.employee_id, a.employee_name, a.manager_id, 
        a.second_layer, b.manager_id as third_layer
    from second_layer a
    left join employees b on a.second_layer = b.employee_id
)
select employee_id
from third_layer
where (manager_id = 1 or second_layer = 1 or third_layer = 1)
    and employee_id != 1;