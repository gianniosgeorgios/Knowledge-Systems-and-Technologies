import pandas as pd 
import sys
import itertools


##############        stops.txt    ----->    stops.ttl  ##############
with open("stops.ttl", "a") as f:
    sys.stdout = f
    #Read Input from .txt file as rows 
    stops = pd.read_csv("googletransit/stops.txt") 
    stops.fillna("UNK", inplace=True)
    stops.head()

    for index, row in stops.iterrows():
        stop_id = row["stop_id"]
        name = row["stop_name"]
        Information = row["stop_desc"]
        latitude = row["stop_lat"]
        longitude = row["stop_lon"]
        
        print(":s{} rdf:type owl:NamedIndividual .".format(stop_id))
        print(":s{} rdf:type :Station .".format(stop_id))
        print(":s{} :OfCompany :ΟΑΣΑ .".format(stop_id))
        print(":s{} :Coordinates \"POINT({} {})\"^^vrdf:Geometry .".format(stop_id, latitude, longitude))
        print(":s{} :Name \"{}\" .".format(stop_id, name))
        print(":s{} :Information \"{}\" .".format(stop_id, Information))
        print()


##############        trips.txt    ----->    trips.ttl  ##############
with open("trips.ttl", "a") as f:
    sys.stdout = f            
    #Read Input from .txt file as rows 
    trips = pd.read_csv("googletransit/trips.txt") 
    trips.fillna("UNK", inplace=True)
    trips.head()

    for index, row in trips.iterrows():
        route_id = row["route_id"].split("-")[0]
        trip_id = row["trip_id"].split("-")[0]
        name = row["trip_headsign"]
    
        print(":t{} rdf:type owl:NamedIndividual .".format(trip_id)) 
        print(":t{} rdf:type :TripsInfo .".format(trip_id))
        print(":t{} :OfCompany :ΟΑΣΑ .".format(trip_id))
        print(":t{} :Name \"{}\" .".format(trip_id, name))
        print(":r{} :Serves :t{} .".format(route_id, trip_id))
        print()


##############        stop_times.txt    ----->    stop_times.ttl  ##############
with open("stop_times.ttl", "a") as f:
    sys.stdout = f
    #Read Input from .txt file as rows 
    stop_times = pd.read_csv("googletransit/stop_times.txt") 
    stop_times.fillna("UNK", inplace=True)
    stop_times.head()

    for index, row in stop_times.iterrows():
        desc = row["trip_id"].split("-")
        trip_id = desc[0]
        desc = '-'.join(desc[2:len(desc) - 1])
        station_id = row["stop_id"]
        arrival = row["arrival_time"]
        departure = row["departure_time"]
    
        print(":As{} rdf:type owl:NamedIndividual .".format(index)) 
        print(":As{} rdf:type :StationEnd .".format(index))
        print(":As{} :OfCompany :ΟΑΣΑ .".format(index))
        print(":As{} :TimeInfo \"{}\" .".format(index, arrival))
        print(":As{} :Information \"{}\" .".format(index, desc))
        print(":As{} :hasStation :s{} .".format(index, station_id))
        print(":t{} :StopsAt :As{} .".format(trip_id, index))
        print()

        print(":Ds{} rdf:type owl:NamedIndividual .".format(index)) 
        print(":Ds{} rdf:type :StationStart .".format(index))
        print(":Ds{} :OfCompany :ΟΑΣΑ .".format(index))
        print(":Ds{} :TimeInfo \"{}\" .".format(index, arrival))
        print(":Ds{} :Information \"{}\" .".format(index, desc))
        print(":Ds{} :hasStation :s{} .".format(index, station_id))
        print(":t{} :StartsFrom :Ds{} .".format(trip_id, index))
        print()


##############        routes.txt    ----->    routes.ttl  ##############
with open("routes.ttl", "a") as f:
    sys.stdout = f
    #Read Input from .txt file as rows 
    routes = pd.read_csv("googletransit/routes.txt") 
    routes.fillna("UNK", inplace=True)
    routes.head(200)

    for index, row in routes.iterrows():
        name = row["route_short_name"]
        long_name = row["route_long_name"]
        # Read codes of route_type and idendify each mean of transport
        if(row["route_type"] == 900): 
            print(":r{} rdf:type owl:NamedIndividual .".format(name))
            print(":r{} rdf:type :Tram .".format(name))
            print(":r{} :OfCompany :ΟΑΣΑ .".format(name))
            print(":r{} :Name \"{}\" .".format(name, long_name))
            print()
        if(row["route_type"] == 1): 
            print(":r{} rdf:type owl:NamedIndividual .".format(name))
            print(":r{} rdf:type :Metro .".format(name))
            print(":r{} :OfCompany :ΟΑΣΑ .".format(name))
            print(":r{} :Name \"{}\" .".format(name, long_name))
            print()
        if(row["route_type"] == 800): 
            print(":r{} rdf:type owl:NamedIndividual .".format(name))
            print(":r{} rdf:type :Trolley .".format(name))
            print(":r{} :OfCompany :ΟΑΣΑ .".format(name))
            print(":r{} :Name \"{}\" .".format(name,long_name))
            print()
        if(row["route_type"] == 3): 
            print(":r{} rdf:type owl:NamedIndividual .".format(name))
            print(":r{} rdf:type :Bus .".format(name))
            print(":r{} :OfCompany :ΟΑΣΑ .".format(name))
            print(":r{} :Name \"{}\" .".format(name,long_name))
            print()




