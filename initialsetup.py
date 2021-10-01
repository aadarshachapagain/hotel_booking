# import mysql.connector
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="c4c",
    passwd="paradise",
    database="db_travelshaw"
)

mycursor = mydb.cursor()
sql_account = "INSERT INTO `account_account_type` (`id`, `display_name`, `type`, `module`, `created_at`, `description`) VALUES (%s, %s, %s,%s,%s,%s)"
val_account = [
    (1, 'Rental Owner', 'rental_owner', 'rental', '2019-04-18 09:00:00.000000', ''),
    (2, 'Rental Staff', 'rental_staff', 'rental', '2019-04-17 00:00:00.000000', ''),
    (3, 'Travel Owner', 'travel_tour_owner', 'travel_tour', '2019-04-04 00:00:00.000000',
     ''),
    (4, 'Travel Staff', 'travel_tour_staff', 'travel_tour', '2019-04-04 00:00:00.000000',
     ''),
    (5, 'Hotel Owner ', 'hotel_owner', 'hotel', '2019-04-04 00:00:00.000000', ''),
    (6, 'Hotel Staff', 'hotel_staff', 'hotel', '2019-04-11 00:00:00.000000', ''),
    (7, 'Restaurant Owner', 'restaurant_owner', 'restaurant', '2019-04-18 10:23:32.593655', ''),
    (8, 'Restaurant Staff', 'restaurant_staff', 'restaurant', '2019-04-18 09:31:32.554624', '')
]
sql_mp = "INSERT INTO `hotel_mealplan` (`id`, `plan`, `full_form`, `status`, `created_at`)VALUES (%s, %s, %s,%s,%s)"
val_mp = [
    (1, 'EP', 'European Plan', 1, '2020-03-19 17:24:30.970372'),
    (2, 'BB', 'Bed and Breakfast', 1, '2020-03-19 17:24:55.549175')
]
sql_ss = "INSERT INTO `hotel_similarsystems` (`id`, `name`, `status`, `created_at`) VALUES (%s, %s, %s,%s)"
val_ss = [
    (1, 'Booking.com', 1, '2020-03-19 17:23:48.459231'),
    (2, 'Bigsafar', 1, '2020-03-19 17:23:57.937146'),
    (3, 'Excel', 1, '2020-03-19 17:24:05.788427')
]

mycursor.executemany(sql_account, val_account)
print('account_type created')
mycursor.executemany(sql_mp, val_mp)
print('mealplan_type created')
mycursor.executemany(sql_ss, val_ss)
print('similar_systems created')
mydb.commit()


