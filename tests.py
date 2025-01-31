from api.models import CustomUser  # Importing the custom user model
from rest_framework.test import APITestCase
from rest_framework import status
from api.models import CustomUser

class ResponseAPITestCase(APITestCase):
    def setUp(self):
        
        self.user = CustomUser.objects.create_user(username='testuser', password='testpassword')

       
        response = self.client.post('/api/token/', {'username': 'testuser', 'password': 'testpassword'}, format='json')
        self.token = response.data['access']

    def test_get_responses(self):
       
        response = self.client.get('/api/responses/', HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_response(self):
        data = {
            'prompt': 'Test prompt',
            'response_text': 'Test response',
            'model_used': 'Test model',
            'processing_time': 1.5,
        }
        
        response = self.client.post('/api/responses/', data, format='json', HTTP_AUTHORIZATION=f'Bearer {self.token}')
        
       
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
