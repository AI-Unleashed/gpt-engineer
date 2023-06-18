import pytest
from resume import Resume
from user_interface import UserInterface

# Test data
valid_input_json = """
{
  "contact_information": {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "phone": "123-456-7890"
  },
  "resume_introduction": "A highly motivated software engineer with 5 years of experience.",
  "professional_experience": [
    {
      "company": "ABC Corp",
      "position": "Software Engineer",
      "duration": "2017-2021",
      "responsibilities": [
        "Developed web applications using Python and Django.",
        "Implemented RESTful APIs for mobile applications."
      ]
    }
  ],
  "skills": ["Python", "Django", "RESTful APIs"],
  "education": [
    {
      "institution": "XYZ University",
      "degree": "Bachelor of Science in Computer Science",
      "graduation_year": "2017"
    }
  ]
}
"""

invalid_input_json = """
{
  "contact_information": {
    "name": "John Doe",
    "email": "john.doe@example.com"
  },
  "resume_introduction": "A highly motivated software engineer with 5 years of experience.",
  "professional_experience": [
    {
      "company": "ABC Corp",
      "position": "Software Engineer",
      "duration": "2017-2021",
      "responsibilities": [
        "Developed web applications using Python and Django.",
        "Implemented RESTful APIs for mobile applications."
      ]
    }
  ],
  "skills": ["Python", "Django", "RESTful APIs"],
  "education": [
    {
      "institution": "XYZ University",
      "degree": "Bachelor of Science in Computer Science",
      "graduation_year": "2017"
    }
  ]
}
"""

def test_resume_initialization():
    resume = Resume(valid_input_json)
    assert resume.input_json == valid_input_json

def test_resume_validation_valid_input():
    resume = Resume(valid_input_json)
    assert resume.validate_input() is None

def test_resume_validation_invalid_input():
    resume = Resume(invalid_input_json)
    with pytest.raises(ValueError):
        resume.validate_input()

def test_resume_generate():
    resume = Resume(valid_input_json)
    resume.generate_resume()
    assert resume.pdf is not None

def test_resume_save():
    resume = Resume(valid_input_json)
    resume.generate_resume()
    resume.save_resume("test_resume.pdf")
    assert os.path.exists("test_resume.pdf")

def test_resume_preview():
    resume = Resume(valid_input_json)
    resume.generate_resume()
    assert resume.preview_resume() is not None

def test_user_interface_get_input(mocker):
    mocker.patch("builtins.input", return_value=valid_input_json)
    ui = UserInterface()
    assert ui.get_input() == valid_input_json

def test_user_interface_display_preview(mocker):
    resume = Resume(valid_input_json)
    resume.generate_resume()
    ui = UserInterface()
    mocker.patch("user_interface.UserInterface.display_preview", return_value=None)
    assert ui.display_preview(resume) is None

def test_user_interface_save_or_edit(mocker):
    resume = Resume(valid_input_json)
    ui = UserInterface()
    mocker.patch("builtins.input", return_value="save")
    assert ui.save_or_edit(resume) == "save"
