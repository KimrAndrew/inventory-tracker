from rest_framework.test import APITestCase,RequestsClient
from django.urls import reverse
from rest_framework import status

from inventory_manager.models.Inventory_Item import InventoryItem
from ..views import Inventory_Item_Detail, Inventory_Item_List


#TODO
# - Test for Delete Inventory Item

class InventoryItemTestCase(APITestCase):
    def setUp(self) -> None:
        data = {
            'name': 'Macbook',
            'description': 'laptop',
            'quantity': 350,
            'price': 1200
        }
        self.client.post('/inventory_manager/v1/inventory_items/',data)

        data = {
            'name': 'Nike Airforce Ones',
            'description': 'Color: Black',
            'quantity': 350,
            'price': 60
        }
        self.client.post('/inventory_manager/v1/inventory_items/',data)

    def test_create_new_inventory_item(self):

        data = {
            "name":"Gucci Slides",
            "description": "The coolest slides in town",
            "quantity": 200,
            "price": 600
        }

        response = self.client.post("/inventory_manager/v1/inventory_items/",data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_inventory_item_list(self):
        response = self.client.get('/inventory_manager/v1/inventory_items/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_inventory_item_detail(self):
        response = self.client.get(reverse("inventory_item_detail", kwargs={"pk": 2}))
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data['name'],"Nike Airforce Ones")

    def test_put_inventory_item(self):

        data = {
            'name': 'Nike Airforce Ones',
            'description': 'Color: Black',
            'quantity': 349,
            'price': 60
        }
        response = self.client.put(reverse("inventory_item_detail", kwargs={"pk": 2}),data)
        self.assertEqual(response.data["name"], "Nike Airforce Ones")
        self.assertEqual(response.data["quantity"], 349)

    def test_patch_inventory_item(self):
        data = {
            "description": 'Color: White'
        }
        response = self.client.patch(reverse("inventory_item_detail", kwargs={"pk": 2}),data)
        self.assertEqual(response.data["name"], "Nike Airforce Ones")
        self.assertEqual(response.data["description"], "Color: White")

    def test_delete_inventory_item(self):
        response = self.client.delete(reverse("inventory_item_detail", kwargs={"pk": 2}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        