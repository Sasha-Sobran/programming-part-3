import unittest

from main import is_gas_supply_possible


class TestGasSupplyFunction(unittest.TestCase):

    def test_gas_supply_possible(self):
        cities = ['Львів', 'Стрий', 'Долина']
        storage = ['Сховище_1', 'Сховище_2']
        pipelines = [['Сховище_2', 'Стрий'], ['Долина', 'Львів'], ['Сховище_1', 'Львів']]

        result = is_gas_supply_possible(cities, storage, pipelines)

        self.assertIsInstance(result, list)

        for res in result:
            for city in res[1]:
                self.assertIn(city, cities)

            for pipe in pipelines:
                if pipe[0] == res[0]:
                    self.assertNotIn(pipe[1], res[1])

    def test_no_gas_supply_possible(self):
        cities = ['Львів', 'Стрий', 'Долина']
        storage = ['Сховище_1', 'Сховище_2']
        pipelines = [['Долина', 'Львів']]

        result = is_gas_supply_possible(cities, storage, pipelines)
        for res in result:
            self.assertEqual(len(res[1]), 3)

    def test_all_paths_accessible(self):
        cities = ['Львів', 'Стрий', 'Долина']
        storage = ['Сховище_1', 'Сховище_2']
        pipelines = [['Сховище_2', 'Стрий'], ['Стрий', 'Львів'], ['Львів', 'Долина'], ['Долина', 'Львів'],
                     ['Сховище_1', 'Львів'], ['Львів', 'Стрий']]

        result = is_gas_supply_possible(cities, storage, pipelines)

        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
