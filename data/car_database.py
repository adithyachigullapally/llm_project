"""
Car inventory database with realistic Indian market vehicles.
Includes detailed specs, pricing, and features.
"""
from typing import List, Dict, Any
from schema import VehicleSpecs


# Comprehensive car inventory
CAR_INVENTORY = [
    # Hatchbacks - Budget Segment
    {
        "vehicle_id": "CAR001",
        "name": "Maruti Suzuki Alto K10",
        "brand": "Maruti Suzuki",
        "model": "Alto K10",
        "year": 2024,
        "type": "hatchback",
        "price": 525000,
        "mileage": 24.9,
        "fuel_type": "petrol",
        "transmission": "manual",
        "engine_cc": 998,
        "power": "66 bhp",
        "torque": "89 Nm",
        "seating": 5,
        "features": ["ABS", "EBD", "Dual Airbags", "Keyless Entry", "Power Windows"],
        "safety_rating": 3.5,
        "warranty_years": 2,
        "colors_available": ["White", "Silver", "Red", "Blue"],
        "stock_status": "available"
    },
    {
        "vehicle_id": "CAR002",
        "name": "Hyundai Grand i10 Nios",
        "brand": "Hyundai",
        "model": "Grand i10 Nios",
        "year": 2024,
        "type": "hatchback",
        "price": 750000,
        "mileage": 20.7,
        "fuel_type": "petrol",
        "transmission": "manual",
        "engine_cc": 1197,
        "power": "82 bhp",
        "torque": "114 Nm",
        "seating": 5,
        "features": ["Touchscreen", "Wireless Charging", "Rear AC Vents", "6 Airbags", "ABS", "ESP"],
        "safety_rating": 4.0,
        "warranty_years": 3,
        "colors_available": ["White", "Silver", "Black", "Red", "Blue"],
        "stock_status": "available"
    },
    {
        "vehicle_id": "CAR003",
        "name": "Tata Tiago",
        "brand": "Tata",
        "model": "Tiago",
        "year": 2024,
        "type": "hatchback",
        "price": 650000,
        "mileage": 23.8,
        "fuel_type": "petrol",
        "transmission": "manual",
        "engine_cc": 1199,
        "power": "84 bhp",
        "torque": "113 Nm",
        "seating": 5,
        "features": ["Harman Audio", "Dual Airbags", "ABS", "Projector Headlamps", "Alloy Wheels"],
        "safety_rating": 4.5,
        "warranty_years": 3,
        "colors_available": ["White", "Grey", "Orange", "Blue", "Red"],
        "stock_status": "available"
    },
    
    # Sedans - Mid Segment
    {
        "vehicle_id": "CAR004",
        "name": "Honda City 5th Generation",
        "brand": "Honda",
        "model": "City",
        "year": 2024,
        "type": "sedan",
        "price": 1350000,
        "mileage": 18.4,
        "fuel_type": "petrol",
        "transmission": "cvt",
        "engine_cc": 1498,
        "power": "119 bhp",
        "torque": "145 Nm",
        "seating": 5,
        "features": ["Sunroof", "Honda Sensing", "8 Airbags", "LED Headlamps", "Wireless Charging", "Alexa Integration"],
        "safety_rating": 4.5,
        "warranty_years": 3,
        "colors_available": ["White", "Black", "Silver", "Blue", "Red"],
        "stock_status": "available"
    },
    {
        "vehicle_id": "CAR005",
        "name": "Hyundai Verna",
        "brand": "Hyundai",
        "model": "Verna",
        "year": 2024,
        "type": "sedan",
        "price": 1450000,
        "mileage": 17.8,
        "fuel_type": "petrol",
        "transmission": "automatic",
        "engine_cc": 1482,
        "power": "113 bhp",
        "torque": "144 Nm",
        "seating": 5,
        "features": ["Ventilated Seats", "Digital Cluster", "ADAS Level 2", "Sunroof", "Wireless Charging", "Bose Audio"],
        "safety_rating": 4.5,
        "warranty_years": 3,
        "colors_available": ["White", "Black", "Red", "Blue", "Grey"],
        "stock_status": "available"
    },
    {
        "vehicle_id": "CAR006",
        "name": "Volkswagen Virtus",
        "brand": "Volkswagen",
        "model": "Virtus",
        "year": 2024,
        "type": "sedan",
        "price": 1550000,
        "mileage": 18.1,
        "fuel_type": "petrol",
        "transmission": "automatic",
        "engine_cc": 1498,
        "power": "148 bhp",
        "torque": "250 Nm",
        "seating": 5,
        "features": ["Ventilated Seats", "Digital Cockpit", "6 Airbags", "ESC", "Cruise Control", "Wireless Charging"],
        "safety_rating": 5.0,
        "warranty_years": 4,
        "colors_available": ["White", "Black", "Red", "Blue", "Silver"],
        "stock_status": "available"
    },
    
    # SUVs - Compact
    {
        "vehicle_id": "CAR007",
        "name": "Tata Nexon",
        "brand": "Tata",
        "model": "Nexon",
        "year": 2024,
        "type": "compact_suv",
        "price": 1050000,
        "mileage": 17.4,
        "fuel_type": "petrol",
        "transmission": "manual",
        "engine_cc": 1199,
        "power": "118 bhp",
        "torque": "170 Nm",
        "seating": 5,
        "features": ["Sunroof", "JBL Audio", "6 Airbags", "ESP", "Drive Modes", "Connected Car"],
        "safety_rating": 5.0,
        "warranty_years": 3,
        "colors_available": ["White", "Red", "Blue", "Grey", "Orange"],
        "stock_status": "available"
    },
    {
        "vehicle_id": "CAR008",
        "name": "Hyundai Venue",
        "brand": "Hyundai",
        "model": "Venue",
        "year": 2024,
        "type": "compact_suv",
        "price": 1250000,
        "mileage": 18.1,
        "fuel_type": "petrol",
        "transmission": "dct",
        "engine_cc": 998,
        "power": "118 bhp",
        "torque": "172 Nm",
        "seating": 5,
        "features": ["Sunroof", "Blue Link", "6 Airbags", "Wireless Charging", "Digital Cluster", "Cruise Control"],
        "safety_rating": 4.0,
        "warranty_years": 3,
        "colors_available": ["White", "Black", "Red", "Blue", "Grey"],
        "stock_status": "available"
    },
    {
        "vehicle_id": "CAR009",
        "name": "Maruti Suzuki Brezza",
        "brand": "Maruti Suzuki",
        "model": "Brezza",
        "year": 2024,
        "type": "compact_suv",
        "price": 1100000,
        "mileage": 19.8,
        "fuel_type": "petrol",
        "transmission": "automatic",
        "engine_cc": 1462,
        "power": "103 bhp",
        "torque": "137 Nm",
        "seating": 5,
        "features": ["Sunroof", "360 Camera", "6 Airbags", "HUD", "Wireless Charging", "Connected Car"],
        "safety_rating": 4.0,
        "warranty_years": 2,
        "colors_available": ["White", "Silver", "Blue", "Red", "Black"],
        "stock_status": "available"
    },
    
    # SUVs - Premium
    {
        "vehicle_id": "CAR010",
        "name": "Mahindra Scorpio-N",
        "brand": "Mahindra",
        "model": "Scorpio-N",
        "year": 2024,
        "type": "suv",
        "price": 1850000,
        "mileage": 15.5,
        "fuel_type": "diesel",
        "transmission": "automatic",
        "engine_cc": 2184,
        "power": "172 bhp",
        "torque": "400 Nm",
        "seating": 7,
        "features": ["4WD", "Sony Audio", "Panoramic Sunroof", "6 Airbags", "ADAS", "Wireless Charging", "Cruise Control"],
        "safety_rating": 4.5,
        "warranty_years": 3,
        "colors_available": ["White", "Black", "Red", "Blue", "Grey"],
        "stock_status": "available"
    },
    {
        "vehicle_id": "CAR011",
        "name": "Hyundai Creta",
        "brand": "Hyundai",
        "model": "Creta",
        "year": 2024,
        "type": "suv",
        "price": 1650000,
        "mileage": 17.4,
        "fuel_type": "petrol",
        "transmission": "automatic",
        "engine_cc": 1497,
        "power": "158 bhp",
        "torque": "253 Nm",
        "seating": 5,
        "features": ["Sunroof", "Ventilated Seats", "ADAS Level 2", "Bose Audio", "Digital Cluster", "Wireless Charging"],
        "safety_rating": 4.5,
        "warranty_years": 3,
        "colors_available": ["White", "Black", "Red", "Blue", "Grey"],
        "stock_status": "available"
    },
    {
        "vehicle_id": "CAR012",
        "name": "MG Hector",
        "brand": "MG",
        "model": "Hector",
        "year": 2024,
        "type": "suv",
        "price": 1750000,
        "mileage": 14.8,
        "fuel_type": "petrol",
        "transmission": "automatic",
        "engine_cc": 1451,
        "power": "141 bhp",
        "torque": "250 Nm",
        "seating": 5,
        "features": ["Panoramic Sunroof", "Infinity Audio", "ADAS", "Connected Car", "Wireless Charging", "Digital Cluster"],
        "safety_rating": 4.0,
        "warranty_years": 5,
        "colors_available": ["White", "Black", "Red", "Blue", "Grey"],
        "stock_status": "available"
    },
    
    # Luxury Segment
    {
        "vehicle_id": "CAR013",
        "name": "Mercedes-Benz C-Class",
        "brand": "Mercedes-Benz",
        "model": "C-Class",
        "year": 2024,
        "type": "luxury_sedan",
        "price": 6200000,
        "mileage": 15.2,
        "fuel_type": "petrol",
        "transmission": "automatic",
        "engine_cc": 1496,
        "power": "201 bhp",
        "torque": "300 Nm",
        "seating": 5,
        "features": ["Burmester Audio", "9 Airbags", "ADAS Level 3", "Digital Cockpit", "Ambient Lighting", "Panoramic Sunroof", "4MATIC AWD"],
        "safety_rating": 5.0,
        "warranty_years": 3,
        "colors_available": ["White", "Black", "Silver", "Blue", "Red"],
        "stock_status": "limited"
    },
    {
        "vehicle_id": "CAR014",
        "name": "BMW 3 Series",
        "brand": "BMW",
        "model": "3 Series",
        "year": 2024,
        "type": "luxury_sedan",
        "price": 6000000,
        "mileage": 16.1,
        "fuel_type": "petrol",
        "transmission": "automatic",
        "engine_cc": 1998,
        "power": "255 bhp",
        "torque": "400 Nm",
        "seating": 5,
        "features": ["Harman Kardon", "8 Airbags", "Driving Assistant", "Head-Up Display", "Gesture Control", "Wireless Charging"],
        "safety_rating": 5.0,
        "warranty_years": 2,
        "colors_available": ["White", "Black", "Blue", "Grey", "Red"],
        "stock_status": "available"
    },
    
    # Electric Vehicles
    {
        "vehicle_id": "CAR015",
        "name": "Tata Nexon EV",
        "brand": "Tata",
        "model": "Nexon EV",
        "year": 2024,
        "type": "electric_suv",
        "price": 1850000,
        "mileage": 0,  # Electric - range in km
        "fuel_type": "electric",
        "transmission": "automatic",
        "engine_cc": 0,
        "power": "143 bhp",
        "torque": "250 Nm",
        "seating": 5,
        "features": ["Range 465km", "Fast Charging", "Connected Car", "JBL Audio", "6 Airbags", "Regenerative Braking"],
        "safety_rating": 5.0,
        "warranty_years": 8,
        "colors_available": ["White", "Blue", "Red", "Grey", "Teal"],
        "stock_status": "available"
    }
]


