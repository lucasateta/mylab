from XYZThings import Value, Thing, Property, Event, Action
from XYZThings.app import XYZThings

import time
import asyncio
import math
import random

class DenoiseProperty(Property):
    def __init__(self, name, value, thing=None, metadata=None):
        super().__init__(name, value, thing, metadata)

    async def get_value(self):
        return await super().get_value()
    
    async def set_value(self, value, with_action=True):
        return await super().set_value(value, with_action=with_action)

class QuickDataProperty(Property):
    def __init__(self, name, value, thing=None, metadata=None):
        super().__init__(name, value, thing, metadata)

    async def get_value(self):
        await asyncio.sleep(5000/1000)
        return await self.thing.data
        # return await super().get_value()
    
    async def set_value(self, value, with_action=True):
        return await super().set_value(value, with_action=with_action)


class MeasureAction(Action):
    title: str = "Measure"
    schema: dict = {
        "title": "Measure",
        "description": "Measure the spectrum",
        "input": {
            "type": "object",
            "required": ["average"],
            "properties": {
                "average": {
                    "type": "integer",
                    "minimum": 0,
                    "maximum": 100,
                }
            }
        }
    }

    async def perform_action(self):
        await super().perform_action()
        average = self.input["average"]
        await self.thing.average_data(average)


class Spectrometer(Thing):
    type_alias = ["Spectrometer"]
    description = "A spectrometer emulation"

    def __init__(self):
        super().__init__(
            "urn:dev:ops:my-spectrometer-1111",
            "my spectrometer",
        )
        self.href_prefix = f"/things/{self.id}"

        self.x_range = range(-100, 100)
        self.integration_time = 200
        self.settings = {
            "voltage": 5,
            "mode": "spectrum",
            "light_on": True,
            "user": {
                "name": "Squidward",
                "id": 1,
            }
        }

        denoise_property = DenoiseProperty(
            "IntegrationTime",
            Value(5000),
            metadata={
                "@type": "DenoiseProperty",
                "title": "IntegrationTime",
                "type": "integer",
                "description": "The integration time",
                "minimum": 0,
                "maximum": 20000,
                "unit": "ms",
            }
        )
        self.add_property(denoise_property)

        quickdata_property = QuickDataProperty(
            "QuickData",
            Value([]),
            metadata={
                "@type": "QuickDataProperty",
                "title": "QD",
                "type": "array",
                "items": {
                    "type": "number"
                }
            }
        )
        self.add_property(quickdata_property)

        self.add_available_action(MeasureAction)


    def make_spectrum(self, x, mu=0.0, sigma=25.0):
        x = float(x - mu) / sigma
        return (
            math.exp(-x * x / 2.0) / math.sqrt(2.0 * math.pi) / sigma + (1 / self.integration_time) * random.random()
        )
    
    @property
    async def data(self):
        await asyncio.sleep(self.integration_time / 1000)
        return [self.make_spectrum(x) for x in self.x_range]
    
    async def average_data(self, n: int):
        summed_data_ = await self.data
        summed_data = summed_data_.copy()
        for _ in range(n):
            summed_data = [summed_data[i] + e1 for i, e1 in enumerate(summed_data_)]
            await asyncio.sleep(25/1000)

        summed_data = [i / n for i in summed_data]

        return summed_data
    


spectrometer = Spectrometer()
spectrometer.href_prefix = f"/things/{spectrometer.id}"
servient = XYZThings(version='0.1.0')
servient.app.state.things.things.update({
    spectrometer.id: spectrometer
})
