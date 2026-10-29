
import sys

from Modules.ip_lookup import get_ip_location

from Modules.username import check_username

from Modules.exif_tool import extract_exif, make_map


BANNER = r"""
		 ████████╗██████╗   █████╗   ██████╗ ███████╗██╗  ██╗
		 ╚══██╔══╝██╔══██╗ ██╔══██╗ ██╔════╝ ██╔════╝╚██╗██╔╝
		    ██║   ██████╔╝ ███████║ ██║      █████╗   ╚███╔╝ 
		    ██║   ██╔══██╗ ██╔══██╗ ██║      ██╔══╝   ██╔██╗ 
		    ██║   ██║  ██║ ██║  ██║ ╚██████╗ ███████╗██╔╝ ██╗
		    ╚═╝   ╚═╝  ╚═╝ ╚═╝  ╚═╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝

			🕵️‍♂️  TraceX - OSINT Exposure Tool 🕵️‍♂️
				Developed by: Ihlas


===================================================
"""

def main_menu():
    while True:
        print(BANNER)
        print(" [1] 🌐 IP Address Tracker")
        print(" [2] 👤 Username Tracker")
        print(" [3] 📸 Photo EXIF / GPS Extractor")
        print(" [0] 🚪 Exit")
        print("===================================================")
        
        choice = input("\n🎯 Choose an option (0-3): ").strip()
        
        if choice == "1":
            target_ip = input("\n🎯 Enter Target's IP Address (e.g., 8.8.8.8): ").strip()
            get_ip_location(target_ip)
            input("\nPress Enter to return to Menu...")
            
        elif choice == "2":
            target_user = input("\n🎯 Enter Target Username (e.g., ihl_a_s): ").strip()
            check_username(target_user)
            input("\nPress Enter to return to Menu...")
            
        elif choice == "3":
            img_path = input("\n🎯 Enter Image Path (e.g., Samples/test.jpg): ").strip().strip('"')
            result = extract_exif(img_path)
            
            if result:
                print("\n-----------------------------------")
                print("📱 Device Brand :", result.get("Make", "N/A"))
                print("📷 Device Model :", result.get("Model", "N/A"))
                print("💻 Software/OS  :", result.get("Software", "N/A"))
                print("⏰ Taken Time   :", result.get("DateTime", "N/A"))
                print("📍 GPS Coords   :", result.get("GPS", "N/A"))
                print("-----------------------------------")
                
                if result.get("GPS"):
                    lat, lon = result["GPS"]
                    out = make_map(lat, lon, label=f"Location: {img_path}")
                    print(f"\n🗺️ Map saved to {out}. Open it in your browser!")
                else:
                    print("\n⚠️ No GPS data found in this image.")
            
            input("\nPress Enter to return to Menu...")
            
        elif choice == "0":
            print("\n👋 Bye! See you on the next cybersecurity mission! 🕵️‍♂️🚀\n")
            sys.exit()
            
        else:
            print("\n❌ Invalid choice! Please select 0, 1, 2, or 3.")
            input("\nPress Enter to try again...")

if __name__ == "__main__":
    main_menu()
