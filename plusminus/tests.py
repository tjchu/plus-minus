from django.test import SimpleTestCase


class PlusMinusCalculatorTests(SimpleTestCase):
    def test_results_page_calculates_percentage(self):
        response = self.client.post('/plusminus/results/', {
            'name': 'Jordan',
            'fga': '10',
            'fgm': '4',
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Jordan')
        self.assertContains(response, '40.00%')

    def test_results_page_rejects_impossible_shot_total(self):
        response = self.client.post('/plusminus/results/', {
            'name': 'Jordan',
            'fga': '5',
            'fgm': '7',
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'more shots than your attempts')

    def test_results_page_handles_zero_attempts(self):
        response = self.client.post('/plusminus/results/', {
            'name': 'Jordan',
            'fga': '0',
            'fgm': '0',
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '0.00%')
