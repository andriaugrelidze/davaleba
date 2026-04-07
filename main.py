users = [
    {"id": 1, "name":"ნუგო"},
    {"id": 2, "age": 21},
    {"id": 1, "age": 30},
    {"id": 3, "name":"ხრუსტალი"},
    {"id": 2, "name":"ზალიკო"}
]
merged = {}
for user in users:
    user_id = user["id"]
    if user_id not in merged:
        merged[user_id] = {}
    merged[user_id].update(user)
print(merged)
categories = {
    "ხილი": ["ვაშლი", "ბანანი"],
    "ბოსტნეული": ["სტაფილო", "ხახვი"],
    "საკონდიტრო": ["ბანანი", "ტორტი"]
}
inverted = {}
for category, items in categories.items():
    for item in items:
        if item not in inverted:
            inverted[item] = []
        inverted[item].append(category)
print(inverted)