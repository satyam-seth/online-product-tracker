import re


def parse_price_with_currency(price_str: str) -> (float, str):  # type: ignore
    """
    Parse a price string to a float, handling multi-character currency symbols and commas.

    :param price_str: The price string to parse (e.g., "$6,999.99", "6,999.99", "€6,999.99", "R$6,999.99")
    :return: A tuple (parsed price as float, currency symbol)
    """
    # Extract the currency symbol or code (one or more non-digit characters at the beginning)
    currency_match = re.match(r"^[^\d]*(\D+)", price_str)

    # Default currency is empty if no symbol is found
    currency = currency_match.group(1).strip() if currency_match else ""

    # Remove currency symbol and non-numeric characters (except for commas and period)
    price_cleaned = re.sub(
        r"[^\d.,-]", "", price_str
    )  # Keep digits, commas, and period

    # Remove commas (thousands separators)
    price_cleaned = price_cleaned.replace(",", "")

    # Convert to float
    return float(price_cleaned), currency
