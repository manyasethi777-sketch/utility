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