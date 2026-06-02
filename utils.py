def calculate_discount(price: float, discount_percent: int) -> float:
    """Calculates the final price after a discount."""
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Discount must be between 0 and 100")
    if price < 0:
        raise ValueError("Price cannot be negative")
    
    discount_amount = price * (discount_percent / 100)
    return round(price - discount_amount, 2)


def is_strong_password(password: str) -> bool:
    """Checks if a password is at least 8 chars long and has a number."""
    if not password:
        return False
    
    has_length = len(password) >= 8
    has_number = any(char.isdigit() for char in password)
    
    return has_length and has_number


def chunk_list(input_list: list, chunk_size: int) -> list:
    """Splits a list into smaller lists of the specified size."""
    if chunk_size <= 0:
        raise ValueError("Chunk size must be greater than 0")
    if not input_list:
        return []
        
    return [input_list[i:i + chunk_size] for i in range(0, len(input_list), chunk_size)]



import os
from datetime import datetime

# --- Global State for Testing ---
system_status = "offline"

def boot_system() -> str:
    """Changes the global system status to online."""
    global system_status
    
    if system_status == "online":
        raise RuntimeError("System is already running.")
    
    system_status = "online"
    return "System successfully booted."


def get_daily_greeting() -> str:
    """Returns a greeting based on the current server time."""
    current_hour = datetime.now().hour
    
    if current_hour < 12:
        return "Good morning!"
    elif current_hour < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"


def is_production_mode() -> bool:
    """Checks the server's environment variables to see if it is in production."""
    env_setting = os.environ.get("SERVER_ENV", "development")
    
    return env_setting.lower() == "production"