# Phone Number Information 
This Python script provides a graphical user interface (GUI) using tkinter to retrieve information about a phone number entered by the user. The script uses the phonenumbers library to validate the phone number and display details such as the region, service provider, and country.

## Features
- Input: Enter a phone number with the country code (+xx xxxxxxxxx).
- Validation: Checks if the entered phone number is valid.
- Information Retrieval: Displays the region, service provider, and country associated with the phone number.
- Error Handling: Manages errors for invalid phone number formats.


## Requirements
```bash
- Python 3.x
- phonenumbers library: Install using pip install phonenumbers
```
## Usage
- Run the script (python phone_number_info_gui.py).
- Enter a phone number with the country code (+xx xxxxxxxxx) into the entry field.
- Click the "Get Info" button to retrieve and display information about the phone number.
- The information is displayed in a message box, including the region, service provider, and country.

## Example
```vim
- Enter: '+1 1234567890'
- Click "Get Info"
- Output:
      - Copy code
      - Phone Number belongs to region: America/New_York
      - Service Provider: Verizon Wireless
      - Phone number belongs to country: United States
```
  ## Notes
Ensure you have an active internet connection for accurate geolocation and carrier information retrieval.
Customize the GUI further by adjusting the styling, layout, and functionality to suit your preferences or specific application requirements.
