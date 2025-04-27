
# ======== Alice's Section ========

# Initialize a list of prime numbers
prime_numbers = [2, 3, 5, 7, 11]

# Function to check if a number is prime
def is_prime(n):
    """Check if n is a prime number."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Pseudocode: Generate primes up to a number
# FOR each number in range:
#     IF number is prime:
#         Add to prime list


# ======== Bob's Section ========

# Dictionary to store user profiles
user_profiles = {
    "alice": {"age": 25, "country": "USA"},
    "bob": {"age": 30, "country": "Canada"},
}

# Function to display all user profiles
def display_profiles(profiles):
    """Prints out all user profiles."""
    for name, info in profiles.items():
        print(f"{name.title()}: Age {info['age']}, Country {info['country']}")

# Pseudocode: Loop through dictionary and print user info


# ======== Charlie's Section ========

# A simple counter variable
counter = 0

# Function to increment the counter
def increment_counter(value):
    """Increments the counter by a given value."""
    global counter
    counter += value
    return counter

# Pseudocode: Increase global counter by input value


# -----------------------------------------
# Code added by: Usama (24I-7321)
# Contribution: Data inspection, missing values handling, new feature engineering
# -----------------------------------------

# To have an idea about the data set
df.head()
df.info()
df.shape
df.describe()

# Checking null values
df.isna().sum()

# Fill null value with median
df['age'].fillna(df['age'].median(), inplace=True)

# Function to calculate missing value percentage per column
def missing_percentage(df):
    return (df.isna().sum() / len(df)) * 100

# New variable to check if a person is an adult
df['is_adult'] = df['age'].apply(lambda x: 1 if x >= 18 else 0)

# Pseudocode:
# 1. Check if dataset has duplicates
# 2. Remove duplicates if found
if df.duplicated().sum() > 0:
    df.drop_duplicates(inplace=True)
