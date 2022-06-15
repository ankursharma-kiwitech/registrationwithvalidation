from rest_framework import serializers, generics, permissions
from rest_framework.response import Response

import validation_message
from register.models import UserDetails, UserAddresses, UserCorrespondanceAddress

'''  authentication serializer  '''


class RegistrationSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(
        required=True, min_length=validation_message.CHAR_LIMIT_SIZE['firstname_min'],
        max_length=validation_message.CHAR_LIMIT_SIZE['firstname_max'],
        error_messages=validation_message.VALIDATION['firstname']
    )

    last_name = serializers.CharField(
        required=True, min_length=validation_message.CHAR_LIMIT_SIZE['lastname_min'],
        max_length=validation_message.CHAR_LIMIT_SIZE['lastname_max'],
        error_messages=validation_message.VALIDATION['lastname']
    )

    email = serializers.EmailField(required=True, error_messages=validation_message.VALIDATION['email'])

    username = serializers.CharField(
        min_length=validation_message.CHAR_LIMIT_SIZE['username_min'],
        max_length=validation_message.CHAR_LIMIT_SIZE['username_max'],
        error_messages=validation_message.VALIDATION['username']
    )

    password = serializers.CharField(required=True, style={'input_type': 'password'},
                                     min_length=validation_message.CHAR_LIMIT_SIZE['password_min'],
                                     max_length=validation_message.CHAR_LIMIT_SIZE['password_max'],
                                     error_messages=validation_message.VALIDATION['password'],
                                     write_only=True)

    is_active = serializers.BooleanField(default=False)

    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    def validate_email(self, email):
        existing = UserDetails.objects.filter(email=email).first()
        if existing:
            raise serializers.ValidationError("Someone with that email "
                                              "address has already registered. Was it you?")
        return email

    def validate(self, data):
        if not data.get('password') or not data.get('password2'):
            raise serializers.ValidationError("Please enter a password and "
                                              "confirm it.")
        if data.get('password') != data.get('password2'):
            raise serializers.ValidationError("Those passwords don't match.")
        return data

    def validate_username(self, username):
        existing = UserDetails.objects.filter(username=username).first()
        if existing:
            raise serializers.ValidationError("Someone with that username "
                                              "has already registered. Was it you?")
        return username

    def create(self, validated_data, password=None):
        user = UserDetails.objects.create(
            username=validated_data['username'],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"],
            password=validated_data["password"],
            is_active=validated_data["is_active"]
        )
        # user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = UserDetails
        fields = ('id', 'first_name', 'last_name', 'email', 'username', 'password', 'password2', 'is_active')
        extra_kwargs = {
            'password': {'write_only': True}
        }


class UserAddressesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddresses
        fields = ('id', 'user', 'address', 'city', 'state', 'country', 'pincode')

    user = serializers.PrimaryKeyRelatedField(queryset=UserDetails.objects.all())
    address = serializers.CharField(required=True, min_length=validation_message.CHAR_LIMIT_SIZE['address_min'],
                                    max_length=validation_message.CHAR_LIMIT_SIZE['address_max'],
                                    error_messages=validation_message.VALIDATION['address'])
    city = serializers.CharField(required=True, min_length=validation_message.CHAR_LIMIT_SIZE['city_min'],
                                 max_length=validation_message.CHAR_LIMIT_SIZE['city_max'],
                                 error_messages=validation_message.VALIDATION['city'])
    state = serializers.CharField(required=True, min_length=validation_message.CHAR_LIMIT_SIZE['state_min'],
                                  max_length=validation_message.CHAR_LIMIT_SIZE['state_max'],
                                  error_messages=validation_message.VALIDATION['state'])
    country = serializers.CharField(required=True, min_length=validation_message.CHAR_LIMIT_SIZE['country_min'],
                                    max_length=validation_message.CHAR_LIMIT_SIZE['country_max'],
                                    error_messages=validation_message.VALIDATION['country'])
    pincode = serializers.CharField(required=True, min_length=validation_message.CHAR_LIMIT_SIZE['pincode_min'],
                                    max_length=validation_message.CHAR_LIMIT_SIZE['pincode_max'],
                                    error_messages=validation_message.VALIDATION['pincode'])

    def create(self, validated_data):
        user = UserAddresses.objects.create(
            user=validated_data['user'],
            address=validated_data['address'],
            city=validated_data['city'],
            state=validated_data['state'],
            country=validated_data['country'],
            pincode=validated_data['pincode']
        )
        user.save()
        return user

    def validate_UserAddress(self, user):
        existing = UserAddresses.objects.filter(user=user).first()
        if existing:
            raise serializers.ValidationError("You have already added an address")
        return user

    def validate_address(self, address):
        if not address:
            raise serializers.ValidationError("Please enter an address")
        return address

    def validate_city(self, city):
        if not city:
            raise serializers.ValidationError("Please enter a city")
        return city

    def validate_state(self, state):
        if not state:
            raise serializers.ValidationError("Please enter a state")
        return state

    def validate_country(self, country):
        if not country:
            raise serializers.ValidationError("Please enter a country")
        return country

    def validate_pincode(self, pincode):
        if not pincode:
            raise serializers.ValidationError("Please enter a pincode")
        return pincode


class UserCorrespondanceAddressSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=UserDetails.objects.all())
    address = serializers.CharField(required=True, min_length=validation_message.CHAR_LIMIT_SIZE['address_min'],
                                    max_length=validation_message.CHAR_LIMIT_SIZE['address_max'],
                                    error_messages=validation_message.VALIDATION['address'])
    city = serializers.CharField(required=True, min_length=validation_message.CHAR_LIMIT_SIZE['city_min'],
                                 max_length=validation_message.CHAR_LIMIT_SIZE['city_max'],
                                 error_messages=validation_message.VALIDATION['city'])
    state = serializers.CharField(required=True, min_length=validation_message.CHAR_LIMIT_SIZE['state_min'],
                                  max_length=validation_message.CHAR_LIMIT_SIZE['state_max'],
                                  error_messages=validation_message.VALIDATION['state'])
    country = serializers.CharField(required=True, min_length=validation_message.CHAR_LIMIT_SIZE['country_min'],
                                    max_length=validation_message.CHAR_LIMIT_SIZE['country_max'],
                                    error_messages=validation_message.VALIDATION['country'])
    pincode = serializers.CharField(required=True, min_length=validation_message.CHAR_LIMIT_SIZE['pincode_min'],
                                    max_length=validation_message.CHAR_LIMIT_SIZE['pincode_max'],
                                    error_messages=validation_message.VALIDATION['pincode'])

    def create(self, validated_data):
        user = UserCorrespondanceAddress.objects.create(
            user=validated_data['user'],
            address=validated_data['address'],
            city=validated_data['city'],
            state=validated_data['state'],
            country=validated_data['country'],
            pincode=validated_data['pincode']
        )
        user.save()
        return user

    def validate_UserCorrespondanceAddress(self, user):
        existing = UserCorrespondanceAddress.objects.filter(user=user).first()
        if existing:
            raise serializers.ValidationError("You have already added an address")
        return user

    def validate_address(self, address):
        if not address:
            raise serializers.ValidationError("Please enter an address")
        return address

    def validate_city(self, city):
        if not city:
            raise serializers.ValidationError("Please enter a city")
        return city

    def validate_state(self, state):
        if not state:
            raise serializers.ValidationError("Please enter a state")
        return state

    def validate_country(self, country):
        if not country:
            raise serializers.ValidationError("Please enter a country")
        return country

    def validate_pincode(self, pincode):
        if not pincode:
            raise serializers.ValidationError("Please enter a pincode")
        return pincode

    class Meta:
        model = UserCorrespondanceAddress
        fields = ('id', 'user', 'address', 'city', 'state', 'country', 'pincode')











