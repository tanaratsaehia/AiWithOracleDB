
-- SALE HISTORY FOR ADMIN
create view admin_sale_history_data as 
select path_picture, users.user_id, user_name, model, production_year, mile_used, license_plate, phone_number, predict_price, user_offer_price, admin_offer_price, status
from users, sales_history, car
where users.user_id = sales_history.user_id and sales_history.car_id = car.car_id
order by sale_id;


-- SALE HISTORY SINGLE USER
select path_picture, model, production_year, mile_used, license_plate, predict_price, user_offer_price, admin_offer_price, status
from users, sales_history, car
where users.user_id = sales_history.user_id and sales_history.car_id = car.car_id and sales_history.user_id = {user_id}
order by sale_id;