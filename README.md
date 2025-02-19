# Phone Number Info

## Overview
This Python script provides a graphical user interface (GUI) using **tkinter** to retrieve information about a phone number entered by the user. The script utilizes the **phonenumbers** library to validate the phone number and display details such as the region, service provider, and country.

## Features
- **Input**: Enter a phone number with the country code (e.g., +xx xxxxxxxxx).
- **Validation**: Checks if the entered phone number is valid.
- **Information Retrieval**: Displays the region, service provider, and country associated with the phone number.
- **Error Handling**: Manages errors for invalid phone number formats.

## Technologies Used
- **Python**: The programming language used for developing the app.
- **tkinter**: Used for creating the graphical user interface (GUI).
- **phonenumbers**: A Python library for parsing, formatting, and validating international phone numbers.

## Requirements
- **Python 3.x**
- **phonenumbers library**: Install it using pip:
    ```bash
    pip install phonenumbers
    ```
- **tkinter library**: Usually comes pre-installed with Python.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/SoubhLance/Phone_Number_Info.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Phone_Number_Info
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Run the script:
    ```bash
    python phone_number_info_gui.py
    ```
2. Enter a phone number with the country code (e.g., +xx xxxxxxxxx) into the entry field.
3. Click the "Get Info" button to retrieve and display information about the phone number.
4. The information is displayed in a message box, including the region, service provider, and country.

## Example
- **Input**: `+1 1234567890`
- **Action**: Click the "Get Info" button
- **Output**:
    ```
    Phone Number belongs to region: America/New_York
    Service Provider: Verizon Wireless
    Phone number belongs to country: United States
    ```

## Notes
- Ensure you have an active internet connection for accurate geolocation and carrier information retrieval.
- You can customize the GUI further by adjusting the styling, layout, and functionality to suit your preferences or specific application requirements.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support
For any issues, questions, or suggestions, feel free to reach out:

- Email: [studysadhu2022@gmail.com](mailto:studysadhu2022@gmail.com)
- GitHub: [SoubhLance](https://github.com/SoubhLance)

If you encounter any bugs or have feature requests, please open an issue in the [GitHub repository](https://github.com/SoubhLance/Phone_Number_Info/issues).

