from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.core.paginator import Paginator
# from .forms import UsersForm
from django.core.mail import send_mail,EmailMultiAlternatives
from sent.models import SentEmail
from django.contrib.auth import authenticate, login
from login.models import Login
from drafts.models import Drafts
def home(request):
    return render(request,'index.html',{})

def login(request):
    return render(request,'/',{})
def logout(request):
    return render(request,'logout.html',{})



from django.contrib.auth.hashers import make_password

def newUser(request):
    data={}
    if request.method == 'POST':
        user_name = request.POST.get('username')
        pass_word = request.POST.get('password')
        
        # Hash the password
        # hashed_password = make_password(pass_word)

        try:
            en = Login(username=user_name, password=pass_word)
            en.save()
        except:
            data={'error_message':"Email is Already there in records"}
    return render(request, 'newUser.html',data)




from django.shortcuts import render, redirect
from login.models import Login

def loginUser(request):
    error_message = None

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = Login.objects.get(username=username)
        except Login.DoesNotExist:
            user = None

        if user is not None and user.password == password:
            # Password comparison, assuming you are storing plain text passwords (not recommended)
            # Redirect to the home page on successful login
            return redirect('home')
        else:
            error_message = 'Invalid username or password.'

    return render(request, 'login.html', {'error_message': error_message})



from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from sent.models import SentEmail
def compose(request):
    if request.method == "POST":
        from_mail = request.POST.get('from_mail')
        to_mail = request.POST.get('to_mail')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
    
        # Add validation for required fields
        if not (from_mail and to_mail and subject and message):
            starred_message = Drafts.objects.create(
                subject=subject if subject else "none",
                recipient=to_mail if to_mail  else "none",
                message=message if message  else "none",
                # Add other fields as needed
                )
            error_message = "All fields are required."
            return render(request, 'compose.html', {'error_message': "All fields are required so message stored in drafts"})

        try:
            msg = EmailMultiAlternatives(subject, message, from_mail, [to_mail])
            # If you want to send HTML content in your email, uncomment and modify the following line:
            # msg.attach_alternative(html_message, "text/html")
            msg.send()
            sent_email = SentEmail(
                    subject=subject,
                    message=message,
                    recipient=to_mail
                )
            sent_email.save()
            # Redirect to a success page or show a success message
            return redirect('home')  # Replace 'success_page' with the actual URL name
        except Exception as e:
            error_message = f"An error occurred while sending the email: {str(e)}"
            return render(request, 'compose.html', {'error_message': error_message})

    return render(request, 'compose.html', {})


def list_sent_emails(request):
    sent_emails = SentEmail.objects.all().order_by('subject')
    # return render(request, 'sentmails.html', {'sent_emails': sent_emails})
   
    data={}
    try:
        if request.method=='GET':
            st=request.GET.get('name')
        if st!=None:
            sent_emails=SentEmail.objects.filter(subject__icontains=st)
        if sent_emails==None:
            sent_emails=True
        data={
            "sent_emails":sent_emails,
        }
        return render(request, 'sentmails.html',data)
    except:
        pass
    # Render the template with the retrieved data



# import imaplib
# from django.shortcuts import render
# import email
# from email.header import decode_header
# from email.utils import parsedate_to_datetime

# def get_inbox_emails(request):
#     # Connect to the IMAP server
#     imap_server = imaplib.IMAP4_SSL('imap.gmail.com')  # Replace with your IMAP server address
#     imap_server.login('cseaiml65@gmail.com', 'llydkizlqkfyqulv')  # Replace with your email credentials

#     # Select the inbox folder
#     imap_server.select('INBOX')

#     # Search for all emails in the inbox
#     _, email_ids = imap_server.search(None, 'ALL')

#     # Fetch email data for each email
#     inbox_emails = []
#     for email_id in email_ids[0].split():
#         _, email_data = imap_server.fetch(email_id, '(RFC822)')
#         raw_email = email_data[0][1]

#         # Parse the email message
#         parsed_email = email.message_from_bytes(raw_email)

