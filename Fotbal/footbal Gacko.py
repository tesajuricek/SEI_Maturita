key = None
results = []
f = open("results.txt", "r")
for x in f:
    results.append(x)
f.close()


def list(results):
    counter = 0
    for result in results:
        counter += 1
        print(f"{counter}. {result.strip()}")


# print(results)
while key != 'q':
    print("Press c to add new record")
    print("Press l to list all records")
    print("Press s to search in records by team name")
    print("Press d to delete specific record by id")
    print("Press u update specific record by id")
    print('Press q to quit or any other key to continue: ')
    key = input("Select action: ")
    last_id = len(results) + 1
    if key == 'c':
        first_name = input('Enter first team name: ')
        first_score = input('Enter first team score: ')
        second_name = input('Enter second team name: ')
        second_score = input('Enter second team score: ')
        results.append(f"{first_name} {first_score} : {second_score} {second_name}")
    elif key == 'l':
        list(results)
    elif key == 's':
        search_team = input('Enter team name: ')
        for result in results:
            if search_team in result:
                print(result.strip())
    elif key == 'd':
        list(results)
        delete_id = int(input('Enter record id: '))
        if 0 < delete_id <= len(results):
            results.pop(delete_id - 1)
    elif key == 'u':
        counter = 0
        for result in results:
            counter += 1
            print(f"{counter}. {result.strip()}")
        update_id = int(input('Enter record id: '))
        if 0 < update_id <= len(results):
            first_name = input('Enter first team name: ')
            first_score = input('Enter first team score: ')
            second_name = input('Enter second team name: ')
            second_score = input('Enter second team score: ')
            results[update_id - 1] = f"{first_name} {first_score} : {second_score} {second_name}"

f = open("results.txt", "w")
for result in results:
    f.writelines(f"{result.strip()}\n")
f.close()
