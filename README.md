# trident-hacks

This repository is for me to collect information I've learned about the Trident OpenROV that isn't documented anywhere else.

# Compass and Calibration

From https://forum.openrov.com/t/how-to-use-the-trident-display-to-full-advantage/6243/14:

Trident has an internal magnetic compass, and fuses its data with a rate gro. To calibrate this pair of 
sensors, rotate the vehicle back and forth about each of its three axes.

The JXD S192 Game Pad, which OpenROV sells as the preferred controller, does not have an internal compass.
This means that the Pilot display of OpenROV Cockpit cannot display heading of the controller.
To visualize the true direction of the vehicle, you'll need an external compass or some other queue for situational awareness.

# Controller software

To get the OpenROV Cockpit software for Android, you need to be admitted to the private beta program. You should request access as soon as 
you have a shipping notification for your Trident.

Set up an account for your self on 
the Google Play store (https://play.google.com/store/account). Then email support@openrov.com and tell them the address you're using for 
Google Play (it might not be the same address you're using to correspond with OpenROV). Ask for access to the OpenROV beta for your Google 
Play account.
