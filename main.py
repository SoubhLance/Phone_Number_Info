import tkinter as tk
from tkinter import messagebox
import phonenumbers
from phonenumbers import carrier, geocoder, timezone

def get_phone_info():
    try:
        mobile_no = phone_entry.get().strip()  # Get phone number from entry widget and strip any extra spaces
        parsed_mobile_no = phonenumbers.parse(mobile_no)
        
        if phonenumbers.is_valid_number(parsed_mobile_no):
            # Prepare information to display
            region_info = ', '.join(timezone.time_zones_for_number(parsed_mobile_no))
            provider_info = carrier.name_for_number(parsed_mobile_no, "en")
            country_info = geocoder.description_for_number(parsed_mobile_no, "en")
            
            # Display information in message box
            info_str = f"Phone Number belongs to region: {region_info}\n" \
                       f"Service Provider: {provider_info}\n" \
                       f"Phone number belongs to country: {country_info}"
            messagebox.showinfo("Phone Number Information", info_str)
        else:
            messagebox.showwarning("Invalid Number", "Please enter a valid mobile number.")
    except phonenumbers.phonenumberutil.NumberParseException:
        messagebox.showerror("Error", "Invalid phone number format. Please enter a valid phone number.")

# Create the main tkinter window
root = tk.Tk()
root.title("Phone Number Information")
root.geometry("400x250")  # Set initial window size

# Styling
root.configure(background='#f0f0f0')  # Set background color

# Main Frame
main_frame = tk.Frame(root, bg='#f0f0f0')
main_frame.pack(fill=tk.BOTH, expand=True)

# Label and Entry for phone number input
phone_label = tk.Label(main_frame, text="Enter Phone number with country code (+xx xxxxxxxxx):", bg='#f0f0f0', font=('Helvetica', 12))
phone_label.pack(pady=10)
phone_entry = tk.Entry(main_frame, width=30, font=('Helvetica', 12))
phone_entry.pack()

# Button to trigger phone number information retrieval
info_button = tk.Button(main_frame, text="Get Info", command=get_phone_info, font=('Helvetica', 12), bg='#4caf50', fg='white', relief=tk.FLAT)
info_button.pack(pady=10)

# Centering the window
window_width = root.winfo_reqwidth()
window_height = root.winfo_reqheight()
position_right = int(root.winfo_screenwidth() / 2 - window_width / 2)
position_down = int(root.winfo_screenheight() / 2 - window_height / 2)
root.geometry(f'+{position_right}+{position_down}')

# Start the tkinter main loop
root.mainloop()
