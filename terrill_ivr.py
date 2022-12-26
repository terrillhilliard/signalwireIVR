import signalwire
from signalwire.relay.client import Client
import os
from flask import Flask, request

app = Flask(__name__)

# Set up the SignalWire client
client = Client(project='main', token='PTf7fb72428c301d287b08d6e7404c09881481ed9911507f6f')


@app.route('/ivr', methods=['POST'])
def ivr():
    # Get the SignalWire context and call object from the request
    context = signalwire.RelayContext(request.form)
    call = context.get_call()

    # Play a greeting message
    call.say('Welcome to our SignalWire. Press 1 to leave a voicemail, or 2 to speak to a representative.')

    # Collect the user's response
    result = call.gather(num_digits=1)

    # Route the call based on the user's response
    if result.digits == '1':
        # Record a voicemail
        call.say('Please leave a message after the beep.')
        recording = call.record(timeout=30)
        if recording.status == 'completed':
            # Save the recording to a file
            with open('voicemail.wav', 'wb') as f:
                f.write(recording.wav)
            call.say('Thank you for your message. It has been saved.')
        else:
            call.say('Sorry, there was an error recording your message.')
    elif result.digits == '2':
        call.say('Connecting you to a representative.')
        call.transfer('+17043369285') # Transfer the call to a representative
    else:
        call.say('Sorry, I did not understand your response. Please try again.')
        call.hangup()

    # Return a empty response to SignalWire
    return '', 204

if __name__ == '__main__':
    app.run()
