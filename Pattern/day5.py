import random

# List of students
students = [
    "Alex Hembya", "Anubhab Paudel", "Anusha Bajgain", "Arpita Chalise", "Ayush Adhikari",
    "Bimun Acharya", "Dhirendra Yadav", "Indrajeet Mahara", "Kabindra Shah", "Kaushlendra Yadav",
    "Khagendra Kumar Chadhary", "Manish Rai", "Mohd Afzal Rain", "Mohit Basnet", "Nasna Maharjan",
    "Prabin Kiran Snehi", "Puja Shrestha", "Rabin Karki", "Raghbendra Prasad Yadav", "Rajeep Paudel",
    "Rekha Adhikari", "Risan Basnet", "Rupesh Karki", "Sakriya Lama", "Samana Pote",
    "Samik Poudel", "Simran Dev", "Smriti Khadka", "Sudip Khadka", "Sujal Mandal",
    "Suman Giri", "Suprim Shrestha", "Surakshya Poudel", "Aschitra Shova Yadav", "Abishek Siwakoti",
    "Amit Maharjan", "Ashu Kumar Shrestha", "Bristi Shahi", "Dipesh Chaudhary", "Kumar Shrestha",
    "Nitesh B.K", "Nitesh Gurung", "Rohit Adhikari", "Sulav Budhathoki", "Surendra Basnet",
    "Yaman Shrestha", "Yogendra Sah"
]

# Shuffle the list of students randomly
random.shuffle(students)

# Divide students into groups of 12
num_groups = len(students) // 12
remaining_students = len(students) % 12

# Print the random groups
for i in range(num_groups):
    group = students[i * 12: (i + 1) * 12]
    print(f"Group {i + 1}:")
    for student in group:
        print(student)
    print()

# If there are remaining students, create an additional group
if remaining_students > 0:
    group = students[num_groups * 12:]
    print(f"Group {num_groups + 1} (Additional group):")
    for student in group:
        print(student)
