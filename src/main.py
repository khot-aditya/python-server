import json
from appwrite.client import Client
import os
from skpy import Skype

# This is your Appwrite function
# It's executed each time we get a request
def main(context):
    
    # The `ctx.req` object contains the request data
    if context.req.method == "GET":
        # Send a response with the res object helpers
        # `ctx.res.send()` dispatches a string back to the client
        return context.res.send("Hello, World!")
    
    if context.req.method == "POST":
        
        context.log(context.req)
        # Access POST data from context.req.data
        post_data = json.loads(context.req.body)
        username = post_data.get("username")
        password = post_data.get("password")
        chatId = post_data.get("chatId")
        message = post_data.get("message")
        
        try:
            # Create a Skype connection
            sk = Skype(username, password)

            contact_username = chatId
            contact = sk.contacts[contact_username]

            # Send a text message
            message_content = message
            contact.chat.sendMsg(message_content)

            return context.res.send("Message sent successfully.")

        except Exception as e:
            return context.res.send(f"Error in Skype connection: {e}")

        finally:
            # Close the Skype connection to ensure proper cleanup
            if sk:
                sk.conn.close()
                
                # Do something with the post data
                context.log(f"Skype connection closed.")

    # `ctx.res.json()` is a handy helper for sending JSON
    return context.res.json(
        {
            "motto": "Build like a team of hundreds_",
            "learn": "https://appwrite.io/docs",
            "connect": "https://appwrite.io/discord",
            "getInspired": "https://builtwith.appwrite.io",
        }
    )
