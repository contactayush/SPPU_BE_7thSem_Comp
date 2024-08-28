# import re
# from email import message_from_string

# def parse_email_header(header):
#     """
#     Parse the email header and extract key information.
    
#     Args:
#     header (str): The email header as a string.

#     Returns:
#     dict: A dictionary containing the extracted information.
#     """
#     # Parse the header into an email message object
#     email_message = message_from_string(header)
    
#     # Extract relevant header fields
#     header_info = {
#         'From': email_message['From'],
#         'To': email_message['To'],
#         'Subject': email_message['Subject'],
#         'Date': email_message['Date'],
#         'Received': email_message.get_all('Received')
#     }
    
#     # Extract IP addresses from the 'Received' headers
#     header_info['Received_IPs'] = []
#     if header_info['Received']:
#         for received in header_info['Received']:
#             # Use regex to find IP addresses
#             ips = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', received)
#             header_info['Received_IPs'].extend(ips)
    
#     return header_info

# # Example usage
# email_header = """Received: from mail.example.com (mail.example.com [192.0.2.1])
#         by mx.example.net with ESMTPS id 1234567890
#         for <recipient@example.net>; Mon, 31 Jul 2024 14:32:01 +0000 (UTC)
# Received: from sender.example.com (sender.example.com [192.0.2.2])
#         by mail.example.com with ESMTPS id abcdefghijkl
#         for <recipient@example.net>; Mon, 31 Jul 2024 14:31:01 +0000 (UTC)
# Date: Mon, 31 Jul 2024 14:30:00 +0000
# From: sender@example.com
# To: recipient@example.net
# Subject: Test Email"""

# parsed_header = parse_email_header(email_header)
# for key, value in parsed_header.items():
#     print(f"{key}: {value}")


import re
def matchre(data, *args):
	for regstr in args:
		matchObj = re.search(regstr + '.*', data, re.M | re.I)
		if matchObj:
			print(matchObj.group(0).lstrip().rstrip())
		else:
			print("No ", regstr, "found")

filename = input("Enter the path for email header file:")
fo = open(filename, "r")
data = fo.read()
matchre(data, "MIME-version", "Date:", "Subject:","Delivered-to:","From:","^to:")
fo.close()