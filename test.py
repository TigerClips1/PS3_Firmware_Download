import webbrowser

def open_url(url):
    webbrowser.open(url, new=2)

def menu():
    print("Choose an option:")
    print("1. Google")
    print("2. KOFI")
    print("3. Python")
    choice = input("Enter your choice: ")
    if choice == "1":
        open_url("https://www.google.com")
    elif choice == "2":
        open_url("https://www.mega.nz")
    elif choice == "3":
        open_url("https://www.python.org")
    else:
        print("Invalid choice. Please try again.")
        menu()

# Call the menu function to display the menu and open the selected URL
menu()
