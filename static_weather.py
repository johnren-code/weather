import glob
import os
import sys
import argparse
import math
import carla

def main():
    argparser = argparse.ArgumentParser(
        description=__doc__)
    argparser.add_argument(
        '--host',
        metavar='H',
        default='127.0.0.1',
        help='IP of the host server (default: 127.0.0.1)')
    argparser.add_argument(
        '-p', '--port',
        metavar='P',
        default=2000,
        type=int,
        help='TCP port to listen to (default: 2000)')
    
    args = argparser.parse_args()


    client = carla.Client(args.host, args.port)
    client.set_timeout(2.0)
    world = client.get_world()
    # weather = carla.WeatherParameters()
    #     weather.cloudiness = weather_parameters.cloudiness
    #     weather.precipitation = weather_parameters.precipitation
    #     weather.precipitation_deposits = weather_parameters.precipitation_deposits
    #     weather.wind_intensity = weather_parameters.wind_intensity
    #     weather.fog_density = weather_parameters.fog_density
    #     weather.fog_distance = weather_parameters.fog_distance
    #     weather.wetness = weather_parameters.wetness
    #     weather.sun_azimuth_angle = weather_parameters.sun_azimuth_angle
    #     weather.sun_altitude_angle = weather_parameters.sun_altitude_angle
    weather = carla.WeatherParameters(cloudiness=50.0,
                                          precipitation=50.0,
                                          precipitation_deposits=50.0,
                                          wind_intensity = 50.0,
                                          fog_density=0.0,
                                          wetness=70.0,
                                          sun_altitude_angle=30.0
                                          )
    world.set_weather(weather)

if __name__ == '__main__':
    main()