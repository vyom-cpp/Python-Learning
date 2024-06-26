import time

# Set friend's birthday date and time (replace with actual date/time)
target_date = "2024-05-06 11:35:00"

# Get current time
current_time = time.time()

# Convert target date to seconds since epoch
target_time = time.mktime(time.strptime(target_date, "%Y-%m-%d %H:%M:%S"))

# Calculate difference in seconds
remaining_seconds = int(target_time - current_time)

# Loop until countdown reaches 0
while remaining_seconds > 0:
  # Calculate minutes remaining
  minutes_left = int(remaining_seconds / 60)

  # Print countdown message (simulates WhatsApp message)
  print(f"{minutes_left} minutes left" if minutes_left > 1 else "Happy Birthday Bro!")

  # Wait for 1 minute before next iteration
  time.sleep(60)

  # Update remaining seconds
  remaining_seconds -= 60