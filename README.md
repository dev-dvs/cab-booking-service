# 🚕 Cab Booking Application

## 📌 Description

A simple cab booking application built using in-memory data structures. The system supports user and driver onboarding, ride booking, billing, and earnings tracking.

---

## ✨ Features

- Users can register and update their details including location.
- Drivers can onboard with vehicle and location details.
- Users can:
  - Search for available rides from source to destination.
  - Choose a ride based on proximity and availability.
  - Get billed based on distance.
- System tracks total earnings per driver.

---

## 📋 Requirements

### 1. User Onboarding

- `add_user(user_detail)`
  - Add basic user details.
- `update_user(username, updated_details)`
  - Update user's contact details.
- `update_userLocation(username, location)`
  - Updates user’s location in (X, Y) coordinates.

### 2. Driver Onboarding

- `add_driver(driver_details, vehicle_details, current_location)`
  - Adds a driver and their current location.
- `update_driverLocation(driver_name)`
  - Updates current driver location.
- `change_driver_status(driver_name, status)`
  - Marks driver as available/unavailable using a boolean.

### 3. Ride Booking

- `find_ride(username, source, destination)`
  - Returns a list of available rides.
- `choose_ride(username, driver_name)`
  - Selects a driver for the ride.
  - ⚠️ Only drivers within a 5-unit distance and in `available` state are shown.
- `calculateBill(username)`
  - Calculates bill based on distance between source and destination.

### 4. Driver Earnings

- `find_total_earning()`
  - Shows the total earnings of all drivers.
