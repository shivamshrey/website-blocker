import logging
import time

from datetime import datetime as dt

logging.basicConfig(level=logging.INFO)

host_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_block_list = ['www.facebook.com', 'www.9gag.com', 'www.netflix.com']

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) <= dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17):
        with open(host_path, 'r+') as file:
            content = file.read()
            
            # Add all sites to be blocked to the 'hosts' file
            for site in website_block_list:
                if site not in content:
                    file.write("\n" + redirect + "\t" + site)
        logging.info("All sites blocked during working hours")
    else:
        with open(host_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            
            # Read 'hosts' file line by line
            for line in content:
                # Check for presence of each site in each line of 'hosts' file
                # and create a list of boolean values based on site's presence
                # True -> site present in that line
                # False -> site not present in that line
                if not any([site in line for site in website_block_list]):
                    # Write the line back to the file if no site is present
                    file.write(line)
                # Truncate all the contents from the point a site is found
                file.truncate()

        logging.info("All sites unblocked during non-working hours")
    time.sleep(5.0)
