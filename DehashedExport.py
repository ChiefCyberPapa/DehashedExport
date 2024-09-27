import requests
import csv
import base64
from colorama import Fore, Style, init

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

# Prompt user for email, API key, and domain to search
email = input(Fore.YELLOW + "Please enter the email associated with your Dehashed API key: ")
api_key = input(Fore.YELLOW + "Please enter your Dehashed API key: ")
domain_to_search = input(Fore.YELLOW + "Please enter the email domain to search (e.g., example.com): ")

# Encode the email and API key for Basic Authentication
auth_string = f'{email}:{api_key}'
auth_encoded = base64.b64encode(auth_string.encode('utf-8')).decode('utf-8')

# API Endpoint for searching
url = 'https://api.dehashed.com/search'
headers = {
    'Accept': 'application/json',
    'Authorization': f'Basic {auth_encoded}'
}

# Params with pagination (starting at page 1)
params = {'query': f'domain:{domain_to_search}', 'page': 1}

# Initialize an empty list to collect all results
all_results = []

# Loop through paginated results
while True:
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        results = response.json()

        # Check if there are any entries in the result
        if 'entries' in results and results['entries']:
            all_results.extend(results['entries'])  # Append results to all_results
            print(f"Page {params['page']} processed, {len(results['entries'])} entries retrieved.")
        else:
            print("No more entries found.")
            break

        # Increment to the next page
        params['page'] += 1
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}, {response.text}")
        break

# Export the collected results to a CSV file
if all_results:
    export_to_csv(all_results, f'dehashed_results_{domain_to_search}.csv')
else:
    print("No data found to export.")

# Success messages at the end of script execution
print(Fore.GREEN + "Wow...that was easy!\n")
print(Fore.GREEN + "Thank you for using the DehashedExport script, used to dump a list of emails by domain from Dehashed.com.\n")
print(Fore.GREEN + "You can buy me a coffee if you like this or send complaints and improvements to ChiefCyberPapa@proton.me.")
