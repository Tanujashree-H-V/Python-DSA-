# Dictionary to store details of two friends
friends = {
    "Alice": {
        "name": "Alice",
        "favorite_subject": "Mathematics",
        "favorite_food": "Pizza"
    },
    "Bob": {
        "name": "Bob",
        "favorite_subject": "Physics",
        "favorite_food": "Sushi"
    }
}

# Access and print the favorite food of Alice
print(f"Alice's favorite food is: {friends['Alice']['favorite_food']}")

# You can also print Bob's favorite food
print(f"Bob's favorite food is: {friends['Bob']['favorite_food']}")