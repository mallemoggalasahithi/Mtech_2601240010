Question 1: PEP 484-Style Type Hints for a Transaction Function

#1. Algorithm
Define Function Signature: Create a function named process_transaction taking explicit type hints: account_id (string), amount (float), and is_deposit (boolean), returning a string.

Validate Input: Check if the transaction amount is valid (greater than zero). If not, raise a ValueError.

Process Transaction: Format the message based on whether it is a deposit or a withdrawal.

Return Result: Return the transaction success message.

#2. Pseudocode
Plaintext
FUNCTION process_transaction(account_id: str, amount: float, is_deposit: bool) -> str
    IF amount <= 0 THEN
        RAISE Error("Amount must be greater than zero")
    END IF
    
    IF is_deposit THEN
        SET action = "deposited into"
    ELSE
        SET action = "withdrawn from"
    END IF
    
    RETURN confirmation_message
END FUNCTION
