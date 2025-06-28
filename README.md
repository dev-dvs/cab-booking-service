### Cab Booking Application

# Description:

Implement a cab booking application. Below are the expected features from the system.

# Features:
The application allows users to book rides on a route.
Users can register themself and make changes to their details.
Driving partner can onboard on the system with the vehicle details
Users can search and select one from multiple available rides on a route with the same source and destination based on the nearest to the user
Requirements:
Application should allow user onboarding.
add_user(user_detail)
Add basic user details
update_user(username, updated_details)
User should be able to update its contact details
update_userLocation(username,Location):
This will update the user location in X , Y coordinate to find nearest in future
Application should allow Driver onboarding
add_driver(driver_details,vehicle_details,current_location)
This will create an instance of the driver and will mark his current location on the map
update_driverLocation(driver_name)
This will mark the current location of driver 
change_driver_status(driver_name,status)
In this driver can make himself either available or unavailable via a boolean
      
Application should allow the user to find a ride based on the criteria below
find_ride (Username,Source , destination)
It will return a list of available ride 
choose_ride(Username,drive_name)
It will choose the drive name from the list
	Note : Only the driver which is at a max distance of 5 unit will be displayed to a user and 
		the driver should be in available state to confirm the booking
calculateBill(Username):
It will return the bill based on the distance between the source and destination and will display it    
Application should at the end calculate the earning of all the driver onboarded in the      application find_total_earning()
Other Notes:
Write a driver class for demo purposes. Which will execute all the commands at one place in the code and have test cases.
Do not use any database or NoSQL store, use in-memory data-structure for now. 
Do not create any UI for the application.
Please prioritize code compilation, execution and completion. 
Work on the expected output first and then add bonus features of your own.
Expectations:
Make sure that you have a working and demo-able code.
Make sure that code is functionally correct.
Use of proper abstraction, entity modelling, separation of concerns is good to have.
Code should be modular, readable and unit-testable.
Code should easily accommodate new requirements with minimal changes.
Proper exception handling is required.
Concurrency Handling (BONUS) [Good if you do this]

# Sample Test Cases:
Onboard 3 users
add_user(“Abhishek, M, 23”); update_userLocation(“Abhishek”,(0,0)) 
add_user(“Rahul , M, 29”); update_userLocation(“Rahul”,(10,0))
add_user(“Nandini, F, 22”) ;update_userLocation(“Nandini”,(15,6))

Onboard 3 driver to the application
add_driver(“Driver1, M, 22”,“Swift, KA-01-12345”,(10,1))
add_driver(“Driver2, M, 29”,“Swift, KA-01-12345”,(11,10))
add_driver(“Driver3, M, 24”,“Swift, KA-01-12345”,(5,3))
	
User trying to get a ride 
find_ride(“Abhishek” ,(0,0),(20,1))
		Output : No ride found [Since all the driver are more than 5 units away from user]
find_ride(“Rahul” ,(10,0),(15,3))
		Output : Driver1 [Available]
		choose_ride(“Rahul”,”Driver1”)
		Output : ride Started
		calculateBill(“Rahul”)
		Output : ride Ended bill amount $ 6
		Backend API Call:	update_userLocation(“Rahul”,(15,3))
					update_driverLocation(“Driver1”,(15,3))
change_driver_status(“Driver1”,False)
find_ride(“Nandini”,(15,6),(20,4))
Output : No ride found [Driver one in set to not available]
Total earning by drivers
find_total_earning()
Driver1 earn $6
Driver2 earn $0
Driver3 earn $0
