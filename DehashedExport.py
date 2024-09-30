import requests
import csv
import base64
from colorama import Fore, Style, init
import os

# Initialize colorama
init(autoreset=True)

# Function to export results to a CSV file
def export_to_csv(data, filename):
    if len(data) == 0:
        print("No data to export.")
        return
    
    # Write data to CSV
    keys = data[0].keys()  # Get headers from the first result
    with open(filename, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)
    print(f"Data exported to {filename}")

# Function to read and parse emails from a file
def read_emails_from_file(file_path):
    if not os.path.isfile(file_path):
        print(f"File '{file_path}' does not exist.")
        return []
    
    with open(file_path, 'r') as file:
        contents = file.read()
    emails = [email.strip() for email in contents.split(',') if email.strip()]
    return emails

# Prompt user for email, API key, and input (domain, single email, list of emails, or file)
email = input(Fore.YELLOW + "Please enter the email associated with your Dehashed API key: ")
api_key = input(Fore.YELLOW + "Please enter your Dehashed API key: ")

# Prompt for the type of input
input_type = input(Fore.YELLOW + "Enter your input (single domain, single email, list of emails separated by commas, or path to a text file of comma-separated values): ")

# Check if the input is a file, a domain, or emails
if os.path.isfile(input_type):
    # If a file is provided, read emails from the file
    email_list = read_emails_from_file(input_type)
    if not email_list:
        print("No valid emails found in the file.")
        exit()
else:
    # Otherwise, treat it as a single input or a list of emails
    email_list = [item.strip() for item in input_type.split(',') if item.strip()]

# Prompt for the desired filename for the CSV export
export_filename = input(Fore.YELLOW + "Enter the desired name for the exported CSV file (without extension): ") + ".csv"

# Encode the email and API key for Basic Authentication
auth_string = f'{email}:{api_key}'
auth_encoded = base64.b64encode(auth_string.encode('utf-8')).decode('utf-8')

# API Endpoint for searching
url = 'https://api.dehashed.com/search'
headers = {
    'Accept': 'application/json',
    'Authorization': f'Basic {auth_encoded}'
}

# Initialize an empty list to collect all results
all_results = []

# Loop through each email or domain in the input
for query in email_list:
    print(f"Processing query: {query}")
    # Params with pagination (starting at page 1)
    params = {'query': query, 'page': 1}

    # Loop through paginated results for each query
    while True:
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            results = response.json()

            # Check if there are any entries in the result
            if 'entries' in results and results['entries']:
                all_results.extend(results['entries'])  # Append results to all_results
                print(f"Page {params['page']} processed for {query}, {len(results['entries'])} entries retrieved.")
            else:
                print(f"No more entries found for {query}.")
                break

            # Increment to the next page
            params['page'] += 1
        else:
            print(f"Failed to retrieve data for {query}. Status code: {response.status_code}, {response.text}")
            break

# Export the collected results to a CSV file
if all_results:
    export_to_csv(all_results, export_filename)
else:
    print("No data found to export.")

# Success messages at the end of script execution
print(Fore.GREEN + "Wow...that was easy!\n")
print(Fore.GREEN + "Thank you for using the DehashedExport script, used to dump a list of emails by domain from Dehashed.com.\n")
print(Fore.GREEN + "You can buy me a coffee if you like this or send complaints and improvements to ChiefCyberPapa@proton.me.")
