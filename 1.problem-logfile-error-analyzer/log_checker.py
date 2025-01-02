def check_log_for_errors_with_for(log_file):
    # import pdb; pdb.set_trace()
    try:
        with open(log_file, "r") as f:
            print("Checking for errors using a for loop...")
            for line_number, line in enumerate(f):
                if "ERROR" in line:
                    print(f"Error found on line {line_number}: {line.strip()}")
                    
    except FileNotFoundError:
        print(f"Log file '{log_file}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

path = './abc.log'
check_log_for_errors_with_for(path)