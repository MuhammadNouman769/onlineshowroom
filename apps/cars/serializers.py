from decimal import Decimal
from rest_framework import serializers
from .models import Cars,ShowRoom

class ShowRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowRoom
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = '__all__'
        '''fields = ['id', 'name', 'description', 'price', 'active', 'chassisnumber']
           exclude = ('name',) '''
    def get_discounted_price(self, obj):
        discounted_price = obj.price - 1000
        return discounted_price

    def validate_price(self, value):
        if value <= Decimal('200.00'):
             raise serializers.ValidationError('Price must be greater than 200')
        return value

    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError('Name and description cannot be same')
        return data



#
# class CarSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField()
#     active = serializers.BooleanField(read_only=True)
#     chassisnumber = serializers.CharField(validators=[alphanumeric])
#     price = serializers.DecimalField(max_digits=10, decimal_places=2)
#
#     def create(self, validated_data):
#         return Cars.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.chassisnumber = validated_data.get('chassisnumber', instance.chassisnumber)
#         instance.price = validated_data.get('price', instance.price)
#         instance.save()
#         return instance
#
#     def validate_price(self, value):
#         if value <= Decimal('200.00'):
#             raise serializers.ValidationError('Price must be greater than 200')
#         return value
#
#     def validate(self, data):
#         name = data.get('name')
#         description = data.get('description')
#         if name and description and name == description:
#             raise serializers.ValidationError('Name and description cannot be same')
#         return data