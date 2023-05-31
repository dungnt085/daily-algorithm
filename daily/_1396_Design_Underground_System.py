from collections import defaultdict

class Underground:
    def __init__(self) -> None:
        self.user = defaultdict()
        self.avgtime = defaultdict()

    def check_in(id:int, station_name:str, t:int ):
        if id not in self.user:
            self.user[id] = {"checkin_station":station_name, "checkin_time":t}

    def check_out(id:int, station_name:str, t:int):
        checkin_station = self.user[id][checkin_station]
        checkin_time = self.user[id][checkin_time]
        del self.user[id]

        key = checkin_station + '-' + station_name
        if key in self.avgtime:
            self.avgtime[key].append(t-checkin_time)
        else:
            self.avgtime[key] = [t-checkin_time]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = startStation+'-'+endStation
        summ = sum(self.avgTime[key])
        length = len(self.avgTime[key])
        return summ/length
    

