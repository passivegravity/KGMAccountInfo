import requests
import json

def login(username, password):
    # Create a session
    session = requests.Session()

    # Define the login URL
    login_url = "https://www.kogama.com/auth/login/"

    # Set the headers for the request
    headers = {
        "Content-Type": "application/json; charset=UTF-8"
    }

    # Prepare the login data
    login_data = {
        "username": username,
        "password": password
    }

    # Convert the login data to JSON
    login_data_json = json.dumps(login_data)

    try:
        # Send the POST request to the login URL
        response = session.post(login_url, headers=headers, data=login_data_json)

        # Check the response status code
        if response.status_code == 200:
            # Login successful
            print("Login successful!\n")

            # Print the response content in a more readable format
            print("Response Content:")
            response_content = json.loads(response.content)
            print(json.dumps(response_content, indent=4))

        else:
            # Login failed
            print("Login failed. Status code:", response.status_code)
    
    except requests.exceptions.RequestException as e:
        # An error occurred during the request
        print("An error occurred:", str(e))


# Prompt user to input username and password
username = input("Enter your username: ")
password = input("Enter your password: ")

# Call the login function
login(username, password)
