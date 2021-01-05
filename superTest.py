class Vehicle:
    def start(self):
        print("Start engine")
    def stop(self):
        print("Stop the egine")
class TwoWheeler(Vehicle):
    def say(self):
        super().start()
        super().stop()
        print("I am in child class")
t = TwoWheeler()
t.say()