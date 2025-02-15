# I deleted the first line of string in the life-expectancy.csv 

with open("life-expectancy.csv") as people_data:
    number_count = 0
    average = 0

    all_min_expectancy = 999999999
    all_min_country = ""
    all_min_year = 0

    all_max_expectancy = 0
    all_max_country = ""
    all_max_year = 0

    lowest_expectancy = 999999999
    lowest_country = ""
    highest_expectancy = 0
    highest_country = ""

    research_year = int(input("Enter the year of interest: "))

    for line in people_data:
        no_whitespace = line.strip()

        # split the line into parts
        parts = no_whitespace.split(",")

        # storing each part in a variable
        country = parts[0]
        year = int(parts[2])
        expectancy = float(parts[3])

        if expectancy < all_min_expectancy:
            all_min_expectancy = expectancy
            all_min_country = country
            all_min_year = year

        if expectancy > all_max_expectancy:
            all_max_expectancy = expectancy
            all_max_country = country
            all_max_year = year

        if research_year == year:
            average += expectancy
            number_count += 1

            if expectancy < lowest_expectancy:
                lowest_expectancy = expectancy
                lowest_country = country
            
            elif expectancy > highest_expectancy:
                highest_expectancy = expectancy
                highest_country = country


    print()
    print(f"The overall max life expectancy is: {all_min_expectancy} from {all_min_country} in {all_min_year}")
    print(f"The overall min life expectancy is: {all_max_expectancy} from {all_max_country} in {all_max_year}")

    print()
    print(f"For the year {research_year}:")
    print(f"The average life expectancy across all countries was {average / number_count}")
    print(f"The max life expectancy was in {highest_country} with {highest_expectancy}")
    print(f"The min life expectancy was in {lowest_country} with {lowest_expectancy}")
