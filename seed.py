from config import db, app
from models import Customer, Order, Driver, Restaurant, Food, Restaurant_Food, Review
from sqlalchemy.exc import IntegrityError

def seed_data():
    with app.app_context():
        # Clear existing data
        db.session.query(Review).delete()
        db.session.query(Order).delete()
        db.session.query(Restaurant_Food).delete()
        db.session.query(Food).delete()
        db.session.query(Restaurant).delete()
        db.session.query(Driver).delete()
        db.session.query(Customer).delete()

        # Add Customers
        customers = [
            Customer(name="Daniel Ogweno", email="daniel@example.com", phone_number="254712345678", _password_hash="$2b$12$KwE5U0VH4s/D5U4XACM6yOJl4o5PU9vrNWiG9U.F4Mxy0Sv22WpaG"),
            Customer(name="Alice Wafula", email="alice@example.com", phone_number="254798765432", _password_hash="$2b$12$T7AG.2teNU8ZalRJZ2M8leBYt4R9uB4uzDYwCFIzqR5VvU1V5GxVW"),
            Customer(name="John Kamau", email="john@example.com", phone_number="254701234567", _password_hash="$2b$12$3pStPK5cQI.Ve2qmsn7xkOtAZRtBt1.0s6u1lN37W8PB3r3fPRnLW"),
            Customer(name="Jane Njeri", email="jane@example.com", phone_number="254799876543", _password_hash="$2b$12$q0sOgve6H.EySk7sz0rSL.rGU33Y8kc04Z7tJo5nndQcURq44zF7K")
        ]
        db.session.add_all(customers)

        # Add Drivers
        drivers = [
            Driver(name="John Wafula", phone_number="254755512345"),
            Driver(name="Daniel Otieno", phone_number="254755543210"),
            Driver(name="Ashley Wanjiku", phone_number="254755598765"),
            Driver(name="Maria Kimani", phone_number="254755532198")
        ]
        db.session.add_all(drivers)

        # Add Restaurants
        restaurants = [
            Restaurant(name="Nyama Choma Palace", location="123 Kenyatta Ave", image="https://theroamingfork.com/wp-content/uploads/2023/01/Mama-Oliech-Z-special-740x493.jpg?ezimgfmt=ngcb1/notWebP"),
            Restaurant(name="Mama Oliech's Kitchen", location="456 Moi Ave", image="https://tb-static.uber.com/prod/image-proc/processed_images/6b0a4bb21b758ad18b04ca2e164fdcc4/fb86662148be855d931b37d6c1e5fcbe.jpeg"),
            Restaurant(name="Java House", location="789 Ngong Rd", image="https://tb-static.uber.com/prod/image-proc/processed_images/1d684549f9a49547d4e1315d478ee88b/fb86662148be855d931b37d6c1e5fcbe.jpeg"),
            Restaurant(name="Carnivore Restaurant", location="101 Lang'ata Rd", image="https://tb-static.uber.com/prod/image-proc/processed_images/4944a9f56d74809000780f09ad45e5ea/fb86662148be855d931b37d6c1e5fcbe.jpeg"),
            Restaurant(name="K'osewe Ranalo Foods", location="102 Koinange St", image="https://tb-static.uber.com/prod/image-proc/processed_images/e050bdd8b2c4d3ae7922b49717112bb8/fb86662148be855d931b37d6c1e5fcbe.jpeg"),
            Restaurant(name="Artcaffe", location="103 Westlands Rd", image="https://tb-static.uber.com/prod/image-proc/processed_images/49828416c0957876f48f9cc25ae9547c/30be7d11a3ed6f6183354d1933fbb6c7.jpeg"),
            
            Restaurant(name="Tamasha", location="104 Kimathi St", image="https://d2jz91etbhmz77.cloudfront.net/uploads/p1600249_custom-0e784641cf2670e12b3250aa6c03254c74d10d4e.jpg"),
            Restaurant(name="K'Osewe Ranalo City", location="105 Biashara St", image="https://thestillery.co.uk/wp-content/uploads/2023/03/food-review-Mbuzi-choma-kenyan-barbeque-best-kenya-meat-fest-2023-nairobi.jpg"),
            Restaurant(name="Sierra", location="106 Yaya Center", image="https://sierrarestaurant.co.ke/wp-content/uploads/2019/11/JLC0275-e1499882038994.jpg"), 
            Restaurant(name="Talisman", location="107 Karen Rd", image="https://newplaceholderimage.com/restaurant3.jpg"),
            Restaurant(name="Hoja Moska", location="108 Railway Lane", image="https://newplaceholderimage.com/restaurant1.jpg"),
            Restaurant(name="Choma Grill", location="109 Mombasa Rd", image="https://newplaceholderimage.com/restaurant2.jpg"),
        ]

        db.session.add_all(restaurants)

        
        foods = [
            Food(name="Nyama Choma", description="Grilled meat", price=1200, image="https://lowcarbafrica.com/wp-content/uploads/2022/10/Nyama-Choma-Kenyan-Grilled-Goat-Meat-1.webp"),
            Food(name="Ugali and Fish", description="Traditional Kenyan dish", price=800, image="https://theroamingfork.com/wp-content/uploads/2023/01/Mama-Oliech-Z-special-740x493.jpg?ezimgfmt=ngcb1/notWebP"),
            Food(name="Pilau Rice", description="Spiced rice dish", price=1000, image="https://eatwellabi.com/wp-content/uploads/2022/06/Kenyan-Pilau-5-720x480.jpg"),
            Food(name="Mandazi", description="East African pastry", price=200, image="https://i.ytimg.com/vi/DGjk_1pfigM/maxresdefault.jpg"),
            Food(name="Chapati", description="Flatbread", price=300, image="https://i0.wp.com/sandhyahariharan.co.uk/wp-content/uploads/2022/09/Stack-of-Roti_-5.jpg?resize=700%2C1050&ssl=1"),
            Food(name="Sukuma Wiki", description="Sautéed collard greens", price=400, image="https://weeatatlast.com/wp-content/uploads/2020/08/Sukuma-Wiki-Recipe-braised-collard-greens.jpg"),
            Food(name="Githeri", description="Maize and beans stew", price=500, image="https://www.chefspencil.com/wp-content/uploads/Kenyan-Githeri-e1712046212481.jpg"),
            Food(name="Samaki Wa Kupaka", description="Coconut fish curry", price=1500, image="https://spicecravings.com/wp-content/uploads/2017/09/DSC_0002-copy.jpg"),
            Food(name="Pilipili Chicken", description="Spicy grilled chicken", price=1300, image="https://www.yummytummyaarthi.com/wp-content/uploads/2015/11/1-54.jpg"),
            Food(name="Beef Stew", description="Slow-cooked beef in sauce", price=1100, image="https://s23209.pcdn.co/wp-content/uploads/2020/03/Best-Ever-Beef-StewIMG_1367.jpg"),
            Food(name="Mahamri", description="Coconut doughnuts", price=250, image="https://assets.bonappetit.com/photos/608f0c83e84aa5ebc05ff63f/1:1/w_1600,c_limit/Go-Live-Mandazi-.jpg"),
            Food(name="Kachumbari", description="Fresh tomato and onion salad", price=150, image="https://i0.wp.com/mealsbymavis.com/wp-content/uploads/2019/05/KACHUMBARI_3-1.jpg?resize=1024%2C683&ssl=1"),
            Food(name="Mutura", description="Kenyan sausage", price=350, image="https://www.tasteatlas.com/Images/Dishes/514401520e9b4c438841c5bf8a9f439b.jpg?mw=1300"),
            Food(name="Samosa", description="Fried pastry with savory filling", price=100, image="https://therecipecritic.com/wp-content/uploads/2023/12/samosa-2-1025x1536.jpg"),
            Food(name="Matoke", description="Steamed plantains", price=600, image="https://cheflolaskitchen.com/wp-content/uploads/2021/12/DSC_1539-Matoke-720x1080.jpg.webp"),
            Food(name="Chips Masala", description="Spicy potato fries", price=400, image="https://thecinnamonjar.com/wp-content/uploads/2023/10/Chips-masala-2-of-5.jpg"),
            Food(name="Mukimo", description="Mashed potatoes and vegetables", price=700, image="https://lh3.googleusercontent.com/YmXrdZuvsGimestvOEJl5MQY1oe7rk4lvlWwKpmlmWpdPcahWalW2hHuFy__Zm7Bcg3O81LMIf4VelFxjgxgN4uXpPhNV1wcxkwvsLFf=s465"),
            Food(name="Nyama Mama Burger", description="Beef burger with a Kenyan twist", price=800, image="https://ocdn.eu/pulscms-transforms/1/8Dzk9kqTURBXy9mMzNjODgyNjZiNzE5MTMzYWYwNjYzMjlmMGMzZmJhOC5qcGVnkpUDAADNBKfNAp-TBc0DFs0Brt4AAqEwBqExAA"),
            Food(name="Masala Fries", description="Spicy fries", price=300, image="https://greatcurryrecipes.net/wp-content/uploads/2016/07/masalafries-735x944.jpg.webp"),
            Food(name="Bhajia", description="Fried potato slices", price=200, image="https://thetockablog.com/wp-content/uploads/2024/01/img_0224.jpg?w=683"),
            Food(name="Vegetable Biryani", description="Spiced rice with mixed vegetables", price=900, image="https://www.madhuseverydayindian.com/wp-content/uploads/2022/11/veg-biryani-683x1024.jpg"),
            Food(name="Chicken Tikka", description="Marinated grilled chicken", price=1400, image="https://www.kitchensanctuary.com/wp-content/uploads/2020/07/Chicken-Tikka-Skewers-tall-FS-87.webp"),
            Food(name="Paneer Butter Masala", description="Paneer in a rich tomato sauce", price=1200, image="https://www.secondrecipe.com/wp-content/uploads/2021/08/roti-paneer-butter-masala-720x873.jpg"),
            Food(name="Veggie Wrap", description="Vegetable-filled wrap", price=600, image="https://tastesbetterfromscratch.com/wp-content/uploads/2014/04/Veggie-Wrap-2.jpg"),
            Food(name="Fruit Salad", description="Mixed fruit salad", price=350, image="https://cdn.loveandlemons.com/wp-content/uploads/2020/06/fruit-salad-recipe-580x791.jpg"),
            Food(name="Pasta Alfredo", description="Creamy pasta with mushrooms", price=1100, image="https://www.modernhoney.com/wp-content/uploads/2018/08/Fettuccine-Alfredo-Recipe-1-1200x1182.jpg"),
            
            
            Food(name="Pizza Margherita", description="Classic pizza with tomatoes and mozzarella", price=1200, image="https://images.unsplash.com/photo-1568605114967-8130f3a36994"),
            Food(name="Tacos", description="Mexican tacos with beef and salsa", price=900, image="https://images.unsplash.com/photo-1601925321480-0666edb02fe6"),
            Food(name="Caesar Salad", description="Fresh caesar salad with croutons", price=800, image="https://images.unsplash.com/photo-1565895405227-bd07d0204fea"),
            Food(name="BBQ Ribs", description="Juicy BBQ pork ribs", price=1600, image="https://images.unsplash.com/photo-1550547660-d9450f859349"),
            Food(name="Chocolate Cake", description="Rich chocolate cake with layers", price=710, image="https://images.unsplash.com/photo-1600891964599-f61ba0e24092"),

            Food(name="Vanilla Ice Cream", description="Creamy vanilla ice cream", price=300, image="https://images.unsplash.com/photo-1488477184167-1a55918962a3"),
            Food(name="Strawberry Tart", description="Fresh strawberry tart", price=500, image="https://images.unsplash.com/photo-1562967916-eb82221dfb22"),
            Food(name="Mango Sorbet", description="Tangy mango sorbet", price=200, image="https://images.unsplash.com/photo-1568474756207-25d6921836b6"),
            Food(name="Carrot Cake", description="Spiced carrot cake with cream cheese frosting", price=750, image="https://images.unsplash.com/photo-1573101441517-1e86a521f21b"),
            Food(name="Apple Pie", description="Classic apple pie", price=600, image="https://images.unsplash.com/photo-1532634896-26909d0d4b94"),
            Food(name="Pecan Pie", description="Rich pecan pie", price=900, image="https://images.unsplash.com/photo-1558005857-cbb87f86f63a"),
            Food(name="Chocolate Chip Cookies", description="Chewy chocolate chip cookies", price=150, image="https://images.unsplash.com/photo-1589884115217-c73e5c69f873"),
            Food(name="Brownies", description="Fudgy chocolate brownies", price=400, image="https://images.unsplash.com/photo-1548369595946-75555c878f33"),
            Food(name="Tiramisu", description="Classic Italian tiramisu", price=800, image="https://images.unsplash.com/photo-1612884761948-9e75e29e3a1c"),
            Food(name="Raspberry Cheesecake", description="Creamy raspberry cheesecake", price=900, image="https://images.unsplash.com/photo-1543353071-087092ec393a"),

        
            Food(name="BBQ Chicken Wings", description="Grilled chicken wings with BBQ sauce", price=900, image="https://images.unsplash.com/photo-1586190848861-99aa4a171e90"),
            Food(name="Fish and Chips", description="Fried fish with crispy fries", price=700, image="https://images.unsplash.com/photo-1562967916-eb82221dfb22"),
            Food(name="Shrimp Cocktail", description="Chilled shrimp with cocktail sauce", price=1200, image="https://images.unsplash.com/photo-1517248135467-4c7edcad34c4"),
            Food(name="Falafel", description="Deep-fried chickpea balls", price=400, image="https://images.unsplash.com/photo-1504909038004-bd56e6b67f6b"),
            Food(name="Greek Salad", description="Salad with feta cheese and olives", price=500, image="https://images.unsplash.com/photo-1568605114967-8130f3a36994"),
            Food(name="Beef Tacos", description="Mexican tacos with beef filling", price=700, image="https://images.unsplash.com/photo-1601925321480-0666edb02fe6"),
            Food(name="Garlic Bread", description="Bread with garlic butter", price=200, image="https://images.unsplash.com/photo-1617196033508-58be8b5e371b"),
            Food(name="Butter Chicken", description="Creamy Indian chicken curry", price=1100, image="https://images.unsplash.com/photo-1565299624946-b28f40a0ae38"),
            Food(name="Chicken Kebab", description="Skewered grilled chicken", price=800, image="https://images.unsplash.com/photo-1554284126-aa88f22d267c"),
            Food(name="Eggplant Parmesan", description="Baked eggplant with cheese", price=900, image="https://images.unsplash.com/photo-1565895405227-bd07d0204fea")
]

        db.session.add_all(foods)
        

        # Add Restaurant_Foods relationships
        restaurant_foods = [
            Restaurant_Food(restaurant=restaurants[0], food=foods[0]),
            Restaurant_Food(restaurant=restaurants[0], food=foods[1]),
            Restaurant_Food(restaurant=restaurants[1], food=foods[2]),
            Restaurant_Food(restaurant=restaurants[1], food=foods[3]),
            Restaurant_Food(restaurant=restaurants[2], food=foods[4]),
            Restaurant_Food(restaurant=restaurants[2], food=foods[5]),
            Restaurant_Food(restaurant=restaurants[3], food=foods[6]),
            Restaurant_Food(restaurant=restaurants[3], food=foods[7]),
            Restaurant_Food(restaurant=restaurants[4], food=foods[8]),
            Restaurant_Food(restaurant=restaurants[4], food=foods[9]),
            Restaurant_Food(restaurant=restaurants[5], food=foods[10]),
            Restaurant_Food(restaurant=restaurants[5], food=foods[11]),
            Restaurant_Food(restaurant=restaurants[6], food=foods[12]),
            Restaurant_Food(restaurant=restaurants[6], food=foods[13]),
            Restaurant_Food(restaurant=restaurants[7], food=foods[14]),
            Restaurant_Food(restaurant=restaurants[7], food=foods[15]),
            Restaurant_Food(restaurant=restaurants[8], food=foods[16]),
            Restaurant_Food(restaurant=restaurants[8], food=foods[17]),
            Restaurant_Food(restaurant=restaurants[9], food=foods[18]),
            Restaurant_Food(restaurant=restaurants[9], food=foods[19]),
            Restaurant_Food(restaurant=restaurants[10], food=foods[20]),
            Restaurant_Food(restaurant=restaurants[10], food=foods[21]),
            Restaurant_Food(restaurant=restaurants[11], food=foods[22]),
            Restaurant_Food(restaurant=restaurants[11], food=foods[23]),
            Restaurant_Food(restaurant=restaurants[11], food=foods[24]),
            Restaurant_Food(restaurant=restaurants[0], food=foods[25]),
            Restaurant_Food(restaurant=restaurants[0], food=foods[26]),
            Restaurant_Food(restaurant=restaurants[1], food=foods[27]),
            Restaurant_Food(restaurant=restaurants[1], food=foods[28]),
            Restaurant_Food(restaurant=restaurants[2], food=foods[29]),
            Restaurant_Food(restaurant=restaurants[2], food=foods[30]),
            Restaurant_Food(restaurant=restaurants[3], food=foods[31]),
            Restaurant_Food(restaurant=restaurants[3], food=foods[32]),
            Restaurant_Food(restaurant=restaurants[4], food=foods[33]),
            Restaurant_Food(restaurant=restaurants[4], food=foods[34]),
            Restaurant_Food(restaurant=restaurants[5], food=foods[35]),
            Restaurant_Food(restaurant=restaurants[5], food=foods[36]),
            Restaurant_Food(restaurant=restaurants[6], food=foods[37]),
            Restaurant_Food(restaurant=restaurants[6], food=foods[38]),
            Restaurant_Food(restaurant=restaurants[7], food=foods[39]),
            Restaurant_Food(restaurant=restaurants[7], food=foods[40]),
            Restaurant_Food(restaurant=restaurants[8], food=foods[41]),
            Restaurant_Food(restaurant=restaurants[8], food=foods[42]),
            Restaurant_Food(restaurant=restaurants[9], food=foods[43]),
            Restaurant_Food(restaurant=restaurants[9], food=foods[44]),
            Restaurant_Food(restaurant=restaurants[10], food=foods[45]),
            Restaurant_Food(restaurant=restaurants[10], food=foods[46]),
            Restaurant_Food(restaurant=restaurants[11], food=foods[47]),
            Restaurant_Food(restaurant=restaurants[11], food=foods[48]),
            Restaurant_Food(restaurant=restaurants[11], food=foods[49]),
            Restaurant_Food(restaurant=restaurants[0], food=foods[50])
        ]
        db.session.add_all(restaurant_foods)

        # Add Orders
        orders = [
            Order(customer=customers[0], driver=drivers[0], food=foods[0]),
            Order(customer=customers[1], driver=drivers[1], food=foods[1]),
            Order(customer=customers[2], driver=drivers[2], food=foods[2]),
            Order(customer=customers[3], driver=drivers[3], food=foods[3]),
            Order(customer=customers[0], driver=drivers[1], food=foods[4]),
            Order(customer=customers[1], driver=drivers[2], food=foods[5]),
            Order(customer=customers[2], driver=drivers[3], food=foods[6]),
            Order(customer=customers[3], driver=drivers[0], food=foods[7]),
            Order(customer=customers[0], driver=drivers[1], food=foods[8]),
            Order(customer=customers[1], driver=drivers[2], food=foods[9]),
            Order(customer=customers[2], driver=drivers[3], food=foods[10]),
            Order(customer=customers[3], driver=drivers[0], food=foods[11]),
            Order(customer=customers[0], driver=drivers[2], food=foods[12]),
            Order(customer=customers[1], driver=drivers[3], food=foods[13]),
            Order(customer=customers[2], driver=drivers[0], food=foods[14]),
            Order(customer=customers[3], driver=drivers[1], food=foods[15]),
            Order(customer=customers[0], driver=drivers[3], food=foods[16]),
            Order(customer=customers[1], driver=drivers[0], food=foods[17]),
            Order(customer=customers[2], driver=drivers[1], food=foods[18]),
            Order(customer=customers[3], driver=drivers[2], food=foods[19]),
            Order(customer=customers[0], driver=drivers[0], food=foods[20]),
            Order(customer=customers[1], driver=drivers[1], food=foods[21]),
            Order(customer=customers[2], driver=drivers[2], food=foods[22]),
            Order(customer=customers[3], driver=drivers[3], food=foods[23]),
            Order(customer=customers[0], driver=drivers[1], food=foods[24])
        ]
        db.session.add_all(orders)

        # Add Reviews
        reviews = [
            Review(message="Delicious nyama choma!", customer=customers[0], food=foods[0]),
            Review(message="Ugali and fish was perfect!", customer=customers[1], food=foods[1]),
            Review(message="Best pilau rice ever!", customer=customers[2], food=foods[2]),
            Review(message="Mandazi was so fresh!", customer=customers[3], food=foods[3]),
            Review(message="Chapati was great!", customer=customers[0], food=foods[4]),
            Review(message="Sukuma wiki was tasty!", customer=customers[1], food=foods[5]),
            Review(message="Githeri was filling!", customer=customers[2], food=foods[6]),
            Review(message="Samaki wa kupaka was delicious!", customer=customers[3], food=foods[7]),
            Review(message="Pilipili chicken was spicy and delicious!", customer=customers[0], food=foods[8]),
            Review(message="Beef stew was rich and tasty!", customer=customers[1], food=foods[9]),
            Review(message="Mahamri were perfect for breakfast!", customer=customers[2], food=foods[10]),
            Review(message="Kachumbari was fresh and tangy!", customer=customers[3], food=foods[11]),
            Review(message="Mutura was a unique experience!", customer=customers[0], food=foods[12]),
            Review(message="Samosa was crispy and flavorful!", customer=customers[1], food=foods[13]),
            Review(message="Matoke was well-cooked and delicious!", customer=customers[2], food=foods[14]),
            Review(message="Chips masala were perfectly seasoned!", customer=customers[3], food=foods[15]),
            Review(message="Mukimo was comforting and tasty!", customer=customers[0], food=foods[16]),
            Review(message="Nyama Mama Burger was juicy and flavorful!", customer=customers[1], food=foods[17]),
            Review(message="Masala fries were spicy and crispy!", customer=customers[2], food=foods[18]),
            Review(message="Bhajia were crunchy and delicious!", customer=customers[3], food=foods[19]),
            Review(message="Vegetable biryani was fragrant and tasty!", customer=customers[0], food=foods[20]),
            Review(message="Chicken tikka was perfectly grilled!", customer=customers[1], food=foods[21]),
            Review(message="Paneer butter masala was creamy and rich!", customer=customers[2], food=foods[22]),
            Review(message="Veggie wrap was fresh and filling!", customer=customers[3], food=foods[23]),
            Review(message="Fruit salad was refreshing and healthy!", customer=customers[0], food=foods[24])
        ]
        db.session.add_all(reviews)

        try:
            # Commit all changes
            db.session.commit()
            print("Database seeded with new data!")
        except IntegrityError:
            db.session.rollback()
            print("Integrity error occurred. Database rollback.")

if __name__ == "__main__":
    seed_data()
