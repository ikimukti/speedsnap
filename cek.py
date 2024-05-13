import subprocess
import json
import datetime

def run_speedtest(server_id):
    # Run the speedtest-cli command for a specific server ID and capture the output
    speedtest_output = subprocess.run(['speedtest-cli', '--json', '--server', str(server_id)], capture_output=True, text=True)
    
    # Check if the command ran successfully
    if speedtest_output.returncode == 0:
        # Parse the JSON output and extract download and upload speeds
        speedtest_data = json.loads(speedtest_output.stdout)
        download_speed = speedtest_data['download'] / 1_000_000  # Convert to Mbps
        upload_speed = speedtest_data['upload'] / 1_000_000  # Convert to Mbps
        return download_speed, upload_speed
    else:
        print(f"Failed to run speedtest-cli for server ID: {server_id}")
        return None, None

def save_speedtest_results(speedtest_results):
    # Generate a timestamp for the filename
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"speedtest_results_{timestamp}.json"
    
    # Save the speed test results to a JSON file
    with open(filename, 'w') as file:
        json.dump(speedtest_results, file, indent=4)

def save_server_list(server_list):
    # Generate a timestamp for the filename
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"server_list_{timestamp}.json"
    
    # Save the server list to a JSON file
    with open(filename, 'w') as file:
        json.dump(server_list, file, indent=4)


def get_server_list():
    # Run the speedtest-cli command to get the server list in JSON format
    speedtest_output = subprocess.run(['speedtest-cli', '--list'], capture_output=True, text=True)
    
    # Check if the command ran successfully
    if speedtest_output.returncode == 0:
        # Print out the raw output for debugging
        print("Raw Output:", speedtest_output.stdout)
        
        # Parse the raw output to extract server information
        server_list = []
        lines = speedtest_output.stdout.strip().split('\n')
        for line in lines:
            parts = line.strip().split(') ')
            if len(parts) >= 2:
                server_id = parts[0].strip()
                server_info = parts[1].strip()
                server_list.append({'id': server_id, 'info': server_info})
        
        return server_list
    else:
        print("Failed to get server list from speedtest-cli")
        return None

# Get the list of speed test servers
server_list = get_server_list()

# Perform speed tests against each server and collect the results
speedtest_results = []
# Memeriksa apakah daftar server berhasil didapatkan dan mencetak hasilnya
if server_list:
    print("Server List:")
    for server in server_list:
        print("Server ID:", server['id'])
        print("Server Name:", server['info'])
        print()
        
        # Run speed test for the current server
        download_speed, upload_speed = run_speedtest(server['id'])

        # Check if speed test was successful and collect the results
        if download_speed is not None and upload_speed is not None:
            speedtest_results.append({
                'server_id': server['id'],
                'server_name': server['info'],
                'download_speed': download_speed,
                'upload_speed': upload_speed
            })
        else:
            print(f"Failed to perform speed test for server ID: {server['id']}")
    # Add error handling here if needed


    # Save the speed test results to a JSON file
    if speedtest_results:
        save_speedtest_results(speedtest_results)
else:
    print("Failed to get server list.")
