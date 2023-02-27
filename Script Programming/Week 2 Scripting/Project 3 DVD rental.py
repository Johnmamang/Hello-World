# The number of new videos rented
new_videos = int(input("Enter the number of new videos rented: "))

# The number of old videos rented
old_videos = int(input("Enter the number of old videos rented: "))

# Calculate the total cost for new videos
new_video_cost = new_videos * 3.00

# Calculate the total cost for old videos
old_video_cost = old_videos * 2.00

# Calculate the total cost for all videos
total_cost = new_video_cost + old_video_cost

# Output the total cost
print("Total cost: $" + str(total_cost))
