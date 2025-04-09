"""Examples of Set and Dictionary syntax."""

pids: set[int] = {710000000, 712345678}
pids.add(730120710)

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}
# to modify the total of vanilla
ice_cream["vanilla"] += 110

# to add a key to the dict
ice_cream["mint"] = 3

# to access or mdoify
ice_cream["chocolate"]
ice_cream["vanilla"] = 10

# Check if key in dictionary
# "chocolate" in ice_cream (how to do it)
if "mint" in ice_cream:
    print(ice_cream["mint"])
else:
    print("no orders of mint.")

# to remove a pair
ice_cream.pop("strawberry")

# how to use for loops
tot_orders: int = 0

for key in ice_cream:
    print(f"{key}: {ice_cream[key]}")
    tot_orders += ice_cream[key]

print(f"Total Order: {tot_orders}")
