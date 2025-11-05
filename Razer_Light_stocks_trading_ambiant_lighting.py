import time
import random
import razer

# Initialize Razer Chroma SDK
chroma = razer_chroma_sdk.ChromaApp("Stock Lighting")

def set_chroma_color(color):
    """
    Applies the given color to all Razer Chroma devices.
    Color is a tuple (R, G, B) with values 0-255.
    """
    chroma.set_all_devices(color)
    print(f"[Chroma] Set color: {color}")

def gradually_change_color(start_color, end_color, duration=2.0, steps=50):
    """
    Gradually transitions the light color from start_color to end_color over 'duration' seconds.
    """
    step_delay = duration / steps
    delta = tuple((end - start) / steps for start, end in zip(start_color, end_color))
    current_color = list(start_color)
    
    for _ in range(steps):
        current_color = [c + d for c, d in zip(current_color, delta)]
        new_color = tuple(int(max(0, min(255, x))) for x in current_color)
        set_chroma_color(new_color)
        time.sleep(step_delay)
    
    set_chroma_color(end_color)

def get_market_data(symbol):
    """ Simulates fetching stock price from Robinhood/Webull (replace with real API). """
    return 100 + random.uniform(-5, 5)

def get_account_data():
    """ Simulates retrieving trade details (replace with real API calls). """
    entry_price = 100.0
    return {
        "entry_price": entry_price,
        "direction": "put",
        "rejection_line": 105.0,
        "stop_loss": entry_price * 0.90,
        "symbol": "AAPL",
    }

def determine_color(current_price, account_data):
    """
    Determines lighting color based on stock price and trade position.
    """
    entry = account_data["entry_price"]
    stop = account_data["stop_loss"]
    rejection = account_data["rejection_line"]
    trade = account_data["direction"].lower()

    green = (0, 255, 0)
    red   = (255, 0, 0)

    if trade == "put":
        if current_price >= rejection or current_price > entry:
            return red
        if current_price <= stop:
            return red
        return green

    elif trade == "call":
        if current_price <= rejection or current_price < entry:
            return red
        if current_price <= stop:
            return red
        return green

    return (255, 255, 255)

def main():
    print("=== Razer Chroma Stock Lighting ===")
    trade_type = input("Enter trade type (call/put): ").strip().lower()
    if trade_type not in ("call", "put"):
        trade_type = "put"

    account_data = get_account_data()
    account_data["direction"] = trade_type
    symbol = account_data["symbol"]

    current_color = (255, 255, 255)
    set_chroma_color(current_color)

    print(f"Monitoring {symbol} for a {trade_type} trade...")
    try:
        while True:
            current_price = get_market_data(symbol)
            target_color = determine_color(current_price, account_data)
            if target_color != current_color:
                print(f"[Market] {symbol} price: {current_price:.2f} → updating color.")
                gradually_change_color(current_color, target_color, duration=2)
                current_color = target_color
            else:
                print(f"[Market] {symbol} price: {current_price:.2f} (no change)")
            time.sleep(5)
    except KeyboardInterrupt:
        print("Exiting Chroma stock lighting.")
        chroma.cleanup()

if __name__ == "__main__":
    main()


