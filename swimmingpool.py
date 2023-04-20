current_position = 1

while True:
    # Prompt user to turn on or off the pool
    pool_status = input("Turn on (1) or turn off (0) the pool: ")

    # Turn on the pool pump
    if pool_status == "1":
        print("Turning on the pool pump...")
    # Turn off the pool pump and turn on the filter
    elif pool_status == "0":
        print("Turning off the pool pump and turning on the filter...")

    # Prompt user for faucet position
    faucet_position = int(input("Enter the position of the faucet (1-6): "))

    # If faucet position is different from current position, turn off filter and move faucet
    if faucet_position != current_position:
        print("Moving faucet to position", faucet_position, "...")
        print("Turning off the filter...")

        # Update current position of the faucet
        current_position = faucet_position
    else:
        print("Faucet is already in position", faucet_position)

    # Prompt user to exit or continue
    exit_program = input("Enter 1 to exit or any other key to continue: ")
    if exit_program == "1":
        break
