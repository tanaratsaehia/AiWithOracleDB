create view admin_sale_history_data as 
select path_picture, users.user_id, user_name, model, production_year, mile_used, license_plate, phone_number, predict_price, user_offer_price, admin_offer_price
from users, sales_history, car
where users.user_id = sales_history.user_id and sales_history.car_id = car.car_id;