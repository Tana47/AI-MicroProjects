def solve_map_coloring():
    graph = {
        "Adilabad": ["Kumurambheem Asifabad", "Nirmal"],
        "Kumurambheem Asifabad": ["Adilabad", "Nirmal", "Mancherial"],
        "Nirmal": ["Adilabad", "Kumurambheem Asifabad", "Mancherial", "Jagtial", "Nizamabad"],
        "Nizamabad": ["Nirmal", "Jagtial", "Rajanna Sircilla", "Kamareddy"],
        "Mancherial": ["Kumurambheem Asifabad", "Nirmal", "Jagtial", "Peddapalli", "Jayashankar Bhupalpally"],
        "Jagtial": ["Nirmal", "Mancherial", "Peddapalli", "Karimnagar", "Rajanna Sircilla", "Nizamabad"],
        "Peddapalli": ["Mancherial", "Jayashankar Bhupalpally", "Karimnagar", "Jagtial"],
        "Jayashankar Bhupalpally": ["Mancherial", "Peddapalli", "Karimnagar", "Hanumakonda", "Warangal Rural", "Mulugu"],
        "Mulugu": ["Jayashankar Bhupalpally", "Warangal Rural", "Mahabubabad", "Bhadradri Kothagudem"],
        "Bhadradri Kothagudem": ["Mulugu", "Mahabubabad", "Khammam"],
        "Khammam": ["Bhadradri Kothagudem", "Mahabubabad", "Suryapet"],
        "Mahabubabad": ["Mulugu", "Bhadradri Kothagudem", "Khammam", "Suryapet", "Jangaon", "Warangal Rural"],
        "Warangal Rural": ["Jayashankar Bhupalpally", "Mulugu", "Mahabubabad", "Jangaon", "Hanumakonda"],
        "Hanumakonda": ["Jayashankar Bhupalpally", "Warangal Rural", "Jangaon", "Siddipet", "Karimnagar"],
        "Karimnagar": ["Peddapalli", "Jayashankar Bhupalpally", "Hanumakonda", "Siddipet", "Rajanna Sircilla", "Jagtial"],
        "Rajanna Sircilla": ["Jagtial", "Karimnagar", "Siddipet", "Kamareddy", "Nizamabad"],
        "Kamareddy": ["Nizamabad", "Rajanna Sircilla", "Siddipet", "Medak", "Sangareddy"],
        "Sangareddy": ["Kamareddy", "Medak", "Medchal Malkajgiri", "Rangareddy", "Vikarabad"],
        "Medak": ["Kamareddy", "Siddipet", "Medchal Malkajgiri", "Sangareddy"],
        "Siddipet": ["Rajanna Sircilla", "Karimnagar", "Hanumakonda", "Jangaon", "Yadadri Bhuvanagiri", "Medchal Malkajgiri", "Medak", "Kamareddy"],
        "Jangaon": ["Hanumakonda", "Warangal Rural", "Mahabubabad", "Suryapet", "Yadadri Bhuvanagiri", "Siddipet"],
        "Yadadri Bhuvanagiri": ["Siddipet", "Jangaon", "Suryapet", "Nalgonda", "Rangareddy", "Medchal Malkajgiri"],
        "Suryapet": ["Jangaon", "Mahabubabad", "Khammam", "Nalgonda", "Yadadri Bhuvanagiri"],
        "Nalgonda": ["Suryapet", "Yadadri Bhuvanagiri", "Rangareddy", "Nagarkurnool"],
        "Nagarkurnool": ["Nalgonda", "Rangareddy", "Mahabubnagar", "Wanaparthy", "Jogulamba Gadwal"],
        "Jogulamba Gadwal": ["Nagarkurnool", "Wanaparthy", "Narayanpet"],
        "Wanaparthy": ["Nagarkurnool", "Mahabubnagar", "Narayanpet", "Jogulamba Gadwal"],
        "Narayanpet": ["Vikarabad", "Mahabubnagar", "Wanaparthy", "Jogulamba Gadwal"],
        "Mahabubnagar": ["Narayanpet", "Vikarabad", "Rangareddy", "Nagarkurnool", "Wanaparthy"],
        "Vikarabad": ["Sangareddy", "Rangareddy", "Mahabubnagar", "Narayanpet"],
        "Rangareddy": ["Vikarabad", "Sangareddy", "Medchal Malkajgiri", "Hyderabad", "Yadadri Bhuvanagiri", "Nalgonda", "Nagarkurnool", "Mahabubnagar"],
        "Hyderabad": ["Rangareddy", "Medchal Malkajgiri"],
        "Medchal Malkajgiri": ["Sangareddy", "Medak", "Siddipet", "Yadadri Bhuvanagiri", "Rangareddy", "Hyderabad"]
    }

    for node, neighbors in list(graph.items()):
        for neighbor in neighbors:
            if neighbor not in graph:
                graph[neighbor] = []
            if node not in graph[neighbor]:
                graph[neighbor].append(node)

    districts = list(graph.keys())
    colors = ["Red", "Green", "Blue", "Yellow"]
    assigned_colors = {}

    def is_safe(district, color):
        for neighbor in graph[district]:
            if assigned_colors.get(neighbor) == color:
                return False
        return True

    def backtrack(index):
        if index == len(districts):
            return True
        
        current_district = districts[index]
        
        for color in colors:
            if is_safe(current_district, color):
                assigned_colors[current_district] = color
                
                if backtrack(index + 1):
                    return True
                
                assigned_colors.pop(current_district)
                
        return False

    if backtrack(0):
        print("Telangana District Map Coloring Successful!\n")
        print(f"{'District':<25} | {'Assigned Color':<10}")
        print("-" * 42)
        for district, color in assigned_colors.items():
            print(f"{district:<25} | {color:<10}")
    else:
        print("No solution exists with the given constraints and colors.")

if __name__ == "__main__":
    solve_map_coloring()