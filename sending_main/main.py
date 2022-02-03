import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email

message = Mail(
    from_email=Email(email = "contact.skillupcommunity@gmail.com", name="Skill-Up-Community"),
    to_emails='annup76779@gmail.com'
	)

message.template_id = "d-9d53928b11ba4d228340c96bba721aff"
message.dynamic_template_data = {
	"user": {
		"name": "Anurag Pandey"
	}
}
# message.category = list("Primary")
print(message.template_id)

try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e)

# import sendgrid
# import os

# sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
# response = sg.client.suppression.bounces.get()
# # print(response.status_code)
# # print(response.body)
# print(response.headers)
