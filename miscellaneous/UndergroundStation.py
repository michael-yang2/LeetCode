class UndergroundSystem:

    def __init__(self):
        self.id_dict = {}
        self.station_avg_time = {}
        self.num_trips = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.id_dict[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        prevStation, checkintime = self.id_dict[id]
        del self.id_dict[id]
        if (prevStation, stationName) not in self.station_avg_time:
            self.station_avg_time[(prevStation, stationName)] = t - checkintime
            self.num_trips[(prevStation, stationName)] = 1
        else:
            prev_avg = self.station_avg_time[(prevStation, stationName)]
            prev_num_trips = self.num_trips[(prevStation, stationName)]
            self.station_avg_time[(prevStation, stationName)] = (prev_avg * prev_num_trips + (t - checkintime))/(prev_num_trips+1)
            self.num_trips[(prevStation, stationName)] = prev_num_trips+1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.station_avg_time[(startStation, endStation)]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)