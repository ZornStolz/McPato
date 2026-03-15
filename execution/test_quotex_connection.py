import asyncio
import os
from dotenv import load_dotenv
from api_quotex import AsyncQuotexClient, get_ssid

# Load environment variables from .env file
load_dotenv()

async def main():
    email = os.getenv("QUOTEX_EMAIL")
    password = os.getenv("QUOTEX_PASSWORD")
    
    if not email or not password:
        print("[-] Error: QUOTEX_EMAIL or QUOTEX_PASSWORD not found in .env")
        return

    print(f"[*] Starting connection test for {email}...")
    
    try:
        # 1) Get / refresh SSID via Playwright helper (opens browser on first run)
        print("[*] Acquiring SSID via Playwright...")
        ok, session_data = await get_ssid(email=email, password=password)
        
        if not ok:
            print("[-] Error: Could not acquire session data.")
            return
            
        demo_ssid = session_data.get("ssid")
        if not demo_ssid:
            print("[-] Error: Could not find SSID in session data.")
            return
            
        print(f"[+] Demo SSID successfully acquired: {demo_ssid[:20]}...")

        # 2) Connect
        print("[*] Connecting WebSocket client...")
        client = AsyncQuotexClient(ssid=demo_ssid, is_demo=True)
        
        if not await client.connect():
            print("[-] Error: Failed to connect to Quotex WebSocket.")
            return
            
        print("[+] WebSocket successfully connected.")

        # 3) Check Balance
        print("[*] Retrieving balance...")
        bal = await client.get_balance()
        print(f"[+] Account Balance: {bal.balance} {bal.currency}")

        # 4) Disconnect
        print("[*] Disconnecting...")
        await client.disconnect()
        print("[+] Connection test complete!")
        
    except Exception as e:
        print(f"[-] An exception occurred during the connection test: {e}")

if __name__ == "__main__":
    asyncio.run(main())
