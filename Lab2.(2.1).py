from lab2 import matrix
def mad_delivery(matrix, patients_in_room, packs_for_patient, robot_capacity):
    m = len(matrix)
    n = len(matrix[0])

    total_patient = m * n * patients_in_room
    tot_packs = total_patient * packs_for_patient

    trips = (tot_packs + robot_capacity - 1) // robot_capacity 
    return total_patient, tot_packs, trips

if __name__ == "__main__":
    patients_in_room = int(input("Введіть кл пацієнтів на палату:"))
    packs_for_patient = int(input("Введіть кл упаковок для пацієнта:"))
    robot_capacity = int(input("Введіть кл упаковок:"))

    total_patients, total_packs, trips = mad_delivery(
        matrix, patients_in_room, packs_for_patient, robot_capacity 
        ) 

    print(f"Кількість пацієнтів: {total_patients}") 
    print(f"Кількість упаковок ліків: {total_packs}") 
    print(f"Робот повертався {trips} раз(ів) за ліками")