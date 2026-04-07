import time
import urllib.request

# Example of IO bound task

# List of urls for download
urls = [
    'http://www.python.org',
    'http://www.python.org/about/',
    'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
    'http://www.python.org/doc/',
    'http://www.python.org/download/',
    'http://www.python.org/getit/',
    'http://www.python.org/community/',
    'https://wiki.python.org/moin/',
]

start_time = time.time()

print("Example of IO bound task")

# Download each url
for url in urls:
    print(f"Download {url}")    # Print message about downloading URL
    response = urllib.request.urlopen(url)
    print(f"Downloaded {url}")  # Print message that downloading of url is finished

end_time = time.time()
print(f"Downloaded {len(urls)} URL during {end_time - start_time} seconds") # Print total time of downloading
print()

# Example of CPU bound task

# Function for calculating factorial
def factorial(n):
    if n ==0:
        return 1
    else:
        return n * factorial(n-1)
    
start_time = time.time()

print("Example of CPU bound task")

# Calculation of factorial for each number from 1 to 20
for i in range (1, 21):
    print(f"Factorial {i} = {factorial(i)}")    # Prinf factorial of number

end_time = time.time()
print(f"Total time of calculation of 20 factorials is {end_time - start_time} seconds")
