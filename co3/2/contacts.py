def process_contact(contact: str | int) -> str:
    """
    Processes a customer's primary contact using PEP 604 union type syntax (str | int).
    """
    if isinstance(contact, int):
        return f"Processed primary contact as a Mobile Number (Integer): {contact}"
    elif "@" in contact:
        return f"Processed primary contact as an Email Address: {contact}"
    else:
        return f"Processed primary contact as a Mobile Number (String): {contact}"

# --- Example Usage ---
if __name__ == "__main__":
    # Example 1: Providing an email address (string)
    print(process_contact("customer@example.com"))
    
    # Example 2: Providing a mobile number (integer)
    print(process_contact(9876543210))
    
    # Example 3: Providing a mobile number (string format)
    print(process_contact("+1-555-0199"))
