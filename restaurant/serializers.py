from rest_framework import serializers
from .models import Booking, Menu, Order, OrderItem, Category

class Bookingserializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['first_name', 'reservations_date', 'reservations_slot']

class MenuBookingserializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['name', 'price', 'menu_item_description']


class CategorySerializer (serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'slug']


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['order', 'menuitem', 'quantity', 'price']


class OrderSerializer(serializers.ModelSerializer):
    orderitem = OrderItemSerializer(many=True, read_only=True, source='order')

    class Meta:
        model = Order
        fields = ['id', 'user', 'delivery_crew',
                  'status', 'date', 'total', 'orderitem']
