# Automated Email Script

This Python script sends automated emails with both plain text and HTML content. It includes an "Icebox" section where additional features can be added in the future.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python
- Git (optional, for cloning the repository)

## Getting Started

1. Clone the repository to your local machine (optional):

   ```bash
   git clone https://github.com/joe-bor/automated-email-script.git
   cd automated-email-script
   ```

2. Install required dependencies using the provided `requirements.txt`

   ```
   pip install -r requirements.txt
   ```

3. Create a file named .env in the project root and add the following:

   ```
   EMAIL=your_email@example.com
   PASSWORD=your_email_password
   RECEIVER_EMAILS=email1@example.com,email2@example.com
   GOALS=goal1, goal2, goal3
   REFLECTIONS=reflection1, reflection2, reflection3
   ```

- Replace the placeholders with your actual email, password, and receiver email addresses. Add your goals and reflections for customization.

4. Execute the script by running the following command:

   ```bash
   python automated_email_script.py
   ```

## Customization

- Email Content:

  - Modify the `get_goals` and `get_reflections` functions in the script to customize your goals and reflections dynamically.
  - Edit the HTML content in the `msg.add_alternative` section for the HTML version to reflect your message.

- Icebox Section:

  - Add or remove items in the "Icebox" section to include or exclude additional features.
  - Modify the script to implement new features in the "Icebox."

## Notes

- Ensure that "Less Secure App Access" is enabled for the sender email account to allow SMTP access. This setting may vary depending on your email provider.

- Always keep sensitive information, such as email passwords, secure.

- Avoid sharing them in public repositories or environments.
