# signalwireIVR
Welcome to the Python IVR using the SignalWire SDK!

This project provides an interactive voice response (IVR) system that allows users to interact with a SignalWire phone number and perform various actions based on their input. The IVR is powered by the SignalWire SDK for Python, which provides a set of tools for building telephony applications with the SignalWire API.



Prerequisites

Before getting started with this IVR, you will need to have completed the following steps:

Signed up for a SignalWire account and purchased a phone number.
Set up your SignalWire project and installed the SignalWire Python client library.
To install the SignalWire Python client library, you can use pip:

pip install signalwire





Getting started

To use this IVR, you will need to authenticate your SignalWire account using your API key and project name. You can find these values in the SignalWire dashboard under "Project Settings."

Once you have your API credentials, you can write a Python script that uses the SignalWire client library to interact with the SignalWire REST API.

Here is an example of how to authenticate your SignalWire account:

import signalwire

signalwire.Client(project='YOUR_PROJECT_NAME', token='YOUR_API_KEY').authenticate()





Functionality

The IVR should handle inbound calls to a SignalWire number and play a short menu to the caller offering them at least two menu options. The menu options should accept input from the caller and perform an action based on that input.

For example, the IVR could allow the caller to:

Record a voicemail
Forward the call to a different number
Gather customer information (e.g. name, email address)
You can customize the menu options and actions to fit your specific needs.




