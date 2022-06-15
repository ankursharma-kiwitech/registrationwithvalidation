CHAR_LIMIT_SIZE = {
    "email_min": 8,
    "email_max": 20,
    "firstname_min": 1,
    "firstname_max": 20,
    "lastname_min": 1,
    "lastname_max": 20,
    "username_min": 1,
    "username_max": 20,
    "password_min": 6,
    "password_max": 16,
    "phone_min": 10,
    "phone_max": 10,
    "address_min": 1,
    "address_max": 100,
    "city_min": 1,
    "city_max": 100,
    "state_min": 1,
    "state_max": 100,
    "pincode_min": 6,
    "pincode_max": 6,
    "country_min": 1,
    "country_max": 100,
    "message_min": 1,
    "message_max": 100,
    "subject_min": 1,
    "subject_max": 100,
    "name_min": 1,
    "name_max": 100,
    "description_min": 1,
    "description_max": 100,


}

VALIDATION = {
    'email': {
        "blank": "EMAIL_BLANK",
        "invalid": "EMAIL_INVALID",
        "required": "EMAIL_REQUIRED",
        "min_length": "EMAIL_MIN_LENGTH",
        "max_length": "EMAIL_MAX_LENGTH"

    },
    'username': {
        "blank": "USERNAME_BLANK",
        "invalid": "USERNAME_INVALID",
        "required": "USERNAME_REQUIRED",
        "min_length": "EMAIL_MIN_LENGTH",
        "max_length": "EMAIL_MAX_LENGTH"
    },
    'firstname': {
        "blank": "first_name cannot be empty ",
        "invalid": "invalid username ",
        "required": "username_required",
        "min_length": "EMAIL_MIN_LENGTH",
        "max_length": "EMAIL_MAX_LENGTH"
    },
    'lastname': {
        "blank": "last name cannot be empty ",
        "invalid": "invalid username ",
        "required": "username_required",
        "min_length": "EMAIL_MIN_LENGTH",
        "max_length": "EMAIL_MAX_LENGTH"
    },

    'password': {
        "blank": "password cannot be empty ",
        "invalid": "invalid username ",
        "required": "username_required",
        "min_length": "PASSWORD_MIN_LENGTH >=6",
        "max_length": "PASSWORD_MAX_LENGTH"
    },
    'address' : {
        "blank": "address cannot be empty ",
        'required': "address_required",
        "min_length": "address_min_length",
        "max_length": "address_max_length"
    },
    'city' : {
        "blank": "city cannot be empty ",
        'required': "city_required",
        "min_length": "city_min_length",
        "max_length": "city_max_length"
    },
    'state' : {
        "blank": "state cannot be empty ",
        'required': "state_required",
        "min_length": "state_min_length",
        "max_length": "state_max_length"
    },
    'pincode' : {
        "blank": "pincode cannot be empty ",
        'required': "pincode_required",
        "min_length": "pincode_min_length",
        "max_length": "pincode_max_length"
    },
    'country' : {
        "blank": "country cannot be empty ",
        'required': "country_required",
        "min_length": "country_min_length",
        "max_length": "country_max_length"
    },
    'phone' : {
        "blank": "phone cannot be empty ",
        'required': "phone_required",
        "min_length": "phone_min_length",
        "max_length": "phone_max_length"
    },


}