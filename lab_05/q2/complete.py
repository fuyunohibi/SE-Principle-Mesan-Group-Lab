class Transportation(object):
   """Abstract base class"""

   def __init__( self, start, end, distance ):
      if self.__class__ == Transportation:
         raise NotImplementedError
      self.start = start
      self.end = end
      self.distance = distance

   def find_cost( self ):
      """Abstract method; derived classes must override"""
      raise NotImplementedError


class Walk( Transportation ):

   def __init__( self, start, end, distance ):
      Transportation.__init__( self, start, end, distance)

   def find_cost( self ):
      return 0
   
# main program
class Taxi(Transportation):
   def __init__(self, start, end, distance, initial_fare=40):
      Transportation.__init__(self, start, end, distance)
      self.initial_fare = initial_fare
   
   def find_cost(self):
      return self.initial_fare * self.distance


class Jet(Transportation):
    def __init__(self, start, end, distance, speed):
        Transportation.__init__(self, start, end, distance)
        self.speed = speed  # Speed of the jet in km/h

    def find_cost(self):
        base_rate = 50 
        speed_factor = 100 
        cost_per_km = max(base_rate - self.speed / speed_factor, base_rate / 2)
        return self.distance * cost_per_km
      
      
class Boat(Transportation):
    def __init__(self, start, end, distance, people):
        Transportation.__init__(self, start, end, distance)
        self.people = people  # Number of people on the boat
        
    def find_cost(self):
        return 100 * self.people + 10 * self.distance
      
trip = [ 
  Walk("KMITL","KMITL SCB Bank", 0.6),
  Jet("Thailand", "Japan", 10, 900),
  Taxi("Bangkok", "Pattaya", 100),
  Boat("Bangkok", "Samutprakan", 30, 25)
]

travel_cost = 0
for travel in trip:
   travel_cost += travel.find_cost()

print(f"The Cost Is: {travel_cost} Baht")