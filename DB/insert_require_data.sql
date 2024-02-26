insert into transmission values (0, 'Manual');
insert into transmission values (1, 'Automatic');
insert into transmission values (2, 'Semi-Auto');
commit;

insert into fuel values (0, 'Petrol');
insert into fuel values (1, 'Diesel');
insert into fuel values (2, 'Hybrid');
insert into fuel values (3, 'Electric');
insert into fuel values (4, 'Other');
commit;


-- exist_data = []
-- j = 0
-- for i in range(len(data['model'])):
--     format_data = [data['model'][i], data['year'][i], data['engineSize'][i], data['mpg'][i], transmission_mapping[data['transmission'][i]], fuel_mapping[data['fuelType'][i]]]
--     if format_data not in exist_data:
--         exist_data.append(format_data)
--         con.insertData(table='car', primary_key=j, values=f"'{format_data[0]}', '{format_data[1]}', '{format_data[2]}', '{format_data[3]}', '{format_data[4]}', '{format_data[5]}'")
--         j+=1
