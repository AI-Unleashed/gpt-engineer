from resume import Resume

class UserInterface:
    def get_input(self):
        input_json = input("Enter the resume data in JSON format: ")
        return input_json

    def display_preview(self, resume: Resume):
        print(f"Preview: The generated resume has {resume.preview_resume()} pages.")

    def save_or_edit(self, resume: Resume):
        while True:
            action = input("Enter 'save' to save the resume, or 'edit' to edit the input JSON: ").lower()
            if action in ["save", "edit"]:
                return action
            else:
                print("Invalid input. Please enter 'save' or 'edit'.")