#         # Get email attributes
#         subject_header = parsed_email["Subject"]
#         subject, encoding = decode_header(subject_header)[0]
#         if isinstance(subject, bytes):
#             subject = subject.decode(encoding or 'utf-8')
#         sender = parsed_email["From"]
#         date = parsedate_to_datetime(parsed_email["Date"])
#         sender = parsed_email[""]

#         # Create a dictionary with email attributes
#         email_info = {
#             "Subject": subject,
#             "From": sender,
#             "Date": date,
#         }

#         inbox_emails.append(email_info)

#     # Close the IMAP connection
#     imap_server.logout()

#     # Render a template or return JSON data with inbox_emails
#     return render(request, 'inbox.html', {'inbox_emails': inbox_emails})

import imaplib
import email
from email.header import decode_header
from email.utils import parsedate_to_datetime
from django.shortcuts import render  # Import the render function from Django

def get_inbox_emails(request):
    # Connect to the IMAP server
    imap_server = imaplib.IMAP4_SSL('imap.gmail.com')  # Replace with your IMAP server address
    imap_server.login('cseaiml65@gmail.com', 'wcjyayrkhvbulwvo')  # Replace with your email credentials

    # Select the inbox folder
    imap_server.select('INBOX')

    # Search for all emails in the inbox
    _, email_ids = imap_server.search(None, 'ALL')

    # Fetch email data for each email
    inbox_emails = []
    for email_id in email_ids[0].split():
        _, email_data = imap_server.fetch(email_id, '(RFC822)')
        raw_email = email_data[0][1]

        # Parse the email message
        parsed_email = email.message_from_bytes(raw_email)

        # Get email attributes
        subject_header = parsed_email["Subject"]
        subject, encoding = decode_header(subject_header)[0]
        if isinstance(subject, bytes):
            subject = subject.decode(encoding or 'utf-8')
        sender = parsed_email["From"]
        date = parsedate_to_datetime(parsed_email["Date"])

         # Get email body (message)
        if parsed_email.is_multipart():
            # For multipart emails, iterate through the parts to find the text/plain part
            for part in parsed_email.walk():
                content_type = part.get_content_type()
                if content_type == "text/plain":
                    try:
                        message = part.get_payload(decode=True).decode('utf-8')
                    except UnicodeDecodeError:
                        # If decoding as utf-8 fails, try 'latin-1' encoding
                        message = part.get_payload(decode=True).decode('latin-1', errors='replace')
                    break
            else:
                # If no text/plain part found, use an empty message
                message = ""
        else:
            # For non-multipart emails, simply get the payload as the message
            try:
                message = parsed_email.get_payload(decode=True).decode('utf-8')
            except UnicodeDecodeError:
                # If decoding as utf-8 fails, try 'latin-1' encoding
                message = parsed_email.get_payload(decode=True).decode('latin-1', errors='replace')


        # Create a dictionary with email attributes and message
        email_info = {
            "Subject": subject,
            "From": sender,
            "Date": date,
            "Message": message,  # Add the message to the dictionary
        }

        inbox_emails.append(email_info)

    # Close the IMAP connection
    imap_server.logout()

    # Render a template or return JSON data with inbox_emails
    return render(request, 'inbox.html', {'inbox_emails': inbox_emails})



from sent.models import SentEmail
from trash.models import Trash

def move_sent_to_trash(sent_message):
    # Create a Trash instance with the same data
    trash_message = Trash.objects.create(
        subject=sent_message.subject,
        recipient=sent_message.recipient,
        sent_date=sent_message.sent_date,
        # Add other fields as needed
    )

    # Delete the original Sent message
    sent_message.delete()

# Usage example:
# sent_message = Sent.objects.get(pk=1)  # Get the Sent message to delete
# move_sent_to_trash(sent_message)       # Move it to the Trash

from django.shortcuts import render
from sent.models import SentEmail

from django.shortcuts import redirect
from sent.models import SentEmail

