#1
class Shape:
    def __init__(self, renderer): # Class constructor
        self.renderer = renderer  # Saving renderer as a unit attribute

    def draw(self):
        pass  # Redefined in children

class Circle(Shape):
    def draw(self): # Draw method for circle
        self.renderer.render_circle() # Calling circle renderer method

class Square(Shape):
    def draw(self):
        self.renderer.render_square()

class Renderer:
    def render_circle(self):
        pass

    def render_square(self):
        pass

class RasterRenderer(Renderer):
    # Realisation of rendering in raster format
    def render_circle(self):
        print("Drawing sircle in raster format")

    # Raster square
    def render_square(self):
        print("Drawing square in raster format")

# Making raster render instance
raster_renderer = RasterRenderer()

# Circle with raster renderer
circle = Circle(raster_renderer)
circle.draw()  # Returns "Drawing sircle in raster format"

# Square
square = Square(raster_renderer)
square.draw()  # Returns "Drawing square in raster format"


#2
class NotificationSender: # Base notification sender interface
    def send(self, message):
        pass


class EmailSender(NotificationSender):
    def send(self, message):
        print(f"Sending email: {message}")  # Method for sending emails


class SmsSender(NotificationSender):
    def send(self, message):
        print(f"Sending SMS: {message}")


class Notification: # Abstract class
    def __init__(self, sender):  # Constructor
        self.sender = sender  # Saving sender as instance unit

    def notify(self, message):
        print("Sending notification...")  # Send start msg
        self.sender.send(message)  # Call send for sending the msg


# Example use case
email_sender = EmailSender()
sms_sender = SmsSender()

email_notification = Notification(email_sender)  # Making a notification w/ email sender
sms_notification = Notification(sms_sender)  # Making a notification w/ sms sender

email_notification.notify("This is an email notification")  # Sending email notification
sms_notification.notify("This is an SMS notification")


