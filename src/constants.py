SQLITE_QUERY = """
            select
                sale_item.id sale_item_id,
                sale_item.sale_id sale_item_sale_id,
                sale_item.product_id sale_item_product_id,
                sale_item.quantity sale_item_quantity,
                sale_item.packed sale_item_packed,
                product.id product_id,
                product.name product_name,
                product.product_category_id product_product_category_id,
                product.unit_price product_unit_price,
                product_category.id product_category_id,
                product_category.name product_category_name,
                sale.id sale_id,
                sale.employee_id sale_employee_id,
                sale.customer_id sale_customer_id,
                sale.date_time sale_date_time,
                customer.id customer_id,
                customer.person_id customer_person_id,
                person.id person_id,
                person.name person_name,
                person.birth person_birth,
                person.uf person_uf,
                person.sex person_sex,
                person.height person_height,
                person.weight person_weight,
                person.daily_sugar_intake person_daily_sugar_intake,
                person.daily_fat_intake person_daily_fat_intake,
                customer_person_city.id customer_person_city_id,
                customer_person_city.name customer_person_city_name,
                customer_person_city.uf_id customer_person_city_uf_id,
                customer_person_city.latitude customer_person_city_latitude,
                customer_person_city.longitude customer_person_city_longitude,
                customer_person_city.capital customer_person_city_capital,
                employee.id employee_id,
                employee.person_id employee_person_id,
                employee.company_id employee_company_id,
                company.id company_id,
                company.name company_name,
                company.uf company_uf,
                company_city.id company_city_id,
                company_city.name company_city_name,
                company_city.uf_id company_city_uf_id,
                company_city.latitude company_city_latitude,
                company_city.longitude company_city_longitude,
                company_city.capital company_city_capital,
                person_1.id person_1_id,
                person_1.name person_1_name,
                person_1.birth person_1_birth,
                person_1.uf person_1_uf,
                person_1.sex person_1_sex,
                person_1.height person_1_height,
                person_1.weight person_1_weight,
                person_1.daily_sugar_intake person_1_daily_sugar_intake,
                person_1.daily_fat_intake person_1_daily_fat_intake,
                employee_person_city.id employee_person_city_id,
                employee_person_city.name employee_person_city_name,
                employee_person_city.uf_id employee_person_city_uf_id,
                employee_person_city.latitude employee_person_city_latitude,
                employee_person_city.longitude employee_person_city_longitude,
                employee_person_city.capital employee_person_city_capital
            from
                sale_item
                inner join product on ((sale_item.product_id = product.id))
                inner join product_category on ((product.product_category_id = product_category.id))
                inner join sale on ((sale_item.sale_id = sale.id))
                inner join customer on ((sale.customer_id = customer.id))
                inner join person on ((customer.person_id = person.id))
                inner join city customer_person_city on ((person.city_id = customer_person_city.id))
                inner join employee on ((sale.employee_id = employee.id))
                inner join company on ((employee.company_id = company.id))
                inner join city company_city on ((company.city_id = company_city.id))
                inner join person person_1 on ((employee.person_id = person_1.id))
                inner join city employee_person_city on ((person_1.city_id = employee_person_city.id))
        """