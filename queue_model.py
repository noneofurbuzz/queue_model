def prob_of_exactly_n():
    plural = "s"
    number_of_people = int(input("Enter n number of people in the queue: "))
    if number_of_people == 1:
        plural = ''
    print(f"The probability that there are exactly {number_of_people} person{plural} in the queue is {(𝜌**number_of_people)*(po)}.")
def prob_at_least_n():
    sum = 0
    plural = 's'
    verb_plural = 'are'
    number_of_people = int(input("Enter n number of people in the queue: "))
    if number_of_people == 1:
        plural = ''
        verb_plural = 'is'
    for i in range(number_of_people):
        probability = (𝜌**i)*(1-𝜌)
        sum = sum + probability
    print(f"The probability that there {verb_plural} at least {number_of_people} person{plural} in the queue is {1-(sum)}.")
def prob_of_no_queue():
    prob_of_zero = 1 - 𝜌
    prob_of_one = 𝜌*(prob_of_zero)
    print(f"The probability that there is no queue is {prob_of_zero + prob_of_one}.")
def expected_people_on_queue():
    print(f"The expected number of people in the queue is {lq}")
def expected_people_in_system():
    print(f"The expected number of people in the system is {ls}")
def expected_waiting_time_system():
    ws = ls/arrival_rate
    plural = 's'
    if ws == 1:
        plural = ''
    print(f"The expected waiting time of the system is {ws} hour{plural}.")
def expected_waiting_time_queue():
    wq = lq/arrival_rate
    plural = 's'
    if wq == 1:
        plural = ''
    print(f"The expected waiting time of the queue is {wq} hour{plural}.")
def server_not_free():
    print(f"The probability that the server is not free is {𝜌}.")
def main():
    print("Welcome to the Queue simulator!\n")
    global length
    global 𝜌 
    global arrival_rate 
    global po
    global service_rate
    global lq
    global ls
    arrival_rate = int(input("Enter the arrival rate of the queue: "))
    service_rate = int(input("Enter the service rate of the queue: "))
    𝜌 = arrival_rate/service_rate
    queue_type = input("Is this an infinite queue (y/n): ").lower()
    if queue_type == "y":
        length = "∞"
    elif queue_type == "n":
        length = int(input("How many people can be in the system: "))
    else:
        print("There seems to be an error. Ensure just y or n is entered.")
    if length == "∞":
        po = 1 - 𝜌
        ls = 𝜌/(1-𝜌)
        lq = ls - 𝜌
    else:
        po = (1 - 𝜌)/(1 - (𝜌**(length + 1)))
        ls = (𝜌*(1 + (length*(𝜌**(length + 1))) - (length + 1)*(𝜌**length)))/((1 - 𝜌)*(1 - 𝜌**(length + 1)))
        lq = ls - 𝜌
    while True: 
        print("What service would you like to perform")
        print("---------------------------------------")
        print("1. Probability of exactly n people in the queue")
        print("2. Probability of at least n people in the queue")
        print("3. Probability that there is no queue")
        print("4. Expected number of people on the queue")
        print("5. Expected number of people in the system")
        print("6. Expected waiting time in the system")
        print("7. Expected waiting time in the queue")
        print("8. Probability that the server is not free")
        print("9. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            prob_of_exactly_n()
        elif choice == "2":
            prob_at_least_n()
        elif choice == "3":
            prob_of_no_queue()
        elif choice == "4":
            expected_people_on_queue()
        elif choice == "5":
            expected_people_in_system()
        elif choice == "6":
            expected_waiting_time_system()
        elif choice == "7":
            expected_waiting_time_queue()
        elif choice == "8":
            server_not_free
        elif choice == "9":
            break
        else: 
            print("There seems to be a problem. Ensure you chose only the numbers selected.")
if __name__ == "__main__":
    main()
