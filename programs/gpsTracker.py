'''
 * ************************************************************
 *      Program: GPS Tracker
 *      Type: Python
 *      Author: David Velasco Garcia @davidvelascogarcia
 * ************************************************************
 *
 * | INPUT PORT                           | CONTENT                                                 |
 * |--------------------------------------|---------------------------------------------------------|
 * | /gpsTracker/data:i                   | Input coordinates to print in the map                   |
 *
 * | OUTPUT PORT                          | CONTENT                                                 |
 * |--------------------------------------|---------------------------------------------------------|
 * | /gpsTracker/data:o                   | Mirror output coordinates                               |
'''

# Libraries
import datetime
import os
import folium
import platform
import webbrowser
import yarp

print("**************************************************************************")
print("**************************************************************************")
print("                     Program: GPS Tracker                                 ")
print("                     Author: David Velasco Garcia                         ")
print("                             @davidvelascogarcia                          ")
print("**************************************************************************")
print("**************************************************************************")

print("")
print("Starting system ...")
print("")

print("")
print("Loading GPS Tracker engine ...")
print("")

print("")
print("Initializing gpsTracker engine ...")
print("")

# Get system configuration
print("")
print("Detecting system and release version ...")
print("")

systemPlatform = platform.system()
systemRelease = platform.release()

print("")
print("**************************************************************************")
print("Configuration detected:")
print("**************************************************************************")
print("")
print("Platform:")
print(systemPlatform)
print("Release:")
print(systemRelease)

print("")
print("**************************************************************************")
print("YARP configuration:")
print("**************************************************************************")
print("")
print("Initializing YARP network ...")
print("")

# Init YARP Network
yarp.Network.init()

print("")
print("[INFO] Opening data input port with name /gpsTracker/data:i ...")
print("")

# Open gpsTracker input data port
gpsTracker_inputPort = yarp.Port()
gpsTracker_inputPortName = '/gpsTracker/data:i'
gpsTracker_inputPort.open(gpsTracker_inputPortName)

# Create gpsTracker input data bottle
gpsTrackerInputBottle = yarp.Bottle()

print("")
print("[INFO] Opening data output port with name /gpsTracker/data:o ...")
print("")

# Open gpsTracker output data port
gpsTracker_outputPort = yarp.Port()
gpsTracker_outputPortName = '/gpsTracker/data:o'
gpsTracker_outputPort.open(gpsTracker_outputPortName)

# Create gpsTracker output data bottle
gpsTrackerOutputBottle = yarp.Bottle()

print("")
print("[INFO] YARP network configured correctly.")
print("")

print("")
print("**************************************************************************")
print("Waiting for input request coordinates:")
print("**************************************************************************")
print("")
print("[INFO] Waiting for input request coordinates at " + str(datetime.datetime.now()) + "...")
print("")

# Read from gpsTracker
gpsTracker_inputPort.read(gpsTrackerInputBottle)
mapCoordinates = gpsTrackerInputBottle.toString()

# Extract latitude from gpsTracker
start = mapCoordinates.find('*') + 1
end = mapCoordinates.find('*', start)
latitude = mapCoordinates[start:end]

# Extract longitude from gpsTracker
start = mapCoordinates.find('+') + 1
end = mapCoordinates.find('+', start)
longitude = mapCoordinates[start:end]

print("")
print("**************************************************************************")
print("Processing input map location request:")
print("**************************************************************************")
print("")
print("[INFO] Processing input map location request at " + str(datetime.datetime.now()) + " ...")
print("")
print("[INFO] Map location: " + str(latitude) + " , " + str(longitude))
print("")

# Get map
print("")
print("[INFO] Getting location map at " + str(datetime.datetime.now()) + " ...")
print("")

locationMap = folium.Map(location=[latitude , longitude])
locationMap.save('gpsTrackerLocationMap.html')

# Open tracking map
webbrowser.open("gpsTrackerLocationMap.html")

print("")
print("[INFO] Location map saved as gpsTrackerLocationMap.html")
print("")

# Variable to control loopGetLocationRequests
loopGetLocationRequests = 0

while int(loopGetLocationRequests) == 0:

    print("")
    print("**************************************************************************")
    print("Waiting for input request coordinates:")
    print("**************************************************************************")
    print("")
    print("[INFO] Waiting for input request coordinates at " + str(datetime.datetime.now()) + " ...")
    print("")

    # Read from gpsTracker
    gpsTracker_inputPort.read(gpsTrackerInputBottle)
    userCoordinates = gpsTrackerInputBottle.toString()

    # Extract gpsTracker  latitude
    start = userCoordinates.find('*') + 1
    end = userCoordinates.find('*', start)
    latitude = userCoordinates[start:end]

    # Extract gpsTracker longitude
    start = userCoordinates.find('+') + 1
    end = userCoordinates.find('+', start)
    longitude = userCoordinates[start:end]


    print("")
    print("[INFO] User location: " + str(latitude) + " , " + str(longitude) + " at " + str(datetime.datetime.now()) + ".")
    print("")

    # Print location in the map
    print("")
    print("[INFO] Locating user at " + str(datetime.datetime.now()) + " ...")
    print("")

    popupInfo = "[LOCATION] User location at: " + str(datetime.datetime.now())
    locationMap = folium.Map(location=[latitude , longitude], zoom_start=12, titles='Locating user ...')
    folium.Marker(location=[latitude , longitude], popup=popupInfo, icon=folium.Icon(color='red')).add_to(locationMap)

    # Save map
    locationMap.save('gpsTrackerLocationMap.html')

    print("")
    print("[RESULTS] The user has beed located at " + str(datetime.datetime.now()) + " ...")
    print("")

    # Open tracking map
    webbrowser.open("gpsTrackerLocationMap.html")

    # Send mirror coordinates
    gpsTrackerOutputBottle.clear()
    gpsTrackerOutputBottle.addString("LOCATION:")
    gpsTrackerOutputBottle.addString(userCoordinates)
    gpsTracker_outputPort.write(gpsTrackerOutputBottle)

# Close YARP ports
print("Closing YARP ports...")
gpsTracker_inputPort.close()
gpsTracker_outputPort.close()

print("")
print("")
print("**************************************************************************")
print("Program finished")
print("**************************************************************************")
print("")
print("gpsTracker program finished correctly.")
print("")