def get_all_vehicles() -> List[VehicleSpecs]:
    """Get all vehicles from inventory as VehicleSpecs objects."""
    return [VehicleSpecs(**car) for car in CAR_INVENTORY]


def get_vehicle_by_id(vehicle_id: str) -> VehicleSpecs:
    """Get specific vehicle by ID."""
    for car in CAR_INVENTORY:
        if car["vehicle_id"] == vehicle_id:
            return VehicleSpecs(**car)
    return None


def search_inventory(
    budget_max: float = None,
    vehicle_type: str = None,
    fuel_type: str = None,
    seating_min: int = None,
    brand: str = None
) -> List[VehicleSpecs]:
    """Search inventory with filters."""
    results = []
    
    for car in CAR_INVENTORY:
        # Apply filters
        if budget_max and car["price"] > budget_max:
            continue
        
        if vehicle_type and car["type"] != vehicle_type:
            continue
        
        if fuel_type and car["fuel_type"] != fuel_type:
            continue
        
        if seating_min and car["seating"] < seating_min:
            continue
        
        if brand and car["brand"].lower() != brand.lower():
            continue
        
        results.append(VehicleSpecs(**car))
    
    return results


def get_vehicle_types() -> List[str]:
    """Get unique vehicle types."""
    return list(set(car["type"] for car in CAR_INVENTORY))


def get_brands() -> List[str]:
    """Get unique brands."""
    return list(set(car["brand"] for car in CAR_INVENTORY))


def get_price_range() -> Dict[str, float]:
    """Get min and max prices."""
    prices = [car["price"] for car in CAR_INVENTORY]
    return {"min": min(prices), "max": max(prices)}