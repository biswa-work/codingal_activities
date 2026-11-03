from abc import ABC, abstractmethod


class SmartDevice(ABC):
    @abstractmethod
    def turn_on(self):
        pass


class SmartLight(SmartDevice):
    def turn_on(self):
        print("Smart light: lights are now ON.")


class SmartFan(SmartDevice):
    def turn_on(self):
        print("Smart fan: fan is now ON.")


class SecurityCamera:
    def check_status(self):
        print("Security camera: recording.")


class DoorLock:
    def check_status(self):
        print("Door lock: secured.")


print("Starting smart devices:")
for device in [SmartLight(), SmartFan()]:
    device.turn_on()

print("\nChecking home status:")
for device in [SecurityCamera(), DoorLock()]:
    device.check_status()
