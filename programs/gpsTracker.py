'''
 * ************************************************************
 *      Program: GPS Tracker
 *      Type: Python
 *      Author: David Velasco Garcia @davidvelascogarcia
 * ************************************************************
 */

/*
  *
  * | INPUT PORT                           | CONTENT                                                 |
  * |--------------------------------------|---------------------------------------------------------|
  * | /gpsTracker/data:i                   | Input coordinates to print in the map                   |
  *
  * | OUTPUT PORT                          | CONTENT                                                 |
  * |--------------------------------------|---------------------------------------------------------|
  * | /gpsTracker/data:o                   | Mirror output coordinates                               |
  *
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
print("Loading GPS Tracker engine ...")

print("")
print("")
print("**************************************************************************")
print("YARP configuration:")
print("**************************************************************************")
print("")
print("Initializing YARP network ...")

# Init YARP Network
yarp.Network.init()


print("")
print("[INFO] Opening data input port with name /gpsTracker/data:i ...")

# Open input data port
gpstracker_inputPort = yarp.Port()
gpstracker_inputPortName = '/gpsTracker/data:i'
gpstracker_inputPort.open(gpstracker_inputPortName)

# Create input data bottle
inputBottle=yarp.Bottle()

print("")
print("[INFO] Opening data output port with name /gpsTracker/data:o ...")

# Open output data port
gpstracker_outputPort = yarp.Port()
gpstracker_outputPortName = '/gpsTracker/data:o'
gpstracker_outputPort.open(gpstracker_outputPortName)

# Create output data bottle
outputBottle=yarp.Bottle()


print("")
print("Initializing gpstracker engine ...")

# Get system configuration
print("")
print("Detecting system and release version ...")
systemPlatform = platform.system()
systemRelease = platform.release()

print("")
print("")
print("**************************************************************************")
print("Configuration detected:")
print("**************************************************************************")
print("Platform:")
print(systemPlatform)
print("Release:")
print(systemRelease)

# Read map coordinates
print("")
print("Waiting for input coordinates ...")

gpstracker_inputPort.read(inputBottle)
mapCoordinates = inputBottle.toString()

start = mapCoordinates.find('*') + 1
end = mapCoordinates.find('*', start)
latitude = mapCoordinates[start:end]

start = mapCoordinates.find('+') + 1
end = mapCoordinates.find('+', start)
longitude = mapCoordinates[start:end]

print("")
print("")
print("**************************************************************************")
print("Processing:")
print("**************************************************************************")

print("[INFO] Map location: "+latitude+" , "+longitude)

# Get map
print("")
print("Getting location map ...")
locationMap = folium.Map(location=[latitude , longitude])


# Save map
locationMap.save('gpstrackerLocationMap.html')
print("Location map saved as gpstrackerLocationMap.html")

while True:
    # Get location
    print("")
    print("Waiting for input location ...")

    gpstracker_inputPort.read(inputBottle)
    userCoordinates = inputBottle.toString()

    start = userCoordinates.find('*') + 1
    end = userCoordinates.find('*', start)
    latitude = userCoordinates[start:end]

    start = userCoordinates.find('+') + 1
    end = userCoordinates.find('+', start)
    longitude = userCoordinates[start:end]

    print("[INFO] User location: "+latitude+" , "+longitude)


    # Print location in the map
    print("")
    print("Locating user ...")

    dateTime = str(datetime.datetime.now())
    popupInfo="User location at: "+dateTime
    locationMap = folium.Map(location=[latitude , longitude], zoom_start=12, titles='Locating user ...')
    folium.Marker(location=[latitude , longitude], popup=popupInfo, icon=folium.Icon(color='red')).add_to(locationMap)

    # Save map
    locationMap.save('gpstrackerLocationMap.html')
    print("[RESULTS] The user has beed located at "+dateTime)

    # Open tracking map
    webbrowser.open("gpstrackerLocationMap.html")

    # Send mirror coordinates
    outputBottle.clear()
    outputBottle.addString(userCoordinates)
    gpstracker_outputPort.write(outputBottle)

# Close YARP ports
print("Closing YARP ports...")
gpstracker_inputPort.close()
gpstr_outputPort.close()

print("")
print("")
print("**************************************************************************")
print("Program finished")
print("**************************************************************************")
