# Initialize donor data
donor_data = {
    'William Gates, III': [653772.32, 12.17],
    'Jeff Bezos': [877.33],
    'Paul Allen': [663.23, 43.87, 1.32],
    'Mark Zuckerberg': [1663.23, 4300.87, 10432.0],
    'Elon Musk': [1000.00, 500.50]
}

def send_thank_you():
    while True:
        full_name = input("Enter the full name of the donor (or type 'list' to see all donors): ").strip()
        if full_name.lower() == 'list':
            print("\nList of donors:")
            for donor in donor_data:
                print(donor)
            print()
        else:
            break

    donation_amount = input("Enter the donation amount: ").strip()
    while True:
        try:
            donation_amount = float(donation_amount)
            break
        except ValueError:
            donation_amount = input("Invalid input. Please enter a valid donation amount: ").strip()

    if full_name in donor_data:
        donor_data[full_name].append(donation_amount)
    else:
        donor_data[full_name] = [donation_amount]

    print("\nDear {},\n\nThank you for your generous donation of ${:.2f}!\n\nSincerely,\nThe Charity Team\n".format(full_name, donation_amount))

def create_report():
    print("{:<25}|{:<15}|{:<10}|{}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    print("-" * 70)

    sorted_donors = sorted(donor_data.items(), key=lambda x: sum(x[1]), reverse=True)
    for donor, donations in sorted_donors:
        total_given = sum(donations)
        num_gifts = len(donations)
        average_gift = total_given / num_gifts
        print("{:<25} ${:<14.2f} {:<10} ${:.2f}".format(donor, total_given, num_gifts, average_gift))

def main():
    while True:
        user_input = input("\nChoose an action:\n1. Send a Thank You\n2. Create a Report\n3. Quit\n").strip()

        if user_input == '1':
            send_thank_you()
        elif user_input == '2':
            create_report()
        elif user_input == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid input. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