def delete_record(request, record_id):
    if request.method == 'POST':
        try:
            record_to_delete = SentEmail.objects.get(id=record_id)
            trash_message = Trash.objects.create(
            subject=record_to_delete.subject,
            recipient=record_to_delete.recipient,
            sent_date=record_to_delete.sent_date,
            # Add other fields as needed
            )
            record_to_delete.delete()
            return redirect('sentmails')  # Redirect to a success page
        except SentEmail.DoesNotExist:
            # Handle the case where the record doesn't exist
            return HttpResponse("Record not found")
    else:
        # Handle GET requests or other HTTP methods if needed
        return HttpResponse("Invalid request method")


from trash.models import Trash
def delete_record_trash(request, record_id):
    if request.method == 'POST':
        try:
            record_to_delete = Trash.objects.get(id=record_id)
            record_to_delete.delete()
            return redirect('trash')  # Redirect to a success page
        except SentEmail.DoesNotExist:
            # Handle the case where the record doesn't exist
            return HttpResponse("Record not found")
    else:
        # Handle GET requests or other HTTP methods if needed
        return HttpResponse("Invalid request method")



# views.py

from django.shortcuts import render
from trash.models import Trash  # Import your TrashModel

def view_trash(request):
    # Retrieve all records from the TrashModel
    trash_emails = Trash.objects.all().order_by('subject')
    data={}
    try:
        if request.method=='GET':
            st=request.GET.get('name')
        if st!=None:
            trash_emails=Trash.objects.filter(subject__icontains=st)
        if trash_emails==None:
            trash_emails=True
        data={
            "trash_emails":trash_emails,
        }
        return render(request, 'trash.html',data)
    except:
        pass
    # Render the template with the retrieved data
    # return render(request, 'trash.html', {'trash_emails': trash_emails})


from django.shortcuts import render

def success_page(request):
    return render(request, 'success.html')  # 'success.html' should be the name of your success page template

from starred.models import Starred
def stared(request):
    starred_mails = Starred.objects.all().order_by('subject')
    data={}
    try:
        if request.method=='GET':
            st=request.GET.get('name')
        if st!=None:
            starred_mails=Starred.objects.filter(subject__icontains=st)
        if starred_mails==None:
            starred_mails=True
        data={
            "starred_mails":starred_mails,
        }
        return render(request, 'starred.html',data)
    except:
        pass
    # Render the template with the retrieved data




from starred.models import Starred
def starred_message(request,record_id):
    if request.method == 'POST':
        try:
            record_to_delete = SentEmail.objects.get(id=record_id)
            starred_message = Starred.objects.create(
            subject=record_to_delete.subject,
            recipient=record_to_delete.recipient,
            message=record_to_delete.message,
            # Add other fields as needed
            )
            
            return redirect('success_page_starred')  # Redirect to a success page
        except SentEmail.DoesNotExist:
            # Handle the case where the record doesn't exist
            return HttpResponse("Record not found")
    else:
        # Handle GET requests or other HTTP methods if needed
        return HttpResponse("Invalid request method")
    


def success_page_starred(request):
    return render(request, 'success_trash.html') 





def starred_trash(request,record_id):
    if request.method == 'POST':
        try:
            record_to_delete = Starred.objects.get(id=record_id)
            record_to_delete.delete()
            return redirect('stared')  # Redirect to a success page
        except SentEmail.DoesNotExist:
            # Handle the case where the record doesn't exist
            return HttpResponse("Record not found")
    else:
        # Handle GET requests or other HTTP methods if needed
        return HttpResponse("Invalid request method")
    


def drafts(request):
    
    draft_mails = Drafts.objects.all().order_by('subject')
    data={}
    try:
        if request.method=='GET':
            st=request.GET.get('name')
        if st!=None:
            draft_mails=Trash.objects.filter(subject__icontains=st)
        if draft_mails==None:
            draft_mails=True
        data={
            "draft_mails":draft_mails,
        }
        return render(request, 'drafts.html',data)
    except:
        pass
    # Render the template with the retrieved data
   

def remove_draft(request,record_id):
    if request.method=="POST":
        # Get id of email from POST request and delete it
        record_to_delete = Drafts.objects.get(id=record_id)
        starred_message = Trash.objects.create(
            subject=record_to_delete.subject,
            recipient=record_to_delete.recipient,
            sent_date=None
            # Add other fields as needed
            )
        record_to_delete.delete()
        return redirect('drafts')