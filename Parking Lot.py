# enum type for Vehicle
class VehicleSize:
    Motorcycle = 1
    Compact = 2
    Large = 3
    Other = 99

class Vehicle:
    size = -1
    # Write your code here
    def __init__(self):
        self.level = -1
        self.row = -1
        self.spot = -1


class Motorcycle(Vehicle):
    # Write your code here
    size = VehicleSize.Motorcycle

class Car(Vehicle):
    # Write your code here
    size = VehicleSize.Compact

class Bus(Vehicle):
    # Write your code here
    size = VehicleSize.Other

class Level:
    # Write your code here
    def __init__(self, rows, spots):
        self.totalRows = rows
        self.spots_per_row = spots
        self.rows = collections.defaultdict(dict)
        for r in range(rows):
            self.rows[r] = self.__initSpots(spots)
    
    def __getType(self, size):
        if size >= self.spots_per_row / 4 * 3:
            return VehicleSize.Large
        elif size >= self.spots_per_row / 4:
            return VehicleSize.Compact
        else:
            return VehicleSize.Motorcycle
        
    def unpark(self, row, spot, vsize):
        spType = self.__getType(spot)
        self.rows[row][spType].append(spot)
        if vsize == VehicleSize.Other:
            self.rows[row][spType].extend(range(spot + 1, spot + 5))
        
        self.rows[row][spType].sort()
        
    def find(self, size):
        for r, sps in self.rows.items():
            spsNum = self.__findSpots(sps, size)
            if spsNum >= 0:
                return r, spsNum
        return -1, -1
                
    def __findSpots(self, sps, size):
        if size < VehicleSize.Other:
            return self.__findSigleOne(sps, size)
        else:
            count = 0
            val = -1
            for index, spot in enumerate(sps[VehicleSize.Large]):
                # print sps[VehicleSize.Large]
                if spot - index != val:
                    count = 1
                    val = spot - index
                else:
                    count += 1
                if count == 5:
                    # print spot
                    for s in range(spot - 4, spot + 1):
                        sps[VehicleSize.Large].remove(s)
                    return spot - 4
            return -1
            
    def __findSigleOne(self, sps, size):
        # for sz, spots in sps.items():
        for sz in [1, 2, 3]:
            spots = sps[sz]
            if sz >= size and spots:
                ans = spots[0]
                spots.pop(0)
                return ans
        return -1
        
    def __initSpots(self, spots):
        sps = {}
        sps[VehicleSize.Motorcycle] = range(0, spots / 4)
        sps[VehicleSize.Compact] = range(spots / 4, spots / 4 * 3)
        sps[VehicleSize.Large] = range(spots / 4 * 3, spots)
        return sps
        


class ParkingLot:
    # @param {int} n number of leves
    # @param {int} num_rows  each level has num_rows rows of spots
    # @param {int} spots_per_row each row has spots_per_row spots
    def __init__(self, n, num_rows, spots_per_row):
        # Write your code here
        self.levels = {}
        for i in range(n):
            self.levels[i] = Level(num_rows, spots_per_row)

    # Park the vehicle in a spot (or multiple spots)
    # Return false if failed
    def park_vehicle(self, vehicle):
        # Write your code here
        for k, v in self.levels.items():
            row, spot = v.find(vehicle.size)
            if spot >= 0:
                vehicle.level, vehicle.row, vehicle.spot = k, row, spot
                return True
        return False


    # unPark the vehicle
    def unpark_vehicle(self, vehicle):
        # Write your code here
        self.levels[vehicle.level].unpark(vehicle.row, vehicle.spot, vehicle.size)
