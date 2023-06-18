from user_interface import UserInterface
from resume import Resume

def main():
    ui = UserInterface()
    while True:
        input_json = ui.get_input()
        resume = Resume(input_json)
        try:
            resume.validate_input()
        except ValueError as e:
            print(f"Invalid input: {e}")
            continue

        resume.generate_resume()
        ui.display_preview(resume)

        action = ui.save_or_edit(resume)
        if action == "save":
            file_name = input("Enter the file name for the resume (without extension): ")
            resume.save_resume(f"{file_name}.pdf")
            print("Resume saved successfully.")
            break
        elif action == "edit":
            continue

if __name__ == "__main__":
    main()
