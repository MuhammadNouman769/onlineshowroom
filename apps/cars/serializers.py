""" ============== IMPORTS =============== """

from decimal import Decimal
from rest_framework import serializers
from .models import Cars, ShowRoom
from .validators import alphanumeric


""" ============== ShowRoom ModelSerializer =============== """

class ShowRoomSerializer(serializers.ModelSerializer):
    """
    Serializer for ShowRoom model.
    Includes all fields of the model.
    """
    class Meta:
        model = ShowRoom
        fields = '__all__'


""" ============== Car ModelSerializer =============== """

class CarModelSerializer(serializers.ModelSerializer):
    """
    ModelSerializer for Cars model.
    Adds a computed field 'discount_price'.
    Includes validations for price and cross-field checks.
    """
    discount_price = serializers.SerializerMethodField()

    class Meta:
        model = Cars
        fields = '__all__'

    def get_discount_price(self, obj):
        """
        Returns a discounted price of 1000 subtracted from the original price.
        If price is None, returns None.
        """
        if obj.price is None:
            return None
        return obj.price - Decimal('1000.00')

    def validate_price(self, value):
        """
        Field-level validation for price.
        Price must be greater than 200.
        """
        if value <= Decimal('200.00'):
            raise serializers.ValidationError('Price must be greater than 200')
        return value

    def validate(self, data):
        """
        Object-level validation.
        Name and description cannot be identical.
        """
        if data.get('name') and data.get('description') and data['name'] == data['description']:
            raise serializers.ValidationError('Name and description cannot be the same')
        return data


""" ============== Car Serializer =============== """

class CarSerializer(serializers.Serializer):
    """
    Regular Serializer for Cars model.
    Explicitly defines all fields and validations.
    """
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField(read_only=True)
    chassisnumber = serializers.CharField(validators=[alphanumeric])
    price = serializers.DecimalField(max_digits=10, decimal_places=2)

    def create(self, validated_data):
        """
        Create a new Cars instance with validated data.
        """
        return Cars.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update an existing Cars instance with validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.chassisnumber = validated_data.get('chassisnumber', instance.chassisnumber)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance

    def validate_price(self, value):
        """
        Field-level validation for price.
        Price must be greater than 200.
        """
        if value <= Decimal('200.00'):
            raise serializers.ValidationError('Price must be greater than 200')
        return value

    def validate(self, data):
        """
        Object-level validation.
        Name and description cannot be identical.
        """
        name = data.get('name')
        description = data.get('description')
        if name and description and name == description:
            raise serializers.ValidationError('Name and description cannot be same')
        return data